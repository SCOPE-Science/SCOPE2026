# The four-block difference graph of a square-zero local ring times a field

## Finding

Let \(A\) be a finite commutative local ring with nonzero maximal ideal \(\mathfrak m\), \(\mathfrak m^2=0\), residue-field order \(q=|A/\mathfrak m|\), and \(h=|\mathfrak m|\). For any finite field \(F\) of order \(s\), put \(R=A\times F\). The weak zero-divisor difference graph \(\mathcal D(R)\) has four nonempty canonical vertex blocks
\[
\begin{aligned}
\mathcal A&=\{(0,u):u\in F^\times\},&a&=s-1,\\
\mathcal B&=\{(x,0):0\ne x\in\mathfrak m\},&b&=h-1,\\
\mathcal C&=\{(x,u):0\ne x\in\mathfrak m,\ u\in F^\times\},&c&=(h-1)(s-1),\\
\mathcal E&=\{(v,0):v\in A^\times\},&d&=h(q-1).
\end{aligned}
\]
Each of \(\mathcal A,\mathcal C\) induces a clique; each of \(\mathcal B,\mathcal E\) induces an independent set. The **only** edges between distinct blocks are all edges between \(\mathcal A\)--\(\mathcal C\), \(\mathcal C\)--\(\mathcal E\), and \(\mathcal E\)--\(\mathcal B\). Thus \(\mathcal D(R)\) is a weighted blow-up of the four-vertex path, with clique/independent labels \(\mathcal A-\mathcal C-\mathcal E-\mathcal B\). There are no isolated vertices, so the conclusion is unchanged if isolated vertices are deleted in the definition of the difference graph.

The graph has
\[
|V|=h(s+q-1)-1,\quad |E|=\binom{h(s-1)}2+s(h-1)h(q-1),
\]
\[
\omega(\mathcal D(R))=\chi(\mathcal D(R))=h(s-1),\qquad
\alpha(\mathcal D(R))=h(q-1)+1.
\]
It is perfect. Its abstract graph isomorphism class determines exactly \((q,h,s)\) **within this family**: two such products have isomorphic difference graphs if and only if the triples agree. It does not determine the local ring: \(\mathbb Z/4\mathbb Z\times\mathbb F_2\) and \(\mathbb F_2[t]/(t^2)\times\mathbb F_2\) have isomorphic difference graphs, despite different characteristics.

## Assumptions and scope

All rings are commutative with identity. The maximal ideal \(\mathfrak m\ne0\) satisfies \(\mathfrak m^2=0\), but it need **not** be principal and the residue field need not embed into \(A\). The finite residue-field order \(q\) and cardinality \(h\) are at least two. The second factor is an arbitrary finite field of prime-power order \(s\ge2\). The zero-divisor graph \(\Gamma(R)\) has vertex set \(Z(R)\setminus\{0\}\) and edges \(xy=0\) for distinct vertices. The weak graph \(W\Gamma(R)\) has an edge between distinct vertices \(x,y\) if there exist **nonzero** \(r\in\operatorname{Ann}(x)\), \(t\in\operatorname{Ann}(y)\) satisfying \(rt=0\). Define \(\mathcal D(R)\) by subtracting the edges of \(\Gamma(R)\) from those of \(W\Gamma(R)\) and deleting any isolated vertices. These definitions are essential: the result does not concern the full weak graph alone or the ordinary zero-divisor graph alone.

## Proof

**Step 1: Classification of vertices.** Every element of a finite local ring is either a unit or lies in its maximal ideal. Its units number \(|A|-|\mathfrak m|=h(q-1)\); moreover \(|A|=hq\). The zero-divisors of \(A\times F\) are precisely pairs with first component in \(\mathfrak m\) or second component zero. After deleting the zero element, these yield exactly the four displayed blocks, each nonempty.

