# Frontier rigidity and exact Heyting endomorphism-rank census for finite weak orders

## Finding
Let \(P_{m,h}=A_1\oplus\cdots\oplus A_h\) be the ordinal sum of \(h\ge1\) antichains, each of cardinality \(m\ge2\). Let \(H_{m,h}=\operatorname{Up}(P_{m,h})\), the finite Heyting algebra of upward-closed subsets, with implication
\[
U\to V=\{x\in P_{m,h}:\uparrow x\cap U\subseteq V\}.
\]
Let \(S(m,t)\) be a Stirling number of the second kind, and write \((m)_{\underline t}=m!/(m-t)!\). The exact image-cardinality polynomial for **all** Heyting endomorphisms is
\[
\boxed{\displaystyle
\sum_{\varphi\in\operatorname{End}(H_{m,h})} z^{|\varphi[H_{m,h}]|}
= m\sum_{k=0}^{h-2}(m!)^k z^{2+k(2^m-1)}
 +(m!)^{h-1}\sum_{t=1}^m (m)_{\underline t}S(m,t)
 z^{(h-1)(2^m-1)+2^t}.}
\]
The first sum is empty when \(h=1\). In particular,
\[
\boxed{\displaystyle |\operatorname{End}(H_{m,h})|
=m\sum_{k=0}^{h-2}(m!)^k+(m!)^{h-1}m^m.}
\]
Every exponent shown occurs; coefficients are the exact multiplicities, with coincident exponents understood to combine (the displayed families are in fact disjoint for \(m\ge2\)).

**Structural classification.** Endomorphisms correspond bijectively to maps of \(P_{m,h}\) of exactly one of the following forms. For some \(0\le k\le h-2\), the highest \(k\) source levels are bijected levelwise onto the highest \(k\) target levels, the next source level is mapped constantly to one point of the next target level, and every remaining lower source point is mapped to that same point. Alternatively, the top \(h-1\) levels are bijected levelwise to themselves and the bottom level is mapped by an arbitrary function into the bottom level. There are no other Heyting endomorphisms.

The **nonuniform extension** is an exact finite recurrence valid for \(P=A_1\oplus\cdots\oplus A_h\) with arbitrary \(a_i=|A_i|\ge1\). Denote the strict source suffix above \(A_i\) by \(P_{>i}\), put \(\mathcal U(x)=\uparrow x\), and for \(S\subseteq P\) define
\[
E(S)=\{y\in P:\mathcal U(y)=S\cup\{y\}\}.
\]
Starting with \(D_{h+1}(\varnothing)=1\), process levels \(i=h,h-1,\ldots,1\), and for each existing suffix-image set \(S\) and each nonempty \(T\subseteq E(S)\) with \(|T|\le a_i\), add
\[
D_i(S\cup T)\mathrel{+}=D_{i+1}(S)\,|T|!S(a_i,|T|).
\]
All unspecified states have count zero. For \(S\subseteq P\), set
\[
\rho(S)=1+\sum_{j=1}^h\bigl(2^{|S\cap A_j|}-1\bigr).
\]
Then the exact endomorphism image-cardinality polynomial of \(\operatorname{Up}(P)\) is
\[
\boxed{\displaystyle \sum_{S\subseteq P}D_1(S)z^{\rho(S)}.}
\]
This recurrence also covers singleton levels, for which the uniform rigidity classification need not hold.

## Assumptions and scope
The partial order on \(P\) is reflexive and antisymmetric: points in the same antichain level are incomparable unless equal, and every point of a lower level is strictly below every point of a higher level. It is **not** the reflexive-linear-preorder modal frame where points within a level are mutually accessible. A Heyting endomorphism preserves both named bounds, binary meet, binary join, and implication. The formula counts distinct algebra homomorphisms, not merely continuous/order-preserving self-maps of the underlying finite \(T_0\)-space.

For finite \(P\), every homomorphism \(\varphi:\operatorname{Up}(P)\to\operatorname{Up}(P)\) is uniquely \(\varphi(U)=f^{-1}(U)\) for a bounded (Esakia) morphism \(f:P\to P\), characterized by
\[
 f(\uparrow x)=\uparrow f(x)\qquad (x\in P).
\]
The latter condition includes order preservation. This is finite Esakia duality; only its specialization to the present posets is counted here. All assertions hold for integers \(m\ge2\), \(h\ge1\); the nonuniform recurrence holds for all \(h\ge1\), \(a_i\ge1\).

## Proof
**1. Duality and pointwise equation.** On a finite poset, the inverse-image map of a bounded morphism preserves the Heyting operations. Conversely, bounded distributive-lattice duality represents each bounded lattice endomorphism by inverse image of a unique monotone map \(f\); its inverse image preserves implication precisely when \(f\) has the bounded-morphism property. For example, if \(z\in\uparrow f(x)\setminus f(\uparrow x)\), the upsets \(U=\uparrow z\) and \(V=\uparrow z\setminus\{z\}\) witness failure of implication preservation at \(x\). Hence the displayed bounded-morphism equation is equivalent to being a Heyting homomorphism.

Write \(I_{i+1}=f(P_{>i})\). Since \(\uparrow x=\{x\}\cup P_{>i}\) for \(x\in A_i\), the bounded-morphism equation is exactly
\[
\uparrow f(x)=\{f(x)\}\cup I_{i+1}\quad(x\in A_i).
\tag{1}
\]
This equation is both necessary and sufficient at every point; it also forces monotonicity, because each upper-level image belongs to the principal upset of each lower-level image.

