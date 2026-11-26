# Exact outer boundary of the \(q\)-numerical disk of an antilinear isometry

## Finding

Let \(H\) be a complex Hilbert space of dimension at least three, with inner product linear in its first variable. Let \(A:H\to H\) be conjugate-linear and satisfy \(\|Ax\|=\sigma\|x\|\) for a fixed \(\sigma>0\). Surjectivity is not required. For \(|q|\le1\) put
\[
 W_q(A)=\{\langle Ax,y\rangle:\|x\|=\|y\|=1,\;\langle x,y\rangle=q\},\qquad
 \alpha=\sigma^{-1}\sup_{\|x\|=1}|\langle Ax,x\rangle|.
\]
Writing \(r=|q|\), the set is a centered disk of outer radius
\[
 R=\sigma\begin{cases}
 1,&0\le r\le\alpha,\\
 \alpha r+\sqrt{1-\alpha^2}\sqrt{1-r^2},&\alpha\le r\le1.
 \end{cases}
\]
It contains its boundary exactly when \(r<\alpha\) or some unit vector attains the ordinary numerical radius \(w(A)=\sigma\alpha\). The zero-radius disk is \(\{0\}\). For each prescribed \(a\in(0,1)\), an infinite-dimensional antiunitary with \(\alpha=a\) has a closed disk for \(r<a\) and an open disk for \(r\ge a\), including the transition point.

## Assumptions and scope

The dimension may be infinite or nonseparable. This is a statement about constant-norm conjugate-linear maps, not general antilinear operators. It includes \(q=0\) and \(|q|=1\). The two-dimensional annulus is not part of the claim.

## Proof

**Overlap interval.** On a complex two-plane the form \(x\mapsto\langle Ax,x\rangle\) is a homogeneous quadratic in the conjugated coordinates. Any homogeneous binary quadratic over \(\mathbb C\) vanishes on a nonzero vector (including when the polynomial is identically zero). Thus there is an isotropic unit vector. Continuity and path connectedness of the unit sphere imply that the possible normalized overlaps \(d=|\langle Ax,x\rangle|/\sigma\) fill \([0,\alpha)\), with \(\alpha\) added exactly when it is attained. When \(\alpha=0\), the overlap set is \(\{0\}\).

**Constrained maximum.** Write \(s=\sqrt{1-r^2}\). Each allowed pair has \(y=\overline q x+su\) with \(u\) a unit vector perpendicular to \(x\); for \(s=0\), the choice of \(u\) is irrelevant. The perpendicular component of \(Ax\) has norm \(\sigma\sqrt{1-d^2}\). Cauchy–Schwarz gives
\[
 |\langle Ax,y\rangle|\le \sigma\bigl(rd+s\sqrt{1-d^2}\bigr).
\]
For fixed \(x\) equality is attained by aligning \(u\) with that component and choosing its phase, or automatically if the component or \(s\) vanishes. Put \(r=\cos\theta\) and \(d=\cos\varphi\) with \(\theta,\varphi\in[0,\pi/2]\). The normalized right hand side is \(\cos(\theta-\varphi)\), whose unique maximum over \(d\in[0,\alpha]\) occurs at \(d=\min(r,\alpha)\). Evaluating it gives the formula for \(R\). For \(r<\alpha\), the maximizing overlap is present. For \(r\ge\alpha\), the unique maximizing overlap is \(\alpha\), so boundary attainment is equivalent to attainment of \(w(A)\).

**Disk and endpoints.** For an isotropic unit vector \(x\), choose a unit \(u\perp x,Ax\), so that zero occurs. If \(s>0\), the unit-pair parameter space is the space of orthonormal two-frames \((x,u)\). Two such frames lie in a common finite-dimensional span and a unitary there carries one to the other; diagonalizing the unitary and continuously varying its eigenvalue arguments gives a path. If \(s=0\), the parameter space is the unit sphere. Consequently the attained moduli form an interval containing zero and all moduli strictly below \(R\). Simultaneously multiplying \(x,y\) by \(e^{i\phi}\) preserves \(q\) and multiplies the coefficient by \(e^{-2i\phi}\). This gives every argument at each attained radius. If \(R=0\), the formula forces \(r=1,\alpha=0\); then every unit vector attains \(w(A)=0\).

**Open disks at and beyond the threshold.** Fix \(0<a<1\), take \(a_j=a(1-2^{-j})\) for \(j\ge1\), write \(J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\), and let \(C\) denote coordinate conjugation. Use
\[
 A=\bigoplus_{j\ge1}\bigl(a_j I+\sqrt{1-a_j^2}\,J\bigr)C
 \quad\text{on }\bigoplus_{j\ge1}\mathbb C^2.
\]
Each real matrix here is orthogonal, so \(A\) is antiunitary. On each block the diagonal coefficient is \(a_j(\bar x_1^2+\bar x_2^2)\); the skew contribution vanishes. Vectors supported on one coordinate of one block give \(w(A)\ge\sup_j a_j=a\). Every unit vector \(x=(x_j)\) has \(|\langle Ax,x\rangle|\le\sum_j a_j\|x_j\|^2<a\), because at least one component with \(a_j<a\) has positive mass. This proves the asserted nonattaining transition.

## Verification and limits

The proof is symbolic and uses no sampling. As exact checks, for \(a=3/5\) in the displayed direct sum, \(r=0\) gives the closed unit disk, \(r=3/5\) gives the open unit disk, \(r=4/5\) gives the open disk of radius \(24/25\), and \(r=1\) gives the open disk of radius \(3/5\). These examples illustrate the distinction between a plateau for the supremum and attainment of that supremum at its last point.

## Relationship to prior work

Majumdar–Müller, arXiv:2610.16823v1, §6, Proposition 6.2 and Theorem 6.6, establish the qualitative disk geometry in dimension at least three for arbitrary antilinear maps, without computing the radius law or the criterion for an open boundary. Kołaczek–Müller, *Numerical Ranges of Antilinear Operators* (2024), DOI 10.1007/s00020-024-02768-5, §2, covers the ordinary endpoint \(|q|=1\). The explicit planar radius and transition formulas are already in *Exact constrained numerical annuli for planar antiunitaries* (Resultary `6b0114c92bf7`) and are not asserted here. A closely overlapping record dated later than the original higher-dimensional finding, *Sharp q-numerical disks and boundary attainment for antiunitary operators* (Resultary `19a402838a5b`), gives the same law, attainment criterion, and direct-sum mechanism for surjective isometries. This comparison does not infer independence or priority from the dates. The full text of Jia–Liu (2025), DOI 10.4153/S000843952500044X, was not available for comparison; its accessible abstract concerns ordinary numerical ranges. Literature-wide priority is not asserted.
