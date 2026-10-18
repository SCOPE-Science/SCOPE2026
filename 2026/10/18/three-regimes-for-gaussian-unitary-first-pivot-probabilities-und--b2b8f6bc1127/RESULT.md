# Three regimes for Gaussian-unitary first-pivot probabilities under planar \(\ell^q\) norms

## Finding
Let \(A\) be an \(n\)-by-\(n\) Gaussian unitary ensemble matrix with \(A_{11}\sim N(0,1)\) and independent first-column off-diagonal entries \(A_{j1}=(X_j+iY_j)/\sqrt2\), where the real coordinates are independent standard normals. For \(1\le q<\infty\), compare a complex candidate \(z=x+iy\) using \(\|z\|_q=(|x|^q+|y|^q)^{1/q}\), and for \(q=\infty\) use \(\|z\|_\infty=\max(|x|,|y|)\). Define \(p_{n,q}\) as the probability that the diagonal candidate wins the first-column comparison without a row swap.

For every fixed \(q\in[1,\infty]\), as \(n\to\infty\), the following **sharp equivalents** hold:

\[
\boxed{p_{n,q}\sim K_q n^{-\alpha_q}(\log n)^{(\alpha_q-1)/2},\quad 1\le q<2,}
\]
\[
\alpha_q=2^{2/q-2},\qquad
K_q=\frac{2^{1/q-1/2}\Gamma(\alpha_q)}{\sqrt{2\pi}}
\left(\frac{\sqrt{\pi(2-q)}}2\right)^{\alpha_q};
\]
\[
\boxed{p_{n,2}\sim\frac1{\sqrt{2n\log n}};}
\]
\[
\boxed{p_{n,q}\sim\frac{\pi^{1/4}}2\frac1{\sqrt n(\log n)^{1/4}},\quad 2<q\le\infty.}
\]
The last equivalent has the **same leading constant for every fixed exponent above two**, including the maximum norm; the logarithmic order changes exactly at the Euclidean exponent. For every integer \(n\ge2\), \(p_{n,q}\) is strictly increasing with \(q\). At \(q=1\) the first formula specializes to the exact known identity \(p_{n,1}=1/(2n-1)\).

## Assumptions and scope
The ensemble is the standard GUE scaling described above; any common positive scaling of the entire matrix leaves the first comparison unchanged. In this statement \(q\) is fixed before \(n\) grows. No assertion of uniformity in exponents approaching two is made. Only the *initial* pivot comparison is studied; the full elimination permutation and subsequent Schur-complement pivots are outside the claim. Zero-probability ties may be resolved arbitrarily. The primary probability object is the comparison of a half-normal diagonal entry against the maximum of independent planar Gaussian norms.

## Proof
**1. Exact reduction to an angular tail.** Let \(Z,Z_1,Z_2\) be independent real standard normals and set
\[
R_q=\frac{\|(Z_1,Z_2)\|_q}{\sqrt2},\qquad
W_q(\theta)=\begin{cases}(|\cos\theta|^q+|\sin\theta|^q)^{1/q},&q<\infty,\\\max(|\cos\theta|,|\sin\theta|),&q=\infty.\end{cases}
\]
Writing \(S_q(x)=\mathbb P(R_q>x)\) and using the independent polar radius and uniform angle of a planar Gaussian, whose radial survival probability is \(\exp(-r^2/2)\), gives the exact integral
\[
S_q(x)=\frac1{2\pi}\int_0^{2\pi}\exp\left(-\frac{x^2}{W_q(\theta)^2}\right)d\theta
=\frac4\pi\int_0^{\pi/4}\exp\left(-\frac{x^2}{W_q(\theta)^2}\right)d\theta.
\]
Since the first-column off-diagonal candidates are independent of \(A_{11}\),
\[
p_{n,q}=\sqrt{\frac2\pi}\int_0^\infty e^{-x^2/2}(1-S_q(x))^{n-1}\,dx.\tag{1}
\]
The function \(S_q\) is continuous and strictly decreasing from one to zero.

