# Sharp vertex-deletion resilience of orthogonal-array graphs in three-variable logic

## Finding
Let \(n\ge3\), let \(2\le t\le n-1\), and let \(\mathcal A\) be any strength-two orthogonal array with \(t\) rows, \(n\) symbols, and \(n^2\) columns (index one). Construct the simple graph \(G(\mathcal A)\) whose vertices are columns, two different columns being adjacent when they agree in some row. Write \(\mathcal R\) for the countable random graph and \(\equiv_{\mathrm{FO}^3}\) for equivalence under all first-order sentences using at most three variable symbols, with equality and adjacency but without counting quantifiers, **at arbitrary quantifier depth**.

For the six integers
\[
\begin{aligned}
A&=n-2+(t-1)(t-2), &B&=(t-1)(n-t+1), &C&=(n-t)(n-t+1),\\
D&=t(t-1), &E&=t(n-t), &F&=(n-t)^2+t-2,
\end{aligned}
\]
set \(m(n,t)=\min\{A,B,C,D,E,F\}\). For every set of vertices \(S\subseteq V(G(\mathcal A))\) satisfying \(|S|\le m(n,t)-1\),
\[
G(\mathcal A)-S\equiv_{\mathrm{FO}^3}\mathcal R.
\]
This is optimal for **each** array: some set of exactly \(m(n,t)\) vertices has a deletion graph not equivalent to \(\mathcal R\), distinguished by an explicit rank-three, three-variable sentence. Thus the exact universal deletion-tolerance radius is \(m(n,t)-1\).

When \(n=q\) is a prime power, orthogonal arrays exist for all these \(t\), and the maximum guaranteed resilience, optimized over the number of coordinate rows, is
\[
\boxed{\max_{2\le t\le q-1}m(q,t)=
\begin{cases}
h(h-1),&q=2h\ (h\ge2),\\
h(h+1)-1,&q=2h+1\ (h\ge1).
\end{cases}}
\]
For even \(q=2h\), the **only** maximizing row counts are \(t=h,h+1\); for odd \(q=2h+1\), the **only** maximizing row count is \(t=h+1\). The optimal universal deletion radius is the displayed maximum minus one. The finite-field constructions attain it, and deleting one additional, suitably chosen set of vertices always fails.

## Assumptions and scope
An index-one strength-two orthogonal array is a \(t\times n^2\) matrix such that every ordered symbol pair occurs exactly once on any selected pair of distinct rows. No field coordinatization is assumed for the fixed-array formula. All deletions are induced subgraphs. Quantifiers range over surviving vertices; no vertex coloring or coordinate predicates are present. No graph is assumed transitive or Desarguesian. The optimization and existence assertion needs \(q\) a prime power, but the fixed-array statement holds for any allowed \(n,t\) admitting an orthogonal array. The range \(2\le t\le n-1\) ensures each of the four two-anchor patterns is initially realized.

## Proof
**1. Strong regularity from the array.** Two different columns agree in at most one row. A fixed column has \(n-1\) neighbors in each row, in disjoint sets, hence degree \(k=t(n-1)\). If \(x,y\) are adjacent, their common-neighbor count is
\(\lambda=n-2+(t-1)(t-2)\): the shared-coordinate class contributes \(n-2\); alternatively a common neighbor shares one of the remaining \(t-1\) rows with \(x\) and a *different* remaining row with \(y\), contributing \((t-1)(t-2)\) by strength two. Distinct ordered choices yield distinct neighbors, since each pair of columns agrees in at most one coordinate. If \(x,y\) are nonadjacent, a common neighbor must agree with \(x\) in one row and \(y\) in a different row; the array property gives \(\mu=t(t-1)\) such neighbors.

