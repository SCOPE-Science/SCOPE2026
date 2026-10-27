# Boundary-layer dominance in the norm of Richardson-extrapolated Bernstein operators

## Finding
Let \(B_nf(x)=\sum_{k=0}^n\binom nk x^k(1-x)^{n-k}f(k/n)\) on \(C[0,1]\), and put \(R_n=2B_{2n}-B_n\). For every integer \(n\ge1\), the **sharp** supremum-norm operator constant is
\[
\|R_n\|_{C\to C}=\max_{0\le x\le1}\left[1+2\sum_{k=0}^n\left(b_{n,k}(x)-2b_{2n,2k}(x)\right)_+\right],\quad b_{m,k}(x)=\binom mk x^k(1-x)^{m-k}.
\]
Define the Poisson boundary profile, for \(\lambda\ge0\), by
\[
G(\lambda)=1+2\sum_{k=0}^{\infty}\left(e^{-\lambda}\frac{\lambda^k}{k!}-2e^{-2\lambda}\frac{(2\lambda)^{2k}}{(2k)!}\right)_+,
\]
with the standard convention at \(\lambda=0\). Then \(G\) is continuous and admits a finite global maximum \(\Gamma\), with
\[
\boxed{\lim_{n\to\infty}\|R_n\|_{C\to C}=\Gamma=\max_{\lambda\ge0}G(\lambda)>1.395.}
\]
There is a **strict boundary-vs-bulk gap**. Whenever \(x_n\in[0,1]\) satisfies \(nx_n(1-x_n)\to\infty\), the point-evaluation norm tends to the smaller universal constant
\[
H=1+4\left[\Phi(-\sqrt{\log2})-\Phi(-\sqrt{2\log2})\right]<1.391,
\]
where \(\Phi\) is the standard normal distribution function. Consequently, for any choice \(x_n\) of a maximizing evaluation point, \(n\min(x_n,1-x_n)\) is bounded, bounded away from zero, and all its subsequential limits maximize \(G\). Thus the asymptotically most unstable evaluation points lie in boundary layers of width \(\Theta(n^{-1})\), not in the Gaussian interior.

The explicit witness \(\lambda=7/5\) satisfies
\[
G(7/5)=1-2e^{-28/5}+\frac{48608}{1875}e^{-14/5}-\frac{119}{25}e^{-7/5}>1.395.
\]
In particular \(G(7/5)>H\). The scalar maximizer of \(G\) is not claimed unique or expressed by a closed-form root.

## Assumptions and scope
All functions are continuous and real- or complex-valued on \([0,1]\), with the usual supremum norm. The integer \(n\) is at least one. At evaluation point \(x\), \(\|\delta_xR_n\|\) means the norm of the corresponding bounded linear functional. The convention \(y_+=\max\{y,0\}\) applies only to real \(y\). The result is about the standard equispaced Bernstein operators and the fixed Richardson coefficients \(2,-1\), not arbitrary linear combinations or other node families. The operator \(R_n\) reproduces all quadratic polynomials, since \(B_n(t^2)=x^2+x(1-x)/n\).

## Proof
**1. Finite sharp norm and extremizers.** The knots of \(B_{2n}\) are \(j/(2n)\), \(0\le j\le2n\). In the signed measure representing \(\delta_xR_n\), the mass at odd knot \(j\) is \(2b_{2n,j}(x)\ge0\); the mass at the even knot \(2k\) is \(2b_{2n,2k}(x)-b_{n,k}(x)\). The signed masses sum to \(2-1=1\). Their total variation is therefore one plus twice the total negative mass, yielding the claimed finite sum. Every choice of signs on these finitely many knots extends by piecewise-linear interpolation to a continuous function of supremum norm one. Hence total variation is genuinely attained for each evaluation point; maximizing over the compact interval proves sharpness. Reflection \(x\mapsto1-x\) preserves the value.

