# Weight enumerator of total double Roman functions on friendship graphs
## Finding
For every integer \(r\ge2\), let \(F_r\) be the friendship graph formed from \(r\) triangles sharing one common center \(c\). Write the noncentral vertices of triangle \(i\) as \(a_i,b_i\).

Define
\[
P(z)=1+z+z^2+z^3,
\]
\[
Q_2(z)=3z^2+4z^3+3z^4+2z^5+z^6,
\]
\[
Q_1(z)=4z^3+3z^4+2z^5+z^6,
\]
and
\[
Q_0(z)=2z^3+3z^4+2z^5+z^6.
\]

If \(T_r(z)\) denotes the weight enumerator of all total double Roman dominating functions on \(F_r\), then
\[
T_r(z)
=
z^3\bigl(P(z)^{2r}-1\bigr)
+z^2Q_2(z)^r
+zQ_1(z)^r
+Q_0(z)^r.
\]

In particular, the total number of such functions is
\[
T_r(1)=16^r-1+13^r+10^r+8^r.
\]
Moreover,
\[
\gamma_{tdR}(F_r)=4,
\]
and there are exactly \(2r\) minimum functions. Each minimum function labels the center by \(3\), exactly one noncentral vertex by \(1\), and every other noncentral vertex by \(0\).

## Assumptions and scope
All graphs are finite, simple, connected, and undirected. A total double Roman dominating function is a map
\[
f:V(G)\longrightarrow\{0,1,2,3\}
\]
such that every vertex labeled \(0\) has either a neighbor labeled \(3\) or at least two neighbors labeled \(2\), every vertex labeled \(1\) has a neighbor labeled at least \(2\), and the subgraph induced by the positive-labeled vertices has no isolated vertex. Its weight is
\[
w(f)=\sum_{v\in V(G)}f(v).
\]
The total double Roman domination number is the minimum weight.

The theorem covers friendship graphs \(F_r\) with \(r\ge2\). The single-triangle case \(F_1=K_3\) is excluded because one step of the center-zero argument uses two distinct pages.

## Proof
The proof partitions all functions according to the label of the common center \(c\). Once \(f(c)\) is fixed, distinct triangle pages are independent, so each case is encoded by one page polynomial.

Suppose first that
\[
f(c)=3.
\]
Every noncentral label in \(\{0,1,2,3\}\) satisfies the double Roman defense conditions because each noncentral vertex is adjacent to \(c\). The positive-support condition fails only when every noncentral vertex has label \(0\), because then the positive support is the isolated vertex \(c\). Thus the contribution is
\[
z^3\bigl(P(z)^{2r}-1\bigr).
\]

Now suppose
\[
f(c)=2.
\]
On one page with ordered labels \((f(a_i),f(b_i))\), the only forbidden pairs are
\[
(0,0),\qquad (0,1),\qquad (1,0).
\]
Indeed, a zero already sees one label \(2\) at the center and therefore needs its page mate to be labeled \(2\) or \(3\), while a label \(1\) is automatically defended by the center. Every allowed page has a positive noncentral vertex, so the positive support has no isolated vertex. Hence the page polynomial is
\[
Q_2(z)=P(z)^2-1-2z
=3z^2+4z^3+3z^4+2z^5+z^6,
\]
and this center state contributes
\[
z^2Q_2(z)^r.
\]

Suppose next that
\[
f(c)=1.
\]
A noncentral zero must have its mate labeled \(3\), and a noncentral vertex labeled \(1\) must have its mate labeled \(2\) or \(3\). Thus the valid ordered page pairs are
\[
(0,3),(3,0),(1,2),(2,1),(1,3),(3,1),(2,2),(2,3),(3,2),(3,3).
\]
Their weight polynomial is
\[
Q_1(z)=4z^3+3z^4+2z^5+z^6.
\]
Every valid page contains a vertex labeled at least \(2\), which both defends the center and attaches the positive page vertices to it. Hence this center state contributes
\[
zQ_1(z)^r.
\]

Finally suppose
\[
f(c)=0.
\]
Because the center is not in the positive support and different pages have no edges between them, the positive-support condition forces both vertices on every page to be positive. A page labeled \((1,1)\) is forbidden because neither label \(1\) has a neighbor labeled at least \(2\). Every other pair in \(\{1,2,3\}^2\) is valid, giving
\[
Q_0(z)=(z+z^2+z^3)^2-z^2
=2z^3+3z^4+2z^5+z^6.
\]
It remains to check the center itself. If any noncentral vertex has label \(3\), the center is defended. Otherwise, each page contains a label \(2\), because \((1,1)\) is forbidden; since \(r\ge2\), the center then has at least two neighbors labeled \(2\). Hence the center-zero contribution is
\[
Q_0(z)^r.
\]

Summing the four disjoint center states proves the enumerator.

Evaluating at \(z=1\) gives
\[
T_r(1)=16^r-1+13^r+10^r+8^r.
\]
The least degree in the center-three term is \(4\), obtained by placing label \(1\) on exactly one noncentral vertex. The other three terms have least degrees at least \(6\) when \(r\ge2\). Therefore the minimum weight is \(4\), and its coefficient is exactly \(2r\), with the stated minimum-function classification.

## Verification
The included checker constructs \(F_r\) directly and tests every labeling in \(\{0,1,2,3\}^{V(F_r)}\) against the defining conditions. It does not use the center-state theorem to decide feasibility.

For \(r=2,3,4\), it checks every weight coefficient against the closed formula, the minimum value, the number and form of minimum functions, and the total number of feasible functions.

## Relationship to prior work
Total double Roman domination was introduced in 2019 as a strengthening of double Roman domination obtained by requiring the positive support to have no isolated vertex. The early theory proves general bounds and characterizes several extremal values. In particular, a published general result already yields total double Roman domination number \(4\) for graphs with a universal vertex, so the scalar equality \(\gamma_{tdR}(F_r)=4\) is prior-implied and is not the originality basis here.

The 2019 primary sources inspected for the parameter do not give a friendship-graph or windmill-graph all-function enumeration in their searchable text. Targeted searches under total double Roman, friendship, windmill, polynomial, and weight-enumerator terminology likewise did not locate a theorem equivalent to the displayed formula.

The new content is the exact structural partition of every feasible function by the center label, the four resulting page polynomials, the full weight distribution, the total function count, and the complete classification and count of minimum functions.

## Limitations
The theorem is restricted to friendship graphs with at least two triangles. The case \(F_1=K_3\) is not included. The scalar minimum value \(4\) is already implied by prior general theory; the refinement claimed here is enumerative and structural.

The exhaustive computation for \(2\le r\le4\) is corroborative only. The all-parameter theorem follows from the page-by-page proof. Search coverage cannot exclude a differently phrased or non-indexed enumeration.

An earlier 2019 paper on the parameter was located with month-level public-date evidence, but an exact public day was not verified in this run. The exact date used for metadata is therefore the independently verified online publication date of the second 2019 primary paper rather than an invented day for the earlier source.

## References
1. Z. Shao, N. Amjadi, S. M. Sheikholeslami, M. Valinavaz, “On the Total Double Roman Domination,” IEEE Access 7 (2019), 52035–52041, DOI 10.1109/ACCESS.2019.2911659.
2. G. Hao, L. Volkmann, D. A. Mojdeh, “Total double Roman domination in graphs,” Communications in Combinatorics and Optimization 5 (2020), 27–39, DOI 10.22049/cco.2019.26484.1118; published online 16 July 2019.
