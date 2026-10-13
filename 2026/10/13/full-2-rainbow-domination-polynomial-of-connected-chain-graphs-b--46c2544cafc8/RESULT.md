# Full 2-rainbow domination polynomial of connected chain graphs by extremal empty labels
## Finding
Let \(G=(A,B,E)\) be any finite connected chain graph. Label its bipartition \(A=\{a_1,\ldots,a_p\}\), \(B=\{b_1,\ldots,b_q\}\), where \(p,q\ge1\), so that
\[
N(a_i)=\{b_1,\ldots,b_{d_i}\},\qquad 1\le d_1\le\cdots\le d_p=q.
\]
Set \(s_j=\min\{i:d_i\ge j\}\) for \(1\le j\le q\); hence \(N(b_j)=\{a_{s_j},\ldots,a_p\}\). A 2-rainbow dominating function assigns to each vertex one of \(\varnothing,\{1\},\{2\},\{1,2\}\), with every empty-labelled vertex seeing both colors among its open neighbors. Write \(R_G(x)=\sum_f x^{\sum_v|f(v)|}\), summing over all such functions.

Define the three local label types \(E\) (forced empty), \(P\) (any nonempty subset of the two colors), and \(F\) (any subset). For \(r\in\{0,1,2\}\), set
\[
h_{E,r}(x)=1,\quad h_{P,r}(x)=(1+x)^{2-r}-1,\quad h_{F,r}(x)=(1+x)^{2-r}.
\]
For a type word \(\tau=(\tau_1,\ldots,\tau_m)\) and a set \(T\subseteq\{1,\ldots,m\}\), define
\[
\Phi(\tau,T;x)=\begin{cases}
\prod_{v=1}^m h_{\tau_v,0}(x),&T=\varnothing,\\
\displaystyle\sum_{r=0}^2(-1)^r\binom2r\prod_{v=1}^m h_{\tau_v,r\mathbf1_{v\in T}}(x),&T\ne\varnothing.
\end{cases}
\]
Here \(\Phi\) enumerates precisely the assignments respecting the type restrictions such that both colors occur on the vertices in \(T\), if \(T\ne\varnothing\).

For \(1\le i\le p\), let \(u_i\) be the length-\(p\) type word consisting of \(i-1\) copies of \(P\), then \(E\), then \(p-i\) copies of \(F\); let \(u_{p+1}=P^p\). For \(1\le j\le q\), let \(v_j\) consist of \(j-1\) copies of \(F\), then \(E\), then \(q-j\) copies of \(P\); let \(v_0=P^q\). Put \(T_A(j)=\{s_j,\ldots,p\}\) when \(j\ge1\) and \(\varnothing\) when \(j=0\), and \(T_B(i)=\{1,\ldots,d_i\}\) when \(i\le p\) and \(\varnothing\) when \(i=p+1\). Then the **complete weight enumerator** is
\[
\boxed{R_G(x)=\sum_{i=1}^{p+1}\sum_{j=0}^{q}
\Phi(u_i,T_A(j);x)\,\Phi(v_j,T_B(i);x).}
\]
The expression has at most \((p+1)(q+1)\) summands with at most three product terms in each factor and computes every coefficient in polynomially many integer-arithmetic operations. In particular, for the four-vertex path and cycle, respectively,
\[
R_{P_4}(x)=12x^3+48x^4+52x^5+28x^6+8x^7+x^8,
\]
\[
R_{C_4}(x)=4x^2+24x^3+62x^4+56x^5+28x^6+8x^7+x^8.
\]

## Assumptions and scope
Graphs are finite, simple, undirected, connected, and bipartite. In a chain graph one can order vertices so that their neighborhoods are nested; repeated degrees and class sizes are permitted. Connectedness forces every \(d_i\ge1\) and \(d_p=q\). Colors are distinguishable: exchanging colors gives a different function unless the labels agree vertex by vertex. The polynomial counts **all** ordinary 2-rainbow dominating functions by total color weight, not solely minimum functions, Roman \(\{2\}\) functions, or total 2-rainbow functions. The formula includes \(K_2\), stars, complete bipartite graphs, and arbitrary Ferrers shapes.

## Proof
Every function has a unique first empty vertex on the \(A\)-side, at index \(i\in\{1,\ldots,p\}\), or no empty vertex on that side (sentinel \(i=p+1\)). Likewise, it has a unique last empty vertex on the \(B\)-side, at index \(j\in\{1,\ldots,q\}\), or none (sentinel \(j=0\)). Fix these two indices. The definitions of first and last empty vertices imply, with no other conditions, exactly the label-type restrictions \(u_i\) on \(A\) and \(v_j\) on \(B\), respectively. Conversely, every labeling respecting these two type words has exactly these indices. Thus the cases indexed by \((i,j)\) are disjoint and exhaustive.

If \(i\le p\), vertex \(a_i\) is empty and must see both colors in its neighborhood \(T_B(i)\). For any other empty \(a_k\), necessarily \(k\ge i\). Since \(d_k\ge d_i\), its neighborhood contains \(T_B(i)\) and therefore automatically sees both colors if \(a_i\) does. If \(i=p+1\), no \(A\)-vertex is empty, so no coverage condition is imposed on the \(B\)-side. Hence all empty vertices on \(A\) are valid exactly when the labels on \(T_B(i)\) jointly carry both colors, with the condition vacuous for the sentinel.

