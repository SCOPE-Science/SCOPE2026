# Global planar Barker–Larman rigidity for arbitrary ellipses
## Finding
Let \(r>0\), and let
\[
B_r(0)\subset\operatorname{int}E_1\cap\operatorname{int}E_2,
\]
where
\[
E_i=c_i+Q_i^{1/2}B_2\subset\mathbb R^2
\]
and each \(Q_i\) is real symmetric positive definite. For \(u\in S^1\), define the support line
\[
H_u=\{x\in\mathbb R^2:u\cdot x=r\}
\]
of the inner disk and the tangent-chord length
\[
L_i(u)=\operatorname{length}(E_i\cap H_u).
\]

If
\[
L_1(u)=L_2(u)
\qquad\text{for every }u\in S^1,
\]
then
\[
c_1=c_2,\qquad Q_1=Q_2,
\]
and therefore
\[
E_1=E_2.
\]

Thus the one-inner-disk Barker–Larman tangent-chord data are globally injective on the complete class of planar ellipses, without a common-center, common-axis, or small-perturbation hypothesis.

## Assumptions and scope
Write
\[
E=c+Q^{1/2}B_2,
\]
with \(Q\) symmetric positive definite. Put
\[
D=\det Q,
\qquad
q(u)=u^{\mathsf T}Qu.
\]
The strict containment
\[
B_r(0)\subset\operatorname{int}E
\]
is equivalent to the positivity, for every \(u\in S^1\), of the radicand appearing below:
\[
q(u)-(r-u\cdot c)^2>0.
\]

The result concerns equality of all chord lengths cut from the outer ellipse by the support lines of one fixed inner Euclidean disk. The inner disk is the same for the two ellipses. No assertion is made for arbitrary outer convex bodies.

## Proof
Fix \(u\in S^1\). Under the affine parametrization
\[
x=c+Q^{1/2}z,
\qquad
\lVert z\rVert\le1,
\]
the line \(H_u\) becomes
\[
(Q^{1/2}u)\cdot z=r-u\cdot c.
\]
Let
\[
a=Q^{1/2}u,
\qquad
s=r-u\cdot c.
\]
The unit disk is cut by the line
\[
a\cdot z=s.
\]
Its chord has half-length
\[
\sqrt{1-\frac{s^2}{\lVert a\rVert^2}}.
\]
If \(v\) is a unit vector perpendicular to \(a\), the affine map stretches that chord direction by
\[
\lVert Q^{1/2}v\rVert.
\]
In two dimensions,
\[
\lVert Q^{1/2}v\rVert^2
=
\frac{\det Q}{u^{\mathsf T}Qu}
=
\frac{D}{q(u)}.
\]
Since
\[
\lVert a\rVert^2=q(u),
\]
we obtain the exact identity
\[
\boxed{
\frac{L_E(u)^2}{4}
=
D\,\frac{q(u)-(r-u\cdot c)^2}{q(u)^2}
}.
\tag{1}
\]

Because \(q(-u)=q(u)\), subtracting (1) at \(u\) and \(-u\) gives
\[
\boxed{
\frac{L_E(u)^2-L_E(-u)^2}{16r}
=
D\,\frac{c\cdot u}{q(u)^2}
}.
\tag{2}
\]

Assume now that two ellipses have identical chord functions.

First suppose that both centers are nonzero. From (2),
\[
D_1\frac{c_1\cdot u}{q_1(u)^2}
=
D_2\frac{c_2\cdot u}{q_2(u)^2}
\qquad(u\in S^1).
\]
After clearing denominators,
\[
D_1(c_1\cdot u)q_2(u)^2
=
D_2(c_2\cdot u)q_1(u)^2.
\tag{3}
\]
Both sides of (3) are homogeneous polynomials of degree \(5\). Equality on \(S^1\) therefore implies the polynomial identity
\[
D_1(c_1\cdot x)q_2(x)^2
=
D_2(c_2\cdot x)q_1(x)^2
\qquad(x\in\mathbb R^2).
\tag{4}
\]

A positive-definite real binary quadratic form has no real linear factor, hence is irreducible in
\[
\mathbb R[x_1,x_2].
\]
In (4), \(q_1\) cannot divide the nonzero linear form \(c_1\cdot x\). Unique factorization therefore forces \(q_1\) and \(q_2\) to be associates:
\[
q_2=kq_1
\]
for some \(k>0\). Consequently,
\[
D_2=k^2D_1.
\]
Substitution into (4) gives
\[
c_2\cdot x=c_1\cdot x
\qquad\text{for all }x,
\]
so
\[
c_2=c_1=:c.
\]
Returning to the full identity (1), with
\[
s(u)=r-u\cdot c,
\]
we have
\[
D_1\frac{q_1-s^2}{q_1^2}
=
k^2D_1\frac{kq_1-s^2}{k^2q_1^2}
=
D_1\frac{kq_1-s^2}{q_1^2}.
\]
Thus
\[
(k-1)q_1(u)=0
\qquad(u\in S^1),
\]
and positive definiteness gives
\[
k=1.
\]
Hence \(Q_1=Q_2\).

