# An exact finite-amplitude prevalence penalty from oscillatory epidemic self-protection

## Finding

In a behavioral susceptible–infected–susceptible mean-field model, stationary oscillations have an exact, sign-definite relationship between variation in protective behavior and the excess mean epidemic prevalence. The result holds at arbitrary oscillation amplitude, not merely near a Hopf bifurcation.

Write \(R=2\alpha\lambda>0\) and \(K=1+c\), with \(c>1\), \(\zeta>0\), \(\mu>0\). Consider the differential equations

\[
\dot x=x(1-x)(2x+\zeta y-K),\qquad
\dot y=y\bigl(R(1-x)(1-y)-\mu\bigr).
\]

For **every** invariant Borel probability measure \(\nu\) whose support is a compact subset of \((0,1)^2\), define the mean protective uptake \(M=\int x\,d\nu\), the mean infection prevalence \(N=\int y\,d\nu\), the behavioral variance \(V=\int(x-M)^2\,d\nu\), and the covariance \(C=\int(x-M)(y-N)\,d\nu\). The following are exact:

\[
2M+\zeta N=K,\qquad C=-\frac{2V}{\zeta},\qquad
(1-M)(1-N)=\frac{\mu}{R}+\frac{2V}{\zeta}.
\]

Let \(\beta_-\le\beta_+\) be the real roots of

\[
F(s):=(1-s)\left(1-\frac{K-2s}{\zeta}\right)=\frac{\mu}{R}.
\]

They are real for every such measure, and

\[
\boxed{V=(M-\beta_-)(\beta_+-M).}
\]

A non-Dirac invariant measure has \(V>0\), hence strictly negative protection–prevalence covariance and \(\beta_-<M<\beta_+\).

Suppose additionally \(\zeta>K+2\) and the larger-root equilibrium is physical, namely \(0<\beta_+<1\) and \(0<y_*=(K-2\beta_+)/\zeta<1\). Then every non-Dirac invariant measure supported in the open square satisfies

\[
\boxed{M<\beta_+,\qquad N>y_*}.
\]

Set \(D=\beta_+-\beta_->0\). The excess mean prevalence over the interior equilibrium is exactly

\[
\boxed{
N-y_*=\frac{2(\beta_+-M)}{\zeta}
=\frac{D-\sqrt{D^2-4V}}{\zeta}>0.}
\]

In particular, the excess prevalence is determined **without reconstructing the oscillation waveform**, solely by the variability of protective uptake and equilibrium parameters. Since \(0<\beta_+-M<D/2\), it also obeys the strict amplitude-sensitive bounds

\[
\frac{2V}{\zeta D}<N-y_*<\frac{4V}{\zeta D}.
\]

The original oscillatory parameter regime of Frieswijk, Zino, Ye, Rizzo, and Cao (2022), Theorem 2, implies \(\zeta>K+2\) and admits an interior periodic solution. Consequently **every** nonconstant interior periodic solution in that regime incurs this strictly positive time-averaged prevalence penalty relative to its interior endemic equilibrium. The word "penalty" compares two mathematical long-run quantities at fixed parameters; it is not an intervention-effect or welfare assertion.

## Assumptions and scope

The state variables \(x,y\) represent mean probabilities or fractions of protection adoption and infection. The dynamic is deterministic and continuous-time with self-protection fully blocking acquisition of infection; no stochastic finite-population claim is made. Parameter restrictions for the general moment identities are \(R,\zeta,\mu>0\) and \(K>2\). The invariant measure is a probability distribution invariant under the full flow and has compact support strictly inside the open physical state square. In particular, uniform time average on a nonconstant interior periodic orbit qualifies. No ergodicity assumption is required; invariant mixtures qualify whenever their support remains interior.

For the prevalence-penalty corollary additionally assume \(\zeta>K+2\), with a physical larger-root equilibrium as specified. Existence of an invariant non-Dirac measure is conditional unless guaranteed by a separate existence theorem. The stated 2022 oscillatory theorem supplies existence in its parameter regime.

For any root \(s\) the corresponding interior stationary prevalence is \(y=(K-2s)/\zeta\), and the disease equation enforces \(F(s)=\mu/R\). A root not leading to \(0<s,y<1\) is algebraic, not an additional physical equilibrium.

## Proof