**2. Exact two-point extension table.** For distinct adjacent anchors, the numbers of third vertices satisfying respectively adjacency to both, adjacency only to the first, adjacency only to the second, and adjacency to neither are
\[
(\lambda,k-1-\lambda,k-1-\lambda,n^2-2k+\lambda)=(A,B,B,C).
\]
For nonadjacent anchors they are
\[
(\mu,k-\mu,k-\mu,n^2-2-2k+\mu)=(D,E,E,F).
\]
These counts include neither anchor. Direct substitution yields exactly the six expressions above. They are strictly positive for \(n\ge3\) and \(2\le t\le n-1\); in particular, every combination of two prescribed edge/nonedge relations is realized.

**3. Exact deletion radius and logic.** For each fixed pair of surviving anchors and prescribed adjacency pattern, deletion of \(s\) vertices can destroy at most \(s\) witnesses. Thus \(s\le m(n,t)-1\) preserves every two-anchor extension requirement simultaneously. The two-extension property also implies zero- and one-anchor requirements by choosing an auxiliary different anchor and forgetting its prescribed relation. In the arbitrary-round three-pebble game against \(\mathcal R\), Duplicator matches equality moves and, when a fresh vertex is selected, matches its prescribed adjacencies to at most two currently occupied vertices. A winning strategy therefore exists for every finite number of rounds: the deletion graph agrees with \(\mathcal R\) in all \(\mathrm{FO}^3\) sentences regardless of rank.

For sharpness, choose a pair and one of the eight extension patterns attaining \(m(n,t)\), and delete **all** of that pattern's \(m(n,t)\) witnesses. Neither anchor belongs to that set. The residual graph violates the corresponding first-order sentence of form
\[
\forall x\forall y\bigl((x\ne y\land\eta(x,y))\rightarrow
\exists z\,(z\ne x\land z\ne y\land \theta(x,z)\land\psi(y,z))\bigr),
\]
where each of \(\eta,\theta,\psi\) is either the edge relation or its negation, with \(\eta\) chosen for the anchors. This sentence has quantifier rank three, uses exactly the symbols \(x,y,z\), and holds in \(\mathcal R\). No larger guaranteed deletion radius is possible.

**4. Sharp optimization.** Let \(q=2h\). If \(t\le h\), then \(m(q,t)\le D=t(t-1)\le h(h-1)\). If \(t\ge h+1\), then \(m(q,t)\le C=(q-t)(q-t+1)\le h(h-1)\). Direct substitution into all six counts shows equality at \(t=h\) and \(t=h+1\), while strictness of these inequalities outside those two row counts proves uniqueness.

Let \(q=2h+1\). For \(t\le h\), \(m(q,t)\le D\le h(h-1)\); for \(t\ge h+2\), \(m(q,t)\le C\le h(h-1)\). At \(t=h+1\), the counts \(A=F=h(h+1)-1\), while each other count is at least \(h(h+1)\). The asserted optimum and its unique maximizing row count follow. Finally, for each prime power \(q\), the \(q^2\) vectors \((x,y)\in\mathbb F_q^2\) and any \(t\) distinct linear forms among \(x,y,x+sy\) for \(s\in\mathbb F_q^\times\) yield the required index-one array. Thus all parameter optima are genuinely attained. Among all \(q+1\) projective directions in the affine plane over \(\mathbb F_q\), each pair of different points lies in exactly one direction class. Replacing the selected \(t\) directions by their complementary \(q+1-t\) directions therefore complements the graph. The maximizing row counts split this direction set as evenly as possible: a single balanced count when \(q\) is odd, and complementary adjacent counts when \(q\) is even. This symmetry gives a structural explanation of the parity split, independently of the optimization inequalities.

