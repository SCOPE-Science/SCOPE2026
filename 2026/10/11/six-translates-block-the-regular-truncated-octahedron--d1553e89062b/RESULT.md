# Six translates block the regular truncated octahedron
## Finding
Let
\[
P=[-1,1]^3\cap
\left\{
x\in\mathbb R^3:
|x_1|+|x_2|+|x_3|\le\frac32
\right\}.
\]
This is a standard realization, up to scale, of the regular truncated octahedron: its \(24\) vertices are the signed coordinate permutations of
\[
\left(1,\frac12,0\right),
\]
its six coordinate facets are squares, and its eight sign facets are regular hexagons.

The blocking number of \(P\) satisfies
\[
b(P)\le6.
\]

Define six normalized translation vectors
\[
\begin{aligned}
z_1&=\left(-\frac58,-\frac78,0\right),&
z_2&=\left(-\frac12,\frac12,-\frac12\right),&
z_3&=\left(-\frac12,\frac12,\frac12\right),\\
z_4&=\left(\frac38,-\frac12,-\frac58\right),&
z_5&=\left(\frac38,-\frac12,\frac58\right),&
z_6&=\left(\frac78,\frac58,0\right).
\end{aligned}
\]
They satisfy
\[
z_i\in\partial P
\qquad(1\le i\le6),
\]
\[
z_i-z_j\notin\operatorname{int}P
\qquad(i\ne j),
\]
and
\[
\partial P
\subset
\bigcup_{i=1}^6
\left(\operatorname{int}P+z_i\right).
\tag{1}
\]

Consequently the six actual translation vectors
\[
u_i=2z_i
\]
give a blocking configuration
\[
P+u_1,\ldots,P+u_6
\]
for \(P\).

## Assumptions and scope
A blocking configuration for a convex body \(K\) is a finite family of pairwise nonoverlapping translates \(K+u_i\), each touching \(K\), such that every further translate touching \(K\) overlaps the interior of at least one member of the family. Here nonoverlapping means that interiors are disjoint.

For a centrally symmetric body \(K\), the standard boundary-cover characterization says that \(K+u_1,\ldots,K+u_m\) is a blocking configuration exactly when
\[
u_i\in\partial(2K),
\qquad
u_i-u_j\notin\operatorname{int}(2K)\quad(i\ne j),
\]
and
\[
\partial(2K)
\subset
\bigcup_{i=1}^m
\left(\operatorname{int}(2K)+u_i\right).
\]
Dividing all coordinates by \(2\) gives the normalized form used in (1).

The result is an upper bound. It does not prove
\[
b(P)=6.
\]
In particular, it does not use the conjectural lower bound
\[
b(K)\ge2d
\]
in dimension \(d=3\).

## Proof
The body \(P\) is centrally symmetric and has the half-space description
\[
|x_j|\le1
\quad(j=1,2,3),
\qquad
\sigma_1x_1+\sigma_2x_2+\sigma_3x_3\le\frac32
\quad
(\sigma_j\in\{-1,1\}).
\]
Its \(24\) vertices are exactly the signed coordinate permutations of
\[
\left(1,\frac12,0\right).
\]

Each displayed \(z_i\) has all coordinates of absolute value at most \(1\) and
\[
|z_{i,1}|+|z_{i,2}|+|z_{i,3}|=\frac32,
\]
so
\[
z_i\in\partial P.
\]
Thus
\[
u_i=2z_i\in\partial(2P),
\]
which means that every translate \(P+u_i\) touches \(P\).

For pairwise nonoverlap, central symmetry gives
\[
\operatorname{int}(P+u_i)\cap\operatorname{int}(P+u_j)=\varnothing
\]
whenever
\[
u_i-u_j\notin\operatorname{int}(2P).
\]
After division by \(2\), it is enough to check
\[
z_i-z_j\notin\operatorname{int}P.
\]
The supplied exact checker verifies all \(15\) differences using the defining inequalities of \(P\).

It remains to prove the boundary cover (1). The boundary has fourteen facets. Six are the coordinate facets
\[
x_j=\pm1,
\]
each with four vertices. The other eight are the sign facets
\[
\sigma_1x_1+\sigma_2x_2+\sigma_3x_3=\frac32,
\]
each with six vertices.

