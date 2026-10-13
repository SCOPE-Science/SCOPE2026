# Orthogonality is the missing boundary in the \(B_5(2)\) Chow-quotient example
## Finding
Consider the equalized one-dimensional torus action of Example 4.8 of Occhetta--Solá Conde on the orthogonal Grassmannian of lines
\[
X=B_5(2),
\]
where the ambient quadric is \(Q^9=B_5(1)\). Write its quadratic vector space as
\[
V=\mathbf C e_-\oplus W\oplus \mathbf C e_+,
\]
with \(e_-\) and \(e_+\) isotropic, \(B(e_-,e_+)=1\), \(W\perp\langle e_-,e_+\rangle\), and \(B|_W\) nondegenerate. The extremal fixed components are canonically
\[
Y_-\cong Y_+\cong Q(W)\cong Q^7,
\]
via
\[
[u]\longmapsto \ell_-(u)=\mathbf P\langle e_-,u\rangle,
\qquad
[v]\longmapsto \ell_+(v)=\mathbf P\langle e_+,v\rangle.
\]

For distinct \([u],[v]\in Q(W)\), the lines \(\ell_-(u)\) and \(\ell_+(v)\) are disjoint. Their projective span cuts \(Q^9\) in a smooth quadric surface if and only if
\[
B(u,v)\ne0.
\]
If \(B(u,v)=0\), the section is reducible: it is the union of two planes meeting along the inner fixed line
\[
m=\mathbf P\langle u,v\rangle\subset Q(W).
\]
In that case the unique Chow-quotient cycle with the prescribed endpoints is the reduced two-component invariant chain
\[
C_-(u,v)\cup C_+(u,v),
\]
where
\[
C_-(u,v)=\left\{\mathbf P\langle e_-+t v,u\rangle:t\in\mathbf P^1\right\},
\qquad
C_+(u,v)=\left\{\mathbf P\langle v,u+s e_+\rangle:s\in\mathbf P^1\right\}.
\]
Consequently, if \(E\) is the unique boundary divisor of the Chow quotient \(\mathcal C X\), then the endpoint contraction
\[
\pi_1:\mathcal C X\longrightarrow Q^7\times Q^7
\]
restricts to a birational map
\[
E\dashrightarrow I,
\qquad
I=\left\{([u],[v])\in Q^7\times Q^7:B(u,v)=0\right\}.
\]
Thus the statement in Example 4.8 that every pair of disjoint endpoint lines spans a smooth quadric surface has a codimension-one exception \(I\setminus\Delta\). The surjectivity conclusion of the example is nevertheless valid there: the missing points are represented by the explicit reducible chains above.

## Assumptions and scope
The base field is \(\mathbf C\). The quadratic form is nondegenerate and the torus action is the equalized action used in Example 4.8 of arXiv:2503.19663v1. The claim concerns only the specific criticality-two action on \(B_5(2)\) and the endpoint morphism \(\pi_1\); it does not identify the entire Chow quotient with a blow-up, nor does it classify higher-criticality orthogonal-Grassmannian quotients.

The incidence divisor \(I\) is defined using the polar form \(B\) of the quadratic form on \(W\). Rescaling \(B\) does not change \(I\).

## Proof
Take distinct isotropic vectors \(u,v\in W\). The endpoint lines are disjoint because an equality
\[
a e_-+b u=c e_++d v
\]
in the direct sum \(\mathbf C e_-\oplus W\oplus\mathbf C e_+\) forces \(a=c=0\), and then forces \(u\) and \(v\) to be proportional if the common projective point exists.

On the four-dimensional vector space \(\langle e_-,u,e_+,v\rangle\), a vector with coordinates \((a,b,c,d)\) has quadratic value, up to a harmless nonzero scalar normalization,
\[
q(ae_-+bu+ce_++dv)=2ac+2B(u,v)bd.
\]
Hence the associated quadric in the projective span \(\mathbf P^3\) has rank four exactly when \(B(u,v)\ne0\). In that case it is smooth, and the two disjoint endpoint lines lie in one ruling, giving the irreducible orbit conic described in the source.

