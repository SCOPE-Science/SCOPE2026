# Complete idempotent rank enumeration for double-star Margolis–Rhodes monoids

## Finding
For integers \(a,b\geq1\), let \(D_{a,b}\) be the tree consisting of adjacent hubs \(u,v\), with \(a\) leaves adjacent to \(u\) and \(b\) leaves adjacent to \(v\). Let \(\operatorname{MR}(D_{a,b})\) be its monoid of partially defined maps whose inverse image of each singleton vertex or edge is empty or a vertex or an edge. Put \(E_{a,b}(t)=\sum_{f^2=f}t^{|\operatorname{im}f|}\), summing over all idempotents of this monoid (including the empty map). Define \(F_s(t)=(1+t)^s\) and \(H_s(t)=(1+t)^s+st(1+t)^{s-1}\). Then

\[
E_{a,b}(t)=H_a(t)H_b(t)+t\big[(F_a(t)+a)H_b(t)+(F_b(t)+b)H_a(t)+F_a(t)+F_b(t)\big]+t^2F_a(t)F_b(t).
\]

In particular the total number of idempotents is

\[
2^{a+b-2}(a+4)(b+4)+a2^{b-1}(b+2)+b2^{a-1}(a+2)+2^a+2^b.
\]

The formula classifies *every* idempotent by image size; for genuine double-branching trees take \(a,b\geq2\). The parameter value \(a=b=1\) recovers the 35 known idempotents of the four-vertex path.

## Assumptions and scope
A partial map \(f:V\rightharpoonup V\) is called graph-continuous when, for every target simplex \(\sigma\) (a singleton or a two-vertex edge), its full preimage \(f^{-1}(\sigma)\) is empty or a simplex in the source graph. The empty partial map is admitted. Composition is the ordinary partial-map composition. The rank of an idempotent is the cardinality of its image. All graphs are finite and loop-free. The result concerns \(\operatorname{MR}(D_{a,b})\), **not** the strict submonoid whose nonempty entire inverse image is required to be an edge.

## Proof
**Idempotent fiber lemma (any finite simple graph).** An idempotent continuous partial map is exactly the following datum: a set \(F\subseteq V\) of fixed vertices, together with a partial injective assignment from some vertices \(y\notin F\) to targets \(x\in F\), subject to (i) every assigned \(y\) is adjacent to its target \(x\); (ii) each target receiving such an assignment is isolated in the induced graph on \(F\). Every vertex not fixed or assigned is undefined. The image equals \(F\).

Indeed, \(f^2=f\) forces every image vertex to be fixed. If a nonfixed vertex \(y\) maps to \(x\), then \(f^{-1}(\{x\})\) contains \(x,y\); hence they form an edge and no other vertex can map to \(x\). If the target \(x\) were adjacent to another fixed point \(z\), the full preimage of \(\{x,z\}\) would contain three vertices, impossible. Conversely, with (i)–(ii), each singleton inverse image is a fixed vertex or a fixed vertex joined to one assigned neighbor; for an edge between fixed vertices neither endpoint receives any assignment, so its preimage is exactly that edge. For any other edge, the preimage is at most the permitted singleton or edge. Thus the datum is equivalent to an idempotent in the monoid.

Apply the lemma and split according to which hubs belong to \(F\). For either leaf set of size \(s\), choosing exactly \(i\) fixed leaves and then choosing whether the adjacent **unfixed** hub maps to one of them or is undefined gives \((i+1)\binom{s}{i}\) choices. Summing over \(i\) yields
\[
\sum_{i=0}^s(i+1)\binom si t^i=H_s(t).
\]

**Neither hub fixed.** Each hub can map to at most one fixed leaf on its own side or be undefined, independently. Therefore the contribution is \(H_a(t)H_b(t)\).

**Only \(u\) fixed.** Select fixed subsets of its \(a\) leaves and of the \(b\) leaves attached to \(v\). If at least one \(u\)-leaf is fixed, the hub \(u\) is not isolated in \(F\), so no other vertex can map to it; the unfixed hub \(v\) has \(j+1\) choices when \(j\) of its leaves are fixed. If no \(u\)-leaf is fixed, \(u\) may additionally receive one of \(a\) unfixed \(u\)-leaves while \(v\) remains undefined or maps to a fixed \(v\)-leaf; and there is one further, mutually exclusive, option \(v\mapsto u\), which forbids any leaf mapping to \(u\). Hence the contribution is \(t[(F_a(t)+a)H_b(t)+F_b(t)]\). (The factor \(F_a+a\) adds the \(a\) extra choices exactly in the zero-fixed-\(u\)-leaf term.)

