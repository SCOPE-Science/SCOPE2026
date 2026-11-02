# Two dispersion reversals in critical clumsy-coupon coverage cycles

## Finding

In an \(m\)-coupon random-refresh collector, fix an integer \(m\ge1\) and \(p\in(0,1)\), put \(q=1-p\), and refresh one uniformly selected coupon type each round, making it present with probability \(q\) and absent with probability \(p\). Let \(C_{m,p}\) be the positive number of rounds between successive **entrances** into the all-present state, with an entrance meaning a transition from a non-full state to the full state. Then the entrance cycles are independent and identically distributed and

\[
\mathbb E C_{m,p}=\frac{1}{p q^m},\qquad
\frac{\operatorname{Var}(C_{m,p})}{(\mathbb E C_{m,p})^2}
=(2-p)q^m+2mp\sum_{j=1}^m\frac{1}{j}\binom mj q^{m-j}p^j-1.
\]

For any fixed \(c>0\), set \(p_m=c/m\) for integers \(m>c\), and write \(\mathcal V_m(c)\) for the squared coefficient of variation above. Then

\[
\mathcal V_m(c)\longrightarrow V(c):=2e^{-c}\bigl(1+cA(c)\bigr)-1,
\qquad A(c):=\sum_{j=1}^{\infty}\frac{c^j}{j\,j!}.
\]

The profile \(V\) has **exactly two positive stationary points**: one strict global minimum \(c_-\) and one strict global maximum \(c_+\), with

\[
\begin{aligned}
c_-&=0.538585232669\ldots,&V(c_-)&=0.557349428200\ldots,\\
c_+&=3.868375184635\ldots,&V(c_+)&=1.626339614493\ldots.
\end{aligned}
\]

It decreases on \((0,c_-)\), increases on \((c_-,c_+)\), and decreases on \((c_+,\infty)\). There is exactly **one** \(c_0>0\) for which \(V(c_0)=1\), namely

\[
c_0=1.502861017335\ldots;
\qquad V(c)<1\ \text{for }0<c<c_0,\quad
V(c)>1\ \text{for }c>c_0.
\]

Both endpoint limits of \(V\) are one. The shape also describes the sequential long-time/large-system Fano factor of the entrance counting process: for each finite \(m\), renewal theory gives asymptotic count variance divided by asymptotic count mean equal to \(\mathcal V_m(c)\). In the critical large-\(m\) regime that factor tends to \(V(c)\). Thus the unique crossing distinguishes sub-Poisson and super-Poisson entrance counts, while the minimum and maximum identify the strongest deviations.

## Assumptions and scope

Each refresh choice and Bernoulli outcome is independent of all earlier choices. All observations are after the refresh. An entrance requires a preceding non-full state; consecutive holding rounds in the full state do not count as new entrances. Because \(p,q>0\), the finite state chain is irreducible, every entrance cycle is almost surely finite, and all its moments exist. The limit holds for every **fixed** \(c>0\) and \(m\to\infty\), not uniformly over unspecified varying \(c\). The cycle variable is not the first collection time from an empty initial collection.

## Proof

**Step 1: Exact full-state return Green function.** Let \(Y_t\) be the number of absent types, started from \(Y_0=0\), and set \(u_t=\Pr(Y_t=0\mid Y_0=0)\). A type never selected during the first \(t\) rounds remains present. Every type selected at least once has its final refresh bit independently present with probability \(q\). For a selected-type set of cardinality \(D_t\), the conditional probability of full occupancy is \(q^{D_t}\). Expanding the product \(\prod_{i=1}^{m}(q+p\mathbf1_{\{i\text{ unselected}\}})\) and observing that a fixed set of \(j\) types remains unselected with probability \((1-j/m)^t\) yields

\[
u_t=\sum_{j=0}^{m}w_j(1-j/m)^t,
\quad w_j=\binom mj q^{m-j}p^j.
\]

Consequently, for \(0\le z<1\),

\[
R_m(z)=\sum_{t\ge0}u_tz^t
=\sum_{j=0}^{m}\frac{w_j}{1-z(1-j/m)}.
\]

**Step 2: Renewal identity and moments.** Upon an entrance into full occupancy, the number \(U\) of rounds spent there **including the departure round** has geometric law \(\Pr(U=k)=q^{k-1}p\). After that departure, the next return to full occupancy completes the entrance cycle \(C_{m,p}\). By the strong Markov property, these are independent and identically distributed over successive entrances. Write \(F_m(z)=\mathbb E[z^{C_{m,p}}]\). The full-state occupation process consists of a geometric holding block followed by a complete entrance cycle, hence its renewal Green function is

\[
R_m(z)=\frac{1}{(1-qz)(1-F_m(z))}.
\]

Put \(\pi=q^m\), and \(r=m\sum_{j=1}^{m}w_j/j\). The finite partial fraction expansion gives, as \(z\uparrow1\),

\[
R_m(z)=\frac{\pi}{1-z}+r+O(1-z).
\]

Writing \(\delta=1-z\), inverting the renewal identity gives

\[
1-F_m(z)=\frac{\delta}{p\pi}
-\frac{q\pi+pr}{(p\pi)^2}\delta^2+O(\delta^3).
\]

On the other hand, direct expansion of the cycle probability-generating function gives

\[
1-F_m(z)=\mathbb E[C_{m,p}]\delta-
\tfrac12\mathbb E[C_{m,p}(C_{m,p}-1)]\delta^2+O(\delta^3).
\]

Comparing coefficients shows \(\mathbb E C_{m,p}=1/(p\pi)\) and

\[
\operatorname{Var}(C_{m,p})/(\mathbb E C_{m,p})^2
=(2-p)\pi+2pr-1,
\]

