# Exact three-dimensional fourth-order spherical modal spectrum and its two-term logarithmic tail

## Finding
Let \(J_\nu\) be the Bessel function of the first kind and \(P_k\) the Legendre polynomial normalized by \(P_k(1)=1\). For every integer \(k\ge0\), define the convergent fourth-order modal moment
\[
I_k=\int_0^\infty J_{k+1/2}(r)^4\,dr.
\]
Then the entire modal spectrum has the exact finite-polynomial representation
\[
\boxed{I_k=\frac1\pi\int_0^1P_k(1-2x^2)^2\,dx.}
\]
In particular, \(\pi I_k\) is a positive rational number for every \(k\), and
\[
\pi I_0=1,\qquad \pi I_1=\frac7{15},\qquad \pi I_2=\frac{11}{35}.
\]
More sharply, with \(K=k+\tfrac12\), and Euler's constant \(\gamma\), the entire high-harmonic tail obeys the **two-term asymptotic**
\[
\boxed{I_k=\frac{\log K+\gamma+\log32+o(1)}{2\pi^2K}\quad(k\longrightarrow\infty).}
\]
For the unnormalized surface measure on \(\mathbb S^2\), and the Fourier transform \(\widehat{f\sigma}(y)=\int_{\mathbb S^2}e^{-iy\cdot\omega}f(\omega)\,d\sigma(\omega)\), the sharp quadratic deficit coefficient in the radial-\(L^4\), angular-\(L^2\) Fourier extension inequality of Xu (Theorem 1.3, cited below) therefore evaluates **without special-function integrals** to
\[
\boxed{\Gamma_{3,4}=8\pi^{5/2}\bigl(1-\sqrt{7/15}\bigr).}
\]
The sharp-stability statement and its equality cases are those of the cited theorem; the newly derived part is the exact evaluation and full two-term modal spectral law, not a new proof of the general inequality.

## Assumptions and scope
The integer \(k\) ranges over every nonnegative degree, including \(k=0\); no other parameters enter the modal identity. The asymptotic is for \(k\to\infty\) with the degree-half-integer \(K=k+1/2\). The use of \(\Gamma_{3,4}\) concerns dimension \(3\), radial exponent \(4\), unnormalized sphere measure, and the Fourier convention displayed above. This exponent lies in the admissible range \(4>3\). The modal moments correspond precisely to \(I_{\nu,k}(q)\) in Xu's notation with \(\nu=1/2\), \(q=4\).

## Proof
**1. Exact moments.** The classical Fourier--Legendre--Bessel identity (DLMF 18.17.21) states, for all real \(y\),
\[
\int_0^1P_k(1-2x^2)\sin(xy)\,dx
 =\frac\pi2 J_{k+1/2}(y/2)^2.
\]
Substitute \(y=2r\). The sine-transform Plancherel identity with frequency \(2r\) is
\[
\int_0^\infty\left|\int_0^1u(x)\sin(2rx)\,dx\right|^2dr
 =\frac\pi4\int_0^1|u(x)|^2dx.
\]
Taking \(u(x)=P_k(1-2x^2)\) and equating the two squared expressions gives \(I_k=\pi^{-1}\int_0^1P_k(1-2x^2)^2dx\). Expanding the polynomial by the standard binomial formula,
\[
P_k(1-2x^2)=\sum_{j=0}^k(-1)^j\binom kj\binom{k+j}j x^{2j},
\]
shows rationality and gives the fully exact finite formula
\[
\pi I_k=\sum_{a,b=0}^k\frac{(-1)^{a+b}\binom ka\binom{k+a}a\binom kb\binom{k+b}b}{2(a+b)+1}.
\]
For \(k=0,1,2\), direct integration yields the three displayed rational values.

**2. The Bessel core constant.** Define \(A(R)=\int_0^R J_0(t)^2dt\). The fixed-order Bessel asymptotic gives
\(J_0(t)^2=[1+\sin(2t)]/(\pi t)+O(t^{-2})\). Consequently \(A(R)=\pi^{-1}\log R+C+o(1)\) for some finite constant \(C\). To identify it, Graf's product identity and the elementary Laplace transform of \(J_0\) give
\[
\int_0^\infty e^{-st}J_0(t)^2dt
 =\frac1\pi\int_0^{\pi/2}\frac{du}{\sqrt{(s/2)^2+\sin^2u}}
 =\frac1\pi\log\frac8s+o(1),\qquad s\downarrow0.
\]
The last asymptotic follows by splitting the integral near \(u=0\), using \(\sin u\sim u\), and integrating the regular remainder, or from the standard complete elliptic integral asymptotic. On the other hand, integration by parts followed by \(sR=v\) gives this Laplace integral as \(\pi^{-1}(-\log s-\gamma)+C+o(1)\). Thus
\[
\boxed{A(R)=\frac{\log R+\gamma+\log8}{\pi}+o(1).}
\]

