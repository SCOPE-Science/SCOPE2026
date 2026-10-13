# Closed lazy walks classify endomorphisms and image ranks of crown Heyting algebras

## Finding
For every integer \(m\ge 3\), let \(P_m\) be the crown poset with minimal points \(a_i\) and maximal points \(b_i\), indexed by \(i\in\mathbb Z/m\mathbb Z\), and precisely the order relations \(a_i<b_{i-1}\) and \(a_i<b_i\). Let \(H_m=\operatorname{Up}(P_m)\) be the finite Heyting algebra of upper sets, with the usual intersection, union, bottom, top and Heyting implication.

**Theorem (complete endomorphism and image-rank census).** There is a bijection between Heyting endomorphisms of \(H_m\) and closed length-\(m\) lazy walks on the cycle \(C_m\) with a chosen starting vertex. Under this bijection, the number of endomorphisms is
\[
|\operatorname{End}(H_m)|=m\biggl(2+\sum_{j=0}^{\lfloor m/2\rfloor}\frac{m!}{j!j!(m-2j)!}\biggr).
\]
Write \(F_0=0,F_1=1\) for Fibonacci numbers and \(L_0=2,L_1=1\) for Lucas numbers, each satisfying \(s_{t+2}=s_{t+1}+s_t\). The **complete set of possible image cardinalities** of these Heyting endomorphisms is
\[
\boxed{\{F_{2k+3}:0\le k\le\lfloor m/2\rfloor\}\ \cup\ \{L_{2m}\}.}
\]
In fact their multiplicities are explicit. For \(k\ge0\), let \(A_k\) be the \((k+1)\)-square matrix with a \(1\) on its diagonal and on both adjacent diagonals, and put \(B_{m,k}=\operatorname{tr}(A_k^m)\), with \(B_{m,-1}=B_{m,-2}=0\). For \(1\le k\le\lfloor m/2\rfloor\), exactly
\[
\boxed{m(B_{m,k}-2B_{m,k-1}+B_{m,k-2})}
\]
endomorphisms have image cardinality \(F_{2k+3}\). Exactly \(m\) have image cardinality \(F_3=2\), and exactly \(2m\) have image cardinality \(L_{2m}\). The latter \(2m\) endomorphisms are precisely the automorphisms.

For instance, the \(84\) endomorphisms of \(H_4\) split by image cardinality as \(2:4\), \(5:56\), \(13:16\), and \(47:8\). In particular, the image-rank spectrum is far smaller than the range of possible integer ranks in a generic finite algebra.

## Assumptions and scope
All algebra and poset structures are finite. The use of \(m\ge3\) ensures that any two different maximal points of \(P_m\) have at most one common lower point; the degenerate four-point crown is excluded. Every endomorphism preserves all operations \((\wedge,\vee,\to,0,1)\) of the Heyting algebra. Its image cardinality means the number of distinct elements in the homomorphic image subalgebra, not the cardinality of the image of the dual poset map. Every occurrence of a walk step \(-1\), \(0\), or \(+1\) is understood modulo \(m\).

Under finite Esakia duality, a Heyting homomorphism \(h:\operatorname{Up}(P_m)\to\operatorname{Up}(P_m)\) is uniquely of the form \(h(U)=f^{-1}(U)\), where \(f:P_m\to P_m\) is order preserving and satisfies the bounded-morphism condition \(f(\uparrow x)=\uparrow f(x)\) for every \(x\in P_m\). We use this standard duality as an established theorem; the new enumeration concerns the particular crown family.

