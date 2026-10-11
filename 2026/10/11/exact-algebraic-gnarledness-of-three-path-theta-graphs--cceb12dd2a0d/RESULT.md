# Exact algebraic gnarledness of three-path theta graphs
## Finding
Let \(X\) be a finite simplicial three-path theta graph: two branch vertices joined by three internally vertex-disjoint simple paths. Write their edge lengths in nondecreasing order as \(a\le b\le c\), and give the simplicial chain complex \(C_*^\Delta(X)\) the marked basis of oriented edges. For every subfield \(F\subset\mathbb R\),
\[
G_1^F(C_*^\Delta(X))=\max\left\{\frac{1}{a+b},\frac{2}{b+c}\right\}.
\]
Thus, with girth \(g=a+b\), one has \(G_1^F=1/g\) exactly when \(c\ge 2a+b\); for \(c<2a+b\), one has \(G_1^F=2/(b+c)>1/g\). In the equilateral case with three paths of length \(L\), the value is \(1/L=2/g\).

## Assumptions and scope
The graph is one-dimensional, finite, connected, and simplicial. The three paths share only their two endpoints. The statement concerns degree-one algebraic gnarledness in the sense of Hofmann--Löh and not geometric gnarledness. No algorithmic claim is made beyond this theta family.

Orient all three paths from the first branch vertex to the second, and let \(p_i\) be the sum of the oriented edges on the \(i\)-th path. Put
\[
x=[p_1-p_3],\qquad y=[p_2-p_3].
\]
Then \((x,y)\) is an integral basis of \(H_1(X;\mathbb Z)\).

## Proof
Fix a cointegral basis \(B\) of \(H_1(X;F)\) and a chain extension \(s\). Set \(q_i=s(p_i)\). Since each \(p_i-p_j\) is a cycle and a chain extension restricts to the canonical cycle-to-homology map,
\[
q_1-q_3=x,\qquad q_2-q_3=y.
\]
Hence there is a vector \(z\in H_1(X;F)\) with
\[
(q_1,q_2,q_3)=(z+x,z+y,z).
\]
If \(\rho=\|s\|_B\), then each path sum gives
\[
\|z+x\|_{B,1}\le a\rho,\qquad
\|z+y\|_{B,1}\le b\rho,\qquad
\|z\|_{B,1}\le c\rho.
\]
Conversely, any \(z\) satisfying these inequalities defines a chain extension by sending every edge of the \(i\)-th path to \(q_i\) divided by that path length. Indeed, a one-cycle has constant coefficient along each path, and the three path coefficients sum to zero. Therefore the optimum for the fixed basis is the weighted one-center radius
\[
R(B)=\inf_z\max\left\{\frac{\|z+x\|_{B,1}{a},\frac{\|z+y\|_{B,1}{b},\frac{\|z\|_{B,1}{c}\right\}.
\]

In dimension two, \(\ell^1\) is linearly isometric to \(\ell^\infty\) under
\[
(r,s)\longmapsto(r+s,r-s),
\]
because \(\max\{|r+s|,|r-s|\}=|r|+|s|\). Weighted \(\ell^1\)-balls therefore become axis-aligned boxes. Three such boxes have a common point exactly when they intersect pairwise, coordinate by coordinate. It follows that
\[
R(B)=\max\left\{
\frac{\|x-y\|_{B,1}{a+b},
\frac{\|x\|_{B,1}{a+c},
\frac{\|y\|_{B,1}{b+c}
\right\}.
\]
The center can be chosen over \(F\), because all endpoints and the critical radius are rational in the chosen coordinates and every subfield of \(\mathbb R\) contains \(\mathbb Q\).

Write the coordinate columns of \(x\) and \(y\) in the cointegral basis as independent integer vectors \(u,v\in\mathbb Z^2\). Conversely, every independent integer pair occurs from a cointegral \(F\)-basis: if \(A\) has columns \(u,v\), then the basis matrix obtained from \((x,y)A^{-1}\) is defined over \(F\) and contains the integral lattice in its integer span. Thus the remaining optimization is
\[
\inf_{u,v}\max\left\{
\frac{\|u-v\|_1}{a+b},
\frac{\|u\|_1}{a+c},
\frac{\|v\|_1}{b+c}
\right\},
\]
where the infimum is over independent \(u,v\in\mathbb Z^2\).

Each of \(u\), \(v\), and \(u-v\) is a nonzero integer vector, so each has \(\ell^1\)-norm at least \(1\). They cannot all have norm \(1\): two independent integral \(\ell^1\)-unit vectors lie on different coordinate axes, and their difference has norm \(2\). Hence one of the three displayed numerators is at least \(2\). The three possibilities are all attained by the unimodular pairs
\[
(e_1,e_2),\qquad(e_1+e_2,e_1),\qquad(e_1,e_1+e_2),
\]
which yield numerator triples \((2,1,1)\), \((1,2,1)\), and \((1,1,2)\), respectively. Since
\[
a+b\le a+c\le b+c,
\]
the optimal placement of the numerator \(2\) is on the largest denominator. Therefore
\[
G_1^F(C_*^\Delta(X))=\max\left\{\frac1{a+b},\frac2{b+c}\right\}.
\]
Finally, \(1/(a+b)\ge2/(b+c)\) is equivalent to \(c\ge2a+b\), giving the stated phase transition.

## Verification
The accompanying exact-arithmetic script checks the lattice lower bound, all three unimodular witness placements, the sorted-length simplification, and the weighted \(\ell^1\)-center formula through the explicit \(\ell^1_2\)-to-\(\ell^\infty_2\) isometry. It exhausts all sorted path-length triples through length \(12\) and all independent coordinate pairs in the box \([-2,2]^2\). The script is a consistency check; the proof above supplies the unbounded quantifiers.

## Relationship to prior work
Hofmann--Löh introduce algebraic gnarledness and define it through chain extensions and cointegral bases. Their Example 7.13 treats a single simplicial circle and exhibits a chain extension of norm \(1/m\) for a circle of \(m\) edges. Their paper does not state a theta-graph formula; full-text searches for “theta”, “cactus”, “graph”, and “girth” find no such result. The present calculation is rank two and depends on optimizing the cointegral basis as well as the chain extension.

A previously established cactus-graph formula gives reciprocal girth when distinct cycles are edge-disjoint. A theta graph is not a cactus: every path lies in two simple cycles. The new term \(2/(b+c)\) is therefore not implied by the cactus statement and is sometimes strictly larger than reciprocal girth. Literature on projection constants of graph cycle spaces, including work on Laakso and diamond graphs, studies a different Banach-space projection invariant and does not state this algebraic-gnarledness formula.

## Limitations
The result is specific to three-path theta graphs in degree one. It does not classify algebraic gnarledness for arbitrary rank-two graphs or arbitrary series-parallel graphs. The literature search cannot exclude an unindexed independent observation or a specialization hidden in a more general projection theorem stated in different language; no such covering implication was found in the inspected sources.

## References
1. Franziska Hofmann and Clara Löh, *Quantitative chain extensions and integral cohomological fillings*, arXiv:2610.02987v1, especially Definition 7.1 and Example 7.13.
2. Stephen J. Dilworth, Denka Kutzarova, and Mikhail I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, arXiv:2007.07949.
