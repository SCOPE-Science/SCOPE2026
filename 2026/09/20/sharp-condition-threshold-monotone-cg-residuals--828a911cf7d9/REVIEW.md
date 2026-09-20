# Review — sharp condition-number threshold for monotone exact-CG residuals

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof reduces each residual ratio to the exact identity
\[
\frac{\|r_{k+1}\|_2^2}{\|r_k\|_2^2}
=
-1+
\frac{\|r_k\|_2^2\|Ap_k\|_2^2}{(p_k^TAp_k)^2}.
\]
The equality \(r_k^TAp_k=p_k^TAp_k\) follows from adjacent
\(A\)-conjugacy, while \(r_k\perp p_{k-1}\) gives
\[
d_k=\frac{\|p_k\|_2^2}{\|r_k\|_2^2}
=1+\beta_{k-1}d_{k-1}.
\]
Applying the Kantorovich inequality to \(A^{1/2}p_k\) yields
\[
\frac{\|p_k\|_2^2\|Ap_k\|_2^2}{(p_k^TAp_k)^2}
\le\frac{(L+\mu)^2}{4L\mu},
\]
which gives both the history-aware and global bounds.

Sharpness is exact: the initial residual
\(\sqrt L\,u_\mu+\sqrt\mu\,u_L\) attains the global bound on any fixed SPD
matrix with extreme eigenvalues \(\mu,L\). Solving when that factor is at
most one gives precisely \(\kappa\le3+2\sqrt2\). The PCG statement follows
from the standard symmetric transformation
\(M^{-1/2}AM^{-1/2}\), whose Euclidean residual is
\(M^{-1/2}r\).

The accompanying deterministic computation reproduces the endpoint
equality at and on both sides of the threshold and checks the global and
history-aware inequalities on 300 SPD examples.

## Originality

**PASS, to the best of our knowledge.**

The checked literature establishes several nearby facts:

- Hestenes--Stiefel (1952) contains classical examples and constructions
  showing that CG residual norms can be nonmonotone.
- Meurant's 2006 exact-arithmetic chapter explicitly states that it studies
  conditions under which residual norms oscillate.
- Carson--Liesen--Strakoš (2024) revisits prescribed CG residual behavior
  and notes the distinction between prescribing residual histories and
  simultaneously controlling the spectrum.
- Brown (2024) derives the exact first-step vector criterion for residual
  increase and gives \(\kappa\ge7\) as a simple sufficient
  condition from one endpoint mixture.
- Standard exact-line-search gradient-descent results control objective or
  energy-norm decrease, not the sharp Euclidean CG residual-step factor
  proved here.

Searches for the exact factor
\((\kappa-1)/(2\sqrt\kappa)\), the threshold
\(3+2\sqrt2\), synonymous monotone-residual formulations, and
Kantorovich-based CG residual conditions did not locate a source stating the
fixed-matrix if-and-only-if threshold, the all-step sharp factor, or the
history refinement.

The principal residual originality risk is historical coverage. The
available excerpt of Meurant's Chapter 2 confirms directly that residual
oscillation conditions are treated there, but the complete theorem-level
chapter was not available for inspection. The relevant full treatment in
Liesen--Strakoš was also not inspected. The original Hestenes--Stiefel
paper was identified and its role was cross-checked through later literature,
but its entire theorem-level discussion of the residual-history construction
was not relied upon as evidence of absence. Accordingly the originality
claim remains explicitly qualified.

## Value

**PASS.**

The result gives a simple sharp boundary between two qualitatively different
regimes of exact CG. Below \(3+2\sqrt2\), Euclidean residual monitoring is
guaranteed to be monotone for every problem with the fixed SPD matrix; above
it, a first-step increase is always constructible using only the two extreme
eigenspaces. The per-step bound is sharp, while the history factor
\(d_k\) supplies a stronger certificate from quantities already determined
by the CG recurrence. The fixed-preconditioner reformulation gives an
immediate interpretation in the natural PCG residual norm.

## Scientific limitations

- Exact arithmetic and finite-dimensional real SPD matrices only.
- No claim about floating-point recursive-residual monotonicity or residual
  gaps.
- No Euclidean-residual monotonicity claim for PCG; the extension is in the
  \(M^{-1}\)-norm.
- The condition-number criterion is uniform over all right-hand sides and
  starting guesses, not necessary for monotonicity of a particular run.
- No new \(A\)-norm error bound, iteration-complexity claim, or performance
  claim is made.
- Complete theorem-level access to the most relevant historical monograph
  treatments was unavailable, leaving residual prior-coverage risk.
