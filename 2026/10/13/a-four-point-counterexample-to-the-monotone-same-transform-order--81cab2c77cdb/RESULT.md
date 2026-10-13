# A four-point counterexample to the monotone same-transform order-statistic correlation conjecture
## Finding
Let \(X_1,X_2,X_3\) be independent and uniform on \(\{1,2,3,4}\). Write
\[
L=\min(X_1,X_2,X_3),\qquad U=\max(X_1,X_2,X_3).
\]
For \(0<a<1/2\), define the strictly increasing function \(g_a:\{1,2,3,4}\to\mathbb R\) by
\[
g_a(1)=0,\qquad g_a(2)=a,\qquad g_a(3)=1-a,\qquad g_a(4)=1.
\]
Then
\[
\operatorname{Corr}(g_a(L),g_a(U))=
\frac{-7a^2+4a+4}{95a^2-68a+28}.
\]
The ordinary extreme-order correlation is
\[
\operatorname{Corr}(L,U)=\frac{41}{143}.
\]
Moreover,
\[
\operatorname{Corr}(g_a(L),g_a(U))-\frac{41}{143}
=
\frac{-96(3a-1)(17a-6)}{143(95a^2-68a+28)}.
\]
The denominator is positive, so the transformed correlation is strictly larger exactly when
\[
\frac13<a<\frac6{17}.
\]
Thus the proposed relation \(\rho_N=R_N^{\prime\prime}=R_N^{\prime}\) for discrete-uniform order statistics fails already for \((N,i,j,n)=(4,1,3,3)\): every \(a\) in the displayed open interval gives a strictly increasing witness and hence
\[
R_4''(1,3:3)>\rho_4(1,3:3).
\]
Within this reflection-symmetric family, the unique maximizer is
\[
a_*=6-4\sqrt2,
\]
where
\[
\operatorname{Corr}(g_{a_*}(L),g_{a_*}(U))=
\frac{5+6\sqrt2}{47}
>
\frac{41}{143}.
\]

