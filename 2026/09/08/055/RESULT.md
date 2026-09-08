# First apolarity invariants for a P5 Perazzo-type quartic with three-variable base

## Context

Hypersurfaces with vanishing Hessian that are not cones, and the Weak Lefschetz
Property (WLP) of their Artinian Gorenstein algebras, form a recognized frontier
(Gordan–Noether, Gondim–Russo, Maeno–Watanabe Hessian–Lefschetz criteria, and the
Fiorindo–Mezzetti–Miró-Roig / Miró-Roig–Pérez-Díez / Mezzetti–Miró-Roig Perazzo
programs). Perazzo forms give the building blocks of vanishing-Hessian
hypersurfaces and always fail the Strong Lefschetz Property. WLP is classified
only for the two-variable-base \(P^{n+2}\) family
\(f=\sum p_i(u,v)x_i+g(u,v)\); Miró-Roig–Pérez-Díez explicitly state those results
do not generalize to the three-variable-base \(P^{n+3}\) family, and
Mezzetti–Miró-Roig leave WLP for intermediate vectors and minimal resolutions
open beyond the 5-variable minimal case (Section 6, Problems 1–2).

## Definitions

Work over \(\mathbb{Q}\). Let \(R=\mathbb{Q}[x_0,x_1,x_2,u,v,w]\) act on
\(S=\mathbb{Q}[X_0,X_1,X_2,U,V,W]\) by differentiation
(\(x_i=\partial/\partial X_i\), etc.). Let

\[F^* = x_0 u^3 + x_1 v^3 + x_2 (u+v)^3 + w^4,\]

a Perazzo-type quartic with three-variable base \((u,v,w)\):
\(p_0=u^3,p_1=v^3,p_2=(u+v)^3\) are algebraically dependent but linearly
independent, and \(w\) occurs via \(w^4\).
Let \(A_{F^*}=R/\mathrm{Ann}_R(F^*)\) be its apolarity (Macaulay inverse-system)
Artinian Gorenstein algebra of socle degree 4.
WLP means some linear form \(\ell\) has maximal rank
\(\times\ell:A_i\to A_{i+1}\) in every degree.

## Result

For \(A=A_{F^*}\):

1. **Hilbert vector.** \(H(A)=(1,6,7,6,1)\) (socle degree 4, length 21).
   Catalecticant ranks: \(\mathrm{rk}\,C_1=6\) (\(56\times 6\)),
   \(\mathrm{rk}\,C_2=7\) (\(21\times 21\)),
   \(\mathrm{rk}\,C_3=6\) (\(6\times 56\)).
2. **Vanishing Hessian.** The classical first Hessian
   \(\det\mathrm{Hess}(F^*)=0\) identically as a polynomial. The rows for
   \(x_0,x_1,x_2\) have entries supported only in the \(u,v\) columns
   (\(3u^2,0\); \(0,3v^2\); \(3(u+v)^2,3(u+v)^2\)), so three rows lie in a
   2-dimensional coordinate subspace and the \(6\times 6\) Hessian is
   identically singular; confirmed by symbolic expansion.
3. **Weak Lefschetz HOLDS** (correcting the admitted target's guess of failure).
   For \(L^*=x_0+x_1+x_2+u+v+w\):
   \(\times L^*:A_1\to A_2\) is \(7\times 6\) of rank 6 with
   \(6\times 6\) minor (rows 0,1,2,4,5,6) equal to \(2\);
   \(\times L^*:A_2\to A_3\) is \(6\times 7\) of rank 6 with
   \(6\times 6\) minor (cols 0–5) equal to \(4\);
   outer maps \(A_0\to A_1\) and \(A_3\to A_4\) have rank 1.
   Hence a (indeed general) linear form is maximal-rank in every degree.
4. **Graded Betti table** of \(A\) over \(R\) (\(\beta_{i,t}=\dim\mathrm{Tor}^R_i(A,k)_t\),
   rows \(t=j\), columns \(i\)):
   \(t{=}0\): 1 0 0 0 0 0 0; \(t{=}1\): all 0;
   \(t{=}2\): 0 14 0 0 0 0 0; \(t{=}3\): 0 2 36 0 0 0 0;
   \(t{=}4\): 0 4 8 39 0 0 0; \(t{=}5\): 0 0 20 12 20 0 0;
   \(t{=}6\): 0 0 0 39 8 4 0; \(t{=}7\): 0 0 0 0 36 2 0;
   \(t{=}8\): 0 0 0 0 0 14 0; \(t{=}9\): all 0;
   \(t{=}10\): 0 0 0 0 0 0 1.
   In particular \(\mathrm{Ann}(F^*)\) needs 14 quadrics + 2 cubics;
   projective dimension 6, regularity 4.

## Proof / evidence

Exact rational computation over \(\mathbb{Q}\) (sympy only, seconds),
replayed end-to-end by `artifacts/verify_Fstar.py` (prints `VERIFY_OK`):

- Apolarity: \((C_k)\) built from differential-action derivatives of \(F^*\);
  rank over \(\mathbb{Q}\) gives \(h_k\).
- Quotient bases = pivot columns of \(C_k\); projectors from row-pivots give
  exact multiplication matrices; commutativity \(x_ix_j=x_jx_i\) checked on
  \(A_0,A_1,A_2\).
- WLP: ranks of \(\times L^*\) computed exactly; nonzero minors 2 and 4
  exhibited; full maximal profile \([1,6,6,1]\) independently confirmed for
  \(L^*\) and two further linear forms.
- Betti numbers via Koszul-complex rank-nullity in each degree \(t\);
  audited by the Euler/Hilbert identity
  \(\sum_i(-1)^i b_i(t)=\sum_j(-1)^j\binom{6}{j}h_{t-j}\) for all
  \(t=0,\dots,10\) and Gorenstein symmetry \(b_i(t)=b_{6-i}(10-t)\).

## Limitations

- Single named object; no general \(P^{n+3}\) classification theorem is claimed.
- Betti numbers are certified Koszul–Tor computations (exact rational), not a
  structural resolution argument; minimality follows from the
  Koszul/minimal-complex rank-nullity construction.
- \(\mathrm{Ann}(F^*)\) is certified via dimension counts
  (\(\dim\mathrm{Ann}_2=14,\dim\mathrm{Ann}_3=50,\dim\mathrm{Ann}_4=125\)) and
  Gorenstein symmetry, not by an exhibited minimal generating set.
- WLP rests on one explicit full-rank linear form \(L^*\) plus generic spot
  checks, not a Zariski-open description of the Lefschetz locus.

## Reproducibility

Run `python3 artifacts/verify_Fstar.py` (requires sympy only; ~seconds).
It asserts the Hilbert vector, Hessian vanishing, both mid-degree ranks with
witness minors, commutativity, and the full Betti table with Euler checks,
then prints `VERIFY_OK`.

## References

- L. Fiorindo, E. Mezzetti, R. M. Miró-Roig, Perazzo 3-folds and the weak
  Lefschetz property. https://arxiv.org/abs/2206.02723
- R. M. Miró-Roig, J. Pérez-Díez, Perazzo hypersurfaces and the weak Lefschetz
  property. https://arxiv.org/abs/2402.09188
- E. Mezzetti, R. M. Miró-Roig, Perazzo \(n\)-folds and the weak Lefschetz
  property. https://arxiv.org/abs/2405.14756
