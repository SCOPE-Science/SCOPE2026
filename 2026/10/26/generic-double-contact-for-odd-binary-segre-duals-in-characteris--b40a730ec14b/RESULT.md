# Generic double contact for odd binary Segre duals in characteristic two

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\), let \(r\ge3\) be odd, set \(N=2^r-1\), and let \(X_r\subset\mathbb P^N_k\) be the Segre embedding of \((\mathbb P^1_k)^r\). Write \(C_{X_r}\) for its conormal incidence variety and \(X_r^\vee\) for its **reduced** projective dual. The conormal projection
\[
\pi:C_{X_r}\longrightarrow X_r^\vee
\]
is generically finite with separable degree \(1\) and **purely inseparable degree exactly \(2\)**. Equivalently, for a general closed hyperplane \(H\in X_r^\vee(k)\), the scheme of points of tangency on \(X_r\) is isomorphic to \(\operatorname{Spec}(k[\epsilon]/(\epsilon^2))\): it has one geometric point of length two.

In the smallest case \(r=3\), with dual coordinates \(a_{ijk}\) indexed by \(i,j,k\in\{0,1\}\), the reduced dual is the **smooth** quadric
\[
X_3^\vee=V(a_{000}a_{111}+a_{001}a_{110}+a_{010}a_{101}+a_{011}a_{100})\subset\mathbb P^7.
\]
Thus an explicit, smooth dual can have an inseparable conormal projection of degree two.

## Assumptions and scope
All varieties are over the stated algebraically closed field. Tangency is scheme-theoretic: for the hyperplane section \(F=0\) on the smooth variety \(X_r\), its contact scheme is cut out locally by \(F\) and all first derivatives of \(F\). The phrase *general hyperplane* means a point in a nonempty Zariski-open subset of the reduced irreducible dual. The assertion applies to every odd integer \(r\ge3\); no assertion is made about even \(r\), general products with larger projective factors, or special tangent hyperplanes.

## Proof
**1. The dual is a hypersurface.** The Segre duality theorem of Kaji (2003, main theorem (1)) proves that the dual of a product of projective spaces is a hypersurface exactly when each factor dimension is at most half their sum. This holds for \(r\ge3\) projective lines. Since the conormal variety is a projective bundle over the smooth irreducible \(r\)-fold \(X_r\), it is irreducible of dimension \(N-1\); hence \(\pi\) is dominant and generically finite over the dual hypersurface.

**2. A general individual contact has length two.** Homogeneity permits work at \(([1:0],\ldots,[1:0])\). With local parameters \(x_1,\ldots,x_r\), a hyperplane tangent there restricts to a general multilinear function
\[
F(x)=\sum_{\substack{S\subseteq\{1,\ldots,r\}\\ |S|\ge2}}c_S\prod_{i\in S}x_i
     =q(x)+\text{terms of degree at least three},\qquad
q(x)=\sum_{i<j}a_{ij}x_i x_j.
\]
The polar bilinear form of \(q\) has matrix \(B\) with zero diagonal and off-diagonal entries \(a_{ij}\). Because \(r\) is odd, \(B\) has rank at most \(r-1\). It has generic rank exactly \(r-1\): for example, set the coefficients on the triangle \(12,13,23\) equal to \(1\), pair the remaining even number of indices disjointly with coefficient \(1\), and set all others to zero. For this specialization \(\ker B\) is spanned by \(v=(1,1,1,0,\ldots,0)\), and \(q(v)=1\) in characteristic two. Hence on a nonempty open set \(\ker B=kv\) and \(q(v)\ne0\), where nonvanishing does not depend on the choice of a nonzero generator of this line.

Take linear coordinates \((y_1,\ldots,y_{r-1},t)\) adapted to the radical, with \(t\)-axis \(kv\). The quadratic part is \(q_U(y)+\lambda t^2\) with \(\lambda\ne0\) and nondegenerate polar matrix for \(q_U\). The formal implicit-function theorem applied to the \(r-1\) equations \(F_{y_i}=0\) uniquely expresses each \(y_i\) as a power series in \(t\) with order at least two. Substitution gives
\[
F(y(t),t)=\lambda t^2+O(t^3),\qquad F_t(y(t),t)=O(t^2).
\]
The completed local contact algebra is therefore \(k[[t]]/(t^2)\), of length exactly two. This argument uses the hyperplane equation as well as the first derivatives; Hessian corank one alone would not establish the length.