**2. The three angular saddle types.** For \(1\le q<2\), the unique maximum in the fundamental quadrant occurs at \(\theta=\pi/4\), with value \(u_q=2^{1/q-1/2}\). Direct differentiation at that point gives
\[
(\log W_q)''(\pi/4)=q-2,
\qquad
\frac1{W_q(\pi/4+t)^2}=u_q^{-2}\bigl(1+(2-q)t^2+o(t^2)\bigr).
\]
By the endpoint form of Laplace's method on the fundamental quadrant, or by summing the four full interior maxima on the circle,
\[
S_q(x)\sim \frac{2u_q}{\sqrt{\pi(2-q)}}\,x^{-1}\exp(-x^2/u_q^2).\tag{2}
\]
The derivative is legitimate for \(q=1\) in a neighborhood of the diagonal saddle, since neither coordinate vanishes there. The maximizer is isolated and the remaining angular region is exponentially negligible.

At \(q=2\), \(W_2\equiv1\), hence the **exact** survival probability is
\[
S_2(x)=e^{-x^2}.\tag{3}
\]
For each fixed \(2<q<\infty\), the maxima occur at the four coordinate axes and have value one. Near an axis,
\[
W_q(t)=1-\tfrac12t^2+o(t^2),\qquad W_q(t)^{-2}=1+t^2+o(t^2).
\]
The same expansion holds for \(q=\infty\), since \(W_\infty(t)=\cos t\) near zero. Consequently the four Gaussian saddles yield
\[
S_q(x)\sim \frac2{\sqrt\pi}\,x^{-1}e^{-x^2},\qquad 2<q\le\infty.\tag{4}
\]
Notice that neither the curvature nor the number of maximizing angles depends on \(q\) in this last regime. For \(2<q<3\), the expansion uses only the existence of the second derivative at the axes; higher smoothness is unnecessary.

**3. Tail-to-pivot transfer with the constant.** More generally, assume for fixed \(a,C>0\) and \(\beta\ge0\) that a continuous decreasing survival function obeys
\[
S(x)\sim Cx^{-\beta}e^{-ax^2}\quad(x\to\infty).
\]
Set \(X=|Z|\), \(U=S(X)\), \(\alpha=(2a)^{-1}\), and \(\gamma=(\beta\alpha-1)/2\). If \(x_s=S^{-1}(s)\), then \(x_s\sim\sqrt{\log(1/s)/a}\). Using the half-normal Mills ratio and the displayed tail relation,
\[
\mathbb P(U\le s)=\mathbb P(X\ge x_s)
\sim\sqrt{\frac2\pi}\,C^{-\alpha}a^{(1-\beta\alpha)/2}s^\alpha
\bigl(\log(1/s)\bigr)^\gamma.\tag{5}
\]
For clarity, the decisive substitution is
\(e^{-x_s^2/2}=(s x_s^\beta/C)^\alpha(1+o(1))\); the additional factor \(x_s^{-1}\) comes from Mills' ratio. Integration by parts gives
\[
\mathbb E(1-U)^{n-1}=(n-1)\int_0^1\mathbb P(U\le s)(1-s)^{n-2}\,ds.
\]
Applying the elementary Abelian limit for a regularly varying distribution function at zero (substitute \(t=ns\) and dominate using two-sided power bounds for the logarithmic factor) proves
\[
\mathbb E(1-U)^{n-1}\sim
\Gamma(\alpha+1)\sqrt{\frac2\pi}\,
C^{-\alpha}a^{(1-\beta\alpha)/2}
 n^{-\alpha}(\log n)^\gamma.\tag{6}
\]
The domination is valid for every \(\alpha>0\), since choose a Potter exponent smaller than \(\alpha\), use \((1-s)^{n-2}\le e^{-(n-2)s}\) away from zero, and bound the fixed upper tail exponentially. Thus no unexplained interchange of a divergent integral is used.

