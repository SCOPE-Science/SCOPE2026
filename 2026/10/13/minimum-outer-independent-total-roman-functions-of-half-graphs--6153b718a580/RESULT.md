# Minimum outer-independent total Roman functions of half graphs
## Finding
Let \(H_n\) be the half graph with \(n\ge2\), bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and adjacency rule
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

Then
\[
\gamma_{oitR}(H_n)=n+2.
\]

For \(n\ge3\), there are exactly \(n+1\) minimum outer-independent total Roman dominating functions. Writing a labeling as
\[
(f(a_1),\ldots,f(a_n);f(b_1),\ldots,f(b_n)),
\]
they are the following staircase family.

At the left endpoint,
\[
F_0=(1,0,\ldots,0;1,\ldots,1,2).
\]

For every
\[
1\le t\le n-1,
\]
\[
F_t=
\left(
2,\underbrace{1,\ldots,1}_{t-1},
\underbrace{0,\ldots,0}_{n-t};
\underbrace{0,\ldots,0}_{t},
\underbrace{1,\ldots,1}_{n-t-1},2
\right).
\]

At the right endpoint,
\[
F_n=(2,1,\ldots,1;0,\ldots,0,1).
\]

For \(n=2\), these three staircase functions are minimum and the all-one function is a fourth minimum.

Thus the minimum-function count is
\[
4\quad\text{for }n=2,
\]
and
\[
n+1\quad\text{for every }n\ge3.
\]

## Assumptions and scope
An outer-independent total Roman dominating function is a map
\[
f:V(G)\to\{0,1,2\}
\]
such that:

1. every vertex labeled \(0\) has a neighbor labeled \(2\);
2. the set of vertices labeled \(0\) is independent; and
3. the subgraph induced by the positive-labeled vertices has no isolated vertices.

Write
\[
V_i=\{v:f(v)=i\},
\qquad
D=V_1\cup V_2.
\]
Then \(D\) is a vertex cover and the weight is
\[
\omega(f)=|D|+|V_2|.
\]

## Proof
The half graph contains the matching
\[
\{a_i b_i:1\le i\le n\},
\]
so every vertex cover has size at least \(n\).

We first classify the minimum vertex covers. A maximum independent set of \(H_n\) has size \(n\). If it contains vertices from both sides and \(t\) is the largest index of a selected \(B\)-vertex, then independence forces every selected \(A\)-vertex to have index greater than \(t\). Reaching size \(n\) then forces the unique form
\[
S_t=\{b_1,\ldots,b_t\}\cup\{a_{t+1},\ldots,a_n\},
\qquad 0\le t\le n.
\]
Hence the minimum vertex covers are exactly
\[
D_t=V(H_n)\setminus S_t
=
\{a_1,\ldots,a_t\}\cup\{b_{t+1},\ldots,b_n\}.
\tag{1}
\]

For
\[
1\le t\le n-1,
\]
the induced graph \(H_n[D_t]\) has no isolated vertices: every selected \(a_i\) is adjacent to \(b_{t+1}\), and every selected \(b_j\) is adjacent to \(a_t\). The endpoint covers \(D_0=B\) and \(D_n=A\) have no edges.

Now let \(f\) be any outer-independent total Roman dominating function. Since \(D\) is a vertex cover,
\[
|D|\ge n.
\]

If \(|D|=n\), totality forces
\[
D=D_t
\]
for some \(1\le t\le n-1\). The zero set is \(S_t\), which meets both bipartition classes. A single vertex labeled \(2\) cannot dominate zeros on both sides of a bipartite graph. Therefore
\[
|V_2|\ge2,
\]
and
\[
\omega(f)=|D|+|V_2|\ge n+2.
\]

If \(|D|\ge n+1\) and the zero set is nonempty, then \(V_2\ne\varnothing\), so again
\[
\omega(f)\ge n+2.
\]

If the zero set is empty, every vertex is positive and
\[
\omega(f)\ge2n.
\]
For \(n\ge2\),
\[
2n\ge n+2.
\]
Thus every feasible function has weight at least \(n+2\).

Each displayed \(F_t\) has weight \(n+2\) and is feasible, proving
\[
\gamma_{oitR}(H_n)=n+2.
\]

It remains to classify equality.

Suppose first that
\[
|D|=n.
\]
Then \(D=D_t\) for some interior index \(t\), and equality forces exactly two vertices labeled \(2\). Since \(b_1\in S_t\) is a leaf whose unique neighbor is \(a_1\), Roman defense forces
\[
f(a_1)=2.
\]
Similarly, \(a_n\in S_t\) forces
\[
f(b_n)=2.
\]
Every other positive vertex must therefore have label \(1\). This is exactly \(F_t\).

Now suppose
\[
|D|=n+1
\]
and equality holds. Then exactly one vertex has label \(2\). Since this single defender cannot dominate zero vertices lying in both bipartition classes, all zeros lie in one side.

If the zero set is contained in \(A\), it has size \(n-1\). Hence
\[
D=B\cup\{a_i\}
\]
for some \(i\). Totality requires every \(b_j\) to have a positive neighbor, so \(a_i\) must be adjacent to every \(b_j\), forcing
\[
i=1.
\]
The sole defender must dominate \(a_n\), so it is \(b_n\). This gives \(F_0\).

The symmetric argument gives \(F_n\).

For \(n\ge3\), the all-positive function has weight \(2n>n+2\), so no further minimum exists. For \(n=2\), the all-one function has weight \(4=n+2\), giving the one exceptional additional minimum.

## Verification
The included verifier constructs \(H_n\) directly for
\[
2\le n\le7
\]
and enumerates every ternary labeling. It checks outer independence of the zero set, Roman defense of every zero, and the no-isolated-vertex condition on the positive support.

The computed minimum weight and complete minimum-function set are then compared with the staircase classification above.

## Relationship to prior work
Outer-independent total Roman domination was introduced in 2019. The introducing primary paper defines the parameter, proves general inequalities involving total co-independent domination and vertex cover, and studies several graph constructions and families. Its inspected full text contains no half-graph occurrence.

A later primary paper develops further inequalities and gives
\[
\gamma_{oitR}(K_{r,s})=r+2
\]
for complete bipartite graphs with \(3\le r\le s\). Its inspected full text contains no half-graph occurrence. Although \(H_n\) and \(K_{n,n}\) have the same bipartition sizes and the same minimum vertex-cover size, the nested deletion pattern in \(H_n\) produces an \(n+1\)-member staircase of minimum functions rather than complete-bipartite symmetry.

The result above is therefore not based only on the scalar value. Its principal content is the complete optimizer classification and the exceptional \(n=2\) boundary.

## Limitations
The theorem classifies minimum outer-independent total Roman functions, not all feasible functions of larger weight.

The all-one function is minimum only at \(n=2\). For \(n\ge3\), the complete minimum family has exactly \(n+1\) members.

The exhaustive computation through \(n=7\) is corroborative only. The arbitrary-\(n\) theorem follows from the minimum vertex-cover classification and the two leaf-forcing arguments.

A differently phrased or non-indexed half-graph treatment may exist despite the targeted searches.

## References
1. A. Cabrera Martínez, D. Kuziak, I. G. Yero, “Outer-independent total Roman domination in graphs,” Discrete Applied Mathematics 269 (2019), 107–119, DOI 10.1016/j.dam.2018.12.018.
2. A. Cabrera Martínez, D. Kuziak, I. G. Yero, “Relating the Outer-Independent Total Roman Domination Number with Some Classical Parameters of Graphs,” Mediterranean Journal of Mathematics 19 (2022), 144, DOI 10.1007/s00009-022-02061-y.
