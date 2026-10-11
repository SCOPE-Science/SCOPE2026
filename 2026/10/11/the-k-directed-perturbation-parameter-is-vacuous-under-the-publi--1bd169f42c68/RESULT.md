# The \(K\)-directed perturbation parameter is vacuous under the published quantifiers
## Finding
Theorem 4.1 of Alizadeh--Rahimi--Osgooei--Rahmani introduces a perturbation parameter \(\gamma\) through the term
\[
\gamma\|K^*f\|^2
\]
and consequently requires
\[
\max\left\{\lambda_2,\lambda_1+\frac{\gamma}{A}\right\}<1.
\]
Under the theorem's literal hypothesis, which is required for every \(f,g\in H\), the \(\gamma\)-term is mathematically redundant.

The exact conclusion from the stated hypothesis is stronger: if
\[
0\le\lambda_1<1,\qquad 0\le\lambda_2<1,
\]
then the perturbed family is a continuous \(K\)-\(g\)-frame with bounds
\[
\frac{1-\lambda_1}{1+\lambda_2}A
\quad\text{and}\quad
\frac{1+\lambda_1}{1-\lambda_2}B.
\]
No restriction on \(\gamma\) is needed.

These two multiplicative factors are sharp as universal constants determined by the displayed perturbation inequality and the original frame bounds.

## Assumptions and scope
Let \(\{\Lambda_\omega\}_{\omega\in\Omega}\) be a continuous \(K\)-\(g\)-frame with bounds \(A,B\), and let \(\{\Gamma_\omega\}_{\omega\in\Omega}\) satisfy the source hypothesis
\[
D(f,g)
\le
\lambda_1L(f,g)+\lambda_2G(f,g)+\gamma\|K^*f\|^2
\]
for every \(f,g\in H\), where
\[
D(f,g)=
\int_\Omega
\left|
\left\langle
(\Lambda_\omega^*\Lambda_\omega-\Gamma_\omega^*\Gamma_\omega)f,g
\right\rangle
\right|\,d\mu(\omega),
\]
\[
L(f,g)=
\int_\Omega
\left|
\left\langle
\Lambda_\omega^*\Lambda_\omega f,g
\right\rangle
\right|\,d\mu(\omega),
\]
and \(G(f,g)\) is defined analogously using \(\Gamma_\omega\).

The result concerns the quantitative content of Theorem 4.1 exactly as quantified in the source. It does not claim that an additive \(K\)-dependent perturbation term is intrinsically useless in other, differently normalized perturbation hypotheses.

## Proof
Fix \(f,g\in H\). For every real \(t>0\), apply the source hypothesis to \(f\) and \(tg\). Linearity of the inner product in the second variable up to the usual conjugation convention and the outer absolute value give
\[
tD(f,g)
\le
t\lambda_1L(f,g)+t\lambda_2G(f,g)+\gamma\|K^*f\|^2.
\]
After division by \(t\),
\[
D(f,g)
\le
\lambda_1L(f,g)+\lambda_2G(f,g)
+
\frac{\gamma}{t}\|K^*f\|^2.
\]
Letting \(t\to\infty\) proves
\[
D(f,g)
\le
\lambda_1L(f,g)+\lambda_2G(f,g).
\]

Now put \(g=f\). Because
\[
\left\langle\Lambda_\omega^*\Lambda_\omega f,f\right\rangle
=
\|\Lambda_\omega f\|^2
\]
and similarly for \(\Gamma_\omega\), write
\[
X(f)=\int_\Omega\|\Lambda_\omega f\|^2\,d\mu(\omega),
\qquad
Y(f)=\int_\Omega\|\Gamma_\omega f\|^2\,d\mu(\omega).
\]
The triangle inequality gives
\[
Y(f)\le D(f,f)+X(f)
\le
(1+\lambda_1)X(f)+\lambda_2Y(f).
\]
Therefore
\[
Y(f)\le
\frac{1+\lambda_1}{1-\lambda_2}X(f)
\le
\frac{1+\lambda_1}{1-\lambda_2}B\|f\|^2.
\]

Likewise,
\[
X(f)\le D(f,f)+Y(f)
\le
\lambda_1X(f)+(1+\lambda_2)Y(f),
\]
so
\[
Y(f)\ge
\frac{1-\lambda_1}{1+\lambda_2}X(f)
\ge
\frac{1-\lambda_1}{1+\lambda_2}A\|K^*f\|^2.
\]
This proves the corrected frame bounds.

For sharpness, take the one-point measure space of mass \(1\), \(H=\mathbb R\), \(K=I\), \(\Lambda=aI\), and \(\Gamma=bI\), with \(a>0\). The original exact frame bounds are
\[
A=B=a^2.
\]
The reduced perturbation hypothesis is exactly
\[
|a^2-b^2|
\le
\lambda_1a^2+\lambda_2b^2.
\]
At
\[
b^2=a^2\frac{1-\lambda_1}{1+\lambda_2},
\]
the inequality is an equality and the new exact lower and upper frame bound is the claimed lower factor times \(a^2\). At
\[
b^2=a^2\frac{1+\lambda_1}{1-\lambda_2},
\]
the inequality is again an equality and the exact frame bound is the claimed upper factor times \(a^2\). Hence neither universal multiplicative factor can be improved.

## Verification
The arXiv full text was inspected at Theorem 4.1 and its complete proof, and the two pages containing the theorem and lower-bound calculation were inspected visually.

The theorem explicitly requires its perturbation inequality for every \(f,g\in H\). Its first three terms scale linearly when \(g\) is replaced by \(tg\), while the final term
\[
\gamma\|K^*f\|^2
\]
does not. This mismatch is the entire mechanism of the correction.

The proof above uses only homogeneity, the triangle inequality, and the original continuous \(K\)-\(g\)-frame inequalities. The sharpness examples are exact scalar calculations.

## Relationship to prior work
The source cites Hua--Huang's work on stability of \(K\)-\(g\)-frames and classical perturbation results for \(g\)-frames as background. Those perturbation frameworks motivate quantitative stability estimates, but the present issue is specific to the mixed two-vector inequality printed in Theorem 4.1: an additive term independent of the universally quantified test vector \(g\) disappears under scaling.

Targeted searches for the exact source, theorem number, the published constants, \(\gamma\)-dependence, and homogeneity/scaling formulations did not locate an indexed erratum or a checked source stating the \(\gamma\)-free sharp bounds above.

The corrected statement does not conflict with perturbation theorems in which every error term has the same homogeneity as the tested coefficient expression.

## Limitations
The result is a correction of the theorem under its literal universal quantification over \(g\). If a different intended hypothesis fixed \(g\), normalized \(g\), or multiplied the \(\gamma\)-term by a norm of \(g\), this scaling argument would not apply and a genuinely \(K\)-dependent perturbation term could remain.

The sharpness assertion concerns universal constants derived only from \(\lambda_1,\lambda_2,A,B\) and the stated perturbation inequality.

## References
1. E. Alizadeh, A. Rahimi, E. Osgooei and M. Rahmani, *Continuous \(K\)-\(g\)-Frames in Hilbert Spaces*, arXiv:1712.03434; Bulletin of the Iranian Mathematical Society 45 (2019), 1091--1104, DOI 10.1007/s41980-018-0186-7.
2. D. Hua and Y. Huang, *\(K\)-\(g\)-Frames and Stability of \(K\)-\(g\)-Frames in Hilbert Spaces*, Journal of the Korean Mathematical Society 53(6) (2016), 1331--1345, DOI 10.4134/JKMS.j150499.
