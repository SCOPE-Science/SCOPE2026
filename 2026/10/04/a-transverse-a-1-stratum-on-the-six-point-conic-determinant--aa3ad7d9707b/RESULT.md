# A transverse \(A_1\) stratum on the six-point conic determinant
## Finding
Let \(X_{2,2,6}\subset(\mathbb P^2)^6\) be the hypersurface of six ordered points lying on a plane conic. Fix one label. On a nonempty Zariski-open subset of the locus where the other five points are distinct and collinear and the distinguished point is off their line, the singular locus of \(X_{2,2,6}\) is smooth of dimension \(9\), and the transverse analytic singularity is \(A_1\). Thus, over \(\mathbb C\), the local analytic germ is a product of a smooth \(9\)-fold with \(V(uv-w^2)\).

An exact witness is
\[
([0:0:1],[1:0:1],[2:0:1],[3:0:1],[4:0:1],[0:1:1]).
\]
At this witness the multi-Veronese matrix has rank \(4\), the Hessian of the defining determinant has rank \(3\), and the Hessian kernel equals the tangent space to the five-collinear stratum. By permutation symmetry, the same generic statement holds on each of the six analogous top-dimensional components.

## Assumptions and scope
Work over \(\mathbb C\). On the affine chart \(z=1\), use the quadratic Veronese row
\[
v(x,y)=(x^2,xy,y^2,x,y,1).
\]
The hypersurface equation is the determinant of the \(6\times6\) matrix with rows \(v(x_i,y_i)\). The statement concerns the generic point of a component on which five specified points are distinct and collinear and the sixth lies off that line. It does not classify intersections of these components, collision strata, or positive-characteristic behavior.

## Proof
The cited determinantal construction identifies \(X_{2,2,6}\) with the six-point conic determinant. The cited singular-locus theorem places the rank-at-most-four locus inside the singular locus, and the cited decomposition of the second degeneracy locus gives, for each choice of exceptional label, a five-collinear component of dimension \(9\).

At the displayed witness, the six Veronese rows have exact rational rank \(4\), so all first derivatives of the determinant vanish. For two distinct point labels \(i\neq j\), a mixed second derivative is the determinant obtained by replacing row \(i\) and row \(j\) by the corresponding first-derivative rows. Exact rational evaluation of these row-replacement determinants gives a \(12\times12\) Hessian of rank \(3\). The principal minor in the three normal directions \((y_1,y_2,y_3)\) has determinant
\[
-576\neq0.
\]

The tangent space to the five-collinear stratum at the witness has nine explicit independent directions: five independent motions of the five points along their common line; the two motions of the sixth point; and two motions of the common line, represented on the five \(y\)-coordinates by \((0,1,2,3,4)\) and \((1,1,1,1,1)\). Direct multiplication shows that all nine vectors lie in the Hessian kernel. Since the Hessian has rank \(3\), its kernel has dimension \(9\), hence it is exactly this tangent space.

The singular locus already contains a local \(9\)-dimensional five-collinear component, while the Jacobian linearization at the witness has tangent space of dimension \(9\). Therefore the singular locus is smooth of dimension \(9\) there. The Hessian is nondegenerate on a complementary three-dimensional normal slice. The holomorphic Morse-Bott lemma then gives a transverse nondegenerate quadratic hypersurface singularity, analytically equivalent to \(uv-w^2=0\). Nonvanishing of the displayed Hessian minor is an open condition, so the conclusion holds on a nonempty Zariski-open subset of the component.

## Verification
The accompanying exact-arithmetic script reconstructs the six Veronese rows at the witness, verifies matrix rank \(4\), verifies all first row-replacement determinants vanish, constructs every mixed second row-replacement determinant, checks Hessian rank \(3\), checks the \((y_1,y_2,y_3)\) principal minor equals \(-576\), constructs the nine tangent vectors, verifies their independence, and verifies that each is killed by the Hessian.

These computations establish the finite algebra needed at the witness. The passage from the witness to a generic open subset uses only openness of rank and nonvanishing conditions; no finite enumeration is used as a substitute for an infinite claim.

## Relationship to prior work
Caminata, Giansiracusa, Moon, and Schaffler give the six-point conic hypersurface as the determinant of the quadratic Veronese evaluation matrix and establish global properties of the point-configuration variety. Caminata, Moon, and Schaffler later describe the relevant second degeneracy locus: for six points, the component with five specified points on a line and one arbitrary point has dimension \(9\), and their general theorem places the second degeneracy locus in the singular locus of the first determinantal variety. Caminata and Schaffler give the Pascal/Grassmann-Cayley viewpoint on the same conic-incidence geometry.

The inspected statements establish the determinant, the rank-drop singularity mechanism, and the five-collinear component, but not the transverse analytic type along that component. The new content is the exact Hessian-kernel calculation and the resulting generic Morse-Bott \(A_1\) normal form.

## Limitations
The conclusion is generic along the top-dimensional five-collinear components and is proved over \(\mathbb C\). No claim is made about the scheme structure of the entire singular locus, component intersections, coincident-point strata, deeper rank drops, or positive characteristic. A classical source using a different Pascal or quotient-model vocabulary could in principle contain an equivalent local statement; targeted searches and the inspected primary sources did not reveal one.

## References
1. A. Caminata, N. Giansiracusa, H.-B. Moon, L. Schaffler, *Equations for point configurations to lie on a rational normal curve*, arXiv:1711.06286.
2. A. Caminata, H.-B. Moon, L. Schaffler, *Determinantal varieties from point configurations on hypersurfaces*, arXiv:2211.13177.
3. A. Caminata, L. Schaffler, *A Pascal's theorem for rational normal curves*, arXiv:1903.00460.
