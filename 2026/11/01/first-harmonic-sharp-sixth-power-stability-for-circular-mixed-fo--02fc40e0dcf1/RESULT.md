# First-harmonic sharp sixth-power stability for circular mixed Fourier extension

## Finding
For each integer \(k\geq0\), write
\[
I_k=\int_0^\infty r\,|J_k(r)|^6\,dr,
\]
where \(J_k\) is the ordinary Bessel function of the first kind. Then the **unique largest positive-degree moment** is the first:
\[
\boxed{I_1>I_k\quad\text{for every integer }k\geq2.}
\]
The proof also gives the explicit rational separator
\[
\boxed{I_1>\frac1{10}>I_k\quad(k\geq2).}
\]
Consequently, for circular Fourier extension at the smallest admissible even exponent \(q=6\), the optimal squared-distance stability coefficient is
\[
\boxed{\Gamma_{2,6}=4\pi^2\left(I_0^{1/3}-I_1^{1/3}\right)>0.}
\]
Every nonzero equality case of the associated stability inequality is either a constant or a first spherical harmonic, that is, an element of the complex span of \(e^{i\theta}\) and \(e^{-i\theta}\). No explicit elementary evaluation of either improper Bessel integral is claimed.

## Assumptions and scope
Let \(d\sigma\) be **unnormalized** arc-length measure on \(\mathbb S^1\), so \(\sigma(\mathbb S^1)=2\pi\). For \(f\in L^2(\mathbb S^1,d\sigma)\), define
\[
(Ef)(x)=\int_{\mathbb S^1}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega),
\]
and
\[
\|Ef\|_{L^6_{\mathrm{rad}}L^2_{\mathrm{ang}}}^6
=\int_0^\infty\left(\int_{\mathbb S^1}|Ef(r\theta)|^2\,d\sigma(\theta)\right)^3 r\,dr.
\]
Let \(P_0\) be orthogonal projection onto the constant functions. The precise sharp inequality is
\[
4\pi^2 I_0^{1/3}\|f\|_2^2
-\|Ef\|_{L^6_{\mathrm{rad}}L^2_{\mathrm{ang}}}^{2}
\geq 4\pi^2\left(I_0^{1/3}-I_1^{1/3}\right)\|f-P_0f\|_2^2.
\]
All quantifiers range over complex-valued \(L^2\) data and integer Bessel orders. The result does not assert strict ordering of **every** pair of positive-degree moments, nor does it assert the same maximizer at exponents other than six.

## Proof
**1. Exhaustive splitting of orders.** For \(n\geq1\), put \(F_n(r)=rJ_n(r)^6\). We show \(I_1>1/10\), \(I_n<1/10\) for \(2\leq n\leq11\), and \(I_n<1/10\) for \(n\geq12\). Since the three ranges exhaust every positive integer order, this proves the strict comparison without extrapolating finite experiments to all orders.

**2. A rigorous finite interval certificate.** Partition \([0,40]\) into \(2000\) intervals of length \(h=1/50\). The composite Simpson sum is
\[
S_n=\frac1{7500}\sum_{j=0}^{2000}w_jjJ_n(j/50)^6,
\]
where \(w_0=w_{2000}=1\), \(w_j=4\) for odd \(j\), and \(w_j=2\) for even interior \(j\). The angular integral representation
\[
J_n(r)=\frac1{2\pi}\int_{-\pi}^\pi e^{i(nu-r\sin u)}\,du
\]
gives \(|J_n^{(a)}(r)|\leq1\) for every integer \(a\geq0\), \(r\geq0\), and \(n\geq0\). By Leibniz's rule, \(|(J_n^6)^{(a)}|\leq6^a\). Thus for all \(r\in[0,40]\),
\[
|F_n^{(4)}(r)|\leq4\cdot6^3+40\cdot6^4=52704.
\]
The standard composite Simpson remainder therefore gives, uniformly in \(n\),
\[
\left|\int_0^{40}F_n(r)\,dr-S_n\right|
\leq\frac{40}{180}\left(\frac1{50}\right)^4\!52704
<\frac1{500}.
\]
The attached standalone `CHECK.py` evaluates **outward-rounded integer-rational enclosures** for all \(J_n(j/50)\) with \(n=1,\ldots,11\), \(j=0,\ldots,2000\). It uses the alternating series
\[
J_n(j/50)=\sum_{a=0}^\infty\frac{(-1)^a(j/100)^{2a+n}}{a!(a+n)!}.
\]
After \(150\) terms the terms are strictly decreasing in magnitude, with an omitted-tail magnitude no larger than the first omitted term. Each of the finite terms is enclosed through outward integer division at scale \(10^{90}\); the omitted first term enlarges the interval in both directions. Raising absolute-value bounds to the sixth power and summing the nonnegative Simpson weights uses only **exact integer arithmetic**. The resulting strict rational comparisons, reproduced from the packaged checker, are
\[
\boxed{S_1>\frac{51}{500},\qquad S_n<\frac7{100}\quad(2\leq n\leq11).}
\]
In particular, \(I_1>S_1-1/500>1/10\).

