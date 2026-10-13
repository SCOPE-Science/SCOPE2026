# Perfect Italian domination of half graphs
## Finding
Let \\(H_n\\) be the half graph with bipartition
\\[
A=\\{a_1,\\ldots,a_n\\},\\qquad B=\\{b_1,\\ldots,b_n\\},
\\]
and edge set
\\[
E(H_n)=\\{a_i b_j:1\\le i\\le j\\le n\\}.
\\]
For every \\(n\\ge4\\),
\\[
\\gamma_I^p(H_n)=4.
\\]

More strongly, the minimum perfect Italian dominating function is unique. It is
\\[
f(a_1)=f(b_n)=2
\\]
and
\\[
f(v)=0
\\]
for every other vertex.

The boundary graph \\(H_3\\) also has perfect Italian domination number \\(4\\), but it has a second optimum, so the uniqueness threshold is exactly \\(n=4\\).

## Assumptions and scope
A perfect Italian dominating function on a graph \\(G\\) is a map
\\[
f:V(G)\\to\\{0,1,2\\}
\\]
such that every vertex \\(v\\) with \\(f(v)=0\\) satisfies
\\[
\\sum_{u\\in N(v)}f(u)=2.
\\]
Its weight is
\\[
\\sum_{v\\in V(G)}f(v),
\\]
and the minimum weight is denoted by \\(\\gamma_I^p(G)\\).

For a labeling of \\(H_n\\), write
\\[
x_i=f(a_i),\\qquad y_i=f(b_i),
\\]
and set
\\[
X=\\sum_i x_i,\\qquad Y=\\sum_i y_i.
\\]
If \\(x_i=0\\), then the exact perfect-Italian condition is
\\[
\\sum_{j=i}^{n}y_j=2,
\\tag{1}
\\]
while if \\(y_j=0\\), it is
\\[
\\sum_{i=1}^{j}x_i=2.
\\tag{2}
\\]

## Proof
The labeling
\\[
f(a_1)=f(b_n)=2
\\]
with every other label \\(0\\) is feasible. Indeed, every zero vertex \\(a_i\\) with \\(i\\ge2\\) sees exactly the label \\(2\\) at \\(b_n\\), and every zero vertex \\(b_j\\) with \\(j\\le n-1\\) sees exactly the label \\(2\\) at \\(a_1\\). Hence
\\[
\\gamma_I^p(H_n)\\le4.
\\tag{3}
\\]

Now suppose a perfect Italian dominating function has weight at most \\(3\\). Since \\(n\\ge4\\), neither bipartition class can be entirely positive, because that alone would contribute weight at least \\(4\\). Thus there is a zero vertex in each side. Equation (1) for a zero in \\(A\\) gives \\(Y\\ge2\\), and equation (2) for a zero in \\(B\\) gives \\(X\\ge2\\). Therefore
\\[
X+Y\\ge4,
\\]
a contradiction. Combining this with (3) yields
\\[
\\gamma_I^p(H_n)=4.
\\]

It remains to prove uniqueness. Let \\(f\\) have weight \\(4\\). Again, each side contains a zero, so the same argument forces
\\[
X=Y=2.
\\tag{4}
\\]
Let \\(q\\) be the largest index with \\(x_q>0\\). Suppose \\(q\\ge2\\). For every \\(j<q\\), the vertex \\(b_j\\) cannot be zero: otherwise (2) would require the prefix \\(x_1+\\cdots+x_j\\) to equal \\(2\\), but the positive label \\(x_q\\) lies outside that prefix while the total side weight is only \\(2\\). In particular,
\\[
y_1>0.
\\]

Now take any \\(i\\ge2\\). If \\(x_i=0\\), then (1) requires the suffix \\(y_i+\\cdots+y_n\\) to equal \\(2\\). But by (4) the total \\(B\\)-weight is \\(2\\), and the positive term \\(y_1\\) is omitted from that suffix, so the suffix has weight strictly less than \\(2\\). Hence every \\(a_i\\) with \\(i\\ge2\\) must be positive. This contributes at least \\(n-1\\ge3\\) to \\(X\\), contradicting (4). Therefore
\\[
q=1.
\\]
Since \\(X=2\\), we obtain
\\[
x_1=2,\\qquad x_i=0\\quad(i\\ge2).
\\]
Finally, \\(a_n\\) is zero, so (1) at \\(i=n\\) gives
\\[
y_n=2.
\\]
Since \\(Y=2\\), all other \\(y_j\\) vanish. Thus the displayed construction is the unique optimum.

For \\(n=3\\), the same lower bound and construction give value \\(4\\), but the labeling
\\[
(x_1,x_2,x_3;y_1,y_2,y_3)=(0,1,1;1,1,0)
\\]
is also feasible. Hence uniqueness begins at \\(n=4\\).

## Verification
The included checker constructs \\(H_n\\) directly and evaluates the exact neighbor-sum condition. For each \\(2\\le n\\le14\\), it exhausts all labelings in \\(\\{0,1,2\\}^{2n}\\) of total weight up to the first feasible weight. In particular, for every \\(4\\le n\\le14\\) it proves computationally that no labeling of weight below \\(4\\) is feasible and that the only weight-
\\(4\\) optimum is the one in the theorem.

## Relationship to prior work
Perfect Italian domination was introduced in 2019. The foundational and early follow-up literature develops tree bounds, general characterizations for very small values, exact results for complete multipartite and other standard classes, and hardness results for bipartite graphs.

A full-text 2019 primary study characterizes graphs with perfect Italian domination number \\(2\\) and \\(3\\) and determines the parameter on complete multipartite graphs, but its searchable text contains no half-graph, chain-graph, or bipartite-permutation specialization.

More recent algorithmic work places perfect Italian domination in polynomial time on broad structured bipartite classes, including path-convex bipartite graphs. This broader algorithmic coverage is compatible with the theorem but does not state the closed half-graph value or the unique optimum labeling. The half graph is a canonical chain graph with strictly nested neighborhoods, and the proof above uses those nested prefix-suffix identities to obtain the exact rigidity statement.

## Limitations
The theorem concerns the canonical half graph, not arbitrary chain graphs with repeated neighborhood classes.

The full minimum-function classification is stated only for \\(n\\ge4\\); \\(H_3\\) has one additional optimum.

The checker is finite corroboration. The arbitrary-order proof is symbolic and does not rely on the computation.

A differently phrased or non-indexed half-graph treatment may exist despite the targeted searches.

## References
1. T. W. Haynes, M. A. Henning, “Perfect Italian domination in trees,” Discrete Applied Mathematics 260 (2019), 164–177, DOI 10.1016/j.dam.2019.01.038.
2. J. Lauri, C. Mitillos, “Perfect Italian domination on planar and regular graphs,” arXiv:1905.06293v1, 15 May 2019; Discrete Applied Mathematics 285 (2020), 676–688, DOI 10.1016/j.dam.2020.05.024.
3. R. Pazhaniappan, M. M. Sathi, M. V. Malayil, “Perfect Italian Domination on Structured Bipartite Graphs: Algorithms, Parameterization, and Hardness,” Mathematics 14 (2026), 3380, DOI 10.3390/math14183380.
