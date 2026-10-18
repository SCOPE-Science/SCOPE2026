# A four-branch toric double-cover germ at a collision in Hikami’s determinantal quintic

## Finding

For the five-punctured-sphere determinantal quintic of Hikami with boundary parameters \(\mathbf b=(-2,-2,0,0,0)\), set \(P=(-2,0,0,0,0)\) in the five affine coordinates \( (p_{01},p_{12},p_{23},p_{34},p_{40})\). At this collision of two accidental rank-four singular strata, the **entire completed hypersurface germ** has a simple four-branch toric normal form:

\[
\widehat{\mathcal O}_{\mathcal Q,P}\cong
\mathbb C[[W,z_1,z_2,z_3,z_4]]/(W^2-z_1z_2z_3z_4).
\]

Its reduced singular locus has exactly six irreducible analytic two-dimensional branches at \(P\), defined by \(W=z_i=z_j=0\) for \(1\le i<j\le4\). The hypersurface germ is normal, Gorenstein, and has multiplicity two. This differs from merely knowing that the kernel-incidence fiber jumps at the point.

## Assumptions and scope

Work over \(\mathbb C\) with the determinantal affine hypersurface \(\mathcal Q=\{\det M=0\}\subset\mathbb A^5\) defined by Hikami, *Character variety of the five-punctured sphere and the determinantal quintic hypersurface*, arXiv:2610.12092v1, equation (2.14). Specialize its boundary trace parameters to \(\mathbf b=(-2,-2,0,0,0)\). The matrix is

\[
M=\begin{pmatrix}
2&2&-p_{01}&-p_{34}&0\\
2&2&2&-p_{12}&-p_{40}\\
-p_{01}&2&2&0&-p_{23}\\
-p_{34}&-p_{12}&0&2&0\\
0&-p_{40}&-p_{23}&0&2
\end{pmatrix}.
\]

The point \(P=(-2,0,0,0,0)\) is the rank-three point at which the closures of the two displayed accidental rank-four strata in Hikami §2.2.3 meet. All conclusions are local at this **one** point, with no claim about other parameter choices.

## Proof

Write \(p_{01}=-2+a\), \(p_{12}=b\), \(p_{23}=c\), \(p_{34}=d\), \(p_{40}=e\). Direct determinant expansion, as verified by the included exact symbolic checker, has the form

\[
\det M=Aa^2+Ba+C,
\]

with \(A=2(b^2+e^2-4)\),

\[
B=-2(4b^2+bcde-4bd-4ce+4e^2),
\qquad C=2(bc-cd+de)^2.
\]

In particular, \(A(0)=-8\ne0\), so completion of the square is a valid analytic coordinate change in the \(a\)-direction. Put \(W_0=2Aa+B\). On the hypersurface, the identity \(W_0^2=B^2-4AC\) holds. A direct polynomial factorization gives

\[
B^2-4AC=-4FG,
\]

where

\[
F=4(b-d)^2+(4-d^2)e^2,
\qquad G=b^2(c^2-4)-4(c-e)^2.
\]

Near the origin choose holomorphic square roots \(\alpha(d)^2=4-d^2\) and \(\beta(c)^2=c^2-4\), with \(\alpha(0)=2\) and \(\beta(0)=2i\). These exist since their arguments are units. Define

\[
\begin{aligned}
z_1&=2(b-d)+i\alpha(d)e,&z_2&=2(b-d)-i\alpha(d)e,\\
z_3&=b\beta(c)-2(c-e),&z_4&=b\beta(c)+2(c-e).
\end{aligned}
\]

Then \(F=z_1z_2\), \(G=z_3z_4\), hence with \(W=W_0/(2i)\) the equation becomes exactly \(W^2=z_1z_2z_3z_4\). The Jacobian of \((b,c,d,e)\mapsto(z_1,z_2,z_3,z_4)\) at the origin has determinant \(-64\) for the specified square-root choices. Moreover, \(\partial W/\partial a=A/i\) is nonzero at the origin. Thus the complete change \((a,b,c,d,e)\mapsto(W,z_1,z_2,z_3,z_4)\) is locally biholomorphic. Taking completed local rings proves the asserted isomorphism.

For \(W^2=z_1z_2z_3z_4\), the Jacobian equations are \(W=0\) and \(\prod_{j\ne i}z_j=0\) for each \(i\). Set-theoretically these hold precisely when at least two of the four \(z_i\) vanish. Hence the reduced singular locus has the six asserted irreducible two-dimensional branches. Since the singular locus has codimension two in the four-dimensional hypersurface and the hypersurface is Cohen–Macaulay, Serre's criterion proves normality. Being a hypersurface, it is Gorenstein. The initial homogeneous equation is \(W^2=0\), so its Hilbert–Samuel multiplicity is two. It is toric as the affine hypersurface parametrized by the binomial \(W^2-z_1z_2z_3z_4\), which is a normal prime binomial variety.

## Verification

The accompanying standalone \(`verify.py`\) reconstructs the specialized symmetric matrix in exact polynomial arithmetic, expands the determinant in the shifted variable, checks each coefficient \(A,B,C\), factors \(B^2-4AC\) into \(-4FG\), checks the linearized branch coordinates and their nonzero determinant, and confirms the rank at \(P\). It uses SymPy and exits with \(`VERIFY_OK`\) on success. The holomorphic square-root choices and analytic inverse function theorem are theoretical arguments, not extrapolations from numerical experiments.

## Relationship to prior work

Hikami, arXiv:2610.12092v1, §2.2.3, specifies the two accidental rank-four strata and their intersecting rank-three point and describes the jump of the kernel-incidence fiber. It does not state this completed local toric normal form, four-branch discriminant, or the six-component local reduced singular locus. The same article's generic rank-three \(A_1\) discussion (§2.2) concerns a distinct generic situation and does not give the collision germ. Standard completion of the square and normal-crossing double-cover theory justify the reduction once the particular discriminant factorization is supplied. In literature and mathematical-record searches performed for the precise four-factor local isomorphism, no equivalent claim was identified; this does not establish exhaustive novelty.

## Limitations

This is a local analytic classification at a single collision point of a fixed five-parameter family. It does not classify other rank-three points, the global singular locus, its resolutions, or the full character variety prior to the determinantal map. Its consequence about six local branches is analytic and reduced, not an assertion about the global irreducibility of each corresponding stratum. A possible unindexed equivalent statement or a general local theorem explicitly specialized to this point remains a priority risk.

## References

- Kazuhiro Hikami, *Character variety of the five-punctured sphere and the determinantal quintic hypersurface*, arXiv:2610.12092v1 (first public October 8, 2026), especially §§2.2 and 2.2.3, equations (2.14), (2.32)–(2.34). https://arxiv.org/html/2610.12092v1
- Standard holomorphic inverse-function theorem, analytic square-root lemma for units, Serre's normality criterion, and Jacobian criterion for hypersurfaces.
