# Minimum total Roman {2}-dominating functions of crown graphs
## Finding
Let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the connected crown graph for \(n\ge3\), with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and deleted perfect matching
\[
M=\{a_i b_i:1\le i\le n\}.
\]
Then
\[
\gamma_{t\{R2\}}(\operatorname{Cr}_n)=4.
\]

Every minimum total Roman \(\{2\}\)-dominating function is obtained by choosing
\[
1\le i<j\le n
\]
and assigning
\[
f(a_i)=f(a_j)=f(b_i)=f(b_j)=1,
\]
with every other vertex labeled \(0\). Hence the exact number of minimum functions is
\[
\binom n2.
\]

## Assumptions and scope
A total Roman \(\{2\}\)-dominating function on a graph \(G\) is a map
\[
f:V(G)\to\{0,1,2\}
\]
such that every zero-labeled vertex \(v\) satisfies
\[
\sum_{u\in N(v)}f(u)\ge2,
\]
and every positive-labeled vertex has a positive-labeled neighbor. Its minimum total weight is
\[
\gamma_{t\{R2\}}(G).
\]

The theorem is stated for the standard connected crown graphs \(n\ge3\). The verifier also checks \(n=2\), where the same formula gives the unique minimum function.

## Proof
Write
\[
x_i=f(a_i),\qquad y_i=f(b_i),
\]
and
\[
X=\sum_i x_i,\qquad Y=\sum_i y_i.
\]
The positive support must meet both bipartition classes.

Suppose a feasible function had weight at most \(3\). Then one side would have total weight \(1\). By symmetry let \(X=1\). Any zero \(b_i\) would receive neighboring weight at most \(1\), so every vertex of \(B\) would have to be positive. This is impossible when \(n\ge3\) and \(Y\le2\). Therefore
\[
\gamma_{t\{R2\}}(\operatorname{Cr}_n)\ge4.
\tag{1}
\]

Choose distinct indices \(i,j\) and assign label \(1\) to
\[
a_i,a_j,b_i,b_j
\]
and \(0\) elsewhere. Every positive vertex is adjacent to the positive vertex on the opposite side with the other selected index. Every zero vertex sees both selected vertices on the opposite side. Thus the function is feasible and has weight \(4\).

For classification, a weight-\(4\) function has side weights
\[
(1,3),\quad(2,2),\quad\text{or}\quad(3,1).
\]
If \(X=1\), every \(b_i\) must be positive. If \(a_p\) is the unique positive \(A\)-vertex, then \(b_p\) is positive but is not adjacent to \(a_p\), violating totality. The case \(Y=1\) is symmetric. Hence
\[
X=Y=2.
\tag{2}
\]

If \(x_i=0\), then
\[
2-y_i=Y-y_i\ge2,
\]
so \(y_i=0\). Symmetrically,
\[
y_i=0\Longrightarrow x_i=0.
\]
Thus the two sides have the same positive support.

That common support cannot contain only one index \(p\), because then \(a_p\) and \(b_p\) are the only positive vertices and are nonadjacent. Therefore the common support has exactly two indices. By (2), all four supported labels equal \(1\). Choosing the support gives exactly
\[
\binom n2
\]
minimum functions.

## Verification
The included checker constructs \(\operatorname{Cr}_n\) for
\[
2\le n\le6.
\]
It exhausts every ternary labeling, checks the exact zero-defense and positive-support conditions, computes the minimum weight, and compares the complete minimum family with the two-common-index formula.

## Relationship to prior work
Total Roman \(\{2\}\)-domination was introduced in a 2019 primary paper that proves general inequalities, complexity results, and characterizations of extreme values. It characterizes all connected graphs with value \(3\), but does not treat crown graphs or enumerate crown optimum functions.

An independent primary study develops further bounds, complexity results, and exact path and cycle values; its searchable full text likewise contains no crown or perfect-matching-deletion result.

A 2024 survey summarizes total Roman \(\{2\}\)-domination results including general bounds, paths, cycles, Hamiltonian graphs, and later developments, without reporting a crown formula.

The scalar value \(4\) is compatible with the published characterization excluding value \(3\), but the stronger conclusion here is the complete optimum-function classification and the exact count \(\binom n2\).

## Limitations
The theorem classifies minimum functions only, not the full weight enumerator.

The exhaustive verification through \(n=6\) is corroborative only. The arbitrary-order result follows from the side-weight and matched-coordinate proof.

A differently phrased or non-indexed crown-graph treatment may exist.

## References
1. S. Cabrera García, A. Cabrera Martínez, F. A. Hernández Mira, I. G. Yero, “Total Roman \(\{2\}\)-domination in graphs,” Quaestiones Mathematicae 44 (2021), 411–434, DOI 10.2989/16073606.2019.1695230; published online 28 November 2019.
2. H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami, J. C. Valenzuela-Tripodoro, “Total Roman \(\{2\}\)-Dominating Functions in Graphs,” Discussiones Mathematicae Graph Theory 42 (2022), 937–958, DOI 10.7151/dmgt.2316.
3. A. Almulhim, B. Al Subaiei, S. R. Mondal, “Survey on Roman \(\{2\}\)-Domination,” Mathematics 12 (2024), 2771, DOI 10.3390/math12172771.
