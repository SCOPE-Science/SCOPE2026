# A parity law for optimal single-site Fock jets and their Laguerre radius candidates

## Finding

In the Gaussian Bargmann--Fock space, the best approximation of a high-degree normalized monomial by the value and the first \(k\) derivatives at a freely chosen *single* point exhibits an all-order parity law. For every fixed integer \(k\ge2\), write \(E_{N,k}\) for its maximal squared captured norm. With the probabilists' Hermite polynomials \(\operatorname{He}_j\), put
\[
H_k(y)=e^{-y^2/2}\sum_{j=0}^{k}\frac{\operatorname{He}_j(y)^2}{j!}.
\]
Then
\[
\lim_{N\to\infty}\sqrt{2\pi N}\,E_{N,k}=\max_{y\in\mathbb R}H_k(y).
\]
If \(k\) is even, \(H_k\) has the unique global maximizer \(y=0\). If \(k\) is odd, its only global maximizers are \(y=\pm\rho_{k+1}\), where \(\rho_{k+1}\) is the least positive root of \(\operatorname{He}_{k+1}\). For any maximizing sampling point \(a_N\), the rescaled squared radius \(y_N=(|a_N|^2-N)/\sqrt N\) approaches this indicated maximizer set; conversely, either prescribed limiting branch attains the sharp asymptotic. There are no claims about which of the two branches wins at finite \(N\) for odd \(k\).

An exact finite-degree classification accompanies the limit: for integers \(N>k\), every global maximizing positive squared radius is among the \(k+1\) positive simple roots of \(L_{k+1}^{(N-k-1)}\), and **every one** of these roots is a strict local maximum of the squared captured norm. They alternate with its \(k\) strict local minima. For example, the sharp limiting constants are \(3/2\) at \(k=2\) and
\[
4(3-\sqrt6)\exp\!\left[-\frac{3-\sqrt6}{2}\right]
\]
at \(k=3\), with maximizing offsets \(0\) and \(\pm\sqrt{3-\sqrt6}\), respectively.

## Assumptions and scope

