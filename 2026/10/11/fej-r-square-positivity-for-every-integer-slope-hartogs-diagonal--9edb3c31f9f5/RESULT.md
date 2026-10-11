# Fejér-square positivity for every integer-slope Hartogs diagonal kernel

## Finding

For each integer \(m\ge2\), write \(d=m-1\). Let
\[
\mathbb H_m=\{(z_1,z_2)\in\mathbb C^2: |z_1|^m<|z_2|<1\}
\]
and denote its Bergman kernel by \(K_m\). In the standard rational formula of Edholm and Mathew [1], put \(s=z_1\overline{w_1}\), \(t=z_2\overline{w_2}\), and let \(P_{m,1}(s,t)\) be the numerator. Define
\[
Q_{m,1}(s)=s^{-1}P_{m,1}(s,s).
\]
Then for every \(|\zeta|=1\),
\[
\boxed{\zeta^{-d}Q_{m,1}(\zeta)
=d+(d+2)\Big|\sum_{j=0}^{d-1}\zeta^j\Big|^2
+\Big|\sum_{j=0}^{d}\zeta^j\Big|^2>d.}
\]
Consequently \(Q_{m,1}\) has no unit-circle roots, and has exactly \(d\) roots in \(0<|s|<1\) and \(d\) in \(|s|>1\), with multiplicities. Every inner root gives a zero of \(K_m\) realized by points inside \(\mathbb H_m\). The result settles the integer-slope family of Conjecture 4.20 in [1] for arbitrary, unbounded \(d\).

## Assumptions and scope

All polynomials use the precise numerator normalization in [1, Theorem 1.3]:
\[
K_m(z,w)=\frac{P_{m,1}(s,t)}{m\pi^2(1-t)^2(t-s^m)^2}.
\]
The restricted diagonal is the complex line \(s=t\) in the holomorphic-factor coordinates \((s,t)\); it is **not** the Hermitian point diagonal \(z=w\), where a Bergman kernel is necessarily positive. The variable \(s\) ranges over the punctured unit disk. All root counts include algebraic multiplicities; no root simplicity is asserted.

## Proof

**1. Exact finite polynomial.** For \(n=1\) and \(0\le j\le m-2=d-1\), the integer functions in [1, Theorem 1.3] specialize to
\[
L(j)=\left\lceil\frac{j+2}{m}\right\rceil=1,
\qquad \kappa(j)=m+j-m=j.
\]
Therefore the five-part numerator formula of [1], after setting \(t=s\) and dividing by \(s\), gives the finite, exact identity
\[
\begin{aligned}
Q_{m,1}(s)={}&(d+1)^2s^d+\sum_{j=0}^{d-1}\big[
(j+1)^2s^j+(j+1)(d-j)s^{j+1}\\
&\hspace{27mm}+(j+1)(d-j)s^{j+d}+(d-j)^2s^{j+d+1}\big].
\end{aligned}
\]
Writing \(Q_{m,1}(s)=\sum_{k=0}^{2d}a_ks^k\), direct collection of the displayed summands yields
\[
a_k=1+(d+3)k\quad(0\le k<d),\qquad
 a_d=d^2+4d+1,\qquad a_{2d-k}=a_k\quad(0\le k<d).
\]
For example, at \(1\le k<d\), the two contributions on the low-degree side are \((k+1)^2+k(d-k+1)=1+(d+3)k\); the central three contributions are \((d+1)^2+d+d\). The high-degree coefficients follow by direct reversal of the two reflected summands. In particular, \(a_0=a_{2d}=1\), the degree is exactly \(2d\), and \(Q_{m,1}\) is palindromic.

**2. Sum-of-squares identity.** Define the nonnegative Fejér polynomials on \(|\zeta|=1\) by
\[
F_r(\zeta)=\left|\sum_{j=0}^{r-1}\zeta^j\right|^2
=\sum_{h=-(r-1)}^{r-1}(r-|h|)\zeta^h,\qquad r\ge1.
\]
The constant Fourier coefficient of \(d+(d+2)F_d+F_{d+1}\) equals \(d+(d+2)d+(d+1)=d^2+4d+1=a_d\). For \(1\le h\le d-1\), its coefficients at \(\zeta^{\pm h}\) are
\[
(d+2)(d-h)+(d+1-h)=1+(d+3)(d-h)=a_{d-h}=a_{d+h}.
\]
The coefficients at \(\zeta^{\pm d}\) are \(1=a_0=a_{2d}\). Comparing every Fourier coefficient therefore proves the boxed identity for *every* integer \(d\ge1\), not just a finite set of examples.

