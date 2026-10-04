# Only first-difference Whittaker–Henderson smoothing is universally range-preserving
## Finding
For integers \(n>p\ge1\) and \(\lambda>0\), let \(D_p\) be the usual \(p\)-th forward-difference matrix and define the unweighted Whittaker–Henderson smoother
\[
S_{p,\lambda}=(I+\lambda D_p^{\mathsf T}D_p)^{-1}.
\]
Thus the smoothed data are \(z=S_{p,\lambda}y\), equivalently the unique minimizer of
\[
\|z-y\|_2^2+\lambda\|D_pz\|_2^2.
\]

There is a sharp dichotomy in the difference order.

For \(p=1\), every entry of \(S_{1,\lambda}\) is strictly positive and every row sums to one. Consequently, for every data vector satisfying
\[
m\le y_i\le M,
\]
one has
\[
m\le (S_{1,\lambda}y)_i\le M
\]
for every coordinate. If the data are nonconstant, every smoothed coordinate lies strictly between the data minimum and maximum.

For every \(p\ge2\), unconditional range preservation fails for every \(\lambda>0\), already at the smallest admissible sample size
\[
n=p+1.
\]
At that size, put
\[
d_j=(-1)^{p-j}\binom pj,
\qquad 0\le j\le p,
\]
so that \(D_p\) consists of the single row \(d\). With
\[
C_p=\sum_{j=0}^p\binom pj^2=\binom{2p}{p},
\qquad
\alpha=\frac{\lambda}{1+\lambda C_p},
\]
the smoother is exactly
\[
S_{p,\lambda}=I-\alpha d^{\mathsf T}d.
\]
For the bounded monotone step data
\[
y=(0,\ldots,0,1)^{\mathsf T},
\]
the coordinate indexed by \(p-2\) is
\[
(S_{p,\lambda}y)_{p-2}
=-\alpha\binom p2<0.
\]
Thus every higher difference order produces an undershoot for every positive smoothing strength, even though the input is nonnegative and nondecreasing.

The failure persists for strictly positive, strictly increasing data. Let
\[
r=(1,2,\ldots,p+1)^{\mathsf T}
\]
and
\[
y_\varepsilon=e_p+\varepsilon r.
\]
Because \(D_pr=0\) for \(p\ge2\),
\[
S_{p,\lambda}y_\varepsilon
=S_{p,\lambda}e_p+\varepsilon r.
\]
Hence
\[
(S_{p,\lambda}y_\varepsilon)_{p-2}
=-\alpha\binom p2+\varepsilon(p-1)<0
\]
whenever
\[
0<\varepsilon<\frac{p\alpha}{2}.
\]
After division by the largest input value this gives a strictly positive, strictly increasing input in \((0,1]\) whose smoothed output is negative.

For the Hodrick–Prescott/second-difference case \(p=2\), the minimal three-point witness is especially simple:
\[
D_2=(1,-2,1),
\qquad
\alpha=\frac{\lambda}{1+6\lambda},
\]
and
\[
S_{2,\lambda}(0,0,1)^{\mathsf T}
=(-\alpha,2\alpha,1-\alpha)^{\mathsf T}.
\]
For Whittaker's third-difference order \(p=3\), the minimal four-point step gives a negative second coordinate for every \(\lambda>0\).

Therefore first differences are the unique Whittaker–Henderson order \(p\ge1\) that preserves the data range for every sample length, every positive smoothing strength, and every bounded input.

## Assumptions and scope
The result concerns the standard unweighted quadratic Whittaker–Henderson problem on equally spaced samples, with identity data-fidelity weights and the ordinary forward-difference penalty. The classification is over integer difference orders \(p\ge1\).

The positive result for \(p=1\) is stronger than monotone-data preservation: it holds for arbitrary bounded data. The negative result for \(p\ge2\) is stronger in the opposite direction: failure occurs even for strictly positive, strictly increasing data and for arbitrarily small \(\lambda>0\).

Weighted fidelity matrices, irregular grids, constrained smoothers, and modified boundary penalties can have different sign properties and are not classified here.

## Proof
For \(p=1\), the matrix
\[
L=D_1^{\mathsf T}D_1
\]
is the path-graph Laplacian. Hence
\[
A=I+\lambda L
\]
has positive diagonal entries, nonpositive off-diagonal entries, and is strictly diagonally dominant. It is therefore a nonsingular irreducible \(M\)-matrix, so
\[
A^{-1}>0
\]
entrywise. Since
\[
D_1\mathbf 1=0,
\]
one also has
\[
A\mathbf 1=\mathbf 1
\]
and therefore
\[
S_{1,\lambda}\mathbf 1=\mathbf 1.
\]
Thus every row of \(S_{1,\lambda}\) is a strictly positive probability vector. Each output coordinate is a convex combination of all input coordinates, proving range preservation and strict interiority for nonconstant data.

