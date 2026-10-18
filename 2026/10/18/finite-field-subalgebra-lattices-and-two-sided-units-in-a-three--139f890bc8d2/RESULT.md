# Finite-field subalgebra lattices and two-sided units in a three-dimensional nonassociative deformation

## Finding
Let \(K=\mathbb F_q\) be any finite field and \(t\in K^\times\). On the three-dimensional vector space \(A_t=K1\oplus Ki\oplus Kj\), take the bilinear product specified by
\[
1x=x1=x,\qquad i^2=j^2=-1,\qquad ij=0,\qquad ji=t(i+j).
\]
Subalgebras below are linear subspaces closed under multiplication, **not assumed to contain the unit**. Define \(k=i+j\) and the three distinct two-dimensional subalgebras
\[
B_i=K1+Ki,\quad B_j=K1+Kj,\quad B_k=K1+Kk.
\]
Each pair of these intersects in \(K1\). They are the **only** proper two-dimensional subalgebras; every proper one-dimensional subalgebra lies in one of them. In particular there are no two-dimensional subalgebras omitting the unit, in any characteristic.

For a quadratic commutative \(K\)-algebra of type *inert* (the field \(\mathbb F_{q^2}\)), *double* (the dual numbers \(K[\varepsilon]/(\varepsilon^2)\)), or *split* (\(K\times K\)), define the following two functions:
\[
\begin{array}{c|ccc}
T&\mathrm{inert}&\mathrm{double}&\mathrm{split}\\\hline
\ell(T)&0&1&2\\
u(T)&q^2-1&q(q-1)&(q-1)^2
\end{array}
\]
Here \(\ell(T)\) counts non-unit-containing one-dimensional subalgebras of that quadratic algebra, while \(\nu(T)\) counts its multiplicatively invertible elements. Let \(T_a\) be the type of \(K[z]/(z^2+1)\) and \(T_k\) the type of \(K[z]/(z^2-tz+2)\). For odd \(q\), \(T_a\) is split when \(-1\) is a square, otherwise inert; \(T_k\) is split, double, or inert according as \(t^2-8\) is a nonzero square, zero, or a nonsquare. For even \(q\), \(T_a\) is always double and \(T_k\) always split.

