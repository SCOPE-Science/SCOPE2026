# Universal logarithmic sampling of discordant ties with persistent receptive edges

## Finding

For a finite graph with the adaptive interaction rule below, suppose that both permanently receptive and permanently unreceptive edges are present. Then, for every unreceptive edge \(e\), the number \(N_e(t)\) of times it is selected among the first \(t\) steps obeys

\[
\lim_{t\to\infty}\frac{N_e(t)}{\log t}=\frac{1}{|\log\delta_e|},\qquad
\lim_{t\to\infty}\frac{\log z_e(t)}{\log t}=-1
\quad\text{almost surely.}
\]

For every receptive edge \(f\), with \(k\) the total number of receptive edges,

\[
\lim_{t\to\infty}\frac{N_f(t)}{t}=\frac1k,\qquad
\lim_{t\to\infty}\frac{\log(1-z_f(t))}{t}
=\frac{\log(1-\gamma_f)}k\quad\text{almost surely.}
\]

The count and rate conclusions apply equally on the event of eventual stabilization into the two nonempty edge classes. Thus one discordant edge is contacted \(\log t/|\log\delta_e|+o(\log t)\) times even though its interaction weight vanishes with the universal logarithmic exponent \(-1\). The exact exponent does not depend on the decay parameter; the multiplicative count coefficient does.

## Assumptions and scope

There is a fixed finite nonempty set of \(m\) edges; at integer time \(t\ge0\) each edge has a weight \(z_e(t)\) satisfying \(0<z_e(0)<1\). Exactly one edge is selected each time, using conditionally independent fresh random sampling with

\[
\mathbb P(E_t=e\mid\mathcal F_t)
=\frac{z_e(t)}{W(t)},\qquad W(t)=\sum_{g=1}^{m}z_g(t).
\]

A selected receptive edge \(f\) receives \(z_f(t+1)=z_f(t)+\gamma_f(1-z_f(t))\), with \(0<\gamma_f<1\); a selected unreceptive edge \(e\) receives \(z_e(t+1)=\delta_e z_e(t)\), with \(0<\delta_e<1\). Unselected weights remain unchanged. Initially assume a *fixed partition* \(\mathcal P\sqcup\mathcal N\) into nonempty receptive and unreceptive sets, and write \(k=|\mathcal P|\). This allows different parameters per edge. The final assertion only requires that the edge classifications become fixed after some almost surely finite (possibly random) integer time, with both eventual classes nonempty; no uniform bound on that time is assumed. In a bounded-confidence interpretation, receptivity means that the endpoints' opinion gap is below the confidence bound at the time of interaction. No independence between opinion histories and edge-selection histories is assumed for this eventual-stabilization extension.

## Proof

**Step 1 (uniform hazard bounds).** Under fixed classification, every receptive edge has nondecreasing weight. Set \(c=\min_{f\in\mathcal P}z_f(0)>0\). Since every edge's weight stays in \((0,1)\),

\[
c\le W(t)\le m\quad\text{for every }t.
\]

Fix an unreceptive edge \(e\), put \(d=\delta_e\in(0,1)\), \(u=z_e(0)\), and let \(N_e(t)\) count its selections before time \(t\). Exactly

\[
z_e(t)=u d^{N_e(t)},\qquad
\frac{u}{m}d^{N_e(t)}\le\mathbb P(E_t=e\mid\mathcal F_t)
\le\frac{u}{c}d^{N_e(t)}.
\]

**Step 2 (geometric waiting times).** Let \(\tau_n\) be the time of the \(n\)-th selection of \(e\) and \(G_n=\tau_{n+1}-\tau_n\). At each step between these two selections, the count of \(e\) stays \(n\); its selection probability is always between \(a d^n\) and \(b d^n\), where \(a=u/m>0\) and \(b=u/c<\infty\). In particular, every \(G_n\) is almost surely finite. For any \(0<\varepsilon<1\), conditional on the stopping-time history at \(\tau_n\), a union bound and the product bound for conditional nonselection give, for all sufficiently large \(n\),

\[
\begin{aligned}
\mathbb P\!\left(G_n\le d^{-(1-\varepsilon)n}\mid\mathcal F_{\tau_n}\right)
&\le b d^{\varepsilon n},\\
\mathbb P\!\left(G_n\ge d^{-(1+\varepsilon)n}\mid\mathcal F_{\tau_n}\right)
&\le\exp\left(-\frac a2 d^{-\varepsilon n}\right).
\end{aligned}
\]

Both probability bounds are summable in \(n\). The first Borel–Cantelli lemma (independence is not needed), followed by a countable sequence of rational \(\varepsilon\downarrow0\), yields

\[
\lim_{n\to\infty}\frac{\log G_n}{n}=|\log d|
\quad\text{almost surely.}
\]

Because \(\tau_n\) is the sum of the preceding positive waiting times, bounding the sum of their exponentials above by the number of terms times the largest term and below by the latest term gives

\[
\lim_{n\to\infty}\frac{\log\tau_n}{n}=|\log d|.
\]

Inverting this increasing sequence (and noting \(\tau_n\to\infty\)) proves \(N_e(t)/\log t\to1/|\log d|\). The exact identity for \(z_e(t)\) above yields \(\log z_e(t)/\log t\to-1\). Since there are finitely many negative edges these conclusions hold simultaneously almost surely.

