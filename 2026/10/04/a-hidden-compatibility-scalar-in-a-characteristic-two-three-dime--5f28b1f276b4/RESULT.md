# A hidden compatibility scalar in a characteristic-two three-dimensional Poisson family
## Finding
Let \(F\) be a field of characteristic \(2\). For \(q\in F\), consider the Poisson algebra \(P_q\) with basis \(x,u,v\), Lie multiplication
\[
[x,u]=u,\qquad [x,v]=v+qu,\qquad [u,v]=0,
\]
and commutative associative multiplication
\[
xv=u,
\]
with every other product of basis vectors equal to zero. This is the family denoted \(P_{3,22}(q)\) in Petrov--Pypka.

Set \(R=P_q^2\) and \(V=[P_q,P_q]\). Then \(R=Fu\) and \(V=Fu\oplus Fv\), so both are intrinsic. Call a basis \((x_0,u_0,v_0)\) adapted if
\[
u_0\in R\setminus\{0\},\qquad v_0\in V\setminus R,\qquad x_0\notin V,
\]
\[
x_0v_0=u_0,\qquad [x_0,u_0]=u_0.
\]
There is a unique scalar \(\kappa(P_q)\in F\) satisfying
\[
[x_0,v_0]=v_0+\kappa(P_q)u_0
\]
for every adapted basis, and \(\kappa(P_q)=q\) in the displayed basis. Thus the parameter is an intrinsic compatibility scalar rather than a coordinate artifact.