## Assumptions and scope
The parent distribution is exactly uniform on the four-point lattice \(\{1,2,3,4}\), the sample size is exactly three, and the order statistics are the minimum and maximum. The quantity \(R_4''(1,3:3)\) is the supremum of \(\operatorname{Corr}(g(L),g(U))\) over nondecreasing nonconstant functions \(g\) on the four-point support, while \(R_4'(1,3:3)\) removes the monotonicity restriction but still applies the same function to both order statistics. The finding proves a strict lower bound for both suprema and disproves their proposed equality with the ordinary correlation. It does not determine the global exact value of either supremum.

## Proof
For \(1\le i\le j\le4\), the number of ordered triples with minimum \(i\) and maximum \(j\) is \(1\) when \(i=j\), while for \(i<j\) it is
\[
(j-i+1)^3-2(j-i)^3+(j-i-1)^3=6(j-i).
\]
Since there are \(4^3=64\) ordered triples, the joint probability matrix of \((L,U)\), multiplied by \(64\), is
\[
\begin{pmatrix}
1&6&12&18\\
0&1&6&12\\
0&0&1&6\\
0&0&0&1
\end{pmatrix}.
\]
Its row sums are \((37,19,7,1)\), and its column sums are \((1,7,19,37)\).

For \(g_a=(0,a,1-a,1)\), direct summation gives
\[
\mathbb E[g_a(L)]=\frac{3a+2}{16},\qquad
\mathbb E[g_a(U)]=\frac{14-3a}{16}.
\]
Because \(g_a(5-k)=1-g_a(k)\) and \(U\) is the reflected version of \(L\), the two transformed variances are equal. Exact calculation gives
\[
\operatorname{Var}(g_a(L))=
\operatorname{Var}(g_a(U))=
\frac{95a^2-68a+28}{256},
\]
and
\[
\operatorname{Cov}(g_a(L),g_a(U))=
\frac{-7a^2+4a+4}{256}.
\]
This yields the stated correlation formula.

The affine transform of the lattice corresponds to \(a=1/3\), so substitution gives
\[
\operatorname{Corr}(L,U)=\frac{41}{143}.
\]
Subtracting this value from the general formula and reducing gives
\[
\frac{-96(3a-1)(17a-6)}{143(95a^2-68a+28)}.
\]
The quadratic denominator has discriminant \((-68)^2-4\cdot95\cdot28=-6016<0\) and positive leading coefficient, hence it is positive for every real \(a\). Therefore the sign is positive exactly for \(1/3<a<6/17\).

For the last statement, differentiating the one-parameter correlation gives
\[
\frac{d}{da}\operatorname{Corr}(g_a(L),g_a(U))
=
\frac{96(a^2-12a+4)}{(95a^2-68a+28)^2}.
\]
The only critical point in \((0,1/2)\) is \(a_*=6-4\sqrt2\), and the derivative changes from positive to negative there. Substitution simplifies to
\[
\frac{5+6\sqrt2}{47}.
\]
Finally,
\[
\frac{5+6\sqrt2}{47}-\frac{41}{143}
=
\frac{6(143\sqrt2-202)}{6721}>0,
\]
because \(2\cdot143^2=40898>40804=202^2\).

## Verification
The accompanying script `verify.py` independently enumerates all \(64\) ordered triples for the rational witness \(a=7/20\), checks the exact transformed correlation
\[
\frac{1817}{6335}=\frac{41}{143}+\frac{96}{905905},
\]
and checks the polynomial identities used for the correlation difference and derivative. The script uses only exact integer and rational arithmetic for these assertions. The infinite or continuous part of the claim is not inferred from enumeration; it follows from the displayed algebraic formulas and sign analysis.

## Relationship to prior work
Papadatos introduced \(R_N'\) and \(R_N''\) for order statistics from a discrete uniform parent and reported preliminary calculations suggesting
\[
\rho_N=R_N''=R_N'<R_N
\]
for all indices and sample sizes. For the extreme pair from three observations, the paper specifically records
\[
R_N'(1,3:3)=\frac{3-7N^{-2}}{9-N^{-2}}
\]
as a formula checked for small \(N\). At \(N=4\), that expression equals \(41/143\), which is the ordinary correlation, whereas the strictly increasing family above gives a larger value. Hence the proposed same-transform equality fails in the smallest four-point case considered here.

A separate 2021 paper by López-Blázquez and Salamanca-Miño studies unrestricted maximal correlation of order statistics from discrete parents and develops numerical optimization because closed forms are generally unavailable. That problem permits two different transformations and therefore concerns \(R_N\), not the same-transform monotone quantity \(R_N''\) disproved here. Related later finite-support work on varying the parent probability vector addresses a different optimization variable and does not imply this counterexample.

## Limitations
The finding is deliberately local in parameter space: it disproves a published general relation through one natural finite model and, more strongly, an open interval of monotone transforms. It does not compute the exact global values of \(R_4''(1,3:3)\) or \(R_4'(1,3:3)\), does not classify all maximizing transforms, and does not address other support sizes or order-statistic pairs. A differently phrased prior counterexample could exist in poorly indexed literature, although targeted searches for the exact notation, four-point model, same-transform monotone correlation, and corrections to the source did not locate one.

## References
1. N. Papadatos, “A discrete analogue of Terrell’s characterization of rectangular distributions,” arXiv:2205.14360v1, 28 May 2022; later published in *Mathematical Methods of Statistics* 32 (2023), 122–132, DOI:10.3103/S1066530723020035.
2. F. López-Blázquez and B. Salamanca-Miño, “Automatic differentiation and maximal correlation of order statistics from discrete parents,” *Computational Statistics* 36 (2021), 2889–2915, DOI:10.1007/s00180-021-01103-5.
