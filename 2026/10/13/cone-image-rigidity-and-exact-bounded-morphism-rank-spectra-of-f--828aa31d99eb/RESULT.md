# Cone-image rigidity and exact bounded-morphism rank spectra of finite regular tree frames

## Finding

Let \(d\ge2\) and \(h\ge0\) be integers. Let \(T_{d,h}\) be the finite full \(d\)-ary rooted tree of height \(h\), ordered by the reflexive ancestor relation. Regard this order as an S4 Kripke accessibility relation. A **bounded endomorphism** is a self-map \(f\) preserving the order and satisfying the back condition: if \(f(x)\le y\), then \(f(x')=y\) for some descendant \(x'\ge x\). These are also finite-poset p-morphisms.

**Cone-image theorem.** The image of every bounded endomorphism is exactly one principal successor cone \(\uparrow v\), and every such cone is the image of a bounded idempotent endomorphism. The complete image-rank polynomial, including all noninjective endomorphisms, and its idempotent analogue admit explicit finite recurrences given below. In particular, no image cardinalities other than

\[
N_{d,k}=1+d+\cdots+d^k=\frac{d^{k+1}-1}{d-1},\quad 0\le k\le h,
\]

occur, and all of them occur.

Define \(R_d(H,K)\), for integers \(0\le K\le H\), to be the number of bounded morphisms from \(T_{d,H}\) onto \(T_{d,K}\) that map root to root. Put \(R_d(H,0)=1\), and \(R_d(0,K)=0\) for \(K>0\). For \(H,K\ge1\) with \(K\le H\), define

\[
A=R_d(H-1,K),\quad B=\sum_{j=1}^{K}d^jR_d(H-1,K-j),
\]

where \(R_d(a,b)=0\) when \(b>a\). Then the **exact recursion** is

\[
\boxed{R_d(H,K)=(A+B)^d-B^d+d!\,R_d(H-1,K-1)^d.}
\]

Let \(E_{d,h}(z)\) count all bounded self-endomorphisms by image cardinality. Then

\[
\boxed{E_{d,h}(z)=\sum_{k=0}^{h}d^kR_d(h,h-k)z^{N_{d,h-k}}.}
\]

For \(a\ge K\), put

\[
S_d(a,K)=\sum_{j=0}^{K}d^jR_d(a,K-j).
\]

This is the number of bounded morphisms from \(T_{d,a}\) to \(T_{d,K}\), without prescribing the source root's image. Let \(I_{d,h}(z)\) count **idempotent** bounded self-endomorphisms by their image cardinality. Then

\[
\boxed{I_{d,h}(z)=\sum_{k=0}^{h}d^k
\left(\prod_{t=1}^{k}S_d(h-t,h-k)^{d-1}\right)
 z^{N_{d,h-k}}.}
\]

An empty product is one. The full-rank coefficient in \(E_{d,h}\) is exactly the order of the iterated wreath-product automorphism group,

\[
\boxed{[z^{N_{d,h}}]E_{d,h}(z)=(d!)^{(d^h-1)/(d-1)},}
\]

whereas the corresponding coefficient in \(I_{d,h}\) is one. Both polynomials have coefficient \(d^h\) at rank one. At height two, the complete formulas simplify to

\[
\begin{aligned}
E_{d,2}(z)&=d^2z+d\big((d!+d)^d-d^d+d!\big)z^{d+1}
 +(d!)^{d+1}z^{d^2+d+1},\\
I_{d,2}(z)&=d^2z+d(d!+d)^{d-1}z^{d+1}+z^{d^2+d+1}.
\end{aligned}
\]

For the binary height-two frame, consisting of seven worlds,

\[
E_{2,2}(z)=4z+28z^3+8z^7,\qquad
I_{2,2}(z)=4z+8z^3+z^7.
\]

Hence it has exactly 40 bounded endomorphisms and 13 bounded idempotents, and its only possible endomorphism image sizes are one, three and seven.

**Finite modal-algebra corollary.** Equip the full Boolean powerset \(\mathcal P(T_{d,h})\) with the S4 diamond \(\Diamond A=\{x:\exists y\ge x,\ y\in A\}\). Every modal-algebra endomorphism is the inverse-image map of a unique bounded frame endomorphism. Its algebraic image has exactly \(2^{|f(T_{d,h})|}\) elements. Thus the modal-algebra endomorphism and idempotent image-cardinality polynomials are obtained from the two displayed frame polynomials by replacing each monomial \(z^{N_{d,k}}\) with \(z^{2^{N_{d,k}}}\). In particular the seven-world frame produces a 128-element S4 modal algebra with 40 endomorphisms and 13 idempotents, having possible endomorphism-image algebra sizes \(2,8,128\).

## Assumptions and scope

The tree has vertices the words over an alphabet of size \(d\) of lengths at most \(h\); the empty word is its root. The order is **reflexive** prefix inclusion, not the edge-only parent relation. The map is not required to fix the ambient root. Images are counted as actual subsets of this fixed labelled tree, and functions are counted individually, not modulo automorphisms. The result is about bounded morphisms/p-morphisms of this finite frame, **not** arbitrary monotone maps or automorphisms of its undirected graph. The height-zero case has one endomorphism and one idempotent.

## Proof

**Step 1: the image is a cone.** For any bounded morphism \(f\) and any \(x\), monotonicity gives \(f[\uparrow x]\subseteq\uparrow f(x)\). The back condition gives the opposite inclusion, so

\[
 f[\uparrow x]=\uparrow f(x).\tag{1}
\]

Apply (1) to the root, whose upper cone is the entire frame. Thus \(f[T_{d,h}]=\uparrow f(\varnothing)\). A vertex of depth \(k\) roots a cone isomorphic to \(T_{d,h-k}\), and there are exactly \(d^k\) such vertices.

**Step 2: root-preserving maps.** A bounded map sending the source root to the target root is automatically onto the target by (1). Fix \(H\ge K\ge1\), and inspect the \(d\) source child subtrees. For one child, its image root may be the target root (\(A\) choices for its entire restriction), or a target vertex at depth \(j\ge1\) (\(d^jR_d(H-1,K-j)\) choices); summing over positive depths gives \(B\). Whenever at least one source child is sent to the target root, that child's subtree already surjects onto the target, so every other source-child restriction may be chosen independently. This yields \((A+B)^d-B^d\) maps.

Suppose instead no source child maps to the target root. To hit a particular immediate target child \(u\), some source child must map exactly to \(u\): a deeper source descendant mapping to \(u\) would have a source child whose image is an ancestor of \(u\), and the only such vertices are the target root and \(u\). Since there are exactly \(d\) source children and \(d\) immediate target children, their images must be a permutation of those target children. The restrictions are independent bounded root-preserving maps from \(T_{d,H-1}\) onto \(T_{d,K-1}\). Their number is \(d!R_d(H-1,K-1)^d\). This proves the recurrence, including its boundary cases.

**Step 3: endomorphism ranks.** Choose the image of the ambient root to be any of \(d^k\) depth-\(k\) vertices, then identify that image cone with \(T_{d,h-k}\). The restriction of the endomorphism is precisely one of the \(R_d(h,h-k)\) root-preserving maps. This proves the polynomial \(E_{d,h}\), and also that all potential ranks occur: for each \(k\), a bounded retraction onto the corresponding cone is constructed in Step 4.

**Step 4: retracts and idempotents.** An idempotent map is the identity on its image. Fix a desired image cone rooted at vertex \(v\) of depth \(k\). Every ancestor \(x\le v\) must map to \(v\): monotonicity yields \(v=f(\varnothing)\le f(x)\le f(v)=v\). Every descendant of \(v\) is fixed. At depth \(t\) along the spine to \(v\), each of the other \(d-1\) child subtrees is independent, has source height \(h-t\), and may map boundedly into the target cone of height \(h-k\) with any root image. By Step 1, the number of such restrictions is \(S_d(h-t,h-k)\). Such choices satisfy the back condition at the spine because the fixed cone is already included in the image of every spine successor cone. Multiplying over spine levels and multiplying by the \(d^k\) possible target roots gives \(I_{d,h}\). Nonemptiness follows by choosing each off-spine map constant at a fixed target leaf; this proves that every cone is a retract.

**Step 5: algebraic dual transfer.** Any Boolean endomorphism of the finite powerset algebra is inverse image under a unique function \(f:T_{d,h}\to T_{d,h}\) (the ultrafilter preimage, or equivalently the partition of the source worlds by the images of singleton atoms). Preserving \(\Diamond\) is exactly the equality \(f[\uparrow x]=\uparrow f(x)\) at every world, by testing the diamond equation on singleton subsets. Hence modal-algebra endomorphisms and bounded frame endomorphisms correspond bijectively. The inverse-image Boolean algebra has one independent membership bit per value in \(f(T_{d,h})\), so has \(2^{|f(T_{d,h})|}\) elements. The equivalence preserves composition up to reversal and therefore preserves idempotence.

**Step 6: extremal coefficients.** The only bounded surjective self-maps of a finite set are bijections. A bijective bounded map of a rooted tree is an order automorphism. At each internal vertex its \(d\) children may be permuted independently, producing \((d!)^{1+d+\cdots+d^{h-1}}\) automorphisms. The only idempotent bijection is the identity. A rank-one bounded map must be constant at a maximal vertex, giving the \(d^h\) maps and idempotents at rank one. For height two insert the base values \(R_d(1,1)=d!\) and \(R_d(1,0)=1\) into the displayed recurrences.

## Verification

The standard-library script `CHECK.py` independently constructs all finite rooted trees of specified arities and exhaustively screens every set map for the defining **cone-image equality** (1), separately testing idempotence. Exhaustive cases are \((d,h)=(2,0),(2,1),(2,2),(3,0),(3,1),(4,1)\), comprising 826,953 raw function tables; every exact rank coefficient agrees with both recurrences. It additionally verifies all-rank, singleton-rank and automorphism formulas at four arities and four positive heights. Reproduce with `python3 CHECK.py` from the extracted package. These finite experiments are not substitutes for the general proof.

## Relationship to prior work

Goldblatt and Hodkinson [1] study the Kripke semantics and canonicality of finite-width and finite-achronal-width modal logics. The complete regular tree frames here have antichain width \(d^h\) and are concrete finite transitive, reflexive examples, but the paper's primary theorems concern canonicality, not enumeration of their bounded endomorphisms. Almeida and Bezhanishvili [2] give coalgebraic semantics for image-finite intuitionistic modal frames and explicitly formulate p-morphisms, including the order-theoretic back condition. The present calculations are a quantitative classification for a restricted finite-poset family, not a claim to have originated p-morphisms, Esakia duality, or the general tree automorphism wreath product. Literature searches did not identify an exact published counterpart of the **paired endomorphism/idempotent image-rank recurrences**; absence from searchable results does not establish priority.

## Limitations

Only uniform finite branching with \(d\ge2\) and fixed finite height is included. The results do not enumerate conjugacy classes, arbitrary modal accessibility relations, or homomorphisms of trees with unrelated branching profiles. The originality status is provisional in the presence of possible unindexed bounded-morphism enumeration results. No independent mathematical audit has been performed.

## References

[1] R. Goldblatt and I. Hodkinson, *Canonicity in power and modal logics of finite achronal width*, arXiv:2207.12596v1 (26 July 2022), The Review of Symbolic Logic 17 (2024), 705–735. DOI: 10.1017/S1755020323000060. Primary MSC2020: 03B45.

[2] R. Nicolau Almeida and N. Bezhanishvili, *A Coalgebraic Semantics for Intuitionistic Modal Logic*, arXiv:2406.10649v1 (15 June 2024), Sections 2–5. Especially Definition 2.2 and Theorems 4.3 and 4.5.

[3] G. Bezhanishvili, N. Bezhanishvili, T. Moraschini and M. Stronkowski, *Profiniteness and representability of spectra of Heyting algebras*, arXiv:2103.02530v1 (3 March 2021), Advances in Mathematics 391 (2021), 107959. Finite Esakia duality discussed in Section 2.