**Complete numerical invariants.** Let \(s_r\) denote the number of \(r\)-tuples generating \(A_t\) as a (not necessarily unital) algebra. Then
\[
\boxed{\#\{\text{one-dimensional subalgebras}\}=1+2\ell(T_a)+\ell(T_k)},
\]
\[
\boxed{\#\{\text{all subalgebras}\}=6+2\ell(T_a)+\ell(T_k)},
\]
\[
\boxed{\#\{\text{elements with a two-sided inverse}\}
=2\nu(T_a)+\nu(T_k)-2(q-1)},
\]
\[
\boxed{s_r=q^{3r}-3q^{2r}+2q^r\quad(r\ge1)}.
\]
Every two-sided inverse, when it exists, is unique. The number of idempotents, including zero, is \(2+4\mathbf 1_{T_a=\mathrm{split}}+2\mathbf 1_{T_k=\mathrm{split}}\); the number of square-zero elements, including zero, is \(1+(q-1)(2\mathbf 1_{T_a=\mathrm{double}}+\mathbf 1_{T_k=\mathrm{double}})\).

The entire inclusion lattice is specified by the five types of members: \(0\), the line \(K1\), the \(2\ell(T_a)+\ell(T_k)\) additional lines, the three planes \(B_i,B_j,B_k\), and \(A_t\). Every additional line lies in exactly one of the three planes; \(K1\) lies in all three. Thus the formulas determine the full incidence structure, not merely total counts. In characteristic two the algebra always has exactly ten subalgebras, three elements with two-sided inverses when \(q=2\), and no one-element generating set when \(q=2\). More generally its count of two-sided invertible elements in even characteristic is \(3(q-1)^2\).

## Assumptions and scope
The parameter \(t\) must be nonzero, and \(K\) must be a finite field of any characteristic. No associativity, commutativity, or unit-preservation assumption on subalgebras is used. Generation means the smallest \(K\)-linear multiplication-closed subspace containing the listed elements. The excluded parameter \(t=0\) has many more unital planes and is not classified here. All formula symbols refer to this one family \(A_t\), not to arbitrary nonassociative algebras.

## Proof
**1. Three unital planes and no nonunital planes.** For \(v=bi+cj\), direct multiplication gives
\[
v^2=-(b^2+c^2)1+tbc(i+j).
\]
A plane containing \(1\) has the form \(K1+Kv\). Closure forces \(tbc(i+j)\in Kv\), so, since \(t\ne0\), it is precisely one of \(B_i,B_j,B_k\). Conversely each displayed plane is closed, and its defining quadratic relations are
\[
i^2=j^2=-1,\qquad k^2=tk-2.
\]
For a plane \(H\) omitting \(1\), the projection \(A_t\to A_t/K1\) restricts to an isomorphism from \(H\), so \(H\) has a basis \(x=i-u1\), \(y=j-v1\) for some \(u,v\in K\). It is the kernel of the linear functional \(L(a1+bi+cj)=a+ub+vc\). Closure under \(x^2,y^2,xy\) requires
\[
L(x^2)=-1-u^2=0,\qquad L(y^2)=-1-v^2=0,\qquad L(xy)=-uv=0.
\]
The first two equations make \(u,v\) nonzero; the third says their product is zero, impossible over a field. Thus the three unital planes exhaust all two-dimensional subalgebras.

**2. One-dimensional subalgebras and their incidences.** For \(z=a1+bi+cj\), one obtains
\[
\det[1,z,z^2]=tbc(b-c).
\]
If \(Kz\) is a subalgebra then \(z^2\in Kz\), making this determinant zero. Thus every one-dimensional subalgebra is contained in one of the three planes. The planes intersect pairwise in \(K1\), which prevents double-counting of other lines. In a two-dimensional unital quadratic algebra, a nonzero vector spans a subalgebra exactly when its square is a scalar multiple of itself. When that scalar is nonzero, rescale the vector to an idempotent; when it is zero, the vector is square-zero. A quadratic field has no additional lines, dual numbers have exactly the line generated by the nilpotent, and a split product has exactly its two primitive-idempotent lines. Hence the stated \(\ell\)-formula and inclusion lattice follow.

**3. Exact quadratic types.** Since \(B_i\cong B_j\cong K[z]/(z^2+1)\) and \(B_k\cong K[z]/(z^2-tz+2)\), the characteristic-odd quadratic discriminants are \(-4\) and \(t^2-8\). The square-class and repeated-root tests yield the three cases stated. In characteristic two, \(z^2+1=(z+1)^2\) and \(z^2-tz+2=z(z+t)\), with distinct factors for \(t\ne0\). Counting lines in the three quadratic algebras gives the complete subalgebra counts; counting idempotent and square-zero vectors in their non-unit lines gives the other two formulas.

**4. Two-sided inverses.** Let \(x=a1+bi+cj\) and \(y=d1+ei+fj\). Their commutator is
\[
xy-yx=t(ce-bf)(i+j).
\]
If \(xy=yx=1\) and \((b,c)\ne(0,0)\), then \((e,f)=\lambda(b,c)\) for some \(\lambda\in K\). The vector part of \(xy\) becomes \((a\lambda+d)(bi+cj)+t\lambda bc(i+j)\). If \(bc(b-c)\ne0\), the two displayed vectors are independent; their coefficients therefore force \(\lambda=d=0\), contradicting \(xy=1\). Thus every two-sided invertible element lies in one of the three planes. For a nonscalar element of such a plane, the commutator condition also forces its inverse to lie in the same plane. Scalar elements have their unique scalar inverses. Therefore invertibility and uniqueness reduce to the ordinary unit groups of the three commutative associative quadratic algebras. Their unit counts are \(\nu(\mathrm{inert})=q^2-1\), \(\nu(\mathrm{double})=q(q-1)\), and \(\nu(\mathrm{split})=(q-1)^2\). Inclusion-exclusion, using the common \(q-1\) nonzero scalars, yields \(2\nu(T_a)+\nu(T_k)-2(q-1)\).

**5. Generation.** Every proper subalgebra lies in one of \(B_i,B_j,B_k\). Thus an \(r\)-tuple generates the full algebra if and only if it is not wholly contained in any of the three planes. Each plane has \(q^2\) elements, while every pairwise and the triple intersection have \(q\) elements. Inclusion-exclusion gives \(q^{3r}-3q^{2r}+2q^r\) generating tuples. This remains valid for \(q=2\), when the single-generator count vanishes.

## Verification
The standalone `verify.py` constructs finite fields by modular arithmetic (prime fields) or explicit irreducible binary polynomials (fields of orders four and eight). It enumerates all one- and two-dimensional subspaces, verifies closure under the defining multiplication, solves the six linear equations for a two-sided inverse, computes generated subalgebras through repeated multiplication and linear spans, and independently enumerates idempotent and square-zero elements. Successful configurations: \((q,t)=(2,1),(3,1),(3,2),(4,1),(4,2),(5,1),(5,2),(7,1),(7,2),(8,1),(8,2),(11,1),(13,1)\). These thirteen finite cases are checks, not a substitute for the general proof above. Run `python verify.py` using Python 3.

## Relationship to prior work
Bermejo Valdés, *Complex slices, inverses, and deformations of a three-dimensional real algebra*, arXiv:2610.12483v1 (first publicly submitted September 13, 2026), studies these multiplication laws over \(\mathbb R\). In particular, its Sections 4, 5, and 9 identify the three quadratic planes, characterize two-sided inverses, and classify real subalgebras for the deformation. Those structural ingredients are acknowledged here. The present theorem supplies a complete **finite-field**, characteristic-uniform subalgebra lattice and its incidences, including nonunital subalgebras, and arithmetic formulas for rational points, two-sided units, nilpotents, idempotents, and generating tuples. The real classification does not imply these cardinalities in positive characteristic. Abdurasulov–Eraliyeva–Kaygorodov, arXiv:2603.04391v1, classifies complex **structurable** algebras; it neither studies these finite fields nor implies these formulas for this general nonassociative family. These comparisons do not assert absolute publication priority.

## Limitations
Only \(t\ne0\) is covered. In characteristic two, the statement concerns this bilinear multiplication without imposing alternate definitions of Jordan or structurable algebras. This is a small-family structural classification, not a new theorem about all three-dimensional nonassociative algebras. No independent external mathematical audit has been performed; equivalent formulas could exist under different algebra notation in unindexed literature.

## References
1. A. J. Bermejo Valdés, *Complex slices, inverses, and deformations of a three-dimensional real algebra*, arXiv:2610.12483v1, Sections 2, 4, 5, 9, https://arxiv.org/html/2610.12483v1.
2. K. Abdurasulov, M. Eraliyeva, I. Kaygorodov, *Unital 3-dimensional structurable algebras: classification, properties and AK-construction*, arXiv:2603.04391v1, https://arxiv.org/html/2603.04391v1.
