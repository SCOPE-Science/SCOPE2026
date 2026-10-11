# Complete-graph fractional stable-set polytopes have a sharp seven-dimensional sphere transition
## Finding
For every integer \(n\ge3\), the fractional stable-set polytope of the clique \(K_n\) is
\[
F_n=\operatorname{FRAC}(K_n)
=\{x\in\mathbb R^n:x_i\ge0,\ x_i+x_j\le1\text{ whenever }1\le i<j\le n\}.
\tag{1}
\]
Its vertices are exactly
\[
0,\quad e_1,\ldots,e_n,\quad
\frac12\mathbf1_S\quad(S\subseteq[n],\ |S|\ge3).
\tag{2}
\]
Here \(\mathbf1_S\) denotes the indicator of the subset \(S\).

The unique minimum enclosing Euclidean ball of \(F_n\) has center
\[
c_n=t_n\mathbf1,
\qquad
t_n=\begin{cases}
\dfrac1n,&3\le n\le6,\\[3pt]
\dfrac{n-4}{4(n-2)},&n\ge7,
\end{cases}
\tag{3}
\]
and squared radius
\[
\boxed{R_n^2=\begin{cases}
1-\dfrac1n,&3\le n\le6,\\[5pt]
\dfrac{n^3}{16(n-2)^2},&n\ge7.
\end{cases}}
\tag{4}
\]

When \(3\le n\le6\), **exactly the unit vectors** \(e_1,\ldots,e_n\) are sphere contacts. When \(n\ge7\), **exactly the unit vectors and the full-half vertex**
\[
h=\frac12\mathbf1
\tag{5}
\]
are contacts. The other half-integral vertices in (2) and the origin lie strictly inside the ball in both regimes.

The true stable-set polytope of the complete graph is the regular-coordinate simplex
\[
\operatorname{STAB}(K_n)=\operatorname{conv}(0,e_1,\ldots,e_n).
\tag{6}
\]
Its unique minimum enclosing center is \(\mathbf1/n\), with squared radius \(1-1/n\). Thus the relaxation gap in **squared** minimum-enclosing radius is
\[
\boxed{
R_n^2-R_{\operatorname{STAB}(K_n)}^2
=\begin{cases}
0,&3\le n\le6,\\[3pt]
\dfrac{(n^2-8n+8)^2}{16n(n-2)^2},&n\ge7.
\end{cases}}
\tag{7}
\]
It starts at \(1/2800\) when \(n=7\), and is positive and increasing in its leading order thereafter. More precisely,
\[
R_n\sim\frac{\sqrt n}{4}
\qquad(n\longrightarrow\infty),
\qquad
R_{\operatorname{STAB}(K_n)}\longrightarrow1.
\tag{8}
\]
The dimension-seven transition marks the first time a genuinely fractional vertex is required to support the minimum enclosing sphere of this canonical edge-relaxation polytope.

## Assumptions and scope
The metric is the standard Euclidean metric of \(\mathbb R^n\). The inequality system (1) is the *edge relaxation* of the clique stable-set polytope, not the stronger clique-inequality relaxation \(\sum_i x_i\le1\). In particular, the all-half vector (5) is feasible because every pair of its coordinates sums to exactly one.

This is the fractional stable-set polytope as defined in the polyhedral combinatorics literature. Kafer, Pashkovich, and Sanità study its circuit diameter, while Hamano, Hibi, and Ohsugi give a precise half-integral vertex criterion that applies to (1). The latter source predates the focal circuit-geometry study and is used only to support the exact vertex structure.

The parameter \(n\ge3\) is essential for the fractional half-support vertices to occur. The smallest member \(n=3\) is also the triangle-cycle fractional stable-set example, but the general transition at \(n=7\) involves a different graph family and is not implied by cycle-specific radius formulas.

## Proof
### 1. Complete vertex set
The defining inequalities yield \(0\le x_i\le1\). The polytope is a vertex-packing relaxation, whose vertices are half-integral. A standard vertex criterion asserts that for a fractional half-integral vertex the subgraph induced by its coordinates equal to \(1/2\) has each connected component containing an odd cycle (Hamano--Hibi--Ohsugi, Lemma 2.2).