It is at least \(d>0\) because both squared moduli are nonnegative. In fact it is strictly greater than \(d\): simultaneous vanishing of the two consecutive geometric sums would require a unit \(\zeta\ne1\) satisfying \(\zeta^d=\zeta^{d+1}=1\), implying \(\zeta=1\), where neither sum vanishes.

**3. Exact root count.** Since \(a_0=a_{2d}=1\), zero is not a root and the polynomial is reciprocal:
\[
Q_{m,1}(s)=s^{2d}Q_{m,1}(s^{-1}).
\]
Thus every root away from the unit circle is paired with its reciprocal, with the same multiplicity. The sum-of-squares identity excludes roots on the circle. The \(2d\) nonzero complex roots therefore split into precisely \(d\) roots of modulus less than one and \(d\) of modulus greater than one, counted with multiplicity.

**4. Realization as interior kernel zeros.** If \(s=re^{i\phi}\) is one of the interior roots, \(0<r<1\), take
\[
z=(\sqrt r\,e^{i\phi},\sqrt r\,e^{i\phi}),\qquad
w=(\sqrt r,\sqrt r).
\]
Both points belong to \(\mathbb H_m\), since \(r^{m/2}<r^{1/2}<1\), and satisfy \(z_1\overline{w_1}=z_2\overline{w_2}=s\). Moreover \(1-s\ne0\) and \(s-s^m\ne0\) for \(0<|s|<1\). Hence the Bergman denominator is nonzero while \(P_{m,1}(s,s)=sQ_{m,1}(s)=0\), giving the asserted genuine zero.

## Verification

The standalone, standard-library script `check_integer_hartogs.py` independently reconstructs the diagonal polynomial from the five pieces of [1, Theorem 1.3], from the older kernel formula [2, Theorem 1.2], from the displayed closed coefficients, and from the finite Fejér Fourier coefficients. Executing `python3 check_integer_hartogs.py` verified exact integer coefficient agreement, degrees, and reciprocity for each \(2\le m\le501\) (500 integers). These finite tests are cross-checks only; the all-integer conclusion is proved by the unrestricted coefficient comparison above.

## Relationship to prior work

Edholm and Mathew [1, Theorem 1.5] prove reciprocal symmetry for all coprime rational slopes and [1, Theorem 1.7] establish their unit-circle conjecture for differences \(m-n=1,2\). Their Section 4.3 describes separate results for differences \(3,4,6\) and poses the general zero-free-circle question as Conjecture 4.20. Those fixed-difference results do not cover the unbounded family \((m,n)=(m,1)\) as \(m\to\infty\). The present identity is a concrete structural square decomposition for that entire axis.

Edholm's earlier exact formula [2] and Edholm--McNeal [3] establish existence of Bergman-kernel zeros for integer \(m\), and indeed the broader range of exponents at least two, respectively. They do **not** provide this complete root count on the specified section or a Fejér positivity identity there. Almughrabi [4] provides another explicit finite formula for the same class of kernels, not an interior-root census. In particular, kernel zero existence does not imply \(Q_{m,1}\) has no unit-circle root or that it has exactly \(m-1\) interior roots.

## Limitations

This proves the axis \(n=1\), not the entire rational-slope conjecture. No assertion is made about the simplicity or geometric location of individual roots, other kernel-zero components, or an optimal uniform circle margin. The integer-slope kernel-zero *existence* was previously known; the new information is the exact infinite-family restricted-root census and its positive-squares certificate. Possible unindexed or unpublished equivalent arguments remain an originality risk.

## References

[1] L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489 (first public 2025-05-26), Theorems 1.3, 1.5, 1.7 and Section 4.3; Math. Z. 313 (2026), 43, DOI 10.1007/s00209-026-04059-8.

[2] L. D. Edholm, *Bergman theory of certain generalized Hartogs triangles*, arXiv:1504.07914, Theorem 1.2, Corollary 4.2, Remark 4.5; Pacific J. Math. 284 (2016), 327–342.

[3] L. D. Edholm and J. D. McNeal, *Bergman subspaces and subkernels: degenerate Lp mapping and zeroes*, arXiv:1605.06223, Theorem 2.27; J. Geom. Anal. 27 (2017), 2658–2683.

[4] R. Almughrabi, *Bergman Kernels of Two Dimensional Monomial Polyhedra*, arXiv:2303.14268, Proposition 2; Complex Anal. Oper. Theory 17 (2023), 103.
