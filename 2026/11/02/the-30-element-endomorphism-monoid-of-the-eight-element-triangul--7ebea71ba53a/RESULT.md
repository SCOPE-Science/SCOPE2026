# The 30-element endomorphism monoid of the eight-element triangular Boolean semiring

## Finding
Let \(\mathbb B=\{0,1\}\) with disjunction and conjunction as its semiring operations, and let \(T_2\) be the eight-element semiring of upper triangular \(2\times2\) matrices over \(\mathbb B\). **Homomorphisms preserve the two binary operations only; constants \(0\) and \(1\) are not named in this signature.**

The monoid \(\operatorname{End}_{(+ ,\cdot)}(T_2)\) has exactly \(30\) members. Of these, exactly \(21\) are retractions (idempotents under composition). The image-size multiplicities, with image size interpreted as the cardinality of the image of a self-map, are

\[
\begin{array}{c|rrrr}
\text{image size}&1&2&4&8\\\hline
\#\text{endomorphisms}&7&20&2&1\\
\#\text{retractions}&7&12&1&1
\end{array}
\]

The automorphism group is trivial. The local group at the diagonal projection has order two and consists of that projection and diagonal interchange; every other maximal subgroup of the endomorphism monoid is trivial. Equivalently, there is exactly one nontrivial maximal subgroup, isomorphic to \(C_2\).

## Assumptions and scope
Write elements as triples \((a,b,c)\in\{0,1\}^3\), representing matrices \(\left(\begin{smallmatrix}a&b\\0&c\end{smallmatrix}\right)\). Addition is componentwise Boolean OR; multiplication is
\[
(a,b,c)(d,e,f)=(ad,\,ae\vee bf,\,cf).
\]
Use \(e=(1,0,0)\), \(z=(0,1,0)\), \(f=(0,0,1)\). The shorthand \(0,1,2,\ldots,7\) denotes the bit masks \(a+2b+4c\), not integers with their usual arithmetic. In particular, \(1=e\), \(2=z\), \(4=f\) and \(7=e+z+f\). The zero matrix is \(0\); the multiplicative identity matrix has mask \(5\), and neither is part of the signature as a specified constant.

## Proof
**1. Reduction to four images.** The additive semilattice is the free three-generator Boolean join-semilattice with a bottom element when its bottom is allowed to move. A join-preserving self-map \(\phi\) is determined by
\[
T=\phi(0),\quad P=\phi(e),\quad Q=\phi(z),\quad R=\phi(f),
\]
with \(T\vee P=P\), \(T\vee Q=Q\), \(T\vee R=R\). For any element \(x\), \(\phi(x)\) is the join of the assigned generator images whose source coordinates occur in \(x\), and equals \(T\) when \(x=0\).

The multiplication relations are \(e^2=e\), \(f^2=f\), \(z^2=0\), \(ez=zf=z\), and \(ze=fz=ef=fe=0\). Together with products involving zero, these are sufficient because multiplication distributes over joins. They give
\[
T^2=T,\quad P^2=P,\quad R^2=R,\quad Q^2=T,
\]
\[
PQ=QR=Q,\qquad QP=RQ=PR=RP=T,
\]
and \(TX=XT=T\) for \(X\in\{P,Q,R\}\). All equations are evaluated by the explicit Boolean triple multiplication above; no assumption that a homomorphism fixes zero or one is made.

**2. Exhaustive structural solution of the finite equations.** The multiplicative idempotents in \(T_2\) are exactly the masks \(0,1,3,4,5,6,7\). Substituting their triples into the equations yields precisely the following disjoint list (tuples are \((T,P,Q,R)\)):

* When \(T=Q=0\), all \(15\) tuples \((0,P,0,R)\) with \(P,R\) idempotent and \(PR=RP=0\) occur. Thirteen have \(P=0\) or \(R=0\), and the remaining two are \((0,1,0,4)\) and \((0,4,0,1)\).
* When \(T=0\) and \(Q\ne0\), the unique solution is \((0,1,2,4)\).
* When \(T\ne0\), necessarily \(Q=T\). There are the six constant maps \((T,T,T,T)\) for \(T\in\{1,3,4,5,6,7\}\), and eight additional solutions \((T,T,T,U)\) and \((T,U,T,T)\) for the four strict pairs \((T,U)\in\{(1,5),(3,7),(4,5),(6,7)\}\).

