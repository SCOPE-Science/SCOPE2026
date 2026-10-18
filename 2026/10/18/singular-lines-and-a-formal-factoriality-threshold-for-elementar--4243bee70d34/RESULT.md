# Singular lines and a formal factoriality threshold for elementary-symmetric quartic hypersurfaces

## Finding
For \(n\ge6\), the hypersurface \(X_n=V(e_4(x_1,\ldots,x_n))\subset\mathbb P^{n-1}\) is integral and normal. Its reduced singular support is precisely the \(\binom n2\) coordinate lines, so its degree is \(\binom n2\). Along the generic point of each line the completed transverse hypersurface is a nondegenerate quadratic cone of dimension \(n-3\). Thus its generic transverse completed local ring has class group \(\mathbb Z\) when \(n=6\), but is factorial when \(n\ge7\). Moreover every (uncompleted) local ring of \(X_n\) is factorial for \(n\ge7\).

## Assumptions and scope
Work over an algebraically closed field \(k\) of characteristic zero. Fix an integer \(n\ge6\). Write \(e_j\) for the \(j\)-th elementary symmetric polynomial in the specified coordinates, and \(e_j(\widehat{x_i})\) when coordinate \(i\) is omitted. The singular support is reduced set-theoretically; no claim about the scheme structure of the Jacobian ideal at line intersections is made. Statements about completed generic local rings are distinguished from statements about Zariski local rings.

## Proof
**1. Singular support.** The partial derivative is \(g_i=e_3(\widehat{x_i})\). The generating identity for elementary symmetric polynomials gives
\[
g_i=e_3-x_i e_2+x_i^2e_1-x_i^3=-H(x_i),\qquad H(T)=T^3-e_1T^2+e_2T-e_3.
\]
Suppose that every \(g_i\) vanishes at a projective point \([x_1:\cdots:x_n]\). Then every coordinate is a root of the monic cubic \(H\). Let \(r_1,\ldots,r_t\) be its distinct nonzero roots, and let \(h_j\) be the multiplicity of \(r_j\) as a root of \(H\), while \(m_j\) is its multiplicity among the coordinates. Newton's identities applied both to \(H\) and to the coordinate multiset show
\[
\sum_{j=1}^t (m_j-h_j)r_j^s=0\quad(s=1,2,3).
\]
For \(t\le3\), the matrix with entries \(r_j^s\), \(1\le s,j\le t\), is a nonzero-diagonal multiple of a Vandermonde matrix and hence invertible. Thus \(m_j=h_j\) for every nonzero root, and the number of nonzero coordinates is at most three. Since \(n\ge6\), at least one coordinate is zero, forcing \(H(0)=0\) and hence at least one zero root in \(H\). Therefore the number of nonzero coordinates is at most two. Conversely, if at most two coordinates are nonzero, every cubic elementary-symmetric derivative vanishes, and the quartic itself vanishes. This proves that the singular set is exactly the coordinate-line arrangement and gives its \(\binom n2\) irreducible reduced components and its degree.

**2. Integral and normal.** A positive-dimensional hypersurface component of a nonreduced divisor would be contained in the gradient vanishing set, contrary to its dimension being at least \(n-2>1\). If the hypersurface were reducible, the intersection of two distinct components in projective space would have dimension at least \(n-3>1\) and would lie in the singular locus, also impossible. Thus \(X_n\) is integral. Being a hypersurface it is Cohen--Macaulay (condition \(S_2\)); its one-dimensional singular locus has codimension \(n-3\ge3\), so it is regular in codimension one. Serre's criterion gives normality.

**3. Generic transverse germ.** Choose a generic point of the line supported on coordinates \(1,2\), with their values \(a,b\ne0\), and denote the remaining \(n-2\) variables by \(z\). The defining equation is exactly
\[
e_4(a,b,z)=ab\,e_2(z)+(a+b)e_3(z)+e_4(z).
\]
The quadratic form \(ab\,e_2(z)\) has Hessian equal to \(ab\) times the zero-diagonal/all-off-diagonal-one matrix of size \(n-2\). Its determinant is \((-1)^{n-3}(n-3)(ab)^{n-2}\ne0\). The formal Morse lemma in characteristic zero thus identifies the completed transverse germ with a nondegenerate quadratic hypersurface, and adjoining the smooth line parameter gives the completed germ at a general closed point.

**4. Formal class groups and Zariski factoriality.** For \(n=6\), the transverse quadratic cone has four variables. Over the residue field of the line generic point (whose constants contain the algebraically closed field \(k\)) the quadric splits, and its completed local ring is isomorphic to \(K[[u,v,s,t]]/(uv-st)\), with divisor class group \(\mathbb Z\). This proves nonfactoriality of that *completed* local ring, not of the original local ring. For \(n\ge7\), the singular locus has codimension \(n-3\ge4\), and every local ring of the normal hypersurface is a local complete intersection and is regular at primes of height at most three. The Samuel--Grothendieck factoriality theorem (SGA 2, Exposé XI, Corollary 3.14) makes each such local ring factorial. It applies also to the higher-dimensional ordinary quadratic completed transverse cones, which are regular in codimension three; hence they are factorial.

## Verification
The standalone Python checker `checker.py` differentiates \(e_4\) symbolically for \(n=6,7\), confirms that every coordinate line lies in the gradient zero locus, verifies the generic transverse Hessian determinant \((-1)^{n-3}(n-3)6^{n-2}\) at \(a=2,b=3\), and tests nonsingularity of selected higher-support points. The executed checker returned `VERIFY_OK`. These finite computations do not establish the infinite statement, which follows from the Newton--Vandermonde and local-ring arguments above.

## Relationship to prior work
Aluffi and Marcolli study banana graph hypersurfaces defined by a degree depending on the number of variables, which includes the quartic \(e_4\) in five variables; that work does not give a fixed-degree fourth elementary-symmetric singular-line classification for every \(n\ge6\). Cafure--Matera--Privitelli analyze singularities of another family of symmetric hypersurfaces arising in Reed--Solomon coding, but their investigated statements do not yield the present exact fixed-quartic line support or formal class-group transition. The Samuel--Grothendieck theorem is a classical input used here, not claimed as novel. Related five-variable singular-scheme calculations do not imply the higher-variable classification or the codimension threshold without the proof above.

## Limitations
The Jacobian singular scheme at coordinate vertices and its embedded components are not determined. The nonfactoriality assertion for \(n=6\) concerns a completed transverse local ring: nonfactoriality of a completion alone does not establish nonfactoriality of its uncompleted algebraic local ring. Characteristic-positive exceptions are not treated. Literature comparisons do not prove absolute priority, and independent validation has not been performed.

## References
- Paolo Aluffi and Matilde Marcolli, *Feynman motives of banana graphs*, arXiv:0807.1690, first posted 2008-07-10.
- Antonio Cafure, Guillermo Matera, and Melina Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed--Solomon codes*, arXiv:1109.2265, first posted 2011-09-10.
- A. Grothendieck, *SGA 2*, Exposé XI, the complete-intersection factoriality theorem and corollary, https://jcreinhold.github.io/sga/ii/11-application-to-the-picard-group.html.
