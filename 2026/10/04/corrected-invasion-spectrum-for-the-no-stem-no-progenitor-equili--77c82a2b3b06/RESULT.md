# Corrected invasion spectrum for the no-stem/no-progenitor equilibrium in a four-stage cell lineage

## Finding

Singh et al. study a four-stage lineage with stem cells \(a\), progenitor cells \(b\), myeloid cells \(c\), and mature cells \(d\). In the dimensionless ordinary model, the three self-renewing compartments have feedback factor \((1+ld)^{-1}\). Define
\[
R_a=(2u_a-1)s_a,
\qquad
R_b=\frac{(2u_b-1)s_b}{g_b},
\qquad
R_c=\frac{(2u_c-1)s_c}{g_c}.
\]

The source's no-stem/no-progenitor equilibrium is
\[
E_1^*=(0,0,c_1,d_1),
\qquad
 d_1=\frac{R_c-1}{l},
\]
with
\[
 c_1=\frac{g_dR_c}{2(1-u_c)s_c}d_1,
\]
and it exists for \(R_c>1\). In particular,
\[
1+ld_1=R_c.
\]

Theorem 5.3 prints the first two eigenvalues as
\[
\frac{R_a}{R_b}-1
\quad\text{and}\quad
 g_b\frac{R_b}{R_c}-g_d.
\]
Those expressions are not the eigenvalues of the Jacobian of the displayed model at \(E_1^*\).

The exact vector-field spectrum is
\[
\lambda_a=\frac{R_a}{R_c}-1,
\qquad
\lambda_b=g_b\left(\frac{R_b}{R_c}-1\right),
\]
together with the two roots of
\[
\lambda^2+
 g_d\left(2-\frac1{R_c}\right)\lambda
+
 g_cg_d\left(1-\frac1{R_c}\right)=0.
\]
For \(R_c>1\), both coefficients of this quadratic are positive, so its two roots have negative real parts.

Therefore the ordinary model has the exact local-stability classification
\[
E_1^*\text{ locally asymptotically stable}
\quad\Longleftrightarrow\quad
R_c>\max\{R_a,R_b\},
\]
with instability when either \(R_a>R_c\) or \(R_b>R_c\). Equality is nonhyperbolic.

The paper's stated stable chain
\[
R_b>R_a,
\qquad
R_c>R_b
\]
is sufficient for this corrected condition, but it is not necessary. More importantly, the eigenvalues displayed in Theorem 5.3 can have the wrong signs.

For example, choose
\[
u_a=\frac34,
\qquad s_a=3,
\qquad
u_b=\frac45,
\qquad s_b=2,
\qquad g_b=1,
\]
\[
u_c=\frac34,
\qquad s_c=4,
\qquad g_c=1,
\qquad g_d=\frac1{10},
\qquad l=1.
\]
Then
\[
R_a=\frac32,
\qquad
R_b=\frac65,
\qquad
R_c=2,
\]
and
\[
E_1^*=\left(0,0,\frac1{10},1\right).
\]
The exact upstream invasion eigenvalues are
\[
\lambda_a=-\frac14,
\qquad
\lambda_b=-\frac25,
\]
while the remaining pair has real part
\[
-\frac3{40}.
\]
Thus \(E_1^*\) is locally asymptotically stable in the ordinary model even though \(R_b<R_a<R_c\). The source formulas instead return
\[
\frac{R_a}{R_b}-1=\frac14
\]
and
\[
 g_b\frac{R_b}{R_c}-g_d=\frac12,
\]
reversing both upstream invasion signs.

## Assumptions and scope

The calculation uses the right-hand side printed for the four-compartment model and the source definitions of \(R_a,R_b,R_c\). Rates \(g_b,g_c,g_d,l\) are positive, \(0\le u_a,u_b,u_c<1\), and the equilibrium considered satisfies \(R_c>1\).

The complete stability equivalence above is for the source's ordinary differential-equation model. The paper subsequently applies an Atangana-Baleanu derivative in Caputo sense to the same right-hand side. The Jacobian correction remains valid for that fractional formulation, but this finding does not assert a complete fractional-order stability criterion; such a criterion must be re-evaluated from the corrected spectrum.

## Proof

Write the ordinary right-hand side in the triangular lineage form
\[
\dot a=\left(f_{a,1}(d)-1\right)a,
\]
\[
\dot b=f_{a,2}(d)a+\left(f_{b,1}(d)-g_b\right)b,
\]
\[
\dot c=f_{b,2}(d)b+\left(f_{c,1}(d)-g_c\right)c,
\]
\[
\dot d=f_{c,2}(d)c-g_dd,
\]
where
\[
f_{a,1}(d)=\frac{R_a}{1+ld},
\quad
f_{b,1}(d)=\frac{g_bR_b}{1+ld},
\quad
f_{c,1}(d)=\frac{g_cR_c}{1+ld}.
\]
At \(E_1^*\), the source equilibrium formula gives
\[
1+ld_1=R_c.
\]
Because \(a=b=0\), all derivatives with respect to \(d\) in the first two rows are multiplied by zero. Hence the two upstream diagonal entries are exactly
\[
f_{a,1}(d_1)-1=\frac{R_a}{R_c}-1
\]
and
\[
f_{b,1}(d_1)-g_b
=g_b\left(\frac{R_b}{R_c}-1\right).
\]
The source proof instead substitutes \(R_b\) into the first denominator and replaces the progenitor loss \(g_b\) by \(g_d\).

