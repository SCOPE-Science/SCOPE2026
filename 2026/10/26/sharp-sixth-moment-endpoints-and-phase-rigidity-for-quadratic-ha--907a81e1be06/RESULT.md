# Sharp sixth-moment endpoints and phase rigidity for quadratic harmonics on the three-sphere

## Finding

Let \(\sigma\) be probability-normalized surface measure on \(S^3\subset\mathbb R^4\), and let \(\mathcal H_2\) be the complex spherical harmonics of exact degree two. For every nonzero \(Y\in\mathcal H_2\),
\[
\boxed{\ \int_{S^3}|Y|^6\,d\sigma\le15\left(\int_{S^3}|Y|^2\,d\sigma\right)^3.\ }
\]
Equality holds if and only if
\[
Y(\omega)=\gamma\bigl((v\cdot\omega)^2-\tfrac14\bigr),
\qquad v\in S^3,\quad \gamma\in\mathbb C\setminus\{0\}.
\]
For every nonzero **real** \(Y\in\mathcal H_2\), there is also the sharp lower endpoint
\[
\boxed{\ \frac{27}{7}\left(\int_{S^3}|Y|^2\,d\sigma\right)^3\le\int_{S^3}|Y|^6\,d\sigma.\ }
\]
Lower equality holds exactly for traceless quadratics whose representing matrix has two equal positive and two equal negative eigenvalues. Up to a nonzero real scalar and an orthogonal change of coordinates, these are
\[
Y(\omega)=\omega_1^2+\omega_2^2-\omega_3^2-\omega_4^2.
\]
This gives the exact two-sided sixth-moment interval for real degree-two harmonics and the complex sharp upper endpoint, with all equality cases.

## Assumptions and scope

A real degree-two spherical harmonic has the form \(Y_A(\omega)=\omega^{\mathsf T}A\omega\), with \(A\) a nonzero real symmetric traceless \(4\times4\) matrix; complex harmonics are \(Y_A+iY_B\) with such real matrices \(A,B\). All integrals and inner products use probability surface measure. The theorem is for exact degree two on the unit three-sphere, not for all degrees, all dimensions, or complex lower endpoints.

For a real \(A\), write \(p_j=\operatorname{tr}(A^j)\). The exact invariant identity is
\[
\mathcal R(A):=\frac{\int_{S^3}Y_A^6\,d\sigma}{\left(\int_{S^3}Y_A^2\,d\sigma\right)^3}
=-\frac{27}{14}+\frac{162}{7}\frac{p_4}{p_2^2}+\frac{72}{7}\frac{p_3^2}{p_2^3}.
\]
Consequently, both *exact* nonnegative real deficits are
\[
\mathcal R(A)-\frac{27}{7}
=\frac{162}{7}\left(\frac{p_4}{p_2^2}-\frac14\right)
+\frac{72}{7}\frac{p_3^2}{p_2^3},
\]
\[
15-\mathcal R(A)
=\frac{162}{7}\left(\frac7{12}-\frac{p_4}{p_2^2}\right)
+\frac{72}{7}\left(\frac13-\frac{p_3^2}{p_2^3}\right).
\]
For any complex \(Y=U+iV\), put \(a=\|U\|_2^2\), \(b=\|V\|_2^2\), \(c=\langle U,V\rangle\), all real. A further quantitative phase-rank estimate holds:
\[
15\|Y\|_2^6-\|Y\|_6^6\ge36\|Y\|_2^2(ab-c^2)\ge0.
\]
The coefficient in this subsidiary estimate is not asserted to be optimal away from the extremizers.

## Proof

**1. Exact sixth-moment identity.** Diagonalize \(A\), with real eigenvalues \(\lambda_1,\ldots,\lambda_4\) summing to zero. Let \(G\) be standard Gaussian in \(\mathbb R^4\), written \(G=R\omega\), with \(\omega\) uniform on \(S^3\) and independent of \(R\). Then \(\mathbb E R^4=4\cdot6=24\) and \(\mathbb E R^{12}=4\cdot6\cdot8\cdot10\cdot12\cdot14=322560\). The formal moment-generating function of \(Q=G^{\mathsf T}AG\) is
\[
\mathbb E e^{zQ}=\prod_{i=1}^4(1-2z\lambda_i)^{-1/2},
\qquad \log \mathbb E e^{zQ}
=\sum_{j\ge2}\frac{2^{j-1}p_j}{j}z^j.
\]
(The linear term vanishes because \(p_1=0\).) Its cumulants are \(\kappa_j=2^{j-1}(j-1)!p_j\), so the sixth moment and variance are
\[
\mathbb E Q^6=3840p_6+1440p_2p_4+640p_3^2+120p_2^3,
\qquad \mathbb E Q^2=2p_2.
\]
Newton identities for four trace-zero eigenvalues give
\[
p_6=\frac34p_2p_4+\frac13p_3^2-\frac18p_2^3.
\]
Hence \(\mathbb E Q^6=4320p_2p_4+1920p_3^2-360p_2^3\). Divide by the corresponding radial moments and use \(\|Y_A\|_2^2=p_2/12\). This proves the displayed invariant formula without any numerical approximation.

**2. Sharp spectral endpoints.** Scale the eigenvalues so that \(p_2=1\); this does not change the ratio. Cauchy--Schwarz gives \(p_4\ge1/4\), with equality if and only if all four squared eigenvalues equal \(1/4\). The trace-zero condition then forces exactly two positive and two negative eigenvalues; automatically \(p_3=0\). This proves the lower endpoint and every lower equality case. The normalized real trace-free matrices form a connected sphere, and the sixth-moment ratio varies continuously on it. Hence all intermediate values between the attained sharp endpoints occur, proving that the real attainable range is the entire closed interval.

