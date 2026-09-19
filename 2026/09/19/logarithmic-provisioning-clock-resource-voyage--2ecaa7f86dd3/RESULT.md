# Logarithmic provisioning clocks and finite consumption capacity in a resource-coupled mortality model

## Source model

Crokidakis (2026), arXiv:2609.20430v1, studies
\[
\begin{aligned}
 h'&=-\lambda(p)h-\mu h+\gamma i,\\
 i'&=\lambda(p)h-(\gamma+\delta)i,\\
 d'&=\mu h+\delta i,\\
 p'&=-c_1h-c_2i-\rho p,
\end{aligned}
\qquad
\lambda(p)=\alpha+\frac{\beta}{1+p},
\]
with \(h+i+d=1\), \(h(0)=1\), \(i(0)=d(0)=0\), and \(p(0)=p_0\). For a fixed stress threshold \(p_c>0\), the critical provisioning time \(t_c\) is the first time at which \(p(t_c)=p_c\). The source paper reports an approximately linear relation between \(t_c\) and \(p_0-p_c\) over its finite observation window and motivates it by setting \(\rho=0\) and freezing the healthy/ill fractions.

The full model has a different large-buffer structure.

## Theorem 1: positive deterioration gives a logarithmic clock

Assume \(\mu>0\), \(\delta>0\), \(c_1,c_2>0\), \(\rho>0\), and \(p_0>p_c>0\). Then the threshold is crossed exactly once and
\[
\boxed{
 t_c=\frac1\rho\log\frac{p_0}{p_c}+o(1)
 \qquad (p_0\to\infty).
}
\]
More precisely, with
\[
q(t)=c_1h(t)+c_2i(t),\qquad
m=\min\{\mu,\delta\},\qquad
c_+=\max\{c_1,c_2\},
\]
and
\[
R(t)=\int_0^t e^{-\rho(t-s)}q(s)\,ds,
\]
one has the exact identity
\[
\boxed{
\frac1\rho\log\frac{p_0}{p_c}-t_c
=\frac1\rho\log\left(1+\frac{R(t_c)}{p_c}\right)\ge0.
}
\]
Furthermore
\[
0\le R(t)\le c_+\Psi_{\rho,m}(t),
\]
where
\[
\Psi_{\rho,m}(t)=
\begin{cases}
\dfrac{e^{-mt}-e^{-\rho t}}{\rho-m},&\rho\ne m,\\[1ex]
t e^{-\rho t},&\rho=m.
\end{cases}
\]
Hence \(R(t_c)\to0\), so the logarithmic formula has the sharp additive constant shown above rather than merely the correct order.

### Proof

