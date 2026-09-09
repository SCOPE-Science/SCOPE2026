# No `<13>`-invariant (157,13,1) difference set in C157: 325-set orbit-union census with code-transfer exclusion

## Context

Existence of a projective plane of order 12 is equivalently existence of a
symmetric 2-(157,13,1) design, equivalently (in the cyclic case) a planar
(157,13,1) difference set in C157 = Z_157 (v = 12^2+12+1 = 157, k = 12+1 = 13,
lambda = 1). The Bruck-Ryser-Chowla conditions are soluble here (n = 12 is
0 mod 4; v = 157 is odd with x^2 = 12y^2+z^2 soluble), and
Delsarte/character-table methods are recorded as non-decisive for order 12
(Matolcsi-Weiner arXiv:1801.09480, arXiv:1709.06149). The order-10 cell was
closed by Lam-Thiel-Swiercz, making order 12 the canonical next open cell.
This record closes the most symmetric fixed-multiplier subcase and transfers
it to coding theory. Context statements (BRC/Delsarte gap, order-10 closure)
are cited from the admitted record, not re-proved here.

## Definitions

- C157 = Z_157 (157 prime); multiplier candidate t = 13 (note t = k).
- ord_157(13) = 6: 13^6 = 1 mod 157, 13^3 = -1 mod 157, powers 1..5 != 1.
- `<13>`-orbits under x -> 13x: {0} plus 26 sextuples (orbit sizes forced:
  13^2 = 12 fixes only 0 since 157 is prime; 13^3 = -1 fixes only 0; hence
  all 156 nonzero elements lie in 6-orbits, 156/6 = 26).
- Canonical sextuple representatives (least elements):
  [1,2,3,4,5,6,7,8,9,10,11,15,16,17,18,19,20,21,22,29,30,31,32,33,43,44].
- Normalized `<13>`-fixed 13-set: S = {0} U Oi U Oj for distinct sextuple
  orbits Oi, Oj (1+6+6 = 13 is the only orbit-size combination summing to 13;
  13 mod 6 = 1 forces inclusion of {0}). Count: C(26,2) = 325. Up to
  translation (normalization 0 in S), these are ALL `<13>`-fixed 13-sets.
- Planar (157,13,1) difference test: S (k = 13) is a difference set iff its
  156 ordered differences a-b (a != b) cover every nonzero residue of Z_157
  exactly once; equivalently |S cap (S+g)| = 1 for all g != 0.
- Orbit code: 157x157 binary circulant incidence matrix from the 157
  translates of S; orbit-code enumerator question via the MacWilliams
  identities.

## Result

1. **Census (0 survivors).** All 325 normalized sets {0} U Oi U Oj fail the
   planar difference test. Survivor list is empty (SURVIVORS.txt:
   `survivors=0`). Per-set exact spectra are logged in census.json:
   distinct-nonzero distribution {42:26, 48:26, 60:78, 66:26, 72:169}
   (best set covers only 72/156 residues, min 84 missing);
   max-multiplicity distribution {4:273, 6:26, 8:26} (minimum over census
   is 4; no set approaches multiplicity <= 1).
2. **Independent replay.** A second stdlib-only script re-decides all 325
   sets via translation intersection numbers (set-operation path, not
   differences) and cross-checks max_mult/missing per set: 0 mismatches;
   REPLAY_SURVIVORS.txt byte-identical to SURVIVORS.txt
   (sha256 2bf46ccbbe671c5e8393406a1c548d41dcae193f309dd62515bef6980234f1a7).
3. **Code transfer.** All 325 orbit-type circulants have F2-rank exactly 157
   (bit-integer elimination, cross-checked by gcd(s(x),x^157+1) = 1 for all
   325, i.e. rank = 157 - deg(gcd)); every orbit code is the full space
   F2^157 with enumerator (1+z)^157 (158/158 exact integer MacWilliams/
   Krawtchouk identities verified; factor lattice x^157+1 = (x+1)f1f2f3
   with deg fi = 52, using ord_157(2) = 52). Every putative symmetric
   2-(157,13,1) incidence matrix satisfies MM^T = 12I+J over Z, so
   det(M)^2 = 12^156*169 and |det M| = 12^78*13 (86-digit even integer),
   hence is singular over F2: every design code is a proper subcode
   (dim <= 156). Therefore no `<13>`-fixed 13-set can be a block of a
   symmetric 2-(157,13,1): the enumerator class required by a
   `<13>`-fixed incidence structure is empty (excluded).