**3. Certified tail bounds for the finite orders.** The classical exact Bessel modulus estimate, recalled as Lemma 3.7 of Xu (2026), gives for \(r>n\geq1\)
\[
|J_n(r)|^2\leq\frac2{\pi\sqrt{r^2-n^2}}.
\]
Consequently, for every \(2\leq n\leq11\),
\[
\begin{aligned}
\int_{40}^\infty F_n(r)\,dr
&\leq\left(\frac2\pi\right)^3\!\int_{40}^\infty\frac{r\,dr}{(r^2-n^2)^{3/2}}\\
&=\left(\frac2\pi\right)^3\frac1{\sqrt{1600-n^2}}
<\frac1{100},
\end{aligned}
\]
where the last inequality follows from \(\pi>3\), \(1600-11^2>38^2\), and \(8/(27\cdot38)<1/100\). Hence
\[
I_n<S_n+\frac1{500}+\frac1{100}
<\frac7{100}+\frac1{500}+\frac1{100}
=\frac{41}{500}<\frac1{10}.
\]

**4. Infinite-order tail.** Xu's estimate (3.87) gives, for every integer \(n\geq4\),
\[
\int_0^\infty r\,|J_n(r)|^5\,dr<\frac{13}{40}.
\]
Landau's uniform estimate (in Xu's displayed equation (2.9)) is
\[
\sup_{r>0}|J_n(r)|<\frac7{10}n^{-1/3}.
\]
Multiplication gives for all \(n\geq12\)
\[
I_n<\frac{91}{400\,n^{1/3}}
\leq\frac{91}{400\,12^{1/3}}<\frac1{10}.
\]
The last inequality is verified by cubing positive quantities: \(91^3\cdot1000<400^3\cdot12\). This handles infinitely many degrees by an analytical estimate; they are **not** covered by the finite checker alone.

**5. Sharp stability and equality.** The known spherical-harmonic reduction has modal sixth moments \(I_n\) in dimension two. Xu's Theorem 1.2 yields \(I_0>I_n\) for every \(n\geq1\); our steps above identify the unique nonzero maximizing degree as \(n=1\). Xu's Theorem 1.3 expresses the sharp coefficient as \((2\pi)^2\bigl(I_0^{1/3}-\max_{n\geq1}I_n^{1/3}\bigr)\), and its equality analysis identifies exactly the constant and maximal-degree pure harmonics. Substitution yields the stated sharp inequality, coefficient and equality classes. No unproved assertion about unbounded or noninteger-degree modes is needed.

## Verification
Execute `python3 CHECK.py` with a standard Python 3 interpreter; no external packages are required. It uses only exact integer operations, performs all node and mode checks, asserts the uniform Simpson error, the Bessel tail comparisons and the infinite-order numerical cutoff, and prints `CHECK_OK 15`. No external floating-point quadrature, polynomial-fit inference, or finite-to-infinite extrapolation is used. The two key analytical published premises are explicitly identified in the proof, rather than being replaced by numerical certification.

## Relationship to prior work
Xu, *Sharp radial–angular mixed norm Fourier extension and global stability on spheres* (first public October 14, 2026), proves the global extremizer and general sharp stability coefficient. In its circle case the optimal nonzero harmonic degree is **not identified** in Theorem 1.3; Proposition 3.11 orders only the first four modes, while (3.87) bounds all higher modes relative to an absolute constant or degree zero. The present finite/infinite comparison identifies the sharp *second* mode at the first admissible even exponent \(q=6\), thereby evaluating the index appearing in Xu's sharp coefficient and its equality class. Xu's quantitative estimates (3.87) and (2.9) are essential imported premises, not new claims.

Carneiro–Oliveira e Silva–Sousa established degree-zero extremality at even exponents, including \(d=2,q=6\), without determining the largest nonconstant degree. Ciccone–Sousa proves the first nonconstant mode at the infinite exponent and for several higher-dimensional finite exponents, but not this circular sixth moment. Oliveira e Silva–Thiele studies sixfold Bessel products connected to the ordinary (unmixed) circle extension problem, not the present all-order diagonal modal comparison. The result does not imply a full strictly decreasing sequence \(I_1>I_2>I_3>\cdots\) and is not an ordinary \(L^6(\mathbb R^2)\) extension extremizer theorem.

## Limitations
The analytic high-order estimate and sharp mixed-norm stability theorem are imported from the cited full-text source; the finite checker certifies the new bounded-order inequalities using exact arithmetic and standard quadrature error estimates. The result identifies the maximizing degree only at exponent six and only for the radial–angular **mixed** norm. Prior results at large exponents or near the critical exponent are outside this fixed-exponent claim. Earlier unindexed proofs of the same circular sixth-moment ordering remain a residual originality risk. No independent mathematical audit has been performed.

## References
1. Z. Xu, *Sharp radial–angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648v1, first public October 14, 2026, especially Theorems 1.2–1.3; Lemma 3.7, equations (2.9), (3.87); Proposition 3.11 and Section 4. https://arxiv.org/html/2610.19648v1.
2. E. Carneiro, D. Oliveira e Silva, M. Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365, first public October 28, 2017; Theorems 1–2. https://arxiv.org/pdf/1710.10365.
3. V. Ciccone, M. Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere*, arXiv:2312.07309, first public December 12, 2023, J. Fourier Anal. Appl. 31 (2025), especially Propositions 3–4 and 6. https://link.springer.com/article/10.1007/s00041-025-10201-7.
4. D. Oliveira e Silva, C. Thiele, *Estimates for certain integrals of products of six Bessel functions*, arXiv:1509.03092, first public September 2015; Rev. Mat. Iberoam. 33 (2017), 1423–1462. https://arxiv.org/abs/1509.03092.
5. L. Landau, *Bessel functions: monotonicity and bounds*, J. Lond. Math. Soc. 61 (2000), 197–215 (uniform Bessel-order suprema); as quoted in reference 1.
