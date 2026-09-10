# No linkage-built socle-6 codimension-4 Gorenstein witness with general Jordan longest part ≤ 6

## Context

Codimension-4 Artinian Gorenstein (AG) Lefschetz geography at socle degree 6 is
open: the r ≤ 5 census is tabulated while r = 6 has only isolated examples
(Abdallah–Schenck), and no WLP ⇒ SLP theorem closes the stratum. The admitted
target asked for a linkage-plus-deformation sextic with Hilbert function
H = (1,4,6,8,6,4,1), WLP failure via an 8×6 middle-rank defect, and
general-linear Jordan type strictly below H^∨ = (7,5,5,5,3,3,1,1) **with
longest part at most 6**.

## Definitions

Let k be algebraically closed of characteristic 0, R = k[x₀,x₁,u,v],
S = k[X₀,X₁,U,V], 0 ≠ F ∈ S₆ homogeneous. Let A = R/Ann(F) be the apolar
(Macaulay-dual) algebra; it is standard-graded Artinian Gorenstein of socle
degree 6 with A₆ ≅ k, A₇ = 0. For L ∈ A₁ write ×L : A → A for multiplication
by L and P(L) for its Jordan partition. "General L" means a nonempty Zariski
open in P(A₁) ≅ P³. The apolar action is
x^α ∘ X^β = β!/(β−α)! X^{β−α} if β ≥ α coordinatewise, else 0.

## Result

**Theorem.** For general L, P(L) has longest part exactly 7. In particular
there is no codimension-4 socle-6 apolar Gorenstein algebra — however
constructed (linkage, deformation, or otherwise) — whose general-linear Jordan
type has longest part at most 6.

**Corollary.** The target conjunction, which requires together with
H = (1,4,6,8,6,4,1), WLP failure, and strict Jordan dominance below
H^∨ = (7,5,5,5,3,3,1,1) the further clause "longest part at most 6", is
unsatisfiable and hence false. The refutation uses only the Jordan clause.

## Proof / Evidence

Write L = Σ aᵢxᵢ, a = (a₀,…,a₃). By the multinomial theorem,
L⁶ = Σ_{|α|=6} (6!/α!) a^α x^α. For |α| = 6 and F = Σ c_β X^β,
x^α ∘ F = α! c_α (constant). Hence

    L⁶ ∘ F = Σ 6!/α! a^α · α! c_α = 6! Σ c_α a^α = 720·F(a).   (*)

Since k is infinite and F ≠ 0, some a has F(a) ≠ 0; char k = 0 gives
720 ≠ 0, so [L⁶] ≠ 0 in the 1-dimensional socle A₆. Thus (×L)⁶ ≠ 0 while
(×L)⁷ = 0 (A₇ = 0): nilpotency index exactly 7, so the largest Jordan block
is exactly 7. The locus {F(a) ≠ 0} is the complement of the sextic
hypersurface V(F) ⊂ P³, a nonempty Zariski open; hence this holds for general
L. The clause "general-linear Jordan type with longest part at most 6" is
therefore unsatisfiable. ∎

Conjugate check: H = (1,4,6,8,6,4,1) sums to 30; sorted parts (8,6,6,4,4,1,1)
have conjugate (7,5,5,5,3,3,1,1), also summing to 30. Strict dominance below
H^∨ is compatible with longest part 7; only the appended "≤ 6" clause is
impossible. The argument needs 6! ≠ 0 (char 0) and k infinite.

Computational corroboration (not the proof): `artifacts/verify_disproof.py`
certifies the conjugate arithmetic, identity (*) on Fermat ΣXᵢ⁶ and a
Perazzo-like sextic (L₀⁶∘F = 2880 = 720·4 and 5760 = 720·8), and Fermat apolar
HF [1,4,4,4,4,4,1] confirming A₆ ≅ k. Run:
`python3 artifacts/verify_disproof.py` → `VERIFY_OK`.

## Limitations

- Disproves the target as stated via the Jordan "≤ 6" clause; does **not**
  rule out a WLP-failure witness at H = (1,4,6,8,6,4,1) with longest part 7.
- Uses characteristic zero (6! ≠ 0) and k infinite; no claim in
  characteristics 2 or 3 where (*) degenerates.
- Covers apolar (Macaulay-dual) Gorenstein algebras, which is the target's
  fixed setting; no statement about non-apolar presentations.

## Reproducibility

Proof replays from the logged polynomials alone: expand (*) as above and
evaluate at any a with F(a) ≠ 0. Machine check:
`python3 artifacts/verify_disproof.py` (stdlib + sympy) → `VERIFY_OK`.

## References

- N. Abdallah, H. Schenck, Free resolutions and Lefschetz properties of some
  Artin Gorenstein rings of codimension four, arXiv:2208.01536.
- R. Gondim, On higher Hessians and the Lefschetz properties,
  arXiv:1506.06387.
- N. Altafi, A. Iarrobino, P. Macías Marques, Jordan type of an Artinian
  algebra, a survey, arXiv:2307.00957.
- B. Costa, R. Gondim, The Jordan type of graded Artinian Gorenstein
  algebras.
