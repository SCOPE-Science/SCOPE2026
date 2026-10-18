# Single-erasure boundary layers for Chebyshev–Lobatto interpolation

## Finding

For every integer \(N\ge2\), let \(x_{j,N}=\cos(j\pi/N)\), \(0\le j\le N\). Delete one index \(k\) and let \(I_{N,k}\) be the unique polynomial interpolation map of degree at most \(N-1\) using the remaining \(N\) nodes, with the uniform norm on \([-1,1]\). Define \(\Lambda_{N,k}=\|I_{N,k}\|_{C([-1,1])\to C([-1,1])}\). With \(d_N=\min\{k,N-k\}\), the following classification holds.

1. If \(k=0\) or \(k=N\), then \(\Lambda_{N,k}/N\to2\).
2. If \(d_N\to\infty\), then \(\Lambda_{N,k}/N\to1\), even if \(d_N/N\to0\).
3. For each fixed integer \(j\ge1\), if \(k=j\) or \(k=N-j\), then
\[
\lim_{N\to\infty}\frac{\Lambda_{N,k}}{N}=\rho_j,
\qquad
\rho_j=\max_{z\ge0}\left|\frac{2z\sin z}{z^2-j^2\pi^2}\right|>1.
\]
The fraction at \(z=j\pi\) has its continuous value of absolute magnitude \(1\). The boundary-layer constants satisfy
\[
\rho_j=1+\frac{3}{8\pi^2j^2}+O(j^{-4})\qquad(j\to\infty).
\]

In fact, put \(\rho_0=2\). These statements combine into the uniform single-erasure law
\[
\lim_{N\to\infty}\max_{0\le k\le N}\left|\frac{\Lambda_{N,k}}{N}-\rho_{\min\{k,N-k\}}\right|=0.
\]
Thus the classification remains meaningful even when the deleted location changes irregularly with \(N\).

More precisely, put \(c_0=c_N=1/2\), \(c_j=1\) for \(0<j<N\), and \(w_j=(-1)^jc_j\). If \(\ell_{j,N}\) are the full-grid cardinal polynomials, then for every \(N\ge2\) and every \(0\le k\le N\),
\[
\left|\Lambda_{N,k}-\left(\frac{N}{c_k}-1\right)\|\ell_{k,N}\|_\infty\right|\le\Lambda_N^{\mathrm{full}}=O(\log(N+1)).
\]
The error bound is uniform in the deletion index. At the deleted node itself, the Lebesgue function is exactly \(N-1\) for an interior deletion and \(2N-1\) for an endpoint deletion.

## Assumptions and scope

All norms are ordinary, unweighted supremum norms of continuous functions on the entire closed interval \([-1,1]\); the operators use exact, rather than rounded, Chebyshev–Lobatto nodes. The limit \(N\to\infty\) is taken with an explicitly described sequence of missing-node indices. The formula for \(\rho_j\) concerns a fixed integer distance \(j\) from an endpoint; it is not a statement about an index growing proportionally to \(N\). The notation \(O(j^{-4})\) has an absolute implied constant for sufficiently large positive integers \(j\).

## Proof

**Exact erasure identity.** The barycentric weights of the full Chebyshev–Lobatto grid are proportional to \(w_j=(-1)^jc_j\), with \(\sum_{j=0}^{N}|w_j|=N\). Let \(\ell_{j,N}\) denote its degree-at-most-\(N\) Lagrange cardinal polynomials. Their leading coefficients are proportional to \(w_j\). Therefore, for every retained index \(i\ne k\),
\[
\widetilde\ell_{i,N,k}(x)
=\ell_{i,N}(x)-\frac{w_i}{w_k}\ell_{k,N}(x)
\]
has degree at most \(N-1\) and the correct Kronecker values at all retained nodes. It is consequently the reduced-grid cardinal polynomial. In particular \(\widetilde\ell_{i,N,k}(x_{k,N})=-w_i/w_k\), yielding the exact missing-node Lebesgue value \(\sum_{i\ne k}|w_i|/|w_k|=N/c_k-1\).