The associative algebra is independent of \(q\). The underlying Lie algebras have exactly two isomorphism types inside the family: \(q=0\), and \(q\ne0\). Nevertheless, Petrov--Pypka prove that the Poisson algebras are pairwise distinguished by the full scalar: \(P_q\cong P_{q'}\) as Poisson algebras exactly when \(q=q'\). Hence distinct nonzero parameters produce nonisomorphic Poisson algebras with isomorphic associative components and isomorphic Lie components.

This is dimension-minimal. In dimensions at most two, the associative and Lie products cannot both be nonzero, so the ordered pair consisting of the associative-algebra and Lie-algebra isomorphism types determines the Poisson isomorphism type. For \(F=\mathbb F_{2^m}\) with \(m\ge2\), the nonzero parameters therefore give \(2^m-1\) distinct Poisson classes over one fixed pair of component-algebra isomorphism types.

## Assumptions and scope
The field is arbitrary of characteristic \(2\). The assertion about two underlying Lie-isomorphism types is internal to the family \(P_q\). The statement about \(2^m-1\) classes concerns the nonzero-parameter subfamily and does not assert that no other three-dimensional Poisson families share the same component types.

The minimality assertion concerns the phenomenon of two nonisomorphic Poisson algebras having isomorphic commutative-associative components and isomorphic Lie components. It uses Petrov--Pypka's arbitrary-field dimension-two result that the two products cannot simultaneously be nonzero.

## Proof
First, the multiplication table gives
\[
P_q^2=Fu,
\]
while the two brackets \([x,u]=u\) and \([x,v]=v+qu\) span \(Fu\oplus Fv\). Hence
\[
R=Fu,\qquad V=Fu\oplus Fv.
\]

Let \((x_0,u_0,v_0)\) be adapted. Relative to the displayed basis write
\[
u_0=au,\qquad v_0=bu+cv,\qquad x_0=dx+ru+sv,
\]
with \(a,c,d\ne0\). Since the only nonzero associative basis product is \(xv=u\), the condition \(x_0v_0=u_0\) gives \(dc=a\). Because \(V\) is abelian as a Lie algebra,
\[
[x_0,u_0]=da\,u.
\]
The adapted condition \([x_0,u_0]=u_0\) therefore gives \(d=1\), and hence \(c=a\). Consequently
\[
[x_0,v_0]=b[x,u]+a[x,v]
              =bu+a(v+qu)
              =v_0+q u_0.
\]
Thus every adapted basis returns the same coefficient \(q\), proving that \(\kappa(P_q)=q\) is intrinsic.

The associative multiplication does not involve \(q\), so all associative components are identical after identifying the displayed bases.

For the Lie component, let \(A_q=\operatorname{ad}_x|_V\). In the ordered basis \((u,v)\),
\[
A_q=\begin{pmatrix}1&q\\0&1\end{pmatrix}.
\]
If \(q,q'\ne0\), the map
\[
x\longmapsto x',\qquad u\longmapsto q'u',\qquad v\longmapsto qv'
\]
is an invertible Lie-algebra homomorphism from the \(q\)-algebra to the \(q'\)-algebra. Thus all nonzero parameters have isomorphic Lie components.

They are not isomorphic to the \(q=0\) Lie algebra. The derived ideal \(V\) is characteristic. For every element \(y\notin V\), the restriction \(\operatorname{ad}_y|_V\) is a nonzero scalar operator when \(q=0\), whereas for \(q\ne0\) it is a non-scalar scalar-plus-rank-one-nilpotent operator. This scalar-versus-nonscalar property is preserved by Lie isomorphism.

Petrov--Pypka prove directly that \(P_q\cong P_{q'}\) as Poisson algebras if and only if \(q=q'\). Combining that theorem with the two component calculations shows that all distinct nonzero parameters are invisible to the separate component-isomorphism types but remain visible to Poisson isomorphism.

Finally, in dimension one the Lie product is zero. In dimension two, Petrov--Pypka prove that the associative and Lie products cannot both be nonzero. If one product is zero, an isomorphism of the other component automatically preserves both Poisson operations. Therefore the component pair determines the Poisson class in dimensions at most two, establishing dimension-three minimality.

## Verification
The proof uses only intrinsic subspaces and exact symbolic identities. The critical change-of-adapted-basis calculation forces \(d=1\) and \(c=a\), after which the coefficient of \(u_0\) in \([x_0,v_0]-v_0\) is exactly \(q\). No finite experiment is used as a substitute for an infinite-field argument.

For the Lie-isomorphism statement, substitution into the two defining brackets verifies the explicit map for arbitrary nonzero \(q,q'\). The separation of \(q=0\) from \(q\ne0\) uses the characteristic ideal \(V=[P_q,P_q]\), so it does not depend on a chosen complement.

The dimension-minimality argument was checked against the dimension-two theorem in the primary source. The source's parameter-separation theorem is used only for Poisson nonisomorphism; the compatibility-scalar invariance and the collapse of the nonzero Lie parameters are proved above.

## Relationship to prior work
Petrov and Pypka classify Poisson algebras of dimension at most three over arbitrary fields. Their characteristic-two family \(P_{3,22}(q)\) has both operations nonzero, and they prove that two members are Poisson-isomorphic exactly when their parameters agree. The present finding extracts a basis-free compatibility scalar from that family and compares the forgetful component types: the associative component is constant, while every nonzero parameter has the same Lie-isomorphism type.

Remm studies deformations that preserve an underlying associative structure or preserve an underlying Lie structure, giving broader conceptual context for varying Poisson compatibility. That work is characteristic-zero and does not state the characteristic-two three-dimensional component-collapse phenomenon here. Abdelwahab, Fernández Ouaridi, and Martín González classify three-dimensional Poisson algebras over the complex field; the characteristic-two family used here is outside that setting.

Database and exact-form searches for the family name, its defining products, and the simultaneous “same associative / same Lie” phenomenon did not locate an equivalent published statement. The closest indexed records concerned either invariants of three-dimensional Lie algebras or other Poisson families, not this compatibility fiber.

## Limitations
The conclusion does not classify every fiber of the forgetful map from Poisson algebras to pairs of component algebras. It isolates one explicit, dimension-minimal fiber phenomenon inside \(P_{3,22}(q)\). The exact global fiber over the same pair of component types could contain Poisson algebras from other families and is not asserted here.

The basis-free scalar is closely related to the coefficient comparison already used in the primary source's proof that \(q\) is an isomorphism invariant. The additional content is the adapted-basis interpretation, the collapse of all nonzero Lie parameters to one Lie-isomorphism type, and the resulting sharp dimension-minimal failure of component types to determine Poisson isomorphism.

## References
1. A. V. Petrov and O. O. Pypka, *On the Structure of Low-Dimensional Poisson Algebras over Arbitrary Fields*, arXiv:2609.13784v1, 2026.
2. E. Remm, *Associative and Lie deformations of Poisson algebras*, arXiv:1105.2670, 2011.
3. H. Abdelwahab, A. Fernández Ouaridi, and C. Martín González, *Degenerations of Poisson algebras*, arXiv:2209.09150, 2022.
