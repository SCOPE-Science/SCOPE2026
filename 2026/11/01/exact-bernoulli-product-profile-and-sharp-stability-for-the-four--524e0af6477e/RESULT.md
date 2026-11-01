# Exact Bernoulli-product profile and sharp stability for the four-cube hypercube inequality

## Finding
For each \(i=1,2,3,4\), let \(0<p_i<1\) and define \(q_i=p_i(1-p_i)\). Put independent product probability weights on the vertices of the four-cube:
\[
x_v=\prod_{i=1}^{4}p_i^{v_i}(1-p_i)^{1-v_i},\qquad v\in\{0,1\}^4.
\]
For each five-element vertex set \(U\), define \(D(U)=\left|\det((1,v)_{v\in U})\right|\), its normalized four-dimensional simplex volume, and set
\[
P(x)=\sum_{|U|=5}D(U)\prod_{v\in U}x_v,\qquad R(p)=\frac{P(x)}{\prod_{i=1}^4q_i}.
\]
Write \(e_k(q)\) for the degree-\(k\) elementary symmetric polynomial in the four variances. Then the exact, four-parameter geometric volume ratio is
\[
\boxed{R(p)=1-4e_3(q)+18e_4(q).}
\]
It obeys the globally sharp quantitative bound
\[
\boxed{R(p)-\frac{105}{128}\ge\frac{23}{128}\sum_{i=1}^{4}(p_i-\tfrac12)^2.}
\]
The minimum \(105/128\) is attained uniquely at four fair Bernoulli parameters; the coefficient \(23/128\) is optimal and is approached as all four parameters tend independently to deterministic endpoints. For all interior parameter vectors, \(R(p)<1\).

## Assumptions and scope
The weights sum to one, and each pair of opposite facet masses in coordinate \(i\) is \(p_i\) and \(1-p_i\). Consequently \(\prod_F\sum_{v\in F}x_v=\prod_iq_i\), so \(R\) is exactly the normalized Hypercube ratio of Averkov--von Dichter--Soprunov for cube dimension four. The theorem concerns only independent (not necessarily identically distributed) Bernoulli vertex weights, not arbitrary sixteen nonnegative weights. At deterministic endpoints \(R\) is interpreted only via its continuous polynomial extension, since the original ratio has zero denominator.

## Proof
Let \(Y=(Y_1,\ldots,Y_4)\) have independent Bernoulli coordinates with means \(p_i\), and let \(\widetilde v=(1,v)\). The Cauchy--Binet identity applied to \(\sum_vx_v\widetilde v\widetilde v^{\mathsf T}\), followed by the Schur-complement identity, gives
\[
\sum_{|U|=5}D(U)^2\prod_{v\in U}x_v=\det\operatorname{Cov}(Y)=\prod_iq_i.
\]
Subtracting the first-power simplex-volume polynomial gives the normalized loss
\[
1-R(p)=\frac{\sum_{|U|=5}(D(U)^2-D(U))\prod_{v\in U}x_v}{\prod_iq_i}.
\]
An exhaustive exact-integer classification of the \(\binom{16}{5}=4368\) vertex sets gives normalized volumes \(D=0,1,2,3\) with multiplicities respectively \(1360,2672,320,16\). For the sets with \(D\ge2\), define a coordinate to be *unbalanced* when it has one or four vertices of binary value one (rather than two or three). The weighted sum of \(D^2-D\) over sets with zero unbalanced coordinates is exactly \(480\); with precisely the specified coordinate \(j\) unbalanced it is exactly \(64\) for each \(j\); and no contributing set has two unbalanced coordinates. The complete 4368-case exact-integer checker is bundled.

Because the sum is invariant under independently complementing cube coordinates, average every summand over these sixteen reflections. After dividing out \(q_i\), a coordinate of type two-or-three contributes \(q_i/2\); a coordinate of type one-or-four contributes \((1-3q_i)/2\). Therefore
\[
\begin{aligned}
1-R(p)&=\frac{480}{16}\prod_iq_i+\frac{64}{16}\sum_j(1-3q_j)\prod_{i\ne j}q_i\\
&=4e_3(q)-18e_4(q),
\end{aligned}
\]
which is the claimed exact profile.

For the stability inequality set \(z_i=4q_i=1-4(p_i-\tfrac12)^2\in[0,1]\). The deficit becomes
\[
G(z)=1-R=\frac1{16}e_3(z)-\frac9{128}e_4(z),\qquad G(1,1,1,1)=\frac{23}{128}.
\]
Consider the multi-affine polynomial
\[
H(z)=\frac{23}{512}\sum_i z_i-G(z).
\]
On every vertex of \([0,1]^4\) with exactly \(k\) coordinates equal to one, its value, for \(k=0,1,2,3,4\), is respectively
\[
0,\quad\frac{23}{512},\quad\frac{23}{256},\quad\frac{37}{512},\quad0.
\]
Every multi-affine polynomial on the cube is the convex multilinear interpolation of its sixteen vertex values; hence \(H(z)\ge0\) for all \(z\in[0,1]^4\). Rearranging yields the displayed sharp inequality. In the interior \(z_i>0\) the only equality point is \(z=(1,1,1,1)\), because every other contributing interpolation vertex has positive value. Thus the unique interior minimizer has \(p_i=1/2\) for all four coordinates. As all \(z_i\downarrow0\), the ratio of the stability gap to \(\sum_i(p_i-\tfrac12)^2\) tends to \(23/128\), proving sharpness of its coefficient. Finally \(G=4e_3-18e_4>0\) for all strictly positive \(q_i\le1/4\), because \(e_3\ge16e_4\), so \(R<1\).

## Verification
Run `python3 check_hypercube_bernoulli.py` with Python standard library only. It exhaustively evaluates all 4368 five-vertex sets using exact Bareiss integer determinants, verifies the exact volume counts and reflected weighted strata, checks the polynomial identity on an exact-rational grid, and certifies all sixteen multi-affine corner inequalities and equality cases. The symbolic proof above, not random samples or a timeout, establishes the inequalities over all real parameters.

## Relationship to prior work
Averkov, von Dichter and Soprunov introduced the Hypercube volume polynomial and proved its general upper bound by a covariance-determinant inequality. The existing sharp three-class symmetric-cone result establishes the value \(105/128\) at uniform weights and a bound on weights constant on the Hamming-weight orbits. It does *not* cover generic independent Bernoulli weights with four distinct biases, which are not invariant under permutation and vertex complementation. The contribution here is the entire exact nonuniform product-profile polynomial, its global minimum, and the sharp four-parameter quadratic stability term. The constant \(105/128\) at uniform weights is credited, not presented as a new value.

## Limitations
This does not strengthen the general sixteen-variable Hypercube inequality and does not classify equality for arbitrary dependent vertex measures. The coefficient \(23/128\) is approached at the boundary through positive product weights; it is not attained at a deterministic distribution where the original normalized ratio is undefined. Unindexed independent-Bernoulli simplex-volume calculations could create historical-priority overlap.

## References
Averkov, G.; von Dichter, K.; Soprunov, I., *On the Log-submodularity for zonoids: from Mixed Volume inequalities to the Hypercube*, arXiv:2608.14909 (first public version August 14, 2026), especially the Hypercube inequality and probabilistic proof in Section 7.

*Sharp symmetric gap for the first open hypercube inequality*, publicly accessible mathematical finding (October 11, 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-symmetric-gap-for-the-first-open-hypercube-inequality--4f3e013d18c9 .