**Sharp uniform comparison.** By the reverse triangle inequality for the \(\ell^1\) norm, for every \(x\in[-1,1]\),
\[
\left|\sum_{i\ne k}|\widetilde\ell_{i,N,k}(x)|
-\left(\frac{N}{c_k}-1\right)|\ell_{k,N}(x)|\right|
\le\sum_{i\ne k}|\ell_{i,N}(x)|
\le\Lambda_N^{\mathrm{full}}.
\]
Taking suprema and using the reverse estimate at a maximizing point of \(|\ell_{k,N}|\) establishes the claimed comparison of operator norms.

**A uniform logarithmic bound for the intact grid.** Write \(x=\cos\theta\), \(\theta_j=j\pi/N\), and let \(\delta=\theta-\theta_j\). The standard Chebyshev cardinal formula, with continuous interpretation at removable singularities, is
\[
\ell_{j,N}(\cos\theta)
=\frac{(-1)^{j+1}c_j\sin\theta\,\sin(N\theta)}{N(\cos\theta-\cos\theta_j)}.
\]
For distinct angles define
\[
R(\theta,\theta_j)
=\frac{\sin\theta\,|\theta-\theta_j|}{|\cos\theta-\cos\theta_j|}.
\]
The denominator divided by \(|\theta-\theta_j|\) is the average of \(\sin t\) between the angles. Concavity of sine on \([0,\pi]\) gives \(0\le R\le2\). Moreover \(|\sin(N\theta)|=|\sin(N\delta)|\le\min\{1,N|\delta|\}\), so
\[
|\ell_{j,N}(\cos\theta)|\le 2c_j\min\left\{1,\frac{1}{N|\theta-\theta_j|}\right\}.
\]
Summing over a uniformly spaced angular grid gives \(\Lambda_N^{\mathrm{full}}\le C(1+\log(N+1))\) with an absolute \(C\), uniformly in the evaluation angle.

**Endpoint and bulk limits.** At either endpoint cardinal index \(0\) or \(N\), the last inequality gives \(\|\ell_{k,N}\|_\infty\le1\); equality holds at its own node. Hence the uniform comparison and \(c_k=1/2\) yield the endpoint coefficient \(2\).

For an interior sequence let \(d_N=\min\{k,N-k\}\to\infty\). Fix \(A>3\). If \(N|\theta-\theta_k|\ge A\), the displayed bound gives \(|\ell_{k,N}(\cos\theta)|\le2/A<1\). Otherwise \(|\theta-\theta_k|\le A/N\) and \(\sin\theta_k\ge2d_N/N\). The mean-value integral for the cosine difference implies, uniformly in this local region,
\[
R(\theta,\theta_k)\le\frac{2d_N+A}{2d_N-A}=1+O(A/d_N).
\]
As \(|\sin(N\delta)|/(N|\delta|)\le1\), the global cardinal norm is \(1+o(1)\); the lower bound \(1\) occurs at the cardinal node. With \(c_k=1\), the normalized deleted-grid Lebesgue constant tends to \(1\).

**Fixed-index boundary layer.** Fix \(j\ge1\) and put \(k=j\). Rescale the endpoint angle as \(\theta=z/N\). Uniformly on every compact \(z\)-interval, the cardinal formula converges, including at the removable pole, to
\[
|\ell_{j,N}(\cos(z/N))|\longrightarrow
\left|\frac{2z\sin z}{z^2-j^2\pi^2}\right|.
\]
Outside \(z\ge A>j\pi\), the logarithmic-grid proof's bound gives \(|\ell_{j,N}|\le2/(A-j\pi)\). This controls the escaping maxima as \(A\to\infty\). Thus \(\|\ell_{j,N}\|_\infty\to\rho_j\). Reflection \(x\mapsto-x\) yields the same answer for \(k=N-j\). At \(z=j\pi\), the limiting modulus equals \(1\), and its derivative immediately to the right is \(1/(2j\pi)>0\), so \(\rho_j>1\).