Let \(S=h+i\). Since
\[
S'=-\mu h-\delta i\le-mS,
\]
we have \(S(t)\le e^{-mt}\), and therefore
\[
0\le q(t)\le c_+e^{-mt}.
\]
Before the positive threshold is reached, the provisioning equation can be integrated exactly:
\[
p(t)=p_0e^{-\rho t}-R(t).
\]
Because \(p'(t)<0\) whenever \(p>0\), any crossing is unique. Since \(p(t)\le p_0e^{-\rho t}\), a crossing occurs no later than \(\rho^{-1}\log(p_0/p_c)\).

At the crossing,
\[
p_0e^{-\rho t_c}=p_c+R(t_c),
\]
which gives the displayed exact clock identity. The exponential survival bound gives the stated estimate on \(R\). For every fixed \(T\),
\[
p(T)\ge p_0e^{-\rho T}-c_+\Psi_{\rho,m}(T),
\]
so \(t_c\to\infty\) as \(p_0\to\infty\). Consequently \(R(t_c)\to0\), completing the proof.

## Theorem 2: zero deterioration has finite lifetime consumption capacity

Now set \(\rho=0\). Then
\[
p(t)=p_0-\int_0^t q(s)\,ds
\]
and
\[
\boxed{
\int_0^\infty q(s)\,ds\le\frac{c_+}{m}.
}
\]
Therefore, if
\[
\boxed{
 p_0>p_c+\frac{c_+}{m},
}
\]
the threshold \(p_c\) is never reached. In particular, the full \(\rho=0\) system cannot possess an asymptotically linear law \(t_c\sim C(p_0-p_c)\) extending to arbitrarily large \(p_0\): sufficiently large buffers are never exhausted to the prescribed threshold before the surviving population disappears.

There is also a sharp large-\(p_0\) consumption limit. Define
\[
D=\alpha\delta+\mu\gamma+\mu\delta.
\]
Then
\[
\boxed{
 p(\infty)
 =p_0-J_\alpha+o(1),
\qquad
J_\alpha=
\frac{c_1(\gamma+\delta)+c_2\alpha}{D},
\qquad p_0\to\infty.
}
\]
Thus the total amount consumed converges to a finite constant determined by the baseline-health dynamics.

### Proof of the large-buffer limit

For \(\rho=0\), the survival estimate gives
\[
p(t)\ge p_0-\frac{c_+}{m}.
\]
Hence, uniformly in time,
\[
\lambda(p(t))=\alpha+O(p_0^{-1})
\qquad (p_0\to\infty).
\]
The \((h,i)\) system therefore converges on every finite interval to the constant-coefficient baseline system
\[
\binom{h}{i}'=
\begin{pmatrix}
-(\alpha+\mu)&\gamma\\
\alpha&-(\gamma+\delta)
\end{pmatrix}
\binom{h}{i},
\qquad (h,i)(0)=(1,0).
\]
The uniform bound \(q(t)\le c_+e^{-mt}\) permits dominated convergence over \([0,\infty)\). Integrating the baseline linear system gives
\[
\int_0^\infty\binom{h}{i}\,dt
=
\frac1D
\binom{\gamma+\delta}{\alpha},
\]
which yields \(J_\alpha\).

## Consequence for the source-paper scaling claim

For the full model with the source-paper choice \(\rho=0.001\), the large-buffer critical time is logarithmic, not linear:
\[
 t_c\sim 1000\log(p_0/p_c)\ \text{days}.
\]
The approximately linear trend reported in the paper is therefore a finite-window regime rather than the asymptotic law of the stated equations. Conversely, in the auxiliary \(\rho=0\) model used to motivate linearity, positive mortality eventually shuts off consumption, so sufficiently large initial buffers never reach a fixed positive stress threshold at all.

For the paper's remaining parameter values and \(p_c=1\), direct numerical integration gives
\[
\begin{array}{c|c|c|c}
p_0&t_c&1000\log p_0&t_c/(1000\log p_0)\\\hline
100&4484.9990&4605.1702&0.973905\\
1000&6876.1071&6907.7553&0.995418\\
10^4&9204.5517&9210.3404&0.999372\\
10^6&13815.3976&13815.5106&0.999992
\end{array}
\]
which matches the theorem. For \(\rho=0\), the baseline limiting consumption is
\[
J_\alpha=12.631578947\ldots,
\]
and direct integrations at \(p_0=1000\) and \(10^4\) consume approximately \(11.8721\) and \(12.5510\), respectively.

## Scientific interpretation

The resource equation contains two qualitatively different depletion mechanisms. Consumption is tied to a living population and therefore has finite lifetime mass when both healthy and ill individuals have positive mortality rates. Spontaneous deterioration \(-\rho p\), by contrast, acts directly on the resource stock for as long as any stock remains. This produces a sharp structural dichotomy:

- \(\rho>0\): every positive threshold is eventually crossed and the large-buffer clock is logarithmic;
- \(\rho=0\): total possible consumption is finite, so sufficiently large buffers never reach a fixed positive threshold.

The finite-window linear behavior can still be a useful empirical approximation, but it is not the global scaling law of the model.

## Originality boundary

The integrating-factor identity, exponential survival comparison, and constant-coefficient compartmental calculation are standard ODE tools and are not claimed as new in isolation. The source-specific contribution is their combination for arXiv:2609.20430v1, yielding the exact large-buffer logarithmic law for the paper's critical provisioning time, the finite-consumption obstruction at \(\rho=0\), and the explicit limiting consumption constant \(J_\alpha\). Searches by the source identifier, exact title, critical-provisioning terminology, resource-coupled terminology, and equivalent logarithmic-threshold wording found no prior statement of these conclusions for this model.

## Limitations

The analysis concerns the deterministic ODE model of arXiv:2609.20430v1 and a fixed positive threshold \(p_c\). It does not validate the historical realism or calibration of the model, does not address stochastic resupply or heterogeneous crews, and does not give a closed-form formula for the intermediate-buffer crossover regime. The \(\rho=0\) limiting-consumption formula uses positive mortality \(\mu,\delta>0\), as in the source parameters.

## Reproducibility

`artifacts/verify_provisioning_clock.py` integrates the stated ODEs for the source parameters and prints the numerical convergence tests quoted above. `artifacts/verification_output.txt` records the resulting values. The numerical checks support the analytic statements but are not a substitute for the proofs.

## References

1. N. Crokidakis, *The dynamics of early transoceanic voyages: A resource-coupled model of crew health and survival*, arXiv:2609.20430v1 (2026), https://arxiv.org/abs/2609.20430.
2. N. Crokidakis, *Modeling the Siege of Syracuse: Resources, strategy, and collapse*, arXiv:2504.01649 (2025), https://arxiv.org/abs/2504.01649. This related historical-dynamics paper was checked for context; it does not contain the source-specific provisioning-time result above.