**3. Matching the oscillatory Legendre tail.** Write \(Q_k=\pi I_k\). The substitution \(x=\sin(\theta/2)\) gives
\[
Q_k=\frac12\int_0^\pi P_k(\cos\theta)^2\cos(\theta/2)\,d\theta.
\]
Fix a small \(\delta\in(0,1)\). The uniform Hilb Bessel approximation for Legendre polynomials on \([0,\delta]\), together with its integrated error, gives
\[
K\int_0^\delta P_k(\cos\theta)^2\cos(\theta/2)\,d\theta
 =\int_0^{K\delta}J_0(u)^2du+O(\delta^2)+o_\delta(1).
\]
Indeed, the Hilb amplitude \((\theta/\sin\theta)^{1/2}\), multiplied by \(\cos(\theta/2)\), contributes the factor \(\theta/[2\sin(\theta/2)]=1+O(\theta^2)\); the \(J_0(u)^2=O((1+u)^{-1})\) bound makes the total contribution of this factor \(O(\delta^2)\). On the complementary interval, the standard interior Legendre cosine asymptotic, oscillatory averaging and the endpoint Bernstein bound give
\[
K\int_\delta^\pi P_k(\cos\theta)^2\cos(\theta/2)\,d\theta
 =\frac1\pi\int_\delta^\pi\frac{\cos(\theta/2)}{\sin\theta}\,d\theta+o_\delta(1)
 =\frac1\pi\log\cot(\delta/4)+o_\delta(1).
\]
The endpoint near \(\theta=\pi\) contributes no additional logarithm: the factor \(\cos(\theta/2)\) cancels its possible singularity. Combining the pieces and the Bessel core evaluation,
\[
2\pi KQ_k
 =\log(K\delta)+\gamma+\log8+\log\cot(\delta/4)
   +O(\delta^2)+o_\delta(1).
\]
As \(\delta\downarrow0\), \(\log[\delta\cot(\delta/4)]=\log4+O(\delta^2)\), so
\(2\pi KQ_k-\log K\to\gamma+\log32\). Since \(I_k=Q_k/\pi\), this proves the claimed two-term asymptotic.

**4. Sharp constant evaluation.** Xu's Theorems 1.2--1.3 prove for \(d\ge3\) that the first nonconstant degree has the largest modal moment and that the sharp quadratic stability coefficient is \((2\pi)^d[I_{\nu,0}(q)^{2/q}-I_{\nu,1}(q)^{2/q}]\). With \(d=3\), \(q=4\), our exact evaluations \(I_0=1/\pi\) and \(I_1=7/(15\pi)\) give the stated value \(8\pi^{5/2}(1-\sqrt{7/15})\).

## Verification
The standalone Python file `verify_spherical_fourth.py` evaluates ten complete polynomial moments in exact rational arithmetic; it checks three original Bessel fourth integrals by numerical quadrature and six high-degree Legendre norms by Gaussian quadrature. In particular, the values \(2\pi KQ_k-\log K\) approach the asserted constant \(\gamma+\log32\). These are finite corroborations only: the infinite rational identity and asymptotic are proved above, not by the calculations. Run `python verify_spherical_fourth.py` with Python 3, NumPy, SciPy and SymPy.

## Relationship to prior work
Carneiro, Oliveira e Silva and Sousa (2018 preprint, published 2019) establish the modal reduction and explicitly evaluate the degree-zero fourth moment in all dimensions. Xu (first preprint October 14, 2026), Theorems 1.2--1.3, establishes all-degree strict ordering and the sharp stability coefficient as a difference of Bessel moments; its displayed formula leaves the special-case coefficient unevaluated. DLMF 18.17.21 already supplies the exact Legendre--Bessel sine-transform identity, so the rational moment representation by Plancherel is a classical-identity consequence rather than a claim of a new product formula. The additional quantitative content here is the **complete two-term high-degree modal tail with its explicit constant**, alongside the evaluable entire rational spectrum and resulting closed stability coefficient. Searches did not identify the combined tail formula in the inspected literature; this does not establish historical uniqueness.

## Limitations
The result is specific to the three-dimensional spherical radial--angular mixed norm at exponent four; it does not reprove modal strict ordering, sharp stability, or their equality cases, which are invoked from Xu's source. The asymptotic gives a two-term expansion with remainder \(o(K^{-1})\) but no effective uniform finite-degree error constant. It does not claim new spherical restriction exponents, arbitrary-dimensional formulas, or independence from the underlying classical special-function identities. Priority among older special-function integral-asymptotic papers cannot be ruled out by the sources inspected.

## References
1. Z. Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648v1 (first public October 14, 2026), Theorems 1.2--1.3, Sections 1--2. https://arxiv.org/pdf/2610.19648
2. E. Carneiro, D. Oliveira e Silva, M. Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365, Adv. Math. 341 (2019), 583--608, especially Theorem 1 and Eq. (4.11). https://arxiv.org/pdf/1710.10365
3. NIST Digital Library of Mathematical Functions, formula 18.17.21 (Legendre--Bessel sine transform) and Section 18.15 (Legendre asymptotics). https://dlmf.nist.gov/18.17.E21 ; https://dlmf.nist.gov/18.15
4. NIST Digital Library of Mathematical Functions, Chapter 10 (Bessel fixed-order asymptotics and Bessel addition formulas). https://dlmf.nist.gov/10.17 ; https://dlmf.nist.gov/10.23