**Only \(v\) fixed.** Interchanging the sides gives \(t[(F_b(t)+b)H_a(t)+F_a(t)]\).

**Both hubs fixed.** They are adjacent fixed points, and neither is isolated in the fixed-vertex subgraph. No additional nonfixed vertex can map to a fixed point: all leaves have only their hub as neighbor. All leaves may independently be fixed or undefined. The contribution is \(t^2F_a(t)F_b(t)\).

These four disjoint and exhaustive cases give the polynomial formula. At \(t=1\), \(F_s(1)=2^s\) and \(H_s(1)=2^{s-1}(s+2)\). Substitution and algebraic collection give the total count displayed above. Every step is valid for all positive integers \(a,b\).

## Verification
The standalone `verify.py` enumerates *all* partial maps (including undefined coordinates) for \((a,b)=(1,1),(1,2),(2,2),(1,3),(2,3)\). Independently, for each map it checks the identity \(f^2=f\) and preimages of **all** vertices and edges, collects its image rank, and compares every coefficient with the closed expression. The resulting rank coefficient lists, in ascending rank order, are:

- \((1,1)\): \((1,10,17,6,1)\), total \(35\).
- \((1,2)\): \((1,13,32,25,8,1)\), total \(80\).
- \((2,2)\): \((1,16,55,66,35,10,1)\), total \(184\).
- \((1,3)\): \((1,16,50,62,39,10,1)\), total \(179\).
- \((2,3)\): \((1,19,81,134,112,52,12,1)\), total \(412\).

Run `python3 verify.py`; it ends with `VERIFY_OK`. These finite checks are corroboration, not a proof for arbitrary parameters; the unrestricted conclusion follows from the four-case argument.

## Relationship to prior work
Margolis and Rhodes, *The Margolis-Rhodes Monoid of a Graph* (arXiv:2609.39370, first public September 30, 2026), give the defining graph-continuity condition, structural results for arbitrary graphs, and explicit enumerations for paths and cycles. Their discussion of idempotent images and regular Green classes is compatible with the fiber lemma but does not supply the double-star rank polynomial above. Their earlier paper *Degree 2 Transformation Semigroups as Continuous Maps on Graphs: Foundations and Structure* (arXiv:2005.02606) develops the underlying graph-continuity framework. The four-vertex-path figure of \(35\) idempotents is already known from the 2026 paper and is only used here as a consistency check.

Known formulas for idempotents on *single* stars are not the present two-hub result: the second branching hub introduces a mutually exclusive bridge assignment, visibly producing the extra \(F_a(t)+F_b(t)\) terms. Results for the strict monoid, ordinary graph endomorphisms, or arbitrary idempotent partial transformations also do not imply the counted graph-continuous family without verifying the full inverse-simplex constraints.

## Limitations
This is a finite combinatorial classification, not a statement about all trees, all continuous maps, or the semigroup generated by idempotents. The proof counts idempotents only. An equivalent double-star consequence could exist in less accessible general transformation-semigroup literature; a 2023 follow-up on degree-two transformation semigroups was located bibliographically but its complete text was not materially checked. The result has only self-review and has not undergone independent audit.

## References
1. S. Margolis and J. Rhodes, *The Margolis-Rhodes Monoid of a Graph*, arXiv:2609.39370v1, September 30, 2026. https://arxiv.org/abs/2609.39370
2. S. W. Margolis and J. Rhodes, *Degree 2 Transformation Semigroups as Continuous Maps on Graphs: Foundations and Structure*, arXiv:2005.02606, May 2020. https://arxiv.org/abs/2005.02606
3. S. Margolis and J. Rhodes, *Degree 2 Transformation Semigroups: Complexity and Examples*, International Journal of Algebra and Computation 33 (2023), 289–316, DOI:10.1142/S0218196723500157 (bibliographic comparison only; full text not inspected).
