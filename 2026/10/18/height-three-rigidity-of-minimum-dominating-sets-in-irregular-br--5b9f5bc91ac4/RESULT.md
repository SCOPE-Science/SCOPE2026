# Height-three rigidity of minimum dominating sets in irregular branching trees

## Finding

Let \(T\) be a finite rooted tree of height \(h\geq 0\). Assume **every leaf has depth exactly \(h\)** and **every nonleaf vertex has at least two children**; the number of children may differ arbitrarily between vertices and levels. Write \(L_j\) for the vertices of depth \(j\), \(\gamma(T)\) for the domination number, and \(\zeta(T)\) for the number of minimum dominating vertex sets. Then, for every \(t\geq0\),

\[
\begin{array}{c|c|c}
\text{height} & \gamma(T) & \zeta(T)\\ \hline
h=3t+1 & \displaystyle\sum_{j=0}^{t}|L_{3j}| &1\\[2pt]
h=3t+2 & \displaystyle\sum_{j=0}^{t}|L_{3j+1}|&1\\[2pt]
h=3t\geq3 & \displaystyle1+\sum_{j=0}^{t-1}|L_{3j+2}|&1+|L_1|
\end{array}
\]

For \(h=0\), \(\gamma(T)=\zeta(T)=1\). More precisely, in the first two cases **the unique** minimum dominating set is the union of the displayed levels. At heights divisible by three and positive, **all** minimum dominating sets are

\[
\left(\bigcup_{j=0}^{t-1}L_{3j+2}\right)\cup\{v\},
\quad v\in L_0\cup L_1.
\]

The striking point is that changing every branching number below the root, even nonuniformly within the same level, changes the size of the optimum but not its multiplicity. Only the root degree affects the nontrivial multiplicity.

## Assumptions and scope

All graphs are finite, simple, and undirected. A set \(D\subseteq V(T)\) *dominates* \(T\) if each vertex belongs to \(D\) or has a neighbour in \(D\). Here \(\gamma(T)=\min\{|D|:D\text{ dominates }T\}\) and \(\zeta(T)=|\{D:D\text{ dominates }T,\ |D|=\gamma(T)\}|\). The root is part of the specified input. A leaf is a vertex with no children, including the root when \(h=0\). A nonleaf has two or more children, with **no uniformity assumption**. The condition that all leaves lie at the same depth is essential to the synchronous three-level structure; trees with unary nodes or leaves at differing depths are not covered.

## Proof

For a rooted subtree \(U\) of remaining height \(k\), introduce three states at its root \(u\). State \(A\) selects \(u\). State \(B\) omits \(u\) but dominates it by a selected child. State \(C\) omits \(u\) and all its children, leaving \(u\) to be dominated by a parent outside \(U\). In every state, all other vertices of \(U\) must already be dominated inside \(U\). Denote the minimum cardinalities by \(a,b,c\), with value \(+\infty\) for an infeasible state. The number of minimizing partial sets is counted separately in each state.

If \(u\) has children \(u_1,\ldots,u_d\), then \(d\ge2\). The state \(A\) has cost

\[
a=1+\sum_i\min\{a_i,b_i,c_i\};
\]
state \(C\) has cost \(c=\sum_i b_i\); and state \(B\) minimizes \(\sum_i\epsilon_i\) over \(\epsilon_i\in\{a_i,b_i\}\), requiring at least one \(\epsilon_i=a_i\). These are exact recurrences, since a parent selects or omits its root and the child subtrees are vertex-disjoint. Whenever costs tie, every minimizing child-state combination is counted; hence multiplicities are not inferred from costs alone.

At height zero, \((a,b,c)=(1,+\infty,0)\), with one partial set in each feasible state. At height one, a root with \(d\ge2\) leaves has \((a,b,c)=(1,d,+\infty)\). State \(A\) is uniquely minimizing. We prove simultaneously the following more precise assertions for every rooted subtree satisfying the hypotheses:

1. For remaining height \(k\equiv1\pmod3\), \(a<b,c\), state \(A\) has exactly one minimizer, and \(b-a\ge d-1\), \(c-a\ge d-1\). The latter bound allows \(+\infty\) at height one.
2. For \(k\equiv2\pmod3\), \(b<a<c\), with \(a=b+1\) and \(c\ge b+d\). States \(A\) and \(B\) each have exactly one minimizer.
3. For positive \(k\equiv0\pmod3\), \(c<a=b=c+1\). State \(C\) has exactly one minimizer, state \(A\) exactly one, and state \(B\) exactly \(d\) minimizers.

At height two, every child has height one. Its uniquely minimizing state is \(A\), with cost gap at least one to \(B\) and with \(C\) infeasible. Therefore the parent has \(b=\sum_i a_i\), \(a=b+1\), and \(c=\sum_i b_i\ge b+d\). Both its \(A\)- and \(B\)-minimizers are unique.

