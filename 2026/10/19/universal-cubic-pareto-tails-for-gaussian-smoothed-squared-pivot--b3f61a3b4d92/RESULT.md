# Universal cubic Pareto tails for Gaussian-smoothed squared-pivot randomized LU

## Finding

Let \(m,n\ge2\). For a real \(m\)-by-\(n\) matrix \(A\) whose entries are independent standard Gaussians, perform one step of exact randomly pivoted LU (RPLU): conditionally on \(A\), choose a pivot \((I,J)\) with probability \(|A_{ij}|^2/\|A\|_F^2\) and retain the Schur complement \(R\) outside the pivot row and column. Put \(Z=\|R\|_F\). Then
\[
\lim_{t\to\infty}t^3\Pr(Z>t)=C_{m,n}
=\frac{16mn}{3(mn+3)\sqrt{2\pi}}
\frac{\Gamma((m+2)/2)}{\Gamma((m-1)/2)}
\frac{\Gamma((n+2)/2)}{\Gamma((n-1)/2)}>0.
\]
More generally, for every deterministic real \(m\)-by-\(n\) matrix \(B\) and every \(\sigma>0\), if \(A=B+\sigma G\) with independent standard-normal entries in \(G\), then \(\lim_{t\to\infty}t^3\Pr(Z>t)=C(B,\sigma)\in(0,\infty)\). For each candidate pivot \((i,j)\), write \(u_{ij}\) and \(v_{ij}\) for the complementary pivot-column and pivot-row vectors, \(W_{ij}\) for the remaining block, and \(S_{ij}=\|u_{ij}\|_2^2+\|v_{ij}\|_2^2+\|W_{ij}\|_F^2\). The coefficient is
\[
C(B,\sigma)=\frac{2}{3\sigma\sqrt{2\pi}}\sum_{i=1}^m\sum_{j=1}^n
e^{-B_{ij}^2/(2\sigma^2)}\mathbb E\left[\frac{(\|u_{ij}\|_2\|v_{ij}\|_2)^3}{S_{ij}}\right].
\]
In particular, any strictly positive independent Gaussian smoothing variance produces a cubic tail, and \(C(0,\sigma)=\sigma^3 C_{m,n}\). For either input model, and every real \(q>0\), \(\mathbb E Z^q<\infty\) if and only if \(q<3\).

For standard Gaussian inputs, \(C_{2,2}=64/(21\pi\sqrt{2\pi})\) and
\[
\mathbb E Z^2=\frac{2m(m-1)n(n-1)}{mn+2}.
\]
The second-moment identity is a consistency check from the established one-step squared-residual analysis, not a new contribution. In contrast, complete-largest-entry pivoting on the same Gaussian inputs gives finite residual moments of all positive orders.

## Assumptions and scope

For the general theorem \(A=B+\sigma G\) with arbitrary deterministic \(B\), fixed \(\sigma>0\), and independent standard-normal entries in \(G\), with fixed integers \(m,n\ge2\). The closed gamma-function coefficient and displayed mean-square formula specialize to \(B=0,\sigma=1\). Unless conditioned on \(A\), expectations average jointly over the input and pivot selection. Pivoting uses exact entry-square probabilities, with no approximations, repeat pivots, or finite-precision effects. Under either Gaussian law all entries are nonzero almost surely. No full-factorization or multi-step claim is made.

## Proof

**1. Weighted pivot integral.** Fix a candidate pivot and permute its row and column into first position. Partition
\[
A=\begin{pmatrix}X&v^{\mathsf T}\\ u&W\end{pmatrix},\qquad
S=\|u\|_2^2+\|v\|_2^2+\|W\|_F^2,\qquad h=\|u\|_2\|v\|_2,\qquad w=\|W\|_F.
\]
The pivot \(X\) is independent of the complement and has Gaussian density \(f\) of mean \(B_{ij}\) and variance \(\sigma^2\). The Schur complement is \(W-uv^{\mathsf T}/X\). The contribution of this candidate to \(\Pr(Z>t)\) is the expectation over the complement of
\[
\int_{\mathbb R}f(x)\frac{x^2}{x^2+S}
\mathbf 1\{\|W-uv^{\mathsf T}/x\|_F>t\}\,dx .
\]
The total tail is the sum of these contributions over the finitely many pivots. For standard Gaussian input the contributions are equal by symmetry. In particular, the pivot-selection weight belongs inside the integral.

**2. Evaluate the limit.** The norm inside the event differs from \(h/|x|\) by at most \(w\). For \(t>w\), the event lies between \(\{|x|<h/(t+w)\}\) and \(\{|x|<h/(t-w)\}\), disregarding null endpoints. Almost surely \(h,S>0\). Since \(f\) is continuous at zero, both bounding integrals multiplied by \(t^3\) converge to \(2f(0)h^3/(3S)\). For \(w\le t/2\), the multiplied integral is bounded by \(16\|f\|_\infty h^3/(3S)\). Since \(h\le S/2\), \(h^3/S\le S^2/8\), which is integrable. The contribution of \(w>t/2\) is bounded by \(\Pr(w>t/2)=o(t^{-3})\), using Gaussian norm moments, so dominated convergence is valid. Substituting the Gaussian density at zero and summing gives \(C(B,\sigma)\). Each term is positive and finite for \(m,n\ge2\), and scaling the entire centered matrix by \(\sigma\) scales \(Z\) by \(\sigma\) without altering pivot probabilities.

