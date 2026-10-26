# A sharp four-point phase transition in Sobolev stability of isotonic regression

## Finding

Let \(P:\mathbb R^4\to\mathbb R^4\) be the **ordinary Euclidean least-squares isotonic projection** onto \(C=\{z:z_1\le z_2\le z_3\le z_4\}\). For \(\gamma>0\), measure perturbations with the discrete path-Sobolev norm
\[
\|z\|_\gamma^2=\sum_{i=1}^4z_i^2+\gamma\sum_{i=1}^3(z_{i+1}-z_i)^2.
\]
(The estimator is defined by Euclidean projection, **not** projection in this Sobolev norm.) Define the exact two-input amplification
\[
L_4(\gamma)=\sup_{x\ne y}\frac{\|P(x)-P(y)\|_\gamma}{\|x-y\|_\gamma}.
\]
Then
\[
\boxed{L_4(\gamma)^2=\begin{cases}
\dfrac{3\gamma^2+4\gamma+1}{2\gamma^2+4\gamma+1},&0<\gamma\le\tfrac12,\\[5pt]
\dfrac{56\gamma^3+98\gamma^2+54\gamma+9}{36\gamma^3+90\gamma^2+54\gamma+9},&\gamma\ge\tfrac12.
\end{cases}}
\]
The branches agree at \(\gamma=\tfrac12\), with \(L_4(1/2)^2=15/14\). The first branch is attained locally precisely on the pooling patterns \((2,2)\) and \((1,2,1)\); the second on \((1,3)\) and \((3,1)\). At the threshold, all four patterns attain the maximum. Here a pattern lists lengths of consecutive equal fitted-value blocks. Every pattern has a nonempty full-dimensional region of input data, so the global Lipschitz supremum is attained by **actual distinct input pairs**, for every \(\gamma>0\).

The squared modulus is continuous but has a strict derivative jump of \(1/126\) at \(\gamma=1/2\); consequently \(L_4\) is not differentiable there. In the strong-gradient limit, \(L_4(\gamma)\to\sqrt{14}/3\). This is the smallest chain length with a genuine switch between optimal pooling geometries: for two observations the modulus is one, while for three observations its square is \((15\gamma^2+16\gamma+4)/(12\gamma^2+16\gamma+4)\) and both one-pair pooling patterns remain jointly optimal for all positive \(\gamma\).

## Assumptions and scope

All vectors are real. The four observations are unweighted in the Euclidean squared-error fit. The graph is the unit-weight four-vertex path; the metric includes unit vertex masses and one common positive gradient coupling \(\gamma\). Both input and output differences are measured with the **same** \(\|\cdot\|_\gamma\). The assertions concern all real input pairs, without generic-position restrictions; the claimed pooling-pattern classification refers to the full-dimensional affine regions of the projection. No claim is made for larger chains or alternate regression loss functions.

## Proof

**1. Pooling cells and global modulus.** Standard pool-adjacent-violators optimality partitions each input into consecutive fitted blocks. On the open region with block lengths \(\pi=(k_1,\ldots,k_r)\), the projection equals a linear block-averaging matrix \(E_\pi\): on each consecutive block of length \(k\), every output equals the arithmetic mean of its \(k\) inputs. Every composition of four occurs on a nonempty open input region: choose strictly decreasing values within each desired block and strictly increasing, widely separated block means. Such data strictly satisfy the internal pooling KKT inequalities and external separation inequalities. Small perturbations retain the same pattern.

The continuous piecewise-linear map \(P\) has only these eight linear pieces. Along any straight input segment, splitting at pooling-cell boundaries and applying the operator norm of the active linear piece gives an upper bound by the maximum of their \(\|\cdot\|_\gamma\)-norms. Conversely, inside an open cell, a small displacement in a maximizing singular direction realizes exactly that piece's norm. Therefore
\[
L_4(\gamma)=\max_{\pi\models4}\|E_\pi\|_{\gamma\to\gamma}.
\]

**2. Exact generalized eigenvalues.** Let \(D\) be the \(3\times4\) consecutive-difference matrix, \(Q_\gamma=I_4+\gamma D^\mathsf TD\), and \(E=E_\pi=E^\mathsf T=E^2\). Then the squared norm of \(E\) is the largest generalized eigenvalue of \((EQ_\gamma E,Q_\gamma)\), equivalently the largest root of \(\det(EQ_\gamma E-tQ_\gamma)=0\). The determinant is a polynomial in \((\gamma,t)\). Direct exact expansion gives the following largest eigenvalues, where \(A,B,H\) abbreviate the rational expressions shown:
\[
\begin{aligned}
A(\gamma)&=\frac{56\gamma^3+98\gamma^2+54\gamma+9}{36\gamma^3+90\gamma^2+54\gamma+9},\\
B(\gamma)&=\frac{3\gamma^2+4\gamma+1}{2\gamma^2+4\gamma+1},\\
H(\gamma)&=\frac{20\gamma^3+43\gamma^2+24\gamma+4}{16\gamma^3+40\gamma^2+24\gamma+4}.
\end{aligned}
\]
For patterns \((1,3)\) and \((3,1)\), the answer is \(A\). For \((2,2)\) and \((1,2,1)\), it is \(B\). For \((1,1,2)\) and \((2,1,1)\), it is \(H\). For \((1,1,1,1)\) and \((4)\), it is \(1\). These eight claims may be verified directly from the matrices \(E_\pi\); the accompanying standard-library checker gives **exact determinant identities for all parameters**, using rational bivariate polynomial interpolation justified by the determinant degree bound. In particular, these are algebraic identities, not conclusions from numerical sampling.

