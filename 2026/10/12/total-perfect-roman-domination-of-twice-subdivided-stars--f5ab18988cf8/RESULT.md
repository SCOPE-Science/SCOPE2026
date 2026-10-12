# Total perfect Roman domination of twice-subdivided stars
## Finding
For every integer \(q\ge3\), let \(T_q^{(2)}\) be the tree obtained from the star \(K_{1,q}\) by subdividing every edge twice. Write the center as \(c\), and write arm \(i\) as
\[
c-u_i-v_i-w_i,
\qquad
1\le i\le q.
\]

Then
\[
\gamma_{tR}^{p}(T_q^{(2)})=2q+3.
\]

The minimum functions admit a complete classification. Every minimum total perfect Roman dominating function satisfies
\[
f(c)=2.
\]
Exactly one arm is exceptional. Every nonexceptional arm has state
\[
(f(u_i),f(v_i),f(w_i))=(0,1,1),
\]
while the exceptional arm has exactly one of the two states
\[
(1,1,1)
\qquad\text{or}\qquad
(1,2,0).
\]
Hence the number of minimum functions is exactly
\[
2q.
\]

## Assumptions and scope
A total perfect Roman dominating function on a graph \(G\) without isolated vertices is a map
\[
f:V(G)\to\{0,1,2\}
\]
such that every vertex labeled \(0\) is adjacent to exactly one vertex labeled \(2\), and the subgraph induced by the positive-labeled vertices has no isolated vertex. Its weight is
\[
\omega(f)=\sum_{v\in V(G)}f(v),
\]
and \(\gamma_{tR}^{p}(G)\) is the minimum weight.

The theorem is stated for \(q\ge3\). The boundary \(q=2\) has
\[
\gamma_{tR}^{p}(T_2^{(2)})=7,
\]
equal to its order, and has additional minimum-function types.

The phrase “twice-subdivided star” means that every original edge of \(K_{1,q}\) is subdivided exactly twice. This is distinct from the “subdivided star” convention in the initiating total-perfect-Roman paper, where every star edge is subdivided exactly once.

## Proof
First observe that
\[
f(v_i)>0
\tag{1}
\]
for every arm \(i\). Indeed, if \(f(v_i)=0\) and \(f(w_i)=0\), then the leaf \(w_i\) has no neighbor labeled \(2\), while if \(f(v_i)=0\) and \(f(w_i)>0\), then \(w_i\) is isolated in the positive support. Both possibilities contradict the definition.

We split according to the label of the center.

### Case \(f(c)=0\)

The zero center must have exactly one neighbor labeled \(2\). Hence exactly one of the vertices \(u_i\) has label \(2\).

Consider an arm with \(f(u_i)=0\). Since \(c\) is not labeled \(2\), the zero vertex \(u_i\) forces
\[
f(v_i)=2.
\]
Because \(u_i=0\), the positive vertex \(v_i\) needs a positive neighbor \(w_i\). Thus this arm has weight at least \(3\).

Consider an arm with \(f(u_i)>0\). By (1), \(v_i>0\). If \(w_i=0\), then the leaf condition forces \(v_i=2\); if \(w_i>0\), the three positive entries already contribute at least \(3\). Thus every such arm has weight at least \(3\), except that the unique arm with \(u_i=2\) has weight at least \(4\). Therefore
\[
\omega(f)\ge4+3(q-1)=3q+1.
\tag{2}
\]

### Case \(f(c)=1\)

Every arm has weight at least \(3\). If \(u_i=0\), then the zero condition at \(u_i\) forces \(v_i=2\), and \(v_i\) needs \(w_i>0\) to avoid being isolated in the positive support. If \(u_i>0\), then \(v_i>0\) by (1), and either \(w_i=0\), which forces \(v_i=2\), or \(w_i>0\). In every case the arm contributes at least \(3\). Hence
\[
\omega(f)\ge1+3q.
\tag{3}
\]

### Case \(f(c)=2\)

If \(u_i=0\), then \(u_i\) already has the center as one label-\(2\) neighbor. Therefore \(v_i\ne2\). By (1),
\[
f(v_i)=1.
\]
Since \(u_i=0\), the vertex \(v_i\) needs \(w_i>0\) in the positive support. Thus an arm with \(u_i=0\) has weight at least \(2\), with equality only at
\[
(0,1,1).
\tag{4}
\]

