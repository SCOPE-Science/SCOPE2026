# Infinite nonreal zeros throughout the subunit Le Roy family

## Finding
Let \(F_p(z)=\sum_{n=0}^{\infty}z^n/(n!)^p\) for any real \(p>0\). For every \(0<p<1\), \(F_p\) has infinitely many zeros and no real zeros. These zeros form infinitely many nonreal conjugate pairs. The negative-ray restriction \(x\mapsto F_p(-x)\) is strictly completely monotone, \(F_p(-x)\to0\), yet
\[
\int_0^\infty F_p(-x)\,dx=\infty.
\]
Combined with the previously established infinite-zero theorem for \(p>1\), this characterizes \(p=1\) as the only zero-free parameter among \(p>0\). The substantive new range is \(0<p<1\), including reciprocal-integer parameters.

## Assumptions and scope
All exponents \(p\) are real and strictly positive, and all zeros are finite complex zeros, counted distinctly unless specified. Complete monotonicity means that \((-1)^k(d/dx)^kF_p(-x)>0\) for every integer \(k\ge0\) and all \(x>0\). The Euler constant is denoted \(\gamma_{\mathrm E}\). We use the classical Hadamard factorization theorem for finite-order entire functions and the Lévy–Khintchine existence theorem for infinitely divisible probability laws.

## Proof
**Lemma (inverse-moment obstruction).** Let \(X\) be a strictly positive random variable with \(\mathbb E e^{aX}<\infty\) for every \(a>0\) and \(\mathbb E[X^{-1}]=\infty\). Suppose the entire function \(M(z)=\mathbb E e^{zX}\) has finite order. Then \(M\) has infinitely many zeros.

Indeed, \(0<M(-x)\le1\) for \(x\ge0\), and dominated convergence gives \(M(-x)\to0\) as \(x\to\infty\), because \(X>0\) almost surely. Tonelli's theorem gives
\[
\int_0^\infty M(-x)\,dx=\mathbb E\left[\int_0^\infty e^{-xX}\,dx\right]=\mathbb E[X^{-1}]=\infty.
\]
If \(M\) had finitely many zeros, Hadamard factorization would give \(M(z)=P(z)e^{Q(z)}\) for polynomials \(P,Q\) with \(P\not\equiv0\). Because \(M\) has real Taylor coefficients, its zero multiset is conjugation-invariant, and \(P\) may be chosen real up to a nonzero constant. Since \(M(-x)>0\), the quotient \(M(-x)/P(-x)\) has a fixed nonzero real sign for all \(x\ge0\). Consequently all nonconstant coefficients of \(Q\) are real: the imaginary part of \(Q(-x)\) is constant modulo \(\pi\) on a connected interval. Thus \(\operatorname{Re}Q(-x)\) is a real polynomial. If it is nonconstant, its leading sign is either positive, forcing \(M(-x)\to\infty\), or negative, making \(M(-x)\) integrable at infinity. Both contradict the previous limits. If it is constant, \(M\) is a polynomial times a nonzero constant, also incompatible with \(M(-x)\to0\). The lemma follows.

Fix \(0<p<1\) and set \(\tau=1-p\in(0,1)\). The classical Gamma-function Lévy–Khintchine identity, valid for every real \(s>-1\), reads
\[
\log\Gamma(1+s)=-\gamma_{\mathrm E}s+\int_0^\infty\bigl(e^{-su}-1+su\bigr)\frac{du}{u(e^u-1)}.
\]
Its Lévy measure on the negative real axis is the pushforward of \(du/[u(e^u-1)]\) under \(u\mapsto-u\); it satisfies \(\int(1\wedge u^2)\,d\nu<\infty\). Hence Lévy–Khintchine, applied with intensity \(\tau\), yields a real random variable \(Y_\tau\) such that
\[
\mathbb E e^{sY_\tau}=\Gamma(1+s)^\tau,\qquad s>-1.
\]
This may equivalently be obtained as the \(\tau\)-time marginal of the infinitely divisible law of the logarithm of a unit exponential random variable. Put \(X=e^{Y_\tau}>0\). Then for each integer \(n\ge0\),
\[
\mathbb E[X^n]=(n!)^\tau.
\]
As \(p>0\), the ratio test gives convergence of \(\sum_{n\ge0}a^n/(n!)^p\) for every real \(a>0\). Tonelli and absolute convergence therefore show
\[
\mathbb E e^{aX}=\sum_{n=0}^\infty\frac{a^n}{(n!)^p}<\infty,\qquad
\mathbb E e^{zX}=F_p(z)\quad(z\in\mathbb C).
\]
For \(0<q<1\), the Gamma identity gives
\[
\mathbb E[X^{-q}]=\Gamma(1-q)^\tau\longrightarrow\infty\quad(q\uparrow1).
\]
Because \(X^{-q}\le1\) on \(\{X>1\}\), the truncated integrals \(\mathbb E[X^{-q}\mathbf1_{\{X\le1\}}]\) also diverge, and monotone convergence there proves \(\mathbb E[X^{-1}]=\infty\). Finally, Stirling's formula applied to the coefficients \(1/(n!)^p\) yields the exact finite entire order \(\rho(F_p)=1/p\). The inverse-moment lemma now gives infinitely many zeros of \(F_p\).

