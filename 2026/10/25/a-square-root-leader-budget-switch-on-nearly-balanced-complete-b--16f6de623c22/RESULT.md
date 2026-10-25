# A square-root leader-budget switch on nearly balanced complete bipartite networks

## Finding

Let \(m\ge2\) be an integer and let \(G=K_{m,m+1}\) be the unweighted simple complete bipartite graph, whose parts are \(A\) (size \(m\)) and \(B\) (size \(m+1\)). For every integer leader budget \(1\le k\le2m\), choose exactly \(k\) distinct noise-free leaders \(S\), with followers \(F=V(G)\setminus S\). Define the unnormalized coherence cost \(J(S)=\operatorname{tr}(L_{FF}^{-1})\), where \(L_{FF}\) is the principal follower block of the *original*, unit-weight graph Laplacian. Then **all** minimizing sets have the following description:

* If \(1\le k\le m\) and \(k^2<2m+1\), all \(k\) leaders lie in \(A\); the minimum is \(J_A=(k+1)(2m+1-k)/[k(m+1)]\), with exactly \(\binom mk\) optimal sets.
* If \(1\le k\le m\) and \(k^2>2m+1\), all \(k\) leaders lie in \(B\); the minimum is \(J_B=J_A-(k^2-2m-1)/[km(m+1)]\), with exactly \(\binom{m+1}k\) optimal sets.
* If \(1\le k\le m\) and \(k^2=2m+1\), exactly the two preceding pure-part classes (and no mixed class) are optimal; their equal minimum is \(J_A=J_B\), and their total count is \(\binom mk+\binom{m+1}k\). Such a tie occurs precisely when \(k\ge3\) is odd and \(m=(k^2-1)/2\).
* If \(m+1\le k\le2m\), every minimizing set contains all of \(B\) and any \(k-m-1\) vertices of \(A\). Its minimum is \((2m+1-k)/(m+1)\) and its number of optimizers is \(\binom m{k-m-1}\).

Thus for low budgets optimal leaders are exclusively in the smaller, higher-degree part, while for larger budgets they all move to the larger part. Optimal sets cannot form a nested chain over all budgets. When \(2m+1\) is not a square, the pure-part switch occurs between consecutive budgets \(\lfloor\sqrt{2m+1}\rfloor\) and \(\lfloor\sqrt{2m+1}\rfloor+1\), provided both budgets are at most \(m\). When it is an odd square, both pure allocations tie at the square-root budget, but there is no mixed optimum bridging them. As an example, for \(m=20\), every six-leader optimum lies in \(A\), whereas every seven-leader optimum lies in the disjoint part \(B\).

## Assumptions and scope

The graph has \(2m+1\) vertices, all bipartite edge conductances equal one, and no edges inside either part. Each leader is noise-free, so only followers' states contribute to the objective. Exactly \(k\), not at most \(k\), vertices are leaders. The given cost is the trace of the grounded inverse, without a possible conventional common \(1/2\) variance factor; multiplying all costs by the same positive factor does not affect the optimal sets. At least one follower remains since \(k\le2m\). No assertion is made for weighted, general unbalanced, directed, or noise-corrupted models.

## Proof

For any leader set, put \(a=|S\cap A|\), \(b=k-a=|S\cap B|\), \(p=m-a\), and \(q=m+1-b\). The feasible integers satisfy \(\max\{0,k-(m+1)\}\le a\le\min\{k,m\}\). The grounded Laplacian, after ordering followers by part, is

\[
L_{FF}=\begin{pmatrix}(m+1)I_p&-\mathbf 1_p\mathbf 1_q^{\mathsf T}\\-\mathbf 1_q\mathbf 1_p^{\mathsf T}&mI_q\end{pmatrix}.
\]

With \(D=m(m+1)-pq>0\), block inversion (or the two-dimensional constant-vector eigenspace and the within-part orthogonal complements) gives for **all** \(p,q\ge0\), including the cases of an empty follower part,

\[
J(a)=\frac{p}{m+1}+\frac qm+\frac{(2m+1)pq}{m(m+1)D}.
\tag{1}
\]

For \(pq=0\) the final term vanishes and the formula is immediate from the remaining diagonal block. For \(pq>0\), the two constant-vector eigenvalues have sum \(2m+1\) and product \(D\), while the remaining positive eigenvalues are \(m+1\) (multiplicity \(p-1\)) and \(m\) (multiplicity \(q-1\)); adding their reciprocal contributions gives (1).

Now assume \(1\le k\le m\). The endpoints \(a=0\) and \(a=k\) are both feasible. Direct substitution into (1) gives