Every facet is triangulated from its centroid to its boundary edges. A triangle \(T\) is certified as covered by \(z_i\) when all three of its vertices satisfy the four strict inequalities
\[
|x_j-z_{i,j}|<1
\quad(j=1,2,3),
\qquad
\sum_{j=1}^3|x_j-z_{i,j}|<\frac32.
\tag{2}
\]
Because \(\operatorname{int}P+z_i\) is convex, condition (2) at the three triangle vertices implies
\[
T\subset\operatorname{int}P+z_i.
\]

If an initial facet triangle has no single certificate, it is subdivided by the three edge midpoints into four triangles, and the same test is repeated. Exact rational arithmetic terminates after at most three subdivision levels. Across all fourteen facets there are \(438\) terminal triangles. Every terminal triangle has one of the six certificates, and the least slack among all four inequalities in (2), over all certified triangle vertices, is exactly
\[
\frac1{16}>0.
\]
Since the terminal triangles partition every facet,
\[
\partial P
\subset
\bigcup_{i=1}^6
(\operatorname{int}P+z_i).
\]

The boundary-cover characterization now shows that
\[
P+2z_1,\ldots,P+2z_6
\]
is a blocking configuration. Hence
\[
b(P)\le6.
\]

## Verification
The standalone file `verify.py` uses only exact rational arithmetic for every scientific inequality.

It reconstructs the \(24\) vertices and all fourteen facets from the half-space model, checks that every facet edge has squared length
\[
\frac12,
\]
checks every \(z_i\in\partial P\), and checks all \(15\) pairwise nonoverlap conditions.

It then triangulates every facet, applies the deterministic midpoint refinement described in the proof, and verifies strict containment of every terminal triangle in one translate. The replay returns:
\[
438
\]
terminal triangles, maximum depth
\[
3,
\]
and minimum exact slack
\[
\frac1{16}.
\]

The computation is an exhaustive finite certificate for a polyhedral boundary cover; no random sampling, floating-point tolerance, grid extrapolation, or unproved infinite inference is used.

## Relationship to prior work
Dalla, Larman, Mani-Levitska, and Zong introduced the blocking-number framework, proved classical exact cases, and gave the centrally symmetric boundary-cover characterization used here. The 2009 Banach Center problem session explicitly asked for further blocking-number results.

More recent work by Wang and Zhang determines the exact blocking number of a rhombic dodecahedron and a three-dimensional cylinder and gives upper bounds for \(\ell_p\) balls. Its searchable full text organizes the results around those three classes and contains no truncated-octahedron case. Long Yu's earlier work likewise treats a three-dimensional crosspolytope, \(\ell_p\) balls, and cylinders.

The regular truncated octahedron is neither a rhombic dodecahedron nor an affine image of one: their face structures differ. Ordinary illumination results for the truncated octahedron concern a different invariant and do not imply the blocking configuration above.

Targeted searches for the exact object under the names “regular truncated octahedron,” “cube–octahedron intersection,” and “permutahedral” blocking, together with searches for six-translate boundary covers, did not locate the displayed rational configuration or an equivalent blocking theorem.

## Limitations
The argument proves only
\[
b(P)\le6.
\]
It does not exclude a blocking configuration with fewer translates.

The certificate is specialized to the regular truncated octahedron. It does not give a six-blocker theorem for arbitrary truncated octahedra, arbitrary parallelohedra, or the full cube–octahedron intersection family.

A differently phrased or unindexed older construction could exist; this is the main residual originality risk.

## References
1. L. Dalla, D. G. Larman, P. Mani-Levitska, and C. Zong, *The Blocking Numbers of Convex Bodies*, Discrete & Computational Geometry 24 (2000), 267–278. DOI: 10.1007/s004540010032.
2. *Open Problem Session*, Banach Center Publications 84 (2009), Problem 12, “Blocking numbers”.
3. L. Yu, *Blocking numbers and fixing numbers of convex bodies*, Discrete Mathematics 309 (2009), 6544–6554. DOI: 10.1016/j.disc.2009.06.034.
4. J. Wang and Y. Zhang, *On the blocking numbers of some special convex bodies*, Contributions to Discrete Mathematics 19 (2024), 209–221. DOI: 10.55016/ojs/cdm.v19i3.75983.
