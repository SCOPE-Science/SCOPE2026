# Exact duration-dependent ranking reversal in a depleted-prey Holling-II assay

## Finding
Consider two **separate**, otherwise identical, closed feeding assays starting at the same prey abundance \(N_0>0\), with one predator per assay, no replacement or reproduction of prey, and fixed Holling-II parameters. Suppose predator 1 has slower dilute-prey searching but shorter handling time: \(0<a_1<a_2\) and \(0<h_1<h_2\). Let \(c_i=1/a_i\), \(N_c=(c_1-c_2)/(h_2-h_1)>0\), and \(q=c_1+h_1N_c=c_2+h_2N_c>0\).

For **every** assay duration \(T>0\), define the sharp initial-prey threshold
\[
N_{0,\mathrm{crit}}(T)=N_c\frac{T/q}{1-e^{-T/q}}.
\]
If \(C_i(T)=N_0-N_i(T)\) is prey consumed by predator \(i\), then
\[
C_1(T)>C_2(T)\iff N_0>N_{0,\mathrm{crit}}(T),\qquad
C_1(T)=C_2(T)\iff N_0=N_{0,\mathrm{crit}}(T).
\]
The reverse strict inequality holds for initial abundance below the threshold. This threshold rises strictly from \(N_c\) to infinity as duration increases. Thus for \(N_0\le N_c\) predator 2 consumes strictly more at every positive time; for \(N_0>N_c\), predator 1 initially consumes more, and the cumulative consumption rankings switch **exactly once**, after which predator 2 consumes more. The unique switch duration is
\[
T_*=q\left[r+W_0(-re^{-r})\right],\qquad r=N_0/N_c>1,
\]
with \(W_0\) the principal real branch of the Lambert \(W\) function. For \(N_0/N_c\downarrow1\), \(T_*/q\sim2(N_0/N_c-1)\); for \(N_0/N_c\to\infty\), \(T_*/q\sim N_0/N_c\).

## Assumptions and scope
Prey amount may be continuous (density or abundance) and is positive at every finite time. The two predator cohorts are **not interacting** and are each tested in a separate well-mixed enclosure. Each assay starts from the same \(N_0>0\) and follows
\[
\frac{dN_i}{dt}=-\frac{a_iN_i}{1+a_i h_iN_i}=-\frac{N_i}{c_i+h_iN_i},\qquad N_i(0)=N_0,\quad i\in\{1,2\},
\]
with \(a_i,h_i>0\) constant and no background prey loss, prey reproduction, prey refuge, predator satiation changes, or stochastic counting. The theorem assumes \(a_1<a_2\) and \(h_1<h_2\). Reversing predator labels yields the opposite tradeoff. If \(a_1\ge a_2\) and \(h_1\le h_2\), with at least one strict, predator 1 consumes more at every positive time; the reversed coordinatewise order similarly gives predator 2 dominance. Identical parameters give ties at every time. Other outcomes are outside the claimed theorem rather than silently incorporated.

## Proof
For each \(i\), separation of variables gives the exact and strictly invertible survivor relation
\[
T=c_i\log(N_0/N_i(T))+h_i\bigl(N_0-N_i(T)\bigr). \tag{1}
\]
Its right-hand side is continuous, strictly decreasing as a function of the unknown survivor \(N_i\in(0,N_0]\), ranges from zero to infinity, and thus determines a unique positive survivor at every finite \(T\). The predators' instantaneous intake rates at a *common* prey density \(N\) are \(N/(c_i+h_iN)\); the strict rate ordering changes at \(N_c\), because \(c_1-c_2=(h_2-h_1)N_c\). This instantaneous crossing alone does **not** establish the cumulative theorem.

Suppose the two cumulative catches agree at a positive time \(T\). Then \(N_1(T)=N_2(T)=n\in(0,N_0)\). Subtracting equation (1) for the two predators yields
\[
N_c\log(N_0/n)=N_0-n. \tag{2}
\]
Substitution into either copy of equation (1) yields
\[
T=q\log(N_0/n),\qquad n=N_0e^{-T/q}. \tag{3}
\]
Combining (2) and (3) proves that equality is **possible only if**
\[
N_0(1-e^{-T/q})=N_cT/q. \tag{4}
\]
Conversely, if (4) holds, take \(n=N_0e^{-T/q}\); equations (2) and (3) hold, so equation (1) holds for both predators. Its uniqueness makes the catches equal. Therefore (4) is necessary and sufficient, and rearrangement gives the claimed unique threshold in \(N_0\).

Fix any \(T>0\). The difference \(C_1(T)-C_2(T)\) varies continuously with \(N_0>0\) and, by (4), has **exactly one** zero. If \(0<N_0\le N_c\), then \(c_1+h_1N\ge c_2+h_2N\) for all \(0<N\le N_0\). Strict scalar-flow comparison therefore gives \(C_1(T)<C_2(T)\). To determine the sign *above* the only zero independently, choose any \(N_0>N_c\exp(T/\min\{c_1,c_2\})\). The differential equations give \(dN_i/dt\ge -N_i/c_i\), hence \(N_i(t)\ge N_0e^{-t/c_i}>N_c\) throughout \([0,T]\). On this whole domain predator 1 has strictly greater instantaneous intake at each common density, so scalar comparison yields \(N_1(T)<N_2(T)\), or \(C_1(T)>C_2(T)\). The difference is therefore negative for small \(N_0\), positive for sufficiently large \(N_0\), continuous, and has just one zero. Its sign on each side follows without relying on a graph or an unverified derivative claim.

