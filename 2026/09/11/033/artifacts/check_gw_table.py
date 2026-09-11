"""MPS Appendix A.3 exception rule-out, class by class (auditor repair item 3).

MPS reference (Markwig-Payne-Shaw, arXiv 2207.01305):
- Thm A.2: shapes (A),(B),(C),(D),(E),(F),(G),(H),(Na),(Oa),(Pa),(Qa),(Qc),
  (Ra),(Sa),(IIa),(IIb),(T),(Ua),(Uc),(Va),(W),(YcI),(YaII),(CCaII),(EE)
  [plus EE/Y subcases spelled out in the proof] contribute 2H per class.
- Thm 1.7 (=Thm 4.23 compact case): compact shapes (A)-(H),(W) give 2H.
- App. A.3 exceptions (NOT 2H in general):
    E1 = {(Nb),(Ob),(Oc),(Pb),(Qb),(Rb),(Rc),(Sb),(Ub),(Vb),(IIc),
          (YbI),(YbII),(CCb)} with GW = <1>+<1>+H (degree 4);
    E2 = {(YaI),(YaIII),(BBa),(BBb),(CCaI)} with initial-dependent values
         (table: monomial Qtypes + <2> + H terms; (BBb) = four <1>s).
  (Degrees are still 4 per class, so the Pluecker degree count cannot detect
  the difference -- the shape check below is load-bearing for v_GW.)

This script reads output/artifacts/shapes.json (7 classes, shapes 3xA/3xB/1xC
resolved by the extension's own hyperplane rules) and checks, for each row:
  (i)   shape in {A,B,C} subset of the Thm A.2 2H-list;
  (ii)  shape NOT in E1 union E2;
  (iii) compact-shape cover (Thm 1.7) also applies;
hence v_GW = (2H)x7 = 14H of degree 28 with no initial-dependent correction.
Writes output/artifacts/gw_table.json (7-row table) and prints it.
"""
import json

A2_2H = {"A","B","C","D","E","F","G","H","Na","Oa","Pa","Qa","Qc","Ra","Sa",
         "IIa","IIb","T","Ua","Uc","Va","W","YcI","YaII","CCaII","EE"}
E1 = {"Nb","Ob","Oc","Pb","Qb","Rb","Rc","Sb","Ub","Vb","IIc",
      "YbI","YbII","CCb"}
E2 = {"YaI","YaIII","BBa","BBb","CCaI"}
EXC = E1 | E2
COMPACT = {"A","B","C","D","E","F","G","H","W"}

sh = json.load(open('output/artifacts/shapes.json'))['shapes']
assert len(sh) == 7, len(sh)

rows = []
for n, s in enumerate(sh, start=1):
    shape, mtype = s['shape'], s['type']
    tris = [sorted(t) for t in s['triangles']]
    in_a2 = shape in A2_2H
    is_exc = shape in EXC
    compact = shape in COMPACT
    if shape == "A":
        why = "Thm A.2 shape (A)->2H (Lemma 4.18 pairing); compact (Thm 1.7)"
    elif shape == "B":
        why = "Thm A.2 shape (B)->2H (Lemma 4.18 pairing); compact (Thm 1.7)"
    elif shape == "C":
        why = "Thm A.2 shape (C)->2H (edge-interior tangencies, as (A)); compact (Thm 1.7)"
    else:
        why = "UNEXPECTED SHAPE -- needs individual A.3 analysis"
    gw = "2H" if (in_a2 and not is_exc) else "NEEDS-CORRECTION"
    rows.append({"class": f"B*_{n}", "motif": mtype, "shape": shape,
                 "triangles": tris, "MPS_case": f"Thm A.2 ({shape})",
                 "in_A2_2H_list": in_a2, "in_A3_exception_list": is_exc,
                 "compact_Thm17_cover": compact, "GW": gw, "why": why})
    assert in_a2, (n, shape)
    assert not is_exc, (n, shape)
    assert compact, (n, shape)
    assert gw == "2H", (n, shape)

assert sorted(s['shape'] for s in sh) == ['A','A','A','B','B','B','C']
assert all(r['GW'] == '2H' for r in rows)
json.dump(rows, open('output/artifacts/gw_table.json', 'w'), indent=1)

print(f"{'class':8s} {'motif':8s} {'shape':6s} {'MPS case':14s} {'A.3?':6s} {'GW':4s}  why")
for r in rows:
    print(f"{r['class']:8s} {r['motif']:8s} {r['shape']:6s} {r['MPS_case']:14s} "
          f"{str(r['in_A3_exception_list']):6s} {r['GW']:4s}  {r['why']}")
print("GW_TABLE_OK: 7/7 classes 2H, none exceptional; v_GW=14H deg 28")