**2. Poisson boundary limit.** If \(nx_n\to\lambda<\infty\), then \(x_n\to0\). The two binomial mass functions \(b_{n,k}(x_n)\) and \(b_{2n,j}(x_n)\) converge in total variation on the nonnegative integers to independent *marginal laws* of Poisson means \(\lambda\) and \(2\lambda\), respectively (the laws do not need a coupling). The map from these laws to the sum of positive differences is continuous in \(\ell^1\). Thus \(\|\delta_{x_n}R_n\|\to G(\lambda)\). Reflection gives the same statement near the right endpoint. Poisson probabilities depend continuously in total variation on their mean, so \(G\) is continuous.

**3. Gaussian bulk limit.** Set \(\sigma_n^2=nx_n(1-x_n)\to\infty\) and \(z_k=(k-nx_n)/\sigma_n\). Stirling's formula uniformly for bounded \(z_k\), including triangular arrays with \(x_n\to0\), gives
\[
\sigma_n b_{n,k}(x_n)=\phi(z_k)+o(1),\qquad
2\sigma_n b_{2n,2k}(x_n)=\sqrt2\,\phi(\sqrt2z_k)+o(1),
\]
where \(\phi(z)=e^{-z^2/2}/\sqrt{2\pi}\). Uniformity follows because both \(nx_n\) and \(n(1-x_n)\) tend to infinity. For the tails \(|z_k|>A\), the positive difference is at most \(b_{n,k}(x_n)\), and Chebyshev's inequality bounds its total mass by \(A^{-2}\). The mesh in \(z\) is \(1/\sigma_n\). Apply Riemann summation for bounded \(z\), then send \(A\) to infinity:
\[
\|\delta_{x_n}R_n\|\to1+2\int_{\mathbb R}\left(\phi(z)-\sqrt2\phi(\sqrt2z)\right)_+\,dz=H.
\]
The sign changes exactly at \(|z|=\sqrt{\log2}\), establishing the displayed \(\Phi\)-formula. The identical Poisson local central limit theorem, with the same tail argument, proves \(G(\lambda)\to H\) as \(\lambda\to\infty\).

**4. The strict gap.** The elementary monotonicity of \(\phi\) on the positive line gives
\[
H-1=4\int_{\sqrt{\log2}}^{\sqrt{2\log2}}\phi(u)\,du
\le2(\sqrt2-1)\sqrt{\frac{\log2}{\pi}}<0.391.
\]
At \(\lambda=7/5\), the ratio of the negative-subtracted to the positive Poisson mass is
\[
Q_k=\frac{2e^{-2\lambda}(2\lambda)^{2k}/(2k)!}{e^{-\lambda}\lambda^k/k!}
=2e^{-\lambda}\frac{(4\lambda)^k k!}{(2k)!},\qquad
\frac{Q_{k+1}}{Q_k}=\frac{2\lambda}{2k+1}.
\]
Elementary exponential bounds give \(Q_0<1<Q_1,Q_2\) and \(Q_3<1\); the displayed ratio is below one for all \(k\ge2\). Thus the *only* negative signed masses occur at \(k=1,2\). Using \(\sum_{k\ge0}(p_\lambda(k)-2p_{2\lambda}(2k))=-e^{-4\lambda}\), the positive-mass formula simplifies to the displayed elementary expression for \(G(7/5)\). Rational Taylor bounds for exponentials certify \(G(7/5)>1.395\), as demonstrated by the standalone checker. Hence \(G(7/5)>H\).

**5. Global asymptotic and optimizer location.** The limit \(G(\lambda)\to H<G(7/5)\), together with continuity, implies \(G\) attains its maximum \(\Gamma\) on a bounded interval. For each fixed \(\lambda\), setting \(x_n=\lambda/n\) proves \(\liminf_n\|R_n\|\ge G(\lambda)\), so \(\liminf_n\|R_n\|\ge\Gamma\). Conversely choose maximizing evaluation points \(x_n\), reflected into \([0,1/2]\), and extract a subsequence realizing the limsup. Along a further subsequence, either \(nx_n\to\lambda<\infty\) (limit \(G(\lambda)\le\Gamma\)) or \(nx_n\to\infty\) (bulk limit \(H<\Gamma\)). Thus \(\limsup_n\|R_n\|\le\Gamma\). The same dichotomy rules out unbounded maximizing \(nx_n\); it also rules out a zero limit since \(G(0)=1<\Gamma\). Every cluster point must attain \(\Gamma\).