**3. Strict comparison and transition.** The common positive denominator of the relevant rational differences makes every comparison explicit:
\[
\begin{aligned}
A-B&=\frac{\gamma^2(2\gamma-1)}{9(2\gamma+1)(2\gamma^2+4\gamma+1)},\\
A-H&=\frac{\gamma^2(44\gamma+5)}{36(2\gamma+1)(2\gamma^2+4\gamma+1)},\\
B-H&=\frac{\gamma^2(4\gamma+1)}{4(2\gamma+1)(2\gamma^2+4\gamma+1)}.
\end{aligned}
\]
Also \(A,B>1\) for every positive \(\gamma\). Hence only \(A\) and \(B\) can be globally maximal, and they cross once, at \(\gamma=1/2\). Differentiating the displayed difference gives \((A-B)'(1/2)=1/126\), proving the cusp. The strong-gradient limit follows from the leading cubic coefficients of \(A\). The stated three-observation formula follows from enumerating its four pooling compositions, and the two-observation norm is one because neighbor averaging commutes with its path quadratic form.

**4. Concrete sharp pairs.** At \(\gamma=1\), choose \(x=(-10,3,2,1)\), \(v=(-31,1,13,17)\), and \(y=x+v/100\). Both inputs have the pooling pattern \((1,3)\), and exact rational calculation gives
\[
\frac{\|P(y)-P(x)\|_1^2}{\|y-x\|_1^2}=\frac{31}{27}=A(1).
\]
At \(\gamma=1/10\), choose \(x=(2,1,5,4)\), \(v=(-7,-6,6,7)\), and \(y=x+v/100\). Both inputs have the pooling pattern \((2,2)\), and
\[
\frac{\|P(y)-P(x)\|_{1/10}^2}{\|y-x\|_{1/10}^2}=\frac{143}{142}=B(1/10).
\]
For arbitrary positive \(\gamma\), existence of attaining pairs follows from the finite-dimensional generalized-eigenvalue principle and the open-cell argument in Step 1; rationality of the examples is not required for that existence proof.

## Verification

Run \(\texttt{python3 verify_phase.py}\) with a standard Python 3 installation. The checker constructs the eight block-averaging matrices, forms the exact rational generalized characteristic determinants and verifies the claimed factorizations. Each side is a bivariate polynomial of degree at most four in each of \(\gamma\) and the spectral variable \(t\); agreement at five distinct rational values of each variable proves the polynomial identities identically, by repeated univariate interpolation. Supplementary noninteger evaluations and two exact rational attaining pairs are also checked. The recorded run returned `EXACT_FOUR_POINT_ISOTONIC_SOBLEV_CERTIFICATE_OK 250`. This proves the finite algebraic identities used above; the global piecewise-linear and attainment arguments are established separately in the proof.

## Relationship to prior work

Yeganova and Wilbur (2009, DOI below) establish pool-adjacent-violators methodology and study regression subject to an *additional Lipschitz restriction on the fitted sequence*, not the two-input Lipschitz modulus of ordinary isotonic regression in a Sobolev perturbation norm. Németh and Németh (2015) establish order-preservation results for Euclidean projections onto isotonic regression cones. Yang and Barber (2017) characterize **whether** isotonic projection is contractive in a prescribed seminorm via neighbor-averaging; the present result computes the exact **noncontractive modulus** and the sharp competition among four-vertex pooling patterns.

A separately published finite-chain \(\ell_p\) stability theorem measures perturbations in symmetric coordinate norms, while the present path-Sobolev norm couples neighboring coordinates and is not permutation-invariant. That theorem's formulas neither yield nor dominate the branch crossover above. No matching four-vertex formula was found in the inspected primary sources or the searched research records; this is a bounded originality assessment, not a proof of global priority.

## Limitations

The result is a sharp four-observation test case, not a theorem about longer chains. The global maximizer classification concerns pooling cells, not uniqueness of every pair attaining the Lipschitz ratio. The formula depends on unit vertex masses, equal path-edge weights and the Euclidean definition of the regression estimator; altering any of these can change the answer. Historical exact matrix-norm calculations or stability tables not indexed by the searches could contain equivalent formulas. No independent scientific audit is claimed.

## References

1. L. Yeganova and W. J. Wilbur, *Isotonic Regression under Lipschitz Constraint*, Journal of Optimization Theory and Applications 141 (2009), 429–443, first published 2009-01-07, DOI: 10.1007/s10957-008-9477-0. Full open-access PDF: https://link.springer.com/content/pdf/10.1007/s10957-008-9477-0.pdf .
2. A. B. Németh and S. Z. Németh, *Isotonic regression and isotonic projection*, arXiv:1503.08458, first posted 2015-03-29, https://arxiv.org/html/1503.08458v2 .
3. F. Yang and R. Foygel Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852, first posted 2017-06-06, https://arxiv.org/abs/1706.01852 .
4. *Sharp \(\ell_p\) stability of finite-chain isotonic metric projections*, published research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-ell-p-stability-of-finite-chain-isotonic-metric-projection--f78c125227d5 .