## Verification
The two supplied Python programs are standalone and require only the standard library. `oa_logic_verify.py` independently constructs the arrays for prime-power orders \(3,4,5,7,8,9,11\) (including explicit extension-field arithmetic), verifies each pair of columns and all four adjacency-pattern counts for every admissible row count, constructs a destructive deletion witness, and checks the parameter optimization for integer orders \(3\) through \(299\). `oa_independent_check.py` uses a separate prime-field construction and direct triple loops for orders \(3,5,7,11\), and independently exhibits deletion failures at optimal row count for \(5,7,11\). Both embedded execution records end in `PASS`. Computations corroborate the counting and edge cases; they do not replace the proofs for arbitrary arrays, prime powers, or all quantifier depths.

Examples: at order \(5\), the optimal \(t=3\) has \(m=5\), tolerating any four vertex deletions; at order \(8\), \(t=4\) or \(5\) has \(m=12\), tolerating any eleven; at order \(9\), \(t=5\) has \(m=19\), tolerating any eighteen.

## Relationship to prior work
Cameron and Stark (2002) define the \(n\)-existential closure property and construct strongly regular examples via different affine-design constructions, emphasizing existence of witnesses rather than exact worst-case deletion tolerance of orthogonal-array column graphs. Baker, Bonato, Nowlin Brown, and Szőnyi (2008) construct existentially closed graphs from **partial affine planes** and study switching; their specified graphs are not the present full orthogonal-array column graphs. Cioabă, Koolen, and Li (2013 preprint, 2014 journal) explicitly give the same orthogonal-array strongly regular parameters, but their theorem concerns minimum vertex cuts separating nontrivial components (Brouwer's conjecture), not preserving three-variable theory of the random graph after arbitrary deletions. Byrne, Byrne, and Cioabă (2026) study the VC dimension and existential closure of strongly regular and Latin-square graphs; its abstract does not settle the deletion-tolerance optimization, but complete full-text comparison was unavailable and remains a priority risk.

The general observation that an existentially closed two-point pattern survives fewer deletions than its witness multiplicity is elementary. The contribution is the **sharp, all-arrays, all-pattern deletion classification, its exact finite-variable logical interpretation, and the attained parity-sensitive optimum over row count**. Earlier results about ordinary \(2\)-existential closure alone cannot imply the exact numerical deletion radius, but a stronger unlocated theorem on witness multiplicities or robust strongly regular graphs could potentially subsume this classification.

## Limitations
The logical equivalence is restricted to noncounting first-order logic with at most three variables in the pure graph signature. It does not imply equality of full first-order theories, counting-logic equivalence, or resilience under edge modifications. The exact formula concerns index-one strength-two orthogonal-array graphs, not every strongly regular graph with the same parameters unless the latter is separately verified. The optimal row count is over this array family, **not** over all graphs on \(q^2\) vertices. No claim of independently certified priority or independently audited mathematical correctness is made. The 2026 related paper was accessible through its abstract but not full text, leaving a documented literature-comparison risk.

## References
1. P. J. Cameron and D. Stark, “A prolific construction of strongly regular graphs with the n-e.c. property,” *Electronic Journal of Combinatorics* **9** (2002), R31; published 19 July 2002. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i1r31/pdf/
2. C. A. Baker, A. Bonato, J. M. Nowlin Brown, and T. Szőnyi, “Graphs with the n-e.c. adjacency property constructed from affine planes,” *Discrete Mathematics* **308** (2008), 901–912; available online 22 August 2007. https://doi.org/10.1016/j.disc.2007.07.029
3. S. M. Cioabă, J. H. Koolen, and W. Li, “Disconnecting strongly regular graphs,” arXiv:1311.5634 (first posted 22 November 2013), *European Journal of Combinatorics* **38** (2014), 1–11. https://arxiv.org/abs/1311.5634
4. I. Byrne, J. Byrne, and S. M. Cioabă, “The VC-dimension of strongly regular graphs,” arXiv:2609.10330 (first posted 9 September 2026). https://arxiv.org/abs/2609.10330
5. A. E. Brouwer, “Orthogonal Arrays,” online reference for array graphs and their strongly regular parameters. https://aeb.win.tue.nl/graphs/OA.html
