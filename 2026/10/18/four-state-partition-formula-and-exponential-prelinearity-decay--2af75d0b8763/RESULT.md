# Four-state partition formula and exponential prelinearity decay on graph-incidence Heyting frames

## Finding

For every finite simple graph \(G=(V,E)\), let \(P_G\) be the finite poset containing one maximal point for each graph vertex and one minimal point for each edge, where an edge-point lies below precisely its two endpoint vertices. Let \(H_G=\operatorname{Up}(P_G)\), with its usual Heyting implication, and choose \(U,V\in H_G\) independently and uniformly. The fraction of pairs satisfying the Gödel–Dummett prelinearity equation \((U\to V)\vee(V\to U)=P_G\) is exactly \(A(G)/Z(G)^2\), where

\[
Z(G)=\sum_{S\subseteq V}2^{|E(G[S])|},\qquad
A(G)=\sum_{\sigma:V\to\{00,10,01,11\}}\prod_{\{u,v\}\in E}W_{\sigma(u),\sigma(v)},
\]

and the matrix \(W\), ordered by states \(00,10,01,11\), is

\[
W=\begin{pmatrix}
1&1&1&1\\
1&2&0&2\\
1&0&2&2\\
1&2&2&4
\end{pmatrix}.
\]

Both integers are computable in \(O(|V|)\) arithmetic operations on forests by a four-state tree recursion. For the path graph \(P_m\) on \(m\ge1\) graph vertices, \(A_m=A(P_m)\) and \(Z_m=Z(P_m)\) satisfy

\[
A_1=4,\quad A_2=23,\quad A_3=147,\quad
A_{m+3}=7A_{m+2}-3A_{m+1}-2A_m \quad(m\ge1),
\]

\[
Z_m=F_{2m+1},\qquad F_0=0,\quad F_1=1,\quad F_{r+2}=F_{r+1}+F_r.
\]

Let \(\alpha=(3+\sqrt5)/2\), and let \(\rho\) denote the spectral radius of \(W\), namely the largest real root of \(t^3-7t^2+3t+2\). Then \(0<\rho<\alpha^2\) and there is an explicit constant \(C>0\) such that

\[
\Pr_{U,V\in H_{P_m}}\bigl((U\to V)\vee(V\to U)=P_{P_m}\bigr)
\sim C\left(\frac{\rho}{\alpha^2}\right)^{m-1}
\quad (m\to\infty).
\]

In particular, the proportion satisfying prelinearity tends to zero exponentially along these height-two frames, despite the uniformly bounded number of upper neighbors of every nonmaximal point. For finite graphs, universal satisfaction of the equation occurs exactly when \(E=\varnothing\).

## Assumptions and scope

Graphs are finite, simple, undirected and loop-free. The empty vertex set is allowed for the partition formula; its poset has one upward-closed subset and the empty product convention gives \(A(G)=Z(G)=1\). For the path/asymptotic statements require \(m\ge1\). The ordering of the four states records the two vertex membership indicators. Here \(F_r\) is the standard Fibonacci sequence. The arithmetic-operation bound does not include integer bit complexity. All probabilities use the uniform distribution on the *upward-closed subsets*, not uniformly random subsets of the graph vertices or independent Bernoulli membership at every poset point.

The poset \(P_G\) is the order-dual of the convention in which graph vertices are minimal and edges maximal; this orientation is essential for the stated formulas. For \(U,V\in\operatorname{Up}(P_G)\), implication is characterized pointwise by

\[
 x\in U\to V\quad\Longleftrightarrow\quad \uparrow x\cap U\subseteq V.
\]

## Proof

**Counting upward-closed sets.** Once the maximal graph vertices contained in an upset \(U\) are fixed as \(S\subseteq V\), an edge-point \(e=\{u,v\}\) may be in \(U\) only if \(u,v\in S\). Conversely, every choice of some of the edges induced by \(S\), together with \(S\), is an upset. Thus this trace has exactly \(2^{|E(G[S])|}\) extensions. Summing over \(S\) proves the expression for \(Z(G)\).

**Failure of local prelinearity.** The implication equation holds at each maximal vertex because the two Boolean membership indicators there are comparable. At an edge-point \(e=\{u,v\}\), both implications fail exactly when its principal upset \(\uparrow e=\{e,u,v\}\) contains a witness to \(U\setminus V\) and a witness to \(V\setminus U\). Neither witness can be \(e\): if \(e\in U\setminus V\), then both \(u,v\in U\) and no point of \(\uparrow e\) can belong to \(V\setminus U\); the other orientation is symmetric. Hence the witnesses must be distinct endpoints, one lying in \(U\setminus V\) and the other in \(V\setminus U\). This occurs exactly when the endpoint states are \(10,01\), in either order. No other condition on optional edge-point memberships affects prelinearity.

For fixed endpoint states \(a,b\in\{00,10,01,11\}\), the edge-point may independently enter \(U\) if both first membership bits are one, and may enter \(V\) if both second membership bits are one. Thus the unconstrained count is \(2^{a_1b_1+a_2b_2}\). Excluding precisely the two forbidden ordered endpoint-state pairs \((10,01)\) and \((01,10)\) yields the displayed matrix \(W\). Multiplication over the distinct edge-points and summation over all vertex states gives \(A(G)\). Therefore \(A(G)/Z(G)^2\) is the exact satisfaction probability.

**Forest recursion.** Root each nontrivial tree, and for its vertices \(x\), their parents \(p\), and child sets \(C(x)\), define a four-entry message