The Hilbert norm is \(\|f\|_{\mathcal F}^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\). Let \(e_N(z)=z^N/\sqrt{N!}\). For \(a\in\mathbb C\) and a nonnegative integer \(k\), define the one-site Hermite-sampling subspace
\[
J_k(a)=\operatorname{span}\{z^j e^{\overline a z}:0\le j\le k\},
\qquad E_{N,k}=\sup_{a\in\mathbb C}\|P_{J_k(a)}e_N\|_{\mathcal F}^2.
\]
Thus \(J_k(a)\) consists of the representing vectors of evaluations \(f(a),f'(a),\ldots,f^{(k)}(a)\). Angles of \(a\) are immaterial by rotational symmetry. The asymptotics keep \(k\) fixed while \(N\to\infty\); they do **not** assert uniformity for growing \(k\), multiple sites, other Fock weights, or finite-degree uniqueness of the best radius.

Define polynomials \(C_j(N;\lambda)\) by
\[
\sum_{j\ge0}\frac{C_j(N;\lambda)}{j!}t^j=(1+t)^N e^{-\lambda t}.
\]
They satisfy \(C_0=1\), \(C_1=N-\lambda\),
\[
C_{j+1}=(N-\lambda-j)C_j-j\lambda C_{j-1},
\qquad \partial_\lambda C_{j+1}=-(j+1)C_j.
\]
We use the convention \(\operatorname{He}_0=1\), \(\operatorname{He}_1(y)=y\), and \(\operatorname{He}_{j+1}(y)=y\operatorname{He}_j(y)-j\operatorname{He}_{j-1}(y)\).

## Proof

**1. Exact projection formula.** The Weyl translation \((W_af)(z)=e^{-|a|^2/2+z\overline a}f(z-a)\) is unitary and sends the span of \(e_0,\ldots,e_k\) onto \(J_k(a)\). Rotational covariance permits \(a=\sqrt\lambda>0\). Extracting the coefficient of \(z^N\) in \(W_ae_j\) gives
\[
|\langle e_N,W_ae_j\rangle|^2
=e^{-\lambda}\frac{\lambda^{N-j}}{N!j!}C_j(N;\lambda)^2.
\]
Consequently the squared projection, denoted \(F_{N,k}(\lambda)\), is
\[
F_{N,k}(\lambda)=\frac{e^{-\lambda}\lambda^N}{N!}
\sum_{j=0}^{k}\frac{C_j(N;\lambda)^2}{j!\lambda^j},\qquad \lambda>0.
\tag{1}
\]
For \(N>k\), its continuous value at \(\lambda=0\) is zero; it also tends to zero as \(\lambda\to\infty\).

**2. All stationary radii exactly.** Differentiate (1), apply the displayed Charlier recurrence and derivative identity, and telescope. The result is
\[
F'_{N,k}(\lambda)=\frac{e^{-\lambda}\lambda^N}{N!}
\frac{C_k(N;\lambda)C_{k+1}(N;\lambda)}{k!\lambda^{k+1}}.
\tag{2}
\]
The generating formula also gives \(C_j(N;\lambda)=j!L_j^{(N-j)}(\lambda)\). As \(N-k-1\ge0\), the \(k+1\) zeros of \(C_{k+1}\) are simple, positive, and increasing. Since \(C'_{k+1}=-(k+1)C_k\), the \(k\) zeros of \(C_k\) interlace the former. At a zero of \(C_{k+1}\), differentiation of (2) once more leaves a strictly negative factor \(-(k+1)C_k^2\), hence a strict local maximum. At a zero of \(C_k\) the sign alternates oppositely, yielding strict local minima. As the two endpoints have value zero, all global maximizers are exactly among the specified positive Laguerre roots (possibly more than one).

**3. Uniform central asymptotics and escape exclusion.** Set \(\lambda=N+y\sqrt N\). In the Charlier generating identity, substitute \(t=s/\sqrt N\) and expand the logarithm, uniformly for \(y,s\) in compact sets:
\[
N\log(1+s/\sqrt N)-(N+y\sqrt N)s/\sqrt N
=-ys-s^2/2+O(N^{-1/2}).
\]
Coefficient comparison for each fixed \(j\) proves \(N^{-j/2}C_j(N;N+y\sqrt N)\to\operatorname{He}_j(-y)\) locally uniformly. Stirling's formula gives \(\sqrt{2\pi N}e^{-\lambda}\lambda^N/N!\to e^{-y^2/2}\) uniformly on the same compacts. Equation (1) then converges to \(H_k(y)\).

For completeness, the maximization cannot escape the central window. On \(N/2\le\lambda\le2N\), recurrence bounds the fixed-degree polynomials by \(|C_j|\le B_k(|N-\lambda|+\sqrt N)^j\). Standard factorial bounds give \(e^{-\lambda}\lambda^N/N!\le B N^{-1/2}\exp[-c(N-\lambda)^2/N]\) for an absolute \(c>0\). Thus the scaled projection is bounded by a polynomial in \(|N-\lambda|/\sqrt N\) times a decaying Gaussian. For \(\lambda\le N/2\), use \(|C_j|\le B_kN^j\) in (1), together with the exponentially small Poisson lower tail, absorbing the finite inverse powers of \(\lambda\) into \(\lambda^{N-j}\); for \(\lambda\ge2N\), use \(|C_j|\le B_k\lambda^j\) and the upper Poisson tail. Both extreme regions contribute \(o(N^{-1/2})\). Consequently every sequence of globally optimal rescaled radii is bounded, and limits maximize \(H_k\).

**4. Global Hermite maximizer classification.** A direct Hermite recurrence calculation yields
\[
H_k'(y)=-\frac{e^{-y^2/2}}{k!}\operatorname{He}_k(y)\operatorname{He}_{k+1}(y).
\tag{3}
\]
The roots of \(\operatorname{He}_{k+1}\) are strict local maxima; those of \(\operatorname{He}_k\) are strict local minima. At a root \(r\) of \(\operatorname{He}_{k+1}\), the Christoffel--Darboux identity reduces to
\[
H_k(r)=\frac{k+1}{k!}e^{-r^2/2}\operatorname{He}_k(r)^2.
\tag{4}
\]
To order these local maxima, let \(w(y)=e^{-y^2/4}\operatorname{He}_{k+1}(y)\). Its differential equation is \(w''+q(y)w=0\) with \(q(y)=k+\tfrac32-y^2/4\). The Sonin quantity \(S=w'^2+qw^2\) satisfies \(S'(y)=-yw(y)^2/2\), strictly decreasing between nonnegative zeros. At a zero \(r\), (4) becomes \(H_k(r)=S(r)/[(k+1)k!]\). Hence the heights at successive nonnegative zeros of \(\operatorname{He}_{k+1}\) strictly decrease. When \(k\) is even, zero is the first such root; when \(k\) is odd, the first positive root and its negative are the nearest roots. Since \(H_k\) tends to zero at infinity, this proves the stated complete parity classification.

For \(k=2\), evaluation at zero gives \(H_2(0)=3/2\). For \(k=3\), the least positive zero of \(\operatorname{He}_4=y^4-6y^2+3\) has squared value \(3-\sqrt6\). Formula (4) gives the displayed constant. The rigorous escape bound above transfers the exact maximizer sets to the asymptotic optimizing sampling radii.

## Verification

The accompanying standard-library program `CHECK.py` checks 42 exact polynomial instances of the derivative identity, the root-count and global-maximality candidate principle for six jet orders at one finite degree, 18 central-limit evaluations for jet orders \(2\) through \(7\), 36 independent shifted-monomial coefficient comparisons, and 45 numerical derivative comparisons. The run completed with `ALL CHECKS PASSED`. These computations illustrate the theorem, while the arguments in the proof establish all infinitely many degrees and jet orders. Run with `python3 CHECK.py`.

## Relationship to prior work

Escudero, Haimi and Romero (arXiv:2004.12922, first public 27 April 2020) study derivative-enhanced Fock sampling via density conditions for infinite sampling sets. Their results motivate multiplicity but do not supply finite one-point optimal radii. Nilsson (arXiv:1202.2557; later journal publication) gives a Charlier-to-Hermite transition and zero convergence, which supplies a known component of the asymptotic analysis; it does not by itself optimize the Fock jet capture. The formula for \(H_k\) is also the standard finite Hermite Christoffel diagonal, or Gaussian-unitary-ensemble one-point density up to normalization. The new claim is the combined Fock approximation extremum, its **finite** Laguerre candidate set, the parity-dependent **global** optimizer locations at all fixed jet orders, and the precise sharp capture constants. The previously obtained first-derivative two-radius law is only the \(k=1\) prototype and is excluded from the present novelty claim.

## Limitations

The order of the jet is fixed as monomial degree tends to infinity; no assertion concerns growing jet order or several sampling sites. The two asymptotic branches at odd jet order are not claimed to be tied at finite degree. The Hermite, Laguerre, Charlier, and Weyl ingredients are classical; the comparative historical novelty of their present optimization synthesis remains subject to independent scholarly review. Numerical experiments are not proof of global maximization. The analysis is within the ordinary one-dimensional Gaussian Fock norm and does not assert the same formulas for non-Gaussian weights.

## References

1. L. A. Escudero, A. Haimi, J. L. Romero, *Multiple Sampling and Interpolation in Weighted Fock Spaces of Entire Functions*, arXiv:2004.12922 (27 April 2020); Complex Analysis and Operator Theory 15, 35 (2021), DOI 10.1007/s11785-020-01065-4. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC7886767/ .
2. M. N. P. Nilsson, *On the Transition of Charlier Polynomials to the Hermite Function*, arXiv:1202.2557 (2012); Constructive Approximation 56, 479--504 (2022), DOI 10.1007/s00365-021-09559-w. Open full text: https://link.springer.com/article/10.1007/s00365-021-09559-w .
3. Classical Laguerre polynomial zero theorem, Hermite recurrence and Christoffel--Darboux kernel identity; standard orthogonal-polynomial facts as explicitly stated and proved where needed above.
