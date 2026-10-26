# Sharp BV perturbation threshold for cyclic three-point medians

## Finding

Fix an integer \(n\ge3\). For a real signal \(x=(x_j)_{j\in\mathbb Z/n\mathbb Z}\), define the periodic three-point running median
\[
(T_nx)_j=\operatorname{median}(x_{j-1},x_j,x_{j+1})
\]
and the cyclic total-variation seminorm
\[
V_n(x)=\sum_{j\in\mathbb Z/n\mathbb Z}|x_{j+1}-x_j|.
\]
Its sharp **two-input** variation-Lipschitz modulus, with the ratio taken only where \(V_n(x-y)>0\), is
\[
\boxed{\sup_{V_n(x-y)>0}\frac{V_n(T_nx-T_ny)}{V_n(x-y)}=
\begin{cases}0,&n=3,\\2,&n=4,5,\\3,&n\ge6.\end{cases}}
\]
For every \(n\ge4\), equality is attained by distinct real signals with different total variation. In contrast, the **one-input** bound \(V_n(T_nx)\le V_n(x)\) holds for all \(n\ge3\) and all real \(x\). Thus a variation-decreasing median filter can amplify variation of differences by the sharp factor three, with the first saturation at six cyclic samples.

## Assumptions and scope

All signals are real-valued, indexed by the finite undirected cycle with its standard cyclic order and unit edge weights. The three-point median has no ties on open strict-order chambers; it is continuous on all data, including ties. All seminorm statements are modulo additive constants. The assertion is for one filtering pass, not iterated or recursively defined median filters. No statistical noise assumptions are imposed.

## Proof

**1. Reduction to finitely many selectors.** On any strict-order chamber, each median output is exactly one of its three inputs, so there is a matrix \(P\) with one entry \(1\) per row, all others zero, and \((T_nx)_j=x_{s(j)}\) for some \(s(j)\in\{j-1,j,j+1\}\). Every selector satisfies \(P\mathbf1=\mathbf1\). Because \(T_n\) is continuous and piecewise linear, the global seminorm-Lipschitz modulus is at most the largest variation-seminorm operator norm among its strict-chamber selectors. This follows by cutting the segment between two data vectors into the finitely many linear pieces, and extending the resulting inequality by continuity when a segment has persistent ties. Conversely, every strict-chamber selector norm is attainable in the Lipschitz supremum: choose an interior base signal and a sufficiently small perturbation in any prescribed direction.

**2. Arc reduction for the cyclic variation ball.** Let \(P\) be any matrix of the preceding kind. For nonconstant \(h\), write its cyclic difference vector \(d_j=h_{j+1}-h_j\), which has zero sum. Its positive and negative parts have equal mass \(V_n(h)/2\). Transporting the positive mass to the negative mass decomposes \(d\) into a nonnegative combination of elementary vectors \(e_p-e_q\), of total coefficient \(V_n(h)/2\). Each such elementary vector is the cyclic difference of the indicator of a nonempty proper consecutive vertex arc \(I\); that indicator has variation \(2\). Because \(P\) preserves constants, the triangle inequality therefore gives
\[
\frac{V_n(Ph)}{V_n(h)}\le\max_{I\text{ proper cyclic arc}}\frac{V_n(P\mathbf1_I)}{2}.
\]
Equality after maximizing over \(h\) holds because each arc indicator is itself admissible. The right side is the maximum number of cyclic connected components of the Boolean set \(\{j:s(j)\in I\}\).

**3. Universal three-component bound.** Write \(R=\{j:s(j)\in I\}\). Since \(s(j)\in\{j-1,j,j+1\}\), the Boolean output is forced to be \(1\) at every vertex in \(I\) other than its first and last vertices, and is forced to be \(0\) at every vertex in the complementary arc other than its first and last vertices. When both arcs have at least three vertices, these forced runs, together with the four potentially ambiguous boundary vertices, permit at most three connected components of \(R\). If either arc has at most two vertices, the support of \(R\), or of its complement, lies in a consecutive run of at most four vertices. A binary run supported in four consecutive positions has at most two connected components; equivalently the same is true of the opposite symbol on the circle. Thus the maximum is always at most three. For \(n=4,5\), any Boolean set on the cycle has at most \(\lfloor n/2\rfloor=2\) connected components. For \(n=3\), every filtering window is the entire vertex set; the output is constant, and the modulus is zero.

**4. Sharpness for small cycles.** An interior base vector \(f\), a proper-arc indicator \(h\), and the resulting number \(V_n(P_fh)/2\) are listed here, with indices starting at zero:

