# Euler characteristic of every tangential Segre--Veronese variety
## Finding
Let
\[
X=\operatorname{SegVer}_{(d_1,\ldots,d_k)}\!\left(\mathbb P(V_1)\times\cdots\times\mathbb P(V_k)\right)
\subset
\mathbb P\!\left(\bigotimes_{i=1}^k\operatorname{Sym}^{d_i}V_i\right),
\]
where
\[
n_i=\dim V_i\ge2,
\qquad
d_i\ge1.
\]
For each factor put
\[
a_i=
\begin{cases}
0,&d_i=1,\\[2mm]
\binom{n_i}{2},&d_i=2,\\[2mm]
n_i(n_i-1),&d_i\ge3.
\end{cases}
\]
Then the tangential variety satisfies
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\tau(X)\right)
=
\prod_{i=1}^k n_i
+
\sum_{i=1}^k a_i\prod_{j\ne i}n_j.
}
\]
Equivalently,
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\tau(X)\right)
=
\left(\prod_{i=1}^k n_i\right)
\left(
1+
\frac12\sum_{d_i=2}(n_i-1)
+
\sum_{d_i\ge3}(n_i-1)
\right).
}
\]
Hence each multidegree entry affects this Euler characteristic only through the three regimes
\[
d_i=1,
\qquad d_i=2,
\qquad d_i\ge3.
\]

## Assumptions and scope
The ground field is \(\mathbb C\), and Euler characteristic means the ordinary topological Euler characteristic of the underlying complex projective variety.

The tangential variety \(\tau(X)\) is the Zariski closure of the union of embedded projective tangent spaces to the smooth Segre--Veronese variety \(X\).

The theorem includes one-factor Veronese varieties and pure Segre varieties as boundary specializations. Those specializations are useful checks, but the new content is the uniform arbitrary-factor mixed-multidegree formula.

## Proof
Choose bases
\[
x_{i,1},\ldots,x_{i,n_i}
\]
for all factors. Choose a diagonal one-parameter subgroup whose weights on all ambient multihomogeneous monomials are pairwise distinct. Therefore every projective fixed point in the ambient space is a coordinate monomial line
\[
[M_1\otimes\cdots\otimes M_k],
\]
where each \(M_i\) is a degree-\(d_i\) monomial.

Since a tangent line is a limit of secant lines,
\[
\tau(X)\subseteq\sigma_2(X).
\]
Consequently every multigraded catalecticant flattening has rank at most two at a point of \(\tau(X)\).

For a degree-\(d\) monomial
\[
M=x_1^{\alpha_1}\cdots x_n^{\alpha_n},
\qquad
\sum_j\alpha_j=d,
\]
the rank of its order-\(e\) catalecticant is the number of exponent vectors \(\beta\) satisfying
\[
0\le\beta_j\le\alpha_j,
\qquad
\sum_j\beta_j=e.
\]
Equivalently, it is the coefficient of \(t^e\) in
\[
\prod_j(1+t+\cdots+t^{\alpha_j}).
\]
It follows immediately that the maximum catalecticant rank of a monomial is at most two exactly in the following cases:

1. \(M=x_a^d\), when the maximum rank is one;
2. \(M=x_ax_b\) with \(a<b\) when \(d=2\), when the maximum rank is two;
3. \(M=x_a^{d-1}x_b\) with \(a\ne b\) when \(d\ge3\), when the maximum rank is two.

Indeed, if the support contains at least three variables, the first catalecticant has rank at least three. If the support contains exactly two variables and both exponents are at least two, the second catalecticant contains the three independent divisor monomials of exponent patterns \((2,0)\), \((1,1)\), and \((0,2)\).

For a tensor-product monomial, a multigraded catalecticant is a tensor product of the local catalecticants, so its rank is the product of the local ranks. Thus two non-pure local factors would give a flattening of rank at least four, while one more complicated local monomial would give rank at least three. Neither can occur on \(\sigma_2(X)\).

Hence every coordinate fixed point of \(\tau(X)\) is pure in all factors except possibly one. In that exceptional factor it must be one of the rank-two monomials listed above.