For the upper endpoint, pair the four eigenvalues and parametrize them as
\[
\lambda_1=\tfrac12(s+t),\quad \lambda_2=\tfrac12(s-t),\quad
\lambda_3=\tfrac12(-s+u),\quad \lambda_4=\tfrac12(-s-u).
\]
Then \(1=s^2+(t^2+u^2)/2\), and direct expansion gives
\[
p_3=\frac34s(t^2-u^2),\qquad
p_4=\frac14s^4+\frac34s^2(t^2+u^2)+\frac18(t^4+u^4).
\]
Put \(v=s^2\in[0,1]\). From \(t^2+u^2=2(1-v)\),
\[
p_4\le\frac12+\frac12v-\frac34v^2\le\frac7{12},
\]
and
\[
p_3^2\le\frac94v(1-v)^2\le\frac13.
\]
Both last inequalities become equalities exactly when \(v=1/3\) and one of \(t,u\) vanishes. These conditions give, up to permutation and a common sign, eigenvalues proportional to \((3,-1,-1,-1)\). Substitution in the invariant sixth-moment identity gives \(\mathcal R(A)\le15\), with precisely the stated real upper extremizers.

**3. The complete complex upper endpoint and phase defect.** For \(Y=U+iV\), define \(H_\theta=\Re(e^{-i\theta}Y)=U\cos\theta+V\sin\theta\). Averaging over \(\theta\in[0,2\pi]\),
\[
\mathbb E_\theta\|H_\theta\|_6^6=\frac5{16}\|Y\|_6^6.
\]
Let \(m=(a+b)/2\) and \(r^2=(a-b)^2/4+c^2\), with \(a,b,c\) as above. Then
\[
\mathbb E_\theta\|H_\theta\|_2^6=m^3+\frac32mr^2
=\frac52m^3-\frac32m(ab-c^2).
\]
Applying the proved real upper estimate \(\|H_\theta\|_6^6\le15\|H_\theta\|_2^6\) and averaging yields
\[
\|Y\|_6^6\le15\|Y\|_2^6-36\|Y\|_2^2(ab-c^2).
\]
Cauchy--Schwarz gives \(ab-c^2\ge0\). If equality holds in the sharp complex upper bound, then \(ab=c^2\), forcing \(U,V\) to be real-linearly dependent in \(L^2\). Thus \(Y\) has constant phase times a real harmonic; equality in the real bound then forces the stated zonal form. Conversely every stated zonal complex multiple attains equality. This completes all assertions.

## Verification

The standalone file `check.py` calculates \(S^3\) moments independently by integrating monomials with exact rational coefficients: for nonnegative integers \(k_i\),
\[
\int_{S^3}\prod_{i=1}^4\omega_i^{2k_i}\,d\sigma
=\frac{\prod_{i=1}^4(2k_i-1)!!}{\prod_{j=0}^{K-1}(4+2j)},\qquad K=\sum_{i=1}^4k_i,
\]
with \((-1)!!=1\), while a monomial with any odd exponent integrates to zero. The checker independently tests the trace formula, both endpoint examples, complex off-diagonal forms, the phase-rank inequality, and the pairing identities, using exact arithmetic. Execute `python check.py` with SymPy installed. A successful run prints the number of checks. Finite tests corroborate but do not replace the symbolic universal proof above.

## Relationship to prior work

Dai--Gorbachev--Tikhonov (2019) study Nikolskii/reverse-Hölder estimates for sparse spherical-harmonic degree packets and prove growth-rate estimates rather than exact fixed-degree-two \(L^2\)-to-\(L^6\) constants. Earlier work by Dai--Feng--Tikhonov and by De Carli--Gorbachev--Tikhonov likewise supplies broad norm comparisons without this particular exact two-sided sixth moment or its complex equality classification. A public result on the exact **fourth** moment of quadratic spherical harmonics gives a sharp fourth-power trace bound, but its statement does not give the sixth-moment invariant identity, the real lower endpoint, or the complex sixth-moment phase defect. Related Gaussian second-chaos six-moment literature addresses distributional approximation rather than this precise spherical norm extremum.

## Limitations

This result is restricted to degree-two harmonics on \(S^3\). The lower constant \(27/7\) is claimed only for real-valued harmonics: complex harmonics may have smaller sixth-moment ratios. No dimension-independent sharp constant, higher-degree assertion, or optimality claim for the coefficient of the subsidiary phase-defect term is made. The novelty assessment is literature-dependent; an older equivalent hidden in invariant-theory or spherical-polynomial literature remains possible, and independent audit has not been performed.

## References

1. F. Dai, D. Gorbachev, S. Tikhonov, *Nikolskii inequality for lacunary spherical polynomials*, arXiv:1905.00323v1, publicly posted 2019-05-01; also *Proc. Amer. Math. Soc.* 148 (2020), 1169--1174. https://arxiv.org/abs/1905.00323
2. F. Dai, H. Feng, S. Tikhonov, *Reverse Hölder's inequality for spherical harmonics*, arXiv:1408.1877 (2014). https://arxiv.org/abs/1408.1877
3. L. De Carli, D. Gorbachev, S. Tikhonov, *Pitt and Boas inequalities for Fourier and Hankel transforms*, *J. Math. Anal. Appl.* 408 (2013), 762--774. https://doi.org/10.1016/j.jmaa.2013.06.045
4. *Sharp L4/L2 norm and extremizers for degree-two spherical harmonics*, public mathematical result (2026). https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-sharp-l4-degree-two-spherical-harmonics--d4106097159f
5. E. Azmoodeh, P. Eichelsbacher, C. Thäle, *Optimal Variance--Gamma approximation on the second Wiener chaos*, arXiv:2106.16018 (2021). https://arxiv.org/abs/2106.16018
