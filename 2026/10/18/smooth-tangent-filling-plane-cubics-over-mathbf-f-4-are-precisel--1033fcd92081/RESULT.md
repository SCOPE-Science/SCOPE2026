# Smooth tangent-filling plane cubics over \(\mathbf F_4\) are precisely Hermitian

## Finding
Let \(k=\mathbf F_4\). The set of geometrically smooth homogeneous ternary cubic equations whose tangent lines at \(k\)-rational points cover \(\mathbf P^2(k)\) consists of precisely \(280\) equations modulo multiplication by \(k^\times\). Every such equation is a nonsingular Hermitian form
\[
 F_A(\mathbf X)=\sum_{i,j=1}^{3}A_{ij}X_i^2X_j,\qquad A_{ji}=A_{ij}^{2},\qquad \det A\ne0,
\]
after multiplying the equation by a nonzero field scalar. The curves are all projectively equivalent under \(\mathrm{PGL}_3(k)\) to
\[
 X^3+Y^3+Z^3=0.
\]
Each has exactly nine \(k\)-points. Its projective stabilizer has order \(216\).

The tangent-filling condition distinguishes the plane embedding from merely attaining the maximal elliptic-curve point count: the geometrically smooth cubic
\[
 X^3+Y^3+YZ^2+Z^3=0
\]
also has nine \(k\)-points, but its rational tangent lines cover only eighteen of the twenty-one rational projective-plane points.

## Assumptions and scope
All curves are plane cubics over \(k=\mathbf F_2[u]/(u^2+u+1)\). "Geometrically smooth" means nonsingular over an algebraic closure, not only at rational points. A rational tangent line is the projective line given by the three partial derivatives at a smooth rational point. "Tangent-filling" means every one of the \(21\) rational points lies on at least one such line. Curves/equations are identified only under nonzero scalar multiplication when they are counted; projective equivalence is considered separately. No classification of singular cubics or of abstract isomorphism classes is asserted.

## Proof
**1. Exhaustive universe.** Order the ten degree-three monomials as
\[
 X^3,\ X^2Y,\ X^2Z,\ XY^2,\ XYZ,\ XZ^2,\ Y^3,\ Y^2Z,\ YZ^2,\ Z^3.
\]
Every nonzero coefficient vector in \(k^{10}\) has a unique projective normalization in which its first nonzero coefficient is \(1\). Therefore there are exactly
\[
 (4^{10}-1)/3=349525
\]
projective cubic equations to check. The attached program generates each one exactly once. The rational projective plane has the explicit list of \(16+4+1=21\) points \([1:y:z]\), \([0:1:z]\), and \([0:0:1]\), with field values ranging over \(k\). All its rational lines are represented by the same list of coefficient triples.

**2. Exact tangent test.** For each normalized coefficient vector, the program computes the cubic value and all three formal partial derivatives at every rational point, using the four-element multiplication table for \(k\). A point is a smooth rational point of the cubic exactly when its value is zero and its gradient is nonzero. The gradient gives its tangent line. The program unions the five rational points on each such tangent and checks whether the result is the entire \(21\)-point plane. This is a finite exhaustive test, not sampling or an extension-degree smoothness test. It produces the following full classification of tangent-filling *equations*, grouped by number of rational zeros and number smooth among those zeros:
\[
 (9,8):5040,\qquad(9,9):280,\qquad(10,10):6048.
\]
There are no other tangent-filling cubic equations among the \(349525\). A geometrically smooth plane cubic has genus one, so the Hasse bound over \(\mathbf F_4\) gives at most \(4+1+2\sqrt4=9\) rational points. Moreover, all rational points of a geometrically smooth curve are smooth. Hence any geometrically smooth tangent-filling cubic is in the \((9,9)\) class of exactly \(280\) equations.

