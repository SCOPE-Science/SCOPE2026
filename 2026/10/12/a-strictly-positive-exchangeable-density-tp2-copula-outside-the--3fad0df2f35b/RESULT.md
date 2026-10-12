# A strictly positive exchangeable density-TP2 copula outside the PMI class

## Finding
There exists an **exchangeable, absolutely continuous bivariate copula** with an everywhere strictly positive piecewise-constant density that is **totally positive of order two** (d-TP2) but **not positive measure inducing** (PMI). An explicit six-by-six checkerboard example is given below. Thus even d-TP2, which implies Markov-kernel TP2, does not suffice for PMI; strict density positivity and exchangeability do not restore the implication.

## Assumptions and scope
For integers \(1\le i\le6\), put \(I_i=((i-1)/6,i/6)\) with arbitrary consistent assignments at cell boundaries. If \(Q\) is a symmetric doubly stochastic six-by-six matrix, define the checkerboard density by \(c_Q(u,v)=6Q_{ij}\) for \((u,v)\in I_i\times I_j\). The associated law is a copula, since its row and column integrals are one. This density is d-TP2 exactly when the matrix \(Q\) has nonnegative ordered two-by-two minors.

For an absolutely continuous copula, PMI requires the reflection contrast
\[
\Delta_c(u,v):=c(u,v)-c(1-u,v)-c(u,1-v)+c(1-u,1-v)\ge0
\]
for almost all \((u,v)\in(0,1/2)^2\); see Fuchs–Tschimpke, Remark 1 and equation (2.4). A strictly negative contrast on an open cell rectangle disproves PMI.

## Proof
First consider the symmetric doubly stochastic matrix
\[
P=\frac1{64}\begin{pmatrix}
32&12&12&8&0&0\\
12&17&17&18&0&0\\
12&17&17&18&0&0\\
8&18&18&20&0&0\\
0&0&0&0&32&32\\
0&0&0&0&32&32
\end{pmatrix}.
\]
Let \(T_i\) denote an adjacent-coordinate averaging matrix, the identity except at rows and columns \(i,i+1\), where its two-by-two block has four entries equal to \(1/2\). These matrices are doubly stochastic and have nonnegative ordered two-by-two minors. In the upper-left four-by-four block, set
\[
A=T_1T_3T_2T_3T_2
=\frac1{16}\begin{pmatrix}8&3&3&2\\8&3&3&2\\0&5&5&6\\0&5&5&6\end{pmatrix}.
\]
Direct multiplication gives \(P=\operatorname{diag}(A^{\mathsf T}A,J_2/2)\), with \(J_2\) the two-by-two all-ones matrix. Ordered two-by-two minors stay nonnegative under multiplication by the Cauchy–Binet identity. They also stay nonnegative under the ordered block-diagonal concatenation of nonnegative matrices. Hence \(P\) is d-TP2 as a checkerboard density.

If \(u\in I_2\) and \(v\in I_3\), the reflected cells are numbered \(5\) and \(4\), respectively. The four-cell contrast is
\[
P_{23}-P_{53}-P_{24}+P_{54}=\frac{17-0-18+0}{64}=-\frac1{64}.
\]
Thus \(\Delta_{c_P}(u,v)=-3/32\) on the whole open rectangle \(I_2\times I_3\). This already proves that exchangeable d-TP2 does not imply PMI, but \(P\) contains zeros. The remaining construction removes every zero without losing either property.