which is the finite formula in the finding. All Taylor expansions are valid since the chain is finite and has geometric hitting-time tails.

**Step 3: Critical limit.** Let \(J_m\sim\operatorname{Bin}(m,c/m)\). Then \(\sum_{j=1}^{m}w_j/j=\mathbb E[\mathbf1_{\{J_m\ge1\}}/J_m]\). Since \(J_m\Rightarrow\operatorname{Poisson}(c)\) and the integrand on nonnegative integers is bounded by one, this expectation tends to \(e^{-c}\sum_{j\ge1}c^j/(j\,j!)=e^{-c}A(c)\). Together with \((1-c/m)^m\to e^{-c}\) and \(mp_m=c\), the critical profile follows. The cycle mean additionally satisfies \(\mathbb E C_{m,c/m}/m\to e^c/c\).

**Step 4: Complete shape classification.** The power series for \(A\) is entire and satisfies \(cA'(c)=e^c-1\). Thus

\[
V'(c)=2e^{-c}g(c),\qquad
 g(c)=(1-c)A(c)+e^c-2
=-1+2c-\sum_{j=2}^{\infty}\frac{c^j}{j(j-1)j!}.
\]

Termwise differentiation proves

\[
 g''(c)=-\sum_{j=2}^{\infty}\frac{c^{j-2}}{j!}<0
\quad(c>0).
\]

Moreover \(g(0)=-1\), \(g(1)=e-2>0\), and \(g(c)\le -1+2c-c^2/4\to-\infty\). Strict concavity, these signs, and the intermediate value theorem imply that \(g\) has exactly two positive zeros and is positive strictly between them. Consequently \(V\) has exactly one strict local minimum and one strict local maximum. Since

\[
V(c)=1-2c+3c^2+O(c^3)\quad(c\downarrow0),\qquad
V(c)=1+\frac2c+O(c^{-2})\quad(c\to\infty),
\]

the endpoint limits equal one, and these are the global minimum and maximum. The negative small-\(c\) correction and positive large-\(c\) correction force precisely one crossing \(V=1\) on the strictly increasing interval between the two stationary points. The displayed decimals follow from high-precision evaluations with sign-changing brackets; the number and type of roots follow analytically, not numerically.

**Step 5: Entrance-count interpretation.** Let \(N_{m,p}(t)\) count all entrance events by round \(t\), starting at an entrance. For fixed \(m\) and \(p\), this is an ordinary renewal count with an aperiodic, exponentially tailed positive cycle law. The renewal count mean is asymptotic to \(t/\mathbb EC\), while the count variance is asymptotic to \(t\operatorname{Var}(C)/(\mathbb EC)^3\). Their ratio tends to the squared cycle coefficient of variation. Taking subsequently \(m\to\infty\) at \(p=c/m\) yields \(V(c)\).

## Verification

Run `python3 verify.py` with the standard library. The checker independently solves rational finite birth-death hitting-time moment systems for all \(1\le m\le8\) at six rational values of \(p\), and compares them to the closed form. It also directly iterates the count-chain transition matrix and compares return probabilities with the binomial expression for \(1\le m\le6\), at two rational parameters and twelve time indices each. It checks numeric sign brackets and selected values. The captured execution returned `VERIFY_OK 291 exact rational and numerical assertions`. Exact-rational checks corroborate the finite algebra but cannot establish the infinite-dimensional or global-calculus statements; those follow from Steps 3–4.

## Relationship to prior work

Attrill and Garoni (2026) establish first-completion-time asymptotics for the clumsy coupon collector, including the critical regime. Long (2026) determines the stationary all-present mass and entrance flux \(pq^m\), giving the known mean recurrence scale and fixed-\(p\) first-hitting laws. The present finite mean is therefore not claimed as new. General infinite-server queue busy-cycle Laplace transforms, second moments, and their renewal derivations are longstanding, in particular Liu–Shi (1996) and Roijers–Mandjes–van den Berg (2006). Thus the finite second-moment expression also is not claimed as an independent foundational discovery. The assessed distinction is the full **two-turning-point and one-crossing classification** of the critical clumsy-collector entrance-cycle dispersion, with its precise sub-/super-Poisson renewal-count interpretation. The inspected full texts do not state that classification; broader queueing results may conceal a stronger equivalent, and priority requires independent verification.

## Limitations

The results are for the specific independent uniform random-scan refresh model, complete occupancy, and entrance-to-entrance (not empty-start first-completion) cycles. The critical limit fixes \(c>0\); no joint \(c,m\) scaling or nonuniform type weights are addressed. The high-precision decimal values are illustrations of analytically defined unique roots; they are not exact algebraic identities. The renewal-count statement takes the observation-horizon limit first, then the system-size limit. A 1996 general busy-cycle source and some older variance literature could be inspected only through bibliographic material, creating a residual historical-priority risk. No independent external audit is claimed.

## References

- L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem*, arXiv:2605.14206, first publicly posted 2026-05-14. https://arxiv.org/abs/2605.14206
- C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511, 2026. https://arxiv.org/abs/2605.14511
- F. Roijers, M. Mandjes and H. van den Berg, *Analysis of congestion periods of an M/M/∞-queue*, CWI report PNA-E0606, 2006, especially §5.2. https://ir.cwi.nl/pub/10841/10841D.pdf
- L. Liu and D.-H. Shi, *Busy period in \(\mathrm{GI}^{X}/\mathrm{G}/\infty\)*, Journal of Applied Probability 33 (1996), 815–829. https://doi.org/10.2307/3215361
- M. F. Ramalhoto, *Bounds for the variance of the busy period of the M/G/∞ queue*, Advances in Applied Probability 16 (1984), 929–932. https://doi.org/10.2307/1427350
