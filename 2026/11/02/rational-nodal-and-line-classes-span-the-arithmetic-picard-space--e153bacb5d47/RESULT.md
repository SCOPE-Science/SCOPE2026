# Rational nodal and line classes span the arithmetic Picard space of a characteristic-three Hessian K3

## Finding

Let \(e_i\) denote the degree-\(i\) elementary symmetric polynomial in four homogeneous coordinates, and let
\[
 H/\mathbb F_3=V(e_1e_3-e_4)\subset\mathbb P^3_{\mathbb F_3}.
\]
Let \(Y\to H\) be its minimal resolution. Write \(E_1,\ldots,E_{15}\) for the exceptional curves and \(L_1,\ldots,L_{20}\) for the proper transforms of **all twenty** projective lines on \(H\) that are defined over \(\mathbb F_3\).

**Theorem.** The \(35\) classes \([E_i]\) and \([L_j]\) span exactly the \(21\)-dimensional arithmetic Néron–Severi space:
\[
\operatorname{span}_{\mathbb Q}\{[E_i],[L_j]\}
=\big(\operatorname{NS}(Y_{\overline{\mathbb F}_3})\otimes\mathbb Q\big)^{\operatorname{Frob}_3=1},
\qquad \dim_{\mathbb Q}=21.
\]
Their \(35\times35\) integral intersection matrix has rank \(21\), with a nonzero \(21\times21\) principal minor of determinant \(1536\). Each line passes through exactly three nodes and each node lies on four of the twenty lines; ten unordered pairs of these lines meet in smooth points of \(H\). Thus the explicit nodal and line configuration generates every arithmetic divisor class **rationally**; integral saturation is not asserted.

## Assumptions and scope

All schemes and divisor classes are over \(\mathbb F_3\) or its indicated algebraic closure. The quartic is the coefficientwise reduction of the displayed integral polynomial, not an arbitrary equation projectively equivalent in characteristic zero. The \(20\) lines are defined over \(\mathbb F_3\); the assertion does not require an enumeration of lines defined only over larger fields. Frobenius invariants refer to geometric Néron–Severi classes after tensoring with \(\mathbb Q\), not a claim about integral bases.

The singular locus is exactly fifteen rational ordinary double points, in coordinate-permutation orbits with representatives
\[
 [1:0:0:0],\quad[1:-1:0:0],\quad[1:1:1:-1],\quad[1:1:1:1],
\]
of respective sizes \(4,6,4,1\). The minimal resolution is a K3 surface.

## Proof

**1. Nodes and the K3 resolution.** For the Cayley cubic \(F=e_3\), an exact determinant identity over the integers is
\[
\det\big(\operatorname{Hess}(F)\big)=-4(e_1e_3-4e_4).
\]
Reducing modulo three gives the displayed quartic. On each of the four standard affine charts, a lexicographic Gröbner basis of the dehomogenized quartic and its three partial derivatives has quotient length exactly nine. Its zero set has exactly nine distinct \(\mathbb F_3\)-points, so those exhaust the geometric singularities on that chart. Normalizing projective coordinates and taking their union gives fifteen points and the four stated permutation orbits. The determinant of the local three-variable Hessian is nonzero at each of the fifteen points; every singularity is an ordinary double point. The finite singular locus forces geometric irreducibility of the quartic (two surface components in projective three-space would intersect in a curve). Thus the ordinary-double-point resolution is a K3 surface.

**2. Enumeration of rational lines.** Every \(\mathbb F_3\)-rational line in \(\mathbb P^3\) has a unique reduced-row-echelon pair of spanning vectors, with one of six possible pivot pairs. There are exactly \(130\) such two-planes in \(\mathbb F_3^4\). Substitute \(ur+vs\) into \(e_1e_3-e_4\) and set all five coefficients of the binary quartic in \(u,v\) to zero. An exhaustive exact enumeration of the six row-echelon charts gives precisely \(20\) lines, with chart counts \(9,5,2,2,1,1\). Since the restriction polynomial itself is identically zero, not merely zero at field points, every listed line is contained scheme-theoretically in \(H\).

**3. Incidences and intersection form.** Over \(\mathbb F_3\), point-on-line and line-meeting relations reduce to ranks of explicit matrices of homogeneous coordinates. The twenty lines have three nodal points apiece; each of the fifteen nodes belongs to four of them. Among line pairs, exactly ten meet outside the singular locus. On the K3 resolution, each \(E_i\) and \(L_j\) is a smooth rational curve of self-intersection \(-2\). The exceptional curves are pairwise disjoint, \(E_i\cdot L_j=1\) exactly for nodal incidence, and \(L_j\cdot L_k=1\) exactly when the corresponding lines meet at a smooth point of \(H\). Distinct lines through an ordinary double point have distinct tangent directions and disjoint strict transforms. Consequently the coordinate incidence data determine the complete \(35\times35\) intersection matrix \(M\). Exact integer linear algebra yields \(\operatorname{rank} M=21\). More concretely, indexing the exceptional curves first in lexicographic order of normalized node coordinates and then the twenty reduced-row-echelon lines in lexicographic pivot/parameter order, the principal submatrix at zero-based indices
\[
 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,19,20,21,24
\]
has determinant \(1536\), a nonzero certificate for the lower bound \(21\).

