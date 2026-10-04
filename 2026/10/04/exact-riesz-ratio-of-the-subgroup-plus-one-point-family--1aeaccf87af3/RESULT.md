# Exact Riesz ratio of the subgroup-plus-one-point family
## Finding
Let
\[
G_m=\mathbb Z_m^2,\qquad
H_m=\mathbb Z_m\times\{0\},\qquad
E_m=H_m\cup\{(0,1)\},
\]
with \(m\ge2\). For an exponential basis partner \(B\) of \(E_m\), Ferguson--Mayeli--Sothanaphan's restriction-class argument shows that exactly one character class on \(H_m\) is represented twice. If the two characters in this repeated class differ by \(k\not\equiv0\pmod m\) in the second coordinate, put
\[
t=\left|1-e^{2\pi i k/m}\right|^2
 =4\sin^2\!\left(\frac{\pi k}{m}\right).
\]

Then the eigenvalues of the Gram matrix \(T(E_m,B)^*T(E_m,B)\) are
\[
\underbrace{m,\ldots,m}_{m-2\text{ times}}
\]
together with the three roots of
\[
p_{m,t}(\lambda)
=\lambda^3-(4m+1)\lambda^2+(4m^2+mt)\lambda-m^2t.
\]
For \(0<t<4\), these three roots satisfy
\[
0<\lambda_1(t)<m<\lambda_2(t)<2m<\lambda_3(t).
\]
Moreover \(\lambda_1(t)\) is strictly increasing and \(\lambda_3(t)\) is strictly decreasing in \(t\). Consequently the same basis partner simultaneously maximizes the lower Riesz constant, minimizes the upper Riesz constant, and minimizes the Riesz ratio: one must maximize \(t\).

Therefore, if \(m\) is even,
\[
L(E_m)=1,\qquad U(E_m)=2m,\qquad \rho(E_m)=2m.
\]
If \(m\) is odd, define
\[
t_m=4\cos^2\!\left(\frac{\pi}{2m}\right),
\]
and let \(\alpha_m\) and \(\gamma_m\) denote the unique roots of \(p_{m,t_m}\) in \((0,m)\) and \((2m,\infty)\), respectively. Then
\[
L(E_m)=\alpha_m,\qquad U(E_m)=\gamma_m,\qquad \rho(E_m)=\frac{\gamma_m}{\alpha_m}.
\]
As \(m\to\infty\) through odd integers,
\[
\rho(E_m)=2m+\frac{\pi}{\sqrt{2m}}+O(m^{-1}),
\]
while for even \(m\) the equality \(\rho(E_m)=2m\) is exact. In particular,
\[
\frac{\rho(E_m)}{2m}\longrightarrow1.
\]

## Assumptions and scope
The tightness quantities are those of Ferguson--Mayeli--Sothanaphan: \(L_E(B)\) and \(U_E(B)\) are the extremal eigenvalues of \(T(E,B)^*T(E,B)\), and \(\rho_E(B)=U_E(B)/L_E(B)\); the set quantities optimize over all exponential basis partners. The result is restricted to the subgroup-plus-one-point family \(E_m\subset\mathbb Z_m^2\).

## Proof
Write \(\omega=e^{2\pi i/m}\). Choose one character from each restriction class on \(H_m\), and let the repeated class have representatives \((s,b_1)\) and \((s,b_2)\). Multiplying columns by unit-modulus constants and permuting columns does not change singular values. After such column scalings, the first \(m\) columns have bottom entry \(1\), while the repeated extra column has bottom entry
\[
z=\omega^{b_2-b_1}=\omega^k.
\]
On the first \(m\) rows, the first \(m\) columns form a Fourier matrix with unit-modulus column factors, and the extra column equals the column from the repeated restriction class. Applying a unitary transformation to those first \(m\) rows reduces the Fourier matrix to \(\sqrt m I_m\). After permuting the repeated class to the first position, the Fourier matrix is unitarily equivalent on the left and right to
\[
A_{m,z}=
\begin{pmatrix}
\sqrt m I_m & \sqrt m e_1\\
1&\cdots&1&z
\end{pmatrix}.
\]

The subspace of coefficient vectors supported on coordinates \(2,\ldots,m\) with coordinate sum zero has dimension \(m-2\), and \(A_{m,z}^*A_{m,z}\) acts there as multiplication by \(m\). On its orthogonal complement, using the ordered basis consisting of the first coordinate, the normalized sum of coordinates \(2,\ldots,m\), and the extra coordinate, the Gram matrix becomes
\[
M_{m,z}=
\begin{pmatrix}
m+1 & \sqrt{m-1} & m+z\\
\sqrt{m-1} & 2m-1 & \sqrt{m-1}\,z\\
m+\overline z & \sqrt{m-1}\,\overline z & m+1
\end{pmatrix}.
\]
Writing
\[
t=|1-z|^2=2-z-\overline z,
\]
direct expansion gives
\[
\det(\lambda I-M_{m,z})
=\lambda^3-(4m+1)\lambda^2+(4m^2+mt)\lambda-m^2t.
\]