\[
J(k)=\frac{(k+1)(2m+1-k)}{k(m+1)},\qquad
J(k)-J(0)=\frac{k^2-2m-1}{km(m+1)}.
\tag{2}
\]

The key strict *chord inequality* is the following exact rational identity. For any integer \(0<a<k\), let \(D_a=km+a^2-ka+a=m(m+1)-pq\). Then

\[
J(a)-\left(\frac{k-a}{k}J(0)+\frac ak J(k)\right)
=\frac{a(k-a)(2m+1)\,[k(m+1)-a-1]}
{k^2m(m+1)D_a}>0.
\tag{3}
\]

The identity follows by substituting (1) and clearing its positive denominators. Positivity is strict because \(a\) and \(k-a\) are positive, \(D_a>0\), and \(k(m+1)-a-1\ge km-1>0\). A convex combination of the two endpoint values is never below their minimum, so every mixed allocation is strictly worse than at least one endpoint. Equation (2) now selects the unique optimal pure part or proves the exact tie. If \(k^2=2m+1\), the square is odd, so \(k\) is odd; the condition \(k\le m\) forces \(k\ge3\), giving all the tie parameters stated.

If \(m+1\le k\le2m\), the follower count is \(f=2m+1-k\le m\). The placement with all of \(B\) selected as leaders has \(q=0\), \(p=f\), and cost \(f/(m+1)\). For any other placement \(q>0\), since \(p+q=f\), (1) gives

\[
J(a)-\frac f{m+1}=q\left(\frac1m-\frac1{m+1}\right)+\frac{(2m+1)pq}{m(m+1)[m(m+1)-pq]}>0.
\tag{4}
\]

The strict first term applies even if \(p=0\). Hence all leaders in \(B\) (plus the required number in \(A\)) is the only optimal allocation. The binomial counts follow from independent vertex permutations within the two parts. Finally, no nested sequence of optimal sets can exist: every one-leader optimizer is in \(A\), but the unique \((m+1)\)-leader optimizer is \(B\) itself; the latter cannot contain the former.

## Verification

The standalone `verify.py` uses exact rational arithmetic only. It compares every feasible allocation for \(2\le m\le100\) and every \(1\le k\le2m\) with the theorem, verifies equations (2) and (3) on the integer ranges, and independently computes the trace of a fully assembled grounded Laplacian inverse for \(2\le m\le7\). It also exhausts all labeled leader subsets for \(2\le m\le4\), checking both minimum costs and optimizer counts. Executing `python verify.py` produces `VERIFY_OK`; `verification_output.txt` records the exact counters. The infinite-family statements are proved by (1)–(4), not by the finite checks.

## Relationship to prior work

Lin, Fardad and Jovanović (arXiv:1302.0450, originally posted 2013-02-03) formulate noise-free leader selection and develop convex/semidefinite relaxations and approximation algorithms. Fitch and Leonard (arXiv:1407.1569, originally posted 2014-07-07) establish the joint-centrality framework and discuss failure of nested optimal leader sets in general, with explicit special-graph results focusing on paths and cycles. Patterson, McGlohon and Dyagilev (arXiv:1412.6595, originally posted 2014-12-20) give algorithms for paths and rings. Those inspected works neither state the all-budget \(K_{m,m+1}\) classification nor the integer threshold \(k^2=2m+1\).

The complete-bipartite three-leader classification appearing in earlier related work determines only the budget \(k=3\); notably the \(K_{4,5}\) tie at \(k=3\) is **not** claimed as a newly discovered special case. General grounded-inverse formulas are established techniques. The new content here is the strict all-budget pure-part theorem, its exact square-root threshold and the full family of optimizer counts. Searches of accessible mathematical records and related alternative objective functions have not located a dominating published statement, but absence from search results is not proof of historical novelty.

## Limitations

The source literature and record searches cannot guarantee that an equivalent all-budget formula does not appear in specialized, incompletely indexed, or inaccessible work. The narrow near-balanced restriction is essential to the clean chord identity; for more imbalanced \(K_{m,n}\), optimal mixed-part allocations can occur, so no general all-bipartite classification is claimed. The discrete non-nesting phenomenon is known in general; only the explicit sharp family and budget switch are claimed here. This work has not undergone independent mathematical validation.

## References

1. F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (first posted 2013-02-03), https://arxiv.org/abs/1302.0450 .
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first posted 2014-07-07), https://arxiv.org/abs/1407.1569 .
3. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (first posted 2014-12-20), https://arxiv.org/abs/1412.6595 .
