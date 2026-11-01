# Exact numerical annuli and dual transitions for two-dimensional antiunitaries

## Finding

Let \(A\) be any antiunitary operator on the two-dimensional complex Hilbert space \(\mathbb C^2\), with inner product linear in its first argument. For every \(q\in\mathbb C\) with \(|q|\le1\), define
\[
W_q(A)=\{\langle Ax,y\rangle:\|x\|=\|y\|=1,\ \langle x,y\rangle=q\}.
\]
The square \(A^2\) is a complex-linear unitary matrix, and its trace is real in \([-2,2]\). Define the conjugacy invariants
\[
b=\frac12\sqrt{2-\operatorname{tr}(A^2)},\qquad
 a=\sqrt{1-b^2},\qquad r=|q|,\qquad t=\sqrt{1-r^2}.
\]
Then \(0\le a,b\le1\), and the **complete constrained numerical range** is the closed annulus (allowing a disk, circle, or point)
\[
\boxed{W_q(A)=\{z\in\mathbb C:R_-(r)\le|z|\le R_+(r)\}},
\]
where both sharp radii are explicit:
\[
\boxed{R_-(r)=\max\{0,bt-ar\}},
\qquad
\boxed{R_+(r)=\begin{cases}
1,&0\le r\le a,\\
ar+bt,&a<r\le1.
\end{cases}}
\]
In particular, the central hole is present **exactly** when \(r<b\), while the outer radius has an exact unit-norm plateau **exactly** when \(r\le a\). Both thresholds are sharp, including the boundary cases. The profile recovers the antiunitary's unitary-conjugacy parameter: the hole radius at \(q=0\) is \(b\), hence \(\operatorname{tr}(A^2)=2-4b^2\).

The opposite symmetry endpoints are: if \(A^2=I\) (conjugation), then \(W_q(A)\) is the closed unit disk for every \(|q|\le1\); if \(A^2=-I\) (the two-dimensional Kramers case), then \(W_q(A)\) is the circle of radius \(\sqrt{1-|q|^2}\). For example, for the rotation-conjugation antiunitary
\[
A\binom{z_1}{z_2}=
\begin{pmatrix}4/5&3/5\\-3/5&4/5\end{pmatrix}
\binom{\overline z_1}{\overline z_2},
\]
the range at \(|q|=1/2\) has outer radius \(1\) and inner radius \((3\sqrt3-4)/10>0\); its hole disappears at \(|q|=3/5\), whereas the outer plateau ends at \(|q|=4/5\).

## Assumptions and scope

This theorem concerns **surjective norm-preserving antilinear** maps on complex \(\mathbb C^2\), not arbitrary antilinear contractions, arbitrary real-linear maps, or complex-linear operators. By antiunitary we mean \(A(\lambda x)=\overline\lambda Ax\) and \(\langle Ax,Ay\rangle=\overline{\langle x,y\rangle}\). The parameter \(q\) is any complex number of modulus at most one; \(r\) denotes its modulus. Inner products are linear in the first variable. Zero-dimensional and one-dimensional spaces, and higher-dimensional antiunitaries, are not included in the classification. Formulae are exact for every admissible parameter and include all endpoints.

## Proof

