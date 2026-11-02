# Exact three-step correlation resonance in a fixed-point-free golden-ratio interval map

## Finding

For the fixed-point-free expanding interval map
\[
F(x)=\begin{cases}
\beta x+1-\beta/2,&0\le x\le 1/2,\\
\beta x-\beta/2,&1/2<x\le1,
\end{cases}
\qquad \beta=(1+\sqrt5)/2,
\]
let \(\mu\) be the invariant absolutely continuous probability measure specified below, and let \(X_n=F^n(X_0)\) with \(X_0\sim\mu\). Its centered coordinate autocovariance is exactly
\[
\operatorname{Cov}(X_0,X_n)=
\begin{cases}
\dfrac{5-\sqrt5}{40}\,\beta^{-n},&n\equiv0\pmod3,\\[4pt]
0,&n\equiv1,2\pmod3,
\end{cases}\quad n\ge0.
\]
Consequently the covariance generating function and Green--Kubo variance are
\[
\sum_{n\ge0}\operatorname{Cov}(X_0,X_n)z^n
=\frac{(5-\sqrt5)/40}{1-\beta^{-3}z^3},
\qquad
\lim_{N\to\infty}\frac1N\operatorname{Var}\!\left(
\sum_{j=0}^{N-1}X_j\right)=\frac{\sqrt5}{20}.
\]
In particular the first two nonzero lags are uncorrelated, although the third lag is strictly positively correlated. The exact lag-three resonance concerns the stationary coordinate observable, not all observables.

## Assumptions and scope

The state space is \([0,1]\) and the discontinuity is assigned to the left branch. Pointwise choices at finitely many partition boundaries do not affect the absolutely continuous stationary statements. The map is increasing with constant slope \(\beta\) on both branches. Set
\[
a=1-\beta/2=(3-\sqrt5)/4,\qquad c=\beta/2,
\]
and partition into \(I_0=[0,a], I_1=[a,1/2], I_2=[1/2,c], I_3=[c,1]\) up to endpoints. The branch images, in this order, are \(I_1\), \(I_2\cup I_3\), \(I_0\cup I_1\), and \(I_2\). Hence the row-to-column transition matrix is
\[
A=\begin{pmatrix}
0&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&0
\end{pmatrix}.
\]
The chosen stationary law has density
\[
h(x)=\begin{cases}
 h_o=\dfrac12+\dfrac{\sqrt5}{10},&x\in I_0\cup I_3,\\[2pt]
 h_i=\dfrac12+\dfrac{3\sqrt5}{10},&x\in I_1\cup I_2.
\end{cases}
\]
These constants give a normalized positive density. Indeed \(A^{\mathsf T}(h_o,h_i,h_i,h_o)^{\mathsf T}=\beta(h_o,h_i,h_i,h_o)^{\mathsf T}\). Reflection symmetry implies \(\mathbb E_\mu X_0=1/2\). The inequalities \(F(x)>x\) for \(0\le x\le1/2\) and \(F(x)<x\) for \(1/2<x\le1\) show that \(F\) has no fixed points.

## Proof

Let \(\mathcal P\) be the Frobenius--Perron operator with respect to Lebesgue measure. Let \(f(x)=x-1/2\) and \(q=h f\). The map respects reflection away from the discontinuity: \(F(1-x)=1-F(x)\), so \(\mathcal P\) preserves the four-dimensional vector space of functions that are affine on each \(I_j\) and antisymmetric under \(x\mapsto1-x\).

On the two left cells, write an antisymmetric function as \(u_0x+v_0\) and \(u_1x+v_1\). The reflected two right-cell expressions are forced. Direct summation of inverse branches of \(F\) gives the coordinate action
\[
N=\begin{pmatrix}
0&0&\beta^{-2}&0\\
0&0&-1/(2\beta)&-\beta^{-1}\\
\beta^{-2}&0&\beta^{-2}&0\\
-a\beta^{-2}&\beta^{-1}&-1/(2\beta)&-\beta^{-1}
\end{pmatrix}.
\]
The vector of \(q\) is \(v=(h_o,-h_o/2,h_i,-h_i/2)^{\mathsf T}\). The defining identity \(\beta^2=\beta+1\) gives by exact multiplication
\[
N^3v=\beta^{-3}v.
\]
This is an identity of functions (almost everywhere), not an extrapolation of sample correlations.

