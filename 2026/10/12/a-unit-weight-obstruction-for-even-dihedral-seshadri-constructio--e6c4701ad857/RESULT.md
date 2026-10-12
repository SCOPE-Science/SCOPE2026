# A unit-weight obstruction for even dihedral Seshadri constructions
## Finding
Fix an integer \(n>4\) and a unit
\[
q\in(\mathbf Z/n\mathbf Z)^*,\qquad 1\le q\le n-1.
\]
Consider the natural weight-\(q\) variant of the dihedral construction in Malara–Merta–Szpond–Zieliński: on
\[
\mathbf P^1\times\mathbf P^1
\]
use
\[
r_q(x,z)=(\zeta x,\zeta^qz),
\qquad
s_q(x,z)=\left(\frac{u}{x},\frac{u^q}{z}\right),
\]
with \(u>1\) and \(\zeta\) a primitive \(n\)-th root of unity. The free orbit of \((1,1)\) lies on
\[
\Gamma_q:\ z=x^q.
\]
After blowing up the \(2n\) orbit points, its strict transform has class
\[
\gamma_q=qH_1+H_2-E
\]
and square
\[
\gamma_q^2=-2(n-q).
\]

Assume, even favorably, that the source's uniform de Jonquières steps remain nondegenerate indefinitely for this unit weight, and that a balanced reflection across \(\gamma_q\) is available. Then the reflected limiting ray has rational ruling slope if and only if
\[
q=n-2.
\]
Consequently, when \(n\) is even, no unit \(q\) in this weight-only template can make the reflected ray proportional to the Seshadri threshold class of a rational bidegree polarization. The obstruction occurs even after granting the two difficult geometric inputs—nondegenerate dynamics and balanced reflection.

This gives a precise limitation on the most direct approach to the even-\(n\) question raised in the source: an even-\(n\) construction must change more than merely the unit weight while retaining the same orbit curve and de Jonquières/reflection template.

## Assumptions and scope
The claim is deliberately restricted to the natural one-parameter weight replacement of the source construction. It keeps:

- the dihedral action with rotation weights \((1,q)\);
- the orbit curve \(z=x^q\);
- the source's uniform de Jonquières transformation on the symmetric marked subspace;
- the source's limiting matrix \(T_n\);
- reflection in the strict transform of the orbit curve.

It does **not** assert that the de Jonquières iteration is nondegenerate for every unit \(q\). Instead, it proves that even if nondegeneracy is achieved, and even if the required balanced normal bundle also exists, the final reflected ray cannot have rational ruling slope for even \(n\).

Nor does the result rule out the broader alternatives explicitly allowed by the source question: a different finite group, a different orbit geometry, a different reflection curve, a different birational dynamics, or a construction not based on a rational bidegree polarization.

## Proof
Let
\[
\Delta=\sqrt{n(n-4)},
\qquad
\alpha=\frac{n-\Delta}{2},
\qquad
\beta=\frac{n+\Delta}{2}.
\]
The source proves that every uniform de Jonquières step, after the factor exchange, acts on the symmetric marked subspace
\[
\operatorname{Span}(H_1,H_2,E)
\]
by the same matrix
\[
T_n=
\begin{pmatrix}
0&1&0\\
1&n&2n\\
0&-1&-1
\end{pmatrix},
\]
independently of the unit weight used in that step. Therefore any indefinitely nondegenerate iteration of this same type has the same dominant isotropic ray
\[
R_n=\alpha H_1+\beta H_2-E.
\]

For the weight-\(q\) action, the orbit of \((1,1)\) is contained in the smooth rational graph
\[
\Gamma_q:\ z=x^q,
\]
which has class \(qH_1+H_2\). Blowing up all \(2n\) orbit points gives
\[
\gamma_q=qH_1+H_2-E,
\qquad
\gamma_q^2=2q-2n=-2(n-q).
\]
Put
\[
a=n-q.
\]
The balanced-reflection formula, if geometrically available, is
\[
s_{\gamma_q}(D)=D+\frac{D\cdot\gamma_q}{a}\gamma_q.
\]
Using
\[
H_1^2=H_2^2=0,
\qquad
H_1\cdot H_2=1,
\qquad
E^2=-2n,
\]
one obtains
\[
R_n\cdot\gamma_q
=
\alpha+q\beta-2n
=
\frac{n(q-3)+(q-1)\Delta}{2}.
\]
After multiplying the reflected class by the harmless positive scalar \(2(n-q)\), its first two coefficients are
\[
A_q=n(n+q^2-4q)+(q^2-n)\Delta
\]
and
\[
B=n(n-3)+(n-1)\Delta.
\]
Thus the ruling slope is
\[
\frac{A_q}{B}.
\]