4. **Controls.** The same difference test passes the Fano (7,3,1) set
   {0,1,3} and the classical (13,4,1) set {0,1,3,9}, and fails the
   interval 13-set in Z_157.

## Proof / evidence

- Orbit claim: verified by exact computation (27 orbits, sizes 1+26x6,
  partitioning Z_157, closed under x -> 13x) plus the prime-field fixed-point
  argument above; both scripts assert it.
- Census claim: exact integer ordered-difference tally on each of the 325
  sets (156 ordered pairs each, ~50k modular operations); independently
  re-decided via intersection numbers with full spectral cross-check.
- Rank claim: two independent exact paths (F2 bit-elimination rank 157 for
  all 325; polynomial-gcd cross-check = 1 for all 325).
- MacWilliams pair: exact integer arithmetic over all 158 Krawtchouk
  identities for the binomial enumerator <-> trivial dual.
- Determinant parity: eigenvalues of 12I+J are 169 (x1) and 12 (x156);
  det(M)^2 = 12^156*169; |det M| = 12^78*13 is even, so every design
  incidence matrix drops rank over F2. Combined with full-rank orbit codes,
  the exclusion follows. This step uses only the design equations plus the
  rank census, independent of the difference spectra.
- Auditor independently re-ran the full 325-set census (frozenset+Counter
  path), the polynomial-gcd rank cross-check, ord_157(2) = 52, controls, and
  determinant parity: all pass; macwilliams.py re-executed to ALL_PASS.

## Limitations

- Fixed-`<13>`-symmetry fragment only: says nothing about (157,13,1)
  difference sets or designs without `<13>` symmetry.
- Does not resolve existence of a projective plane of order 12.
- "Multiplier" is used in the orbit-stabilizer sense (x -> 13x permutes S);
  no claim that 13 is a multiplier of a full design in Hall's sense beyond
  gcd(13,157) = 1 eligibility.
- BRC indecisiveness / Delsarte-gap context is cited, not re-proved.

## Reproducibility

Stdlib-only Python 3; seconds-scale (rank census dominates, ~1 min):

```
python3 census.py       # orbits.json, census.json, SURVIVORS.txt (survivors=0)
python3 replay.py       # REPLAY_OK, exit 0, byte-identical survivor files
python3 macwilliams.py  # ALL_PASS, exit 0 (Parts A-E), macwilliams.json
```

SHA-256: census.json b178edba0c01bb580581b86eb905b51300454180452e599ddf7c080297b23e16;
SURVIVORS.txt / REPLAY_SURVIVORS.txt 2bf46ccbbe671c5e8393406a1c548d41dcae193f309dd62515bef6980234f1a7;
orbits.json 5c2101653b5fbe6539601ad17b530a513c6ea594c4a09ddbc813f8d9dcbc2467.

## References

- Lam, Thiel, Swiercz, "The non-existence of finite projective planes of
  order 10", Canad. J. Math. 1989. https://doi.org/10.4153/CJM-1989-041-8
- Matolcsi, Weiner, "Finite projective planes and the Delsarte LP-bound".
  https://arxiv.org/abs/1801.09480
- Matolcsi, Weiner, "Character tables and the problem of existence of finite
  projective planes". https://arxiv.org/abs/1709.06149
- Francetic, Herke, Horsley, "More nonexistence results for symmetric pair
  coverings". https://arxiv.org/abs/1505.05949
- Miller, "Forbidden multipliers in abelian difference sets".
  https://arxiv.org/abs/2511.10231
- Perrott, "Existence of Projective Planes". https://arxiv.org/abs/1603.05333
- Bruck-Ryser-Chowla Theorem (MathWorld).
  https://mathworld.wolfram.com/Bruck-Ryser-ChowlaTheorem.html
- arXiv API query all:"157,13,1" — 0 results (2026-09-09).
  https://export.arxiv.org/api/query?search_query=all:%22157,13,1%22&start=0&max_results=5
