# Correct endemic-equilibrium multiplicity for a saturated-treatment vector–host model

## Finding

The published endemic-equilibrium classification for the saturated-treatment vector–host model is internally inconsistent. The source reduces every positive endemic equilibrium to a positive root of
\[
C_0 I_h^2+C_1 I_h+C_2=0,
\]
where, when the saturation parameters satisfy \(b>0\) and \(u>0\),
\[
C_0>0
\]
and
\[
C_2=\mu_h\mu_v^2(\delta_h+\mu_h+\gamma u)(1-\mathcal R_0^2).
\]

The correct positive-root classification is therefore completely determined by the signs of \(C_2\), \(C_1\), and the discriminant
\[
\Delta=C_1^2-4C_0C_2.
\]

If
\[
\mathcal R_0>1,
\]
then \(C_2<0\), so the two roots have opposite signs. Hence there is exactly one positive endemic root.

If
\[
\mathcal R_0=1,
\]
then \(C_2=0\), and
\[
I_h(C_0I_h+C_1)=0.
\]
Besides the disease-free root, a positive endemic root exists exactly when
\[
C_1<0,
\]
in which case it is
\[
I_h=-\frac{C_1}{C_0}.
\]

If
\[
\mathcal R_0<1,
\]
then \(C_2>0\), so any two real roots have the same sign. Their sum is
\[
-\frac{C_1}{C_0}.
\]
Thus there are two distinct positive endemic roots exactly when
\[
C_1<0,
\qquad
\Delta>0.
\]
There is one positive double root exactly when
\[
C_1<0,
\qquad
\Delta=0,
\]
and there is no positive endemic root otherwise.

This directly corrects the third bullet of Lemma 3.1, which states that with nonzero saturation and \(\mathcal R_0<1\) the quadratic has one sign change and hence a unique feasible endemic equilibrium. A quadratic with \(C_0>0\) and \(C_2>0\) cannot have exactly one simple positive root. Uniqueness in the subthreshold regime occurs only on the double-root fold.

The contradiction is realized by the admissible parameter choice
\[
\mu_h=\mu_v=\delta_h=\gamma=u=\alpha_1=\alpha_2=\beta_2=\Lambda_v=1,
\]
\[
b=100,
\qquad
\Lambda_h=10,
\qquad
\beta_1=\frac{29}{100}.
\]
For this choice,
\[
\mathcal R_0^2=\frac{29}{30}<1,
\]
while the source's own coefficients are
\[
C_0=658,
\qquad
C_1=-\frac{8013}{100},
\qquad
C_2=\frac1{10},
\]
with
\[
\Delta=\frac{61576169}{10000}>0.
\]
The two positive roots are
\[
I_h^{(1)}\approx0.00126103019756310,
\qquad
I_h^{(2)}\approx0.120517085303957.
\]
They generate two distinct positive endemic equilibria of the original five-dimensional model.

## Assumptions and scope

The model is the five-compartment vector–host system printed in the source, with positive recruitment, mortality, transmission, saturation, and treatment parameters. The correction concerns the saturated-treatment case
\[
b>0,
\qquad
u>0,
\]
where the source denotes the treatment-control factor by \(u\); in the formulas below that source notation \(u\) is retained.

The result classifies positive roots of the exact endemic-equilibrium polynomial printed by the source and verifies that the corresponding reconstructed states satisfy the original equilibrium equations. It does not classify local or global stability of the two subthreshold endemic equilibria, nor does it claim that every parameter set with \(\mathcal R_0<1\) exhibits backward bifurcation.

## Proof

For \(b,u>0\), every factor in the printed coefficient
\[
C_0=bu(\delta_h+\mu_h)
\left[
\mu_h\bigl(\alpha_1\beta_2\Lambda_v+
\mu_v(\beta_2+\alpha_2\mu_v)\bigr)
+\beta_1\beta_2\Lambda_v
\right]
\]
is positive, so \(C_0>0\).

The source gives
\[
C_2=\mu_h\mu_v^2(\delta_h+\mu_h+\gamma u)
(1-\mathcal R_0^2).
\]
Therefore the sign of \(C_2\) is the sign of \(1-\mathcal R_0^2\).

When \(\mathcal R_0>1\), the product of the two roots is
\[
\frac{C_2}{C_0}<0,
\]
so the roots are real and have opposite signs. Exactly one is positive.

