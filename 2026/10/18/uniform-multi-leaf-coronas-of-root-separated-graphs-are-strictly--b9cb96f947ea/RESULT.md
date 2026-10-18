# Uniform multi-leaf coronas of root-separated graphs are strictly stable

## Finding
Let \(H\) be a finite simple graph on \(n\ge1\) vertices whose independence polynomial \(I(H,z)\) has only real roots in \(( -\infty,-1/4]\). For every integer \(m\ge2\), form \(H\circ\overline{K_m}\) by adjoining \(m\) mutually nonadjacent pendant leaves to **each** vertex of \(H\). Then every zero of \(I(H\circ\overline{K_m},z)\) has strictly negative real part.

In particular the assertion holds for \(H=P_n\) (\(n\ge1\)) and \(H=C_n\) (\(n\ge3\)), with no upper bound on \(n\) or \(m\). The tree \(P_n\circ\overline{K_m}\) for \(n\ge5,m\ge2\) has at least three branching vertices and hence is not a spider. The proof also establishes the scalar criterion: for every real \(a\ge1/4\) and integer \(m\ge1\), every zero of \(z+a(1+z)^m\) lies strictly in the left half-plane.

## Assumptions and scope
All graphs are finite, simple, undirected; a pendant leaf is adjacent solely to its designated base vertex. Write \(I(G,z)=\sum_{S\subseteq V(G)\text{ independent}} z^{|S|}\), and let \(\alpha(H)\) be the maximum cardinality of an independent set in \(H\). Strict Hurwitz stability means every complex polynomial root \(\zeta\) satisfies \(\operatorname{Re}\zeta<0\). The hypothesis on \(H\) is about all complex roots (including multiplicities), not merely the smallest real root. The requirement on the leaf count is uniform over every vertex. No assertion is made for varying nonuniform leaf counts or for arbitrary stable cores without the real-root condition.

## Proof
**1. Exact corona factorization.** Independently choose an independent subset \(S\) of the base graph. A selected base vertex forbids its own leaves; each unselected base vertex admits any of its \(m\) leaves. Thus
\[
I(H\circ\overline{K_m},z)=(1+z)^{mn}I\!\left(H,\frac{z}{(1+z)^m}\right).
\]
If the roots of \(I(H,t)\) are \(-a_1,\ldots,-a_\alpha\), including multiplicity, where \(a_j\ge1/4\), then \(I(H,t)=\prod_{j=1}^{\alpha}(1+t/a_j)\), because the constant coefficient is one. Therefore the *polynomial identity*, after cancellation, is
\[
I(H\circ\overline{K_m},z)=\frac{(1+z)^{m(n-\alpha)}}{\prod_{j=1}^{\alpha}a_j}\prod_{j=1}^{\alpha}\bigl[z+a_j(1+z)^m\bigr].\tag{1}
\]
The prefactor adds only the negative root \(-1\) when \(n>\alpha\). It remains to control each scalar factor.

**2. Uniform scalar half-plane lemma.** Fix an integer \(m\ge1\) and real \(a\ge1/4\). Put \(f_{m,a}(z)=z+a(1+z)^m\). As \(a\to\infty\), the roots of the monic-normalized polynomial \((1+z)^m+z/a\) all converge to \(-1\), hence are strictly in the left half-plane for sufficiently large \(a\). Roots depend continuously on \(a>0\) as a multiset, and the degree is fixed. To show no root can leave the open left half-plane while \(a\ge1/4\), it suffices to exclude roots on the imaginary axis for these \(a\).

Clearly \(f_{m,a}(0)=a>0\). Suppose \(f_{m,a}(iy)=0\) for \(y>0\), and write \(\theta=\arctan y\in(0,\pi/2)\). The identity \(a(1+iy)^m=-iy\) yields
\[
m\theta=\frac{3\pi}{2}+2k\pi\quad\text{for an integer }k\ge0,
\qquad a=\frac{y}{(1+y^2)^{m/2}}=\sin\theta\,\cos^{m-1}\theta.\tag{2}
\]
For \(m\le3\), the angle equation has no solution. For \(m=4,5,6\), only \(k=0\) is possible, giving \(\theta=3\pi/(2m)\). If \(m=4\), then \(\theta=3\pi/8\) and \(\cos\theta<1/2\), so \(a<1/8\). If \(m=5\), then \(\theta=3\pi/10>\pi/4\), so \(a<\cos^4\theta<1/4\). If \(m=6\), \(\theta=\pi/4\) and \(a<\cos^5\theta<1/4\). Each contradicts \(a\ge1/4\).

