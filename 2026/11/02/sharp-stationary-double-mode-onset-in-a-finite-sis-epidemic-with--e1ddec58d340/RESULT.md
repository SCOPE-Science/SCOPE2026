# Sharp stationary double-mode onset in a finite SIS epidemic with an external reservoir

## Finding

For a finite homogeneously mixing susceptible–infected–susceptible (SIS) population with persistent external infection, the stationary infection-count distribution can have *two distinct local modal components* even though the corresponding deterministic mean-field equation has only one feasible equilibrium. The exact onset in the within-population transmission intensity is a finite minimum, and its minimizing infected count has a square-root rather than population-scale order in the weak-importation regime.

Write \(n\ge2\) for population size; \(a=\alpha/\delta>0\) for external infection rate per susceptible relative to recovery; and \(b=\beta/\delta\ge0\) for infection rate per infected–susceptible pair relative to recovery. If \(a\ge1/n\), the infection-count stationary distribution is unimodal for all \(b\). If \(0<a<1/n\), define

\[
b_c(n,a)=\min_{1\le k\le n-1}\frac{k+1-a(n-k)}{k(n-k)}.
\]

For \(0\le b\le b_c(n,a)\) the distribution is nonincreasing, strictly so below the threshold; for \(b>b_c(n,a)\) it has exactly two separated local modal components, one at zero infections and the other at a positive count. Away from finitely many adjacent-mass tie values, both are strict single-state local maxima. This statement concerns the *locations of local modes*, not equality of their heights, not a discontinuity of stationary probabilities, and not an extinction transition.

The minimizing integer in the threshold formula is obtained by checking at most two integers adjacent to

\[
z_* = \frac{\sqrt{(1-na)(n+1)}-(1-na)}{1+a},
\]

with candidates clipped to \([1,n-1]\). In the weak-external-source scaling \(a_n=\lambda/n\), with fixed \(0<\lambda<1\), any minimizing integer \(k_n\) satisfies

\[
\frac{k_n}{\sqrt n}\longrightarrow\sqrt{1-\lambda},\qquad
b_c(n,\lambda/n)=\frac1n+\frac{2\sqrt{1-\lambda}}{n^{3/2}}+O(n^{-2}).
\]

Thus the local second mode first appears a distance of order \(n^{-3/2}\) above the traditional per-edge mean-field threshold \(1/(n-1)\), which has different interpretation.

## Assumptions and scope

The population contains exactly \(n\) individuals. Each susceptible becomes infected independently from an external reservoir at rate \(\alpha>0\), and independently across each ordered infectious–susceptible contact at rate \(\beta\ge0\); infected individuals recover at rate \(\delta>0\). With \(K\in\{0,\ldots,n\}\) the number infected, the continuous-time chain has birth and death rates

\[
\lambda_k=(n-k)(\alpha+\beta k),\qquad \mu_k=\delta k.
\]

The chain is irreducible for every \(\alpha>0\). A local modal component is a maximal contiguous constant-probability plateau whose value exceeds its outside neighboring probabilities, with absent boundary neighbors ignored. A single strict local maximum is a modal component containing exactly one state. All statements are for the unique stationary law and exact discrete counts, with no approximation of the distribution.

## Proof

**1. Stationary ratios and adjacent-mass signs.** Reversible detailed balance of the finite birth–death chain gives a positive stationary law \((\pi_k)_{k=0}^n\) determined by \(\pi_0\) and

\[
R_k=\frac{\pi_{k+1}}{\pi_k}=\frac{(n-k)(a+bk)}{k+1},\qquad 0\le k<n.
\]

Consequently the sign of \(\pi_{k+1}-\pi_k\) equals the sign of

\[
F(k)=(n-k)(a+bk)-(k+1)
=-bk^2+(nb-a-1)k+(na-1).
\]

For \(b>0\), this is a concave quadratic in \(k\) and \(F(n)=-(n+1)<0\). At \(b=0\), \(F(k)=a(n-k)-k-1\) is strictly decreasing. If \(na\ge1\), then \(F(0)\ge0\), and the positive-sign integers form an initial block, possibly with one boundary tie. Thus the stationary sequence first increases (possibly after an initial tie) and then decreases: one modal component.

If \(0<na<1\), then \(F(0)<0\). For \(k\ge1\), the condition \(F(k)>0\) is equivalent to

\[
b>h(k),\qquad h(k)=\frac{k+1-a(n-k)}{k(n-k)}.
\]

The minimum \(b_c\) is positive. When \(b\le b_c\), no adjacent ratio exceeds one and \(R_0=na<1\), so all masses are nonincreasing. When \(b>b_c\), at least one interior sign is positive; since \(F\) is concave, the positive-sign integers form one contiguous nonempty interval strictly after index zero. Its entry and exit produce exactly one positive modal component, in addition to the strict zero-count mode. Equality cases only widen the modal plateau; they do not introduce a third component. This proves the finite-state classification and its exact boundaries.

**2. Two-candidate threshold minimization.** Put \(c=1-na>0\). For real \(x\in(0,n)\), the continuous extension is

\[
h(x)=\frac{(1+a)x+c}{x(n-x)}.
\]

The sign of its derivative is the sign of \((1+a)x^2+2cx-nc\), which is strictly increasing from a negative number to a positive number on \((0,n)\). Hence \(h\) has a unique global continuous minimum, at the positive root \(z_*\) stated above. The minimum over integers \(1,\ldots,n-1\) is attained by one of the nearest feasible integers on either side of that root; no numerical minimization over the full range is needed.