**Step 2: Exact weak adjacency.** Since \(\mathfrak m\ne0\) and \(\mathfrak m^2=0\), fix \(0\ne z\in\mathfrak m\). Each vertex in \(\mathcal A\cup\mathcal B\cup\mathcal C\) is annihilated by \((z,0)\ne0\), whose square vanishes. Each vertex of \(\mathcal E\) is annihilated by \((0,1)\ne0\), and \((z,0)(0,1)=0\). Therefore any two distinct vertices are weakly adjacent except possibly two in \(\mathcal E\). For those two, the annihilator of each is \(\{0\}\times F\), and two nonzero members of this field factor cannot multiply to zero. Hence there is **no** weak edge inside \(\mathcal E\), and every other distinct pair is weakly adjacent.

**Step 3: Subtract ordinary zero-product edges.** Multiplication in the second factor is nonzero for pairs in \(\mathcal A\cup\mathcal C\). Also, \(0\ne x\in\mathfrak m\) multiplied by any unit of \(A\) is nonzero. Consequently every pair within \(\mathcal A\) or \(\mathcal C\), and every pair across \(\mathcal A,\mathcal C\), \(\mathcal B,\mathcal E\), or \(\mathcal C,\mathcal E\), has nonzero product and is weakly adjacent. All remaining pairs either have zero product (within \(\mathcal B\), across \(\mathcal A,\mathcal B\), or across \(\mathcal A,\mathcal E\), or \(\mathcal B,\mathcal C\)) or are not weakly adjacent (within \(\mathcal E\)). This is precisely the stated four-block structure. Because the block quotient is the path \(\mathcal A-\mathcal C-\mathcal E-\mathcal B\), every vertex has a neighbor.

**Step 4: Numerical invariants.** The disjoint union of \(\mathcal A\) and \(\mathcal C\) induces \(K_{a+c}\), where \(a+c=h(s-1)\). All other edges are the complete bipartite edges \(\mathcal C\)--\(\mathcal E\) and \(\mathcal E\)--\(\mathcal B\), giving \(\binom{a+c}{2}+d(b+c)=\binom{h(s-1)}2+s(h-1)h(q-1)\) edges. A clique has at most \(a+c\) vertices because any clique meeting \(\mathcal E\) has at most \(c+1\) vertices, and \(a\ge1\). Color the vertices of \(\mathcal A\cup\mathcal C\) with distinct \(a+c\) colors. Give every vertex of \(\mathcal E\) one color already used on \(\mathcal A\), and every vertex of \(\mathcal B\) one color already used on \(\mathcal C\). These are proper choices since \(\mathcal E\) is not adjacent to \(\mathcal A\), \(\mathcal B\) is not adjacent to \(\mathcal C\), and the two reused colors differ. Hence \(\chi=\omega=a+c\). An independent set may contain vertices from \(\mathcal E\) or from \(\mathcal B\), not both; if it meets \(\mathcal E\), it can add at most one vertex of \(\mathcal A\) and none of \(\mathcal C\). If it meets \(\mathcal B\), it can add at most one vertex of the clique \(\mathcal A\cup\mathcal C\). As \(d=h(q-1)\ge h>b=h-1\), the sharp maximum is \(d+1\), attained by \(\mathcal E\) and one vertex of \(\mathcal A\). Finally, \(P_4\) and both complete and edgeless graphs are perfect, and perfection is preserved under graph substitution; applying this to its four blocks proves perfectness for every induced subgraph.

**Step 5: Intrinsic reconstruction.** Two vertices in any block have the same adjacency to all vertices outside the pair; within each clique block they are true twins and within each independent block they are false twins. No pair of vertices from distinct blocks is twin: the quotient graph is the twin-free path \(P_4\), all its blocks are nonempty, and every pair of distinct quotient vertices is distinguished by a third quotient vertex. Therefore the four blocks are exactly the maximal graph-theoretic twin classes. An isomorphism induces an automorphism of this \(P_4\) quotient. Its only nontrivial automorphism reverses the path, interchanging \(\mathcal C\) with \(\mathcal E\). This cannot be induced by a graph isomorphism, because \(\mathcal C\) is an internal clique, whereas \(\mathcal E\) is an independent set of size \(d\ge2\): if \(c>1\), internal adjacency contradicts reversal; if \(c=1\), sizes contradict it. Thus all four blocks are graph-intrinsically labeled, yielding \(s=a+1\), \(h=b+1\), \(q=d/h+1\). Conversely identical triples produce identical block sizes and hence isomorphic graphs.