## Verification
Run `python check.py` using only the Python standard library. It independently enumerates **all sign assignments** at the nodes for several small degrees and rational evaluation points, verifies the exact finite formula using rational arithmetic, certifies the sign pattern at \(\lambda=7/5\), rigorously encloses the required exponentials by rational Taylor bounds, and compares the finite binomial profiles with the limiting constants numerically at degrees 20, 50, 100, 250, and 500. These finite tests are consistency checks: the infinite assertions are established in Steps 2–5, not inferred from the numerical tests.

## Relationship to prior work
Butzer's classical work, *Linear Combinations of Bernstein Polynomials* (1953), explicitly introduced the same two-level acceleration \(2B_{2n}-B_n\) and analyzed smooth-function approximation orders and sharp approximation orders for Lipschitz data. It did **not**, in the inspected full text (pp.559–567), compute the induced sharp supremum operator norm or the Poisson-boundary versus Gaussian-bulk separation here. Lu and Zhang (2010, arXiv:1007.1044) consider *modified, weighted* Bernstein combinations for singular functions and prove direct and inverse approximation statements. Their Theorem 1 and its proofs, inspected in the arXiv full text, do not give this exact unweighted endpoint norm or the boundary/bulk asymptotic. Other subsequent studies of Bernstein combinations similarly focus on approximation estimates. The present statement concerns worst-case bounded-input stability, a different quantity from smooth-function approximation error. This is a comparison of precise implications, not an inference from search-result titles.

## Limitations
The constant \(\Gamma\) is characterized as a convergent scalar Poisson variational problem; uniqueness of its maximizer and a closed elementary expression are **not** established. The numerical estimate \(\Gamma\approx1.3953\) is only exploratory and is not used in the proof. The proof does not address arbitrary extrapolation coefficients. The full text of a relevant 2022 two-Bernstein-combination paper could not be obtained; unindexed earlier operator-norm calculations remain a residual originality risk. The 1953 predecessor's publication year is documented, but not an exact first-public calendar day. The earliest precisely dated source in this report is the first arXiv posting on July 7, 2010, not the date the underlying construction was introduced.

## References
1. P. L. Butzer, *Linear Combinations of Bernstein Polynomials*, Canadian Journal of Mathematics **5** (1953), 559–567, DOI `10.4153/CJM-1953-063-7`. Full text: `https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4D868C3C54B8A7676EB3C1AD535AC34A/S0008414X00044278a.pdf/linear_combinations_of_bernsteinpolynomials.pdf`.
2. Shunsheng Guo, Cuixiang Li, Xiwu Liu, and Zhanjie Song, *Pointwise Approximation for Linear Combinations of Bernstein Operators*, Journal of Approximation Theory **107** (2000), 109–120, DOI `10.1006/jath.2000.3504` (abstract inspected; full text inaccessible).
3. Wen-ming Lu and Lin Zhang, *Another weighted approximation of functions with singularities by combinations of Bernstein operators*, arXiv `1007.1044`, first public July 7, 2010, `https://arxiv.org/abs/1007.1044`. Public version 5 examined, with introduction and main-results section examined in full text.
4. Lu Wenming, *Pointwise weighted approximation of functions with inner singularities by Bernstein operators*, Journal of Progressive Research in Mathematics **7** (2016), published April 20, 2016, `https://scitecresearch.com/ojs-3.2.1-5/index.php/jprm/article/view/484` (dated bibliographic record; full text inaccessible).
5. Gancho Tachev, *Linear combinations of two Bernstein polynomials*, Mathematical Foundations of Computing **6** (2023), 586–590, DOI `10.3934/mfc.2022061` (abstract inspected, December 27, 2022 online publication; full text inaccessible).
