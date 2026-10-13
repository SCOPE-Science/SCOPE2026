# Affine moduli, sharp symmetry, and polar collapse for osculating-conic arrangements

## Finding
Let \(k\) be an algebraically closed field of arbitrary characteristic. For each finite set \(S\subset k\) of \(m\geq3\) distinct elements, define the reduced plane curve
\[
\mathcal A_S=V(F_S),\qquad F_S=\prod_{t\in S}(z^2-xy+t xz)\subset\mathbb P^2_k.
\]
Its components are smooth conics belonging to the osculating pencil studied in [1]. The following statements hold simultaneously.

**Projective moduli and full stabilizer.** The curves \(\mathcal A_S\) and \(\mathcal A_T\), for sets of equal cardinality, are projectively equivalent over \(k\) if and only if \(T=aS+b\) for some \(a\in k^\times\), \(b\in k\). The full projective automorphism group is, canonically,
\[
\operatorname{Aut}_{\mathbb P^2}(\mathcal A_S)\simeq\{(a,b)\in k^\times\ltimes k:aS+b=S\}.
\]
In particular its order is at most \(m(m-1)\).

**Sharp symmetry boundary.** Equality \(|\operatorname{Aut}_{\mathbb P^2}(\mathcal A_S)|=m(m-1)\) holds if and only if \(k\) has positive characteristic \(p\), \(m=p^e\) with \(e\geq1\), and \(S\) is an affine image of the unique subfield \(\mathbb F_{p^e}\subset k\). In that case the full automorphism group is \(\operatorname{AGL}(1,p^e)\).

**Arithmetic polar collapse on the sharp-symmetry locus.** For the distinguished set \(S=\mathbb F_q\), where \(q=p^e\geq3\), the homogeneous equation and its gradient are
\[
F_{\mathbb F_q}=g^q-f^{q-1}g,\qquad
\nabla F_{\mathbb F_q}=f^{q-2}(z^3,x^2z,-x^2y-xz^2),
\quad f=xz,\ g=z^2-xy.
\]
After removing the greatest common factor, the polar map is
\[
\Phi=[z^3:x^2z:-x^2y-xz^2].
\]
It is dominant, of total function-field degree exactly \(2\): it is generically separable for odd \(p\) and purely inseparable for \(p=2\). These properties also hold for every affine image of \(\mathbb F_q\), using the induced projective conjugacy and the dual transformation of the polar map.

**Finite-field geometric moduli.** Let \(q=p^e\) and \(3\leq m\leq q\). The number \(N(q,m)\) of geometric projective equivalence classes among the arrangements whose individual conics have distinct parameters in \(\mathbb F_q\) equals
\[
\frac{1}{q(q-1)}\left[\binom qm+(q-1)\mathbf1_{p\mid m}\binom{q/p}{m/p}+q\sum_{\substack{d\mid(q-1)\\d>1}}\varphi(d)\left(\mathbf1_{d\mid m}\binom{(q-1)/d}{m/d}+\mathbf1_{d\mid(m-1)}\binom{(q-1)/d}{(m-1)/d}\right)\right].
\]
Here any term whose indicated divisibility condition fails is zero, and \(\varphi\) is Euler's totient function. The formula counts projective equivalence over the algebraic closure, not merely over \(\mathbb F_q\).

## Assumptions and scope
Work with the **particular coordinate pencil** \(q_t=z^2-xy+t xz\), not all conic pencils. The base field \(k\) is algebraically closed for geometric equivalence and stabilizers. Distinct elements of \(S\) guarantee that \(F_S\) is reduced. The automorphism group consists of projective linear transformations, not arbitrary abstract automorphisms of the normalization or of the reducible curve. The polar degree is the field-extension degree, including inseparability; it is not the geometric generic-fiber cardinality in characteristic two. The finite-field count concerns *split* unions of conics indexed by an \(m\)-subset of \(\mathbb F_q\), with equivalences allowed over its algebraic closure.