On the real positive axis each term of the defining power series is nonnegative, so \(F_p(x)>0\) for \(x\ge0\). On the negative axis \(F_p(-x)=\mathbb E e^{-xX}>0\). Derivatives under the integral are justified for every \(x>0\), with
\[
(-1)^k\frac{d^k}{dx^k}F_p(-x)=\mathbb E[X^k e^{-xX}]>0\quad(k=0,1,2,\ldots),
\]
so complete monotonicity is strict. Real coefficients force all nonreal zeros to occur in conjugate pairs. The previous Tonelli identity gives nonintegrability on the negative ray.

At \(p=1\), \(F_1(z)=e^z\), hence it is zero-free. For \(p>1\), infinitely many zeros follow from the theorem of Rosas (arXiv:2510.10054, Theorem 3.1). Thus exactly one positive real parameter is zero-free.

## Verification
The Gamma Lévy exponent is valid for \(s>-1\): near \(u=0\) its compensated integrand is bounded, while at infinity it behaves as \(e^{-(1+s)u}/u\) plus integrable lower-order terms. The associated Lévy measure has the required second-moment integrability near the origin. Strict positivity of the representing random variable is immediate from exponentiation. The Mellin pole at \(s=-1\) entails infinite reciprocal moment using truncation to \(X\le1\), not an invalid direct interchange of nonmonotone negative moments. Hadamard factorization applies because \(\rho(F_p)=1/p<\infty\). The proof is complete analytically and does not rely on finite numerical root plots.

## Relationship to prior work
Rosas (2025, arXiv:2510.10054v1) proves infinitely many zeros of the Le Roy series for \(p>1\) using a coefficient-growth theorem; its hypothesis fails for \(p<1\), and that paper does not handle the subunit case. Simon (2021, arXiv:2012.11018v2) proves complete monotonicity and Gamma-moment representations for a larger three-parameter Le Roy family. These established facts motivate, but do not state, the present infinitely-many-nonreal-zeros conclusion for \(0<p<1\) or the inverse-moment zero criterion. The classical order observation alone settles nonreciprocal-integer \(1/p\), but cannot settle \(p=1/m\) for integers \(m\ge2\). Earlier special-function surveys focus on integral representations, moment properties and asymptotics rather than this complete zero-free parameter classification.

## Limitations
This result does not locate individual nonreal zeros, determine their multiplicities or prove a density asymptotic. It treats real positive \(p\), not arbitrary complex exponents or generalized Le Roy parameters. The complete-monotonicity component is previously known; its use in the infinite-zero argument and the resulting subunit zero classification are the claimed additions. Historical priority outside the inspected sources remains uncertain; no independent audit has been performed.

## References
1. A. Rosas, *If \(\sum n!c_nz^n\) is entire and \(c_n\) does not terminate, then \(\sum c_nz^n\) has infinitely many zeros*, arXiv:2510.10054v1 (first public 2025-10-11), Sections 1 and 3, especially Theorem 3.1. https://arxiv.org/html/2510.10054v1
2. T. Simon, *Remark on a Mittag-Leffler function of Le Roy type*, arXiv:2012.11018v2 (2021), Sections 1–3. https://arxiv.org/html/2012.11018v2
3. V. Kiryakova et al., *The Generalized Fox–Wright Function: The Laplace Transform, the Erdélyi–Kober Fractional Integral and Its Role in Fractional Calculus*, Mathematics 12 (2024), 1918. https://doi.org/10.3390/math12121918
4. Classical Hadamard factorization and Lévy–Khintchine formula (standard background results).