For \(m\ge7\), independently of the phase condition, maximize the modulus expression on the right of (2) over all \(y>0\). Elementary differentiation gives
\[
\max_{y>0}\frac{y}{(1+y^2)^{m/2}}
=\frac{(m-1)^{(m-1)/2}}{m^{m/2}}
\le\sqrt{\frac{6^6}{7^7}}<\frac14.\tag{3}
\]
The bound is nonincreasing in \(m\), since for each fixed \(y>0\), the underlying function decreases in \(m\). The final strict inequality follows from \(16\cdot6^6<7^7\). This again contradicts \(a\ge1/4\). Complex conjugation excludes negative imaginary roots as well. Hence no root crosses the imaginary axis, and all roots of \(f_{m,a}\) have strictly negative real parts. Equation (1) proves the general graph assertion.

**3. Path and cycle instances.** The independence polynomial of \(P_n\) satisfies the recurrence \(I(P_n,z)=I(P_{n-1},z)+zI(P_{n-2},z)\) with \(I(P_0,z)=1\), \(I(P_1,z)=1+z\). Solving this recurrence gives all its zeros as
\[
-\frac{1}{4\cos^2(j\pi/(n+2))},\quad 1\le j\le\left\lfloor\frac{n+1}{2}\right\rfloor.
\]
The cycle polynomial is \(I(C_n,z)=I(P_{n-1},z)+zI(P_{n-3},z)\) for \(n\ge3\), and the same recurrence, with cyclic boundary conditions, gives its zeros as
\[
-\frac{1}{4\cos^2((2j-1)\pi/(2n))},\quad 1\le j\le\left\lfloor\frac n2\right\rfloor.
\]
The latter two formulas can also be verified by the characteristic roots of the path transfer matrix. Every displayed denominator is strictly less than four and positive, so each base root lies in \(( -\infty,-1/4)\). The general result applies.

## Verification
The accompanying `check.py` independently enumerates independent vertex subsets on 19 path/cycle coronas and matches the derived generating-polynomial substitution, tests exact rational Hurwitz determinants for 60 scalar polynomials of degree at most ten with \(a\ge1/4\), and checks the elementary bound \(16\cdot6^6<7^7\). An additional nonclaimed boundary diagnostic demonstrates why the root separation hypothesis has content: the four-leaf corona of a complete graph \(K_t\) is stable at \(t=19\) but not at \(t=20\), by exact quartic Hurwitz determinants. These finite checks support the algebraic identities; the infinite assertion is proved by the continuous root-crossing argument above, not inferred from enumeration.

Run from this package with `python check.py` (Python 3 and SymPy required). The script does not use any external service or hidden input.

## Relationship to prior work
Brown and Cameron (2018) introduced systematic half-plane stability constructions and proved stability for *iterated single-leaf extensions* of claw-free graphs, among other results. The operation in the present finding is different: all \(m\ge2\) pendant leaves are attached directly to each original vertex, whereas repeated one-leaf extension also attaches leaves to vertices created in earlier iterations. Hibi, Kara, and Vien (2026, Proposition 3.1) give the general independence-polynomial formula for arbitrary whiskering, and characterize symmetry and evaluations at \(-1\); the factorization's combinatorial counting is therefore not claimed as new. Zhang and Tu (2026) establish strict stability for spiders (trees with at most one branching vertex). The path-corona trees here have unboundedly many branching vertices, and the cycle-corona graphs are not trees. The claimed new content is a uniform all-multiplicity Hurwitz-stability mechanism and its infinite graph-family consequences, not the already known corona identity or the spider special cases.

## Limitations
The criterion is sufficient, not necessary, and \(1/4\) is not asserted to be the optimal scalar threshold. Uniformity of the pendant-leaf multiplicity is essential to the factorization used here. The claim makes no classification of all stable trees, all caterpillars, or all nonuniform whiskerings. While the identified primary literature addresses nearby operations, unindexed equivalent results cannot be excluded by search alone. The full text of the September 2026 spider paper was not accessible in the inspected sources; its stated theorem was compared using its abstract and verified bibliographic metadata.

## References
1. J. I. Brown and B. Cameron, *On the Stability of Independence Polynomials*, Electronic Journal of Combinatorics 25(1) (2018), P1.46; doi:10.37236/7280; arXiv:1802.02478.
2. T. Hibi, S. Kara, and D. Vien, *Independence Polynomials of Graphs*, arXiv:2603.16695v1 (first posted 2026-03-17), especially Section 3, Proposition 3.1 and Theorem 3.2.
3. L. Zhang and J. Tu, *Stability of Independence Polynomials of Spiders*, arXiv:2609.04694v1 (first posted 2026-09-04).