If \(k\equiv0\pmod3\) and \(k\ge3\), each child is of type 2: its uniquely cheapest state is \(B\), and switching to \(A\) costs exactly one. For the parent, \(c=\sum_i b_i\), \(a=c+1\), and \(b=c+1\). The \(C\)- and \(A\)-optima use all children in state \(B\), while state \(B\) requires exactly one child in state \(A\), giving exactly \(d\) choices. This proves assertion 3.

If \(k\equiv1\pmod3\) and \(k\ge4\), each child is of type 0: its unique cheapest state is \(C\), precisely one cheaper than \(A\) or \(B\). Thus \(a=1+\sum_i c_i\) is unique, whereas \(b=c=\sum_i(c_i+1)=a+d-1\). This proves assertion 1 for larger heights.

If \(k\equiv2\pmod3\) and \(k\ge5\), each child is of type 1: its unique cheapest state is \(A\), with \(b_i-a_i\ge1\) and \(c_i-a_i\ge1\). Therefore \(b=\sum_i a_i\) is unique, \(a=b+1\) is unique, and \(c=\sum_i b_i\ge b+d\), proving assertion 2. This closes the induction.

The global root may only be in state \(A\) or \(B\); state \(C\) is inadmissible without a parent. Consequently, the global optimizer is unique in heights congruent to one or two modulo three, while in positive heights divisible by three there are exactly \(1+d\) minimizers (one from root state \(A\), and \(d=|L_1|\) from root state \(B\)). Propagating the **unique minimizing state choices** above down the tree shows that the selected levels are exactly those in the displayed formulas, except that the top choice at heights divisible by three is either the root or exactly one root child. Thus both the optimum sizes and the complete optimizer classification follow. The single-vertex boundary case follows directly.

## Verification

Run `python3 verify.py` from the directory containing this document. The verifier independently enumerates every dominating subset of 313 small-tree instances with labelled vertices and possibly irregular branching, including their **entire minimum-set families**, and compares to both the classified optimizers and cardinality formulas. An independently coded bottom-up minimum-and-count dynamic program additionally checks all 363 levelwise branching profiles of heights one through five with branching factors two, three or four, and 425 independently seeded irregular trees of heights two through six. Total: 1,101 comparison instances, all passed in the recorded run. These finite checks corroborate but do not replace the unrestricted induction.

## Relationship to prior work

Allagan, Gray, Sawyer and Morgan (arXiv:2601.03485, first posted 2026-01-07), Theorem 10, establish a period-three dominion law for **complete binary trees**. The present theorem extends its explicit minimum-set multiplicities and gives a full optimizer classification for arbitrarily irregular full-depth branching trees, where different vertices at the same level may have different degrees. Their general linear-time dynamic-programming theorem provides an algorithm, not these closed formulas for irregular branching. The earlier Livingston–Stout paper discusses constant-time domination algorithms for **fixed-arity** complete trees and possible counting extensions without supplying this nonuniform equality-case classification. Petr, Portier and Versteegen give general forest bounds on minimum-set multiplicities, not the exact structure here. The binary case and the general algorithmic principles are not claimed as discoveries.

## Limitations

The result concerns ordinary domination on rooted trees with all leaves at equal depth and at least two children per internal vertex. It does not classify trees with unary nodes or leaves at differing depths, nor other domination variants. Both structural assumptions matter: for the four-vertex path rooted at an endpoint (three unary internal vertices), the actual number of minimum dominating sets is four, not the predicted two; and for the five-vertex tree with a root joined to one leaf and to a parent of two additional leaves (unequal leaf depths), there are two minimum dominating sets rather than the unique level-one set predicted by the formula outside its scope. It is an explicit theorem deduced from the given finite-state induction, not a claim of a new general-purpose domination algorithm. Literature priority is assessed against the inspected sources and search results, not independently certified; unseen equivalent formulations remain a residual risk. 

## References

1. J. Allagan, E. Gray, J. Sawyer, and G. Morgan, *Four Dominion Growth Regimes in Trees: Forcing, Fibonacci Enumeration, Periodicity, and Stability*, arXiv:2601.03485 (first posted 2026-01-07). https://arxiv.org/abs/2601.03485
2. J. Petr, J. Portier, and L. Versteegen, *On the number of minimum dominating sets and total dominating sets in forests*, Journal of Graph Theory **106** (2024), 976–993, DOI:10.1002/jgt.23107; arXiv:2206.13182. https://arxiv.org/abs/2206.13182
3. M. Livingston and Q. F. Stout, *Constant Time Computation of Minimum Dominating Sets*, Congressus Numerantium **105** (1994), 116–128. https://web.eecs.umich.edu/~qstout/abs/BR94dom.html
