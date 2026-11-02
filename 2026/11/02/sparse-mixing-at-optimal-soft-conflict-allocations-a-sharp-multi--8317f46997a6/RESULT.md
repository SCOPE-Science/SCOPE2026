# Sparse mixing at optimal soft-conflict allocations: a sharp multipartite bound and a bipartite residue law

## Finding
Let \(G=K_{a_1,\ldots,a_r}\) be a complete \(r\)-partite graph with positive integer part sizes and \(r\geq2\), and let \(n\geq1\) agents have the identical unit-additive valuation \(v(S)=|S|\). Every good must be allocated, and a conflict is counted whenever an edge of \(G\) has both ends assigned to the same agent. Then **every** conflict-minimizing EF1 allocation has at most \(r-1\) *mixed bundles* (bundles containing goods from two or more parts). This upper bound is attained for every \(r\geq2\), even by every feasible EF1 allocation in a suitable instance.

More precisely, when \(r=2\), write \(G=K_{a,b}\), assume \(a+b=nq\) for a positive integer \(q\), and let \(d\) be the unique integer with \(0\leq d<q\) and \(a\equiv d\pmod q\). The exact minimum number of violations among complete EF1 allocations is
\[
\operatorname{OPT}_{\mathrm{EF1}}(K_{a,b},n)=d(q-d).
\]
If \(d=0\), every optimum is entirely unmixed; if \(d>0\), every optimum has precisely one mixed bundle, with \(d\) goods from the first part and \(q-d\) from the second. In particular, for \(G=K_{n,n}\) and \(n\) agents with \(n\geq2\), the exact optimum is zero for even \(n\) and one for odd \(n\), whereas the general \(|E(G)|/n\) guarantee is \(n\).

## Assumptions and scope
The \(a_t\) are positive integers, parts are nonempty and pairwise disjoint, and every pair of vertices from distinct parts conflicts while no within-part pair conflicts. The number \(n\) of agents is any positive integer, including \(n>|V(G)|\) (empty bundles are then allowed). All goods have identical value exactly one to every agent; the objective measures **unweighted** edges inside assigned bundles, not the value loss from those edges. A complete allocation assigns every vertex to exactly one agent. An allocation is EF1 when each agent values their own bundle at least as highly as another agent's bundle after removing at most one good. For unit valuations this is equivalent to bundle sizes differing by at most one. A mixed bundle is nonempty and meets at least two of the graph's partite sets.

## Proof
**1. Reduce EF1 to fixed column sums.** Put \(m=\sum_{t=1}^{r}a_t\), and write \(m=nq+s\), with \(0\leq s<n\). Under unit valuations, EF1 holds exactly when there are \(s\) bundles of size \(q+1\) and \(n-s\) bundles of size \(q\). Necessity follows from the EF1 comparison between the smallest and largest bundles; sufficiency follows by removing one unit good from any larger bundle. Fix any such labeling of the bundle-size vector \((s_1,\ldots,s_n)\).

Let \(x_{tj}\) be the number of part-\(t\) goods given to agent \(j\). Then \(x_{tj}\) are nonnegative integers satisfying
\[
\sum_{j=1}^n x_{tj}=a_t,\qquad \sum_{t=1}^r x_{tj}=s_j.
\]
Conversely, each such matrix is realized by allocating the labeled goods of each part in the prescribed counts. The number of violated edges is
\[
C(X)=\sum_{j=1}^{n}\sum_{1\leq t<u\leq r}x_{tj}x_{uj}
=\frac12\sum_{j=1}^{n}\left(s_j^2-\sum_{t=1}^{r}x_{tj}^2\right).
\]
Thus minimizing \(C\), at fixed quota vector, is equivalent to maximizing \(F(X)=\sum_{t,j}x_{tj}^2\).

**2. The support of any minimizer is a forest.** Construct the bipartite support graph of \(X\), with the \(r\) part nodes on one side, the \(n\) agent nodes on the other, and an edge \((t,j)\) exactly when \(x_{tj}>0\). Suppose the support has a cycle. Because the cycle is bipartite, its edges alternate in sign; let \(D\) have entries \(+1\) and \(-1\) alternately around that cycle and zero elsewhere. Both \(X+D\) and \(X-D\) are nonnegative integer matrices with unchanged row and column sums: every cycle entry was initially at least one and each node sees one positive and one negative incident change. Yet
\[
F(X+D)+F(X-D)=2F(X)+2\sum_{t,j}D_{tj}^2>2F(X).
\]
Hence one of these two feasible matrices has strictly larger \(F\), contradicting minimality of \(C\). Therefore the support graph of **every** optimum is acyclic.