For every integer \(n>4\), the number \(\Delta\) is irrational. Indeed, if \(\Delta=m\) were integral, then
\[
(n-2-m)(n-2+m)=4.
\]
The two factors have the same parity. The only positive same-parity factorization of \(4\) is \(2\cdot2\), which forces \(m=0\) and \(n=4\), a contradiction.

Because \(B>0\) and \(\Delta\notin\mathbf Q\), the quotient \(A_q/B\) is rational exactly when the rational and \(\Delta\)-coefficient pairs are proportional. The corresponding determinant is
\[
\begin{aligned}
&n(n+q^2-4q)(n-1)
-(q^2-n)n(n-3)\\
&\qquad=2n(q-n)(q-n+2).
\end{aligned}
\]
For
\[
1\le q\le n-1,
\]
this vanishes exactly at
\[
q=n-2.
\]
Hence the reflected ruling slope is rational if and only if \(q=n-2\).

A Seshadri threshold ray coming from a rational bidegree polarization
\[
d_1H_1+d_2H_2
\]
must have rational ruling slope \(d_1/d_2\). Therefore the only weight in this template capable of reproducing the source's final rational-polarization identification is \(q=n-2\). If \(n\) is even, however,
\[
\gcd(n,n-2)=2,
\]
so \(q=n-2\) is not a unit modulo \(n\). This contradicts the unit hypothesis required by the source's de Jonquières iteration. Thus no unit-weight replacement can close the same reflection-to-Seshadri step for even \(n\).

## Verification
The accompanying `verify.py` reconstructs the intersection and reflection calculation symbolically over
\[
\mathbf Q[n,q,\Delta].
\]
It verifies the formulas for the reflected \(H_1\), \(H_2\), and exceptional coefficients and factors the rationality determinant exactly as
\[
2n(q-n)(q-n+2).
\]
It also verifies the identity
\[
(n-2)^2-n(n-4)=4,
\]
which underlies the elementary irrationality proof for \(\Delta\).

A finite arithmetic sweep through \(5\le n\le100\) is included only as a sanity check; the theorem itself is proved by the symbolic factorization and the parity argument, not by enumeration. The saved replay output ends in `VERIFY_OK`.

## Relationship to prior work
Malara–Merta–Szpond–Zieliński prove the odd-\(n\) family using the special weight \(q=n-2\), establish the unit-weight uniform de Jonquières lemma, show that its symmetric pullback matrix is independent of the unit weight, and identify the reflected limiting ray with the Seshadri ray. Their final section explicitly asks whether even \(n\) can be handled by changing the weights or by using a more general finite-group action. The checked text does not contain the obstruction above.

Laface–Ugaglia supply the preceding \(n=5\) dihedral example. Their construction uses the same basic de Jonquières/reflection mechanism in that isolated case; it does not analyze a general unit weight or an even-\(n\) obstruction.

Dionne–Roth develop the broader reflection theory for multipoint Seshadri constants on \(\mathbf P^1\times\mathbf P^1\), including substantial even-point behavior. Their even-point results concern the nef cone and reflection dynamics for very general points, not the source's finite-dihedral unit-weight template. In particular, they do not imply that a different unit weight can or cannot realize the specific reflected Seshadri ray considered here.

Targeted searches for the even-\(n\) question, unit-weight variants, the condition \(q=n-2\), and reflected-ruling-slope formulations found no statement covering this obstruction.

## Limitations
The result is an obstruction to a **weight-only** extension, not a negative answer to the source's full even-\(n\) question. It does not prove that an even-\(n\) irrational limiting nef ray cannot be produced, and it does not exclude a different finite-group action or a different special curve.

The balanced normal bundle for \(\gamma_q\) is not asserted for general \(q\); the proof intentionally grants it as a favorable hypothesis. Thus the obstruction is located later in the mechanism: even after a successful balanced reflection, the resulting ruling slope is irrational for every admissible unit weight when \(n\) is even.

The statement concerns rational bidegree polarizations on \(\mathbf P^1\times\mathbf P^1\). It makes no claim about irrational polarizations or about unrelated surface models.

## References
1. G. Malara, Ł. Merta, J. Szpond, M. Zieliński, *Dihedral reflections and an infinite series of irrational Seshadri constants*, arXiv:2610.01783v1, 2026.
2. A. Laface, L. Ugaglia, *Irrational Seshadri constants from dihedral orbits*, arXiv:2609.26521v2, 2026.
3. C. Dionne, M. Roth, *Seshadri constants on \(\mathbf P^1\times\mathbf P^1\) and applications to the symplectic packing problem*, Forum of Mathematics, Sigma 13 (2025), e191.