When \(\mathcal R_0=1\), the polynomial factors as
\[
I_h(C_0I_h+C_1),
\]
which gives the threshold statement immediately.

When \(\mathcal R_0<1\), one has \(C_2/C_0>0\). If real roots exist, they have the same sign. Their sum is
\[
-\frac{C_1}{C_0}.
\]
Hence they are positive exactly when \(C_1<0\). Distinctness is exactly \(\Delta>0\), while \(\Delta=0\) gives the unique positive double root. If \(\Delta<0\), there is no real endemic root; if \(C_1\ge0\), any real roots are nonpositive.

For the explicit witness, the reproduction number satisfies
\[
\mathcal R_0^2
=
\frac{\beta_1\beta_2\Lambda_h\Lambda_v}
{\mu_v^2\mu_h(\mu_h+\delta_h+\gamma u)}
=
\frac{29}{30}.
\]
Direct substitution into the printed coefficients yields the stated exact values of \(C_0,C_1,C_2\), and \(\Delta\).

For either positive root \(I_h\), the remaining equilibrium coordinates can be reconstructed directly from the original equations as
\[
S_v=\frac{1+I_h}{1+2I_h},
\qquad
I_v=\frac{I_h}{1+2I_h},
\]
\[
S_h=\frac{10}{1+(29/100)I_v/(1+I_v)},
\qquad
R_h=\frac{I_h}{1+100I_h}.
\]
All coordinates are positive. Substitution into the five equilibrium equations gives zero residuals, completing the witness.

## Verification

The bundled `verify.py` uses exact rational arithmetic for \(\mathcal R_0^2\), \(C_0\), \(C_1\), \(C_2\), and \(\Delta\). It then computes the two positive roots and reconstructs all five equilibrium coordinates from the original model equations.

For the smaller root it obtains approximately
\[
(S_h,I_h,R_h,S_v,I_v)
=
(9.9963581218,0.0012610302,0.0011198178,0.9987421422,0.0012578578),
\]
and for the larger root approximately
\[
(9.7497320126,0.1205170853,0.0092338168,0.9028897929,0.0971102071).
\]
All five differential-equation residuals are below the numerical tolerance used by the checker.

## Relationship to prior work

Khan, Iqbal, Khan, and Alzahrani (2020), DOI 10.3934/mbe.2020220, is the primary source. Its equation (3.1) gives the quadratic and its coefficients. The second bullet of Lemma 3.1 correctly identifies the possibility of two positive subthreshold roots under a negative linear coefficient and a nonnegative discriminant, but the immediately following bullet states a generic unique feasible subthreshold endemic equilibrium in the same saturated-treatment regime. The two statements are incompatible except on the discriminant-zero fold.

Backward bifurcation in vector-borne epidemic models is established prior theory. Lashari, Hattaf, Zaman, and Li (2013), DOI 10.12785/amis/070138, study backward bifurcation and optimal control in a different vector-borne system. Hu, Yin, and Wang (2019), DOI 10.1155/2019/1352698, analyze a different vector-borne model with saturated infection and cure rates; their full text explicitly classifies quadratic equilibrium roots through coefficient signs. Those works support the standard role of root multiplicity but do not state the correction to Lemma 3.1 of the 2020 model or the witness above.

## Limitations

The finding is an equilibrium-existence correction, not a stability theorem. In the subthreshold two-root regime, additional analysis is required to decide which endemic equilibrium is stable and to establish a complete backward-bifurcation diagram.

The explicit witness is chosen to make the algebra transparent and lies in the model's positive parameter domain; it is not asserted to be a calibrated dengue or malaria parameter set.

The source's later optimal-control calculations are not assessed here.

## References

1. M. A. Khan, N. Iqbal, Y. Khan, E. Alzahrani, “A biological mathematical model of vector-host disease with saturated treatment function and optimal control strategies,” Mathematical Biosciences and Engineering 17 (2020), 3972–3997. DOI: 10.3934/mbe.2020220.
2. Z. Hu, S. Yin, H. Wang, “Stability and Hopf Bifurcation of a Vector-Borne Disease Model with Saturated Infection Rate and Reinfection,” Computational and Mathematical Methods in Medicine (2019), Article 1352698. DOI: 10.1155/2019/1352698.
3. A. A. Lashari, K. Hattaf, G. Zaman, X.-Z. Li, “Backward bifurcation and optimal control of a vector borne disease,” Applied Mathematics & Information Sciences 7 (2013), 301–309. DOI: 10.12785/amis/070138.