For \(0<t<4\), let \(p=p_{m,t}\). We have
\[
p(0)=-m^2t<0,
\]
\[
p(m)=m^2(m-1)>0,
\]
and
\[
p(2m)=m^2(t-4)<0.
\]
Since the Gram matrix is positive definite, all roots are positive, and these signs force exactly one root in each of \((0,m)\), \((m,2m)\), and \((2m,\infty)\). Thus the smallest and largest Gram eigenvalues are \(\lambda_1(t)\) and \(\lambda_3(t)\).

Differentiating the identity \(p_{m,t}(\lambda_j(t))=0\) yields
\[
\frac{d\lambda_j}{dt}
=-\frac{m(\lambda_j-m)}{p'_{m,t}(\lambda_j)}.
\]
At the smallest and largest simple roots, \(p'_{m,t}\) is positive. Hence \(\lambda_1'(t)>0\) and \(\lambda_3'(t)<0\). It follows that \(L_E(B)\) increases, \(U_E(B)\) decreases, and \(\rho_E(B)\) decreases as \(t\) increases. Therefore all three set-level optima occur at the largest possible \(t\).

If \(m\) is even, take \(k=m/2\), so \(t=4\), and
\[
p_{m,4}(\lambda)=(\lambda-1)(\lambda-2m)^2.
\]
This gives
\[
L(E_m)=1,\qquad U(E_m)=2m,\qquad \rho(E_m)=2m.
\]

If \(m\) is odd, the largest chord among \(m\)-th roots is obtained at \(k=(m\pm1)/2\), giving
\[
t_m=4\cos^2\!\left(\frac{\pi}{2m}\right).
\]
This proves the exact root characterization.

For the asymptotic, write
\[
t_m=4-\delta_m,
\qquad
\delta_m=4\sin^2\!\left(\frac{\pi}{2m}\right)
=\frac{\pi^2}{m^2}+O(m^{-4}).
\]
If the largest root is \(2m+x_m\), substitution into the cubic gives the exact equation
\[
x_m^2(2m-1+x_m)=\delta_m m(m+x_m).
\]
It follows first that \(x_m=O(m^{-1/2})\), and then
\[
x_m=\frac{\pi}{\sqrt{2m}}+O(m^{-3/2}).
\]
The smallest root is a simple perturbation of the root \(1\) at \(t=4\), so
\[
\alpha_m=1+O(m^{-2}).
\]
Therefore
\[
\frac{\gamma_m}{\alpha_m}
=2m+\frac{\pi}{\sqrt{2m}}+O(m^{-1}).
\]

## Verification
The accompanying `verify.py` reconstructs the canonical Fourier matrices for many values of \(m\) and \(k\), verifies directly that
\[
\det(\lambda I-T^*T)
=(\lambda-m)^{m-2}p_{m,t}(\lambda)
\]
at multiple test values of \(\lambda\), checks the three root intervals by bisection, verifies the monotonic optimization in \(t\), and confirms the even/odd formulas numerically. It prints `VERIFY_OK`.

The finite computations are consistency checks only. The universal statement follows from the analytic reduction and root monotonicity above.

## Relationship to prior work
Ferguson--Mayeli--Sothanaphan introduce the Riesz tightness quantities and, in their Example 4.19, study exactly the family \(E_m\). They prove the restriction-class structure used above and obtain only
\[
L(E_m)\le2,
\qquad
\rho(E_m)\ge\frac{m+1}{2},
\]
which suffices to show \(\rho(E_m)\to\infty\). Their paper does not give the Gram spectrum, exact set-level Riesz constants, the exact even-modulus value \(\rho(E_m)=2m\), or the sharp asymptotic \(\rho(E_m)\sim2m\).

Targeted exact-form searches and semantic-database searches for the family, its Gram spectrum, and its exact condition number did not return a covering result. Work on Riesz bases for Euclidean multi-tiles concerns a different setting and does not imply this finite-group formula.

## Limitations
For odd \(m\), the exact answer is given by distinguished roots of an explicit cubic rather than by a simplified radical expression. The result is specific to \(E_m\), and no claim is made about general one-point perturbations of subgroups. Unindexed or differently phrased literature remains a residual originality risk.

## References
1. S. Ferguson, A. Mayeli, and N. Sothanaphan, "Riesz bases of exponentials and multi-tiling in finite abelian groups," arXiv:1904.04487, first posted 9 April 2019.
2. C. Frederick and K. A. Okoudjou, "Finding duality for Riesz bases of exponentials on multi-tiles," *Applied and Computational Harmonic Analysis* 51 (2021), 104--117. DOI: 10.1016/j.acha.2020.10.006.
