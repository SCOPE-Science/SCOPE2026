# Fractional local edge dimension of friendship graphs
## Finding
For every integer \(r\ge2\), let \(F_r\) be the friendship graph formed by \(r\) triangles sharing one common center \(c\). Write the two noncentral vertices of blade \(i\) as \(a_i,b_i\).

Then
\[
\operatorname{FLED}(F_r)=r,
\]
where \(\operatorname{FLED}\) denotes fractional local edge dimension.

More strongly, the minimum fractional local edge-resolving function is unique:
\[
g(c)=0,
\qquad
g(a_i)=g(b_i)=\frac12
\quad
(1\le i\le r).
\]

Thus, for friendship graphs with at least two blades, passing from fractional edge resolution of all edge pairs to the local version involving only adjacent edge pairs does not lower the optimum value.

## Assumptions and scope
All graphs are finite, simple, connected, and undirected.

For an edge \(e=xy\) and a vertex \(w\), write
\[
d(w,e)=\min\{d(w,x),d(w,y)\}.
\]
For two adjacent edges \(e,f\), their local edge-resolving neighborhood is
\[
R_\ell(e,f)=\{w\in V(G):d(w,e)\ne d(w,f)\}.
\]

A function
\[
g:V(G)\to[0,1]
\]
is a fractional local edge-resolving function when
\[
\sum_{w\in R_\ell(e,f)}g(w)\ge1
\]
for every pair of adjacent edges \(e,f\). The fractional local edge dimension is the minimum of
\[
\sum_{w\in V(G)}g(w)
\]
over all such functions.

The theorem is stated for \(r\ge2\). The one-blade graph is the triangle and is excluded from the claimed family statement.

## Proof
Let
\[
U=\{a_1,b_1,\ldots,a_r,b_r\}
\]
be the set of \(2r\) noncentral vertices.

First consider any two distinct vertices \(u,v\in U\). The center edges
\[
cu
\qquad\text{and}\qquad
cv
\]
are adjacent. Their local edge-resolving neighborhood is exactly
\[
R_\ell(cu,cv)=\{u,v\}.
\]

Indeed, \(u\) has distance \(0\) from \(cu\) and distance \(1\) from \(cv\), while \(v\) behaves symmetrically. The center \(c\) has distance \(0\) from both edges. Every third noncentral vertex has distance \(1\) from both center edges, because it is adjacent to \(c\).

Therefore every fractional local edge-resolving function satisfies
\[
g(u)+g(v)\ge1
\]
for every two distinct \(u,v\in U\).

Summing these inequalities over all unordered pairs in \(U\) gives
\[
(2r-1)\sum_{u\in U}g(u)\ge\binom{2r}{2}=r(2r-1),
\]
and hence
\[
\sum_{u\in U}g(u)\ge r.
\]
Since \(g(c)\ge0\), every feasible function has total weight at least \(r\).

Now define
\[
g(c)=0
\]
and
\[
g(u)=\frac12
\qquad
(u\in U).
\]
The center-edge constraints above have weight exactly \(1\).

It remains to check the other adjacent edge pairs. Inside blade \(i\), the edge \(a_i b_i\) is adjacent to both center edges. Direct distances give
\[
R_\ell(ca_i,a_i b_i)
=
\{c,b_i\}\cup\bigl(U\setminus\{a_i,b_i\}\bigr)
\]
and
\[
R_\ell(cb_i,a_i b_i)
=
\{c,a_i\}\cup\bigl(U\setminus\{a_i,b_i\}\bigr).
\]
Under the proposed function, either neighborhood has total weight
\[
\frac12+(2r-2)\frac12
=
r-\frac12
\ge1,
\]
because \(r\ge2\). Hence the function is feasible and has total weight \(r\). This proves
\[
\operatorname{FLED}(F_r)=r.
\]

Finally, suppose a feasible function has total weight \(r\). Then the lower bound above forces
\[
\sum_{u\in U}g(u)=r
\qquad\text{and}\qquad
g(c)=0.
\]
Equality in the complete system
\[
g(u)+g(v)\ge1
\]
for \(u\ne v\) forces every noncentral weight to equal \(1/2\). For example, if \(m\) is the least noncentral weight, every other noncentral weight is at least \(1-m\), and the total lower bound is strict unless \(m=1/2\); then every pair inequality forces all remaining weights to be at least \(1/2\), while their total is exactly \(r\). Thus the optimum is unique.

## Verification
The included checker constructs \(F_r\) for every
\[
2\le r\le8,
\]
computes all-pairs vertex distances, forms every adjacent-edge local resolving neighborhood directly, and solves the resulting fractional linear program.

It independently verifies the two symbolic neighborhood formulas used in the proof and checks the complete optimal face coordinate by coordinate.

## Relationship to prior work
Fractional local edge dimension was introduced in 2023 as a local relaxation of fractional edge dimension, imposing edge-resolving constraints only on adjacent edge pairs. The introducing paper gives bounds and exact values for several standard families; its abstract lists the Petersen and Coxeter graphs and families including cycles, complete graphs, wheels, grids, and complete multipartite graphs.

Friendship graphs had already been studied for the global fractional edge dimension. A 2021 paper proves
\[
\operatorname{edim}_f(F_r)=r.
\]
The theorem here shows that the local relaxation still has value \(r\) for every \(r\ge2\), and additionally determines the unique optimal fractional local weighting.

Exact searches under friendship graph, windmill graph, fractional local edge dimension, and FLED terminology did not locate a published friendship-graph computation. The full text of the introducing fractional-local paper was not accessible through the available open sources during this check; its abstract and later literature summaries list its computed families without friendship graphs. This access limitation remains an originality risk.

## Limitations
The theorem concerns fractional local edge dimension, not ordinary local edge metric dimension or global fractional edge dimension.

Only friendship graphs with at least two blades are included. The triangle boundary is deliberately excluded.

The finite linear-program computations are corroborative only. The all-\(r\) result and uniqueness follow from the symbolic local edge-resolving neighborhoods and the complete pairwise inequality system on the noncentral vertices.

A differently named or non-indexed friendship-graph result may exist, and the unavailable full text of the introducing fractional-local paper is a residual literature-access risk.

## References
1. N. Goshi, S. Zafar, T. Rashid, “Fractional local edge dimensions of a graph,” Discrete Mathematics, Algorithms and Applications, DOI 10.1142/S1793830923500246; ahead-of-print record dated 17 March 2023.
2. N. Goshi, S. Zafar, T. Rashid, J. L. G. Guirao, “A Combinatorial Approach to the Computation of the Fractional Edge Dimension of Graphs,” Mathematics 9 (2021), 2364, DOI 10.3390/math9192364.
