# Exact quadratic Shapiro coefficient-sum norm and rigidity

## Finding
Let \(p(z)=a_0+a_1z+a_2z^2\) be a complex polynomial and define \(\|p\|_{\infty}=\max_{|z|=1}|p(z)|\). Then the first unresolved odd-length case of the coefficient-partial-sum problem has the exact constant
\[
\max_{\|p\|_{\infty}\le1}|a_0+a_1|=\frac{2}{\sqrt3}.
\]
Equality holds **if and only if**
\[
p(z)=e^{i\phi}\frac{2+4z-z^2}{3\sqrt3},\qquad \phi\in\mathbb R.
\]
Equivalently, the functional with coefficient vector \((1,1,0)\) on complex polynomials of degree at most two has norm \(2/\sqrt3\), with a unique norm-one extremizer modulo scalar phase.

## Assumptions and scope
All polynomial coefficients may be complex; there are no sign, reality, or root-location restrictions. The degree bound is **at most two** (including lower-degree cases). Norms are taken on the closed complex unit disk; the maximum-modulus principle identifies this with the circle norm used above. The asserted equality classification covers all admissible polynomials, including possible vanishing coefficients.

## Proof
**1. An exact two-node interpolation certificate.** Put
\[
\zeta=e^{i\pi/3}=\frac{1+i\sqrt3}{2},\qquad
\lambda=\frac{e^{-i\pi/6}}{\sqrt3}=\frac12-\frac{i}{2\sqrt3}.
\]
The three identities
\[
\lambda+\overline\lambda=1,\quad
\lambda\zeta+\overline\lambda\,\overline\zeta=1,\quad
\lambda\zeta^2+\overline\lambda\,\overline\zeta^2=0
\]
imply, for every complex polynomial of degree at most two,
\[
a_0+a_1=\lambda p(\zeta)+\overline\lambda\,p(\overline\zeta).
\]
Consequently,
\[
|a_0+a_1|\le2|\lambda|\|p\|_{\infty}
=\frac{2}{\sqrt3}\|p\|_{\infty}.
\]
This proves the global upper bound **without** any reality assumption.

**2. Exact attainment.** Define
\[
p_*(z)=\frac{2+4z-z^2}{3\sqrt3}.
\]
For \(z=e^{it}\) and \(x=\cos t\), elementary expansion yields
\[
|2+4e^{it}-e^{2it}|^2=27-8\left(x-\frac12\right)^2\le27.
\]
Equality is attained precisely when \(\cos t=1/2\), i.e. at \(\zeta\) and \(\overline\zeta\). Thus \(\|p_*\|_{\infty}=1\), while \(a_0+a_1=6/(3\sqrt3)=2/\sqrt3\). This proves sharpness.

**3. Rigidity of equality.** Suppose \(\|p\|_{\infty}\le1\) and \(|a_0+a_1|=2/\sqrt3\). Multiplying \(p\) by a unimodular constant, assume \(a_0+a_1=2/\sqrt3\). Equality in both triangle and evaluation bounds from step 1 forces
\[
p(\zeta)=e^{i\pi/6}=p_*(\zeta),\qquad
p(\overline\zeta)=e^{-i\pi/6}=p_*(\overline\zeta).
\]
Therefore \(p-p_*=c(z^2-z+1)\) for a single complex number \(c\). Because \(|p|\le1\) and \(|p|=1\) at these two nodes, the angular derivatives of \(|p(e^{it})|^2\) vanish at \(t=\pm\pi/3\). The same holds for \(p_*\). Using
\[
\frac{d}{dt}|p(e^{it})|^2
=2\operatorname{Re}\bigl(i e^{it}p'(e^{it})\overline{p(e^{it})}\bigr),
\]
we obtain the two real equations
\[
\operatorname{Re}\!\left[\left(-\frac32-\frac{i\sqrt3}{2}\right)c\right]=0,
\qquad
\operatorname{Re}\!\left[\left(\frac32-\frac{i\sqrt3}{2}\right)c\right]=0.
\]
Writing \(c=u+iv\), these respectively read \(-3u+\sqrt3v=0\) and \(3u+\sqrt3v=0\). Hence \(u=v=0\) and \(p=p_*\). Undoing the scalar normalization proves the equality classification.

## Verification
The standalone `verify.py` checks the three interpolation identities exactly over \(\mathbb Q(\sqrt3,i)\), the complete unit-circle squared-modulus identity, sharp contact values, and the nonsingular real stationarity system. It requires Python 3 with SymPy and reports `PASS` on success. The analytic proof in the preceding section covers every complex quadratic polynomial; finite tests are not the basis of the universal claim.

## Relationship to prior work
This is the parameter choice \((n,d)=(1,3)\) in Shapiro's partial-sum problem. Technau, *Shapiro's problem on polynomials with large partial sums of coefficients* (arXiv:2603.24405, first submitted March 25, 2026; journal publication June 10, 2026), states in Example 2.10 only the upper bound \(\mathscr M_{1,3}\le1/2+1/\sqrt2\). The proved constant \(2/\sqrt3\) is strictly smaller and sharp, and the equality classification is new to the comparison with that paper. Technau's Theorems 2.5 and 2.6 solve different periodic or alternating coefficient functionals; his cited Newman theorem covers \(d=2(n+1)\), not \(d=3\). The proof uses the general kind of norm-attaining boundary-node functional introduced by Shapiro, but computes the exact nodes and the unique extremizer in this concrete case.

## Limitations
No assertion is made for degree three or higher, other coefficient vectors, or infinite-dimensional holomorphic function classes. The result does not solve Shapiro's problem in general. An exhaustive historical priority examination of every early thesis and related operator-functional article was not possible; the available recent primary source explicitly described its bound for this very parameter as an upper bound rather than an exact value.

## References
1. Marc Technau, *Shapiro's problem on polynomials with large partial sums of coefficients*, arXiv:2603.24405 (March 25, 2026), **Forum of Mathematics, Sigma** 14 (2026), e69, DOI: 10.1017/fms.2026.10213. See Problem 1.1, Theorems 1.3, 2.5, 2.6, Corollary 2.8 and Example 2.10. https://arxiv.org/abs/2603.24405
2. H. S. Shapiro, *Extremal problems for polynomials and power series*, PhD thesis, Massachusetts Institute of Technology, 1952; the general boundary-node approach is summarized in reference 1, Section 2.2.
3. D. J. Newman, *Polynomials with large partial sums*, **Journal of Approximation Theory** 23 (1978), 187–190, DOI: 10.1016/0021-9045(78)90106-5; exact even-length case as stated in reference 1, Theorem 1.3.
4. W. W. Rogosinski, *Linear functionals on bounded polynomials of given order*, **Mathematica Scandinavica** 10 (1962), 53–70, DOI: 10.7146/math.scand.a-10513; bibliographic identification only, full text not inspected here.