**2. Exact nonuniform transfer.** Suppose the images of all source levels strictly above \(A_i\) form exactly \(S\). Equation (1) says that each element of \(A_i\) can be sent precisely to a point of \(E(S)\), independently of the other elements of the same antichain. For a prescribed nonempty **exact** new image set \(T\subseteq E(S)\), there are exactly \(|T|!S(a_i,|T|)\) surjections \(A_i\twoheadrightarrow T\). Their resulting total suffix image is \(S\cup T\). The displayed recurrence therefore counts each bounded morphism exactly once by its entire image. Every image of a bounded morphism is an upset: if \(y=f(x)\), then \(\uparrow y=f(\uparrow x)\subseteq f(P)\). Moreover \(f^{-1}[\operatorname{Up}(P)]\) is isomorphic to \(\operatorname{Up}(f(P))\): all upsets of the image are also upsets of \(P\), and surjectivity onto the image distinguishes them. The number of upsets of the induced weak order on an image \(S\) is \(\rho(S)\), by its unique lowest nonempty level. This proves the complete nonuniform recurrence and its image-cardinality interpretation.

**3. Rigid uniform transitions.** Assume every target level has size \(m\ge2\). Start at the top source level. Equation (1) forces its image to lie in the maximal target level. If this image is a singleton \(\{y\}\), then \(E(\{y\})=\{y\}\), because no lower point has an upset equal to \(\{y,z\}\) with only one of the \(m\ge2\) maximal points present. Thus all lower source levels are forced to this same point. If the top-level image has between two and \(m-1\) points, then \(E(S)=\varnothing\); hence this case is impossible when lower source levels exist. The remaining possibility is the entire top target antichain, which requires a permutation of its \(m\) points. For such a complete top suffix \(S=A_h\), equation (1) forces the next source level to map into \(A_{h-1}\), with independent arbitrary choices at that level. As long as another lower source level remains, the new level image must be either a singleton (forcing all subsequent levels to that same point) or all \(m\) points (a permutation, enabling the next lower target level). A proper image of size between two and \(m-1\) again makes \(E\) empty. Induction downwards proves the claimed dichotomy; the bottom level, having no lower source levels, may use any nonempty subset of its target level. Conversely every map listed satisfies equation (1), so the classification is exact.

**4. Enumeration and image ranks.** For the first type, \(k\) upper-level permutations give \((m!)^k\) choices; the frontier singleton has \(m\) choices and all lower images are forced. Its image contains a single point on one level and the complete \(k\) higher antichains. It therefore has exactly \(2+k(2^m-1)\) upsets. For the second type, the upper \(h-1\) permutations give \((m!)^{h-1}\) choices. An arbitrary function on the bottom \(m\)-point antichain with exactly \(t\) image points has \((m)_{\underline t}S(m,t)\) possibilities. Its image poset has \(t\) bottom points and \(h-1\) complete higher levels, hence exactly \((h-1)(2^m-1)+2^t\) upsets. Summing the disjoint cases proves the rank polynomial. The identity \(\sum_{t=1}^m(m)_{\underline t}S(m,t)=m^m\) gives the total number.

## Verification
Run the attached standalone script `artifacts/verify.py` with Python 3.9 or newer (standard library only). Independent brute-force enumeration of all functions tests the bounded-morphism equation for **all 31 ordered compositions of integers from one through five**, totaling 52,165 candidate maps. It checks the nonuniform recurrence's rank profile exactly. Separately, it checks the closed uniform formula against full map enumeration for six small parameter pairs and against the independent suffix recurrence for 36 further width-height pairs. Finally, direct preservation of the entire Heyting implication table is compared to the bounded-morphism test for every map on six small posets (319 candidates), including failures. The script prints `VERIFY_OK` on success.

## Relationship to prior work
Finite Esakia duality and its p-morphism characterization are standard, as described by Bezhanishvili, Carai and Morandi (2023, Section 2). They do not enumerate these endomorphism monoids. Pouzet and Zaguia (2007) study ordinary order-preserving endomorphisms and weak-order decompositions, but preservation of Heyting implication imposes the strictly stronger condition (1). A published transfer recurrence for cardinalities of finite weak-order mapping spaces counts **all monotone maps**, not bounded morphisms, and does not imply the image-rank polynomial here. Another published weak-order retraction criterion concerns order-preserving retractions and eventual images, not arbitrary implication-preserving endomorphisms. Results for finite linear-preorder modal algebras concern a different relation with mutually accessible same-level points and do not imply the antisymmetric Heyting theorem here.

## Limitations
This classification is for uniform weak-order **posets** of width \(m\ge2\), not arbitrary posets, preorders, or all finite Heyting algebras. The nonuniform recurrence is finite but has potentially exponentially many subset states, and its arithmetic cost is not claimed polynomial in the input size. An earlier equivalent structural count under other terminology remains a bibliographic risk. Computational checks do not certify any unbounded statement independently of the proof. No independent mathematical or originality audit is claimed.

## References
1. G. Bezhanishvili, L. Carai, P. J. Morandi, *Heyting frames and Esakia duality*, arXiv:2302.07913v1, first public 2023-02-15, especially Theorem 2.2 and Lemma 2.3. https://arxiv.org/html/2302.07913v1
2. M. Pouzet, I. Zaguia, *Weak orders admitting a perpendicular linear order*, *Discrete Mathematics* 307 (2007), 97–107, DOI 10.1016/j.disc.2006.05.038. https://doi.org/10.1016/j.disc.2006.05.038
3. *Exact cardinality recurrence for mapping spaces between finite weak orders*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-cardinality-recurrence-for-mapping-spaces-between-finite-w--1cee64311a06
4. *Singleton-gap criterion for retracts and eventual images of finite weak orders*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-singleton-gap-criterion-for-retracts-and-eventual-images-of-fini--4d39f7ca58cd