For an antisymmetric piecewise affine function represented by \(w\), put \(\Lambda(w)=\int_0^1 f(x)w(x)\,dx\), where \(w\) also denotes its represented function. Explicitly, \(\Lambda\) is twice the sum of the elementary integrals of \((x-1/2)(u_jx+v_j)\) over \([0,a]\) and \([a,1/2]\). Evaluating these four polynomial antiderivatives gives
\[
\Lambda(v)=\frac{5-\sqrt5}{40},\qquad
\Lambda(Nv)=0,\qquad\Lambda(N^2v)=0.
\]
All identities are checked independently by the standalone exact-arithmetic program `check.py`.

The transfer identity and stationarity give, for all nonnegative integers \(n\),
\[
\operatorname{Cov}(X_0,X_n)
=\int_0^1 f(x)f(F^n(x))h(x)\,dx
=\Lambda(N^nv).
\]
The cubic identity yields the stated three residue classes and absolute summability of the covariances. Finally the finite stationary variance identity
\[
\frac{1}{N}\operatorname{Var}\left(\sum_{j=0}^{N-1}X_j\right)
=C_0+2\sum_{n=1}^{N-1}(1-n/N)C_n
\]
converges by dominated convergence to \(C_0(1+\beta^{-3})/(1-\beta^{-3})=\sqrt5/20\). This proves the claimed limit without assuming a central limit theorem.

## Verification

Run `python check.py` with Python 3 and SymPy. It tests the Markov density eigenvector and normalization, centered mean, cubic transfer identity, the first seven covariances, and the exact Green--Kubo simplification. The general correlation formula rests on the explicitly proved finite-dimensional operator identity; finite computational tests are auxiliary checks.

## Relationship to prior work

Lawnik, Moysis and Volos (2023) introduce the relevant family of piecewise maps without fixed points and examine chaotic and pseudorandom properties. Their branch construction includes this particular linear choice; the exact stationary covariance sequence here is additional. Intermediate beta transformations and their finite-type symbolic structures predate that paper. Li, Sahlsten and Samuel (2014), Quackenbush, Samuel and West (2020), and work on invariant densities for generalized beta transformations establish important earlier structural techniques. No novelty is claimed for the piecewise map, its Markov representation as such, or the general Frobenius--Perron method. The narrowly asserted contribution is the particular exact three-step coordinate-correlation identity and associated Green--Kubo value.

## Limitations

The result is for exactly the golden-ratio slope, symmetric discontinuity, explicitly stated stationary law and centered coordinate observable. It makes no general assertion about nearby parameters, cryptographic security, independence of symbols, universal mixing rates, or a central limit theorem. Zero correlation at lags one and two does not mean probabilistic independence. Literature comparisons do not establish exhaustive publication priority; earlier beta-transfer operator calculations could conceivably subsume this explicit specialization. Independent mathematical validation has not been performed.

## References

1. M. Lawnik, L. Moysis, C. Volos, *A Family of 1D Chaotic Maps without Equilibria*, Symmetry **15** (2023), 1311, first publicly published 27 June 2023, https://doi.org/10.3390/sym15071311 .
2. B. Li, T. Sahlsten, T. Samuel, *Intermediate beta-shifts of finite type*, 2014 preprint, https://www.researchgate.net/publication/259933351_Intermediate_beta-shifts_of_finite_type .
3. B. Quackenbush, T. Samuel, M. West, *Periodic Intermediate Beta-Expansions of Pisot Numbers*, Mathematics **8** (2020), 903, https://arxiv.org/abs/2004.13386 .
4. P. Góra, *Invariant densities for generalized beta-maps*, Ergodic Theory and Dynamical Systems **27** (2007), 1583–1598, https://doi.org/10.1017/S0143385707000053 .
5. K. Dajani, S. Sanderson, *Ergodic properties of a parameterised family of symmetric golden maps: the matching phenomenon revisited*, arXiv:2301.08623 (2023), https://arxiv.org/abs/2301.08623 .