## Proof
**1. Classification of bounded morphisms.** Every maximal point \(b_i\) must map to a maximal point, since \(f(\uparrow b_i)=\{f(b_i)\}=\uparrow f(b_i)\). Write \(f(b_i)=b_{u_i}\), where \(u_i\in\mathbb Z/m\mathbb Z\). For a minimal point \(a_i\), boundedness gives
\[
\uparrow f(a_i)=f(\uparrow a_i)=\{f(a_i),b_{u_{i-1}},b_{u_i}\}.
\]
If \(u_{i-1}=u_i\), its unique solution is \(f(a_i)=b_{u_i}\). Otherwise, the two distinct maximal images must be adjacent in the cyclic crown. More precisely, they must differ by \(+1\) or \(-1\) modulo \(m\); their unique common lower point must be the value \(f(a_i)\). Conversely, every such adjacent-or-equal pair has exactly one admissible value of \(f(a_i)\). Therefore a bounded morphism is uniquely equivalent to a cyclic word \((u_0,\ldots,u_{m-1})\) in which neighboring values differ by \(-1\), \(0\), or \(+1\). Choosing \(u_0\) and the \(m\) successive increments, including the closing increment, establishes the claimed bijection with based closed lazy walks.

**2. Total count and winding.** Each increment lies in \(\{-1,0,1\}\). Since their sum is divisible by \(m\) and lies in \([-m,m]\), it equals \(-m\), \(0\), or \(m\). The two nonzero cases each require all increments to have the same nonzero sign; each yields \(m\) maps. The zero-sum increment words have equally many \(+1\) and \(-1\) entries, say \(j\) of each, with \(m-2j\) zeros. Their number is \(\sum_j m!/(j!j!(m-2j)!)\). Multiplying by \(m\) starting labels and adding the \(2m\) nonzero-winding maps proves the total formula.

**3. Images of zero-winding maps.** Lift a zero-winding cyclic walk to a closed integer walk. Its traversed edges form a connected proper arc of the target cycle, since a closed walk visiting all \(m\) cycle edges would use at least \(2m\) edge steps if its total winding were zero, whereas only \(m\) steps are available. Let this arc have \(k\) edges. If \(k>0\), traversing each edge in both directions requires at least \(2k\) steps, so \(1\le k\le\lfloor m/2\rfloor\). Its \(k+1\) maximal target points all occur among images of maximal source points. Each traversed edge has some adjacent source top labels at its two ends and hence contributes the unique lower target point to the dual-map image. Conversely no other lower point can occur. Thus the poset image \(f(P_m)\), with induced order, is exactly a path-shaped crown fragment with \(k+1\) maxima and \(k\) minima. When \(k=0\), it consists of one maximal point. Every \(k\) in this interval is realized by traversing an arc forward and backward and inserting zero steps.

**4. Heyting-image sizes.** For any finite poset \(P\), any map \(f:P\to P\), and any upper sets \(U,V\), one has \(f^{-1}(U)=f^{-1}(V)\) precisely when \(U\cap f(P)=V\cap f(P)\). Every upper set of the induced subposet \(f(P)\) is the restriction of an upper set of \(P\) (take upward closure in \(P\)). Consequently the set-theoretic image of the inverse-image homomorphism has cardinality \(|\operatorname{Up}(f(P))|\).

The number of upper sets of the path fragment with \(k\) lower and \(k+1\) upper points is \(F_{2k+3}\). One direct derivation identifies upper sets with antichains, which here are independent vertex sets in the underlying path on \(2k+1\) vertices; the independent-set recurrence \(I_s=I_{s-1}+I_{s-2}\), initialized at \(I_0=1,I_1=2\), gives \(F_{2k+3}\). For nonzero winding, all increments have sign \(+1\) or \(-1\) and the dual map is a crown automorphism, so its image has cardinality \(|H_m|\). By the same antichain/independent-set bijection, \(|H_m|\) is the number of independent sets in an even cycle of length \(2m\), namely \(L_{2m}\). This gives the entire image spectrum.

