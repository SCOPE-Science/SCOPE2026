# A complete radial Weyl criterion for uniformly convex Fock weights

## Finding

Fix a complex dimension \(d\geq1\), a decay exponent \(\beta>0\), and a radial real \(C^2\) potential \(\Phi\) on \(\mathbb C^d\) satisfying the uniform real-Hessian bounds \(mI\leq\operatorname{Hess}_{\mathbb R}\Phi\leq MI\), with constants \(0<m\leq M<\infty\). Write \(\Phi(z)=\phi(|z|)\) and \(h(r)=\phi'(r)/r\) for \(r>0\). In the holomorphic Hilbert space with norm squared \(\int_{\mathbb C^d}|F(z)|^2e^{-2\Phi(z)}\,dv(z)\), let \(T_f\) be the Toeplitz operator of the positive radial symbol \(f(z)=(1+|z|^2)^{-\beta/2}\).

Let \(N(t)=\#\{j:s_j(T_f)>t\}\), with singular values decreasing and counted with multiplicity, and put \(R_t=(t^{-2/\beta}-1)^{1/2}\) for \(0<t<1\). Then the following *pointwise Weyl-profile formula* holds, without any assumption that the radial curvature has a limit:

\[
 t^{2d/\beta}N(t)=\frac{h(R_t)^d}{d!}+O(t^{1/\beta})\quad(t\downarrow0).
\]

For each integer \(n\geq0\), define \(r_n>0\) by \(r_n\phi'(r_n)=n+d-1/2\). Uniformly for all indices \(j\) in the degree-\(n\) multiplicity block

\[
 \binom{n+d-1}{d}<j\leq\binom{n+d}{d},
\]

the singular values obey

\[
 j^{\beta/(2d)}s_j(T_f)
 = (d!)^{-\beta/(2d)}h(r_n)^{\beta/2}+O(n^{-1/2})\quad(n\to\infty).
\]

Consequently a finite positive classical Weyl constant exists **if and only if** \(\lim_{r\to\infty}h(r)=H\) exists. In that case

\[
 N(t)\sim\frac{H^d}{d!}t^{-2d/\beta},\qquad
 s_j(T_f)\sim\left(\frac{H^d}{d!}\right)^{\beta/(2d)}j^{-\beta/(2d)}.
\]

More generally let \(h_-:=\liminf_{r\to\infty}h(r)\) and \(h_+:=\limsup_{r\to\infty}h(r)\). The **complete** sets of finite subsequential limits of \(t^{2d/\beta}N(t)\) as \(t\downarrow0\) and of \(j^{\beta/(2d)}s_j(T_f)\) as \(j\to\infty\) are, respectively,

\[
 \left[\frac{h_-^d}{d!},\frac{h_+^d}{d!}\right],\qquad
 \left[(d!)^{-\beta/(2d)}h_-^{\beta/2},
 (d!)^{-\beta/(2d)}h_+^{\beta/2}\right].
\]

The sufficient condition is strictly weaker than convergence of the real Hessian. For \(0<a<1/3\), the smooth radial weight \(\phi(r)=r^2/2+a(1-\cos r)\) has an oscillating radial Hessian eigenvalue, yet \(h(r)\to1\) and therefore has the standard Gaussian Weyl constant. By contrast, for \(0<a<1/3\), the smooth weight

\[
 \phi(r)=\frac{r^2}{2}+\frac{a}{4}\left[(1+r^2)
 \bigl(\sin\log(1+r^2)-\cos\log(1+r^2)\bigr)+1\right]
\]

has \(h(r)=1+a\sin\log(1+r^2)\), so its scaled counting function has the **exact** cluster interval \([(1-a)^d/d!,(1+a)^d/d!]\).

## Assumptions and scope

The real Hessian bound is understood on \(\mathbb R^{2d}\). For a radial \(C^2\) potential it is equivalent, at positive radius, to \(m\leq\phi''(r)\leq M\) and \(m\leq\phi'(r)/r\leq M\). The regularity at the origin gives \(\phi'(0)=0\). The Lebesgue-volume normalization in the Hilbert-space inner product cancels from every Toeplitz eigenvalue. No convergence of \(\phi''(r)\), pointwise third-derivative estimates, analyticity of the weight, or monotonicity of \(h\) is assumed. Constants in the error terms may depend on the fixed values \(d,\beta,m,M\) but not on the particular index or threshold.

The claim concerns the specific positive decreasing power symbol. It does not assert a Weyl criterion for arbitrary, nonradial, sign-changing or complex-valued Toeplitz symbols. For \(d>1\) the degree multiplicities are essential and are explicitly retained.

## Proof

**1. Radial spectral decomposition.** Orthogonality of homogeneous holomorphic polynomials under the radial measure and their density in the weighted Fock space yield an orthogonal decomposition into homogeneous degrees. Each degree-\(n\) subspace has dimension \(\binom{n+d-1}{d-1}\). Rotation invariance makes the radial Toeplitz operator scalar on this subspace, with eigenvalue

\[
 \lambda_n=
 \frac{\int_0^\infty (1+r^2)^{-\beta/2}
          r^{2n+2d-1}e^{-2\phi(r)}\,dr}
      {\int_0^\infty r^{2n+2d-1}e^{-2\phi(r)}\,dr}.
\]

These eigenvalues are strictly decreasing: the probability law in degree \(n+1\) is the degree-\(n\) law tilted by the strictly increasing function \(r^2\), whereas the symbol is strictly decreasing. Equivalently their difference is a strictly negative covariance divided by a positive moment. Since \(\lambda_n\to0\) by the localization proved below, \(T_f\) is compact, positive and diagonal, and its singular values are precisely these eigenvalues with the displayed multiplicities. No spectral mass or eigenvalues are omitted.

**2. Uniform saddle localization.** Set \(L_n(r)=(2n+2d-1)\log r-2\phi(r)\). The identity \(L_n'(r_n)=0\) is equivalent to \(r_n\phi'(r_n)=n+d-1/2\). Because

\[
 L_n''(r)=-\frac{2n+2d-1}{r^2}-2\phi''(r)\leq-2m,
\]

\(L_n\) is strictly concave and has a unique positive maximizer. The bounds \(m\leq h\leq M\) give \(r_n\asymp\sqrt n\). On \(|r-r_n|\leq1\) for large \(n\), \(|L_n''(r)|\leq C\); this uses \(n/r_n^2\asymp1\) and the upper Hessian bound. Therefore the normalized denominator is bounded below by \(ce^{L_n(r_n)}\), while global strong concavity yields

\[
 \mathbb P_n\{|R-r_n|>u\}\leq C\int_{|v|>u}e^{-mv^2}\,dv,
\]

where \(\mathbb P_n\) is the probability law having density proportional to \(e^{L_n(r)}\) on \((0,\infty)\). In particular \(\mathbb E_n|R-r_n|=O(1)\), and the probability of \(|R-r_n|>r_n/2\) is exponentially small in \(r_n^2\).

On the remaining central interval the logarithmic derivative of \((1+r^2)^{-\beta/2}\) is bounded by \(C/r_n\) and its ratio to its value at \(r_n\) is uniformly bounded. The Gaussian tail is negligible even after division by \((1+r_n^2)^{-\beta/2}\). It follows that

\[
 \lambda_n=(1+r_n^2)^{-\beta/2}\bigl(1+O(r_n^{-1})\bigr).
\]

This estimate is uniform over the stated radial Hessian class and requires no higher smoothness.

**3. Individual singular values and full cluster set.** The count of monomials through degree \(n\) is \(\binom{n+d}{d}\), so uniformly inside the degree-\(n\) block \(j=n^d/d!\,(1+O(n^{-1}))\). Use \(r_n^2h(r_n)=n+d-1/2\) in the preceding approximation. One obtains exactly the displayed blockwise law, with error \(O(n^{-1/2})\).

The map \(q(r)=r\phi'(r)\) is increasing with \(q'(r)=\phi'(r)+r\phi''(r)\) between \(2mr\) and \(2Mr\). Hence successive \(r_n\) have gaps \(O(1/r_n)\). Also \(h'(r)=(\phi''(r)-h(r))/r\), so \(|h'(r)|\leq C/r\). Thus the samples \(h(r_n)\) recover every tail limit point of the continuous function \(h(r)\). The tail limit-point set of a bounded continuous real function on a ray is the closed interval between its liminf and limsup. Continuity and the positive-power map give the stated singular-value cluster interval.

**4. Sharp counting profile.** For \(t\downarrow0\), set \(R_t=(t^{-2/\beta}-1)^{1/2}\), so the symbol evaluated at \(R_t\) is exactly \(t\). The uniform relative approximation in Step 2 and the fact that the symbol's logarithmic derivative at radius \(R_t\) is asymptotic to \(-\beta/R_t\) imply that there is a fixed \(A>0\) such that, for all sufficiently small \(t\), eigenvalues with saddle radii below \(R_t-A\) exceed \(t\), and those with saddle radii above \(R_t+A\) are below \(t\). For the near-threshold region choose \(A\) larger than the uniform relative-error constant divided by \(\beta\); outside that region use strict monotonicity of \(\lambda_n\). Since \(q'(r)\asymp r\), the final included degree is \(n_t=q(R_t)+O(R_t)\). Counting its homogeneous multiplicities gives

\[
 N(t)=\binom{n_t+d}{d}=\frac{q(R_t)^d}{d!}\bigl(1+O(R_t^{-1})\bigr).
\]

Now \(t^{2/\beta}R_t^2=1-t^{2/\beta}\), \(q(R_t)=R_t^2h(R_t)\), and \(h\) is bounded above and below. This yields

\[
 t^{2d/\beta}N(t)=\frac{h(R_t)^d}{d!}+O(t^{1/\beta}).
\]

The radius \(R_t\) ranges continuously through all sufficiently large radii as \(t\downarrow0\), proving the full counting cluster interval directly. The pointwise counting profile also shows that a Weyl coefficient exists exactly when \(h\) converges. The usual monotone-inversion equivalence between counting and decreasing singular values verifies the two constant formulas.

**5. Strictness and exact oscillation examples.** For the first example the radial and tangential Hessian eigenvalues are \(1+a\cos r\) and \(1+a\sin r/r\), so both are uniformly positive, while the former has no limit. Nonetheless \(h(r)=1+a\sin r/r\to1\). For the second example direct differentiation gives

\[
 h(r)=1+a\sin\log(1+r^2),\qquad
 \phi''(r)=1+a\sin\log(1+r^2)+\frac{2ar^2}{1+r^2}\cos\log(1+r^2).
\]

Both radial Hessian eigenvalues lie between \(1-3a\) and \(1+3a\). The phase \(\log(1+r^2)\) runs through infinitely many complete periods; thus \(h_-=1-a\) and \(h_+=1+a\), making both interval formulas explicit. These examples also verify the claimed strict separation between radial-slope and Hessian convergence.

## Verification

The analytic proof is contained in Steps 1–5. A standalone Python/scipy checker in `check.py` evaluates the defining radial eigenvalue quotients by saddle-shifted numerical integration for the Gaussian weight and the two explicit nonquadratic weights. It tests dimensions one through three, three exponents and three increasing degrees; 162 finite diagnostics passed. It prints representative convergence of the scaled singular values toward the predicted local slope profile. These finite checks are supplementary only. They are not used to prove asymptotics, complete cluster sets, the necessary-and-sufficient condition, or exact error bounds.

Run from the package root with `python check.py` after installing `requirements.txt`. The checker has no external data files or network dependencies.

## Relationship to prior work

Xu and Dong's 2026 paper proves quadratic-weight Weyl constants and constructs a *one-dimensional* smoothly oscillating radial weight yielding two distinct subsequential constants (Theorems 5.1–5.2 and Proposition 5.3). Its proof also supplies the radial eigenvalue representation and a saddle estimate along specially chosen plateaux. The present finding retains those known ingredients and adds an all-dimensional, uniform pointwise counting profile, the complete interval of limit points, and an exact *if-and-only-if* condition on radial geometry; it also establishes existence without convergence of the full Hessian. Neither the quadratic case nor the two-subsequence counterexample states this criterion. Grudsky and Vasilevski study radial symbols on the *Gaussian* Fock space, not variable radial Hessians. Huang, Wang and Zeng study rearrangement descriptions of singular-value asymptotics for Fock-type spaces; their accessible abstract does not state the radial geometric equivalence or the exact profile. Their full text could not be inspected, and stronger implicit overlap cannot be ruled out. Related work on oscillating radial **symbols** with a fixed Gaussian weight is not the same as oscillating the *weight* while keeping the power symbol fixed.

## Limitations

This is an analytical self-reviewed result, not an independently validated or externally certified theorem. It is restricted to a fixed positive decreasing radial power symbol and uniformly convex, uniformly bounded-Hessian radial weights. The uniform error bounds have fixed dimension and exponent; no parameter-uniform high-dimensional limit is claimed. The pointwise geometric profile may be a corollary of an uninspected, more general Fock-type spectral rearrangement theorem; publication-priority uncertainty remains. Numerical diagnostics cannot resolve that uncertainty or replace the proof.

## References

1. Chunxu Xu and Jianxiang Dong, *IDA symbols and Schatten--Lorentz theory for Toeplitz operators on weighted Fock spaces*, arXiv:2609.16970, first posted 2026-09-15. Relevant material: Theorems 5.1--5.2, Proposition 5.3 and its proof, Section 6.
2. S. M. Grudsky and N. L. Vasilevski, *Toeplitz operators on the Fock space: radial component effects*, Integral Equations and Operator Theory 44 (2002), 10--37. Available author-hosted PDF: https://www.math.cinvestav.mx/~grudsky/Papers/71.pdf.
3. Wenjie Huang, Xiaofeng Wang and Zhicheng Zeng, *Asymptotic behavior of singular values of Toeplitz and Hankel operators on Fock-type spaces*, Banach Journal of Mathematical Analysis 20 (2026), article 16, DOI:10.1007/s43037-025-00477-8. Accessible abstract consulted; full text unavailable in this review.