If \(B(u,v)=0\), the equation reduces to \(ac=0\). Thus the section is the union
\[
\mathbf P\langle e_-,u,v\rangle\ \cup\ \mathbf P\langle u,v,e_+\rangle,
\]
whose intersection is \(m=\mathbf P\langle u,v\rangle\). Because \(u\) and \(v\) are isotropic and orthogonal, \(m\subset Q(W)\), so it represents a point of the inner fixed component.

The two displayed families \(C_-(u,v)\) and \(C_+(u,v)\) consist of isotropic two-planes. For example,
\[
B(e_-+tv,u)=tB(v,u)=0,
\]
and each generator is isotropic; the verification for the second family is identical. Their limits are
\[
\ell_-(u)\longrightarrow m\longrightarrow\ell_+(v).
\]
Each component is a one-dimensional torus-orbit closure of one Plücker degree, so their reduced union satisfies the invariant-chain conditions used in Corollary 2.7 of the source. Since \(X\) has Picard number one, that corollary places the chain in \(\mathcal C X\).

Conversely, a reducible cycle in this criticality-two quotient has a node represented by a line \(m'\subset Q(W)\) in the inner fixed component. A first component joining \(\ell_-(u)\) to \(m'\) forces \([u]\in m'\), while a second component joining \(m'\) to \(\ell_+(v)\) forces \([v]\in m'\). For distinct \([u],[v]\), this gives
\[
m'=\mathbf P\langle u,v\rangle.
\]
Such a line is contained in \(Q(W)\) exactly when \(B(u,v)=0\). The two degree-one orbit closures with these endpoints are then the explicit components above, so the reducible cycle is unique.

Theorem 3.12 of the source says that, at criticality two, the reducible locus is one irreducible boundary divisor \(E\). The preceding argument shows that its image under \(\pi_1\) is contained in \(I\), contains the dense open subset \(I\setminus\Delta\), and has a single point over every pair in that open subset. The incidence variety \(I\) is irreducible: its projection to the first \(Q^7\) has irreducible tangent-hyperplane quadric sections as fibers. Therefore \(E\to I\) is birational.

## Verification
The critical local calculation is the rank test for
\[
2ac+2\beta bd,
\qquad \beta=B(u,v).
\]
Its symmetric coefficient matrix has nonzero determinant exactly when \(\beta\ne0\). At \(\beta=0\), the factorization \(ac=0\) gives the two planes and their intersection line directly.

The chain check is exact rather than experimental: substitution into the bilinear form proves both two-plane families are isotropic for every parameter, and their parameter limits give the three required fixed lines. No finite computation is being used to infer an infinite statement.

The source's Example 4.8 was read in full around the endpoint morphism; it explicitly asserts smoothness for every disjoint endpoint pair and then derives surjectivity and birationality. Corollary 2.7 and Theorem 3.12 were separately checked because they are the two nontrivial source results used to place the reducible chain in the quotient and to identify the unique boundary divisor.

## Relationship to prior work
Occhetta--Solá Conde prove that the Chow quotient in this example is smooth, that its reducible cycles form a unique boundary divisor, and that the endpoint morphism is a divisorial birational contraction. Their Example 4.8 describes a smooth quadric surface and an irreducible orbit conic for a pair of disjoint extremal lines. The calculation above shows that disjointness alone is insufficient: orthogonality of the two \(W\)-points is a separate codimension-one condition, and on that condition the surface splits and the Chow cycle becomes reducible.

Targeted searches for the orthogonality-incidence formulation, the reducible-chain formulation, and this specific correction to Example 4.8 did not locate a published statement of the same claim. The closest checked source is the initiating paper itself, whose stated smoothness assertion is strictly stronger and fails on \(I\setminus\Delta\).

## Limitations
This result does not determine the scheme structure of every exceptional fiber over the diagonal, and it does not prove that \(\mathcal C X\) is the blow-up of \(Q^7\times Q^7\) along the diagonal. It identifies the codimension-one reducible locus away from the diagonal and its birational image. A prior source using different terminology for the same incidence divisor could have escaped the targeted searches.

## References
1. G. Occhetta and L. E. Solá Conde, *Chow quotients of \(\mathbf C^*\)-actions on convex varieties*, arXiv:2503.19663v1, 25 March 2025; see Corollary 2.7, Theorem 3.12, and Example 4.8. Published in *Épijournal de Géométrie Algébrique* 10 (2026), Article 16.
