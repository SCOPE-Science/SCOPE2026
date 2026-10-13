# Sharp three-point support geometry for three-draw extreme-order correlation
## Finding
Let \(X_1,X_2,X_3\) be independent and identically distributed, uniformly on three distinct real points \(x_1<x_2<x_3\). Write
\[
L=\min_{1\le i\le3}X_i,\qquad U=\max_{1\le i\le3}X_i.
\]
Then
\[
\operatorname{Corr}(L,U)\le \frac14.
\]
Equality holds if and only if
\[
x_2=\frac{x_1+x_3}{2}.
\]
Thus the arithmetic progression is the unique three-point support geometry, up to positive affine transformation, that maximizes the correlation of the extreme order statistics for three iid draws with equal parent masses.

## Assumptions and scope
The parent law has exactly three distinct atoms and assigns mass \(1/3\) to each. Pearson correlation is well defined because both extremes are nondegenerate. Correlation is invariant under applying the same positive affine transformation to all observations, so normalize the support to \(\{0,t,1\}\) with \(0<t<1\). The claim varies the support geometry while keeping the probability vector fixed and uniform. It does not optimize over nonuniform masses, larger supports, or sample sizes other than three.

## Proof
After normalization, let each \(X_i\) be uniform on \(\{0,t,1\}\), \(0<t<1\). Direct counting of the \(27\) equally likely ordered samples gives
\[
\mathbb E L=\frac{7t+1}{27},\qquad
\mathbb E U=\frac{7t+19}{27},
\]
\[
\mathbb E L^2=\frac{7t^2+1}{27},\qquad
\mathbb E U^2=\frac{7t^2+19}{27},
\]
and
\[
\mathbb E(LU)=\frac{t^2+6t+1}{27}.
\]
Hence
\[
\operatorname{Cov}(L,U)
=-\frac{2(11t^2-11t-4)}{729},
\]
\[
\operatorname{Var}(L)=\frac{2(70t^2-7t+13)}{729},\qquad
\operatorname{Var}(U)=\frac{2(70t^2-133t+76)}{729}.
\]
The quadratic \(11t^2-11t-4\) is negative on \((0,1)\), so the covariance is positive. Therefore maximizing the correlation is equivalent to maximizing its square
\[
R(t)=\operatorname{Corr}(L,U)^2
=\frac{(11t^2-11t-4)^2}
{(70t^2-133t+76)(70t^2-7t+13)}.
\]
Differentiation and exact factorization give
\[
R'(t)=
\frac{81(2t-1)(11t^2-11t-4)(791t^2-791t+380)}
{(70t^2-133t+76)^2(70t^2-7t+13)^2}.
\]
For \(0<t<1\), the final quadratic is strictly positive because
\[
791t^2-791t+380=791\left(t-\frac12\right)^2+\frac{729}{4}>0.
\]
Since \(11t^2-11t-4<0\), one has \(R'(t)>0\) for \(t<1/2\) and \(R'(t)<0\) for \(t>1/2\). Thus \(t=1/2\) is the unique global maximizer. Substitution yields
\[
R\left(\frac12\right)=\frac1{16},
\]
so \(\operatorname{Corr}(L,U)=1/4\) there. Undoing the affine normalization gives the stated equality condition.

## Verification
The symbolic checker `verify.py` independently enumerates all \(27\) ordered samples, derives the five raw moments, reconstructs the covariance and variances, verifies the displayed rational formula for \(R(t)\), verifies the derivative factorization exactly, and checks \(R(1/2)=1/16\). The proof itself is analytic; the checker is a reproducibility aid rather than an extrapolation from finite numerical experiments.

## Relationship to prior work
Papadatos's 2022 discrete analogue of Terrell's theorem treats two iid draws from an equally weighted finite support and proves that, for fixed support cardinality, an arithmetic progression uniquely maximizes the min-max correlation in that two-draw problem. The same paper recalls the universal Székely-Móri bound for general sample size, which for the minimum and maximum of three draws is \(1/3\); that general bound does not determine the sharper three-atom value \(1/4\) or its support-geometry equality case.

Papadatos's earlier sample-size-three paper gives a sharp covariance bound over arbitrary parent distributions and characterizes a continuous hyperbolic-sine extremizer. That covariance theorem neither fixes equal three-point masses nor optimizes Pearson correlation over the interior support location, so it does not imply the present statement.

A separate indexed result for two iid draws on an equally spaced three-point support optimizes the parent probability vector. That problem varies masses with geometry fixed; the present problem keeps masses fixed and varies geometry, and it uses three draws. Neither statement implies the other.

## Limitations
The theorem is a complete classification only for equal masses on exactly three atoms and sample size three. It does not give the sharp correlation over arbitrary three-point probability vectors, arbitrary finite supports, or other sample sizes. Searches did not locate an equivalent statement, but an older elementary calculation under different discrete-order-statistic notation remains a residual originality risk.

## References
1. N. Papadatos, *A discrete analogue of Terrell's characterization of rectangular distributions*, arXiv:2205.14360v1 (2022). Primary MSC 60E15.
2. N. Papadatos, *Upper bound for the covariance of extreme order statistics from a sample of size three*, Sankhyā Ser. A 61 (1999), 229–240.
3. G. J. Székely and T. F. Móri, *An extremal property of rectangular distributions*, Statistics & Probability Letters 3 (1985), 107–109.
