# A checkerboard stability transition in \(4\times4\) anti-Monge least squares

## Finding
Let \(\mathcal C_n\) denote the cone of real \(n\times n\) arrays whose adjacent mixed second differences are nonnegative, and let \(\Pi_n\) be their unweighted Frobenius-nearest-point map. Equip input and output arrays with the entrywise maximum norm. Then the exact global Lipschitz constants are
\[
\operatorname{Lip}_{\infty}(\Pi_2)=\frac32,\qquad
\operatorname{Lip}_{\infty}(\Pi_3)=\frac{17}{9},\qquad
\operatorname{Lip}_{\infty}(\Pi_4)=\frac94.
\]
For the \(4\times4\) cone, the *unique* active inequality set producing the largest Jacobian norm is the checkerboard of five plaquettes: the four corner plaquettes and the central plaquette in its \(3\times3\) grid. Exactly the four central output entries have maximal Jacobian absolute row sum \(9/4\). In contrast, forcing every mixed difference to vanish gives Jacobian norm \(17/8\), strictly smaller by \(1/8\). For the \(2\times2\) and \(3\times3\) cones, full pooling is optimal. Moreover, \(\operatorname{Lip}_{\infty}(\Pi_n)\ge9/4\) for every \(n\ge4\); no exact value is asserted for \(n\ge5\).

## Assumptions and scope
For integers \(n\ge2\), identify arrays with vectors in \(\mathbb R^{n^2}\) by row-major order. For \(1\le i,j<n\), set
\[
(D_n x)_{ij}=x_{ij}-x_{i,j+1}-x_{i+1,j}+x_{i+1,j+1},\qquad
\mathcal C_n=\{x\in\mathbb R^{n^2}:D_nx\ge0\}.
\]
The orientation describes **anti-Monge**, or supermodular, arrays; multiplying all arrays by \(-1\) yields the equivalent Monge convention and the same stability constants. The map \(\Pi_n(y)\) is the unique minimizer of \(\sum_{i,j}(x_{ij}-y_{ij})^2\) over \(x\in\mathcal C_n\). The Lipschitz constant is the supremum over all distinct real input arrays, not a stochastic risk or a Hilbert-space operator norm.

## Proof
**1. All active sets occur.** The \((n-1)^2\) rows of \(D_n\) are linearly independent: for any prescribed plaquette slacks \(s_{ij}\), taking \(x_{ij}=\sum_{p<i}\sum_{q<j}s_{pq}\) gives \(D_nx=s\). Therefore every subset \(A\) of the plaquettes occurs as a strictly complementary active set. Choose slacks zero on \(A\), one off \(A\), construct \(z\) as above, and put \(y=z-D_A^T\mathbf1\). The optimality conditions for Euclidean projection are satisfied with active multipliers equal to one and strictly positive inactive slacks. Hence on a neighborhood of \(y\), the projection is the affine orthogonal projection onto \(D_Ax=0\), with Jacobian
\[
P_A=I-D_A^T(D_AD_A^T)^{-1}D_A.
\]
For the empty set, \(P_A=I\). Positive multipliers and inactive slacks ensure the claimed neighborhood exists.

**2. Global reduction.** A polyhedral projection is continuous and piecewise affine with finitely many affine formulas of the preceding form. Restricting to any input segment and integrating along its finitely many affine pieces proves
\[
\operatorname{Lip}_{\infty}(\Pi_n)
=\max_{A\subseteq\{1,\ldots,(n-1)^2\}}\|P_A\|_{\infty\to\infty}
=\max_A\max_{1\le k\le n^2}\sum_{h=1}^{n^2}|(P_A)_{kh}|.
\]
The reverse inequality holds because every active set has an open realization, and an absolute-row-sign perturbation attains the corresponding Jacobian norm locally. No restriction to actual observed active sets is omitted.

**3. Exhaustive exact rational certificate.** The accompanying standalone `check_exact.py` uses rational Gauss–Jordan inversion, constructs \(D_A\) independently from the displayed mixed-difference formula, and enumerates **every** one of the \(2^{(n-1)^2}\) subsets for \(n=2,3,4\). It checks symmetry, idempotence, annihilation of active constraints, and all row sums using exact fractions. The following table records the exact largest row sum among active sets of each size for \(n=4\):

| Number of active plaquettes | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Maximum row sum | \(1\) | \(3/2\) | \(9/5\) | \(27/14\) | \(21/10\) | \(9/4\) | \(43/20\) | \(17/8\) | \(19/9\) | \(17/8\) |

The unique global maximizing mask is integer \(341=2^0+2^2+2^4+2^6+2^8\), with plaquettes indexed zero-based in row-major order. For \(n=3\) the exact maxima by active-set size are \(1,3/2,9/5,11/6,17/9\), uniquely maximized with all four plaquettes active; for \(n=2\) the maxima are \(1,3/2\). Because the loops cover precisely all subsets, these finite rational calculations constitute exhaustive finite proofs of the asserted constants, not sampling experiments. The Python file contains the entire arithmetic verification and requires no third-party modules.

