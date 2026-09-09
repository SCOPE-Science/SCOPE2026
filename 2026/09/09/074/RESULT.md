# Unitarity exclusion for the rank-6 Grothendieck ring of NsdGOL6 orbit 17 (D^2 = 9)

## Context
Rank-6 modular data are classified up to modular data (Ng–Rowell–Wang–Wen,
arXiv:2203.14829; Ng–Rowell–Wen, arXiv:2308.09670), but the tables leave
potential unitary data whose categorical realization is explicitly open
(2308.09670 abstract). The low-rank program advances one fixed Grothendieck
ring at a time (Ocneanu rigidity makes each pentagon–hexagon check finite).
Green (arXiv:1908.07128) decides only the Galois orbit
<(012)(345)> (non-self-dual, two surviving families); other rank-6 orbits
are left open.

## Definitions
- Source: `NsdGOL6.g` ancillary to arXiv:2308.09670 (192 entries, 20 Galois
  orbits), archived as `output/artifacts/NsdGOL6.g`.
- Cell: Galois orbit 17, entries (17,1) = 6_{16/3,9.}^{9,746} (irep 25) and
  (17,2) = 6_{8/3,9.}^{9,711} (irep 25); S excerpt archived as
  `output/artifacts/SsL6lng_orbit17.txt`.
- Fusion ring R17: the filed `Nij_k` shared by (17,1) and (17,2); self-dual
  (every object its own dual, N[i][j][0] = delta_{ij}).
- Dimensions: filed `d = [1, cs(9,2), 1, cs(9,1), -1, cs(9,4)]` where
  `cs(9,k) = c_9^k = 2cos(2πk/9)`; numerically [1, 0.347, 1, 1.532, -1, -1.879].
- Spins: (17,1) s = [0,1/9,2/3,4/9,1/3,7/9]; (17,2) s = [0,8/9,1/3,5/9,2/3,2/9].
- S-matrix (symmetric, S_00 = 1): S_0· = (1, c_9^2, 1, c_9^1, -1, c_9^4);
  S_11=S_22=S_33=S_44=S_55=1; S_12=c_9^1, S_13=1, S_14=-c_9^4, S_15=1;
  S_23=c_9^4, S_24=-1, S_25=c_9^2; S_34=-c_9^2, S_35=1; S_45=-c_9^1.
- Exact field: K = Q(u), u = 2cos(2π/9), minimal polynomial u^3-3u+1,
  basis {1,u,u^2}; C1=u=c_9^1, C2=u^2-2=c_9^2, C4=2-u-u^2=c_9^4.

## Result
For the fixed rank-6 Grothendieck ring R17 of NsdGOL6 Galois orbit 17
(entries (17,1) and (17,2), irep 25, D^2 = 9), no unitary modular tensor
category realizes its potential modular datum. Every S-matrix candidate on
this ring forces a negative (d_4 = -1 exactly) and non-Frobenius–Perron
(d_1 = u^2-2 < 1 ≤ FPdim_1 exactly) categorical dimension, with Galois label
σ_8 ∈ Gal(Q(ζ_9)/Q) fixing S and exchanging the two T-vectors.

## Proof / evidence
Exact stdlib-only replay: `python3 output/artifacts/verify.py` → `VERIFY_OK`.
1. Candidate completeness: parsing archived NsdGOL6.g (192 entries), a
   36-distinct-ring census places the exact R17 fusion ring at precisely
   (17,1) and (17,2); both file the same d vector above. No other ring is
   isomorphic under a 0-fixing relabeling.
2. Genuine candidate: exact arithmetic in Q(u) gives S^2 = 9I (S real
   symmetric, so SS† = 9I) and Σ d_a^2 = 9; the exact Verlinde formula
   reproduces all 216 filed integers Nij_k.
3. Negative dimension: first row d = (1, C2, 1, C1, -1, C4) has d_4 = -1 < 0
   exactly; unitary MTC quantum (= Frobenius–Perron) dimensions are all > 0.
4. Non-FP: filed fusion matrix N_1 has exact row sums [1,3,3,2,4,2], so its
   Perron root FPdim_1 ≥ 1 (Horn–Johnson, Matrix Analysis, Thm 8.1.22 /
   Collatz–Wielandt). But d_1 = C2 = u^2-2 < 1: u^2 > 2 (since
   C2 = 2cos(4π/9) > 0 as 4π/9 < π/2), so u > 0; if u^2 ≥ 3 then u^3 ≥ 3u,
   contradicting u^3 = 3u-1 < 3u. Hence d ≠ FPdim vector.
5. Galois closure: σ_8: ζ_9 ↦ ζ_9^8 (order 2, complex conjugation, fixing the
   real subfield hence S) sends spin numerators [0,1,6,4,3,7] ↦ [0,8,3,5,6,2]
   entrywise, exchanging the two T-vectors; the orbit is Galois-closed of
   size 2.
This is not Green 1908.07128: Green assumes Gal = ⟨(012)(345)⟩
(non-self-dual) with two surviving families (Theorem 3.5); R17 is self-dual
with real D^2 = 9 data in Q(ζ_9)^+ (irep 25), a different orbit.

## Limitations
- Decides unitary realizability only; non-unitary MTC realization of R17 is
  left open (the candidates are admissible modular data).
- Candidate completeness is relative to the published full rank-6
  classification (2203.14829 + 2308.09670 v2, 192 entries); it inherits their
  completeness claim (Ocneanu rigidity + SL(2,Z)-representation pipeline).
- The SsL6lng table flags these entries 'Not pseudo-unitary' as an unproved
  label; the new contribution is the exact replayable ring-level certificate
  with cited S entries and Galois labels, not the flag itself.
- One analytic one-liner (cos(4π/9) > 0 from cosine monotonicity on [0,π])
  sits outside the Fraction computation and is proved in DRAFT §4.

## Reproducibility
`python3 output/artifacts/verify.py` (same directory as `NsdGOL6.g`,
stdlib only) → `VERIFY_OK` (C1 ring census + filed d; C2 exact S^2 = 9I,
D^2 = 9; C3 exact Verlinde = 216 filed integers; C4 d_4 = -1; C5 row-sum
bound vs u^2 < 3; C6 σ_8 T-swap). Live NsdGOL6.g downloaded from
https://arxiv.org/src/2308.09670v2/anc/NsdGOL6.g is hash-identical
(sha256 eeea55e0ae75982b0afcf7d8e936d7cb7d4adae7a42096e719d13b30974fab0b).

## References
- S.-H. Ng, E. C. Rowell, X.-G. Wen, Classification of modular data up to
  rank 12, arXiv:2308.09670.
- S.-H. Ng, E. C. Rowell, Z. Wang, X.-G. Wen, Reconstruction of modular data
  from SL_2(Z) representations, arXiv:2203.14829.
- D. Green, Classification of Rank 6 Modular Categories with Galois Group
  ⟨(012)(345)⟩, arXiv:1908.07128.
- R. Horn, C. Johnson, Matrix Analysis, Thm 8.1.22 (row-sum Perron bound).