It remains to handle a zero center. If \(c_1=0\), equation (2) and equality of the data give
\[
D_2\frac{c_2\cdot u}{q_2(u)^2}=0
\qquad(u\in S^1),
\]
so \(c_2=0\). Thus either both centers are nonzero or both are zero.

Assume now
\[
c_1=c_2=0.
\]
On \(S^1\), equation (1) becomes
\[
D_i\frac{q_i(u)-r^2}{q_i(u)^2}.
\]
Homogenizing with
\[
s_0(x)=x_1^2+x_2^2
\]
and clearing denominators gives
\[
D_1\bigl(q_1-r^2s_0\bigr)q_2^2
=
D_2\bigl(q_2-r^2s_0\bigr)q_1^2.
\tag{5}
\]

Suppose first that neither \(q_i\) is a scalar multiple of \(s_0\). If \(q_1\) and \(q_2\) were not associates, then irreducibility and (5) would force \(q_1\) to divide
\[
q_1-r^2s_0,
\]
hence to divide \(s_0\), contradicting the assumption that \(q_1\) is not a scalar multiple of \(s_0\). Therefore
\[
q_2=kq_1.
\]
As above,
\[
D_2=k^2D_1,
\]
and substitution into the unhomogenized chord identity forces
\[
k=1.
\]

Finally, if \(q_1=a\,s_0\), the first ellipse is a centered circle and its squared half-chord is the constant
\[
a-r^2.
\]
If \(q_2\) were not a scalar multiple of \(s_0\), then \(q_2(u)\) would range over a nondegenerate interval, while
\[
t\longmapsto D_2\frac{t-r^2}{t^2}
\]
has derivative
\[
D_2\frac{2r^2-t}{t^3}
\]
and therefore cannot be constant on an interval. Thus \(q_2=b\,s_0\) as well. Equality of the constant chord data gives
\[
a-r^2=b-r^2,
\]
so \(a=b\).

All cases give
\[
c_1=c_2,\qquad Q_1=Q_2,
\]
which proves the theorem.

## Verification
The proof is analytic. The bundled `verify.py` independently checks the affine chord formula against direct line--ellipse intersection for deterministic nonconcentric positive-definite examples. It also checks the antipodal odd-part identity and verifies on exact integer-grid samples that proportional shape matrices and equal centers are the only way the displayed polynomial factor relation can persist in the tested families.

The finite checks do not prove the quantified theorem. The continuum argument is the exact affine slice formula followed by real-polynomial unique factorization and the separate centered-circle branch above.

## Relationship to prior work
Yaskin and Zhang formulate the Barker--Larman problem for one inner Euclidean ball and state that it is open in every dimension \(n\ge2\). Their planar positive result assumes data from two disks, not one.

Makai and Martini subsequently describe the original hyperplane problem as unsolved and prove a local determination theorem for sufficiently small smooth perturbations. In their discussion of the plane they emphasize the difficulty of the one-disk problem and list two relevant global special cases: Santaló's characterization of a concentric circle by constant tangent-chord length, and uniqueness among polygons under suitable hypotheses. Their result does not give global uniqueness for arbitrary ellipses with free centers.

More recent polygonal reconstruction theorems still use polygonal structure. The result here instead treats the complete smooth five-parameter family of planar ellipses and allows arbitrary displacement of the ellipse center relative to the prescribed inner disk.

## Limitations
The theorem is restricted to ellipses. It does not settle the Barker--Larman problem for arbitrary smooth, strictly convex, or analytic planar bodies.

The proof uses the algebraic rigidity of positive-definite quadratic forms; it does not provide a stability modulus under noisy chord measurements or a minimal finite set of tangent directions.

The original Barker--Larman article was not available in full during bounded lawful-access checks. Later full-text sources summarize its pertinent planar partial results without identifying an arbitrary-ellipse injectivity theorem, but an unindexed or differently phrased conic-specific argument in older literature remains a residual historical risk.

## References
1. V. Yaskin and N. Zhang, *Non-central sections of convex bodies*, arXiv:1509.08174v1, 28 September 2015.
2. E. Makai, Jr. and H. Martini, *Unique local determination of convex bodies*, arXiv:1602.00959v1, 2 February 2016.
3. J. A. Barker and D. G. Larman, *Determination of convex bodies by certain sets of sectional volumes*, Discrete Mathematics 241 (2001), 79--96, DOI:10.1016/S0012-365X(01)00111-X.