For the winning \(4\times4\) face, the Jacobian row at output \((2,2)\), displayed as a \(4\times4\) coefficient array, is
\[
\frac1{16}\begin{pmatrix}
-3&3&1&-1\\ 3&9&3&1\\ 1&3&-3&-1\\ -1&1&-1&1
\end{pmatrix}.
\]
Its absolute entry sum is \(36/16=9/4\). Symmetry gives the same norm at \((2,3),(3,2),(3,3)\), and the exact enumeration certifies that no other cell or mask attains it.

**4. Explicit finite-pair attainment.** Take the three \(4\times4\) arrays
\[
z=\begin{pmatrix}0&0&0&0\\0&0&1&1\\0&1&2&3\\0&1&3&4\end{pmatrix},\qquad
y=\begin{pmatrix}-1&1&-1&1\\1&-2&3&0\\-1&3&0&4\\1&0&4&3\end{pmatrix},
\]
\[
v=\begin{pmatrix}-1&1&1&-1\\1&1&1&1\\1&1&-1&-1\\-1&1&-1&1\end{pmatrix}.
\]
The mixed differences of \(z\) form the checkerboard \(\begin{psmallmatrix}0&1&0\\1&0&1\\0&1&0\end{psmallmatrix}\), while \(y=z-D_A^T\mathbf1\); therefore \(\Pi_4(y)=z\). With \(\varepsilon=1/100\), the projected point at \(y+\varepsilon v\) is \(z+\varepsilon P_Av\). Its five active multipliers are positive, with minimum \(397/400\), and its four inactive slacks are positive, with minimum \(99/100\), as checked exactly in the certificate. The output difference at \((2,2)\) is \(9\varepsilon/4\), whereas the input maximum difference is \(\varepsilon\). Thus the global constant is attained by an actual finite pair.

**5. Why the transition matters.** When all plaquettes are active, arrays have the additive form \(x_{ij}=r_i+c_j\), and projection is row mean plus column mean minus grand mean. Its norm is exactly \(3-4/n+2/n^2\); this equals the global norm for \(n=2,3\) but only \(17/8\) when \(n=4\). The checkerboard face beats it, establishing the first square-size failure of the full-pooling extremizer principle. Finally, for every \(n>4\), embed the five checkerboard plaquette constraints in the upper-left \(4\times4\) window and leave all other constraints inactive. The Jacobian is the \(4\times4\) winning projection direct-summed with an identity on the remaining entries, hence has norm \(9/4\). Step 1 ensures this embedded active set is realizable, proving the persistent lower bound.

## Verification
Run `python3 check_exact.py` in the directory containing this file. It evaluates the two, sixteen, and five hundred twelve active subsets in dimensions two, three, and four, respectively, with only exact rational arithmetic. It verifies the stated per-cardinality maxima, the unique maximizing masks, the explicit winning Jacobian, and strict KKT feasibility of the finite attainment pair. The completed run printed the expected maxima and the multiplier/slack minima \(397/400\) and \(99/100\). The certificate is finite and exhaustive for sizes through four; it does not attempt to enumerate larger squares.

## Relationship to prior work
Chatterjee, Guntuboyina and Sen (first public preprint June 10, 2015) study bivariate matrix isotonic least squares and its *statistical risk*, with coordinatewise monotonicity rather than mixed-difference inequalities. Hütter, Mao, Rigollet and Robeva (first public preprint April 5, 2019) formulate anti-Monge least-squares estimation with the same mixed-difference cone and provide estimation rates and Dykstra projection algorithms. The latter contains the correct underlying operator but not, in the examined main results, algorithm section, proof or appendices, the \(4\times4\) maximum-norm Lipschitz constant or its uniquely extremizing checkerboard active face. The active-set Jacobian technique is standard polyhedral projection theory; novelty is claimed only for this exact sharp first-square transition, its complete active-set classification, and explicit finite-pair realization. Published scalar isotonic and weighted two-row stability results concern different constraints or only two rows and do not imply the genuinely two-dimensional checkerboard face result.

## Limitations
The claim concerns real, unweighted, contiguous-square anti-Monge least squares and coordinatewise maximum-norm input/output errors, not arbitrary weights, pre-Monge permutations, multivariate mixed constraints, or stochastic minimax risk. Constants are exact only for square sizes two, three and four; the larger-square statement is only a lower bound. The finite proof depends on the included exact-arithmetic code and its stated exhaustive enumeration, not on a closed-form inequality valid for all sizes. Historical priority remains subject to independent bibliographic review, including possible earlier formulations under polyhedral cone or submodular regression terminology. No independent external validation is asserted.

## References
1. S. Chatterjee, A. Guntuboyina, B. Sen, *On matrix estimation under monotonicity constraints*, arXiv:1506.03430 (first posted 2015-06-10), https://arxiv.org/abs/1506.03430.
2. J.-C. Hütter, C. Mao, P. Rigollet, E. Robeva, *Estimation of Monge Matrices*, arXiv:1904.03136 (first posted 2019-04-05), https://arxiv.org/abs/1904.03136.