Write \(n_+\) for the number of nonempty bundles. Restrict to the \(r+n_+\) non-isolated nodes. A forest on these nodes has at most \(r+n_+-1\) edges (also when \(n_+=1\)); hence
\[
\sum_{j:s_j>0}\bigl(\deg(j)-1\bigr)
=|E(\operatorname{supp}X)|-n_+\leq r-1.
\]
Each mixed bundle has support degree at least two and contributes at least one to this sum. This proves the \(r-1\) bound. If \(n_+=0\), which cannot occur because every \(a_t>0\), the conclusion would be immediate.

**3. Sharpness.** Fix \(r\geq2\). Take \(r\) parts, each of size \(r-1\), and \(n=r-1\) agents. The total \(r(r-1)\) goods force every EF1 bundle to have exactly \(r\) goods. No single part contains \(r\) goods, so every one of the \(r-1\) bundles must be mixed, regardless of its allocation. At least one EF1 allocation exists by arbitrary distribution into blocks of size \(r\), so every optimum attains the bound.

**4. Exact bipartite residue law and all equality cases.** Suppose \(a+b=nq\) and \(q\geq1\). Every EF1 bundle has exactly \(q\) goods. Since \(r=2\), any optimal allocation has at most one mixed bundle, by Step 2. If \(d=0\), one can make \(a/q\) pure first-part bundles and \(b/q\) pure second-part bundles, yielding zero violations; no optimum can contain a mixed bundle because each such bundle has at least one violated edge. If \(1\leq d<q\), an all-pure allocation is impossible, because then the first-part size would be a multiple of \(q\). Therefore each optimum has exactly one mixed bundle. If it contains \(x\) first-part goods, then \(a=kq+x\) for some integer \(k\), with \(0<x<q\), forcing \(x=d\). That bundle produces exactly \(d(q-d)\) violations, and all pure bundles produce zero. Such an allocation exists: use \(\lfloor a/q\rfloor\) pure first-part bundles, one bundle containing \(d\) first-part and \(q-d\) second-part goods, and fill the remaining bundles with second-part goods. All counts are nonnegative and sum to \(n\). This establishes the exact formula and the characterization of every optimum. For \(K_{n,n}\) with \(n\) agents, \(q=2\) and \(d\equiv n\pmod2\), giving the asserted parity law and the comparison with \(|E|/n=n\).

## Verification
Run `python3 verify.py` from the directory containing this result. The Python program independently enumerates **all feasible occupancy matrices** (not merely one allocation algorithm) for 864 combinations of positive multipartite sizes and agent counts, covering 69,276 matrices. It verifies that some optimizer has at most \(r-1\) mixed bundles, that the exact bipartite residue formula holds whenever the total number of goods is divisible by the number of agents, and that **all** bipartite optimizers have the claimed mixing pattern. It also independently checks sharpness examples for \(2\leq r\leq9\) and the odd-family specialization through \(n=49\). The proof in the preceding section, not finite checks, establishes all universally quantified statements.

## Relationship to prior work
Yoneda and Yoneda, *Fair Division with Soft Conflicts* (arXiv:2602.20929, originally submitted 2026-02-24), define the same edge-violation objective and prove that identical additive valuations permit a balanced EF1 allocation with at most \(|E|/n\) violations, without restricting the conflict graph; their Theorem 7 provides an algorithm. Their upper bound neither gives the **exact optimum** on the complete bipartite family nor implies that *every* optimal allocation has a sparse mixing support. The present theorem treats a restricted graph family and unit valuations, but identifies a sharp structural property and a residue-dependent exact minimum. For odd \(K_{n,n}\), the universal upper bound is \(n\), while the true optimum equals one.

Garijo, Márquez, and Robles, *New Results on the Robust Coloring Problem* (arXiv:2201.12650; published 2024), study monochromatic-edge minimization subject to *proper-coloring* constraints on another graph. In the soft-conflict formulation here, no conflict edge is prohibited, and **equitable bundle sizes are mandatory**; this distinct feasible set matters. General transportation-matrix and equitable graph-partition perspectives explain the proof method, and an equivalent special-case formula in unindexed graph-partition literature remains possible.

## Limitations
The theorem concerns identical positive **unit** valuations only. It does not establish analogous sparse-mixing behavior for heterogeneous additive valuations or for general conflict graphs, and does not prove a universal optimal approximation ratio. The exact residue formula assumes two nonempty graph parts and \(a+b\) divisible by \(n\). The multipartite support-forest statement applies without that divisibility assumption, but is not an exact numerical formula for more than two parts. The computational check is finite and does not constitute an infinite proof. An independent scientific review has not been performed.

## References
1. Hirotaka Yoneda and Masataka Yoneda, *Fair Division with Soft Conflicts*, arXiv:2602.20929, first version submitted February 24, 2026. https://arxiv.org/abs/2602.20929
2. Delia Garijo, Alberto Márquez, and Rafael Robles, *New Results on the Robust Coloring Problem*, arXiv:2201.12650, published in 2024. https://arxiv.org/html/2201.12650v3