If \(u_i>0\), then the arm has weight at least \(3\): when \(w_i=0\), the leaf condition forces \(v_i=2\); when \(w_i>0\), the three positive entries contribute at least \(3\).

The positive center must itself have a positive neighbor, so at least one \(u_i\) is positive. Therefore
\[
\omega(f)\ge2+3+2(q-1)=2q+3.
\tag{5}
\]

For \(q\ge3\), the bounds in (2) and (3) are strictly larger than (5), since
\[
3q+1>2q+3
\quad\text{and}\quad
3q+1>2q+3.
\]
Hence every minimum function has \(f(c)=2\).

To attain equality in (5), exactly one arm has \(u_i>0\), all other arms have the unique weight-\(2\) state in (4), and the exceptional arm must have total weight \(3\). Its positive \(u_i\) must be \(1\). If \(w_i=0\), then \(v_i=2\), giving
\[
(1,2,0).
\]
If \(w_i>0\), weight \(3\) forces
\[
(1,1,1).
\]
Both states satisfy the defining conditions.

Thus the minimum weight is \(2q+3\), and the unique exceptional arm can be chosen in \(q\) ways and in either of two states. Hence there are
\[
2q
\]
minimum functions.

## Verification
The included checker constructs \(T_q^{(2)}\) directly and tests the definition vertex by vertex.

It exhaustively checks every labeling for
\[
q=2,3,4,
\]
a total of
\[
3^7+3^{10}+3^{13}=1{,}655{,}559
\]
labelings. It obtains
\[
\gamma_{tR}^{p}(T_2^{(2)})=7,
\qquad
\gamma_{tR}^{p}(T_3^{(2)})=9,
\qquad
\gamma_{tR}^{p}(T_4^{(2)})=11.
\]
For \(q=3\) and \(q=4\), every minimum function is one of the stated \(2q\) functions.

The checker also constructs and directly validates all stated minimum functions for every
\[
3\le q\le50.
\]

## Relationship to prior work
The 2023 initiating paper defines total perfect Roman domination exactly as used here. It proves the universal upper bound
\[
\gamma_{tR}^{p}(G)\le |V(G)|
\]
for connected graphs without isolated vertices and characterizes equality. In particular, it explicitly defines a “subdivided star” as a star in which every edge is subdivided exactly once, and that once-subdivided family belongs to the equality class
\[
\gamma_{tR}^{p}(G)=|V(G)|.
\]

The present family is the next uniform subdivision step: every star edge is subdivided twice. Its order is
\[
3q+1,
\]
but for \(q\ge3\) the theorem gives
\[
\gamma_{tR}^{p}(T_q^{(2)})=2q+3,
\]
so the second subdivision creates an exact gap
\[
(3q+1)-(2q+3)=q-2
\]
from the extremal order bound. The initiating paper also proves
\[
\gamma_{tR}^{p}(G)\le3\gamma^{p}(G)
\]
and characterizes trees attaining equality, but those statements do not imply the exact value or the two-state minimum-function classification for \(T_q^{(2)}\).

Targeted literature searches under “twice-subdivided star,” “balanced spider,” “spider,” and total-perfect-Roman terminology did not locate an exact treatment of this repeated-subdivision family.

## Limitations
The theorem concerns uniform arm length \(3\): exactly two subdivisions on every edge of a star. It does not determine total perfect Roman domination for arbitrary spiders or for three or more uniform subdivisions.

The boundary \(q=2\) has additional minimum-function types and is excluded from the structural theorem.

Finite exhaustive computation is corroborative only. The arbitrary-\(q\) theorem follows from the three center-label cases and the local arm lower bounds.

A differently phrased or non-indexed treatment of this exact repeated-subdivision family may exist.

## References
1. A. Almulhim, “Total Perfect Roman Domination,” Symmetry 15(9) (2023), 1676, DOI 10.3390/sym15091676; published 31 August 2023.
2. H. Abdollahzadeh Ahangar, M. A. Henning, V. Samodivkin, I. G. Yero, “Total Roman domination in graphs,” Applicable Analysis and Discrete Mathematics 10(2) (2016), 501–517, DOI 10.2298/AADM160802017A.