- \(n=4\): \(f=(0,2,1,3)\), \(I=\{0,1\}\), selector \(s=(1,2,1,2)\), output mask \((1,0,1,0)\), ratio \(2\).
- \(n=5\): \(f=(0,1,3,2,4)\), \(I=\{0,1,2\}\), selector \(s=(1,1,3,2,3)\), output mask \((1,1,0,1,0)\), ratio \(2\).
- \(n=6\): \(f=(0,2,1,5,3,4)\), \(I=\{2,3,4\}\), selector \(s=(1,2,1,4,5,4)\), output mask \((0,1,0,1,0,1)\), ratio \(3\).

**5. Sharpness for all larger cycles.** For every \(n\ge7\), choose distinct values obeying
\[
f_{n-2}=0<f_0=1<f_{n-1}=2<f_1=3<f_3=4<f_2=5<f_4=6,
\]
with the remaining values (if any) distinct and greater than \(6\). Choose the arc \(I=\{0,1,2\}\). The medians at output positions \(n-1,1,3\) select coordinates \(0,1,2\), respectively, so their output-mask values are \(1\). The medians at positions \(0,2\) select coordinates \(n-1,3\), so those output-mask values are \(0\). Every other output position is at graph distance greater than one from \(I\), hence also produces \(0\). The output mask therefore has precisely three isolated components and variation \(6\), while \(V_n(\mathbf1_I)=2\). Taking \(x=f\) and \(y=f+\varepsilon\mathbf1_I\), with \(\varepsilon>0\) small enough to preserve strict order, gives an attaining pair. The cases in Step 4 use the same perturbation argument.

**6. Individual-data variation contraction.** For any real level \(t\), thresholding commutes with the median:
\[
\mathbf1_{\{T_nx>t\}}=T_n(\mathbf1_{\{x>t\}}),
\]
where the right side is the three-input Boolean majority. If adjacent Boolean inputs agree, both adjacent majority windows contain that same pair and their outputs agree. Thus every transition of the Boolean median output occurs at an original Boolean transition, yielding \(V_n(T_n\mathbf1_{\{x>t\}})\le V_n(\mathbf1_{\{x>t\}})\). Integrating over \(t\) with the elementary discrete coarea identity \(|a-b|=\int|\mathbf1_{a>t}-\mathbf1_{b>t}|\,dt\) proves \(V_n(T_nx)\le V_n(x)\).

## Verification

Run `python3 median_tv_checker.py` after extracting that standalone file alongside this document. The checker exhaustively enumerates all strict orderings and all proper cyclic arcs for \(3\le n\le7\), with exactly \(5910\) orderings; it checks explicit integer witnesses and actual attaining signal pairs for every \(4\le n\le40\), and verifies individual-data Boolean variation contraction on all \(8184\) binary masks of lengths \(3\) through \(12\). All passed. The all-dimension theorem follows from Steps 1--6, not from finite enumeration. The checker requires only Python standard-library modules.

## Relationship to prior work

Classical median filtering and its threshold decomposition are established tools. Qiu (1994) proves a local median-cost minimization identity using thresholded binary signals; this is not a two-input variation modulus. Restrepo and Chacón (1994) report one-input variation decrease for median filtering; their reported finite-signal convention uses nonpadding boundaries, not this periodic two-input problem. Arias-Castro and Donoho (2006/2009) analyze minimax statistical risks for median versus linear filtering, not the deterministic cyclic two-input sharp BV norm. The present result concerns a different operator invariant: the variation of the **difference** of two filtered datasets divided by the variation of their input difference.

## Limitations

The formula concerns only the three-point window and uniform cyclic variation. It does not establish sharp constants for larger windows, paths with nonperiodic boundary rules, weighted cycles, higher-order variations, vector-valued medians, or iteration. One relevant 1994 full text was not accessible for full comparison; the originality assessment retains this historical uncertainty. The claim of novelty is qualified by the literature examined, not by absence of search hits.

## References

1. E. Arias-Castro and D. L. Donoho, *Does median filtering truly preserve edges better than linear filtering?*, arXiv:math/0612422, first public version December 14, 2006, subsequently Annals of Statistics 37 (2009), 1172--1206. https://arxiv.org/abs/math/0612422
2. G. Qiu, *Functional Optimization Properties of Median Filtering*, IEEE Signal Processing Letters 1 (1994), 64--65. Author-hosted full text: https://people.cs.nott.ac.uk/pszqiu/webpages/Papers/Functional%20Optimisation%20Properties%20of%20Median%20Filtering.pdf
3. A. Restrepo and L. Chacón, *A Smoothing Property of the Median Filter*, IEEE Transactions on Signal Processing 42 (1994), 1553--1555, https://doi.org/10.1109/78.286974. Abstract verified; full text not materially inspected.
4. N. C. Gallagher and G. L. Wise, *A Theoretical Analysis of the Properties of Median Filters*, IEEE Transactions on Acoustics, Speech, and Signal Processing 29 (1981), 1136--1141, https://doi.org/10.1109/TASSP.1981.1163708. Abstract-level comparison only.
