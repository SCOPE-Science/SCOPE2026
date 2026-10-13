# A sharp high-media-growth trichotomy for endemic equilibria in a fear–awareness epidemic model

## Finding

Consider the fear–media epidemic model
\[
\dot S=\Lambda-\frac{\beta SI}{1+\omega I}-\frac{\lambda MS}{p+M}+\lambda_0A-dS+\nu I,
\]
\[
\dot I=\frac{\beta SI}{1+\omega I}-(\nu+\alpha+d)I,
\]
\[
\dot A=\frac{\lambda MS}{p+M}-(\lambda_0+d)A,
\qquad
\dot M=rI-r_0(M-M_0).
\]
Let
\[
C=\nu+\alpha+d,
\qquad
b=\lambda_0+d,
\qquad
q=\frac{\lambda}{b},
\qquad
\mathcal R_0=\frac{\beta\Lambda}{dC}.
\]
Assume the disease-free threshold of the source satisfies \(\mathcal R_1>1\), so the unique positive endemic equilibrium exists. Write its infected and media coordinates as \(I_r\) and \(M_r\), emphasizing dependence on the media-advertisement growth rate \(r\).

Define
\[
h(M)=\frac{M}{p+M},
\qquad
\kappa=\frac{\mathcal R_0-1}{q},
\]
and
\[
D(M)=1+\frac{\alpha}{d}+\frac{C\omega}{\beta}\bigl(1+qh(M)\bigr),
\qquad
D_\infty=1+\frac{\alpha}{d}+\frac{C\omega}{\beta}(1+q).
\]
Then the endemic equilibrium obeys
\[
I_rD(M_r)=\frac{Cq}{\beta}\bigl(\kappa-h(M_r)\bigr),
\qquad
M_r=M_0+\frac{r}{r_0}I_r.
\]
These two identities give a complete high-\(r\) trichotomy.

If
\[
\lambda>(\mathcal R_0-1)(\lambda_0+d),
\]
then
\[
M_r\to M_\infty=\frac{p\kappa}{1-\kappa}
\]
and
\[
I_r\sim\frac{r_0(M_\infty-M_0)}{r}.
\]

If
\[
\lambda=(\mathcal R_0-1)(\lambda_0+d),
\]
then
\[
M_r\to\infty,
\qquad
I_r\to0,
\]
with the critical law
\[
\sqrt r\,I_r\to
\sqrt{\frac{r_0Cqp}{\beta D_\infty}}.
\]

If
\[
\lambda<(\mathcal R_0-1)(\lambda_0+d),
\]
then
\[
M_r\to\infty,
\qquad
I_r\to
\frac{(C/\beta)\,[\mathcal R_0-(1+q)]}{D_\infty}>0.
\]
Thus saturation in the awareness-transfer term creates a sharp boundary between inverse-linear suppression, inverse-square-root critical suppression, and a positive endemic floor.

For the parameter values in Table 1 of the source,
\[
\mathcal R_0=\frac{7500}{4001},
\qquad
q=\frac{100}{67},
\qquad
\kappa=\frac{234433}{400100}<1,
\]
so the first regime applies. The limiting advertisement level is
\[
M_\infty=\frac{281319600}{165667}=1698.1028207\ldots,
\]
and
\[
I_r\sim\frac{1984861}{331334}\frac1r
=\frac{5.9905141036\ldots}{r}.
\]

## Assumptions and scope

All demographic and transition parameters are positive, and \(\omega\ge0\). The result concerns the positive equilibrium of the printed four-dimensional ODE system.

The source's disease-free threshold can be written
\[
\mathcal R_1=
\frac{\mathcal R_0}{1+q h(M_0)}.
\]
The assumption \(\mathcal R_1>1\) is therefore exactly
\[
h(M_0)<\kappa.
\]
It guarantees the source's unique positive endemic equilibrium for each finite \(r>0\).

The theorem concerns equilibrium geometry, not the attracting set for large \(r\). The source reports that increasing \(r\) can destabilize the endemic equilibrium through Hopf bifurcation. Accordingly, a small or vanishing equilibrium coordinate does not by itself imply trajectory-level eradication when that equilibrium is unstable.

## Proof

At a positive equilibrium, the infected equation gives
\[
S_r=\frac{C}{\beta}(1+\omega I_r).
\]
The aware equation gives
\[
A_r=q h(M_r)S_r,
\]
and the media equation gives
\[
M_r=M_0+\frac{r}{r_0}I_r.
\]

Adding the susceptible, infected, and aware equations yields
\[
\dot N=\Lambda-dN-\alpha I,
\qquad
N=S+I+A.
\]
Hence at equilibrium
\[
S_r+I_r+A_r=\frac{\Lambda-\alpha I_r}{d}.
\]
Substituting the two expressions for \(S_r\) and \(A_r\), and using
\[
\mathcal R_0=\frac{\beta\Lambda}{dC},
\]
gives the exact scalar identity
\[
I_rD(M_r)=\frac{Cq}{\beta}\bigl(\kappa-h(M_r)\bigr).
\]
Because \(I_r>0\), one necessarily has
\[
h(M_r)<\kappa.
\]