**4. Substitution and exact endpoints.** In equation (2) choose \(a=u_q^{-2}\), \(\beta=1\), \(C=2u_q/\sqrt{\pi(2-q)}\), giving \(\alpha_q=u_q^2/2=2^{2/q-2}\). Equation (6), with \(\Gamma(\alpha+1)=\alpha\Gamma(\alpha)\), simplifies to the stated \(K_q\). In equation (3), \(a=C=1\) and \(\beta=0\), yielding \(1/\sqrt2\) and logarithmic exponent \(-1/2\). In equation (4), \(a=1\), \(\beta=1\), \(C=2/\sqrt\pi\), yielding \(\pi^{1/4}/2\) and exponent \(-1/4\).

For \(q=1\), the identity \(|z_1|+|z_2|=\max(|z_1+z_2|,|z_1-z_2|)\) and orthogonal Gaussian invariance reduce the first pivot event to one absolute standard normal being the largest among \(2n-1\) independent absolute standard normals. This proves \(p_{n,1}=1/(2n-1)\), independently checking the leading constant. For finite \(n\), the planar \(\ell^q\) norm of a vector with both coordinates nonzero strictly decreases as \(q\) increases, and the independent half-normal diagonal candidate has a positive density at every positive value. Therefore \(q\mapsto p_{n,q}\) is strictly increasing, also at the maximum-norm endpoint.

## Verification
The standalone `verify.py` numerically evaluates the exact angular survival integral and the outer pivot integral; checks the six non-Euclidean angular prefactors; cross-checks the exact \(\ell^1\) probability for seven sizes and the \(\ell^2\) binomial-sum formula for three sizes; tests asymptotic normalizations across six exponents; and verifies strict finite-size monotonicity. It completed **28 numerical and endpoint assertions**. This diagnostic does not establish the infinite asymptotics: those follow from saddle expansions, Mills' ratio, and the regularly varying integral argument above. The proof does not use floating-point outputs as a premise.

## Relationship to prior work
Gunawan and Peca-Medlin (2025), *Pivot probabilities and norm effects in Gaussian elimination for \(\beta\)-ensembles*, arXiv:2506.20470, develop the implementation-dependent complex pivot problem at dimension two, explicitly distinguishing the \(\ell^1\) and \(\ell^2\) conventions. Gunawan, Peca-Medlin and Zhong (2026), *Random permutations using GEPP*, arXiv:2610.10481, Proposition 6 and Section 4.1, prove the exact all-size \(\ell^1\) probability and the \(\ell^2\) asymptotic. These are incorporated as established endpoints, not independently new contributions.

The present statement classifies the previously untreated continuum of fixed norm exponents, including the quantitative power-law spectrum below two and the common sharp leading coefficient above two. General Gaussian Laplace asymptotics and regular-variation transfer are classical methods, but neither inspected primary GEPP paper states or proves this norm-indexed phase diagram. Earlier theoretical results with all norm exponents, potentially formulated in terms of extreme-value tails rather than pivoting, remain an originality risk.

## Limitations
The result covers one pivot of dense GUE under a specified norm convention. It does not establish stability or floating-point growth guarantees, a distributional result for the entire elimination permutation, or uniform behavior in a triangular array of exponents \(q=q_n\) approaching two. The rates are sharp for fixed \(q\), but finite-size convergence to the leading constants may be slow, especially near two. General-purpose Gaussian-tail methods could encode overlapping ingredients even when no identically formulated pivot theorem was located.

## References
1. K. Gunawan and J. Peca-Medlin, *Pivot probabilities and norm effects in Gaussian elimination for \(\beta\)-ensembles*, arXiv:2506.20470v1 (first public version June 25, 2025), https://arxiv.org/abs/2506.20470.
2. K. Gunawan, J. Peca-Medlin and C. Zhong, *Random permutations using GEPP*, arXiv:2610.10481v1 (first public version October 7, 2026), https://arxiv.org/abs/2610.10481. Especially Proposition 6, Section 4.1, and Section 5.
