# Extinction has a nondegenerate susceptible boundary law, not point convergence
## Finding
For the stochastic SIRS system (1.3) in Huang, Du, and Liang, define \(a=\varepsilon\sigma_1\). When \(a>0\), extinction of infection cannot mean almost-sure convergence of the full stochastic state to the deterministic disease-free point \(E_0=(\Lambda/\mu,0,0)\). The paper's Theorem 3.2 proves exponential extinction of \(I\) together with the time-average limits \(\langle S\rangle\to\Lambda/\mu\) and \(\langle R\rangle\to0\), but its numerical discussion later upgrades this to pointwise convergence. That upgrade is incompatible with the printed SDE.

There is also an exact replacement for the susceptible part of the disease-free stochastic state. On the invariant face \(I=R=0\),
\[
dS=(\Lambda-\mu S)\,dt-aS\,dB_1.
\]
Its stationary law is inverse-gamma with shape \(k=1+2\mu/a^2\) and scale \(q=2\Lambda/a^2\):
\[
p(s)=\frac{q^k}{\Gamma(k)}s^{-k-1}\exp(-q/s),\qquad s>0.
\]
Under the hypothesis \(\mu>a^2/2\) used in Theorem 3.2, this law has
\[
\mathbb E[S]=\frac{\Lambda}{\mu},\qquad
\operatorname{{Var}}(S)=\frac{\Lambda^2a^2}{\mu^2(2\mu-a^2)}.
\]
For the paper's extinction simulation parameters \(\varepsilon=0.75\), \(\sigma_1=0.6\), \(\Lambda=1\), and \(\mu=0.2\), one has \(a=9/20\), so the boundary law is \(\operatorname{{InvGamma}}(241/81,800/81)\), with mean \(5\) and variance \(2025/79\).

## Assumptions and scope
The claim concerns the Itô SIRS model printed as equation (1.3), with positive \(\Lambda\) and \(\mu\), and nonzero susceptible mortality-noise amplitude \(a=\varepsilon\sigma_1\). The impossibility of convergence to \(E_0\) uses only positivity of \(S\), continuity of the incidence function at extinction, and \(a>0\). The inverse-gamma formula concerns the invariant face \(I=R=0\); it is not a claim that every interior trajectory has already been proved here to converge in distribution to that boundary law.

The numerical moment calculation additionally uses the exact decimals reported in the paper. The theorem's condition \(\mu>\varepsilon^2(\sigma_1^2\vee\sigma_2^2\vee\sigma_3^2)/2\) implies \(\mu>a^2/2\), so the boundary law has finite variance in the theorem's stated parameter regime.

## Proof
Assume for contradiction that a sample path satisfies \(S(t)\to\Lambda/\mu\), \(I(t)\to0\), and \(R(t)\to0\). The susceptible equation is
\[
dS=\left(\Lambda-\mu S-\frac{\beta I}{f(I)}S+\delta R\right)dt-aS\,dB_1.
\]
Since \(S(t)>0\), Itô's formula gives
\[
d\log S=\left(\frac{\Lambda}{S}-\mu-\frac{\beta I}{f(I)}+\frac{\delta R}{S}-\frac{a^2}{2}\right)dt-a\,dB_1.
\]
Under the assumed convergence, the drift integrand tends to \(-a^2/2\). Dividing the integrated identity by \(t\) and using \(B_1(t)/t\to0\) almost surely therefore gives
\[
\frac{\log S(t)}{t}\longrightarrow-\frac{a^2}{2}.
\]
But convergence of \(S(t)\) to the positive constant \(\Lambda/\mu\) requires \(\log S(t)/t\to0\), a contradiction. Hence the deterministic disease-free point cannot be an almost-sure point limit when \(a>0\).

For the boundary law, set \(I=R=0\). The zero-current stationary Fokker--Planck equation for \(p\) is
\[
\frac{d}{ds}\left(a^2s^2p(s)\right)=2(\Lambda-\mu s)p(s).
\]
Writing \(k=1+2\mu/a^2\) and \(q=2\Lambda/a^2\), direct integration yields \(p(s)\propto s^{-k-1}e^{-q/s}\). The exponential cutoff makes the density integrable at zero, and \(k>1\) makes it integrable at infinity. Normalization gives the inverse-gamma density displayed above. Standard inverse-gamma moments yield the stated mean and, when \(k>2\), the stated variance. Since \(k>2\) is equivalent to \(\mu>a^2/2\), Theorem 3.2's noise bound is sufficient for finite variance.

For the reported simulation, \(a=(3/4)(3/5)=9/20\), hence \(a^2=81/400\). Therefore
\[
k=1+\frac{2/5}{81/400}=\frac{241}{81},\qquad q=\frac{2}{81/400}=\frac{800}{81},
\]
and
\[
\operatorname{{Var}}(S)=\frac{2025}{79}.
\]

## Verification
The accompanying `verify.py` checks the zero-current coefficient identity symbolically at the coefficient level and recomputes the exact rational shape, scale, mean, variance, and theorem noise inequality for the paper's extinction parameters. Its expected terminal output is `VERIFY_OK`.

The source's Theorem 3.2 states time-average convergence for \(S\) and \(R\), not pointwise convergence. The paper's numerical discussion later says that the path almost surely tends to \(E_0=(5,0,0)\). The contradiction above uses the printed susceptible noise term itself, so it does not depend on a numerical discretization.

## Relationship to prior work
Huang, Du, and Liang explicitly contrast their natural-death perturbation with the earlier transmission-noise SIRS model of Cai, Kang, and Wang. In the latter structure the stochastic transfer term is proportional to infection, so it disappears on the disease-free face; that predecessor can support a disease-free stationary distribution concentrated differently and does not imply the inverse-gamma boundary law produced by susceptible multiplicative mortality noise.

More broadly, stochastic epidemic literature routinely distinguishes deterministic equilibria from stationary distributions. Cai, Kang, and Wang report a unique disease-free stationary distribution in their stochastic SIRS model, while Cao et al. analyze stationary distributions and extinction in a stochastic SIR model. Those results motivate checking the boundary law here, but neither covers the source-specific \(dS=(\Lambda-\mu S)dt-aS\,dB_1\) reduction, the exact moments above, or the contradiction with the 2026 paper's point-convergence statement.

## Limitations
This result does not alter the paper's proved exponential extinction statement for \(I\), nor does it disprove the time-average limit \(\langle S\rangle\to\Lambda/\mu\). It does not prove the full interior process converges in distribution to the boundary inverse-gamma law after infection extinction; establishing that stronger asymptotic distributional statement would require an additional argument. The originality claim is source-specific: the inverse-gamma stationary family for affine multiplicative diffusions is classical, while the new content here is its exact application to this printed SIRS boundary dynamics and the resulting correction of the paper's deterministic point-convergence interpretation.

## References
1. J. Huang, J. Du, H. Liang, “Dynamics and stochastic sensitivity technique of a stochastic SIRS epidemic model,” *AIMS Mathematics* 11(3), 6720–6743 (2026), DOI: 10.3934/math.2026278.
2. Y. Cai, Y. Kang, W. Wang, “A stochastic SIRS epidemic model with nonlinear incidence rate,” *Applied Mathematics and Computation* 305, 221–240 (2017), DOI: 10.1016/j.amc.2017.02.003.
3. Z. Cao et al., “A regime-switching SIR epidemic model with a ratio-dependent incidence rate and degenerate diffusion,” *Scientific Reports* 9, 10696 (2019), DOI: 10.1038/s41598-019-47131-6.
