# The sharp pairwise-difference weaving bound needs a square-root term

## Finding
Theorem 4 of Alizadeh--Sadri, *Constructions of weaving continuous \(g\)-frames for operators in Hilbert spaces*, states a sufficient pairwise-difference condition for a family of continuous \(K\)-\(g\)-frames to be woven. Its qualitative conclusion is correct, but its advertised universal lower frame bound is too large.

For
\[
E_i(J;f)=\int_J\|\Lambda_{\omega i}f\|^2\,d\mu(\omega)
\]
and
\[
D_{ij}(J;f)
=
\int_J\|(\Lambda_{\omega i}-\Lambda_{\omega j})f\|^2\,d\mu(\omega),
\]
assume
\[
D_{ij}(J;f)
\le
M\min\{E_i(J;f),E_j(J;f)\}
\]
for every \(i\ne j\), every measurable \(J\subseteq\Omega\), and every \(f\in H\). If
\[
A=\sum_{i=1}^m A_i,\qquad
B=\sum_{i=1}^m B_i
\]
are the sums of valid individual lower and upper bounds, then the sharp universal conclusion from these data is
\[
\frac{A}
{1+(m-1)(1+\sqrt M)^2}
\|K^*f\|^2
\le
\sum_{j=1}^m
\int_{\sigma_j}\|\Lambda_{\omega j}f\|^2\,d\mu(\omega)
\le
B\|f\|^2
\]
for every measurable partition \(\{\sigma_j\}_{j=1}^m\) of \(\Omega\).

The source instead prints the larger lower constant
\[
\frac{A}{1+(m-1)(M+1)}.
\]
That constant is false for every \(m\ge2\) and \(M>0\).

## Assumptions and scope
The notation is the source's continuous \(K\)-\(g\)-frame setting. Each
\[
\Lambda_{\omega i}:H\to H_\omega
\]
is bounded and measurable in the usual continuous-\(g\)-frame sense, and the individual families satisfy
\[
A_i\|K^*f\|^2
\le
E_i(\Omega;f)
\le
B_i\|f\|^2.
\]

No closed-range hypothesis on \(K\) is used. The correction concerns only the quantitative lower bound in Theorem 4; the pairwise hypothesis still implies wovenness.

The sharpness example is already one-dimensional and uses a one-point measure space, so there are no convergence, measurability, or range-closure subtleties.

## Proof
Fix a measurable partition
\[
\Omega=\sigma_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}\sigma_m.
\]
For each pair \(i,j\), view the coefficient functions on \(\sigma_j\) as vectors in the Hilbert direct integral. Minkowski's inequality gives
\[
E_i(\sigma_j;f)^{1/2}
\le
D_{ij}(\sigma_j;f)^{1/2}
+
E_j(\sigma_j;f)^{1/2}.
\]
The pairwise hypothesis implies
\[
D_{ij}(\sigma_j;f)
\le
M E_j(\sigma_j;f),
\]
and hence
\[
E_i(\sigma_j;f)
\le
(1+\sqrt M)^2E_j(\sigma_j;f).
\]

Now sum the individual lower frame inequalities:
\[
A\|K^*f\|^2
\le
\sum_{i=1}^mE_i(\Omega;f)
=
\sum_{j=1}^m\sum_{i=1}^mE_i(\sigma_j;f).
\]
For fixed \(j\), retain \(E_j(\sigma_j;f)\) itself and bound the other \(m-1\) terms by the estimate above. This yields
\[
A\|K^*f\|^2
\le
\left(
1+(m-1)(1+\sqrt M)^2
\right)
\sum_{j=1}^mE_j(\sigma_j;f).
\]
Dividing proves the corrected lower bound.

For the upper bound,
\[
\sum_{j=1}^mE_j(\sigma_j;f)
\le
\sum_{j=1}^mE_j(\Omega;f)
\le
B\|f\|^2.
\]

To prove sharpness, fix arbitrary \(m\ge2\) and \(M>0\), and put
\[
c=1+\sqrt M.
\]
Take
\[
\Omega=\{\omega_0\},\qquad
\mu(\{\omega_0\})=1,\qquad
H=H_{\omega_0}=\mathbb C,\qquad
K=I.
\]
Define
\[
\Lambda_{\omega_0,1}=I,\qquad
\Lambda_{\omega_0,i}=cI
\quad(2\le i\le m).
\]
For \(i\ge2\),
\[
\|(\Lambda_{\omega_0,i}-\Lambda_{\omega_0,1})f\|^2
=
M\|f\|^2
=
M\min\{\|f\|^2,c^2\|f\|^2\},
\]
while differences between two indices at least \(2\) vanish. Thus the source hypothesis is satisfied exactly.