For completeness, the short finite-table steps are reproducible without any classification theorem: \((a,b,c)^2=(a,\,b(a\vee c),\,c)\), so the sole non-idempotent is the mask \(2\). Evaluation of \(Q^2=T\) and \(PQ=QR=Q\) against the seven idempotents gives the two branches \((T,Q)=(0,0)\), \((0,2)\), or \((T,T)\) with \(T\ne0\); testing the eight possible values of each remaining coordinate yields exactly the displayed pairs. The included verifier executes this same exhaustive finite-table step independently, starting from **all** \(8^4\) possible assignments, then checks all operation pairs rather than assuming the case list.

Hence the complete number is \(15+1+6+8=30\).

**3. Image sizes and retractions.** Among the listed maps, the seven constant maps (including the zero map) have image size one; the twelve remaining \(T=Q=0\) maps with one of \(P,R\) zero and the eight nonconstant \(T\ne0\) maps have image size two. The two orthogonal nonzero-idempotent pairs \((P,R)=(1,4),(4,1)\) have image size four and the remaining identity map has image size eight. Direct substitution into \(\phi^2=\phi\) within the four-image list gives, in increasing order of image size, \(7,12,1,1\) retractions, hence \(21\) overall. Each step can also be checked by an explicit eight-point map-composition table and is fully repeated in `verify.py`.

**4. Maximal subgroups.** The only bijective endomorphism is the identity, so \(\operatorname{Aut}(T_2)\) is trivial. Define \(\pi(a,b,c)=(a,0,c)\) and \(\tau(a,b,c)=(c,0,a)\). Both are endomorphisms and \(\pi^2=\pi\), \(\tau^2=\pi\), \(\pi\tau=\tau\pi=\tau\); they form a group of order two with identity \(\pi\) in the transformation monoid. Each maximal subgroup at an idempotent endomorphism \(r\) identifies with a subgroup of the automorphism group of its image algebra \(r(T_2)\); indeed, a two-sided local inverse must restrict to an automorphism of this image. The rank-one images are singletons; rank-two images are two-element join-semilattices and have no nontrivial addition-preserving bijections; and the rank-eight image has only the identity automorphism. The sole rank-four idempotent is \(\pi\), whose two-element-coordinate diagonal algebra admits precisely the identity and the swap. This proves the assertion for every maximal subgroup.

## Verification
`verify.py` is a standalone Python standard-library checker. Run `python verify.py` in the directory containing that file; its final output begins with `VERIFY_OK`. It independently enumerates all join-preserving maps using the four images and tests addition and multiplication on all \(64\) ordered pairs each; builds the structural classification as a separate set; computes all image ranks, all \(30\times30\) compositions, the \(21\) retractions, and each local group. It also reproduces the five kernel partitions known from congruence theory. The verifier is finite exhaustive corroboration; the displayed four-image reduction and structural-case proof establish why enumeration covers *every* self-homomorphism.

## Relationship to prior work
Jiao and Shao [1] identify the eight-element \(T_2\), study its identity basis, and in Theorem 10.1/Corollary 10.2 give its five congruences. Their result *already entails* that endomorphism image sizes can only be \(1,2,4,8\), by the first isomorphism theorem. The new content here is **the number and explicit form of all self-homomorphisms**, the exact retraction counts, and the unique nontrivial maximal subgroup; the rank possibilities by themselves are **not new**. Their full manuscript has been withdrawn as incomplete, so no unproved global finite-basis statement is needed as a premise for our elementary computation. Volkov [2] analyzes identities of upper triangular Boolean matrix semirings; our self-map census concerns a different invariant.

## Limitations
The classification applies to the eight-element two-by-two Boolean triangular semiring in the binary-operation-only signature. If preservation of a *named* zero or identity is additionally required, the census changes. It does not classify higher-dimensional triangular semirings or semirings over larger lattices. Historic priority is provisional: older unindexed work may have counted the same endomorphism monoid. The proof is finite exact; no claim of independently audited correctness is made.

## References
1. J. Jiao and X. Shao, *The finite basis problem for \(2\times2\) triangular Boolean matrix semirings and incidence semirings*, arXiv:2609.32356v3 (first publicly posted September 26, 2026), especially Section 10, Theorem 10.1 and Corollary 10.2. https://arxiv.org/abs/2609.32356
2. M. V. Volkov, *Identities of triangular Boolean matrices*, arXiv:2412.16113v4 (2025). https://arxiv.org/abs/2412.16113