**Step 3 (receptive edges).** For a receptive edge \(f\), the conditional selection probability is at least \(z_f(0)/m\). For any fixed edge, the centered selection indicators form bounded martingale differences, so their averages tend almost surely to zero (for instance by Azuma's inequality and Borel–Cantelli). Thus

\[
\liminf_{t\to\infty}\frac{N_f(t)}{t}\ge\frac{z_f(0)}m>0.
\]

The exact deficit identity

\[
1-z_f(t)=(1-z_f(0))(1-\gamma_f)^{N_f(t)}
\]

shows \(z_f(t)\to1\) exponentially. Step 2 shows all unreceptive weights tend to zero. Consequently \(W(t)\to k\) and the conditional selection probabilities of receptive edges converge to \(1/k\). Apply the same bounded-martingale strong law and Cesàro convergence to obtain \(N_f(t)/t\to1/k\). Taking logarithms of the displayed deficit identity gives the stated exponential-rate limit. Their simultaneous validity follows by finiteness of the graph.

**Step 4 (eventually fixed classes).** For every deterministic integer \(T\) and each nonempty pair of disjoint subsets partitioning the edges, couple the original model after \(T\) to a process whose classes are frozen at that partition, using the same future uniform random choices and the observed weights at \(T\). Conditional on the information at \(T\), Steps 1–3 apply with those (strictly positive) weights, so the frozen process satisfies all limits with conditional probability one. On the event that the original classes agree with the frozen partition for all times after \(T\), the coupled weight and selection trajectories coincide. There are countably many \(T\) and finitely many partitions, so the result holds almost surely on their union, precisely the event of eventual stabilization into two nonempty classes. The finite offset before \(T\) does not change any limit.

## Verification

The accompanying `verification/check.py` uses Python's standard library to simulate an edge-proportional process with one receptive and two unreceptive edges, including distinct decrease rates. It tests finite-time contact counts against the logarithmic scales and weight exponents, and checks a bounded-confidence three-agent configuration in which the two edge classes cannot change. A comparison simulation with every edge unreceptive is included solely to reproduce a known different regime. All checks passed when executed from the supplied file. Monte Carlo arithmetic and finite-time behavior are corroboration, **not** the proof of the almost-sure theorem, which is given above.

For a concrete graph realization, consider the path on three agents with initial opinions \((0.2,0.3,0.9)\), confidence bound \(c=0.25\), and conventional compromise parameter \(0<\mu\le1/2\). The first edge is always receptive: averaging keeps the first two opinions in \([0.2,0.3]\). The second edge is always unreceptive, as its endpoint gap remains at least \(0.6\). Both types therefore occur with probability one for any interior initial edge weights.

## Relationship to prior work

Thompsky, Wu, Porter and Luo [1] define the edge-proportional selection process, its positive and negative weight updates, and almost-sure convergence of each weight to zero or one (their Section IV.1, Theorem 2). Their Section IV.2 analyzes eventual stabilization of effective graphs. Those statements do not specify the calendar-time asymptotic selection counts or the universal \(\log z_e(t)/\log t=-1\) exponent. The present theorem quantifies those rates in the mixed receptive/unreceptive regime and permits heterogeneous update parameters.

McNulty and Raban [2] rigorously analyze a closely related sampler with \(\mathbb P(E_t=e)\) proportional to a decreasing exponential potential of the count for **every** coordinate. Their Section 2.3 assumes strictly positive discount exponents and proves asymptotically positive frequencies for all coordinates; that all-unreceptive regime is distinct and is not claimed as new here. In the present mixed regime the receptive weights instead *increase* toward one, so the negative coordinates have sublinear logarithmic counts and the usual all-positive-discount conclusion cannot imply the displayed limits. Kaur [3] studies negatively reinforced urn sampling from weights on occupancy proportions rather than these raw-count, mixed-sign rules.

## Limitations

The model is finite and discrete-time, with strictly interior initial weights and strict update factors. The precise rate is an almost-sure asymptotic, not a deterministic pointwise-in-time upper or lower bound or a uniform finite-sample confidence interval. The eventual-stabilization corollary does not assert stabilization when limiting opinion gaps hit the confidence boundary. The leading negative-edge exponent cannot distinguish different decay factors without observing the logarithmic contact-count coefficients. The result does not address adaptive graph rewiring, continuous-time tie decay, or finite-window statistical identifiability. No claim of universal novelty beyond the specified model and hypotheses is made.

## References

[1] L. Thompsky, Y. Y. Wu, M. A. Porter, J. Luo, *A Bounded-Confidence Model of Opinion Dynamics with Adaptive Interaction Probabilities*, arXiv:2605.20418v1 (publicly posted 2026-05-19), https://arxiv.org/html/2605.20418v1 . Relevant material: Sections III, IV.1 and IV.2.

[2] B. McNulty and M. Raban, *Self-Balancing Sequential Sampling: Fast Convergence with Controlled Predictability*, arXiv:2607.20818v1, https://arxiv.org/abs/2607.20818 . Relevant material: Sections 2.1–2.3 and Appendix B.2.

[3] N. Kaur, *Negatively Reinforced Balanced Urn Schemes*, arXiv:1808.00796, https://arxiv.org/abs/1808.00796 . Relevant material: model definition and main laws of large numbers.