Now let \(p\ge2\) and take \(n=p+1\). There is only one \(p\)-th forward difference, so
\[
D_p=d.
\]
Vandermonde's identity gives
\[
dd^{\mathsf T}
=\sum_{j=0}^p\binom pj^2
=\binom{2p}{p}=C_p.
\]
The Sherman–Morrison formula therefore yields
\[
(I+\lambda d^{\mathsf T}d)^{-1}
=I-\frac{\lambda}{1+\lambda C_p}d^{\mathsf T}d
=I-\alpha d^{\mathsf T}d.
\]
Because the last component of \(d\) equals one, applying the smoother to \(e_p\) gives
\[
S_{p,\lambda}e_p=e_p-\alpha d^{\mathsf T}.
\]
The component \(p-2\) of \(d\) is
\[
d_{p-2}=\binom p2>0,
\]
so the corresponding smoothed component is strictly negative. This proves failure at the minimal admissible sample length for every \(\lambda>0\).

Finally, \(r_j=j+1\) is affine in the sample index. Every difference of order at least two annihilates affine data, so \(D_pr=0\) and hence \(S_{p,\lambda}r=r\). Adding \(\varepsilon r\) to the step witness makes the input strictly positive and strictly increasing without changing the negative contribution from the step. The displayed bound on \(\varepsilon\) is exactly the condition that the \(p-2\) coordinate remain negative.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. For first differences it constructs \(I+\lambda D_1^{\mathsf T}D_1\), inverts it by rational Gaussian elimination for several sample lengths and rational smoothing parameters, and checks strict positivity and unit row sums.

For every \(2\le p\le10\) and several rational \(\lambda\), it constructs the minimal \(n=p+1\) difference row, verifies
\[
\sum_j d_j^2=\binom{2p}{p},
\]
checks the Sherman–Morrison inverse exactly, and confirms the negative \(p-2\) coordinate for both the step witness and a strictly increasing perturbation.

The all-order conclusions are analytic consequences of the \(M\)-matrix and rank-one arguments above; the finite replay is corroborative and is not used as an exhaustive proof.

## Relationship to prior work
Whittaker's classical graduation method penalizes squared finite differences, with the original paper emphasizing third differences. Modern Whittaker–Henderson treatments write the smoother as
\[
(I+\lambda D_p^{\mathsf T}D_p)^{-1}.
\]
Those definitions and normal equations are prior work.

Explicit formulas for the order-one smoother weights have been derived in the literature. The positivity of the order-one inverse is therefore not claimed here as a new formula; it is used as one side of the order classification. Likewise, explicit finite-sample formulas for the order-two Hodrick–Prescott filter and the fact that some HP weights can be negative are prior-covered phenomena.

The claim here is the exact all-order range-preservation dichotomy: order one is the only difference order that is universally range-preserving, while every order \(p\ge2\) fails for every \(\lambda>0\) at the minimal length \(p+1\), with an explicit monotone step witness and a robust strictly increasing witness. Targeted searches under Whittaker–Henderson, Hodrick–Prescott, positive smoother, monotone data, cumulative/range preservation, negative weights, and difference-penalty terminology did not locate an implication-equivalent theorem.

## Limitations
The proof uses identity fidelity weights and a uniform-grid forward-difference penalty. General weighted Whittaker–Henderson graduation can lose the path-Laplacian \(M\)-matrix structure even at order one, so the theorem should not be transferred without a new argument.

The result classifies range preservation, not approximation quality, frequency response, or statistical optimality. A higher-order smoother may be entirely appropriate even though it is not order-preserving.

The order-one smoother-weight literature is explicit enough that its positivity may be derivable there, and the HP literature contains exact formulas with negative coefficients. The principal originality risk is therefore that an older paper on positive linear smoothers or graduation states the same cross-order dichotomy in different terminology.

## References
1. E. T. Whittaker, *On a New Method of Graduation*, Proceedings of the Edinburgh Mathematical Society 41 (1922), 63–75, DOI: 10.1017/S0013091500077853. The paper was read to the Edinburgh Mathematical Society on 14 November 1919.
2. Hiroshi Yamada and Fatima Tuj Jahra, *Explicit formulas for the smoother weights of the Whittaker–Henderson graduation of order 1*, Communications in Statistics - Theory and Methods 48 (2019), 3153–3161, DOI: 10.1080/03610926.2018.1476713.
3. Robert M. de Jong and Neslihan Sakarya, *The Econometrics of the Hodrick–Prescott Filter*, Review of Economics and Statistics 98 (2016), 310–317, DOI: 10.1162/REST_a_00523.
4. Tucker McElroy, *Exact formulas for the Hodrick–Prescott filter*, The Econometrics Journal 11 (2008), 209–217, DOI: 10.1111/j.1368-423X.2008.00230.x.
5. Larkin B. Scott and L. Ridgway Scott, *Efficient Methods for Data Smoothing*, SIAM Journal on Numerical Analysis 26 (1989), 681–692, DOI: 10.1137/0726040.