For \(1\le i\le5\) and \(0<\varepsilon<1\), let
\[
R_i(\varepsilon)=I_6-\frac{\varepsilon}{2}(e_i-e_{i+1})(e_i-e_{i+1})^{\mathsf T},
\qquad \varepsilon=\frac1{100000}.
\]
Each \(R_i(\varepsilon)\) is symmetric, doubly stochastic and TP2: its sole modified adjacent block has diagonal \(1-\varepsilon/2\), off-diagonal \(\varepsilon/2\), and determinant \(1-\varepsilon\ge0\). Define
\[
S=(R_1(\varepsilon)R_2(\varepsilon)R_3(\varepsilon)R_4(\varepsilon)R_5(\varepsilon))^5,
\qquad Q=S^{\mathsf T}PS.
\]
Products of TP2 matrices remain TP2, so \(Q\) is TP2. It is symmetric and doubly stochastic. Each of the five full sweeps offers a positive-probability adjacent transition or self-loop; any two of six indices can therefore be connected by a path with at most five sweeps. Consequently every entry of \(S\) is positive. Since all diagonal entries of \(P\) are positive, \(Q_{ij}=\sum_{k,l}S_{ki}P_{kl}S_{lj}>0\) for all \(i,j\).

For the operator maximum absolute row-sum norm, each of the 25 factors satisfies \(\|R_i(\varepsilon)-I\|_\infty=\varepsilon\). Stochasticity and telescoping give both \(\|S-I\|_\infty\le25\varepsilon\) and \(\|S^{\mathsf T}-I\|_\infty\le25\varepsilon\). Hence
\[
\|Q-P\|_\infty
\le\|(S^{\mathsf T}-I)PS\|_\infty+\|P(S-I)\|_\infty
\le50\varepsilon.
\]
Each matrix entry changes by at most \(50\varepsilon\). The same reflection contrast for \(Q\) therefore obeys
\[
Q_{23}-Q_{53}-Q_{24}+Q_{54}
\le-\frac1{64}+200\varepsilon
=-\frac1{64}+\frac1{500}<0.
\]
The strictly positive, exchangeable d-TP2 density \(c_Q\) consequently fails PMI on \(I_2\times I_3\). This proves the claim.

## Verification
The accompanying `verify_positive_tp2_not_pmi.py` uses exact rational arithmetic. It reconstructs the finite matrix factorization, verifies all 225 ordered two-by-two minors, stochastic marginal sums, symmetry and the exact base reflection defect. It then reconstructs all 25 rational smoothing factors, verifies strict positivity and all 225 minors of \(Q\), and checks the analytic perturbation bound and negative PMI contrast. These are finite exact checks; the all-point density conclusion follows from its constant values on finitely many rectangles and the analytic matrix-product argument.

## Relationship to prior work
Fuchs and Tschimpke (2023, later published 2024) define PMI and its density reflection criterion. Their Example 7 gives a Marshall–Olkin copula that is MK-TP2 but not PMI; the example includes a singular component and therefore does **not** establish failure for the stronger d-TP2 condition. Fuchs and Tschimpke (2022) prove the hierarchy d-TP2 implies MK-TP2, making the distinction essential. The present constructive witness settles that stronger nonimplication with a strictly positive density and exchangeability. Familiar Gaussian and Frank copula families satisfy both d-TP2 and PMI for positive dependence parameters, so those family-specific equivalences do not settle the general question.

## Limitations
The copula density is strictly positive but piecewise constant, not smooth. The result is a counterexample, not a claim that six cells are minimal, not a classification of all d-TP2 copulas, and not a counterexample restricted to Archimedean copulas. Failure of PMI alone does not establish failure of any particular integrated concordance inequality. Bibliographic priority beyond the two directly inspected foundational papers has not been independently established.

## References
1. S. Fuchs and M. Tschimpke, *A novel positive dependence property and its impact on a popular class of concordance measures*, arXiv:2306.09676v1 (first public 2023-06-16), subsequently *Journal of Multivariate Analysis* 200 (2024), 105259, doi:10.1016/j.jmva.2023.105259. In particular Definition 1, Remark 1, equation (2.4), and Example 7.
2. S. Fuchs and M. Tschimpke, *Total positivity of copulas from a Markov kernel perspective*, arXiv:2205.01914v1 (2022-05-04), Sections 1 and 3.
