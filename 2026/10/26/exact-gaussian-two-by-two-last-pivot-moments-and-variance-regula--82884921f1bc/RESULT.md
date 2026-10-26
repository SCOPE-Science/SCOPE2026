# Exact Gaussian two-by-two last-pivot moments and variance regularization by partial pivoting

## Finding
Let \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), where the four entries are independent standard real Gaussian variables. Perform ordinary Gaussian elimination in exact arithmetic after choosing the first pivot as the larger of \(|a|\) and \(|c|\). Let \(Z\) be the lower-right entry of the resulting upper-triangular factor. Then for every integer \(m\ge1\),
\[
\mathbb E[Z^{2m}]=\frac{4(2m-1)!!}{\pi}\sum_{j=0}^{m-1}\frac{\binom{m-1}{j}}{2j+1},
\qquad\mathbb E[Z^{2m+1}]=0.
\]
In particular \(\operatorname{Var}(Z)=4/\pi\), \(\mathbb E[Z^4]=16/\pi\), and the ordinary standardized kurtosis is exactly \(\pi\), giving excess kurtosis \(\pi-3\). By contrast the unpivoted second pivot \(d-bc/a\) has infinite variance. The complete characteristic function of \(Z\) is
\[
\varphi_Z(t)=\frac2\pi\int_{-1}^1\frac{\exp[-t^2(1+r^2)/2]}{1+r^2}\,dr.
\]

## Assumptions and scope
The matrix entries are independent \(N(0,1)\), the row pivot uses the largest absolute value in the first column, and all operations use exact real arithmetic. Zero pivots and ties occur with probability zero. The result describes a single final pivot in dimension two, not the entire GEPP growth factor or a large-dimensional asymptotic. All probabilities refer to the original random matrix law.

## Proof
Put \(T=c/a\). Rotational invariance of the independent pair \((a,c)\) gives the standard Cauchy density \(f_T(t)=1/[\pi(1+t^2)]\). Upon choosing the larger absolute first-column entry as the pivot, the lower/upper first-column ratio becomes \(R=T\) when \(|T|\le1\), and \(R=1/T\) otherwise. The reciprocal transformation of the Cauchy density shows that \(R\) has the normalized density
\[
f_R(r)=\frac2{\pi(1+r^2)}\mathbf 1_{(-1,1)}(r).
\]
Conditional on the first column (and hence on the choice of row permutation and on \(R\)), the two entries of the second column remain independent standard Gaussians. Denote them, in their pivoted order, by \(B,D\). The second pivot is \(Z=D-RB\). Therefore \(Z\mid R=r\sim N(0,1+r^2)\), giving the characteristic-function integral above, exact symmetry, and the even-moment identity
\[
\mathbb E Z^{2m}=(2m-1)!!\frac2\pi\int_{-1}^1(1+r^2)^{m-1}dr
=\frac{4(2m-1)!!}{\pi}\sum_{j=0}^{m-1}\frac{\binom{m-1}{j}}{2j+1}.
\]
For \(m=1,2\) the integrals are respectively \(1\) and \(4/3\), giving \(4/\pi\) and \(16/\pi\). Division of the fourth moment by the variance squared yields \(\pi\).

Without pivoting, \(Z_0=d-(c/a)b\). Conditional on \(a,b,c\), the independent centered \(d\) contributes variance one; the other term has squared expectation \(\mathbb E[(c/a)^2]\mathbb E[b^2]=\infty\) because \(\mathbb E[a^{-2}]=\infty\). Thus \(\mathbb E[Z_0^2]=\infty\).

## Verification
The accompanying standalone `check.py` evaluates the rational coefficients of the even-moment formula exactly for \(m=1,2,3\), and compares numerical second/fourth sample moments against \(4/\pi\) and \(16/\pi\) for a reproducibly seeded sample of 120,000 Gaussian matrices. The infinite distributional identity follows from conditional Gaussianity and change of variables, not from the sample.

## Relationship to prior work
Spielman and Yu (2026) analyze large growth of GEPP for Gaussian random matrices and define the exact-arithmetic final upper-triangular factor; their main bounds concern high-dimensional growth probabilities, not the exact two-dimensional final-pivot moment sequence. Gunawan, Peca-Medlin and Zhong (2026) study the permutation induced by pivoting, a different random variable. Classical average-case pivoting theory by Trefethen and Schreiber (1990) supplies background on entry growth but may already contain related special-dimensional distributions. The result should be regarded as an exact finite-dimensional benchmark, not a novelty claim for Cauchy ratios or Gaussian conditioning independently.

## Limitations
The source comparisons do not exhaust all older numerical linear-algebra texts; an equivalent exact \(2\)-by-\(2\) pivot law may have appeared under another description. The result is confined to iid real Gaussian entries and one elimination stage, and does not imply a particular high-dimensional tail law or floating-point rounding-error bound. The variance contrast is a property of the last pivot, not an assertion that every pivoting statistic improves monotonically.

## References
1. D. A. Spielman and X. Yu, *Large Growth Happens: Gaussian Elimination with Partial Pivoting on Random Matrices*, arXiv:2610.08701v1 (October 6, 2026), https://arxiv.org/html/2610.08701v1.
2. K. Gunawan, J. Peca-Medlin and C. Zhong, *Random permutations using GEPP*, arXiv:2610.10481v1 (October 7, 2026), https://arxiv.org/abs/2610.10481.
3. L. N. Trefethen and R. S. Schreiber, *Average-Case Stability of Gaussian Elimination*, SIAM J. Matrix Anal. Appl. **11** (1990), 335–360, https://doi.org/10.1137/0611023.
