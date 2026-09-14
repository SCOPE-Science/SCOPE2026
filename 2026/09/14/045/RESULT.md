# Realizability of Jordan degree types for T=(1,3,6^5,3,1): 11 two-prime-verified potentials in 7 Table-6 rows

## Context

Let K be a field, R=K[x,y,z], S=K[X,Y,Z] with contraction action. For F in S_j,
A=R/Ann(F) is Artinian Gorenstein of socle degree j; every such algebra arises
this way (Macaulay duality). For l in A_1 the rank matrix M_{A,l} records
ranks of multiplication by powers of l, and the Jordan degree type (JDT)
records Jordan block sizes with initial degrees, obtained by second
differences (AAIY Definition 2.19).

Reference throughout: N. Abdallah, N. Altafi, A. Iarrobino, J. Yameogo,
Jordan degree type for codimension three Gorenstein algebras of small
Sperner number, arXiv:2406.06322v2. Its Theorem 1 proves all potential JDT
occur for Sperner numbers s<=5, while for s=6, T=(1,3,6^k,3,1), Theorems
3.9-3.10 and Table 6 give at most 65 potential rank matrices/JDT (k>=5) in
22 Delta rows, with occurrence left as conjecture (Question 4.13).

## Definitions

- T=(1,3,6,6,6,6,6,3,1): socle degree j=8, k=5 (minimal case of k>=5).
- Rank matrix: (M_{A,l})_{u,v}=rk(m_{l^{v-u}}:A_u->A_v).
- JDT matrix J from M by J[u,v]=M[u,v]+M[u-1,v+1]-M[u-1,v]-M[u,v+1];
  admissibility requires J>=0 and Gorenstein symmetry
  eta(p,nu)=eta(p,j+1-nu-p) (AAIY Lemmas 2.2, 2.7(iv)).
- Lemma 2.15 (k>=3): the kxk center block (rows/cols 2..k+1 at j=8) is
  upper-triangular Toeplitz: M[u,v] depends only on v-u. Write
  r_i=M[2,2+i] (r_0=6), Delta_i=r_{i-1}-r_i; each admissible pair selects a
  Table-6 Delta row.

## Result

For T=(1,3,6^5,3,1) at j=8, 11 of the 65 Table-6 potential rank matrices /
JDT occur as computed pairs (A=R/Ann(F),l): five JDT variants with
Delta=(0,0,0,0) (row #1) and one variant each with Delta=(1,0,0,0) [#2],
(3,0,0,0) [#5], (2,2,2,0) [#19], (2,2,1,1) [#20], (3,2,1,0) [#17],
(3,1,1,1) [#18]. Each record passes H=T, corrected Toeplitz-center
admissibility, nonnegative JDT matrix, and symmetry identically under
GF(1000000007) and GF(1000000009), with explicit F and l in sweep_v2.json.
Coupled audit correction: Lemma-2.15 admissibility is diagonal constancy,
not column constancy; the earlier column predicate admitted only
Delta=(0,0,0,0) and is withdrawn (minimal counterexample: M[2,3]=M[3,4]=4,
M[2,4]=M[3,5]=2 is Toeplitz with r=(6,4,2,1,0) but fails column check).

## Proof / evidence

Engine fast_ag.py: contraction catalecticants, Hilbert functions,
multiplication-by-l ranks, JDT matrix, all by exact Gaussian elimination
mod p. Search sweep_v2.py: ~870 valid punctual-cone Gor(T) algebras
(a+b<=3 family, Lemma 2.13 tight-scheme preimage) plus 300 Waring power-sum
algebras at j=8, each against all 124 GF(p) linear-form directions over
{-2,...,2}^3. Filters: H=T; corrected toeplitz_center(); J>=0; symmetry;
r_0=6, r,Delta>=0. Certificates in sweep_v2.json (11 records with F,l,JDT,
r,Delta). Verification verify2p.py recomputes all 11 under both primes:
11/11 pass with identical rank matrices. Engine validated on published
s=3/s=4 table examples in characteristic 0. Independent audit recomputation
confirmed ALL_OK, diag(M)=H, total dim 38 with JDT size sum 38.

## Limitations

Finite-field computed evidence only: exact characteristic-0 (sympy/QQ)
certification timed out at j=8, so these are two-prime-verified computed
realizations, not characteristic-0 theorems. Two large primes agreeing is
strong evidence (ranks over GF(p) can only drop versus char 0 at fixed
integer data when p exceeds all minors) but not proof. Only k=5 computed;
no lifting to all k>=5 claimed. Corner-variant enumeration within realized
rows incomplete. 54 of 65 variants (15 Delta rows, including all r_1 in
{4,5}) remain unconstructed; stratification census explains sampling stall.

## Reproducibility

Run sweep_v2.py to regenerate sweep_v2.json (seed 424242), then verify2p.py
for two-prime recomputation. Key predicates: toeplitz_center() diagonal
constancy and delta_of_M() r_i=M[2,2+i] in fast_ag.py. Artifacts preserved:
fast_ag.py, sweep_v2.py, sweep_v2.json, verify2p.py.

## References

- Abdallah-Altafi-Iarrobino-Yameogo, arXiv:2406.06322v2
  (DOI 10.1016/j.laa.2025.08.018).
- Altafi, Jordan types with small parts..., DOI 10.1016/j.laa.2022.03.013.
