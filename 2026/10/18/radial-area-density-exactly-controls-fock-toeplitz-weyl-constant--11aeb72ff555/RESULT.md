# Radial area density exactly controls Fock Toeplitz Weyl constants

## Finding

Fix \(\beta>0\). Let \(\Phi\) be a real radial \(C^2\) weight on \(\mathbb C\) whose real Hessian satisfies \(mI\leq\nabla^2\Phi\leq MI\) for some \(0<m\leq M<\infty\), and let \(T_f\) be the Toeplitz operator on the holomorphic weighted Fock space \(F^2_\Phi\subset L^2(\mathbb C,e^{-2\Phi(|z|)}dA(z))\) with fixed positive symbol \(f(z)=(1+|z|^2)^{-\beta/2}\). Write its decreasing singular values as \(s_1,s_2,\ldots\). For each integer \(n\geq0\), let \(\rho_n>0\) be the unique solution of
\[
\rho_n\Phi'(\rho_n)=n+\tfrac12,
\qquad b(r)=\frac{\Phi'(r)}r.
\]
Then there is a constant depending only on \(m,M,\beta\) such that
\[
\boxed{(n+1)^{\beta/2}s_{n+1}(T_f)=b(\rho_n)^{\beta/2}+O((n+1)^{-1/2})}\qquad(n\to\infty).
\]
In particular, with \(L_-=\liminf_{r\to\infty}b(r)\) and \(L_+=\limsup_{r\to\infty}b(r)\), the *complete cluster set* of \(((n+1)^{\beta/2}s_{n+1})_{n\geq0}\) is
\[
\boxed{[L_-^{\beta/2},L_+^{\beta/2}].}
\]
The following three statements are equivalent for any \(L>0\):
\[
\lim_{t\downarrow0}t^{2/\beta}\#\{j:s_j(T_f)>t\}=L;
\qquad
\lim_{r\to\infty}\frac{\Phi'(r)}r=L;
\qquad
\lim_{r\to\infty}\frac{2\Phi(r)}{r^2}=L.
\]
Equivalently, the Weyl coefficient exists precisely when the large-disk average of the planar Laplacian \(\Delta\Phi\) has a limit, and the coefficient is one half that limit. This is an exact necessary-and-sufficient radial geometric condition, not an assumption of convergence of the Hessian.

## Assumptions and scope

The radial function is denoted by the same letter \(\Phi:[0,\infty)\to\mathbb R\) and its extension \(z\mapsto\Phi(|z|)\). We assume the extension is \(C^2\), so \(\Phi'(0)=0\). The Hessian hypothesis is equivalent, for \(r>0\), to \(m\leq\Phi''(r)\leq M\) and \(m\leq\Phi'(r)/r\leq M\). The Fock norm is \(\|h\|^2=\int_{\mathbb C}|h(z)|^2e^{-2\Phi(|z|)}dA(z)\). The operator \(T_f=P_\Phi M_f\) is bounded and positive. The counting function uses strict inequality; this convention does not affect its limit. No assertion is made for nonradial weights, arbitrary complex symbols, or weights without two-sided Hessian bounds.

## Proof

**Diagonalization and ordering.** Angular integration makes the monomials orthogonal. Taylor polynomials are complete: for an entire \(h(z)=\sum_{n\geq0}c_nz^n\), angular Parseval and Tonelli give \(\|h\|^2=\sum_n|c_n|^2\|z^n\|^2\); the sums are finite exactly for elements of \(F^2_\Phi\). Consequently \(T_f\) is diagonal on normalized monomials, with eigenvalues
\[
\lambda_n=\frac{\int_0^\infty (1+r^2)^{-\beta/2}r^{2n+1}e^{-2\Phi(r)}\,dr}{\int_0^\infty r^{2n+1}e^{-2\Phi(r)}\,dr}.
\]
Let \(\mathbb E_n\) denote expectation for the probability density proportional to the denominator integrand. Since \(r^2\) increases and \(f(r)\) strictly decreases, the covariance inequality yields
\[
\lambda_{n+1}=\frac{\mathbb E_n[f(R)R^2]}{\mathbb E_n[R^2]}<\mathbb E_n[f(R)]=\lambda_n.
\]
Thus the ordered singular values satisfy \(s_{n+1}=\lambda_n\), once \(\lambda_n\to0\), which follows from the concentration estimate below.

**Uniform saddle concentration.** Put \(h_n(r)=(2n+1)\log r-2\Phi(r)\), \(r>0\). Its unique maximizer is \(\rho_n\), since \(h_n'(r)=0\) exactly when \(r\Phi'(r)=n+1/2\); this latter function increases strictly from zero to infinity. The Hessian bounds give
\[
\sqrt{(n+1/2)/M}\leq\rho_n\leq\sqrt{(n+1/2)/m},
\qquad h_n''(r)=-\frac{2n+1}{r^2}-2\Phi''(r)\leq-2m.
\]
Hence \(e^{h_n(r)}\leq e^{h_n(\rho_n)}e^{-m(r-\rho_n)^2}\). On \(|r-\rho_n|\leq1\), for sufficiently large \(n\), the same Hessian bounds imply \(h_n''(r)\geq-C_{m,M}\), so the normalizing integral is bounded below by \(c_{m,M}e^{h_n(\rho_n)}\). It follows that, uniformly in \(n\),
\[
\mathbb E_n|R-\rho_n|\leq C_{m,M},\qquad
\mathbb P_n(|R-\rho_n|>u)\leq C_{m,M}\int_{|x|>u}e^{-mx^2}\,dx.
\]
On \(|R-\rho_n|\leq\rho_n/2\), the logarithmic derivative of \(f\) yields \(|f(R)/f(\rho_n)-1|\leq C_\beta|R-\rho_n|/\rho_n\). Outside that event, the Gaussian tail multiplied by the worst possible ratio \(f(R)/f(\rho_n)\leq(1+\rho_n^2)^{\beta/2}\) is exponentially negligible. Therefore
\[
\lambda_n=(1+\rho_n^2)^{-\beta/2}\bigl(1+O_{m,M,\beta}(\rho_n^{-1})\bigr).
\]
Using \(\rho_n^2b(\rho_n)=n+1/2\) and \(\rho_n\asymp\sqrt n\) gives the displayed uniform \(O(n^{-1/2})\) tracking formula and \(\lambda_n\to0\).

**No missed curvature limits.** The function \(b\) obeys \(|b'(r)|=|\Phi''(r)/r-\Phi'(r)/r^2|\leq2M/r\). Since \(H(r)=r\Phi'(r)\) has derivative \(\Phi'(r)+r\Phi''(r)\geq2mr\), consecutive solutions satisfy \(\rho_{n+1}-\rho_n=O(1/\rho_n)\). Thus \(b(\rho_n)\) samples the full tail cluster set of the continuous function \(b(r)\). Its tail cluster set is exactly the interval \([L_-,L_+]\): the image of every connected half-line is an interval and the closures are nested compact intervals. Applying the tracking formula and continuity of positive powers proves the asserted cluster interval.

**Equivalence of geometric and spectral limits.** The tracking formula and the complete cluster interval show that \((n+1)^{\beta/2}s_{n+1}\) has a limit \(L^{\beta/2}\) if and only if \(b(r)\to L\). Monotone inversion for strictly decreasing positive eigenvalues gives \(\lim_{t\downarrow0}t^{2/\beta}N(t;T_f)=L\) if and only if \(s_j\sim L^{\beta/2}j^{-\beta/2}\). Finally \(b(r)\to L\) implies \(2\Phi(r)/r^2\to L\) by integration. Conversely, if \(2\Phi(r)/r^2\to L\), convexity places \(\Phi'(r)\) between the backward and forward secant slopes on \([(1-\varepsilon)r,r]\) and \([r,(1+\varepsilon)r]\), giving
\[
L(1-\varepsilon/2)\leq\liminf_{r\to\infty}\Phi'(r)/r\leq\limsup_{r\to\infty}\Phi'(r)/r\leq L(1+\varepsilon/2).
\]
Letting \(\varepsilon\downarrow0\) proves the converse. The divergence theorem gives the exact disk-area identity
\[
\frac1{\pi R^2}\int_{|z|<R}\Delta\Phi(|z|)\,dA(z)=\frac{2\Phi'(R)}R,
\]
so one half of the limiting average equals \(L\), finishing the proof.

**Strictness and oscillatory examples.** The smooth weight \(\Phi(r)=r^2/2+\frac15(1-\cos r)\) has Hessian between \(4I/5\) and \(6I/5\), while its radial Hessian eigenvalue \(\Phi''(r)=1+\frac15\cos r\) has no limit; nevertheless \(\Phi'(r)/r\to1\), so its Weyl coefficient is exactly one. For a prescribed nontrivial cluster interval, take
\[
\Phi(r)=\frac{r^2}{2}+\frac1{20}\left[(1+r^2)\bigl(\sin\log(1+r^2)-\cos\log(1+r^2)\bigr)+1\right].
\]
Then \(\Phi'(r)/r=1+\frac15\sin\log(1+r^2)\), its Hessian lies between \(\frac25 I\) and \(\frac85 I\), and the normalized singular values have *exactly* the cluster interval \([(4/5)^{\beta/2},(6/5)^{\beta/2}]\).

## Verification

The self-contained `verify_radial_weyl.py` computes the monomial moment ratios using centered quadrature (avoiding overflow), independently obtains the saddle radii by root solving, and tests the stated local tracking on quadratic, oscillatory-Hessian and oscillatory-slope examples. It also differentiates the explicit oscillatory weight numerically. The executable reports `RADIAL_FOCK_WEYL_MOMENT_CHECKS_OK checks=20`. These are finite numerical consistency checks only. Infinite-dimensional completeness, asymptotic control and the equivalences are proved above analytically; no extrapolation from numerical tests is used as proof.

## Relationship to prior work

Xu and Dong (arXiv:2609.16970, first posted 2026-09-15), Theorems 5.1–5.2, give Weyl constants for quadratic weights and more general principal symbols. Their Proposition 5.3 constructs a radial uniformly Hessian-bounded weight for which no Weyl constant exists, using saddle-point calculations on alternating plateaux, and explicitly asks for weaker asymptotic geometric hypotheses. The present theorem supplies both a necessary-and-sufficient criterion for the entire radial Hessian-bounded class and the exact cluster set even in the nonconvergent case. Their saddle-point estimates motivate, but their stated results do not give, this global characterization.

Bdarneh (arXiv:2609.20652, first posted 2026-09-17), Theorem 6.2, gives the general moment-ratio eigenvalue formula for radial weighted Fock Toeplitz operators; the paper studies invariant algebras and a different slow-weight counterexample to square-root-metric uniform continuity. Its full-text theorem has no Weyl-limit characterization under uniform convexity. Results for classical Gaussian Toeplitz symbols with oscillatory *symbols*, rather than the fixed symbol and variable *weights* here, do not determine the claimed geometric equivalence. Literature searches did not establish a broader theorem that already implies the result; that uncertainty remains subject to independent expert verification.

## Limitations

The one-complex-variable radial assumption, global two-sided Hessian bounds, and fixed positive regularly decaying symbol are essential to the stated theorem. The quantitative remainder depends on these bounds and need not remain uniform for degenerating weights. The result does not establish a nonradial Weyl theorem, exact asymptotics for arbitrary symbols, a general multidimensional weight criterion, or independent originality certification. The primary motivating paper already proves some special quadratic and nonconvergent cases. The present claim is restricted to the full radial iff/cluster characterization and tracking estimate.

## References

1. C. Xu and J. Dong, *IDA symbols and Schatten–Lorentz theory for Toeplitz operators on weighted Fock spaces*, arXiv:2609.16970v1 (2026-09-15), especially §5, Theorems 5.1–5.2 and Proposition 5.3. https://arxiv.org/html/2609.16970
2. K. Bdarneh, *Toeplitz C*-algebras on radially weighted Fock spaces: commutativity and spectral representation*, arXiv:2609.20652 (first posted 2026-09-17), especially Theorem 6.2 and §9. https://arxiv.org/abs/2609.20652
3. S. Looi, *The Berezin liminf criterion fails for radial Toeplitz operators*, arXiv:2603.10879 (2026-03-11); related radial-symbol oscillations in the classical Gaussian/Bergman setting, a different question. https://arxiv.org/abs/2603.10879
