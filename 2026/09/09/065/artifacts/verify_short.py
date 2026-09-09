#!/usr/bin/env python3
"""Verifier for the (5e8,5.2e8] Coins short-window census.
Checks (stdlib only):
 1. The three window bitmaps exist, have the right byte length, and are byte-identical.
 2. sha256 matches the logged value a3e7646a....
 3. Every marked value is admissible mod 24 (subset of {0,4,12,13,16,21}); no violations.
 4. Recomputes E_short from bitmap A + residue table; checks E file has exactly those
    349 entries in order, least 500004300, greatest 519931204.
 5. Checks admissible totals: 5000001 admissible, 4999652 present, 349 absent.
 6. Verifies the witness chain file: every frame satisfies the Descartes equation
    (a+b+c+d)^2 = 2(a^2+b^2+c^2+d^2), consecutive frames are single Vieta moves,
    and the birth quadruple contains 500000004 and satisfies Descartes.
"""
import hashlib, os, re
BASE = os.path.dirname(os.path.abspath(__file__))
LO, BOUND = 500_000_000, 520_000_000
RES = {0, 4, 12, 13, 16, 21}
EXPECT_SHA = "a3e7646a0a7a5230011c0f98b962f210d2dc5bc64df65a3192c4ba52f6cc12b6"
def fail(m):
    print("VERIFY_FAIL:", m); raise SystemExit(1)
paths = ["bitmap_shortA_5e8_52e8.bin", "bitmap_shortB_5e8_52e8.bin", "bitmap_shortC_5e8_52e8.bin"]
datas = []
for p in paths:
    fp = os.path.join(BASE, p)
    if not os.path.exists(fp): fail("missing " + p)
    d = open(fp, "rb").read()
    datas.append(d)
nbytes = (BOUND - LO + 7) // 8
for p, d in zip(paths, datas):
    if len(d) != nbytes: fail("%s length %d != %d" % (p, len(d), nbytes))
if not (datas[0] == datas[1] == datas[2]): fail("bitmaps differ")
sha = hashlib.sha256(datas[0]).hexdigest()
if sha != EXPECT_SHA: fail("sha mismatch " + sha)
print("bitmaps: 3 files, %d bytes each, byte-identical, sha256 OK" % nbytes)
data = datas[0]
def present(v):
    i = v - LO - 1
    return (data[i >> 3] >> (i & 7)) & 1
pc = 0; viol = 0
for bi, b in enumerate(data):
    bb = b
    while bb:
        j = (bb & -bb).bit_length() - 1
        bb &= bb - 1
        v = LO + 1 + (bi << 3) + j
        if v > BOUND: break
        pc += 1
        if v % 24 not in RES:
            viol += 1
            if viol <= 5: print("violation:", v)
if viol: fail("%d residue violations" % viol)
print("residue audit: %d marked values, all in {0,4,12,13,16,21}" % pc)
E = [v for v in range(LO + 1, BOUND + 1) if v % 24 in RES and not present(v)]
adm_total = sum(1 for v in range(LO + 1, BOUND + 1) if v % 24 in RES)
raw = open(os.path.join(BASE, "E_short_5e8_52e8.txt")).read().split()
Efile = list(map(int, raw))
if Efile != E: fail("E file mismatch (len file=%d recomputed=%d)" % (len(Efile), len(E)))
if adm_total != 5000001: fail("adm_total=%d" % adm_total)
if pc != 4999652: fail("present=%d" % pc)
if len(E) != 349: fail("E size=%d" % len(E))
if E[0] != 500004300 or E[-1] != 519931204: fail("E endpoints %d %d" % (E[0], E[-1]))
print("census: admissible=%d present=%d E=%d least=%d greatest=%d" % (adm_total, pc, len(E), E[0], E[-1]))
txt = open(os.path.join(BASE, "chain_present_500000004.txt")).read()
rows = []
for line in txt.splitlines():
    m = re.match(r"\s*\d+:\s*\((-?\d+),(-?\d+),(-?\d+),(-?\d+)\)\s*sum=(-?\d+)", line)
    if m:
        q = tuple(map(int, m.groups()[:4])); s = int(m.group(5))
        rows.append((q, s))
if not rows: fail("empty chain")
def desc(q):
    s = sum(q); return s * s == 2 * sum(x * x for x in q)
for q, s in rows:
    if not desc(q) or s != sum(q): fail("chain descartes fail %r" % (q,))
for (q0, _), (q1, _) in zip(rows, rows[1:]):
    d = [i for i in range(4) if q0[i] != q1[i]]
    if len(d) != 1: fail("chain non-single move")
    i = d[0]; rest = sum(q0) - q0[i]
    if q1[i] != 2 * rest - q0[i]: fail("chain non-vieta move")
m = re.search(r"birth_quad:\s*\((-?\d+),(-?\d+),(-?\d+),(-?\d+)\)", txt)
if not m: fail("no birth_quad")
bq = tuple(map(int, m.groups()))
if not desc(bq) or 500000004 not in bq: fail("bad birth quad %r" % (bq,))
print("chain: %d frames, all Descartes + Vieta-adjacent, birth quad %r OK" % (len(rows), bq))
print("VERIFY_OK")