**1. The invariant and the range of the antilinear diagonal pairing.** Let \(Kx=\overline x\). Write \(A=UK\) with \(U\in U(2)\). Conjugation of \(A\) by a scalar unitary multiplies \(U\) by any prescribed scalar of modulus one, without changing \(W_q(A)\); hence assume \(\det U=1\). Every such \(U\) has the form
\[
U=\begin{pmatrix}u&v\\-\overline v&\overline u\end{pmatrix},
\qquad |u|^2+|v|^2=1.
\]
Writing \(c=\operatorname{Re}v\) and \(h=\operatorname{Im}v\) gives
\[
U=S+cJ,\qquad
S=\begin{pmatrix}u&ih\\ih&\overline u\end{pmatrix},\quad
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
Here \(S=S^{\mathsf T}\), \(SS^*=(1-c^2)I\), and direct multiplication gives
\[
\operatorname{tr}(A^2)=\operatorname{tr}(U\overline U)=2-4c^2.
\]
Thus \(b=|c|\) and \(a=\sqrt{1-c^2}\). The skew matrix \(J\) has zero quadratic form, so for every unit \(x\),
\[
\alpha(x):=\langle Ax,x\rangle
=\overline x^{\mathsf T}S\overline x.
\]
If \(a>0\), the symmetric unitary \(S/a\) admits a Takagi factorization \(S=aVV^{\mathsf T}\) with \(V\) unitary. Consequently the set of possible values of \(|\alpha(x)|\) is exactly \([0,a]\): in the Takagi basis choose unit vectors of the form \((\cos\gamma,i\sin\gamma)\), for \(0\le\gamma\le\pi/4\), to obtain \(a\cos(2\gamma)\). Conversely Cauchy--Schwarz gives \(|\alpha(x)|\le a\). If \(a=0\), \(S=0\) and the attainable set is \(\{0\}\). The endpoints and every intermediate value are therefore attained in all cases.

**2. Exact constrained modulus reduction.** Fix a unit \(x\). Choose a unit \(v_x\perp x\). Because \(A\) is antiunitary,
\[
\big|\langle Ax,x\rangle\big|^2+
\big|\langle Ax,v_x\rangle\big|^2=1.
\]
Every admissible \(y\) with \(\langle x,y\rangle=q\) has the form \(y=\overline q\,x+t e^{i\vartheta}v_x\) for some real \(\vartheta\) (if \(t=0\), its second summand vanishes). Hence, with \(s=|\alpha(x)|\in[0,a]\),
\[
\langle Ax,y\rangle=q\alpha(x)+t e^{-i\vartheta}\langle Ax,v_x\rangle,
\]
and its achievable moduli for that fixed \(x\) fill precisely
\[
\Big[\big|rs-t\sqrt{1-s^2}\big|,\ 
rs+t\sqrt{1-s^2}\Big].
\]
The upper envelope \(f(s)=rs+t\sqrt{1-s^2}\) on \([0,a]\) has its global maximum at \(s=r\) if \(r\le a\), with value \(1\), and otherwise at \(s=a\), with value \(ar+bt\). For the lower envelope, \(g(s)=rs-t\sqrt{1-s^2}\) is nondecreasing and vanishes at \(s=t\). Thus the smallest modulus is zero when \(t\le a\), and is \(bt-ar>0\) otherwise. Since \(t\le a\) is equivalent to \(r\ge b\), this proves the stated formulas for the two extreme radii.

**3. No gaps, and full circular symmetry.** For \(r<1\), admissible pairs \((x,y)\) are a continuous image of the connected unitary group \(U(2)\) (all normalized two-frames with the fixed overlap \(q\)); for \(r=1\), the parameter space is the connected unit sphere. The continuous modulus map therefore has an interval as its image, containing the two attained extrema. Replacing \((x,y)\) by \((e^{i\omega}x,e^{i\omega}y)\) leaves their overlap unchanged and rotates \(\langle Ax,y\rangle\) through the factor \(e^{-2i\omega}\). Every intermediate radius occurs in every angular direction. Compactness of the parameter space gives closedness. This proves the exact annulus assertion.

**4. Symmetry and recovery.** For completeness, the same Takagi construction also proves the precise conjugacy statement: since \(\det S=a^2\), a Takagi factor \(V\) can be chosen with \(\det V=1\) (flipping one column changes its determinant without changing \(VV^{\mathsf T}\)). The identity \(V^*J\overline V=J\) then reduces \(UK\) unitarily to \((aI+cJ)K\). A real diagonal reflection changes the sign of \(c\), so \(b=|c|\) is a complete unitary-conjugacy invariant; when \(a=0\), the same conclusion follows directly from \(U=cJ\). At \(r=0\), the formulas give \(R_-(0)=b\) and \(R_+(0)=1\), so this single range identifies \(b\) and the real trace of \(A^2\). The same two-dimensional unitary-congruence normal form used in step 1, or the standard Wigner antiunitary normal form, shows that \(b\) specifies the conjugacy class. The cases \(b=0\) and \(b=1\) are exactly \(A^2=I\) and \(A^2=-I\), respectively, and their formulas follow by substitution.

## Verification

A standalone reproducible script, `check.py`, constructs exact boundary witnesses from the rotation-conjugation normal form, verifies the overlap constraint, checks the sharp inner and outer radii, samples additional admissible pairs, and verifies invariance under random unitary changes of basis. It reports **12,978 passed deterministic finite checks** over 42 parameter pairs. Run `python3 check.py` with NumPy. These tests are supplementary only: the universal continuum statement is proved analytically by the Takagi reduction, one-variable optimization, and connectedness argument above.

## Relationship to prior work

Majumdar and Müller (2026), Section 6, introduce \(q\)-numerical ranges of real-linear and antilinear operators. Their Proposition 6.2 and Theorem 6.6 cover the disk phenomenon in dimension at least three, their Example 6.3 exhibits a two-dimensional antiunitary with a missing center, and their Remark 6.7 gives a qualitative annulus in dimension two. None of those cited statements gives the pair of radii for *all* two-dimensional antiunitaries. Kołaczek and Müller (2024, 2025) treat ordinary numerical ranges (the case \(|q|=1\)); the more general \(q\)-profile and its independent hole-closing and norm-plateau transitions are a different question. Wigner's antiunitary normal forms, as exposited by Loring (2025), supply established algebraic context, not the optimized \(q\)-range formula. The contribution here is the exact two-parameter constrained numerical annulus and its converse invariant recovery, **not** the pre-existing normal form or qualitative shape theorem.

## Limitations

This is a self-review, not independent verification or a priority guarantee. The argument is self-contained up to the standard finite-dimensional Takagi factorization and connectedness of the unitary group. A potentially relevant broader study by Jia and Liu (2025), focused in its accessible abstract on ordinary antilinear numerical ranges, was not available in complete text; latent equivalent formulas there cannot be excluded without a full-text comparison. Older generalized numerical-range literature could also contain an equivalent implicit computation. No claims are made for higher dimensions, non-isometric antilinear operators, or arbitrary real-linear maps.

## References

1. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823v1 (first public October 12, 2026), Section 6, https://arxiv.org/html/2610.16823v1.
2. T. A. Loring, *Transforming antiunitary symmetries to a normal form*, arXiv:2508.13004v1 (2025), Introduction and Sections 2–3, https://arxiv.org/html/2508.13004v1.
3. D. Kołaczek and V. Müller, *Numerical Ranges of Antilinear Operators*, Integral Equations and Operator Theory 96 (2024), article 17, https://doi.org/10.1007/s00020-024-02768-5.
4. D. Kołaczek and V. Müller, *Real linear operators and numerical ranges*, arXiv:2508.04347v1 (2025), Section 6, https://arxiv.org/html/2508.04347v1.
5. B. Jia and T. Liu, *A characterization of numerical ranges for antilinear operators*, Canadian Mathematical Bulletin 69 (2026), 372–387, first published online April 14, 2025, https://doi.org/10.4153/S000843952500044X (accessible abstract only).