**3. Hermitian identification and geometric smoothness.** The attached independent coefficient predicate tests all three possible nonzero scalings for whether each of those \(280\) candidate forms has Hermitian coefficients. In the monomial order above, a Hermitian form has coefficient vector
\[
 (a,b,c,b^2,0,c^2,d,e,e^2,f),\quad a,d,f\in\mathbf F_2,\quad b,c,e\in\mathbf F_4.
\]
The corresponding \(3\)-by-\(3\) Hermitian matrix has nonzero determinant for every candidate. No candidate fails either condition. Independently enumerating all \(2^3\cdot4^3=512\) Hermitian matrices yields exactly \(280\) of nonzero determinant. Because the derivative of \(X_i^2X_j\) with respect to \(X_j\) is \(X_i^2\) in characteristic two, the gradient of \(F_A\) is \(A^{\mathsf T}\mathbf X^{[2]}\). Invertibility of \(A\) implies this gradient never vanishes at any geometric projective point. Thus all \(280\) are geometrically smooth. Conversely, they were all found tangent-filling by the exhaustive test. The usual Hermitian orthogonality argument also proves existence directly: the orthogonal complement of any external rational point has isotropic points, while an isotropic point lies on its own tangent.

**4. Orbits and stabilizers.** Every nondegenerate Hermitian form on a three-dimensional vector space over \(\mathbf F_4\) is isometric to the diagonal form, so the \(280\) equations constitute one projective orbit. Since \(|\mathrm{GL}_3(\mathbf F_4)|=(64-1)(64-4)(64-16)=181440\), and the unitary stabilizer of one nonsingular Hermitian form has order \(|\mathrm U_3(2)|=648\), this orbit has length \(181440/648=280\). Dividing by the common order-three scalar subgroup gives projective stabilizer order \(648/3=216\), in agreement with \(|\mathrm{PGL}_3(\mathbf F_4)|/280=60480/280=216\).

**5. Nine points alone do not suffice.** The displayed non-Hermitian example has gradient \((X^2,Y^2+Z^2,Z^2)\), which has no nonzero common zero over an algebraic closure. The finite exact tangent computation gives nine rational curve points, all smooth, but its tangent lines cover only eighteen rational plane points. Therefore the classification cannot be replaced by the weaker condition of attaining the elliptic point bound.

## Verification
Run \(\texttt{python3 verify\_f4\_tangent.py}\) with Python 3; there are no third-party dependencies. The program exhaustively evaluates \(349525\) projective cubic equations, explicitly constructs all \(21\) points and lines, checks all rational tangent incidences, and independently enumerates all \(512\) Hermitian matrices. It asserts exactly \(280\) smooth candidate equations, zero non-Hermitian candidates, exactly \(280\) nonsingular Hermitian matrices, and the nine-point non-filling contrast. The expected final line is \(\texttt{PASS}\). Smoothness over an algebraic closure is proved by the matrix/gradient identity, not inferred from enumeration over finite extensions.

## Relationship to prior work
Asgarli and Ghioca [1, Example 3.1] prove that the Hermitian plane curve of degree \(\sqrt q+1\) is tangent-filling over every square field. Their work does not claim the converse classification of all smooth cubics over \(\mathbf F_4\), nor the exact count or projective stabilizer. The order-two unital classification of Grundhöfer–Stroppel–Van Maldeghem [2] treats unitals *already embedded inside a generalized Hermitian unital*; the tangent-line set of an arbitrary smooth plane cubic is not assumed to be such a subunital. Thus that embedding theorem does not directly imply the present classification. The local calculations here also rule out a shortcut via the maximal elliptic point count alone.

## Limitations
The statement is restricted to geometrically smooth plane cubic embeddings over \(\mathbf F_4\). It does not classify tangent-filling cubics with singularities, smooth curves of other degrees or fields, or abstract elliptic curves. The exhaustive finite step is certified by source-code enumeration and finite-field arithmetic, not by an independent formal proof assistant. A differently phrased older finite-geometry classification could potentially subsume the claim; bibliographic novelty remains subject to independent literature review. No independent audit has been performed.

## References
[1] S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420v1 (first posted 26 February 2023), Example 3.1 and Introduction; later in *Bull. Aust. Math. Soc.*, DOI: 10.1017/S0004972723000382. https://arxiv.org/abs/2302.13420

[2] T. Grundhöfer, M. J. Stroppel and H. Van Maldeghem, *Finite subunitals of the Hermitian unitals*, *Journal of Geometry* 113 (2022), article 22, Theorems 2.2 and 3.1, DOI: 10.1007/s00022-022-00636-4. https://cage.ugent.be/~hvm/artikels/249.pdf
