# Exact all-order painless B-spline Gabor bounds and a sharp exponential conditioning law

## Finding
For every integer \(n\ge2\) and every integer oversampling factor \(q\ge n\), let \(B_n=\mathbf1_{[0,1]}^{*n}\) be the cardinal B-spline, and consider the Gabor family
\[
\mathcal G_{n,q}=\{ e^{2\pi i m t/q} B_n(t-k):m,k\in\mathbb Z\}\subset L^2(\mathbb R).
\]
Put \(E_n=\sum_{k\in\mathbb Z}B_n(k)^2\) and \(H_n=\sum_{k\in\mathbb Z}B_n(k+1/2)^2\). The **optimal** (largest lower and smallest upper) frame bounds are
\[
(A_{n,q},U_{n,q})=\begin{cases}
(qH_n,qE_n),&n\text{ even},\\
(qE_n,qH_n),&n\text{ odd}.
\end{cases}
\]
In particular, each frame is genuine and the bounds are rational numbers, computable from a finite sum. The normalized frame operator is multiplication by a continuous one-periodic function that is **strictly decreasing** on \([0,1/2]\) for even \(n\) and **strictly increasing** there for odd \(n\); its only maxima and minima occur at the asserted integer and half-integer classes.

The optimal spectral condition number \(\kappa_n=U_{n,q}/A_{n,q}\), independent of \(q\ge n\), satisfies the **sharp asymptotic law**
\[
\boxed{\lim_{n\to\infty}\left(\frac{\pi^2}{4}\right)^n(\kappa_n-1)
=\frac4{\sqrt{3(1-4/\pi^2)}}.}
\]
The exponential base and its leading coefficient are exact.

## Assumptions and scope
The \(n\)-fold convolution is Lebesgue convolution; \(B_n\) is nonnegative, continuous for \(n\ge2\), supported on \([0,n]\), and normalized by \(\int B_n=1\). The Gabor atoms use time step one and frequency step \(1/q\), without \(L^2\)-renormalization of \(B_n\). The frame inequality is \(A\|f\|_2^2\le\sum_{k,m}|\langle f,e^{2\pi i mt/q}B_n(\cdot-k)\rangle|^2\le U\|f\|_2^2\) for every \(f\in L^2(\mathbb R)\). The range \(q\ge n\) matters: no claim is made for \(q<n\) or nonintegral lattices.

The endpoints can be evaluated by the finite truncated-power identity
\[
B_n(t)=\frac1{(n-1)!}\sum_{j=0}^n(-1)^j\binom nj(t-j)_+^{n-1}.
\]
For example \((E_2,H_2)=(1,1/2)\), \((E_3,H_3)=(1/2,19/32)\), \((E_4,H_4)=(1/2,265/576)\) and \((E_5,H_5)=(61/144,32227/73728)\).

## Proof
**1. Exact diagonal frame operator.** Fix an integer translation \(k\). The function \(f(t)B_n(t-k)\) is supported in an interval of length at most \(n\le q\). The functions \(q^{-1/2}e^{2\pi i mt/q}\) form a complete orthonormal Fourier system on any interval of length \(q\). Their Parseval identity gives
\[
\sum_{m\in\mathbb Z}|\langle f,e^{2\pi i mt/q}B_n(\cdot-k)\rangle|^2
=q\int_{\mathbb R}|f(t)|^2B_n(t-k)^2\,dt.
\]
Summing over \(k\), with Tonelli, yields the exact frame form \(q\int |f(t)|^2P_n(t)\,dt\), where \(P_n(t)=\sum_k B_n(t-k)^2\). Consequently the optimal bounds are exactly \(q\min P_n\) and \(q\max P_n\), provided \(\min P_n>0\); positivity follows from partition of unity \(\sum_kB_n(t-k)=1\).

**2. Alternating Fourier-coefficient signs.** Write \(P_n(x)=c_{n,0}+2\sum_{m\ge1}c_{n,m}\cos(2\pi m x)\). The coefficients are real and \(c_{n,m}=\int_{\mathbb R}B_n(t)^2e^{-2\pi imt}\,dt\). The Fourier transform of \(B_n\) is \(e^{-\pi in\xi}(\sin(\pi\xi)/(\pi\xi))^n\), so convolution of transforms gives, for every positive integer \(m\),
\[
c_{n,m}=\frac{(-1)^n}{\pi}\int_{\mathbb R}
\frac{\sin^{2n}u}{u^n(\pi m-u)^n}\,du.
\]
The integrand's singularities at \(0\) and \(\pi m\) are removable; the integral is absolutely convergent. Set \(a=\pi m\). The finite partial-fraction identity is
\[
\frac1{u^n(a-u)^n}=\sum_{j=1}^n\binom{2n-j-1}{n-1}
\frac{u^{-j}+(a-u)^{-j}}{a^{2n-j}}.
\]
For odd \(j\), symmetric principal values of the two separate terms vanish by evenness and \(\pi\)-periodicity of \(\sin^{2n}u\); for even \(j\) they agree and are absolutely integrable. At \(j=1\), pair the terms before sending the cutoffs to infinity. Thus
\[
(-1)^nc_{n,m}=\frac2\pi\sum_{r=1}^{\lfloor n/2\rfloor}
\binom{2n-2r-1}{n-1}\frac{I_{n,r}}{(\pi m)^{2n-2r}}>0,
\quad I_{n,r}=\int_{\mathbb R}\frac{\sin^{2n}u}{u^{2r}}\,du>0.
\]
Each \(I_{n,r}\) is finite. In particular the sequence \((-1)^nc_{n,m}\) is a strictly positive linear combination of the powers \(m^{-2s}\), \(s=n-r\ge1\). It also obeys \(|c_{n,m}|\le |c_{n,1}|m^{-n}\).

