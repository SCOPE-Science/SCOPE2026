# An exceptional parabolic curvature changes seven-mode Fourier observability by two powers

## Finding

For a real parameter \(a\), a positive time \(T\), and integers \(-N\le n\le N\), define
\[
 \phi_{n,a}(t)=\exp\!\bigl(2\pi i(n^2t+na t^2)\bigr),\qquad
 \Lambda_N(a,T)=\min_{\sum_{n=-N}^{N}|c_n|^2=1}
 \frac1T\int_0^T\left|\sum_{n=-N}^{N}c_n\phi_{n,a}(t)\right|^2dt.
\]
For every fixed \(a\ne0\) and \(N\in\{1,2,3\}\), \(\Lambda_N(a,T)>0\) for every \(T>0\). Put
\[
 r_* = \frac{\sqrt{4603057}-1183}{2880},\qquad
 a_*=2\pi\sqrt{r_*}=3.63226929209483\ldots.
\]
There are positive constants, depending on the fixed nonzero \(a\), bounding the following ratios above and below as \(T\downarrow0\):
\[
 \begin{aligned}
 \Lambda_1(a,T)&\asymp_a T^4,\\
 \Lambda_2(a,T)&\asymp_a T^8,\\
 \Lambda_3(a,T)&\asymp_a T^{12},&& |a|\ne a_*,\\
 \Lambda_3(a,T)&\asymp_a T^{14},&& |a|=a_*.
 \end{aligned}
\]
Thus the first curvature-induced exceptional small-time exponent within the symmetric frequency sections \(\{-N,\dots,N\}\), \(N\le3\), occurs at exactly seven modes. The exceptional curvature increases the exponent of vanishing of the **optimal squared** Riesz lower bound by two, without making the family linearly dependent. When \(a=0\), the functions at \(n\) and \(-n\) coincide, so \(\Lambda_N(0,T)=0\) for all \(N\ge1\) and \(T>0\).

## Assumptions and scope

The observation trajectory is precisely \(x(t)=at^2\); the dispersion relation is \(\omega(n)=n^2\) and the Fourier convention includes \(2\pi\) in the phase. The integral is with respect to normalized time measure \(dt/T\), not arc-length measure. The statement concerns the complex coefficient norm \(\ell^2(\{-N,\ldots,N\})\), fixed \(a\), and the limit \(T\downarrow0\). The implicit comparison constants are not asserted uniform as \(a\) approaches \(0\) or \(\pm a_*\). The first-public motivating paper was submitted on 2026-03-16; the revised version was examined for its statements.

## Proof

**1. Finite analytic jet-rank principle.** Consider \(m\) functions \(f_1,\ldots,f_m\), analytic in a neighborhood of \(0\), and the \(m\)-component jet rows \(A_k=(f_1^{(k)}(0),\ldots,f_m^{(k)}(0))\). Suppose \(q\ge0\) is the smallest integer for which rows \(A_0,\ldots,A_q\) span \(\mathbb C^m\). Then
\[
 \inf_{\|c\|_2=1}\int_0^1\left|\sum_j c_j f_j(Ts)\right|^2ds\asymp T^{2q}
 \quad(T\downarrow0).
\]
For the lower bound, Taylor expansion to order \(q\) gives \(\sum c_jf_j(Ts)=P_{T,c}(s)+O(T^{q+1}\|c\|_2)\), uniformly on \(0\le s\le1\), where
\[
 P_{T,c}(s)=\sum_{k=0}^{q}\frac{T^k}{k!}(A_kc)s^k.
\]
Equivalence of norms on the fixed space of degree-at-most-\(q\) complex polynomials and injectivity of the stacked jet map imply \(\|P_{T,c}\|_{L^2(0,1)}\ge C T^q\|c\|_2\) when \(0<T\le1\). The remainder is one order smaller. For the upper bound, minimality of \(q\) gives a unit vector \(c\) annihilated by all earlier rows (and not by \(A_q\)); its Taylor expansion is \(O(T^q)\) uniformly. This proves both bounds, including when a jet order is missing.

**2. Exact derivatives.** Set \(u=2\pi i\), \(v=2\pi ia\), and \(w=v/u^2=-ia/(2\pi)\). Differentiating the exponential series shows
\[
 \phi_{n,a}^{(k)}(0)=u^k H_k(w;n),\qquad
 H_k(w;n)=k!\sum_{j=0}^{\lfloor k/2\rfloor}
 \frac{w^j n^{2k-3j}}{j!(k-2j)!}.
\]
For \(n=0\), the convention at the constant term is \(H_0(w;0)=1\), and \(H_k(w;0)=0\) for \(k>0\). Since \(u\ne0\), the ranks of the derivative rows equal those of the polynomial rows \((H_k(w;n))_n\).

