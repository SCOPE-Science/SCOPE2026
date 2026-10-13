# Ordinary zero forcing of leaf coronas via uniquely restricted matchings

## Finding

**Theorem (exact cut-matching characterization and polynomial).** Let \(G=(V,E)\) be any finite simple graph with \(n=|V|\ge1\). Construct its *leaf corona* \(W(G)=G\circ K_1\) by attaching to each \(v\in V\) a private leaf \(v'\). For a subset \(S\subseteq V(W(G))\), let \(R=\{v\in V:v\in S\}\), \(D=\{v\in V:v'\in S\}\), and \(U=V\setminus(R\cup D)\). Let \(B(D,U)\) be the bipartite graph with parts \(D\) and \(U\), retaining precisely the edges of \(G\) between these parts. Then \(S\) is an **ordinary** zero forcing set of \(W(G)\) if and only if \(B(D,U)\) has a uniquely restricted matching saturating every vertex of \(U\). (For \(U=\varnothing\), the empty matching qualifies.) Consequently the entire zero forcing polynomial is

\[
\mathcal Z(W(G);x)=\sum_{\substack{D,U\subseteq V,\ D\cap U=\varnothing\\B(D,U)\text{ has a uniquely restricted matching saturating }U}}x^{n-|U|}(1+x)^{|D|}.
\]

Here a matching is *uniquely restricted* if it is the only perfect matching on the graph induced by the endpoints it matches, equivalently if it has no alternating cycle. The formula applies without connectivity or planarity assumptions.

**Complete-graph corollary (polynomial and all inclusion-minimal sets).** For every integer \(n\ge2\), writing \(t=2x+x^2\),

\[
\mathcal Z(K_n\circ K_1;x)=t^n+n\bigl(t^{n-1}-x^{n-1}\bigr).
\]

Thus \(Z(K_n\circ K_1)=n-1\), the number of **minimum-cardinality** sets is \(n(2^{n-1}-1)\), and the **inclusion-minimal** zero forcing sets are exactly (i) the single set of all \(n\) original clique vertices, and (ii) those choosing exactly one empty root–leaf pair, exactly one initially blue vertex from every other pair, and at least one leaf among these choices. There are therefore exactly \(1+n(2^{n-1}-1)\) inclusion-minimal sets; their sizes are \(n-1\) and \(n\), and the upper zero forcing number is \(n\).

## Assumptions and scope

All graphs are finite, simple, and undirected; the forcing rule is ordinary zero forcing: a blue vertex with **exactly one** white neighbor makes that neighbor blue. A set is zero forcing if finitely many legal forces color every vertex blue. In the stated bipartite graph, isolated vertices of \(D\) are allowed. A saturated matching contains \(|U|\) edges and meets every vertex in \(U\); it need not meet every vertex of \(D\). The integer \(n\) in the clique corollary is at least two. The assertion about \(Z\) counts selected vertices, not forcing steps.

## Proof