**3. Global strict monotonicity.** For any integer \(s\ge1\), the cosine Dirichlet series \(F_s(x)=\sum_{m\ge1}m^{-2s}\cos(2\pi mx)\) strictly decreases on \([0,1/2]\). Indeed the Gamma-integral formula expresses it as a positive weighted integral of
\[
\sum_{m\ge1}e^{-mt}\cos(2\pi mx)
=\frac12\left(\frac{\sinh t}{\cosh t-\cos(2\pi x)}-1\right),\qquad t>0,
\]
which is strictly decreasing in \(x\in[0,1/2]\). The representation in step 2 is a positive finite combination of such series, with overall sign \((-1)^n\). Therefore \(P_n\) has the stated strict monotonicity and, by symmetry and periodicity, its global extrema occur only at integer and half-integer points. This proves the exact bounds and equality location claim.

**4. Sharp condition-number asymptotics.** Parseval gives
\[
c_{n,0}=\frac1\pi\int_{\mathbb R}\left(\frac{\sin u}{u}\right)^{2n}du
\sim\sqrt{\frac3{\pi n}},
\]
since \(\log(\sin u/u)=-u^2/6+O(u^4)\) at the unique unit-modulus maximum \(u=0\). For the first oscillatory coefficient, define \(h(u)=\sin^2u/[u(\pi-u)]\), continuously extended at \(0,\pi\). On \((0,\pi)\) the elementary concavity bound \(\sin^2u\le4u(\pi-u)/\pi^2\) is strict off the midpoint; outside this interval \(|h(u)|\le1/(\pi+1)<4/\pi^2\). Therefore its unique global absolute maximum is \(h(\pi/2)=4/\pi^2\), where \((\log h)''=-2(1-4/\pi^2)\). Laplace's method with the absolute smaller exterior tails yields
\[
(-1)^nc_{n,1}=\frac1\pi\int_{\mathbb R}h(u)^n\,du
\sim \frac{(4/\pi^2)^n}{\sqrt{\pi n(1-4/\pi^2)}}.
\]
The power decomposition in step 2 bounds all higher Fourier coefficients by \(|c_{n,m}|\le |c_{n,1}|m^{-n}\). Consequently
\[
|P_n(0)-P_n(1/2)|=4|c_{n,1}|(1+O(3^{-n})),
\qquad \min P_n=c_{n,0}(1+o(1)).
\]
Dividing gives the stated exact exponential coefficient for \(\kappa_n-1=(\max P_n-\min P_n)/\min P_n\).

## Verification
The bundled standalone `CHECK.py` uses Python's standard-library exact rational arithmetic to evaluate 11 integer orders, rational grids, partition-of-unity and reflected values. It verifies the listed exact endpoint fractions, strict monotonicity at 32 grid subdivisions for each order, and supplementary finite-order values of the asymptotic scaling. A separate exact symbolic algebra test checked the general partial-fraction identity at integer orders 2 through 10. The infinite-order assertions follow from the analytical argument above, not from these finite checks.

To reproduce the bundled checks, run `python CHECK.py` from the directory containing the extracted file. No external packages or internet access are required.

## Relationship to prior work
The exact diagonalization of Gabor frame forms when the support is no longer than the modulation period is classical (the painless case); it is used here without claiming priority. Hasannasab and Lemvig (2026) analyze B-spline Zak-transform zero sets and integer-oversampled frame existence, rather than the all-order **optimal constants**, parity-specific equality locations and sharp high-order conditioning coefficient given here. Stangl and Frederick (2026) treat the complete frame region for the second-order spline along a fixed-density hyperbola, rather than the present all-order conditioning profile. Earlier Gabor work on cardinal and exponential B-splines likewise supplies frame existence and general methods but not the proved asymptotic constant in the inspected material.

## Limitations
The result applies to cardinal integer-order B-splines with unit translation and frequency period \(q\ge n\); it says nothing about general compactly supported windows, smaller frequency periods, arbitrary lattice shapes or finite-dimensional approximate Gram matrices. No assertion is made that the monotonicity lemma itself is historically novel: an unindexed classical spline identity could give it directly. The assessed contribution combines explicit optimal Gabor bounds for all orders with the exact exponential conditioning constant; comprehensive priority verification remains subject to external review. All extremal statements use the specified unnormalized atoms and the optimal infinite-dimensional frame bounds.

## References
1. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116 (initially posted 2026-09-11), https://arxiv.org/abs/2609.13116.
2. A. Stangl and C. Frederick, *The frameset of the second-order B-Spline along \(ab=1/q\)*, arXiv:2609.00481 (initially posted 2026-08-31 UTC), https://arxiv.org/abs/2609.00481.
3. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), https://arxiv.org/abs/1311.7359.
4. I. Daubechies, A. Grossmann, and Y. Meyer, *Painless nonorthogonal expansions*, J. Math. Phys. 27 (1986), 1271–1283.