**3. Determinants for the first three symmetric sections.** Let \(J_N(w)\) have rows \(k=0,\ldots,2N\) and columns \(n=-N,\ldots,N\). Exact integer polynomial algebra gives
\[
 \begin{aligned}
 \det J_1(w)&=-4w,\\
 \det J_2(w)&=17280w^2,\\
 \det J_3(w)&=597196800w^3\bigl(57600w^4-47320w^2-22247\bigr).
 \end{aligned}
\]
At the physical value \(w=-ia/(2\pi)\), put \(r=a^2/(4\pi^2)=-w^2\). For \(a\ne0\), the seven-mode determinant vanishes exactly when
\[
 57600r^2+47320r-22247=0.
\]
The left side is strictly increasing for \(r\ge0\) and has the unique positive root \(r_*\) above. The smaller two sections have no exceptional nonzero \(a\).

**4. The exceptional seven-mode jet is recovered exactly one order later.** In \(J_3(w)\), the six-by-six minor using rows \(0,\ldots,5\) and columns \(n=-3,-2,-1,1,2,3\) equals
\[
 66355200w^3(90w^2-143).
\]
It never vanishes for purely imaginary nonzero \(w\), hence the first six rows always have rank six. Replace the seventh row of \(J_3\) (order six) by the order-seven jet. The resulting determinant is
\[
 83607552000w^3(12600w^4-7369w^2-5272).
\]
At the exceptional value \(w^2=-r_*\), the last parenthesis is
\[
 12600r_*^2+7369r_*-5272
 =-\frac{11929}{4}r_*-\frac{12975}{32}<0.
\]
Therefore rows \(0,\ldots,5,7\) span \(\mathbb C^7\), whereas rows \(0,\ldots,6\) have rank six. The first spanning jet order is \(q=7\) exactly at \(|a|=a_*\), and \(q=6\) at all other nonzero \(a\). The first spanning orders for \(N=1,2\) are \(2,4\), respectively. Applying Step 1 gives the stated exponents.

**5. Every positive observation interval.** In each nonzero-curvature case the displayed finite jet family has full rank. Hence no nonzero combination of the analytic functions can vanish on any positive-length interval. The defining integral is therefore positive for every unit coefficient vector. Compactness of the coefficient sphere makes its minimum positive. At zero curvature the pairs of opposite modes are identical, proving the remaining assertion.

## Verification

The standalone `CHECKER.py` uses only Python's standard library. It computes the five determinant polynomials by exact integer-preserving elimination at eleven distinct integer values of \(w\), including the two seven-mode determinants and the six-row minor. Their polynomial degree bounds are respectively \(1,4,9,9,6\), so eleven agreeing samples certify each identity for all complex \(w\). Executing `python CHECKER.py` produced `PASS` for every identity. This is an exact finite algebra certificate; it does not replace the analytic jet-rank argument for all sufficiently small positive \(T\).

As a separate numerical diagnostic (not used for proof), high-precision Hermitian Gram-matrix eigenvalues were computed for \(a=1\) and \(a=a_*\) over several small time windows; they were consistent with the claimed leading powers. The certificate intentionally excludes arbitrary-precision quadrature and external dependencies.

## Relationship to prior work

Haak, Jaming, Wang and Wang study curved Ingham inequalities for the same dispersive Fourier family. Their revised preprint proves qualitative finite-frequency lower bounds for a positive observation interval, and treats a three-mode Wronskian. Their displayed small-time obstruction gives an upper restriction of order \(T^2\) from a two-mode test, but does not classify the smallest eigenvalue for the symmetric seven-mode section or identify the isolated curvature at which its decay rate changes. The current result is a finer, fixed-seven-mode small-time classification, not a deduction of a new infinite-frequency Ingham theorem. Classical Ingham inequalities for separated affine frequencies address a different geometry.

## Limitations

No uniform estimate in the curvature parameter is claimed, nor any result for arbitrary analytic curves, arbitrary dispersion exponents, or symmetric sections with \(N\ge4\). The power laws are two-sided asymptotic orders, not explicit sharp leading coefficients. The general jet-rank principle is elementary finite-dimensional analysis; the nontrivial classified invariant is the first nonzero curvature resonance and its exact impact on the seven-mode observation exponent. The source comparison cannot exclude implicit equivalent coverage in unindexed older work.

## References

1. Bernhard H. Haak, Philippe Jaming, Ming Wang, and Yunlei Wang, *Curved Ingham Inequalities for Dispersive Trigonometric Sums*, arXiv:2603.15193, first publicly submitted 2026-03-16, revised 2026-09-28. https://arxiv.org/abs/2603.15193 . Sections 1, 3.2, 4 and Appendix B of the revised full text were inspected.
2. A. E. Ingham, *Some trigonometrical inequalities with applications to the theory of series*, Math. Z. 41 (1936), 367–379, as cited in reference 1. Background, not an asserted full-text inspection.
3. Jiaqi Yu and Shanlin Huang, *Fractal Turán–Nazarov Inequality and Observability for Schrödinger Equations*, arXiv:2607.17505 (2026). Abstract-level context only; the full text was not inspected. https://arxiv.org/abs/2607.17505 .