For the clique \(K_n\), a nonempty half-support meets this condition precisely when it contains at least three vertices. Conversely, every half vector \(\mathbf1_S/2\) for \(|S|\ge3\) is a vertex: coordinates outside \(S\) are pinned to zero, and the three pairwise tight edge equalities on a triangle inside \(S\), combined with the remaining tight equalities in the clique, force every coordinate in \(S\) to equal \(1/2\).

An integral feasible vertex can have at most one coordinate equal to one, so it is either \(0\) or some \(e_i\). This proves (2). This conclusion can also be checked directly by considering the graph of tight pair inequalities: a connected bipartite component permits a small alternating perturbation, while a nonbipartite component forces all its coordinates to \(1/2\).

### 2. Reduction to one scalar
Every compact Euclidean set has a unique minimum-enclosing-ball center. Since the symmetric group \(S_n\) acts isometrically on \(F_n\) by permuting coordinates, that center must be a fixed point of the entire group, hence \(t\mathbf1\) for some real \(t\).

The squared distances from this center to the three kinds of vertices are
\[
D_0(t)=nt^2,
\qquad
D_1(t)=nt^2+1-2t,
\tag{9}
\]
and, for the half-support vertices of cardinality \(k\),
\[
D_{k/2}(t)=nt^2+k\left(\frac14-t\right)
\qquad(3\le k\le n).
\tag{10}
\]
The full-half vector has distance
\[
D_h(t)=n\left(\frac12-t\right)^2.
\tag{11}
\]

### 3. The two candidate centers and the transition
Consider first the unit-vector simplex \(\operatorname{conv}(e_1,\ldots,e_n)\). Its minimum-enclosing center is
\[
c_0=\frac1n\mathbf1,
\qquad
R_0^2=1-\frac1n.
\tag{12}
\]
Indeed, every unit vector has the same distance, and their barycenter is \(c_0\). Consequently every ball containing \(F_n\) has radius at least \(R_0\).

At \(t=1/n\), the half-support distance (10) is affine in \(k\). For \(n=3\), the only allowed cardinality is \(k=3\), and direct substitution shows strict interiority. For \(n\ge4\), the coefficient \(1/4-1/n\) is nonnegative, so the largest half-support distance occurs at \(k=n\). Hence this simplex ball contains *all* vertices exactly when
\[
n\left(\frac12-\frac1n\right)^2\le1-\frac1n.
\tag{13}
\]
After multiplying by \(4n\), the difference between the two sides has sign equal to that of
\[
n^2-8n+8.
\tag{14}
\]
The expression (14) is negative for \(3\le n\le6\) and positive for all \(n\ge7\). Thus the simplex ball is the minimum enclosing ball for \(3\le n\le6\), and all fractional vertices are strictly inside it. Its optimal center is unique by the unit-vector barycenter identity below.

For \(n\ge7\), the simplex ball no longer contains \(h\). To balance the distances to the unit vectors and to \(h\), solve
\[
D_1(t)=D_h(t).
\tag{15}
\]
Using (9) and (11), equality is equivalent to
\[
1-2t=\frac n4-nt,
\]
which has the unique solution
\[
t=t_n=\frac{n-4}{4(n-2)}.
\tag{16}
\]
It satisfies \(0<t_n<1/4\). Therefore the right side of (10) is strictly increasing with \(k\); among fractional vertices, only the full-half vector \(h\) is farthest. Also, \(D_0(t_n)<D_1(t_n)\), because \(1-2t_n>0\).

Substituting (16) into (11) gives
\[
R_n^2=n\left(\frac12-t_n\right)^2
=\frac{n^3}{16(n-2)^2}.
\tag{17}
\]
Equations (10), (16), and (17) show that the ball centered at \(c_n=t_n\mathbf1\) contains all vertices of \(F_n\) and has exactly the asserted contacts.

### 4. Global minimality and uniqueness
For \(3\le n\le6\), the center is
\[
c_n=\frac1n\sum_{i=1}^n e_i,
\tag{18}
\]
a convex combination of equal-radius contact points.

For \(n\ge7\), set
\[
a_n=\frac{n}{2(n-2)^2},
\qquad
b_n=\frac{n^2-8n+8}{2(n-2)^2}.
\tag{19}
\]
Both coefficients are strictly positive. They satisfy
\[
na_n+b_n=1,
\qquad
a_n+\frac{b_n}{2}=t_n.
\tag{20}
\]
Thus the proposed center is again a strict convex combination of equal-radius contacts:
\[
c_n=a_n\sum_{i=1}^n e_i+b_n h.
\tag{21}
\]

