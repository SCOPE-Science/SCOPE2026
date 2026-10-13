# Perfect double Italian domination of crown graphs
## Finding
Let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph for \(n\ge4\), with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad
B=\{b_1,\ldots,b_n\},
\]
and deleted perfect matching
\[
M=\{a_i b_i:1\le i\le n\}.
\]

Then
\[
\gamma_{dI}^{p}(\operatorname{Cr}_n)=6.
\]

More strongly, a function
\[
f:V(\operatorname{Cr}_n)\to\{0,1,2,3\}
\]
is a minimum perfect double Italian dominating function if and only if there is a vector
\[
z=(z_1,\ldots,z_n)\in\{0,1,2,3\}^n
\]
with
\[
\sum_{i=1}^{n}z_i=3
\]
such that
\[
f(a_i)=f(b_i)=z_i
\qquad(1\le i\le n).
\]

Hence the exact number of minimum functions is
\[
\binom{n+2}{3}.
\]

## Assumptions and scope
A perfect double Italian dominating function on a graph \(G\) is a map
\[
f:V(G)\to\{0,1,2,3\}
\]
such that every vertex \(v\) with
\[
f(v)\in\{0,1\}
\]
satisfies
\[
3\le\sum_{u\in N[v]} f(u)\le4.
\]
The minimum possible total weight is denoted by
\[
\gamma_{dI}^{p}(G).
\]

For the crown graph, write
\[
x_i=f(a_i),\qquad y_i=f(b_i),
\]
and define the side weights
\[
X=\sum_i x_i,\qquad Y=\sum_i y_i.
\]
Because \(a_i\) is adjacent to every \(b_j\) except \(b_i\), the defining inequalities become
\[
3\le x_i+Y-y_i\le4
\tag{1}
\]
whenever \(x_i\le1\), and
\[
3\le y_i+X-x_i\le4
\tag{2}
\]
whenever \(y_i\le1\).

The theorem is stated for \(n\ge4\). The boundary graph \(\operatorname{Cr}_3\cong C_6\) also has minimum weight \(6\), but has additional non-synchronized minimum functions, so the optimizer classification begins at \(n=4\).

## Proof
First, let
\[
z\in\{0,1,2,3\}^n,\qquad \sum_i z_i=3,
\]
and set
\[
x_i=y_i=z_i.
\]
If \(z_i\le1\), then the closed-neighborhood sum at either endpoint of the deleted pair is
\[
z_i+3-z_i=3.
\]
Vertices labeled \(2\) or \(3\) impose no condition. Thus every such synchronized vector is a perfect double Italian dominating function of total weight \(6\). Hence
\[
\gamma_{dI}^{p}(\operatorname{Cr}_n)\le6.
\tag{3}
\]

We prove that weight below \(6\) is impossible. Suppose
\[
X+Y\le5.
\]
By symmetry assume
\[
X\le2.
\]
Because \(n\ge4\), at least one coordinate has
\[
x_i=0.
\]

If \(X=2\), then \(Y\le3\). From (1),
\[
y_i\le Y-3\le0,
\]
so \(y_i=0\). Equation (2) then requires
\[
X\ge3,
\]
a contradiction.

If \(X=1\), then \(Y\le4\). From (1),
\[
y_i\le Y-3\le1.
\]
Therefore (2) applies, but
\[
y_i+X\le2,
\]
again contradicting its lower bound \(3\).

If \(X=0\), then every \(x_i=0\) and \(Y\le5\). If every \(y_i\ge2\), then
\[
Y\ge2n\ge8,
\]
impossible. Hence some \(y_i\le1\), and (2) gives
\[
y_i+X\le1<3.
\]
Thus no function has weight below \(6\). Together with (3),
\[
\gamma_{dI}^{p}(\operatorname{Cr}_n)=6.
\]

Now let \(f\) be any minimum function. Thus
\[
X+Y=6.
\]
We show that neither side can have weight at most \(2\).

Suppose first that \(X=2\), so \(Y=4\). If \(x_i=0\), then (1) gives
\[
y_i\le1,
\]
while (2) gives
\[
y_i+2\ge3.
\]
Hence every zero coordinate of \(x\) has
\[
y_i=1.
\]
If \(x_i=1\), then (1) and (2) force
\[
y_i=2.
\]
If \(x_i=2\), then \(y_i\le1\) would make (2) read
\[
y_i\ge3,
\]
so again
\[
y_i\ge2.
\]
Therefore every zero coordinate contributes at least \(1\) to \(Y\), and every positive coordinate contributes at least \(2\). Since \(X=2\), the positive support of \(x\) has size at least one and the number of zeros is at least \(n-2\). In either possible shape of a weight-\(2\) vector, these lower bounds give
\[
Y\ge n+1>4
\]
when there is one positive coordinate, or
\[
Y\ge n+2>4
\]
when there are two positive coordinates. This is impossible for \(n\ge4\).