For the lower \((c,d)\) block, define
\[
h_c=2(1-u_c)s_c.
\]
Then
\[
f_{c,2}(d)=\frac{h_c}{1+ld}
\]
and the equilibrium relation is
\[
\frac{h_c}{R_c}c_1=g_dd_1.
\]
The lower block is
\[
\begin{pmatrix}
0&-\dfrac{lg_cc_1}{R_c}\\[5pt]
\dfrac{h_c}{R_c}&-g_d-\dfrac{lh_cc_1}{R_c^2}
\end{pmatrix}.
\]
Using
\[
d_1=\frac{R_c-1}{l}
\]
and
\[
c_1=\frac{g_dR_cd_1}{h_c},
\]
its trace becomes
\[
-g_d\left(2-\frac1{R_c}\right)
\]
and its determinant becomes
\[
g_cg_d\left(1-\frac1{R_c}\right).
\]
This proves the quadratic factor stated above. When \(R_c>1\), its trace is negative and determinant positive, so both roots have negative real part.

Thus only the two upstream invasion eigenvalues can change stability. They are both negative exactly when
\[
R_a<R_c
\quad\text{and}\quad
R_b<R_c.
\]
This yields the claimed complete ordinary-model classification.

## Verification

The bundled `verify.py` constructs the symbolic Jacobian, substitutes the source equilibrium identities, and verifies the factorization
\[
\left(\lambda-\lambda_a\right)
\left(\lambda-\lambda_b\right)
\left[
\lambda^2+
 g_d\left(2-\frac1{R_c}\right)\lambda
+g_cg_d\left(1-\frac1{R_c}\right)
\right].
\]

It also evaluates the explicit witness
\[
R_a=\frac32,
\quad
R_b=\frac65,
\quad
R_c=2,
\quad
 g_b=g_c=1,
\quad
 g_d=\frac1{10},
\]
and checks the corrected eigenvalues and the two positive values returned by the source formulas.

The complete stability result is analytic; finite computation only replays symbolic algebra and exact rational arithmetic.

## Relationship to prior work

Singh et al. (2022), DOI 10.3934/math.2022289, introduce the four-stage stem/progenitor/myeloid/mature model. Their Theorem 5.1 gives the no-stem/no-progenitor equilibrium with \(d_1=(R_c-1)/l\), while Theorem 5.3 prints the inconsistent first two eigenvalues and states stability under the ordered chain \(R_b>R_a\), \(R_c>R_b\). The proof explicitly uses the identity \(1+ld_1=R_b\), although the equilibrium formula gives \(1+ld_1=R_c\).

Nakata, Getto, Marciniak-Czochra, and Alarcón (2011), DOI 10.1080/17513758.2011.558214, analyze two- and three-compartment hierarchical cell-production models with mature-cell feedback and reproduction numbers. Their full analysis shows how an intermediate progenitor stage changes local stability, but their model has no additional myeloid stage and therefore does not contain the two-upstream-invasion spectrum at the four-stage equilibrium considered here.

The corrected result is therefore not a new general theory of hierarchical cell production. It is a complete source-specific classification of the boundary equilibrium created by the added myeloid compartment.

## Limitations

The finding does not provide a full local-stability theorem for the Atangana-Baleanu-Caputo fractional system. Fractional stability depends on the relevant fractional characteristic condition, and the source's fractional conclusion must be recomputed from the corrected Jacobian spectrum.

The classification is local. It does not determine the global basin of the no-stem/no-progenitor equilibrium or the nonlinear behavior at the nonhyperbolic boundaries \(R_a=R_c\) or \(R_b=R_c\).

The explicit witness is a mathematically admissible parameter choice used to expose the sign error; it is not presented as an empirical calibration.

## References

1. R. Singh, A. U. Rehman, M. Masud, H. A. Alhumyani, S. Mahajan, A. K. Pandit, P. Agarwal, “Fractional order modeling and analysis of dynamics of stem cell differentiation in complex network,” AIMS Mathematics 7 (2022), 5175–5198. DOI: 10.3934/math.2022289.
2. Y. Nakata, P. Getto, A. Marciniak-Czochra, T. Alarcón, “Stability analysis of multi-compartment models for cell production systems,” Journal of Biological Dynamics 6 (2012), 2–18. DOI: 10.1080/17513758.2011.558214.