\[
M_{x\to p}(t)=\sum_{s\in\{00,10,01,11\}}W_{s,t}\prod_{y\in C(x)}M_{y\to x}(s).
\]

The empty child product is one. At a root \(r\), the tree's numerator is \(\sum_s\prod_{y\in C(r)}M_{y\to r}(s)\). Replace \(W\) by \(B=\left(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right)\) and four states by two to obtain \(Z(G)\). Isolated vertices contribute factors four and two respectively; disconnected components multiply. Every vertex contributes a bounded number of operations per incident edge, giving \(O(|V|)\) exact integer arithmetic operations for a forest.

**Path recurrence.** For a path on \(m\) vertices, successive edge-weight products give

\[
A_m=\mathbf1_4^{\mathsf T}W^{m-1}\mathbf1_4,
\qquad
Z_m=\mathbf1_2^{\mathsf T}B^{m-1}\mathbf1_2.
\]

The symmetric matrix \(W\) has characteristic polynomial \((t-2)(t^3-7t^2+3t+2)\). The eigenvector \((0,1,-1,0)^{\mathsf T}\) for eigenvalue two is orthogonal to \(\mathbf1_4\), so this eigenvalue does not contribute to \(A_m\). Applying the cubic polynomial to \(W\) between the two all-ones vectors gives the stated third-order recurrence and initial values. The characteristic polynomial of \(B\) is \(t^2-3t+1\); the initial values \(Z_1=2\), \(Z_2=5\) identify \(Z_m=F_{2m+1}\).

**Exponential decay.** Both \(W\) and \(B\) are nonnegative primitive symmetric matrices (their squares are strictly positive). Write \(u\) and \(v\) for their strictly positive Euclidean unit Perron eigenvectors. Standard Perron–Frobenius spectral asymptotics give

\[
C=\frac{(\mathbf1_4^{\mathsf T}u)^2}{(\mathbf1_2^{\mathsf T}v)^4}>0,
\quad
\frac{A_m}{Z_m^2}\sim C\left(\frac\rho{\alpha^2}\right)^{m-1}.
\]

Up to a state permutation, the matrix \(B\otimes B\) has entry \(2^{a_1b_1+a_2b_2}\) at states \(a,b\). It strictly dominates \(W\) entrywise at precisely the two forbidden corners. Perron–Frobenius strict spectral monotonicity for the irreducible positive Kronecker matrix gives \(\rho(W)<\rho(B\otimes B)=\alpha^2\). Finally, if \(G\) has any edge \(\{u,v\}\), the upsets \(U=\{u\}\) and \(V=\{v\}\) give a direct failure at that edge-point. If \(G\) has no edges, the poset is an antichain and its Heyting algebra is Boolean, so prelinearity always holds.

## Verification

The standalone program `verify.py` reconstructs all upsets explicitly. It directly evaluates both implications using principal-upset containment and compares its satisfaction count with an independently enumerated four-state partition function. It also checks implication by an independent adjunction-based implementation on the smallest frames, tests forest dynamic programming against direct spin sums, and checks the path transfer recurrences. On execution it returned `VERIFY_OK graphs= 84 independent_pairs= 2490828 adjunction_graphs= 11 tree_recursions= 11 path_recurrence_to=15`. The 84 tested graph instances comprise all simple graphs on at most four labelled vertices and nine additional selected graphs with five or six vertices. Direct exhaustive tests are not an infinite proof; the preceding arguments establish the theorem for all finite graphs and all path lengths.

## Relationship to prior work

Bumpus and Kocsis introduced degree-of-satisfiability problems for Heyting algebras, including binary logical principles; the present result uses that established viewpoint rather than claiming it. Lewis-Smith describes Kripke semantics for a logic extending Gödel–Dummett logic, including linear-frame prelinearity. The present frames are graph-indexed, generally not linear, and the result is an exact probabilistic counting formula with a transfer-matrix decay theorem. Trotter and Wang study incidence posets in their standard orientation (vertices below edges) via order dimension and cover graphs; here the *dual* incidence order is used for logical semantics and counting. A previous exact prelinearity calculation for ordinal sums of antichains addresses weak-order frames, not general graph-incidence frames or the four-state graph partition function. The earlier height-two negation-fiber reconstruction framework does not state the joint prelinearity law, its path recurrence, or the exponential rate.

## Limitations

The path asymptotic is restricted to graph paths; arbitrary families of finite graphs may exhibit different rates. The linear-time forest algorithm counts arithmetic operations, not bit operations. The result does not address probabilistic validity under nonuniform distributions on Heyting-algebra elements, or graph incidence posets with the opposite orientation. The finite verifier checks examples, not every graph. Equivalent partition functions may have appeared elsewhere under another description, and publication priority is not independently settled.

## References

1. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515, first public 2021-10-21, https://arxiv.org/abs/2110.11515. Full text inspected (introduction and relevant implication/satisfiability sections).
2. A. Lewis-Smith, *A Kripke Semantics for Hajek's BL*, arXiv:2308.04518, first public 2023-08-08, https://arxiv.org/abs/2308.04518. Full text inspected (Kripke semantics and prelinearity sections).
3. W. T. Trotter and R. Wang, *Incidence Posets and Cover Graphs*, arXiv:1308.2471, first public 2013-08-12, https://arxiv.org/abs/1308.2471. Orientation convention and graph-poset scope inspected.
