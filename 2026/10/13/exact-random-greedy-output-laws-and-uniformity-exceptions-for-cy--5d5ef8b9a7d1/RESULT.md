# Exact random-greedy output laws and uniformity exceptions for cycle graphs
## Finding
Let \(C_n\) be the simple cycle on \(n\ge3\) labeled vertices. Scan a uniformly random ordering of its vertices and accept a vertex exactly when none of its previously accepted neighbors has been accepted. The result is a maximal independent set \(I\). Every maximal independent set has cyclic successive selected-vertex distances \(d_1,\ldots,d_k\in\{2,3\}\). The following formulas give the **probability of each individual maximal independent set**, not only its size distribution.

On real functions on \([0,1]\), define the integral operator \(A\) and the function \(b\) by
\[
 (Af)(u)=\int_0^1(1-\min\{u,v\})f(v)\,dv,\qquad b(u)=1-u,
\]
and let \(\phi_a=\langle b,A^a b\rangle\) for every integer \(a\ge0\). If all distances are \(2\), so that \(n=2k\), then
\[
 \Pr(\mathbf I=I)=T_k:=\operatorname{tr}(A^k).
\]
If at least one distance is \(3\), write \(t\ge1\) for the number of 3-distances and \(a_1,\ldots,a_t\) for the nonnegative counts of 2-distances between consecutive 3-distances in the cyclic gap list. Then
\[
 \boxed{\Pr(\mathbf I=I)=\prod_{j=1}^t\phi_{a_j}.}
\]
These are explicitly computable positive rational numbers. For \(g_0(u)=1-u\), \(g_{a+1}=Ag_a\), and \(\phi_a=\int_0^1(1-u)g_a(u)\,du\), polynomial integration computes every factor. In the remaining all-2 case the exact generating function is
\[
 \boxed{\sum_{k\ge1}T_kz^k=-z\frac{D'(z)}{D(z)},\qquad D(z)=\cosh\sqrt z-\sqrt z\sinh\sqrt z.}
\]
The generating function is interpreted as a formal power series at \(z=0\).

**Uniformity classification.** The random-order greedy algorithm gives equal probability to every maximal independent set of \(C_n\) **if and only if**
\[
 \boxed{n\in\{3,4,5,7\}.}
\]
In particular the phenomenon is not simply even-versus-odd: \(C_7\) is uniform, whereas \(C_6\) and every \(C_n\) with \(n\ge8\) are not.

## Assumptions and scope
Every graph is a finite undirected simple cycle \(C_n\) with \(n\ge3\); the scan is a uniformly random permutation, equivalently independent continuous uniform arrival priorities. The algorithm's output is an inclusion-maximal independent vertex set, not necessarily a maximum-cardinality independent set. Probabilities above refer to **labeled individual sets**, not orbit probabilities or the aggregated distribution of cardinalities. In the cyclic gap list, the distance from the last selected vertex to the first is measured along the cycle; a single selected vertex of \(C_3\) has its unique cyclic distance equal to \(3\). The trace is the operator trace on \(L^2([0,1])\), well-defined for the trace-class integral operator \(A\), whose kernel is pointwise positive but which need not be positive semidefinite. No claim is made for paths, arbitrary unicyclic graphs, or graphs of higher degree.

## Proof
**1. The maximal independent sets and the arrival-time certificate.** If two selected vertices were adjacent, independence would fail; hence successive selected vertices are at cyclic distance at least two. If the distance were at least four, an unselected vertex in the middle of that gap would have no selected neighbor, contradicting maximality. Conversely gaps \(2\) and \(3\) suffice for maximality: each unselected vertex is adjacent to a selected endpoint. The same argument covers the one-vertex maximal independent sets of \(C_3\).

For a fixed maximal independent set \(I\) and continuously distributed independent vertex priorities, greedy outputs precisely \(I\) if and only if **each outside vertex has a neighbor belonging to \(I\) with earlier priority**. The forward implication holds since every rejected vertex was rejected by an earlier accepted neighbor. For the reverse implication, if some vertex outside \(I\) were accepted, the earliest accepted outside vertex would have an earlier neighbor in \(I\); if that neighbor had been rejected then a still earlier accepted outside vertex would exist, contradiction. So every vertex outside \(I\) is rejected and every vertex of \(I\) is accepted.

**2. Independent gap contributions.** Conditional on arrival priorities \(u_1,\ldots,u_k\) of the selected vertices, priorities of unselected vertices are independent uniform values. In a distance-2 gap between priorities \(u,v\), the sole intervening vertex must arrive after at least one selected endpoint. Its conditional success probability is \(1-\min\{u,v\}\). In a distance-3 gap, each of the two intervening vertices has **only one** neighbor in \(I\), and both must arrive after its corresponding selected endpoint. The joint factor is \((1-u)(1-v)\). Multiplying over gaps and integrating all selected priorities gives the exact output probability. The distance-2 factor is the kernel of \(A\); the distance-3 factor is the kernel of the rank-one operator \(B=b\otimes b\). Thus the desired integral is \(\operatorname{tr}(K_1\cdots K_k)\), where \(K_i=A\) for a 2-gap and \(K_i=B\) for a 3-gap. This trace identity is valid even for \(k=1\), and the trace-class property follows from the decomposition of \(A\) below. If no \(B\) occurs it is \(T_k=\operatorname{tr}(A^k)\). Otherwise cyclicity of the trace and the identity
\[
 (b\otimes b)A^a(b\otimes b)=\langle b,A^ab\rangle(b\otimes b)
\]
produce \(\prod_{j=1}^t\phi_{a_j}\) exactly, for every run count including zeros.

**3. Fully explicit rational evaluation.** Let \(f(u)=\sum_{m=0}^d c_m u^m\) be any rational polynomial. Splitting the defining integral at \(v=u\) gives
\[
 (Af)(u)=\left(\sum_{m=0}^d\frac{c_m}{m+1}\right)(1-u)
       +\sum_{m=0}^d\frac{c_m u^{m+2}}{(m+1)(m+2)}.
\]
With initial polynomial \(g_0=b=1-u\), this is an exact terminating rational recurrence for every \(g_a=A^ab\), and
\[
 \phi_a=\sum_m\frac{[u^m]g_a}{(m+1)(m+2)}.
\]
In particular
\[
 \phi_0=\frac13,\quad \phi_1=\frac15,\quad \phi_2=\frac17,\quad
 \phi_3=\frac8{81},\quad \phi_4=\frac{34}{495},\qquad
 \phi_0\phi_2-\phi_1^2=\frac4{525}>0.
\]
All \(\phi_a>0\) since \(b>0\) almost everywhere and the kernel of \(A\) is strictly positive on the interior square.

For completeness, the trace generating function also has an exact analytic proof. Let \(J=1\otimes1\) and let \(M\) be the kernel operator \(M(u,v)=\min\{u,v\}\). Then \(A=J-M\). The positive trace-class operator \(M\) has eigenvalues \(1/[\pi^2(j+1/2)^2]\), \(j=0,1,\ldots\), by the elementary boundary-value problem \(-h''=\lambda^{-1}h\), \(h(0)=0\), \(h'(1)=0\). Its Fredholm determinant is therefore
\[
 \det(1+zM)=\prod_{j\ge0}\left(1+\frac{z}{\pi^2(j+1/2)^2}\right)=\cosh\sqrt z.
\]
Solving \((1+zM)f=1\) by twice differentiating and using these boundary conditions yields
\[
 f(u)=\frac{\cosh(\sqrt z(1-u))}{\cosh\sqrt z},\qquad
 \langle1,f\rangle=\frac{\tanh\sqrt z}{\sqrt z}.
\]
The rank-one determinant identity then gives
\[
 \det(1-zA)=\det(1+zM)\left(1-z\langle1,(1+zM)^{-1}1\rangle\right)
 =\cosh\sqrt z-\sqrt z\sinh\sqrt z=D(z).
\]
The formal identity \(-z\,\frac d{dz}\log\det(1-zA)=\sum_{k\ge1}\operatorname{tr}(A^k)z^k\) proves the stated generating function. It also makes every \(T_k\) an exact rational number.

**4. Uniformity, sufficiency.** For \(n=3,4,5,7\) all maximal independent sets form a **single dihedral automorphism orbit**: respectively the cyclic gap multisets \((3)\), \((2,2)\), \((2,3)\), and \((2,2,3)\) are unique up to cyclic rotation and reversal. The random-priority law is invariant under graph automorphisms, so the output law is uniform in these four cases.

**5. Uniformity, necessity: finitely many boundaries.** For each of \(n\in\{6,8,9,10,11,12,14\}\), the following two valid cyclic gap profiles give unequal exact probabilities; their sums equal the specified \(n\):

| \(n\) | First profile and probability | Second profile and probability |
|---|---|---|
| 6 | \((3,3)\): \(1/9\) | \((2,2,2)\): \(1/3\) |
| 8 | \((2,3,3)\): \(1/15\) | \((2,2,2,2)\): \(7/30\) |
| 9 | \((3,3,3)\): \(1/27\) | \((3,2,2,2)\): \(8/81\) |
| 10 | \((3,3,2,2)\): \(1/21\) | \((3,2,3,2)\): \(1/25\) |
| 11 | \((3,3,3,2)\): \(1/45\) | \((3,2,2,2,2)\): \(34/495\) |
| 12 | \((3,3,2,2,2)\): \(8/243\) | \((3,2,3,2,2)\): \(1/35\) |
| 14 | \((3,3,2,2,2,2)\): \(34/1485\) | \((3,2,3,2,2,2)\): \(8/405\) |

**6. Uniformity, necessity: every remaining order.** For any **odd** \(n\ge13\), take precisely three 3-gaps and \(a=(n-9)/2\ge2\) 2-gaps. Choose two cyclic profiles whose runs of consecutive 2-gaps between the three 3-gaps are \((2,0,a-2)\) and \((1,1,a-2)\). By the exact law their probabilities differ by
\[
 \phi_{a-2}(\phi_0\phi_2-\phi_1^2)=\frac4{525}\phi_{a-2}>0.
\]
For every **even** \(n\ge16\), use four 3-gaps and \(a=(n-12)/2\ge2\) 2-gaps, with run profiles \((2,0,0,a-2)\) and \((1,1,0,a-2)\). The positive difference is
\[
 \phi_{a-2}\phi_0(\phi_0\phi_2-\phi_1^2)=\frac4{1575}\phi_{a-2}>0.
\]
Every displayed profile has gaps only \(2\) and \(3\), hence corresponds to a maximal independent set of the relevant labeled cycle. Combining these infinite constructions, the seven boundary checks, and the four uniform cases proves the if-and-only-if classification for every \(n\ge3\).

## Verification
The self-contained `verify.py` uses only Python standard-library exact rational arithmetic. It computes the \(\phi_a\) polynomial recurrence, the \(T_k\) formal-series recurrence, and every cyclic-gap predicted probability. It compares these **independently** to exact probabilities obtained by first-accepted-vertex recursion on induced subgraphs, with no use of the integral-kernel formulas in that recursion. Every maximal independent set of every cycle \(C_n\), \(3\le n\le18\), was checked: **637 individual sets** across **16 graphs**. All output probabilities summed to \(1\) on each graph; the uniformity outcomes matched \(\{3,4,5,7\}\). A second direct enumeration of all **46,230 vertex orders** for \(3\le n\le8\) agreed with the predictions. In particular the code independently asserts \(\phi_0,\ldots,\phi_4\), \(T_3,T_4,T_5\), and the gap \(4/525\). Run `python3 verify.py`; the full actual standard output is saved in `verification-output.txt`. These finite tests check implementation and boundary conditions but do not substitute for the proof for every \(n\).

## Relationship to prior work
Fairfax-Ball's October 1, 2026 preprint proves that the random-order greedy maximal-independent-set law is uniform on a tree only for \(K_1\) and \(K_2\); the checked full manuscript presents classification **beyond trees** as a separate open direction. Cycles are neither trees nor included in that result, and the four exceptional cycles show that the tree obstruction does not simply carry over.

Krivelevich, Mészáros, Michaeli and Shikhelman study the same random greedy process, emphasizing local weak limits and expected occupied densities. Their scope does not determine the probability of each maximal independent set of every finite cycle or the exact uniformity exceptions. Pippenger's random sequential adsorption model uses the same sequential occupancy rule and studies occupancy probabilities and jamming behavior; its accessible abstract does not establish the configuration-resolved theorem here.

A published exact-law theorem for **connected chain graphs** gives probabilities via Ferrers-neighborhood recurrences. It does not imply the law for cycles: except for \(C_4\), cycles are not chain graphs. An exact-law theorem for threshold graphs likewise does not cover the nontrivial cycles here. A 2026 preprint of Kryven, Versendaal and de Vries gives a sufficient uniformity condition, but a strong converse for all cycles was not established by the accessible description; the complete text could not be inspected, so its unexamined contents are a specific residual literature risk.

The contribution is the complete **labeled-set probability formula**, the rational trace generator for the all-2 case, and the **if-and-only-if** uniformity classification, not the random greedy algorithm, the independent arrival-priority representation, or elementary independence/maximality arguments. The literature search and the comparisons described above are bounded and do not constitute proof of global publication priority.

## Limitations
This theorem concerns simple cycles only, with a uniform random vertex ordering and unweighted edges. It does not identify laws on arbitrary unicyclic graphs or characterize uniformity for all graphs. Complete earlier literature on random sequential adsorption and the inaccessible full Kryven–Versendaal–de Vries article may contain equivalent or stronger formulations; publication priority therefore remains uncertain pending independent human literature review. The computer enumeration is finite, while the all-order assertions are proved symbolically. The stated self-review is not independent validation.

## References
1. J. Fairfax-Ball, “Greedy Uniformity on Trees: Exact Obstruction and Near-Uniform Spiders,” arXiv:2610.02276v1 (first posted 2026-10-01), full manuscript `paper/main.tex` at `https://github.com/jfairfaxball-348/Greedy-Uniformity-on-Trees`.
2. M. Krivelevich, T. Mészáros, P. Michaeli, and C. Shikhelman, “Greedy maximal independent sets via local limits,” arXiv:1907.07216 (first posted 2019-07-16), Random Structures & Algorithms, DOI 10.1002/rsa.21200.
3. N. Pippenger, “Random Sequential Adsorption on Graphs,” SIAM Journal on Discrete Mathematics 2 (1989), 393–400, DOI 10.1137/0402034.
4. M. Kryven, R. Versendaal, and J. de Vries, 2026 preprint on uniform iterative maximal-independent-set construction, arXiv:2608.07239 (full text not accessible in this review).
5. “Exact random-greedy maximal-independent-set law on chain graphs,” publicly accessible mathematical finding (2026), `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-random-greedy-maximal-independent-set-law-on-chain-graphs--36fe61ce32de`.
