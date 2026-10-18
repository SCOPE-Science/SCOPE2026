# Exact constrained numerical annuli for planar antiunitaries

## Finding

Let \(A\) be a conjugate-linear operator on \(\mathbb C^2\) satisfying \(\|Ax\|=c\|x\|\) for all \(x\), where \(c>0\). For any orthonormal basis, write \(Ax=M\overline x\). Set
\[
 b=\tfrac12|M_{12}-M_{21}|,\qquad a=\sqrt{c^2-b^2}.
\]
These are basis-independent, with \(0\le a,b\le c\) and \(a^2+b^2=c^2\). For \(q\in\mathbb C\), \(|q|\le1\), define
\[
 W_q(A)=\{\langle Ax,y\rangle:\|x\|=\|y\|=1,\ \langle x,y\rangle=q\}.
\]
Here the complex Hilbert inner product is **linear in its first argument**. Put \(t=|q|\) and \(s=\sqrt{1-t^2}\). The complete range is the **closed** annulus
\[
 \boxed{W_q(A)=\{z\in\mathbb C:r_-(t)\le |z|\le r_+(t)\}},
 \qquad r_-(t)=\max\{0,bs-at\},
\]
where
\[
 \boxed{r_+(t)=\begin{cases}c,&ct\le a,\\ at+bs,&ct\ge a.\end{cases}}
\]
Both branches coincide at the transition. The range contains zero exactly when \(t\ge b/c\). Its maximum modulus equals the operator norm exactly when \(t\le a/c\). Thus two independent transition thresholds describe the disappearance of the hole and the loss of full-norm attainment. The thresholds exchange their order when \(a\) and \(b\) cross.

## Assumptions and scope

The Hilbert space is complex and has dimension exactly two. The operator is antiunitary up to the positive scalar \(c\), not merely an arbitrary antilinear contraction. The parameter \(q\) may be complex, including \(q=0\) and \(|q|=1\). No claim is made for dimension at least three or for antilinear maps with unequal singular values.

In the invariant \(b\), the entries of \(M\) are matrix entries relative to **any** orthonormal basis; this is meaningful because \(M\) transforms by unitary congruence, not unitary similarity. At \(b=0\), the range is the full closed disk of radius \(c\) for every \(q\). At \(a=0\), it is the circle \(\{|z|=c\sqrt{1-|q|^2}\}\), including the singleton at \(|q|=1\). At \(q=0\) its radii are \(b,c\); at \(|q|=1\) it is the disk of radius \(a\).

## Proof

**1. The two invariant parameters and a canonical form.** Write \(M=cV\) with \(V\in U(2)\), and decompose \(M=S+K\) with \(S=(M+M^T)/2\), \(K=(M-M^T)/2\). As every complex skew-symmetric two-by-two matrix is of the form \(\kappa J\), where
\[
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad |\kappa|=b,
\]
we have \(K^*K=b^2I\). Under a unitary basis change \(U\), the matrix becomes \(U^*M\overline U\) and its skew part becomes \(U^*K\overline U=\overline{\det U}\,\kappa J\). Thus \(b\) is basis independent.

Define \(T=V^*V^T\). It is unitary with determinant one. By Cayley–Hamilton in dimension two, \(T+T^*=(\operatorname{tr}T)I\). Therefore
\[
 S^*S=\frac{c^2}{4}\bigl(2I+T+T^*\bigr)=\sigma^2I
\]
for some nonnegative \(\sigma\). Symmetric and skew-symmetric matrices are orthogonal in the Hilbert–Schmidt inner product, so from \(\operatorname{tr}(M^*M)=2c^2\) we obtain \(\sigma^2+b^2=c^2\). Hence \(\sigma=a\).

For \(a>0\), the symmetric matrix \(S/a\) is unitary. Its Takagi factorization gives \(S/a=UU^T\) for some unitary \(U\). After congruence by \(U\), the symmetric part becomes \(aI\), and the skew part is \(\kappa'J\), \(|\kappa'|=b\). Since the full transformed matrix is \(c\) times unitary, its mixed cross term is zero:
\[
 0=(aI)^*(\kappa'J)+(\kappa'J)^*(aI)
   =a(\kappa'-\overline{\kappa'})J.