For either regime, write the contact representation as \(c_n=\sum_v\lambda_v v\), with \(\lambda_v\ge0\), \(\sum_v\lambda_v=1\), and \(\|v-c_n\|^2=R_n^2\). For any proposed alternative center \(y\in\mathbb R^n\), expansion of squares gives the exact identity
\[
\sum_v\lambda_v\|v-y\|^2
=R_n^2+\|y-c_n\|^2.
\tag{22}
\]
Hence at least one contact satisfies \(\|v-y\|^2\ge R_n^2+\|y-c_n\|^2\). No smaller ball exists, and equality in the minimum radius is possible only at \(y=c_n\). This proves global minimality and uniqueness in all dimensions, independently of a numerical optimization method.

### 5. Comparison with integral stable sets
The stable sets of a clique are precisely the empty set and the singletons, so the integral polytope is (6). The ball (12) contains every vertex of that simplex, and the contact barycenter (18) proves it is minimal and unique. Subtracting its squared radius from (17), then simplifying, gives
\[
\frac{n^3}{16(n-2)^2}-\frac{n-1}{n}
=\frac{(n^2-8n+8)^2}{16n(n-2)^2}
\tag{23}
\]
for \(n\ge7\). This is strictly positive and yields the exact gap (7). The asymptotics (8) are immediate from (17).

## Verification
The proof is symbolic for all integers \(n\ge3\). The graph-theoretic half-integrality and odd-cycle-support criterion used in Step 1 is explicitly stated in Hamano--Hibi--Ohsugi; the circuit-diameter primary literature defines the identical edge-relaxation polytope. Both inspected sources address, respectively, arithmetic and circuit geometry, not a Euclidean smallest-sphere computation.

`verify.py` independently constructs and checks the full vertex set for \(3\le n\le12\), verifies both sphere formulas and all contact layers, checks exact barycentric identities with rational arithmetic, and for \(3\le n\le8\) independently solves a full-dimensional minimum-enclosing-ball optimization over all listed vertices. Finite checks corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work
Kafer, Pashkovich, and Sanità study the circuit diameter of classical combinatorial optimization polytopes and explicitly include the fractional stable-set polytope. They do not evaluate Euclidean minimum enclosing spheres or classify sphere contacts.

Hamano, Hibi, and Ohsugi study Ehrhart series of fractional stable-set polytopes. Their Lemma 2.2 gives the half-integral odd-cycle-support vertex criterion needed in Step 1, but the paper's stated results concern Ehrhart and Gorenstein structures, not Euclidean enclosure.

The triangle case satisfies \(K_3=C_3\), so its fractional stable-set polytope can equally be regarded as a cycle-graph example. For \(n\ge4\), complete graphs and cycles have different edge systems and different half-support vertex structures; a cycle-specific argument does not itself determine this complete-graph transition.

The canonical integer stable-set simplex and its centered sphere provide a natural comparison: the edge relaxation remains metrically harmless for dimension at most six, but creates an increasingly large outer-radius gap from dimension seven onward. The contact-barycenter weights (19)--(21) identify the exact mechanism of that change.

## Limitations
The theorem is specific to the standard edge-relaxation \(\operatorname{FRAC}(K_n)\) with its ordinary Euclidean metric. It is not a claim about the clique-inequality relaxation, general graph fractional stable-set polytopes, their inscribed balls, or arbitrary affine images.

Only the outer minimum-enclosing sphere and its contacts are determined. No new Ehrhart, circuit-diameter, or lattice-point result is claimed. A general convex-hull-of-simplex-plus-half-supports theorem under other terminology could cover the metric formulas; no such exact comparison was located in the inspected literature.

## References
1. Sean Kafer, Kanstantsin Pashkovich, and Laura Sanità, *On the Circuit Diameter of Some Combinatorial Polytopes*, arXiv:1709.09642, first public version 2017-09-27; *SIAM Journal on Discrete Mathematics* 33(1) (2019), 1--25, DOI 10.1137/17M1152115.
2. Ginji Hamano, Takayuki Hibi, and Hidefumi Ohsugi, *Ehrhart series of fractional stable set polytopes of finite graphs*, arXiv:1603.09613, first public version 2016-03-31; *Annals of Combinatorics* 22 (2018), 563--573, DOI 10.1007/s00026-018-0392-2.
