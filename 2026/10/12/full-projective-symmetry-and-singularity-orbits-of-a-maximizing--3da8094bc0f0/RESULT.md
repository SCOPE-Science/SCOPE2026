# Full projective symmetry and singularity orbits of a maximizing nonic

## Finding
Over \(\mathbb C\), let
\[
D=V\!\left(XYZ\left((X^2+Y^2+Z^2)^3-27X^2Y^2Z^2\right)\right)\subset\mathbb P^2.
\]
The complete projective stabilizer of \(D\) is the signed-permutation group
\[
\operatorname{Aut}_{\mathbb P^2}(D)=(\mu_2^3/\mu_2)\rtimes S_3\cong S_4,
\qquad |\operatorname{Aut}_{\mathbb P^2}(D)|=24.
\]
Its three singularity orbits have sizes \(6\), \(4\), and \(3\), with types respectively \(E_7\), \(A_1\), \(A_1\); the point stabilizers have orders \(4\), \(6\), and \(8\).

## Assumptions and scope
The base field is \(\mathbb C\) (characteristic zero). Projective automorphisms are elements of \(\operatorname{PGL}_3(\mathbb C)\) preserving the reduced divisor \(D\). Let \(Q=(X^2+Y^2+Z^2)^3-27X^2Y^2Z^2\). The originating construction calls this degree-nine divisor maximizing, with three distinct line components and a geometrically irreducible sextic component \(V(Q)\). The latter irreducibility also follows independently from the parametrization below. No conclusion is asserted about abstract automorphisms of the normalization or characteristics two and three.

## Proof
**Irreducibility of the sextic.** The map \([u:v:w]\mapsto[u^3:v^3:w^3]\) sends the irreducible smooth conic \(u^2+v^2+w^2=0\) into \(V(Q)\), since for \(A=u^2,B=v^2,C=w^2\) with \(A+B+C=0\), one has \(A^3+B^3+C^3=3ABC\). The map has generic degree one: two generic preimages with the same three cubes differ, after a common scaling, by individual cube-root multipliers. Substitution into the conic equation gives \((\omega^{2a}-\omega^{2c})u^2+(\omega^{2b}-\omega^{2c})v^2=0\) at the generic conic point, forcing all three multipliers equal. A general line pulls back to a divisor of degree \(6\) on the conic, so the irreducible image has degree \(6\). Hence \(Q\), which has degree six and vanishes on that image, is irreducible over \(\mathbb C\). Moreover, none of \(X,Y,Z\) divides \(Q\).

**Exhaustiveness of projective symmetries.** Every automorphism of the reduced divisor permutes its irreducible components, preserving their degrees. Therefore it permutes the three coordinate lines, and hence is represented by a monomial matrix: a coordinate permutation followed by \(\mathrm{diag}(a,b,c)\), with \(abc\ne0\). The sextic polynomial \(Q\) is symmetric, so remove the permutation. Then \(Q(aX,bY,cZ)=\lambda Q(X,Y,Z)\) for some \(\lambda\ne0\). Comparing the coefficients of \(X^6,Y^6,Z^6\) gives \(a^6=b^6=c^6=\lambda\). Comparing \(X^4Y^2\), \(X^4Z^2\) gives \(a^4b^2=a^4c^2=\lambda=a^6\), thus \(a^2=b^2=c^2\). After dividing by a common projective scalar, \((a,b,c)\in\{\pm1\}^3\) modulo the common sign. Conversely all signed permutations preserve \(XYZQ=0\) as a reduced divisor. There are \(4\cdot 6=24\) transformations. Their action on the four projective points \([1:\pm1:\pm1]\) is faithful (four points in general position determine a projectivity) and transitive, identifying the group with \(S_4\).

**Singularity orbits.** The source's exhaustive local classification gives six \(E_7\) points \([0:1:\pm i]\), \([1:0:\pm i]\), \([1:\pm i:0]\); four nodal points \([1:\pm1:\pm1]\); and the three coordinate vertices, which are also nodes. Signed permutations act transitively on each of these three distinct subsets; they cannot mix them because singularity type or coordinate-vertex incidence is preserved. Hence the orbit sizes are \(6,4,3\). By orbit--stabilizer with group order \(24\), the respective stabilizer orders are \(4,6,8\). The source identifies these as all singular points, and the assertions depend on that already established list, not a new singularity classification.

## Verification
The accompanying `verify.py` recomputes the exact integer coefficients of \(Q\), confirms invariance of the defining polynomial under all \(24\) signed permutations, verifies the four-node orbit is faithful and transitive and checks the three singularity-orbit cardinalities. Algebraic completeness follows from the coefficient comparison in the proof, not from exhaustive testing over an infinite group.

## Relationship to prior work
Dimca, Ilardi, Pokora, and Sticlaru, Example 6.4 in *Construction of free curves by adding lines to a given curve* (first publicly available 2023-01-03), give the degree-nine maximizing equation and the exact \(6E_7+7A_1\) singularity basket. They do not state the full projective stabilizer or its orbit decomposition. The signed-permutation realization of \(S_4\) is classical and occurs, for example, for other symmetric plane-quartic families in Meagher--Top; that representation alone does not classify the stabilizer of the present reducible nonic. An earlier exact arithmetic point-count result for this same divisor proves neither the maximality of this stabilizer nor the complex singularity-orbit description. Historical or unindexed literature may contain an equivalent symmetry computation.

## Limitations
The calculation concerns only projective automorphisms in characteristic zero. The underlying singularity locations/types and maximizing freeness are prior work. No abstract automorphism classification, finite-characteristic symmetry statement, or uniqueness claim among all maximizing nonics is made. The novelty comparison is based on accessible inspected sources and cannot rule out all unindexed computations.

## References
1. A. Dimca, G. Ilardi, P. Pokora, G. Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117, Example 6.4; first arXiv public date 2023-01-03. https://arxiv.org/pdf/2301.01117
2. S. Meagher, J. Top, *Twists of genus three curves over finite fields*, Section 4, a different Ciani-quartic \(S_4\) representation (comparison only). https://home.mathematik.uni-freiburg.de/arithgeom/TwistsGenThreeCurve.pdf