**Large boundary-index expansion.** Put \(a=j\pi\) and write \(z=a+\delta\), with \(\delta\ge-a\). The modulus defining \(\rho_j\) becomes exactly
\[
\left|\frac{\sin\delta}{\delta}\right|
\frac{2(a+\delta)}{2a+\delta}.
\]
For \(\delta\le0\), this is at most \(1\). For sufficiently large \(a\), the expression is below \(1\) for \(\delta\ge1\): on \([1,2]\), use \(|\sin\delta|/\delta\le\sin(1)\) and the second factor at most \(1+1/a\); on \([2,a]\), use the upper bound \(1/\delta+1/(2a)\le1/2+1/(2a)\); and on \([a,\infty)\), use the upper bound \(2/\delta\le2/a\). On \(0\le\delta\le1\), the inequality \(\sin\delta/\delta\le1-c\delta^2\) for an absolute \(c>0\), together with \(2(a+\delta)/(2a+\delta)\le1+\delta/(2a)\), forces every maximizer to satisfy \(\delta=O(1/a)\). Substituting \(\delta=y/a\) gives uniformly for bounded \(y\),
\[
\frac{\sin\delta}{\delta}\frac{2(a+\delta)}{2a+\delta}
=1+\frac{y/2-y^2/6}{a^2}+O(a^{-4}).
\]
The quadratic has unique maximum \(3/8\) at \(y=3/2\). Uniform localization then yields \(\rho_j=1+3/(8j^2\pi^2)+O(j^{-4})\).

**Uniformity over all deletion indices.** If the final uniform formula failed, take a sequence of degree/index pairs with error bounded away from zero. Pass to a subsequence where either \(d_N=\min\{k,N-k\}\) is a fixed integer, or \(d_N\to\infty\). The preceding endpoint, fixed-index and bulk limits cover these two alternatives. In the unbounded case, the large-index estimate gives \(\rho_{d_N}\to1\). Each alternative contradicts failure of the uniform formula.

## Verification

A standard-library Python checker, `check_erasure.py`, separately evaluates reduced-grid cardinal functions using weights \(w_i(x_{i,N}-x_{k,N})\). It compares these with the cancellation identity, verifies every deleted-node weight and the pointwise comparison, and samples the three large-degree regimes against the explicit boundary-mode variational constants. The packaged checker passed 1242 deterministic finite assertions. For reference, the numerical values are \(\rho_1\approx1.031819618245588\) and \(\rho_2\approx1.009025844398614\). Finite tests are consistency checks, not proofs of the limits or historical priority.

To reproduce: run `python3 check_erasure.py` from the directory containing this document and the checker. The analytical proof is self-contained apart from the standard exact Chebyshev–Lobatto barycentric weights and elementary trigonometric inequalities, both displayed above.

## Relationship to prior work

The intact Chebyshev–Lobatto grid has logarithmic Lebesgue growth. Salzer's 1972 interpolation formulas, Mascarenhas's 2013 preprint on stable barycentric evaluation, and Xiang's 2014 preprint on interpolation errors and fundamental-polynomial bounds supply the classical full-grid setting. They do not, in the inspected material, give the single-erasure operator-norm asymptotic classification above. Wu's 2026 perturbation theory concerns distinct full-size angularly perturbed grids, not deletion of a node and reduction by one in polynomial degree. The exact boundary-profile constant depends on the deleted node's distance from the edge; this exceeds a mere restatement of the intact-grid logarithmic estimate.

## Limitations

No finite-degree exact global maximizing location is asserted (except for the exact Lebesgue value evaluated at the missing node). The result treats one missing node, exact Chebyshev–Lobatto coordinates, and uniform error amplification; it does not cover multiple erasures, noisy-node displacement, rounded arithmetic or a claim of universal practical instability for smooth data. Some older printed literature, particularly Salzer's original full text, was not available for line-by-line historical comparison. Mathematical priority has not been established independently.

## References

- H. E. Salzer, “Lagrangian Interpolation at the Chebyshev Points ...; Some Unnoted Advantages,” *The Computer Journal* 15 (1972), 156–159, DOI: 10.1093/comjnl/15.2.156. Abstract and bibliographic record inspected.
- W. F. Mascarenhas, “The stability of barycentric interpolation at the Chebyshev points of the second kind,” arXiv:1309.7944, first public preprint 2013-09-30. Full open-text paper inspected, including introduction, formula (3)/(4), numerical-stability analysis and appendices.
- S. Xiang, “On Interpolation Approximation: Convergence rates for polynomial interpolation for functions of limited regularity,” arXiv:1411.7746, first public preprint 2014-11-28. Full open-text paper inspected, especially introduction and fundamental-polynomial estimates.
- H.-N. Wu, “When do perturbed Chebyshev–Lobatto points remain Chebyshev?”, arXiv:2606.23409, first public preprint 2026-06-22. Full open-text paper inspected as a later mathematical comparison only.