**5. Exact multiplicities.** Fix an oriented target arc of \(k\) edges, where \(1\le k\le\lfloor m/2\rfloor\). There are exactly \(m\) possible such arcs. A zero-winding walk whose traversed arc is exactly this one is a closed length-\(m\) lazy walk on the reflexive path \(\{0,\ldots,k\}\) which visits both end vertices. The trace \(B_{m,k}\) counts all closed walks on this path. Inclusion-exclusion removes walks missing either endpoint, leaving \(B_{m,k}-2B_{m,k-1}+B_{m,k-2}\); the convention that negative-index traces vanish handles \(k=1\). Such a walk uniquely identifies its traversed target arc. Multiply by \(m\) arcs. The case \(k=0\) consists of \(m\) constant maximal-label walks. Finally there are \(2m\) automorphisms of winding \(\pm1\). Distinct values of \(k\) produce strictly increasing Fibonacci numbers, and \(L_{2m}\) exceeds the largest path count, completing the exact multiplicity classification.

## Verification
Run `python3 verify.py` using the Python standard library. The script exhaustively enumerates all functions on the six-point crown, independently checks order preservation and the bounded-morphism condition, and confirms that the \(27\) admissible maps exactly match the lazy-walk construction. For \(m=3,4,5,6,7\), it exhaustively enumerates all admissible top-label tuples and checks the complete endomorphism and image-cardinality census, including the closed-walk matrix multiplicities. For \(m=3,4\), it additionally checks the Heyting implication equation directly on all pairs of upper sets. Its output ends in `VERIFY_OK`. These finite computations corroborate, but do not prove, the uniform statement for arbitrary \(m\).

## Relationship to prior work
Grilletti and Quadrellaro (2023) characterize the finite Esakia spaces dual to regular Heyting algebras and supply the duality framework; crown frames with \(m\ge3\) meet their finite regularity criterion. Hyttinen, Martins, Moraschini, and Quadrellaro (preprints 2023; published later) study finite-generation phenomena in Heyting-algebra varieties under primary MSC \(03C05\). These works motivate precise structural invariants of finite Heyting algebras but do not present the closed-lazy-walk endomorphism spectrum described here.

Classical studies by Currie and Visentin and by Farley enumerate **order-preserving** maps on fences and crowns, whereas Heyting endomorphisms are dual to the strictly more constrained bounded morphisms. Contemporary classifications of finite-space homotopy classes of crown maps likewise work with all order-preserving maps and answer a different question. The independent-set/Fibonacci/Lucas counts for path and cycle posets and the central-trinomial identity are standard combinatorial ingredients, not individually claimed as new. The specific synthesis, including exact Heyting endomorphism image ranks and their multiplicities, is the proposed contribution.

## Limitations
The theorem is restricted to ordinary finite Heyting endomorphisms of cyclic crown posets with \(m\ge3\). It does not classify the full endomorphism monoid multiplication, maps between different crowns, or the degenerate case \(m=2\). Historical literature on counting constrained crown maps could conceivably contain an equivalent bounded-morphism census; the older order-preserving-map papers were identified bibliographically, but their complete texts were not available in this comparison. The rank-spectrum theorem was compared at the statement/implication level against accessible relevant treatments, not certified independently. Verification is finite; the unrestricted theorem is supported by the symbolic argument above.

## References
1. G. Grilletti and D. E. Quadrellaro, *Esakia duals of regular Heyting algebras*, arXiv:2303.11246v1 (first posted 2023-03-20), DOI:10.1007/s00012-023-00833-5.
2. T. Hyttinen, M. Martins, T. Moraschini, and D. E. Quadrellaro, *Strictly n-finite varieties of Heyting algebras*, precursors arXiv:2306.15997 (2023-06-28) and arXiv:2306.12250 (2023-06-21), DOI:10.1017/jsl.2024.48.
3. J. D. Farley, *The number of order-preserving maps between fences and crowns*, Order 12 (1995), DOI:10.1007/BF01108588.
4. J. D. Currie and T. I. Visentin, *The number of order-preserving maps of fences and crowns*, Order 8 (1992), DOI:10.1007/BF00383399.