If \(X=1\), then \(Y=5\). The vector \(x\) has exactly one coordinate equal to \(1\) and at least \(n-1\) zeros. At every zero coordinate, (1) gives
\[
y_i\le2.
\]
Values \(0\) and \(1\) are impossible by (2), because then
\[
y_i+1<3.
\]
Thus every such coordinate has
\[
y_i=2,
\]
and
\[
Y\ge2(n-1)\ge6,
\]
a contradiction.

If \(X=0\), then \(Y=6\), and every coordinate of \(x\) is zero. Equations (1)--(2) force every \(y_i\ge2\), so
\[
Y\ge2n\ge8,
\]
again impossible.

Hence
\[
X\ge3.
\]
By symmetry,
\[
Y\ge3.
\]
Since \(X+Y=6\),
\[
X=Y=3.
\tag{4}
\]

With (4), suppose \(x_i\le1\). Equation (1) becomes
\[
3\le x_i+3-y_i\le4,
\]
so
\[
y_i\le x_i.
\tag{5}
\]
In particular \(y_i\le1\), and then (2) gives
\[
x_i\le y_i.
\tag{6}
\]
Thus
\[
x_i=y_i
\]
whenever \(x_i\le1\). By symmetry the same conclusion holds whenever \(y_i\le1\).

Therefore, at every coordinate either
\[
x_i=y_i\le1,
\]
or both labels are at least \(2\). A side of total weight \(3\) can contain at most one coordinate with value at least \(2\). At all other coordinates the two sides already agree, and because the two side sums are equal by (4), the remaining coordinate also agrees. Hence
\[
x_i=y_i
\]
for every \(i\).

Writing this common vector as \(z\), we have
\[
z_i\in\{0,1,2,3\},
\qquad
\sum_i z_i=3.
\]
Conversely, such vectors were already shown feasible. This proves the complete classification.

Finally, the number of nonnegative integer \(n\)-tuples summing to \(3\) is
\[
\binom{n+2}{3},
\]
and the upper bound \(3\) on each coordinate is automatic for such a composition.

## Verification
The included checker independently evaluates the defining closed-neighborhood inequalities on every labeling of total weight at most \(6\) for
\[
4\le n\le10.
\]
It verifies that no labeling of weight below \(6\) is feasible and that every feasible weight-\(6\) labeling is exactly a synchronized pair of side vectors of total side weight \(3\).

## Relationship to prior work
Perfect double Italian domination was introduced in 2023. The foundational paper defines the invariant by the exact closed-neighborhood interval
\[
3\le\sum_{u\in N[v]}f(u)\le4
\]
for vertices labeled \(0\) or \(1\), establishes NP-completeness even for bipartite graphs, compares the invariant with perfect double Roman domination, and treats several standard and extremal graph families.

The crown graph is a dense regular bipartite graph obtained by deleting a perfect matching from \(K_{n,n}\). The inspected primary source does not state a crown-graph theorem, and targeted searches under both “crown graph” and “\(K_{n,n}\) minus a perfect matching” formulations did not locate an equivalent result.

The theorem above gives more than a scalar optimum: it identifies every minimum labeling through an exact synchronization law across the deleted matching and gives the closed multiplicity
\[
\binom{n+2}{3}.
\]
The synchronization is specific to the crown neighborhood identity and is not supplied by the general complexity or extremal results.

## Limitations
The theorem is restricted to balanced crown graphs with \(n\ge4\). The cycle \(\operatorname{Cr}_3\cong C_6\) has additional minimum functions.

The finite checker examines only labelings of total weight at most \(6\), which is sufficient to verify the claimed minimum and all minimizers but is not an enumeration of nonminimum feasible functions.

A differently phrased or non-indexed crown treatment may exist despite the targeted searches.

## References
1. G. Hao, P. Jalilolghadr, D. A. Mojdeh, “Perfect double Italian domination of a graph,” AKCE International Journal of Graphs and Combinatorics 20(3) (2023), 247–257, DOI 10.1080/09728600.2023.2218457; published online 21 June 2023.
