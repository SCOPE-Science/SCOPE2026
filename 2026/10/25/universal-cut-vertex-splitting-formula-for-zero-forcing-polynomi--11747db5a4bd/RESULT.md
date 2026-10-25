# Universal cut-vertex splitting formula for zero-forcing polynomials

## Finding

For every finite simple connected graph assembled by identifying the roots of at least two otherwise disjoint nontrivial connected graphs, the *entire* ordinary zero-forcing polynomial is determined by four rooted polynomials per branch. The formula is valid without restrictions on degrees, cycles, blocks, or branch orders.

Write \(G=H_1\vee_v\cdots\vee_v H_k\), where \(k\ge2\), each graph \(H_i\) is finite, simple, connected, has at least two vertices, and distinct branches meet precisely in the vertex \(v\), with no other cross-branch edges. Set \(U_i=V(H_i)\setminus\{v\}\). A zero-forcing set is a set of initially blue vertices from which repeated forcing by a blue vertex with exactly one white neighbor eventually makes every vertex blue. Define \(\mathcal Z(G;z)=\sum_{S\text{ zero-forcing}}z^{|S|}\).

For every \(T\subseteq U_i\), run the following deterministic closure operation **without permitting \(v\) to force**: repeatedly color the unique white neighbor of an eligible *nonroot* blue vertex until no such move remains. Eligibility always counts all white neighbors, including \(v\) if white. Order of eligible moves does not affect the terminal blue set (proved below).

Let \(C_i^+(T)\) be the terminal blue set when \(v\) is initially blue. Classify \(T\) as **A** if this terminal set is all of \(V(H_i)\). Otherwise classify it as **B** if exactly one neighbor of \(v\) is white after closure and coloring that neighbor by a single force from \(v\), followed by further nonroot closure, colors all of \(V(H_i)\). All other \(T\) are **C**.

Separately let \(C_i^0(T)\) be the terminal blue set when \(v\) starts white and is held white while nonroot vertices are allowed to force only other nonroot vertices. Set \(\alpha_i(T)=1\) precisely if some nonroot blue vertex in \(C_i^0(T)\) has \(v\) as its unique white neighbor; otherwise set it to zero.

For \(X\in\{A,B\}\) define \(X_i(z)=\sum_{T:\operatorname{type}(T)=X}z^{|T|}\), and define \(\overline X_i(z)=\sum_{T:\operatorname{type}(T)=X,\;\alpha_i(T)=0}z^{|T|}\). For any two lists of polynomials, set

\[
\mathscr R((a_i),(b_i))=\prod_{i=1}^k a_i+\sum_{i=1}^k b_i\prod_{j\ne i}a_j.
\]

**Cut-vertex splitting theorem.** For all \(G\) and all \(k\) above,

\[
\boxed{\mathcal Z(G;z)=(1+z)\mathscr R((A_i),(B_i))-\mathscr R((\overline A_i),(\overline B_i)).}
\]

In particular the formula is coefficientwise a count of zero-forcing initial sets, even though its displayed expression includes subtraction.

## Assumptions and scope

All vertices are distinguished in counting subsets. Graphs are finite, simple, undirected and connected; the root is a genuine cut vertex, and \(k\) is the number of components of \(G-v\). Each branch contains its root and one component of \(G-v\). There are no restrictions on possible cycles within branches. The ordinary color-change rule is used; the root cannot perform two distinct forces because after its first force it has no remaining white neighbor. Polynomials are ordinary cardinality-generating polynomials with coefficients in \(\mathbb Z[z]\). No probabilistic or asynchronous forcing convention is assumed.

## Proof

**1. Monotonicity of nonroot closure.** Suppose an eligible blue nonroot vertex \(u\) has a unique white neighbor \(w\). Any later legal sequence not yet coloring \(w\) leaves \(u\) with the same sole white neighbor, and thus the force \(u\to w\) is still available; if \(w\) is colored along the way, the intended effect has already occurred. Inductively, any two maximal nonroot-only forcing processes from one initial blue set yield identical blue closures. The same argument applies with the root held white: all neighbors are counted when deciding eligibility, but forces into the root are suppressed. A maximal local closure may therefore be used as a canonical process state.

**2. When the root starts blue.** Fix initial blue subsets \(T_i\subseteq U_i\) and initially color \(v\). Nonroot moves are contained in their own branches. By step 1 they can all be performed before any use of \(v\). If the root never forces, precisely the branch configurations of type A complete. If it forces, it has exactly one white neighbor at that instant; this neighbor belongs to one branch \(r\), all branches other than \(r\) must be type A, and branch \(r\) must be type B (one additional root force followed by nonroot closure completes it). Conversely these local conditions construct a global forcing sequence. Thus the polynomial enumerating the nonroot initial choices is exactly \(\mathscr R((A_i),(B_i))\), and including the initially blue root contributes \(z\mathscr R((A_i),(B_i))\). The alternatives all-A and exactly-one-B are disjoint because types A and B are disjoint.

