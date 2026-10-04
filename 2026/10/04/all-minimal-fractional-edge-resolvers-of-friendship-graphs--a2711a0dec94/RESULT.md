# All minimal fractional edge resolvers of friendship graphs
## Finding
Let \(F_k\), with \(k\ge2\), be the friendship graph consisting of \(k\) triangles sharing a common center \(c\), and let \(U=V(F_k)\setminus\{c\}\). A function \(g:V(F_k)\to[0,1]\) is an edge resolving function exactly when \[g(x)+g(y)\ge1\quad\text{for every distinct }x,y\in U.\] It is a minimal edge resolving function exactly when \(g(c)=0\) and either \(g(x)=1/2\) for every \(x\in U\), or there are a unique distinguished vertex \(a\in U\) and a parameter \(t\in[0,1/2)\) such that \(g(a)=t\) and \(g(x)=1-t\) for every \(x\in U\setminus\{a\}\). Consequently the weights of minimal edge resolving functions fill the interval \([k,2k-1]\), and the published value \(\operatorname{edim}_f(F_k)=k\) is attained by a unique edge resolving function, namely \(g(c)=0\) and \(g(x)=1/2\) for all \(x\in U\).

## Assumptions and scope
All graphs are finite, simple, and connected. For \(k\ge2\), let \(F_k\) be the friendship graph with common center \(c\) and outer vertices
\[
U=\{v_i,w_i:1\le i\le k\},
\]
where \(c v_i w_i c\) is the \(i\)-th triangle.

For distinct edges \(e,e'\), write
\[
R(e,e')=\{z:d(z,e)\ne d(z,e')\}.
\]
An edge resolving function is a map \(g:V(F_k)\to[0,1]\) satisfying
\[
\sum_{z\in R(e,e')}g(z)\ge1
\]
for every distinct pair of edges. It is minimal if no coordinate can be decreased while preserving feasibility.

## Proof
First consider two distinct outer vertices \(x,y\in U\). The two spokes \(cx\) and \(cy\) have
\[
R(cx,cy)=\{x,y\}.
\]
The center has distance zero to both spokes, every outer vertex different from \(x,y\) has distance one to both, and \(x,y\) distinguish the two edges. Hence every edge resolving function satisfies
\[
g(x)+g(y)\ge1
\]
for all distinct \(x,y\in U\).

Conversely, every resolving neighborhood in \(F_k\) contains at least two outer vertices. Two spokes give the pair of their outer endpoints; a spoke and the rim edge in the same triangle give all vertices except one endpoint; a spoke and a rim edge from another triangle contain outer vertices from both triangles; and two rim edges from distinct triangles contain the four outer endpoints. Therefore the pair inequalities on \(U\) imply every edge-resolving inequality. The center coordinate is absent from this reduced system.

It remains to classify the coordinatewise-minimal points of
\[
g(x)+g(y)\ge1\qquad(x\ne y,\ x,y\in U).
\]
Minimality first forces \(g(c)=0\).

Order the \(2k\) outer weights as
\[
a_1\le a_2\le\cdots\le a_{2k}.
\]
Feasibility is equivalent to \(a_1+a_2\ge1\). If \(a_1+a_2>1\), then \(a_1>0\) and one may decrease \(a_1\) slightly, contradicting minimality. Thus
\[
a_1+a_2=1.
\]
For every \(j\ge3\), the positive coordinate \(a_j\) must belong to a tight pair constraint; otherwise it can be decreased. Since \(a_1\) is the smallest coordinate, this is possible only when
\[
a_1+a_j=1.
\]
Hence
\[
a_2=a_3=\cdots=a_{2k}=1-a_1.
\]
Writing \(t=a_1\), the ordering gives \(0\le t\le1/2\). If \(t<1/2\), there is exactly one vertex with weight \(t\), since two such vertices would have total weight below one. If \(t=1/2\), all outer vertices have weight \(1/2\).

Conversely, every function of the displayed form is feasible. When \(t<1/2\), every positive high coordinate lies in a tight pair with the distinguished low vertex, and the low coordinate itself is tight with every high coordinate when \(t>0\); for \(t=0\), only the high coordinates need protection from decrease. At \(t=1/2\), every pair constraint is tight. Thus all of these functions are minimal.

For \(t<1/2\), the weight is
\[
t+(2k-1)(1-t)=2k-1-(2k-2)t.
\]
Together with the uniform endpoint \(t=1/2\), the minimal-function weights fill \([k,2k-1]\). The weight is minimized uniquely at \(t=1/2\), giving \(\operatorname{edim}_f(F_k)=k\).

## Verification
The included checker builds \(F_k\) directly for \(2\le k\le8\), computes all-pairs graph distances, and reconstructs every edge resolving neighborhood from the definition. It verifies that the size-two resolving neighborhoods are exactly all two-element subsets of \(U\), and that every resolving neighborhood contains at least two outer vertices.

The checker then solves the original vertex-level linear program and separately optimizes every coordinate over the optimum face. In every tested graph the optimum is \(k\), the center is forced to zero at optimum, and every outer coordinate is forced to \(1/2\). It also samples the full one-parameter minimal-function family at several rational values and checks coordinatewise minimality through tight constraints.

## Relationship to prior work
The 2021 paper introducing fractional edge dimension gives the defining linear program and establishes general bounds and exact values for several graph classes. A later 2021 paper applies a combinatorial criterion to friendship graphs and proves the scalar identity
\[
\operatorname{edim}_f(F_k)=k.
\]
That paper also defines minimal edge resolving functions, but its friendship-graph result is stated at the level of the minimum value.

The present result determines the complete feasible inequality system on friendship graphs, classifies every minimal edge resolving function, determines the full interval of possible minimal-function weights, and shows that the optimum function is unique. Exact-phrase and semantic searches for friendship graphs together with minimal edge resolving functions, optimizer uniqueness, feasible polytopes, and fractional edge resolvers located the scalar-value paper but no equivalent classification.

## Limitations
The theorem concerns friendship graphs with at least two triangles and fractional edge dimension under the standard edge-distance definition. The scalar value \(\operatorname{edim}_f(F_k)=k\) is prior work and is included only as a consequence. The finite LP checks are corroborative; the all-orders classification follows from the proof. Search coverage cannot exclude an unindexed or differently phrased optimizer classification.

## References
1. E. Yi, “On the edge dimension and fractional edge dimension of graphs,” arXiv:2103.07375v1, 12 March 2021; Discrete Applied Mathematics 316 (2022), 157–170, DOI 10.1016/j.dam.2022.07.014.
2. N. Goshi, S. Zafar, T. Rashid, J. L. G. Guirao, “A Combinatorial Approach to the Computation of the Fractional Edge Dimension of Graphs,” Mathematics 9(19) (2021), 2364, DOI 10.3390/math9192364.
