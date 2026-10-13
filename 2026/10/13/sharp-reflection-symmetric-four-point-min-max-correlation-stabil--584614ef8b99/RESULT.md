# Sharp reflection-symmetric four-point min-max correlation stability
## Finding
Let \(0\le \theta\le1\). Let \(X_1,X_2\) be independent with the same law on \(\{0,1,2,3\}\), given by
\[
\Pr(X=0)=\Pr(X=3)=\frac{\theta}2,
\qquad
\Pr(X=1)=\Pr(X=2)=\frac{1-\theta}2.
\]
Write \(L=\min(X_1,X_2)\) and \(U=\max(X_1,X_2)\). Then
\[
\rho(\theta):=\operatorname{Corr}(L,U)
=
\frac{(1+4\theta-2\theta^2)^2}
{3+24\theta-12\theta^2+16\theta^3-4\theta^4}.
\]
For every \(0\le\theta\le1\),
\[
\rho(\theta)\le\frac5{11},
\]
and equality holds if and only if \(\theta=1/2\), i.e. exactly for the uniform law on the four-point lattice. More precisely,
\[
\frac5{11}-\rho(\theta)
=
\frac{4(2\theta-1)^2(1+12\theta-4\theta^2)}
{11(3+24\theta-12\theta^2+16\theta^3-4\theta^4)}.
\]
Thus the four-point rectangular law is not only extremal inside the natural reflection-symmetric probability family; its correlation deficit has an exact quadratic stability factor in the mass imbalance.

## Assumptions and scope
The support is the equally spaced four-point set \(\{0,1,2,3\}\), the sample size is two, and the parent law is reflection-symmetric about \(3/2\). The parameter \(\theta\) is the total mass on the two outer atoms. The result includes the endpoint laws \(\theta=0\) and \(\theta=1\), which are nondegenerate two-point laws. It does not claim the same \(5/11\) bound for every nonsymmetric probability vector on four points.

## Proof
Reflection symmetry gives \(\mathbb E X=3/2\). Put
\[
\delta=\frac12\mathbb E|X_1-X_2|.
\]
Since
\[
L=\frac{X_1+X_2-|X_1-X_2|}2,
\qquad
U=\frac{X_1+X_2+|X_1-X_2|}2,
\]
we have
\[
\mathbb E L=\frac32-\delta,
\qquad
\mathbb E U=\frac32+\delta.
\]
Also \(LU=X_1X_2\). Independence therefore gives
\[
\operatorname{Cov}(L,U)
=\mathbb E[X_1X_2]-\mathbb E L\,\mathbb E U
=\delta^2.
\]
The reflection \(x\mapsto3-x\) sends \(L\) in law to \(3-U\), so
\[
\operatorname{Var}(L)=\operatorname{Var}(U).
\]

A direct four-atom summation gives
\[
\delta=\frac{1+4\theta-2\theta^2}4
\]
and
\[
\operatorname{Var}(L)=\operatorname{Var}(U)
=\frac{3+24\theta-12\theta^2+16\theta^3-4\theta^4}{16}.
\]
Consequently
\[
\rho(\theta)
=\frac{\operatorname{Cov}(L,U)}{\operatorname{Var}(L)}
=\frac{(1+4\theta-2\theta^2)^2}
{3+24\theta-12\theta^2+16\theta^3-4\theta^4}.
\]
Subtracting this expression from \(5/11\) and factoring gives
\[
\frac5{11}-\rho(\theta)
=
\frac{4(2\theta-1)^2(1+12\theta-4\theta^2)}
{11(3+24\theta-12\theta^2+16\theta^3-4\theta^4)}.
\]
The denominator equals \(176\operatorname{Var}(L)\) and is strictly positive for the whole interval because every law in the family is nondegenerate. Moreover \(1+12\theta-4\theta^2>0\) on \([0,1]\). Hence the deficit is nonnegative and vanishes exactly at \(2\theta-1=0\). This proves the sharp bound and the equality statement.

## Verification
The accompanying `verify.py` independently derives the joint law of \((L,U)\) from the four atom probabilities, verifies the displayed symbolic formulas, verifies the exact factorization of the deficit, and checks rational parameter values throughout a finite grid. The grid is only a stress test; the universal claim follows from the displayed exact factorization and positivity argument.

## Relationship to prior work
Papadatos proved a discrete analogue of Terrell's extremal theorem. For a law uniform on \(N\) lattice points, his sharp bound for the minimum-maximum correlation is
\[
\frac{1-N^{-2}}{2+N^{-2}},
\]
so the four-point rectangular value is \(5/11\). His theorem concerns a uniform distribution on the underlying finite population and does not give the present exact stability profile when the four fixed support points retain reflection symmetry but their masses vary.

A published three-point result goes in the complementary probability-vector direction: on three equally spaced atoms and sample size two, it proves that the uniform probability vector uniquely maximizes the minimum-maximum correlation, with value \(8/19\). The present theorem is the next support size in the symmetry-preserving mass deformation and supplies an exact deficit formula rather than only the extremal value. No implication from the three-point statement yields the four-point formula above.

## Limitations
The nonsymmetric four-point probability simplex is not classified here, and no claim is made about larger supports or sample sizes above two. The main residual literature risk is that this one-parameter exact formula may be implicit in older order-statistic correlation calculations under different notation; targeted searches for the four-point symmetric mass family and the exact \(5/11\) stability statement found no such source.

## References
1. N. Papadatos, “A discrete analogue of Terrell's characterization of rectangular distributions,” arXiv:2205.14360v1, first public 28 May 2022; later Mathematical Methods of Statistics 32 (2023), 122–132, DOI 10.3103/S1066530723020035.
2. “Sharp min-max correlation over three-point probability weights,” published record 92f0f4188ee4.