## Proof
**1. Intersections and intrinsic marking.** Each \(q_t\) is smooth in every characteristic: its derivative with respect to \(y\) is \(-x\), and when \(x=0\) its sole point has coordinates \(P=[0:1:0]\), where the derivative with respect to \(x\) equals \(-1\). Any pair of distinct components meets only at \(P\) and \(Q=[1:0:0]\), because \(q_s-q_t=(s-t)xz\). Their local intersection multiplicities are \(3\) at \(P\) and \(1\) at \(Q\): in the chart \(y=1\), the branch \(q_t=0\) has \(x=z^2/(1-tz)\), and the differences of two such expressions vanish to order exactly three; in the chart \(x=1\), the branch is \(y=z^2+tz\), and distinct branches meet transversely. All \(m\) branches have the same tangent \(x=0\) at \(P\); at \(Q\) their tangents \(y=tz\) are pairwise distinct. These are exactly the two singular points of \(\mathcal A_S\). Thus \(P\), \(Q\), and the tangent line \(x=0\) are intrinsically distinguished by the divisor, since \(m\geq3\).

**2. The complete projective action.** A projectivity taking \(\mathcal A_S\) to \(\mathcal A_T\) must fix \(P,Q\) and preserve \(x=0\). Hence its matrix, after a scalar, is
\[
M=\begin{pmatrix}A&0&0\\0&C&D\\0&0&G\end{pmatrix},\qquad ACG\ne0.
\]
Substitution into \(q_t\) yields \(G^2z^2-ACxy+(tAG-AD)xz\). Being proportional to a member of the same normalized pencil forces \(AC=G^2\); its target parameter is affine in \(t\), with nonzero slope \(A/G\). Conversely, for any \(a\ne0\) and \(b\), the projectivity
\[
T_{a,b}:[x:y:z]\longmapsto[a^{-1}x:ay+bz:z]
\]
satisfies \(q_{at+b}(T_{a,b}(x,y,z))=q_t(x,y,z)\), and therefore carries \(\mathcal A_S\) onto \(\mathcal A_{aS+b}\). The map from projective stabilizers to affine permutations of \(S\) is injective: an affine transformation acting identically on two distinct parameters is the identity and the corresponding displayed projectivity is the identity; the matrix normal form shows no other projectivity is possible. This proves the moduli and stabilizer statements. An affine permutation is determined by the images of any two distinct parameters, so its order is at most \(m(m-1)\).

**3. Rigidity of equality.** Equality gives sharp two-transitivity on ordered pairs of distinct elements of \(S\). Affine-normalize so \(0,1\in S\). For each \(c\in S^\times\), the unique affine element taking \((0,1)\) to \((0,c)\) is the scaling \(t\mapsto ct\), hence \(cS=S\). The element taking \((0,1)\) to \((1,0)\) is the reflection \(t\mapsto1-t\). Conjugation by the scalings supplies the reflections \(t\mapsto c-t\) for all \(c\in S^\times\). Choose distinct \(c,d\in S^\times\), possible because \(m\ge3\). Composing their reflections gives the nonzero translation \(t\mapsto t+(c-d)\). Conjugating this translation by each scaling \(t\mapsto a t\), for \(a\in S^\times\), gives translations by \(a(c-d)\). Such translates of zero lie in \(S\); since \(S\) and \((c-d)S\) have equal cardinality, \((c-d)S=S\). Therefore translations by every element of \(S\) preserve \(S\), proving closure under addition and additive inverses. The scaling invariance already establishes closure under multiplication; as \(0,1\in S\), the finite set \(S\) is a finite subfield of \(k\). A finite subfield has order \(p^e\), and it exists only in characteristic \(p>0\). Conversely its full affine group preserves it and has order \(q(q-1)\), attaining the bound.

