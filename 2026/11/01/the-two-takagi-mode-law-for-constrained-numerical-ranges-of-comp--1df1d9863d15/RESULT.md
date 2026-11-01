# The two-Takagi-mode law for constrained numerical ranges of compact symmetric antilinear operators

## Finding
Let \(H\) be a complex Hilbert space of dimension at least two, and let \(A:H\to H\) be a compact antilinear operator with \(\langle Ax,y\rangle=\langle Ay,x\rangle\) for all vectors (inner products are linear in the first variable). Write \(\sigma_1\ge\sigma_2\ge\sigma_3\ge\cdots\ge0\) for the Takagi singular values of \(A\), with zeros appended as necessary. For every \(q\in\mathbb C\) with \(|q|\le1\), the constrained numerical range
\[
W_q(A)=\{\langle Ax,y\rangle:\|x\|=\|y\|=1,\ \langle x,y\rangle=q\}
\]
is **exactly** the closed disk centered at zero with radius
\[
R_q(A)=\frac{(1+|q|)\sigma_1+(1-|q|)\sigma_2}{2}.
\]
This gives a two-mode spectral law in every finite dimension and for compact symmetric antilinear operators in infinite dimension. If \(\sigma_2>\sigma_3\) and \(|q|<1\), every maximizing pair \((x,y)\) spans the top-two Takagi singular subspace. The singular-value gap assumption is only for this rigidity conclusion, not for the disk formula.