**Step 6: Non-rigidity of the ring.** The two local rings \(A_1=\mathbb Z/4\mathbb Z\) and \(A_2=\mathbb F_2[t]/(t^2)\) both satisfy the hypotheses with \(q=h=2\). They are not isomorphic, because their characteristics are \(4\) and \(2\). Their products with \(\mathbb F_2\) have the same triple \((q,h,s)=(2,2,2)\), hence isomorphic five-vertex difference graphs: a four-cycle with one pendant edge.

## Verification

The standalone dependency-free Python program `verify.py` constructs actual multiplication tables for \(\mathbb Z/p^2\mathbb Z\), \(\mathbb F_p[t]/(t^2)\), and \(\mathbb F_p\oplus V\) with \(V^2=0\). For eleven small choices, it exhaustively enumerates every vertex, every nonzero annihilator witness pair, and every weak/ordinary/difference edge. It separately checks block cardinalities, all predicted adjacencies, the edge formula, an explicit proper coloring, an independent set, and precise twin equivalence; its terminal success line is `VERIFY_OK 11 rings`. Execute `python3 verify.py`. This finite enumeration checks examples only; the universally quantified theorem follows from Steps 1--6.

## Relationship to prior work

Nikmehr, Azadi and Nikandish (2021) defined weakly zero-divisor adjacency using annihilator witnesses. Shylla, Mawiong and Kharbhih (2026) study the full weak graph, not the edge difference. Wani (arXiv:2607.17677, first public July 20, 2026) defines the difference graph and establishes its support-class structural theory and ring reconstruction for *reduced* products of fields. Its concluding Section 9 explicitly isolates the additional annihilator states in nonreduced finite chain rings and mentions length-two cases as tractable, without classifying them. The present theorem treats the natural **nonreduced** two-factor family with arbitrary square-zero local first factor (including non-chain rings), obtaining a four-block graph and an exact parameter-reconstruction/non-rigidity dichotomy. It does not imply or contradict Wani's reconstruction theorem, whose reduced-ring hypothesis is essential.

## Limitations

The theorem assumes precisely one finite field factor and one nonfield local factor with square-zero maximal ideal. It does not classify arbitrary products of more factors or maximal ideals with nonzero square. Reconstruction is only within the stated family; it cannot identify the characteristic or the isomorphism type of the local factor. The finite program samples prime residue and second-factor fields, while the proof also covers all prime powers. Possible unindexed equivalent nonreduced-case literature remains an originality risk; no independent mathematical audit is represented.

## References

1. B. A. Wani, *The Weak Zero-Divisor Difference Graph of a Finite Commutative Ring*, arXiv:2607.17677, first public July 20, 2026; especially Definition 1.1, Sections 3, 8--9. https://arxiv.org/abs/2607.17677
2. M. J. Nikmehr, A. Azadi, R. Nikandish, *The weakly zero-divisor graph of a commutative ring*, Revista de la Unión Matemática Argentina **62** (2021), 105--116, doi:10.33044/revuma.1677.
3. H. Shylla, S. M. Mawiong, J. P. J. Kharbhih, *Laplacian Spectrum of the Weakly Zero-Divisor Graph of a Finite Commutative Ring*, arXiv:2605.24640 (2026).
4. L. Lovász, *Normal hypergraphs and the perfect graph conjecture*, Discrete Math. **2** (1972), 253--267 (perfect-graph substitution principle).