Suppose first that \(\kappa<1\). Since \(h\) is strictly increasing,
\[
M_r<M_\infty:=\frac{p\kappa}{1-\kappa}.
\]
The relation
\[
I_r=\frac{r_0(M_r-M_0)}{r}
\]
therefore implies \(I_r\to0\). The scalar identity then forces
\[
h(M_r)\to\kappa,
\]
so \(M_r\to M_\infty\). Finally,
\[
rI_r=r_0(M_r-M_0)\to r_0(M_\infty-M_0),
\]
which is the claimed \(r^{-1}\) law. The strict inequality \(M_\infty>M_0\) follows from \(h(M_0)<\kappa\).

Now suppose \(\kappa=1\). The scalar identity is
\[
I_rD(M_r)=\frac{Cqp}{\beta(p+M_r)}.
\]
If a subsequence of \(M_r\) were bounded as \(r\to\infty\), then the media relation would give \(I_r\to0\), whereas the right-hand side above would stay bounded away from zero. Hence \(M_r\to\infty\), and consequently \(I_r\to0\) and \(D(M_r)\to D_\infty\). Combining the two equilibrium identities gives
\[
\frac{(M_r-M_0)(p+M_r)}{r}
=
\frac{Cqp}{\beta r_0D(M_r)}.
\]
Therefore
\[
\frac{M_r^2}{r}\to\frac{Cqp}{\beta r_0D_\infty},
\]
and multiplication by the media relation yields
\[
\sqrt r\,I_r\to
\sqrt{\frac{r_0Cqp}{\beta D_\infty}}.
\]

Finally suppose \(\kappa>1\). Since \(h(M)<1\),
\[
I_rD(M_r)
\ge
\frac{Cq}{\beta}(\kappa-1)>0.
\]
Because \(D(M_r)\le D_\infty\), the infected equilibrium is bounded below by a positive constant independent of \(r\). Hence the media relation forces \(M_r\to\infty\). Thus \(h(M_r)\to1\) and \(D(M_r)\to D_\infty\), and the scalar identity gives
\[
I_r\to
\frac{(C/\beta)\,[\mathcal R_0-(1+q)]}{D_\infty}>0.
\]
This proves all three regimes.

## Verification

The bundled `verify.py` uses exact rational arithmetic for all terminating-decimal Table 1 parameters. It checks the source threshold \(\mathcal R_1>1\), the regime inequality, the exact limiting media level, and the exact inverse-linear coefficient.

It also solves the exact equilibrium identity numerically for a sequence of large finite \(r\) values. The product \(rI_r\) approaches
\[
5.9905141036\ldots,
\]
matching the analytic coefficient. These finite calculations replay the Table 1 specialization; they are not used to prove the infinite-\(r\) theorem.

## Relationship to prior work

Misra, Tripathi, and Verma prove existence and uniqueness of the endemic equilibrium when \(\mathcal R_1>1\), show that its infected coordinate decreases with the growth rate of media advertisements, and numerically study variation of that equilibrium with \(r\). They also show that sufficiently large \(r\) can destabilize the endemic equilibrium through Hopf bifurcation. The source does not classify the limiting endemic level as \(r\to\infty\), identify the dissemination threshold separating vanishing and nonvanishing limits, or derive the critical \(r^{-1/2}\) law.

Misra, Rai, and Takeuchi study an earlier media-awareness epidemic model with a related saturating awareness-transfer mechanism. That model has a different media equation in which advertisement growth is reduced by the aware population. Its analysis establishes monotone dependence and Hopf behavior but does not imply the present high-feedback trichotomy.

A related exact observation for the earlier model concerns changing the maintained baseline number of advertisements. Varying that baseline changes the disease-free threshold itself. By contrast, in the present model \(r\) is an infection-driven feedback coefficient and does not enter \(\mathcal R_1\); the three asymptotic laws above arise from the coupled equilibrium relation \(M_r=M_0+rI_r/r_0\). Thus the earlier baseline threshold does not imply the inverse-linear, inverse-square-root, or positive-floor limits proved here.

A later paper by the same authors studies a modified fear, television, and social-media model. Its abstract describes a different feedback structure and stability analysis. Full text was not available through the lawful sources checked, so it remains a residual comparison risk rather than evidence of coverage.

## Limitations

The theorem describes the endemic equilibrium branch, including parameter regimes in which that equilibrium may be dynamically unstable. It does not classify the high-\(r\) periodic orbit born at Hopf bifurcation or prove that trajectory averages obey the same asymptotics.

The result does not estimate parameters from data or claim that increasing media feedback alone is a practical eradication strategy. In the first regime the disease-free equilibrium remains unstable for every finite \(r\) whenever \(\mathcal R_1>1\), even though the endemic equilibrium tends to zero in the singular limit.

The comparison with the later same-author model is limited by unavailable full text.

## References

1. A. K. Misra, K. K. Tripathi, M. Verma, “Modeling the effects of psychological fear and media-induced awareness on the dynamics of infectious diseases,” Discrete and Continuous Dynamical Systems - B 29 (2024), 909–936. DOI: 10.3934/dcdsb.2023118. Early access: 30 June 2023.
2. A. K. Misra, R. K. Rai, Y. Takeuchi, “Modeling the control of infectious diseases: Effects of TV and social media advertisements,” Mathematical Biosciences and Engineering 15 (2018), 1315–1343. DOI: 10.3934/mbe.2018061.
3. K. K. Tripathi, A. K. Misra, M. Verma, “Modeling the effects of psychological fear, TV and social media advertisements on the control of infectious diseases,” International Journal of Biomathematics (2025). DOI: 10.1142/S0218339025500147.