**1. Initial private-leaf forces.** All selected private leaves \(d'\), \(d\in D\), either already have a blue original neighbor or legally force their original neighbor \(d\). These initial forces leave every original vertex outside \(U\) blue, every original vertex of \(U\) white, and the private leaves of \(U\) white. Call this normalized position the *leaf-normalized state*. Any order of these forces is valid, so it suffices to study what can force the remaining original vertices \(U\).

**2. Only selected-leaf donors can force an originally empty pair.** Consider a root \(v\notin D\). Its private leaf \(v'\) is initially white. While \(v'\) is white, \(v\) cannot legally force an original neighbor: that would leave at least two white neighbors, the leaf and the intended original neighbor. If \(v\) later forces its own leaf, all its original neighbors were already blue at that moment. Thus no root outside \(D\) can perform a force onto an original vertex of \(U\), in any forcing chronology. Roots in \(D\) have blue private leaves and may force vertices of \(U\) when uniquely exposed. Each such donor can force at most one \(U\)-vertex because after its first force all its neighbors are blue. Hence the normalized process can color all \(U\) if and only if there is an ordering \(u_1,\dots,u_k\) of \(U\) and distinct donors \(d_1,\dots,d_k\in D\), each adjacent to \(u_i\), with

\[
N_G(d_i)\cap\{u_i,u_{i+1},\ldots,u_k\}=\{u_i\}
\qquad(1\le i\le k).
\]

The necessity follows by extracting the donor forces from any successful sequence, postponing private-leaf forces, which can never enable an original-neighbor force from a nondonor. The sufficiency follows by carrying out donor forces in the displayed order and finally forcing each remaining private leaf from its now-blue root.

**3. Matching equivalence.** Given such a sequence, the edges \(d_iu_i\) form a matching saturating \(U\). Each donor \(d_i\) has no edges to \(u_j\) for \(j>i\). Any alternating cycle with respect to this matching would contain a matched donor with the earliest index on the cycle and an incident nonmatching edge to a *later* matched \(U\)-vertex, a contradiction. Thus the matching is uniquely restricted. Conversely, suppose \(M=\{d_iu_i\}\) saturates \(U\) and is uniquely restricted. Draw a dependency arrow \(u_j\longrightarrow u_i\) whenever \(d_i\) is adjacent to \(u_j\), \(j\ne i\). A directed cycle would yield an \(M\)-alternating cycle; hence this directed graph is acyclic. Choose a topological order in which every arrow's tail precedes its head. When \(u_i\) is processed, each other originally white neighbor of \(d_i\) has already been colored; hence \(d_i\) forces \(u_i\). These steps clear \(U\), proving equivalence.

**4. Polynomial.** Fix disjoint \(D,U\subseteq V\). For \(v\in U\), neither member of its pair is selected. For \(v\in D\), its private leaf is selected and its root may independently be selected or not, contributing \(x(1+x)\). For every \(v\notin D\cup U\), exactly its root is selected, contributing \(x\). Therefore the corresponding weight sum is \(x^{n-|U|}(1+x)^{|D|}\), and the matching criterion does not depend on the optional root choices. Each \(S\) determines exactly one \((D,U)\); summing gives the formula without multiplicities.

**5. Complete cliques and minimality.** When \(G=K_n\), every donor sees every empty-pair vertex. Thus if \(|U|\ge2\), no donor has exactly one neighbor in the remaining \(U\) at the outset, so forcing cannot begin. When \(U\) has one vertex, forcing succeeds precisely if \(D\ne\varnothing\). The \(U=\varnothing\) choices contribute \(t^n\). Choosing one empty pair, and from every remaining pair a nonempty selection with at least one leaf among them, contributes \(n(t^{n-1}-x^{n-1})\). The smallest nonzero degree is \(n-1\), with coefficient \(n(2^{n-1}-1)\).

A zero forcing set with a doubly selected pair is not inclusion-minimal: remove the original vertex of that pair, leaving the donor leaf and all other pair statuses unchanged. Among sets with no empty pair and exactly one selected vertex per pair, removing a selected **root** creates one empty pair. If any other pair has a selected leaf, the remainder is still zero forcing. If every selected vertex is a root, removing any vertex creates an empty pair but no donor, and this *all-originals* set is inclusion-minimal. Finally a zero forcing set with exactly one empty pair and one selection per other pair is inclusion-minimal: deletion creates a second empty pair, which cannot be forced from any donor. These and only these sets are minimal, as asserted.

## Verification

A standalone Python 3 program (`verify.py`) implements (i) a direct step-by-step ordinary zero forcing closure on the actual \(2n\)-vertex corona, independently of (ii) the donor peeling criterion and (iii) a separate weighted cut sum. It compares all blue subsets for **every** graph on at most four vertices (75 labeled edge-choice instances), plus 157 reproducibly sampled graphs on five to seven vertices, totaling **500,260** separate initial-set predicate comparisons. It separately checks clique polynomials for \(2\le n\le9\) and inclusion-minimality against one-at-a-time deletions for \(2\le n\le8\). The captured output in `verify_output.txt` ends with `VERIFY_OK`. These finite checks supplement, but do not replace, the general proof.

## Relationship to prior work

Boyer et al. introduced and systematically studied the zero forcing polynomial in arXiv:1801.08910v1 (2018); their complete-graph formula concerns \(K_n\) itself and does not give this leaf-corona enumeration. Brimkov and Carlson, *Minimal Zero Forcing Sets* (arXiv:2204.01810v2, 2022), Proposition 1, invoke mixed leaf/root selections on \(K_{n/2}\circ K_1\) to show exponentially many inclusion-minimal sets, but do not enumerate their polynomial or complete minimal-set family. In fact the stronger assertion there that every such mixed selection is inclusion-minimal is incompatible with the classification above: in \(K_4\circ K_1\), selecting \(1',2',3,4\) is zero forcing but remains zero forcing upon deleting root \(3\), because \(1'\to1\), \(2'\to2\), \(1\to3\), and then remaining private leaves can be forced. This distinguishes successful forcing from inclusion-minimal forcing. Javaid et al., arXiv:1607.04071v1 (2016), analyze scalar zero forcing for coronas whose attached graphs have at least two vertices; their relevant formula does not cover the attached singleton \(K_1\). General relationships between constrained matchings and zero forcing predate this work; the matchings themselves and the zero forcing concept are not new. The new claim is the explicit leaf-corona cut specialization with its weight enumeration and exact clique minimal profile.

## Limitations

The cut-sum is exact for every graph but may involve exponentially many disjoint \((D,U)\) pairs; **no general polynomial-time algorithm** is claimed. The matching criterion is a structural characterization, not a bound on the complexity of finding an optimum. General constrained-matching literature may contain an equivalent interpretation, and unindexed equivalent polynomial identities cannot be excluded by literature searching. No independently conducted external audit has been performed. The exhaustive checks are finite and are not a proof for arbitrary \(n\).

## References

1. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (2018), https://arxiv.org/html/1801.08910v1.
2. B. Brimkov and J. Carlson, *Minimal Zero Forcing Sets*, arXiv:2204.01810v2 (2022), especially Proposition 1, https://arxiv.org/html/2204.01810v2.
3. I. Javaid et al., *On the zero forcing number of corona and lexicographic product*, arXiv:1607.04071v1 (2016), https://arxiv.org/abs/1607.04071.
4. M. Tréfois and J.-C. Delvenne, *Zero forcing number, constrained matchings and strong structural controllability*, arXiv:1405.6222 (2014), https://arxiv.org/abs/1405.6222.