Write \(s=T/q\). Elementary differentiation shows that \(B(s)=s/(1-e^{-s})\) is strictly increasing for \(s>0\), because \(B'(s)=[1-(1+s)e^{-s}]/(1-e^{-s})^2>0\) by \(e^s>1+s\). Moreover \(B(0+)=1\), \(B(\infty)=\infty\). If \(N_0\le N_c\), no positive time can solve \(N_0=N_cB(T/q)\); if \(N_0>N_c\), exactly one time does, and strict ranking changes as asserted.

For \(r=N_0/N_c>1\) and \(s=T_*/q>0\), the equality \(r=B(s)\) becomes \((r-s)e^{s}=r\). Set \(u=r-s\): then \((-u)e^{-u}=-re^{-r}\). Since the positive-time root has \(0<u<1\), it is \(u=-W_0(-re^{-r})\), yielding the stated \(T_*\). The other real Lambert branch corresponds to the trivial time-zero root and must not be counted as a positive reversal. Taylor expansion \(B(s)=1+s/2+s^2/12+O(s^4)\) as \(s\downarrow0\), and \(B(s)\sim s\) as \(s\to\infty\), give the claimed limits. The derivative and endpoint statements require only \(a_i,h_i,N_0,T>0\) with the stated strict tradeoff.

## Verification
A standalone standard-library implementation in `verify.py` solves each exact survivor equation by bisection and checks the threshold against independent numerical survivors. It also tests exact crossover equality, the example below and the asymptotic branches; it is not used to prove the continuum result. For \(a_1=1\), \(a_2=2\), \(h_1=1/5\), \(h_2=3/5\), one has \(N_c=q=5/4\). At \(T=2\),
\[
N_{0,\mathrm{crit}}(2)=\frac{2}{1-e^{-8/5}}\approx2.505940702043707.
\]
At \(N_0=3\), predator 1 consumes more at \(T=2\), but the unique switch occurs later at \(T_*\approx2.635787459322323\). At \(N_0=2\), predator 2 already consumes more at \(T=2\).

## Relationship to prior work
The one-predator Holling type-II intake law is classical. Rogers (1972) and Royama (1971) developed the depleted-prey assay equation, while Real (1977) generalized the functional-response perspective. Rosenbaum and Rall (2018, Sections 1.1–1.3 and Discussion) describe the exact Rogers survivor relationship and its Lambert-\(W\) inversion; those facts are **prior art**, not the claim here. Oaten and Murdoch (1975) analyze functional response and switching among *prey types* in one predator's diet, not comparing two independently assayed fixed-parameter predators. The present claim is the necessary-and-sufficient **finite-duration versus initial-stock ranking threshold**, and its once-only duration reversal, for two separate predator assays with a crossing attack/handling tradeoff. It is stronger than merely noticing an instantaneous feeding-rate intersection, and neither follows solely from the title or terminology of a prior paper.

## Limitations
This is a conditional deterministic comparison, not a field-validated prediction or a result for predators competing simultaneously over one prey stock. No prey immigration, growth, behavioral adaptation, or estimation uncertainty is included. Full text of the Rogers (1972) source and the Oaten–Murdoch (1975) paper was not accessible during the literature comparison; an equivalent buried comparison in those works or general scalar-flow theory is possible. Only the Rosenbaum–Rall (2018) accessible article was read at relevant full-text level among the most directly applicable comparison sources. An independent mathematical audit remains unperformed; the reported self-review is not independent certification.

## References
1. Oaten, A. and Murdoch, W. W. (1975), *Switching, Functional Response, and Stability in Predator-Prey Systems*, The American Naturalist 109, 299–318. doi:10.1086/282999. Publisher dates it 1975-05-01.
2. Real, L. A. (1977), *The Kinetics of Functional Response*, The American Naturalist 111, 289–300. doi:10.1086/283161.
3. Rogers, D. (1972), *Random Search and Insect Population Models*, Journal of Animal Ecology 41, 369–383. doi:10.2307/3474; issue evidence June 1972, exact public day unverified.
4. Rosenbaum, B. and Rall, B. C. (2018), *Fitting functional responses: Direct parameter estimation by simulating differential equations*, Methods in Ecology and Evolution 9, 2076–2090. doi:10.1111/2041-210X.13039. Full text: https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13039.
5. Kisdi, É. and Liu, S. (2006), *Evolution of handling time can destroy the coexistence of cycling predators*, Journal of Evolutionary Biology 19, 49–58. doi:10.1111/j.1420-9101.2005.00993.x. Related but distinct coupled-predator study.