## Assumptions and scope
The antilinear adjoint is defined by \(\langle Ax,y\rangle=\langle A^\#y,x\rangle\), so the hypothesis is \(A=A^\#\). For matrices this is precisely \(A z=M\overline z\) with \(M=M^{\mathsf T}\). Compact Takagi factorization provides an orthonormal basis in which \(A(x_j)_j=(\sigma_j\overline{x_j})_j\). For a space of dimension two, put \(\sigma_3=0\) solely when interpreting the rigidity hypothesis. The zero operator is included. No claim is made for general nonsymmetric antilinear operators or for noncompact operators.

## Proof
**Step 1: reduce the phase.** Multiplying \(y\) by a unimodular scalar rotates both \(q=\langle x,y\rangle\) and \(\langle Ax,y\rangle\) by that scalar. We may therefore calculate the moduli with \(q=\rho\in[0,1]\), where \(\rho=|q|\). Multiplying both \(x\) and \(y\) by the same unimodular scalar preserves \(q\) and rotates the antilinear value through every argument; hence \(W_q(A)\) is circularly symmetric.

**Step 2: the sharp upper bound.** Suppose \(0\le\rho<1\), and put \(b_+=(1+\rho)/2\), \(b_-=(1-\rho)/2\). Every constrained unit pair can be written
\[
x=\sqrt{b_+}\,u+\sqrt{b_-}\,v,\qquad
y=\sqrt{b_+}\,u-\sqrt{b_-}\,v,
\]
for orthonormal vectors \(u,v\). Since \(A\) is symmetric antilinear, the cross terms cancel and
\[
\langle Ax,y\rangle=b_+\langle Au,u\rangle-b_-\langle Av,v\rangle.
\]
In a Takagi basis define the positive diagonal operator \(D\) by \(De_j=\sigma_j e_j\). The triangle inequality gives \(|\langle Au,u\rangle|\le\langle Du,u\rangle\) and likewise for \(v\). The Ky Fan variational inequalities yield
\[
\begin{aligned}
|\langle Ax,y\rangle|
&\le b_+\langle Du,u\rangle+b_-\langle Dv,v\rangle\\
&=b_-\bigl(\langle Du,u\rangle+\langle Dv,v\rangle\bigr)
 +(b_+-b_-)\langle Du,u\rangle\\
&\le b_-(\sigma_1+\sigma_2)+(b_+-b_-)\sigma_1\\
&=b_+\sigma_1+b_-\sigma_2.
\end{aligned}
\]
This argument is valid for compact operators on infinite-dimensional Hilbert spaces as well as for matrices. If \(\rho=1\), the constraint forces \(y=x\) up to phase, and the same bound follows from \(|\langle Ax,x\rangle|\le\sigma_1\).

**Step 3: attainment.** Let \(e_1,e_2\) be two orthonormal Takagi vectors for the largest singular values. Set
\[
x=\sqrt{b_+}\,e_1+i\sqrt{b_-}\,e_2,\qquad
y=\sqrt{b_+}\,e_1-i\sqrt{b_-}\,e_2.
\]
Both vectors have norm one, \(\langle x,y\rangle=\rho\), and direct substitution gives
\[
\bigl|\langle Ax,y\rangle\bigr|=b_+\sigma_1+b_-\sigma_2.
\]
For complex \(q\) change the phase of \(y\); this does not change the modulus. The same vectors also cover the endpoint \(\rho=1\). Thus the supremum is a maximum with the displayed radius.

**Step 4: the center and all intervening radii.** If \(\sigma_1=0\) the conclusion is immediate. If \(\sigma_2=0\), take \(x=e_2\) in the kernel and any unit \(y\) with the required inner product to obtain zero. Now suppose \(\sigma_1,\sigma_2>0\). In the span of \(e_1,e_2\), put \(x_\theta=\cos\theta\,e_1+i\sin\theta\,e_2\), and choose its perpendicular unit vector \(v_\theta=i\sin\theta\,e_1+\cos\theta\,e_2\). With \(\eta=\sqrt{1-\rho^2}\), all admissible partners have the form \(y=\rho x_\theta+\eta e^{i\varphi}v_\theta\). Direct calculation gives
\[
|\langle Ax_\theta,x_\theta\rangle|=|\sigma_1\cos^2\theta-\sigma_2\sin^2\theta|,
\quad
|\langle Ax_\theta,v_\theta\rangle|=(\sigma_1+\sigma_2)\cos\theta\sin\theta.
\]
For \(0<\rho<1\), the difference between \(\rho\) times the first modulus and \(\eta\) times the second starts positive at \(\theta=0\) and is negative where \(\tan^2\theta=\sigma_1/\sigma_2\). At an intermediate angle it vanishes; choosing \(\varphi\) for destructive interference gives \(\langle Ax_\theta,y\rangle=0\). For \(\rho=0\) take \(x=e_1,y=e_2\); for \(\rho=1\) use the angle at which the first modulus vanishes.

The space of constrained unit pairs is path connected: when \(|q|<1\), represent each as an orthonormal two-frame, then join the frames by a continuous path of unitaries; for \(|q|=1\) use the unit sphere. Hence the continuous modulus function takes every value between the attained minimum zero and the attained maximum \(R_q(A)\). Circular symmetry from Step 1 gives the entire closed disk, with no missing boundary points.

**Step 5: rigidity.** Assume \(|q|<1\) and \(\sigma_2>\sigma_3\). Both \(b_+\) and \(b_-\) are positive. Equality in the sharp bound forces equality in the Ky Fan sum \(\langle Du,u\rangle+\langle Dv,v\rangle\le\sigma_1+\sigma_2\). The strict second-to-third singular-value gap implies \(\operatorname{span}\{u,v\}\) is exactly the top-two Takagi subspace. Since \(\operatorname{span}\{x,y\}=\operatorname{span}\{u,v\}\), the maximizing pair has the claimed two-mode support. This does not require distinct first and second singular values.

## Verification
Run `python3 verify_q.py` using only the Python standard library. The included deterministic program passed 83,568 finite assertions for diagonal Takagi models in dimensions two, three, five and nine, including random admissible pairs, exact maximizing pairs and zero-valued witnesses. These checks confirm selected algebra and boundary cases; the operator theorem and rigidity rely on the proof above, not on finite enumeration.

## Relationship to prior work
Majumdar and Müller (arXiv:2610.16823v1, Section 6, 12 October 2026) introduce the antilinear constrained \(q\)-numerical range, prove its disk shape in dimensions at least three, and give a dimension-two annulus description and a skew antiunitary exception. They do not supply the present sharp two-singular-value radius for arbitrary compact symmetric antilinear operators or its maximizing-frame rigidity. Kołaczek and Müller (2024) establish disk geometry for the ordinary antilinear numerical range, corresponding here to \(|q|=1\). Classical Takagi factorization and Ky Fan inequalities are used explicitly as ingredients, not claimed as new.

## Limitations
The result is confined to compact antilinearly self-adjoint operators on a complex Hilbert space of dimension at least two. The disk radius can be computed from two Takagi singular values; it says nothing about the full constrained range of nonsymmetric antilinear operators. Rigidity requires a strict spectral gap below the second singular value. No independent scientific audit or publication-priority determination has been performed. Equivalence hidden in older constrained-bilinear-form literature remains a residual originality risk.

## References
1. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823v1 (12 October 2026), especially Section 6. https://arxiv.org/html/2610.16823
2. D. Kołaczek and V. Müller, *Numerical Ranges of Antilinear Operators*, Integral Equations and Operator Theory 96, article 17 (2024), DOI:10.1007/s00020-024-02768-5. https://doi.org/10.1007/s00020-024-02768-5
3. D. Kołaczek and V. Müller, *Real linear operators and numerical ranges*, arXiv:2508.04347 (2025). https://arxiv.org/abs/2508.04347
4. Standard Autonne–Takagi factorization for complex symmetric compact operators and the Ky Fan maximum principle; used as classical linear-algebra inputs.