**1. Stationary logarithmic balance.** Let \(\mathcal L\) denote the flow generator. All logarithms below have bounded derivatives on the compact support, so invariance gives \(\int\mathcal Lg\,d\nu=0\) for every chosen \(g\). This follows either by differentiating the invariant integral at time zero or by bounded integration along the stationary flow.

For \(g_1(x,y)=\log(x/(1-x))\), direct substitution yields

\[
\mathcal Lg_1=2x+\zeta y-K.
\]

Integrating establishes \(2M+\zeta N=K\).

For the smooth function \(g_2(x,y)=-M\log x-(1-M)\log(1-x)\), where \(M\) is a fixed scalar once the measure is chosen,

\[
\mathcal Lg_2=(x-M)(2x+\zeta y-K).
\]

Integrating and expanding centered second moments, with \(\int(x-M)\,d\nu=0\), gives \(2V+\zeta C=0\). Notice that no local linearization or small-amplitude approximation occurs.

Finally \(g_3(x,y)=\log y\) gives

\[
\mathcal Lg_3=R(1-x)(1-y)-\mu.
\]

Consequently \((1-M)(1-N)+C=\mu/R\). Substitution of the covariance formula yields the third claimed identity.

**2. Exact quadratic moment shell.** Eliminate \(N\) using \(N=(K-2M)/\zeta\). The susceptible-contact identity becomes

\[
F(M)-\frac{\mu}{R}=\frac{2V}{\zeta},
\]

where the quadratic \(F\) has strictly negative leading coefficient \(-2/\zeta\). Because its value at \(M\) is at least \(\mu/R\), its level equation has real roots. Factoring it gives

\[
F(s)-\frac{\mu}{R}=-\frac2\zeta(s-\beta_-)(s-\beta_+).
\]

Evaluation at \(M\) proves \(V=(M-\beta_-)(\beta_+-M)\). The elementary sum-of-roots formula is

\[
\beta_-+\beta_+=\frac{K+2-\zeta}{2}.
\]

If \(V>0\), \(M\) lies strictly between the roots, so the roots are distinct. Conversely, \(V=0\) implies the invariant measure is supported on \(x=M\). Stationarity of that measure forces \(\dot x=0\) at almost every support point, hence \(y=(K-2M)/\zeta\) almost surely. Both coordinates are constant, so the measure is Dirac. This proves that every non-Dirac invariant measure has \(V>0\).

**3. Strict mean gap and its size.** Under \(\zeta>K+2\) the root sum is negative. Since \(\beta_+>0\) by the physical-equilibrium hypothesis, this implies \(\beta_-<-\beta_+<0\). By \(M\in(0,1)\) and the strict root interval, \(M<\beta_+\). The first stationary balance then gives

\[
N-y_* = \frac{2(\beta_+-M)}{\zeta}>0.
\]

Let \(d=\beta_+-M\) and \(D=\beta_+-\beta_-\). The shell is \(V=d(D-d)\). Also \(0<d<\beta_+<D/2\), where the last inequality uses \(\beta_-<-\beta_+\). Thus the **smaller root** of this equation determines \(d\), namely \(d=(D-\sqrt{D^2-4V})/2\). The displayed gap formula follows. Since \(D/2<D-d<D\), the shell implies \(V/D<d<2V/D\), giving the strict bounds.

**4. Presence in the established oscillatory regime.** In the source theorem write \(R=2\alpha\lambda>\mu\). Its restriction \(c\ge 2R/\mu-3\) gives \(K=c+1\ge 2(R-\mu)/\mu\). Its strict condition \(\zeta>RK/(R-\mu)\) therefore implies \(\zeta>K+2\), because

\[
\frac{RK}{R-\mu}-(K+2)=\frac{K\mu-2(R-\mu)}{R-\mu}\ge0.
\]

The source also establishes the relevant unique physical interior equilibrium and an interior nonconstant periodic orbit. Apply steps 1–3 to its normalized period measure. No claim of new cycle existence or attraction is required.

## Verification

A standalone `verify.py` reproduces two symbolic factorization identities with SymPy and a high-accuracy numerical periodic-orbit check for the source's Example 1 with \(c=3\), \(\alpha=3\), \(\lambda=1/2\), \(\mu=1\), and \(\zeta=19/2\). It detects the final two protection maxima along a converged numerical trajectory, integrates observables over that numerical period, and checks the three balance equations, the exact variance shell and the mean-prevalence gap. The program requires `numpy`, `scipy`, and `sympy` as listed in `requirements.txt`. Run from the extracted package directory with `python verify.py`.