\]
Thus \(\kappa'\) is real; a real orthogonal reflection makes it equal to \(b\). When \(a=0\), a scalar unitary congruence makes the phase of \(\kappa\) vanish. In every case there is an orthonormal basis in which
\[
 M=\begin{pmatrix}a&b\\-b&a\end{pmatrix},\qquad a,b\ge0,\quad c^2=a^2+b^2.
\]

**2. One-vector overlaps.** In this basis,
\[
 \langle Ax,x\rangle=a(\overline{x_1}^{\,2}+\overline{x_2}^{\,2})
\]
for every unit vector \(x\). Accordingly, \(m=|\langle Ax,x\rangle|\) takes every value in \([0,a]\). For \(a>0\), take \(x=(\cos\theta,i\sin\theta)\), \(0\le\theta\le\pi/4\): then \(m=a\cos(2\theta)\). When \(a=0\) the interval consists only of zero. Always \(\|Ax\|=c\).

**3. Two-vector constraint.** Given a unit \(x\), every allowed \(y\) has the form
\[
 y=\overline q\,x+s e^{i\phi}v,
\]
where \(v\) is a unit vector orthogonal to \(x\), and \(\phi\) is arbitrary. In complex dimension two, \(|\langle Ax,v\rangle|=\sqrt{c^2-m^2}\). Since \(\langle\cdot,\cdot\rangle\) is linear in the first argument,
\[
 \langle Ax,y\rangle=q\langle Ax,x\rangle+s e^{-i\phi}\langle Ax,v\rangle.
\]
Thus, as \(\phi\) varies, the *moduli* for this fixed \(x\) form precisely
\[
 \bigl[\,|tm-s\sqrt{c^2-m^2}|,\quad tm+s\sqrt{c^2-m^2}\,\bigr].
\]
Varying \(m\) over the connected interval \([0,a]\) fills a single closed radial interval: equivalently, the continuous map from the connected compact parameter set of \((m,\phi)\) has a connected compact image under modulus. Simultaneously rotating both \(x,y\) by \(e^{i\eta}\) preserves their mutual inner product and multiplies \(\langle Ax,y\rangle\) by \(e^{-2i\eta}\). Hence every modulus in that interval occurs with all complex phases.

**4. Sharp endpoints.** The outer radius is the maximum of
\[
 f(m)=tm+s\sqrt{c^2-m^2}\quad (0\le m\le a).
\]
By Cauchy–Schwarz, \(f(m)\le c\), with equality exactly at \(m=ct\) when that point lies in \([0,a]\). Beyond it, the maximum is at \(m=a\), giving \(at+bs\). This also holds at \(t=0,1\) by inspection.

For the inner radius, minimize the absolute value of
\[
 g(m)=tm-s\sqrt{c^2-m^2}.
\]
The function \(g\) is increasing on \([0,a]\), with \(g(0)=-sc\) and \(g(a)=at-bs\). Therefore its absolute value has minimum zero precisely when \(at\ge bs\), which is equivalent to \(t\ge b/c\); otherwise its minimum is \(bs-at\). At \(t=1\) the minimum is zero because \(m=0\) is available. This proves both endpoint formulas, their attainability, and the claimed annulus.

## Verification

The supplied standalone script `check.py` reconstructs the canonical matrices, tests the Gram constraint for complex \(q\), and checks explicit extremizers for both radii, including pure symmetric and pure skew boundaries. It is a finite numerical diagnostic only; the theorem follows from the exact argument above. The matrix identity \(S^*S=(c^2-b^2)I\) was separately tested for random complex unitary matrices, with no deviation beyond floating-point roundoff. Neither test establishes the theorem beyond the proof.

## Relationship to prior work

Kołaczek and Müller (2025, arXiv:2508.04347v1, first posted 2025-08-06) study numerical ranges of real-linear and antilinear operators, providing the primary literature motivation. Their ordinary numerical range treats one unit vector, corresponding to \(|q|=1\), rather than the full constrained two-vector family or these radii. Kołaczek and Müller (2024) prove that ordinary antilinear numerical ranges on dimension at least two are disks; that special case is acknowledged and not claimed as new.

Majumdar and Müller (arXiv:2610.16823v1, submitted 2026-10-12) subsequently define the generalized \(q\)-numerical range, prove its circular geometry and note dimension-two annuli with *implicit infimum/supremum radii* in Remark 6.7. Their Example 6.3 treats the purely skew unit antiunitary. Those general annulus and pure-skew assertions are prior coverage, not claimed here. Their paper does **not** supply the explicit two-invariant formulas, the two sharp thresholds, or the general scaled antiunitary classification proved here. Work on \(q\)-numerical ranges of complex-linear operators, including Chien–Nakazato (2005) and later sharp estimates, concerns a different operator class and does not imply this claim by unitary similarity.

## Limitations

This is a dimension-two statement for scalar multiples of antiunitaries only. It does not provide radii for general nonisometric antilinear operators, and it does not address higher-dimensional operators. Its proof uses standard Takagi factorization, not claimed as new. Although relevant published sources and a mathematical research database were compared, earlier equivalent formulas under different parametrizations remain a publication-priority risk. This is a self-review, not independent peer validation.

## References

1. D. Kołaczek and V. Müller, *Real linear operators and numerical ranges*, arXiv:2508.04347v1 (2025-08-06), https://arxiv.org/html/2508.04347v1.
2. D. Kołaczek and V. Müller, *Numerical Ranges of Antilinear Operators*, Integral Equations and Operator Theory **96** (2024), Article 17, https://doi.org/10.1007/s00020-024-02768-5.
3. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823v1 (2026-10-12), https://arxiv.org/html/2610.16823v1 (subsequent related literature comparison).
4. I. Hur and J. E. Lee, *Numerical ranges of conjugations and antilinear operators*, Linear and Multilinear Algebra **69** (2021), 2990–2997, https://doi.org/10.1080/03081087.2019.1702915.
5. M.-T. Chien and H. Nakazato, *The q-numerical ranges of normal operators*, Linear and Multilinear Algebra **53** (2005), 393–416, https://doi.org/10.1080/03081080500156888.