The individual exact lower bounds are
\[
A_1=1,\qquad A_i=c^2\quad(2\le i\le m),
\]
so
\[
A=1+(m-1)c^2.
\]
A partition assigning the unique point to family \(1\) has energy \(\|f\|^2\). Consequently the exact universal lower weaving bound of this example is \(1\).

The corrected formula gives
\[
\frac{1+(m-1)c^2}{1+(m-1)c^2}=1.
\]
The published formula gives
\[
\frac{1+(m-1)(M+2\sqrt M+1)}
{1+(m-1)(M+1)}
=
1+
\frac{2(m-1)\sqrt M}
{1+(m-1)(M+1)}
>1,
\]
contradicting the explicit weave. Therefore the corrected constant is sharp for every allowed \(m\) and \(M\).

## Verification
The full public text of the source was inspected at Theorem 4 and its complete proof. The theorem states the pairwise difference hypothesis and the denominator
\[
1+(m-1)(M+1).
\]
In the proof, the key estimate replaces the squared norm of a sum by the sum of the two squared norms:
\[
\|\Lambda_{\omega i}f\|^2
\le
\|(\Lambda_{\omega i}-\Lambda_{\omega j})f\|^2
+
\|\Lambda_{\omega j}f\|^2.
\]
That inequality is false in general because the cross term has been omitted.

The repaired proof uses Minkowski before squaring, which gives the exact factor
\[
(1+\sqrt M)^2.
\]
The scalar sharpness family verifies every hypothesis symbolically and attains equality in the corrected universal bound.

A later 2022 paper on generalized continuous \(K\)-weaving frames uses, in its proof, the coarser safe factor
\[
2(M+1).
\]
Since
\[
(1+\sqrt M)^2\le2(M+1),
\]
that proof mechanism is compatible with the correction here but does not give the sharp constant.

## Relationship to prior work
The 2021 source is the exact primary statement being corrected. Its pairwise hypothesis is a natural continuous-\(K\)-\(g\)-frame analogue of perturbative weaving criteria.

The 2022 paper *Generalized Continuous \(K\)-Weaving Frames* contains a closely related sufficient-condition proof. Its displayed estimate uses the elementary factor \(2(M+1)\), which avoids the missing-cross-term error but is strictly weaker than the sharp factor \((1+\sqrt M)^2\) unless \(M=1\).

Earlier continuous weaving \(g\)-frame literature establishes qualitative perturbation and weaving criteria, but the checked full-text and indexed statements do not provide the sharp all-\(m\), all-\(M\) correction above.

Targeted searches using the source DOI, theorem number, published denominator, the square-root denominator, pairwise-difference aliases, and correction terminology did not locate an indexed erratum or an equivalent sharp correction.

## Limitations
The theorem proved here optimizes the universal lower guarantee obtainable from the source's stated pairwise inequality together with the summed individual lower bound \(A\). It does not compute the exact weaving lower bound of a fixed family from finer geometric data.

The sharpness construction uses exact individual lower bounds. If deliberately nonoptimal lower bounds are inserted into \(A\), both the published and corrected numerical guarantees weaken accordingly.

An unindexed note, thesis, or informal correction may contain the same square-root factor.

## References
1. E. Alizadeh and V. Sadri, *Constructions of weaving continuous \(g\)-frames for operators in Hilbert spaces*, Problems of Analysis. Issues of Analysis 10(28)(2) (2021), 3--17, DOI 10.15393/j3.art.2021.9310.
2. Shipra, Chander Shekhar and R. Chugh, *Generalized Continuous \(K\)-Weaving Frames*, Jordan Journal of Mathematics and Statistics 15(4B) (2022), 1111--1126, DOI 10.47013/15.4.21.
3. E. Alizadeh and V. Sadri, *On continuous weaving \(g\)-frames in Hilbert spaces*, Wavelets and Linear Algebra 7(1) (2020), 23--36, DOI 10.22072/wala.2020.114423.1248.