**3. No second geometric contact for a general hyperplane when \(r\ge5\).** For an ordered pair \((P,Q)\) of distinct points of \((\mathbb P^1)^r\), suppose the coordinates differ in exactly \(j\) factors. The pair stratum has dimension \(r+j\), and the product \((\operatorname{PGL}_2)^r\) moves it to a pair of binary-coordinate vertices at Hamming distance \(j\). Each embedded tangent space is spanned by the \(r+1\) coordinate vectors in the Hamming ball of radius one about its vertex. The two balls intersect in \(e_j=2\) vectors for \(j=1,2\), and in no vectors for \(j\ge3\). Thus hyperplanes tangent at both points form a projective linear space of dimension \(N-(2r+2-e_j)\). The corresponding incidence space has dimension at most
\[
N-r+j-2+e_j.
\]
For every \(r\ge5\), this is strictly smaller than \(N-1=\dim X_r^\vee\), for all \(1\le j\le r\). Consequently a general member of the dual cannot have two distinct geometric contact points, even after passage to an algebraic closure.

**4. Unique geometric contact when \(r=3\).** Express a trilinear hyperplane section as \(x^{\mathsf T}(z_0 A_0+z_1 A_1)y\), with \(2\times2\) matrices \(A_0,A_1\). Write
\[
\det(z_0 A_0+z_1 A_1)=\alpha z_0^2+\beta z_0z_1+\gamma z_1^2.
\]
A tangency of the trilinear form at a point where the matrix pencil has rank one is exactly a double root of this binary quadratic, together with its unique left and right kernels. In characteristic two the discriminant is \(\beta^2\); thus the **reduced** dual has equation \(\beta=0\). Here \(\beta=a_{000}a_{111}+a_{001}a_{110}+a_{010}a_{101}+a_{011}a_{100}\), whose polar matrix is nonsingular, so this dual quadric is smooth. For a general point of it, \(\alpha\gamma\ne0\) and the determinant quadratic is a nonzero square, with exactly one geometric root. At that root the matrix is of rank one, determining one left kernel, one right kernel, and hence one point of tangency.

**5. Degree and inseparability.** Steps 2--4 prove that a general geometric fibre of \(\pi\) is supported at exactly one point and has local algebra \(k[\epsilon]/(\epsilon^2)\). Its scheme length, hence the degree of the generically finite map, is two. A separable field extension of degree two would have two geometric generic points; therefore this degree-two extension is purely inseparable.

## Verification
The independent executable `verify.py` uses exact integer/symbolic operations and arithmetic modulo two. It checks the \(2\times2\) determinant-pencil middle coefficient, constructs the quadratic-radical specialization for \(r=3,5,7,9\), and enumerates radius-one Hamming-ball intersections to check the dimension formula at those values. Execute with `python verify.py` (SymPy required); the expected output begins `VERIFY_OK`. These tests are only reproducibility aids. The argument for all odd \(r\) is the symbolic rank, contact-algebra, and incidence-dimension proof above.

## Relationship to prior work
Kaji (2003) proves that products of projective spaces have hypersurface duals under the triangle inequalities, and that the Segre embedding is **nonreflexive** in characteristic two when the total dimension is odd. His theorem and Hessian-rank argument do **not** specify the degree of the conormal projection or determine the full scheme length of a general contact. The present result provides that quantitative degree-two refinement, using the nonzero value of the quadratic form on the Hessian radical and a distinct-contact incidence bound. Ottaviani (2013) supplies background on hyperdeterminants and Segre duals; its general treatment is not used as an originality argument about characteristic two. The characteristic-two square of Cayley's \(2\times2\times2\) hyperdeterminant is acknowledged as classical, not claimed new.

## Limitations
This result concerns a generic hyperplane of the **reduced** dual and does not classify exceptional contact fibres, the integral discriminant's multiplicities in arbitrary formats, or higher inseparability for different projective embeddings. Kaji's broad nonreflexivity theorem is known: the potentially new point is only the uniform exact inseparable degree and double-contact structure. Related formulations in older literature might already imply this refinement; an exhaustive historical classification is not claimed.

## References
- H. Kaji, *On the Duals of Segre Varieties*, Geometriae Dedicata **99** (2003), 221–229. DOI: 10.1023/A:1024968503486. Author preprint: https://kaji.w.waseda.jp/preprints/DSV3.pdf.
- G. Ottaviani, *Introduction to the Hyperdeterminant and to the Rank of Multidimensional Matrices*, in *Commutative Algebra* (2013), 609–638, arXiv:1301.0472. https://arxiv.org/abs/1301.0472.