Dually, if \(j\ge1\), vertex \(b_j\) is empty, and every other empty \(b_k\) has \(k\le j\). As \(s_k\le s_j\), the neighborhood \(N(b_k)\) contains \(N(b_j)=T_A(j)\). Thus all empty vertices on \(B\) are valid exactly when the labels on \(T_A(j)\) jointly carry both colors. When \(j=0\) there are no such conditions.

For fixed type word and nonempty test set \(T\), start from all type-allowed assignments. Delete those with color \(1\) absent on \(T\) and those with color \(2\) absent there; add back assignments with both colors absent. Forbidding a given set of \(r\) distinct colors at a vertex of \(T\) leaves \(h_{\tau_v,r}(x)\) choices by weight; outside \(T\), it leaves \(h_{\tau_v,0}(x)\). Ordinary inclusion-exclusion over the two colors gives exactly the displayed \(\Phi\), including the forced-empty case \(h_{E,r}=1\). For empty \(T\) no coverage is requested, giving the first case of the definition.

The two coverage conditions involve opposite bipartition sides. Conditional on the unique pair \((i,j)\), the weight enumerator therefore factors into \(\Phi(u_i,T_A(j);x)\Phi(v_j,T_B(i);x)\). Summing over all pairs proves the formula for every finite connected chain graph. There are only quadratically many pairs and each factor is a sum of at most three products of elementary binomial polynomials, proving the arithmetic-operation bound.

## Verification
The accompanying standalone Python 3 script `verify_rainbow_chain.py` independently constructs the bipartite graph and enumerates all \(4^{p+q}\) color-subset labelings for every one of the \(111\) nondecreasing positive chain degree profiles with \(1\le p,q\le5\), \(p+q\le8\), and \(d_p=q\). It tests each empty vertex's open-neighborhood color union literally, and independently computes the complete coefficient array by the displayed inclusion-exclusion product formula. The exact replay prints `VERIFY_OK profiles=111 labelings=3843216 coefficient_checks=1651 max_order=8` and the displayed path and cycle examples. Its exhaustive finite census validates these small cases, but the unrestricted theorem rests on the preceding proof.

## Relationship to prior work
Brešar and Šumenjak introduced ordinary 2-rainbow domination and its minimum-weight graph invariant. Padamutham and Palagiri's 2020 treatment of Roman \(\{2\}\)-domination includes a nested-neighborhood chain-graph characterization and an algorithm for the **minimum Roman \(\{2\}\) weight**; the latter uses three numeric labels and a different condition, so it does not determine the four-label all-function enumerator above. Kumar and Reddy's 2023 paper investigates algorithms for the **minimum total 2-rainbow domination** problem on chain graphs, which includes an additional positive-vertex support condition and concerns optimum weight. The accessible publisher page and abstract do not state the present polynomial; full text could not be inspected end to end.

A publicly available result, *All 2-rainbow dominating functions of complete multipartite graphs* (2026), already counts the four-label functions on all complete multipartite graphs. Its complete proof was inspected. Among connected bipartite chain graphs, it covers the complete-bipartite subfamily, but not noncomplete Ferrers graphs such as \(P_4\). A separate result, *Roman domination polynomial of chain graphs* (2026), counts different three-label Roman functions and does not imply the four-label rainbow enumerator; its complete proof was also inspected. An ordinary domination-polynomial formula for chain graphs likewise counts selected subsets, not color-subset labelings. The claims here concern the full arbitrary-shape chain-graph two-color enumerator rather than those known results.

## Limitations
No claim is made about all bipartite graphs, more than two colors, or independent/total rainbow variants. The explicit formula gives a polynomial-time arithmetic expression, not a uniformly linear-time implementation or an asymptotic complexity lower bound. Finite numerical checks cover order at most eight only and are not an infinite proof. Poorly indexed Ferrers-graph enumerators and inaccessible full-text sections of neighboring total-domination papers remain residual bibliographic risks; neither a null search nor the graph-class partition proves global novelty.

## References
1. B. Brešar and T. K. Šumenjak, *On the 2-rainbow domination in graphs*, Discrete Applied Mathematics 155 (2007), 2394–2400.
2. C. Padamutham and V. S. R. Palagiri, *Complexity of Roman {2}-domination and the double Roman domination in graphs*, AKCE International Journal of Graphs and Combinatorics (first public 2020-05-04), DOI: 10.1016/j.akcej.2020.01.005. Full open-access text: https://www.tandfonline.com/doi/full/10.1016/j.akcej.2020.01.005 .
3. M. Kumar and P. V. S. Reddy, *Total 2-Rainbow Domination in Graphs: Complexity and Algorithms*, International Journal of Foundations of Computer Science (first public 2023-10-28), DOI: 10.1142/S0129054123500260.
4. *All 2-rainbow dominating functions of complete multipartite graphs*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-2-rainbow-dominating-functions-of-complete-multipartite-grap--7f7bcd9e9b58 .
5. *Roman domination polynomial of chain graphs*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-roman-domination-polynomial-of-chain-graphs--e846e0fa619b .
6. *Exact domination polynomial of chain graphs*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-domination-polynomial-of-chain-graphs--f5aba0dd8f21 .
