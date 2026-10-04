# An irreducible breakthrough floor invalidates a reported vaccination threshold

## Finding

For the eight-class COVID-19 vaccination model of Ihsanjaya and Susyanto, the published next-generation calculation gives
\[
R_0(v)=\left(\beta_1\frac{\Lambda}{\mu+v}+\beta_2\frac{v\Lambda}{\mu(\mu+v)}\right)
\frac{\gamma(1-\omega)}{(\gamma+\mu)(\alpha_1+\alpha_2+\mu)}.
\]
Set
\[
q=\frac{\gamma(1-\omega)}{(\gamma+\mu)(\alpha_1+\alpha_2+\mu)},\qquad
R_S=\frac{\Lambda q\beta_1}{\mu},\qquad
R_V=\frac{\Lambda q\beta_2}{\mu}.
\]
Then the vaccination-rate dependence is exactly
\[
R_0(v)=\frac{\mu R_S+vR_V}{\mu+v}.
\]
Therefore \(R_0(v)\) is a weighted average of the zero-vaccination endpoint \(R_S\) and the infinite-vaccination endpoint \(R_V\). Its derivative is
\[
\frac{dR_0}{dv}=\frac{\mu(R_V-R_S)}{(\mu+v)^2},
\]
so increasing vaccination suppresses \(R_0\) exactly when \(\beta_2<\beta_1\). More importantly, if \(R_S>1\), vaccination alone can cross below threshold only if
\[
R_V<1.
\]
When \(R_S>1>R_V\), the unique threshold is
\[
v_c=\mu\frac{R_S-1}{1-R_V}.
\]

For the paper's Table 2 values,
\[
q\approx0.912611669304,
\qquad R_S\approx44272.5303859,
\qquad R_V\approx2.66178403547.
\]
Thus
\[
R_0(v)>1\qquad\text{for every }v\ge0.
\]
The breakthrough-infection coefficient \(\beta_2\) alone creates a supercritical floor, so no vaccination rate can yield the subthreshold regime claimed from those printed parameters.

At fixed Table 2 \(\beta_2\), solving \(R_0=1\) for \(\beta_1\) gives the actual boundary
\[
\beta_1(v)=\frac{\mu+v}{\Lambda q}-\frac{\beta_2v}{\mu}
=1.8408706096\times10^{-7}-0.00728364140571\,v.
\]
It is nonnegative only for
\[
v\le2.52740422964\times10^{-5},
\]
so the paper's reported critical value \(v\approx0.023\) cannot lie on a positive-\(\beta_1\) \(R_0=1\) boundary obtained from its Eq. (3.1) and Table 2.

The paper's Figure 1 parameter statement is independently inconsistent with disease-free stability. With
\[
v=0.4,\qquad \beta_1=0.000815,\qquad \beta_2=0.00000059,
\]
Eq. (3.1) gives
\[
R_0\approx3.66948154069.
\]
The disease-free infected subsystem then has a positive eigenvalue
\[
\lambda_+\approx0.180133902020,
\]
so that displayed disease-free equilibrium is linearly unstable.

## Assumptions and scope

All statements use the model exactly as printed in Eq. (2.1) and the reproduction number printed as Eq. (3.1). Parameters satisfy the paper's biological sign conditions, in particular \(\mu>0\), \(v\ge0\), and nonnegative transmission coefficients. The numerical contradictions use the decimal parameter values printed in Table 2 and in the paragraph introducing Figure 1.

The conclusion is about the published mathematical specification. It does not establish which parameter scaling, if any, was used in unreported simulation code.

## Proof

At the disease-free equilibrium printed in the source,
\[
S_0=\frac{\Lambda}{\mu+v},
\qquad
V_{S,0}=\frac{v\Lambda}{\mu(\mu+v)}.
\]
The paper's Eq. (3.1) can therefore be written as
\[
R_0(v)=q\bigl(\beta_1S_0+\beta_2V_{S,0}\bigr)
=\frac{\Lambda q}{\mu+v}
\left(\beta_1+\frac{\beta_2v}{\mu}\right).
\]
Substituting the definitions of \(R_S\) and \(R_V\) gives
\[
R_0(v)=\frac{\mu R_S+vR_V}{\mu+v}.
\]
Differentiation yields
\[
R_0'(v)=\frac{\mu(R_V-R_S)}{(\mu+v)^2}.
\]
This proves the exact monotonicity criterion. If \(R_S>1\), the limit
\[
\lim_{v\to\infty}R_0(v)=R_V
\]
shows that a subthreshold vaccination regime is possible exactly when \(R_V<1\). Solving \(R_0(v)=1\) in that case gives
\[
v_c=\mu\frac{R_S-1}{1-R_V}.
\]