In that check \(\beta_+=(-21+\sqrt{1113})/24\approx0.5150689431\) and \(y_*\approx0.3126170646\). The approximate periodic means are \(M\approx0.5046971249\) and \(N\approx0.3148006053\); \(V\approx0.0287275102\) and \(C\approx-0.0060478969\). The five independently evaluated residuals have magnitudes below \(6\times10^{-12}\). A numerical trajectory only corroborates, and does not prove, the invariant-measure theorem.

## Relationship to prior work

Frieswijk et al. (2022) introduce precisely the analyzed mean-field flow in their Proposition 1, Eq. (6). Their Lemma 2, Proposition 2 and Theorem 2 provide equilibrium branches, their local stability, and sufficient conditions for attraction toward sustained cycles. The new finding does **not** claim those statements: it establishes a finite-amplitude identity linking time-averaged prevalence to the variance of protection, a strictly negative covariance, and an explicit strict elevation of mean prevalence above the unique interior equilibrium in the oscillatory regime. Inspection of the source's dynamics, theorem statements and proofs did not identify these quantitative stationary-moment laws.

Ye et al. (2021) develop a related stochastic, network-based behavior–epidemic framework using distinct state dynamics; their cycle examples do not establish the precise invariant-moment identities of the current planar limiting flow. Khazaei, Paarporn, García, and Eksin's evolutionary social-distancing model instead couples a replicator equation with an SEIRS compartment system and does not supply these exact two-dimensional SIS stationary moments. Paarporn and Eksin (2023) study a related SIS model with evolutionary social distancing; its accessible abstract identifies a similar topic, but the primary full text could not be inspected, so its possible equivalent claims remain an explicit bibliographic uncertainty, not a source classified as non-covering. Previously indexed recurrence and mean–variance identities for nonlinear-incidence SI or delayed predator–prey equations have a comparable *method*, but involve different vector fields and equilibrium polynomials and thus do not imply the displayed law.

The comparison is at the level of statements and implications, not the shared words "epidemic" or "limit cycle." Standard invariant-measure integration is used in the proof; originality is restricted to the **model-specific quantitative identity and strict epidemiological implication**, not to the general integration technique.

## Limitations

The conclusion is about the deterministic macroscopic mean-field equations, not the exact finite stochastic network. Compact interior support is essential for the logarithmic test functions and excludes boundary-supported measures. The strict prevalence comparison requires \(\zeta>K+2\) and a physical larger-root equilibrium; without these, the universal moment identities still hold but the sign of the comparison with a particular physical equilibrium is not asserted. This result does not establish existence or uniqueness of periodic orbits outside previously proved regions, global attraction, or welfare benefits of any intervention. Inaccessible or unindexed studies could contain an equivalent stationary-moment calculation; independent expert validation has not been performed.

## References

1. K. Frieswijk, L. Zino, M. Ye, A. Rizzo, and M. Cao, *A mean-field analysis of a network behavioural–epidemic model*, arXiv:2203.04016 (first posted 8 March 2022), later IEEE Control Systems Letters **6** (2022), 2533–2538, DOI: 10.1109/LCSYS.2022.3168260. Proposition 1, Lemma 2, Proposition 2, Theorem 2 and Appendix.
2. M. Ye, L. Zino, A. Rizzo, and M. Cao, *Game-theoretic modeling of collective decision-making during epidemics*, arXiv:2008.01971 (2020), Physical Review E **104** (2021), 024314, DOI: 10.1103/PhysRevE.104.024314.
3. H. Khazaei, K. Paarporn, A. García, and C. Eksin, *Disease spread coupled with evolutionary social distancing dynamics can lead to growing oscillations*, 2021 IEEE Conference on Decision and Control, 4280–4286, DOI: 10.1109/CDC45484.2021.9683594; author-hosted accessible manuscript.
4. K. Paarporn and C. Eksin, *SIS epidemics coupled with evolutionary social distancing dynamics*, American Control Conference (2023), 4308–4313, DOI: 10.23919/ACC55779.2023.10156026; primary full text not accessed during this comparison.