**3. Evaluate the centered coefficient.** Let \(a=m-1\), \(b=n-1\), \(c=(m-1)(n-1)\) and \(D=a+b+c=mn-1\). For a standard Gaussian input, \(U=\|u\|_2^2\), \(V=\|v\|_2^2\) and \(H=\|W\|_F^2\) are independent chi-squared variables with degrees of freedom \(a,b,c\). Their sum \(S\sim\chi_D^2\) is independent of the Dirichlet proportions \((U/S,V/S,H/S)\) of parameters \((a/2,b/2,c/2)\). The gamma integral gives
\[
\begin{aligned}
\mathbb E[h^3/S]
&=D(D+2)\frac{\Gamma(D/2)}{\Gamma(D/2+3)}
  \frac{\Gamma((a+3)/2)}{\Gamma(a/2)}\frac{\Gamma((b+3)/2)}{\Gamma(b/2)}\\
&=\frac{8}{mn+3}\frac{\Gamma((m+2)/2)}{\Gamma((m-1)/2)}
  \frac{\Gamma((n+2)/2)}{\Gamma((n-1)/2)}.
\end{aligned}
\]
Multiplying by \(2mn/(3\sqrt{2\pi})\) yields \(C_{m,n}\). Substitution of \(m=n=2\) gives the stated special value.

**4. Moment frontier.** Layer cake gives \(\mathbb E Z^q=q\int_0^\infty t^{q-1}\Pr(Z>t)\,dt\) for \(q>0\), including infinite values. With a positive finite cubic tail coefficient the integral converges precisely for \(q<3\), and diverges logarithmically at \(q=3\).

**5. Mean square and complete pivoting.** For a fixed matrix with no zero entries, each squared pivot cancels the residual denominator when multiplied by its pivot selection weight. Every squared \(2\)-by-\(2\) minor is counted for its four choices of pivot corner, and hence
\[
\mathbb E[Z^2\mid A]=\frac{4}{\|A\|_F^2}\sum_{i<k}\sum_{j<\ell}
(A_{ij}A_{k\ell}-A_{i\ell}A_{kj})^2.
\]
For an arbitrary fixed nonzero matrix with zero entries, only nonzero pivot corners contribute: the factor 4 in each term must instead be the number of nonzero entries of that minor's \(2\)-by-\(2\) submatrix. This follows by summing the cancellation identity only over nonzero pivots. In the Gaussian model the factor 4 applies almost surely. On a standard Gaussian matrix, every squared minor determinant has mean 2. This square is homogeneous of degree four in the \(mn\) entries. Since the Gaussian radius \(r=\|A\|_F\) and direction are independent and \(\mathbb E r^4/\mathbb E r^2=mn+2\), dividing the determinant square by \(\|A\|_F^2\) gives expectation \(2/(mn+2)\). Summing yields the mean square in the Finding.

With largest-entry pivoting, every entry in \(u,v\) has magnitude at most \(|X|\) and \(|X|\le\|A\|_F\). The residual norm is then bounded by
\[
\|W\|_F+\frac{\|u\|_2\|v\|_2}{|X|}
\le (1+\sqrt{(m-1)(n-1)})\|A\|_F.
\]
Gaussian input norm moments are finite at every positive order.

## Verification

The supplied `reproduce.py` (Python 3 with NumPy and SciPy) checks the \(2\)-by-\(2\) coefficient numerically from its gamma form and the oriented-minor identity on Gaussian rectangular inputs, and compares sample squared residuals and scaled tail frequencies with their predicted values in three centered sizes. It does not certify the tail limit, moment divergence, or general noncentral coefficient. The results here follow from the analytic proof.

## Relationship to prior work

Gilles and Wilber introduced squared-entry RPLU and derived conditional expected squared-error bounds, including the one-step Gram-matrix calculation. Divan and Gilles analyzed approximate pivot distributions and spectral convergence through determinant identities. Those analyses concern pivot randomness for fixed inputs, where the finite support of selected nonzero pivots makes all residual moments finite. The theorem here analyzes the joint input/pivot law; the fixed-matrix conditional mean-square result alone cannot determine the sharp tail or integrability of moments of order three. Spielman and Yu's Gaussian growth bounds concern conventional partial pivoting, which uses a different rule.

## Limitations

This is a one-step, exact-arithmetic result for independent additive real Gaussian entry noise with fixed positive standard deviation; the closed gamma coefficient additionally assumes the underlying matrix is zero. It is not a uniform statement as the smoothing variance goes to zero, a multi-step convergence rate, a high-probability relative-error estimate, or a finite-precision growth theorem. The failure of higher moments is unconditional over random matrices, not conditional on a fixed nonzero matrix. Equivalent formulations in unexamined literature remain possible.

## References

1. M. A. Gilles and H. Wilber, *Low-Rank Approximation by Randomly Pivoted LU*, arXiv:2601.22344v1 (2026-01-29), https://arxiv.org/abs/2601.22344.
2. R. Divan and M. A. Gilles, *Convergence rates of randomly pivoted methods for low-rank approximations*, arXiv:2609.06287v1 (2026-09-05), https://arxiv.org/abs/2609.06287.
3. D. A. Spielman and S. H. Yu, *Large Growth Happens: Gaussian Elimination with Partial Pivoting on Random Matrices*, arXiv:2610.08701v1 (2026-10-06), https://arxiv.org/abs/2610.08701.