**4. Arithmetic Picard upper bound.** Independent exact enumeration of normalized projective points gives
\[
\#H(\mathbb F_3)=25,\qquad \#H(\mathbb F_9)=145.
\]
Resolving fifteen rational nodes replaces a point with a projective line over each extension, hence
\[
\#Y(\mathbb F_3)=70,\qquad \#Y(\mathbb F_9)=280.
\]
The latter is the K3 Weil upper bound \(1+9^2+22\cdot9=280\). The triangle-equality case of purity forces all \(22\) squared degree-two Frobenius eigenvalues to equal \(9\); the first count then gives eigenvalue \(+3\) with multiplicity \(21\) and \(-3\) with multiplicity one. Thus the cohomological space of Frobenius-normalized eigenvalue \(+1\) has dimension \(21\).

**5. Generation.** Every exceptional curve and every listed strict transform is defined over \(\mathbb F_3\), so its divisor class maps into that \(21\)-dimensional eigenvalue space under the étale first-Chern-class map. The nonzero intersection minor proves the classes have at least \(21\) independent algebraic classes. Therefore they span the entire Frobenius-fixed geometric Néron–Severi space over \(\mathbb Q\). The K3 Tate theorem in odd characteristic additionally identifies a one-dimensional geometric Picard complement on which Frobenius acts by \(-1\); that complement is not generated by the stated rational curves.

## Verification

Run `python verify.py` with Python 3 and SymPy. The supplied self-contained script checks the integer Hessian identity, all four characteristic-three Gröbner bases, the fifteen geometric nodal points, all \(130\) rational Grassmannian lines, quartic coefficient restrictions, the full nodal/line incidence, the \(35\)-curve intersection matrix and the displayed minor. It independently counts the quartic over both \(\mathbb F_3\) and \(\mathbb F_9=\mathbb F_3[u]/(u^2+1)\); the Frobenius conclusion uses the K3 Weil theorem rather than numerical extrapolation. `VERIFY_OUTPUT.txt` records an execution from the package source.

## Relationship to prior work

Rosenberg established families of Hessian quartics related to Kummer surfaces. Dardanelli and van Geemen studied Hessian K3 surfaces of cubic surfaces and their characteristic-zero transcendental lattices. Dolgachev's configuration study records the \((15_4,20_3)\) nodal/Steiner-line configuration for general complex 15-nodal quartics. Dolgachev's later Picard-group study treats moduli-general complex 15-nodal quartics, with expected Picard rank \(16\), not this characteristic-three arithmetic Picard rank \(21\). The singularity basket and zeta function of this particular characteristic-three quartic are not proposed as new; the contribution here is the **explicit rational generation of the full arithmetic Picard space by these thirty-five curves**, established through their exact intersection pairing and the arithmetic upper bound. The same rational model can also be viewed as the characteristic-three elementary-symmetric Clebsch Hessian.

## Limitations

The \(35\) classes are proved to generate only **after tensoring with \(\mathbb Q\)**; no integral Néron–Severi basis, saturation index, or Artin invariant is determined. Exhausting \(\mathbb F_3\)-rational lines does not classify lines over the algebraic closure. The Frobenius-invariant rank statement is unconditional, whereas the description of the remaining geometric divisor direction invokes the established K3 Tate theorem. Historical novelty is subject to the possibility of unindexed or otherwise inaccessible explicit positive-characteristic Picard-lattice calculations.

## References

1. J. E. Rosenberg, *Hessian quartic surfaces that are Kummer surfaces*, arXiv:math/9903037 (first posted 1999-03-07).
2. I. Dolgachev, *Abstract configurations in algebraic geometry*, arXiv:math/0304258 (first posted 2003-04-18), especially §9.6.
3. E. Dardanelli and B. van Geemen, *Hessians and the moduli space of cubic surfaces*, arXiv:math/0409322 (first posted 2004-09-18), especially §3.
4. I. Dolgachev, *15-nodal quartic surfaces. I: Quintic del Pezzo surfaces and congruences of lines in projective 3-space*, arXiv:1906.12295 (first posted 2019-06-28), especially §8.
