# Minimum outer-independent double Roman functions of half graphs
## Finding
Let \(H_n\) be the half graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]
Then
\[
\gamma_{oidR}(H_2)=5,\qquad
\gamma_{oidR}(H_n)=n+4\quad(n\ge3).
\]

For every \(n\ge4\), there are exactly \(n+1\) minimum functions. They are
\[
F_0=(2,0,\ldots,0;1,\ldots,1,3),
\]
\[
F_t=
\left(
3,\underbrace{1,\ldots,1}_{t-1},
\underbrace{0,\ldots,0}_{n-t};
\underbrace{0,\ldots,0}_{t},
\underbrace{1,\ldots,1}_{n-t-1},3
\right),
\qquad 1\le t\le n-1,
\]
and
\[
F_n=(3,1,\ldots,1;0,\ldots,0,2).
\]

For \(H_2\), the four minima are
\[
(0,0;2,3),\quad(0,1;2,2),\quad(2,2;1,0),\quad(3,2;0,0).
\]

For \(H_3\), the eight minima are
\[
(0,0,0;2,2,3),\quad(0,0,1;2,2,2),\quad
(2,0,0;1,1,3),\quad(2,2,2;1,0,0),
\]
\[
(3,0,0;0,1,3),\quad(3,1,0;0,0,3),\quad
(3,1,1;0,0,2),\quad(3,2,2;0,0,0).
\]

## Assumptions and scope
An outer-independent double Roman dominating function is a map
\[
f:V(G)\to\{0,1,2,3\}
\]
such that every vertex labeled \(0\) has either one neighbor labeled \(3\) or at least two neighbors labeled \(2\), every vertex labeled \(1\) has a neighbor labeled \(2\) or \(3\), and the zero-labeled set is independent.

Put
\[
D=\{v:f(v)>0\}
\]
and
\[
e(f)=|V_2|+2|V_3|.
\]
Then
\[
\omega(f)=|D|+e(f).
\]

## Proof
Assume \(n\ge4\). Since the zero set is independent, \(D\) is a vertex cover. The matching
\[
\{a_i b_i:1\le i\le n\}
\]
therefore gives
\[
|D|\ge n.
\tag{1}
\]

If zeros occur in both bipartition classes, then a zero in \(A\) requires at least two excess units in \(B\), while a zero in \(B\) requires at least two excess units in \(A\). Hence
\[
e(f)\ge4.
\tag{2}
\]

Suppose all zeros lie in \(A\). If \(|D|=n\), then \(D=B\). Every positive vertex of \(B\) labeled \(1\) would lack a neighbor labeled \(2\) or \(3\), so every vertex of \(B\) has label at least \(2\), and
\[
e(f)\ge n\ge4.
\tag{3}
\]

If \(|D|=n+1\) and \(e(f)\le2\), all available excess is needed in \(B\) to defend the zeros, leaving the unique positive vertex of \(A\) labeled \(1\). Then the label-\(1\) vertices of \(B\) have no strong positive neighbor in \(A\), impossible for \(n\ge4\). Thus
\[
e(f)\ge3.
\tag{4}
\]

If \(|D|\ge n+2\) and zeros remain, at least one zero requires one label \(3\) or two labels \(2\), so
\[
e(f)\ge2.
\tag{5}
\]
If there are no zeros, the all-\(1\) labeling is infeasible, and every feasible all-positive labeling has weight exceeding \(n+4\).

Equations (1)--(5), together with the symmetric one-sided-zero case, imply
\[
\omega(f)\ge n+4.
\]
Every displayed \(F_t\) has weight \(n+4\), so
\[
\gamma_{oidR}(H_n)=n+4
\qquad(n\ge4).
\]

We classify equality. If \(|D|=n\), then the zero set is a maximum independent set. The maximum independent sets are exactly
\[
S_t=\{b_1,\ldots,b_t\}\cup\{a_{t+1},\ldots,a_n\},
\qquad0\le t\le n.
\]
For an interior index \(1\le t\le n-1\), \(b_1\) is zero and forces \(f(a_1)=3\), while \(a_n\) is zero and forces \(f(b_n)=3\). These two labels consume all four excess units, so every other positive vertex has label \(1\). This is \(F_t\). The endpoint covers \(A\) and \(B\) cannot attain equality for \(n\ge4\), because their label-\(1\) vertices would have no strong neighbor in the opposite side.

If \(|D|=n+1\), then equality gives \(e(f)=3\), and the zero set lies in one bipartition class. Suppose it lies in \(A\). Then
\[
D=B\cup\{a_i\}.
\]
The vertex \(a_i\) must be strong so that the label-\(1\) vertices of \(B\) have a strong neighbor. It cannot have label \(3\), because only one excess unit would remain to defend the zeros; hence \(f(a_i)=2\). The remaining two excess units must be a single label \(3\) in \(B\). All label-\(1\) vertices of \(B\) must be adjacent to \(a_i\), forcing \(i=1\), and the label \(3\) must dominate every zero \(a_2,\ldots,a_n\), forcing it to be \(b_n\). This is \(F_0\). The symmetric argument gives \(F_n\).

If \(|D|=n+2\), equality would give \(e(f)=2\). Zeros cannot occur on both sides. If they all lie in \(A\), then \(D\) contains all of \(B\) and two vertices of \(A\), while all excess must lie in \(B\) to defend the zeros. Consequently the label-\(1\) vertices of \(B\) have no strong neighbor in \(A\), impossible for \(n\ge4\). Thus no further equality case exists.

The graphs \(H_2\) and \(H_3\) are finite boundary cases. Exhausting all
\[
4^{2n}
\]
labelings proves the displayed complete lists, giving minimum weights \(5\) and \(7\), respectively.

## Verification
The included checker constructs \(H_n\) for
\[
2\le n\le5
\]
and enumerates every labeling in
\[
\{0,1,2,3\}^{V(H_n)}.
\]
It tests outer independence, the zero-defense rule, and the label-\(1\) support rule directly. The resulting minimum weight and complete minimum-function set are compared with the theorem.

## Relationship to prior work
Outer-independent double Roman domination was introduced in 2019. A closely following primary paper develops small-value characterizations, general bounds, complexity, corona formulas, and a complete-bipartite benchmark; its searchable full text contains no half-graph or chain-graph occurrence.

For \(m\le n\), that paper gives
\[
\gamma_{oidR}(K_{m,n})=
\begin{cases}
3,&m=1,\\
2m,&m\in\{2,3\},\\
m+4,&m\ge4.
\end{cases}
\]
Thus the large balanced complete-bipartite scalar has the same \(n+4\) form, but it does not imply the half-graph equality structure. The principal contribution here is the complete staircase classification and the exceptional boundary multiplicities.

## Limitations
The theorem classifies minimum functions rather than all feasible higher-weight functions.

The \(H_2\) and \(H_3\) lists are finite exhaustive results. The infinite-family proof begins at \(n=4\).

The finite checker through \(n=5\) is corroborative for the arbitrary-\(n\) theorem. The \(n\ge4\) result follows analytically from vertex-cover structure, excess-weight accounting, and leaf forcing.

A differently phrased or non-indexed half-graph result may exist.

## References
1. H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami, “Outer independent double Roman domination,” Applied Mathematics and Computation 364 (2020), 124617, DOI 10.1016/j.amc.2019.124617; public bibliographic record dated 16 August 2019.
2. D. A. Mojdeh, B. Samadi, Z. Shao, I. G. Yero, “Outer independent double Roman domination number of graphs,” arXiv:1909.01775v1, 20 August 2019; Bulletin of the Iranian Mathematical Society 48 (2022), 1789–1803.
