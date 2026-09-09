# Vacuous single-cell shadings of 1324/2143 and exact mesh-avoidance census to n=10

## Context

Wilf-equivalence of mesh patterns is classified for length 2 (Hilmarsson et al.:
1024 patterns to at most 65, then 56 classes, conjectured 46; closed at 46
Wilf-classes by Zhang–Zhao 2026) and for length-2 meshes inside 231-avoiding
classes (Tannock–Ulfarsson). Length-4 mesh Wilf-classes are open. Classical
length-4 growth constants already separate (Albert et al.: Wilf–Stanley limit
of 4231-avoiders >= 9.35, refuting Arratia's (k-1)^2 bound). The minimal
non-classical decorations — single shaded cells over the representative bases
1324 (hard classical growth) and 2143 (separable-type, Wilf-equivalent to 1234)
— are the canonical first frontier beyond classical patterns.

## Definitions

Work in 0-based values. Classical bases: 1324 = [0,2,1,3], 2143 = [1,0,3,2].
For an occurrence at indices I=(i1<i2<i3<i4) with values (a,b,c,d) and
S = sorted values, mesh cell (cc,cr) in {0,..,4}^2 is the open rectangle
x in (xlo,xhi), y in (ylo,yhi) with xlo=-1 if cc=0 else I[cc-1],
xhi=n if cc=4 else I[cc], ylo=-1 if cr=0 else S[cr-1], yhi=n if cr=4 else
S[cr]. A mesh occurrence is a classical occurrence whose shaded-cell
rectangle contains no point of the permutation graph. Occurrence points lie
on the rectangle boundary (each has x-coordinate one of the I[k], none
strictly between consecutive I's for the relevant column gaps), hence are
never strictly inside their own cell.

Window W (labels M0..M7):

| label | base | shaded cell | gloss |
|---|---|---|---|
| M0 | 1324 | (0,0) | corner, x<i1, y<min |
| M1 | 1324 | (0,1) | edge, x<i1, a<y<c |
| M2 | 1324 | (1,1) | near-corner, i1<x<i2, a<y<c |
| M3 | 1324 | (2,2) | central, i2<x<i3, c<y<b |
| M4 | 2143 | (0,0) | corner, x<i1, y<b |
| M5 | 2143 | (0,1) | edge, x<i1, b<y<a |
| M6 | 2143 | (1,1) | near-corner, i1<x<i2, b<y<a |
| M7 | 2143 | (2,2) | central, i2<x<i3, a<y<d |

Here a,b,c,d denote the values at i1,i2,i3,i4. `dihedral.py` certifies the 8
meshes are pairwise inequivalent under reverse/complement/inverse (orbit sizes
M0:4, M1:8, M2:4, M3:2, M4:4, M5:8, M6:4, M7:2) and that the classical orbits
of 1324 and 2143 are disjoint. Av_n(m) = number of permutations of length n
avoiding mesh m; B0=Av(1324), B1=Av(2143).

## Result

**Theorem (vacuous shadings, all n).** M0, M1, M2, M3 each coincide with
classical 1324 for ALL n, and M5, M6 each coincide with classical 2143 for
ALL n: every classical occurrence contains an unshaded occurrence. In
particular the dihedrally-inequivalent pairs — all 6 pairs among
{M0,M1,M2,M3} (headline: corner-shaded M0 vs centrally-shaded M3) and
(M5,M6) — are Wilf-equivalent. Only M4 and M7 are genuinely restrictive.

**Theorem (dual-certified census, n=1..10).** Two independent brute-force
routes agree on all 80 cells. Exact avoidance numbers:

| m | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| M0 | 1 | 2 | 6 | 23 | 103 | 513 | 2762 | 15793 | 94776 | 591950 |
| M1 | 1 | 2 | 6 | 23 | 103 | 513 | 2762 | 15793 | 94776 | 591950 |
| M2 | 1 | 2 | 6 | 23 | 103 | 513 | 2762 | 15793 | 94776 | 591950 |
| M3 | 1 | 2 | 6 | 23 | 103 | 513 | 2762 | 15793 | 94776 | 591950 |
| M4 | 1 | 2 | 6 | 23 | 104 | 534 | 3060 | 19445 | 136976 | 1072110 |
| M5 | 1 | 2 | 6 | 23 | 103 | 513 | 2761 | 15767 | 94359 | 586590 |
| M6 | 1 | 2 | 6 | 23 | 103 | 513 | 2761 | 15767 | 94359 | 586590 |
| M7 | 1 | 2 | 6 | 23 | 104 | 530 | 2958 | 17734 | 112657 | 750726 |

Classical rows: B0 = 1,2,6,23,103,513,2762,15793,94776,591950 (matches OEIS
A061552 for 1324); B1 = 1,2,6,23,103,513,2761,15767,94359,586590 (matches
A005802 for 1234, consistent with 2143~1234).

**Corollary (finite-window separation).** max Av_10 / min Av_10 =
1072110/586590 = 1.827699 >= 1.5, attained at M4 vs M5/M6. This is a
finite-window ratio, NOT an asymptotic growth-rate theorem.

Distinguishing witnesses in S5: M4 avoids (0,2,1,4,3) — its unique classical
2143-occurrence at indices 1-4 with values 2,1,4,3 has its corner region
x<1,y<1 occupied by (0,0), so the sole occurrence is shaded (hence
mesh-avoiding, giving Av_5=104>103). M7 avoids (1,0,2,4,3) — its unique
classical occurrence at indices 0,1,3,4 with values 1,0,4,3 has central
region 1<x<3,0<y<3 containing (2,2), so the sole occurrence is shaded
(Av_5=104>103).

## Proof / evidence

*Vacuity lemma (proof).* Minimal-counterexample + replacement,
machine-checked over all relative orders by `vacuity.py` (VACUITY_OK). For
each case the value-order of the 5 involved entries is forced (exactly one
constrained relative order) and the replacement tuple keeps the base pattern:
- M0 (1324,(0,0), region v<min): minimal-i1 occurrence; region point (j,v)
  gives (v,b,c,d)=1324 starting at j<i1, contradiction.
- M1 (1324,(0,1), region a<v<c): minimal-i1; same replacement, contradiction.
- M2 (1324,(1,1), region a<v<c): minimal-i2 then maximal-i1; region point
  gives (v,b,c,d)=1324 with same i2 but larger first index j in (i1,i2).
- M3 (1324,(2,2), region c<v<b): minimal-i3; region point gives (a,b,v,d)=
  1324 with third index j in (i2,i3), j<i3.
- M5 (2143,(0,1), region b<v<a): minimal-i1; (v,b,c,d)=2143.
- M6 (2143,(1,1), region b<v<a): minimal-i2 then maximal-i1; same.
The script enumerates all 5!=120 relative orders of (a,b,c,d,v) per case and
asserts the replacement pattern equals the base; it simultaneously certifies
M4/M7 replacements FAIL (yield (0,1,3,2) and (1,0,2,3)), consistent with
genuineness.

*Census (experimental evidence, dual-certified).* Route A: recursive
prefix-DFS, rank-counting classical test, half-open interval shading scan
with occurrence skip, quadruples ascending. Route B: lexicographic
next_permutation, chained-comparison test (a<c<b<d for 1324; b<a<d<c for
2143), descending bubble sort, full rectangle point count, quadruples
descending. `verify.py` gives VERIFY_OK: 80/80 agreement, collapse-pair scan
exactly the 6 among M0-M3 plus M5-M6, mesh>=classical sanity, classical rows
identical across routes. A third stdlib Python point-set implementation
reproduces all rows to n<=7 plus spot n=8 cells. Occurrence buffer 300 >
C(10,4)=210; counts fit in long.

## Limitations

1. Route B is a second independent brute force, NOT the transfer-matrix /
   insertion-encoding replay named in the admission audit plan; certification
   is by implementation independence, weaker than method independence.
2. No asymptotic growth-rate separation is proved; the 1.827699 ratio is a
   finite-window (n=10) datum only. No nontrivial exponential upper bounds
   (only Av_n <= n!).
3. Completeness of W as the full dihedral-reduced single-cell set is assumed
   from the frozen window, not certified (only pairwise inequivalence of the
   8 listed meshes is certified). The headline collapse does not require it.
4. OEIS anchors are embedded constants in `verify.py`, not live OEIS fetches;
   primary certification is dual-route agreement.

## Reproducibility

All files under `output/artifacts/` (stdlib except C compiler):
`python3 output/artifacts/dihedral.py` -> DIHEDRAL_OK;
`python3 output/artifacts/vacuity.py` -> VACUITY_OK;
`gcc -O2 -o enumA output/artifacts/enumA.c` (same for B),
`./enumA > routeA.log`, `./enumB > routeB.log`;
`python3 output/artifacts/verify.py` -> VERIFY_OK (80/80, ratio 1.827699).

## References

- Hilmarsson et al., Wilf-classification of mesh patterns of short length,
  arXiv:1409.3165 (length-2 only).
- Tannock–Ulfarsson, Equivalence classes of mesh patterns with a dominating
  pattern, arXiv:1704.07104 (length-2 under dominating constraint).
- Albert et al., On the Wilf-Stanley limit of 4231-avoiding permutations,
  arXiv:math/0502504 (classical 4231 >= 9.35).
- Kitaev–Liese, Harmonic numbers, Catalan's triangle and mesh patterns,
  arXiv:1209.6423 (eight small-length meshes; precedent for 8-pattern unit).