**3. When the root starts white.** First allow every nonroot-only force that does not color \(v\), in all branches. This yields each \(C_i^0(T_i)\), independently, by step 1. To ever color the root, a nonroot blue vertex must have it as its unique remaining white neighbor. Such a force exists if and only if \(\alpha_i(T_i)=1\) for at least one branch: an available root-targeting force remains available until either the root is colored or the process terminates, and all nonroot closures are order-independent. After one such force colors \(v\), every branch resumes from a blue configuration containing its initial \(T_i\) and the blue root, so by monotonicity the resulting maximal nonroot blue configuration equals \(C_i^+(T_i)\) (the closure computed with the root blue at the outset). Thereafter at most one force from \(v\) is possible. By step 2, completion is therefore equivalent to the same all-A-or-one-B condition, **and** to at least one activation indicator being one. Conversely both conditions provide a forcing sequence: first saturate nonroot moves with the root white, force the root from an activating branch, then saturate with the root blue and use the one optional root force.

The all-A-or-one-B subsets have nonroot generating polynomial \(\mathscr R((A_i),(B_i))\). Those with no available root activation have polynomial \(\mathscr R((\overline A_i),(\overline B_i))\); the nonactivation restriction factors branchwise. Their difference counts precisely the successful initially-root-white sets. Adding the initially-root-blue contribution yields the displayed formula, with no omitted cases. This proves the theorem for all finite \(k\ge2\).

**Concrete specialization.** For any integers \(k\ge2\), \(m_i\ge2\), let \(G\) be obtained from the cliques \(K_{m_i+1}\) by identifying a single common vertex. The local clique calculation gives

\[
\mathcal Z(G;z)=z^{\sum_i(m_i-1)}\left((1+z)\prod_i(z+m_i)-\prod_i m_i\right).
\]

Indeed, every successful initial set contains all but at most one nonroot vertex from each blade; at most one blade can need the root's single force; if the root starts white, some blade must already be fully selected to color it. This last identity is a consistency example of the general theorem rather than a separate novelty claim.

## Verification

The reproducible checker `verify.py` implements ordinary global zero forcing directly on the assembled graph, independent of the four-state expression, then compares coefficient dictionaries. It exhaustively tests all ordered pairs of the 43 connected rooted labeled graphs on two to four vertices (1,849 joins), and all ordered triples of five rooted graphs on two or three vertices (125 joins). Thus the test spans **1,974 assembled rooted cases**. It separately checks 23 nonuniform clique-bouquet examples against the displayed specialization. All exact comparisons pass; see `verify_output.txt`. These finite tests support but do not replace the unrestricted proof.

## Relationship to prior work

Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips, and Reinhart introduced the ordinary zero-forcing polynomial and explicitly asked in their Section 6, Question 1 for a splitting formula based on cut vertices or separating sets. Their disjoint-union identity is not a formula for connected one-point unions. Menon and Singh studied graph-operation inequalities for zero-forcing set counts, including wedges, without the unrestricted **exact** coefficient formula here. German's 2026 paper establishes path-extremal coefficientwise bounds on distance-hereditary and canonical split-decomposition classes rather than complete polynomials for arbitrary cut-vertex compositions. Published exact formulas for special graph families (such as friendship graphs, fans, and certain clique constructions) agree with examples of this identity, but none of those special cases implies the arbitrary-branch four-state expression.

The contribution is the general rooted-state splitting identity, not the already-known zero-forcing polynomial of friendship graphs or a new bound on the zero-forcing number.

## Limitations

The local polynomials are defined constructively by considering every subset of each branch, so no polynomial-time algorithm for unrestricted graphs is claimed. The theorem does not provide a splitting formula directly in terms of the *unrooted* polynomials \(\mathcal Z(H_i;z)\) alone; its four rooted state polynomials retain necessary activation information. It covers a separator of size one, not arbitrary larger separators. An exact equivalent in older or unindexed work is still a bibliographic risk, and independent mathematical assessment has not been performed.

## References

1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips and C. Reinhart, *The zero forcing polynomial of a graph*, Discrete Applied Mathematics 258 (2019), 35–48; arXiv:1801.08910, https://arxiv.org/html/1801.08910v1. See Section 6, Question 1.
2. K. Menon and A. Singh, *Exploring the influence of graph operations on zero forcing sets*, Discrete Mathematics 348 (2025), article 114516, DOI:10.1016/j.disc.2025.114516, https://doi.org/10.1016/j.disc.2025.114516.
3. S. German, *The Path-Extremal Conjecture for Zero Forcing: Distance-Hereditary Graphs and a Split-Decomposition Reduction*, arXiv:2605.10836, first public 11 May 2026, https://arxiv.org/html/2605.10836v1.
4. D. D. Row, *A technique for computing the zero forcing number of a graph with a cut-vertex*, Linear Algebra and its Applications 436 (2012), 4423–4432, DOI:10.1016/j.laa.2011.05.012 (scalar zero-forcing number, not a reviewed full-text polynomial formula).