**3. Weak-importation asymptotics.** Set \(a_n=\lambda/n\) and \(c=1-\lambda\in(0,1)\). The continuous minimizer satisfies \(z_* = \sqrt{cn}-c+O(n^{-1/2})\). At the critical point, the derivative equation \((1+a)z_*^2+2cz_*=nc\) implies the exact identity

\[
h(z_*)=\frac{c}{z_*^2}.
\]

Expansion yields \(h(z_*)=n^{-1}+2\sqrt c\,n^{-3/2}+O(n^{-2})\). Any minimizing integer differs from \(z_*\) by at most one, and the second derivative of \(h\) in that bounded neighborhood is \(O(n^{-5/2})\); Taylor's theorem bounds the integer-rounding correction by \(O(n^{-5/2})\). Therefore the stated threshold and \(k_n/\sqrt n\) asymptotics follow. The conventional deterministic threshold is \(1/(n-1)=1/n+O(n^{-2})\), which proves the claimed scale separation.

**4. Exact witness.** For \(n=16\) and \(a=1/32\), the continuous minimizer lies between \(2\) and \(3\) and direct rational comparison gives \(b_c=41/448\), attained at \(k=2\). At \(b=1/10>b_c\), \(R_0=1/2\), \(R_1=63/64<1\), \(R_2=259/240>1\), and \(R_5=187/192<1\). The concavity sign structure forces strict stationary maxima at \(k=0\) and \(k=5\), separated by a local minimum at \(k=2\). This is an exact discrete witness.

## Verification

Run \(\texttt{python3 checker.py}\) using the Python standard library. The checker reconstructs unnormalized stationary probabilities by exact rational detailed balance, verifies the local-modal-component classification for parameter grids of randomly selected rational values at population sizes \(2\) through \(36\), verifies the candidate-integer threshold calculation, and checks the witness with rational arithmetic. The included code executed with 46,765 passing exact-rational assertions. The general theorem and asymptotic formula are analytically proved above; the finite tests are not substituted for an infinite proof.

## Relationship to prior work

Stone, Wilkinson-Herbots and Isham (first publicly available in October 2007) used the SIS model with an external infection source and the stationary infected-count distribution for head-lice epidemiology. The underlying SIS model and equilibrium birth–death product are **not** claimed as new. Neal's 2014 work treats the homogeneously mixing stochastic SIS epidemic and quasi-stationary approximations for general infectious periods; its explicitly reported primary MSC classification is 92D30. Foxall's 2014 spontaneous-infection study establishes finite-chain convergence and monotonicity, rather than the claimed exact stationary mode boundary. Van Mieghem's 2020 paper describes a qualitatively different sharp change in **mean** prevalence for fixed population and very weak self-infection. Nieddu, Forgoston and Billings (2022) compute the stationary distribution and use its shape and a continuous-extension derivative at zero as an approximate outbreak-regime indicator; the exact two-mode onset, two-candidate minimizer, and weak-immigration square-root scale are not stated in its inspected sections. He, Luczak and Ross's 2024 preprint (2025 journal version) studies total-variation mixing-time cutoff with fixed per-person self-infection, a different population-scaling regime.

The contribution assessed here is the exact discrete local-mode classification together with its minimal positive-count threshold and asymptotic finite-size location; merely reproducing the known birth–death stationary law would not be original. Historical priority is not independently certified.

## Limitations

This is a mathematical property of a finite, completely mixed, homogeneous SIS chain. Its second local maximum need not have appreciable *total probability mass*, and no empirical or clinical prediction follows. The main sharp threshold is the onset of a **local** mode, not a sharp stationary transition or an asymptotic first-order phase transition. The weak-importation expansion assumes fixed \(0<\lambda<1\) and does not cover its boundary values. The model excludes heterogeneity, time dependence, incubation states and endogenous reservoir dynamics. One plausible primary model source could not be read in full through available lawful access; its complete supplementary and technical contents are a residual historical-priority risk.

## References

1. P. Stone, H. Wilkinson-Herbots and V. Isham, “A stochastic model for head lice infections,” *Journal of Mathematical Biology* 56 (2008), 743–763; first electronically available October 2007. https://doi.org/10.1007/s00285-007-0136-0
2. P. Neal, “Endemic behaviour of SIS epidemics with general infectious period distributions,” *Advances in Applied Probability* 46 (2014), 241–255. https://doi.org/10.1239/aap/1396360112
3. E. Foxall, “Convergence and monotonicity for a model of spontaneous infection and transmission,” *Advances in Applied Probability* 46 (2014), 560–584. https://doi.org/10.1239/aap/1401369707
4. P. Van Mieghem, “Explosive phase transition in susceptible-infected-susceptible epidemics with arbitrary small but nonzero self-infection rate,” *Physical Review E* 101 (2020), 032303. https://doi.org/10.1103/PhysRevE.101.032303
5. G. T. Nieddu, E. Forgoston and L. Billings, “Characterizing outbreak vulnerability in a stochastic SIS model with an external disease reservoir,” *Journal of the Royal Society Interface* 19 (2022), 20220253. https://doi.org/10.1098/rsif.2022.0253
6. R. He, M. Luczak and N. Ross, “Cutoff for the logistic SIS epidemic model with self-infection,” arXiv:2407.18446 (2024), *Advances in Applied Probability* 57 (2025), 1456–1483. https://arxiv.org/abs/2407.18446