For the paper's Table 2 coefficients, direct substitution gives \(R_V\approx2.66178403547>1\), while \(R_S\approx44272.5303859>1\). Since \(R_0(v)\) is a convex combination of these two numbers, it is greater than one for every nonnegative \(v\).

Solving the same equation for \(\beta_1\) instead gives
\[
\beta_1(v)=\frac{\mu+v}{\Lambda q}-\frac{\beta_2v}{\mu}.
\]
Substitution of Table 2 yields the displayed affine function. Its zero occurs at \(v\approx2.52740422964\times10^{-5}\), so no positive \(\beta_1\) solution to \(R_0=1\) exists at \(v\approx0.023\).

For the Figure 1 parameter statement, the relevant \((E,A)\) block of the disease-free Jacobian is
\[
J_{EA}=
\begin{pmatrix}
-(\gamma+\mu)&\beta_1S_0+\beta_2V_{S,0}\\
\gamma(1-\omega)&-(\alpha_1+\alpha_2+\mu)
\end{pmatrix}.
\]
Its determinant is
\[
(\gamma+\mu)(\alpha_1+\alpha_2+\mu)(1-R_0).
\]
Thus \(R_0>1\) forces one positive and one negative eigenvalue. The printed Figure 1 values give \(R_0\approx3.66948154069\) and \(\lambda_+\approx0.180133902020\).

## Verification

The bundled `verify.py` recomputes \(q\), both endpoint reproduction numbers, the Table 2 value \(R_0(0.4)\), the exact affine \(R_0=1\) boundary in \((v,\beta_1)\), the nonnegative-boundary cutoff, and the Figure 1 disease-free eigenvalue. It also checks the interpolation identity against the original Eq. (3.1) at several vaccination rates.

All general conclusions are algebraic. No finite numerical experiment is used as evidence for an infinite-range statement.

## Relationship to prior work

Ihsanjaya and Susyanto (2023) print the model, the disease-free equilibrium, Eq. (3.1), Table 2, the Figure 1 parameter statement, and the later assertion that a critical vaccination rate near \(0.023\) separates outbreak from no-outbreak behavior. The weighted-endpoint identity above is not stated there, and direct substitution into their Eq. (3.1) conflicts with that numerical threshold and with their Figure 1 disease-free label.

Diagne, Rwezaura, Tchoumi, and Tchuenche (2021), which the 2023 paper cites as a model precursor, already emphasize that imperfect vaccination can fail to eradicate disease when efficacy is too low even at high coverage. That general principle is therefore not claimed as new. Their model uses a different vaccine-efficacy parameterization and does not imply the source-specific endpoint values, corrected threshold line, or Figure 1 instability found here.

Bamen, Ntaganda, Tellier, and Pamen (2023) derive vaccination-coverage conditions for a different imperfect-vaccine model with population turnover and vaccine trade-offs. Their analysis reinforces that eradication depends jointly on coverage and vaccine properties, but it does not contain the Ihsanjaya--Susyanto Eq. (3.1) or its numerical incompatibility.

## Limitations

The result diagnoses the printed equations and parameters only. An undocumented population rescaling, different breakthrough coefficient, or different simulation input could change the numerical conclusions, but such a change would be a different specification from the one publicly stated. The result does not classify endemic equilibria or establish global dynamics when \(R_0>1\).

## References

1. M. M. M. Ihsanjaya and N. Susyanto, “A mathematical model for policy of vaccinating recovered people in controlling the spread of COVID-19 outbreak,” AIMS Mathematics 8 (2023), 14508–14521. DOI: 10.3934/math.2023741.
2. M. L. Diagne, H. Rwezaura, S. Y. Tchoumi, and J. M. Tchuenche, “A Mathematical Model of COVID-19 with Vaccination and Treatment,” Computational and Mathematical Methods in Medicine (2021), 1250129. DOI: 10.1155/2021/1250129.
3. H. L. N. Bamen, J. M. Ntaganda, A. Tellier, and O. M. Pamen, “Impact of Imperfect Vaccine, Vaccine Trade-Off and Population Turnover on Infectious Disease Dynamics,” Mathematics 11 (2023), 1240. DOI: 10.3390/math11051240.