**4. Polar map.** Over \(\mathbb F_q\), the root identity \(\prod_{t\in\mathbb F_q}(U+t)=U^q-U\) gives \(F=g^q-f^{q-1}g\) by homogenization. In characteristic \(p\), \(q=0\) and \(-(q-1)=1\). Differentiation gives \(\nabla F=f^{q-2}(g\nabla f-f\nabla g)\), and direct expansion gives the claimed cubic triple. It has no nonconstant common factor: the first two entries have common factor \(z\), while the third is not divisible by \(z\). On the dense open chart \(x=1,z=u\ne0,y=v\), the two function-field coordinates of the target obtained by dividing by the second polar coordinate are
\[
s=u^2,\qquad w=-\frac{v+u^2}{u}.
\]
Thus \(k(u,v)=k(s,w)(u)\), with the irreducible quadratic relation \(u^2=s\) over the rational function field \(k(s,w)\). The field extension has degree two; it is separable exactly when \(p\ne2\). In characteristic two, the degree-two extension is purely inseparable. Affine changes of parameters are realized by projectivities, whose chain rule changes polar source and target only by invertible linear transformations; dominance, total degree and separability are therefore unchanged.

**5. The exact finite-field orbit count.** An affine equivalence over \(\overline{\mathbb F}_q\) between two subsets of \(\mathbb F_q\) of size at least two is already defined over \(\mathbb F_q\): the images of two distinct elements uniquely determine \(a,b\in\mathbb F_q\). Hence geometric classes equal \(\operatorname{AGL}(1,q)\)-orbits of \(m\)-subsets. Burnside's lemma has three types: the identity fixes \(\binom qm\) subsets; each of the \(q-1\) nontrivial translations is a product of \(q/p\) cycles of length \(p\); and for every nonidentity slope of order \(d\mid q-1\), its \(q\) affine maps each have one fixed point and \((q-1)/d\) cycles of length \(d\). There are \(\varphi(d)\) slopes of order \(d\). Selecting cycles (possibly including the one fixed point) gives exactly the displayed formula.

## Verification
The companion dependency-free `verify.py` checks exact affine coordinate substitutions in three odd prime fields, directly enumerates all \(5616\) projective transformations over \(\mathbb F_3\) to recover precisely six stabilizers, and independently compares the Burnside formula with exhaustive orbit enumeration for all admissible subset sizes over \(\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_{11},\mathbb F_{13}\). It also checks the sharp \(m=q\) cases over several prime powers and verifies the Frobenius product and exact gradient polynomial identities in characteristics three, five and seven. These calculations check special instances only; the universal assertions follow from the preceding arguments.

## Relationship to prior work
Di Gennaro, Ilardi, Miró-Roig, Schenck and Vallès [1, Example 4.3] introduced the precise pencil \(f=xz\), \(g=z^2-xy\) and established characteristic-zero freeness for specific unions of smooth members. Their Theorem 3.6 and Proposition 4.1 address freeness of pencil unions, not the full projective stabilizer, the equivalence classification by parameter subsets, or the characteristic-dependent degree and inseparability of the polar map for the full finite-field parameter set. The earlier paper of Dimca [2] gives conic-pencil freeness and topology, but its available abstract and bibliographic material do not establish the present geometric/arithmetic group-and-polar classification; its complete text has not been compared. Standard affine-group action and Burnside's lemma are established tools, not claimed as discoveries. The precise conic-arrangement synthesis, sharp symmetry boundary, and polar collapse are the claimed contribution. Searches of current mathematical-record titles and claims did not identify a covering result, but absence from search results is not a proof of priority.

## Limitations
The theorem does not classify arbitrary conic arrangements or all pencil types; it concerns a fixed normalized osculating pencil. It does not claim new characteristic-zero freeness or the individual affine-group and Burnside principles. The polar-map formula is specific to maximally symmetric parameter sets and does not describe generic \(S\). No assertion about positive-characteristic freeness is made. The number of geometric points in a generic fiber can differ from the total polar degree in characteristic two. Full priority against every unindexed historical source cannot be established from available searches; in particular, the full older conic-pencil paper [2] was not inspected.

## References
[1] R. Di Gennaro, G. Ilardi, R. M. Miró-Roig, H. Schenck, J. Vallès, *Free curves, eigenschemes and pencils of curves*, arXiv:2306.09443v1 (first public posting 2023-06-15), Example 4.3, Theorem 3.6, Proposition 4.1. https://arxiv.org/abs/2306.09443

[2] A. Dimca, *Free and nearly free curves from conic pencils*, arXiv:1704.07196 (2017). https://arxiv.org/abs/1704.07196