Conversely, all those surviving coordinate monomials lie on \(\tau(X)\). At the coordinate point
\[
[x_{1,c_1}^{d_1}\otimes\cdots\otimes x_{k,c_k}^{d_k}],
\]
the embedded tangent space contains, for every factor \(i\), all coordinate directions obtained by replacing one copy of \(x_{i,c_i}\) by another basis vector. These are exactly
\[
x_{i,a}x_{i,b}
\]
in degree two and
\[
x_{i,a}^{d_i-1}x_{i,b}
\]
in degree at least three, with all other factors pure.

There are
\[
\prod_i n_i
\]
pure fixed points. The number of additional local tangent monomials in factor \(i\) is
\[
a_i=
0,
\quad
\binom{n_i}{2},
\quad
n_i(n_i-1)
\]
according as \(d_i=1\), \(d_i=2\), or \(d_i\ge3\). For each such local choice there are
\[
\prod_{j\ne i}n_j
\]
choices of pure monomials in the remaining factors. Therefore the fixed locus has exactly the cardinality in the stated formula.

Finally, for a complex projective algebraic variety with an algebraic \(\mathbb C^*\)-action,
\[
\chi_{\mathrm{top}}(Y)=\chi_{\mathrm{top}}(Y^{\mathbb C^*}).
\]
The fixed locus here is finite, so its Euler characteristic is its number of points, proving the formula.

## Verification
The bundled checker reconstructs all local monomials and their catalecticant ranks from exponent vectors. It verifies that the only local monomials of maximal catalecticant rank at most two are exactly the pure and near-pure monomials used in the proof.

It then checks mixed one-, two-, and three-factor parameter grids. For every tested ambient coordinate monomial it computes the product of local maximal catalecticant ranks and verifies that the rank-at-most-two criterion gives exactly the stated fixed-point count.

These finite calculations are regression evidence only. The theorem for arbitrary numbers of factors, dimensions, and multidegrees is the symbolic flattening and tangent-space argument above.

## Relationship to prior work
Ballico and Bernardi study exactly the tangential varieties of Segre--Veronese varieties. Their archival paper computes tensor rank on the tangential variety for any number of factors and studies decompositions in the two-factor case. Its inspected full text does not state an Euler-characteristic formula, and a targeted full-text search found no occurrence of “Euler.”

Earlier work on tangent developables of Segre--Veronese surfaces likewise studies tensor rank rather than the global topological invariant computed here.

Two specializations are already covered by stronger or earlier facts: for one factor and degree at least three the formula reduces to the Veronese value \(n^2\), and for pure Segre multidegree the formula reduces to the number of coordinate pure tensors. The accepted claim is the arbitrary mixed-multidegree formula and its degree-threshold behavior.

Targeted searches using “Euler characteristic,” “tangential variety,” “Segre--Veronese,” partially symmetric tensors, fixed points, and the equivalent monomial-count formulation did not locate the general formula or a stronger statement implying it.

## Limitations
Ordinary Euler characteristic is coarse. The theorem does not determine Betti numbers, intersection cohomology, mixed Hodge structure, singularities, degree, equations, or tensor-rank stratification inside the tangential variety.

The fixed-point proof is elementary once the correct multigraded flattenings are used, so an older unindexed or folklore observation remains a residual originality risk.

The statement is over \(\mathbb C\); no arithmetic or positive-characteristic analogue is asserted.

## References
Edoardo Ballico and Alessandra Bernardi, *A uniqueness result on the decompositions of a bi-homogeneous polynomial*, arXiv:1507.06083, first submitted 22 July 2015; later published in *Linear and Multilinear Algebra* 65 (2017), 677--698, DOI 10.1080/03081087.2016.1202182.

Edoardo Ballico, *On the ranks of points of tangent developables (scrolls and Segre-Veronese varieties)*, *International Journal of Pure and Applied Mathematics* 91 (2014), 381--387, DOI 10.12732/ijpam.v91i3.11.
