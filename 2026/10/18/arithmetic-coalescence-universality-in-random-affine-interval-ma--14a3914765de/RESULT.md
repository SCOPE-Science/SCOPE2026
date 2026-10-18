# Arithmetic coalescence universality in random affine interval maps

## Finding

For every integer \(b\ge2\), consider the equal-base random affine interval maps introduced in Homburg and Kalle [1]:
\[
f_0(x)=bx\pmod1,\qquad
f_j(x)=\frac{x+j-1}{b}\quad(1\le j\le b),\qquad 0\le x<1.
\]
At each time choose \(f_0\) with probability \(p\in(0,1)\), and each \(f_j\), \(j\ge1\), with probability \(q/b\), where \(q=1-p\). Apply the **same** independently chosen branch at each time to two initial points \(x\ne y\). Let \(\tau\) be their first exact meeting time (with \(\tau=\infty\) if they never meet).

Write \(\mathbb Z[1/b]=\{m/b^r:m\in\mathbb Z,\ r\in\mathbb N_0\}\). The following classification holds for *every fixed pair* \(x,y\in[0,1)\):

1. If \(x-y\notin\mathbb Z[1/b]\), then \(\tau=\infty\) for **every** branch sequence.
2. If \(x-y\in\mathbb Z[1/b]\), let \(k\ge1\) be the smallest integer for which \(b^k(x-y)\in\mathbb Z\). For each integer \(n\ge1\),
\[
\Pr(\tau=n)=
\begin{cases}
\displaystyle\frac{k}{n}\binom{n}{(n+k)/2}p^{(n+k)/2}q^{(n-k)/2},&n\ge k,\ n\equiv k\pmod2,\\[4pt]
0,&\text{otherwise}.
\end{cases}
\]
The probability generating function, with nonmeeting trajectories contributing zero, is
\[
\mathbb E[z^\tau\mathbf1_{\tau<\infty}]
=\left(\frac{1-\sqrt{1-4pqz^2}}{2qz}\right)^k,
\qquad 0<z\le1.
\]
In particular,
\[
\Pr(\tau<\infty)=
\begin{cases}1,&p\ge\tfrac12,\\(p/q)^k,&p<\tfrac12.\end{cases}
\]
For \(p\ne1/2\), conditional on \(\tau<\infty\),
\[
\mathbb E[\tau\mid\tau<\infty]=\frac{k}{|2p-1|},\qquad
\operatorname{Var}(\tau\mid\tau<\infty)=\frac{4kpq}{|2p-1|^3}.
\]
At the critical probability \(p=1/2\), meeting occurs almost surely but has infinite expected waiting time, with the sharp survival asymptotic
\[
\Pr(\tau>n)\sim k\sqrt{\frac{2}{\pi n}}\quad(n\to\infty).
\]
The entire law is independent of the base \(b\) and of the positions of \(x,y\) beyond their minimal denominator depth \(k\).

There is a parameter-universal **critical crossover**. Fix \(a>0\) and \(\theta\in\mathbb R\), choose \(\varepsilon\downarrow0\), integers \(k_\varepsilon\ge1\) with \(\varepsilon k_\varepsilon\to a\), and probabilities \(p_\varepsilon=(1+\theta\varepsilon)/2\in(0,1)\). Choose any pair at minimal denominator depth \(k_\varepsilon\). Then
\[
\Pr(\tau<\infty)\longrightarrow
\exp\bigl(a(\theta-|\theta|)\bigr),
\]
and, **conditional on meeting**,
\[
\varepsilon^2\tau\ \xrightarrow{\mathrm{law}}\ T_{a,|\theta|},\qquad
\mathbb E[e^{-uT_{a,|\theta|}}]
=\exp\left(a\left[|\theta|-\sqrt{\theta^2+2u}\right]\right),\quad u\ge0.
\]
Here \(T_{a,c}\) is the first hitting time of zero by standard Brownian motion started at \(a\) with constant drift \(-c\). Its density on \(t>0\) is
\[
\frac{a}{\sqrt{2\pi t^3}}\exp\left(-\frac{(a-ct)^2}{2t}\right).
\]
For \(c>0\) this is an inverse-Gaussian first-passage law; at \(c=0\) it is the heavy-tailed Lévy first-passage law. At fixed \(x\), the set of other initial points meeting almost surely for \(p\ge1/2\) is the countable dense set \((x+\mathbb Z[1/b])\cap[0,1)\), excluding \(x\); all these meetings hold simultaneously on a single probability-one event.

## Assumptions and scope

The maps act on the half-open interval \([0,1)\), with the fractional-part convention for \(f_0\); the integer \(b\ge2\) need not be prime. The branch choices are independent across time and shared by the two trajectories. Every statement for fixed \(b,p,x,y\) is exact in real arithmetic. Exact meeting, meaning equality of the two coordinates, is distinguished from asymptotic synchronization, meaning convergence of their separation to zero. The crossover concerns a *sequence* of pairs whose minimal \(b\)-adic denominator depths tend to infinity; the positions of the pairs may otherwise vary arbitrarily.

## Proof

**Arithmetic separation invariant.** For a current signed difference \(d=x-y\), any contracting branch sends \(d\) to \(d/b\). The expanding branch sends it to \(bd-m\), with \(m\in\mathbb Z\) the difference of the integer parts of \(bx\) and \(by\). Thus membership of \(d\) in \(\mathbb Z[1/b]\) is preserved in both directions: neither operation can turn an element outside this ring into an element inside it. Equality of the images forces the new difference to belong to the ring, so non-\(b\)-adic pairs never meet.

**Exact depth dynamics.** Suppose \(d\ne0\) belongs to \(\mathbb Z[1/b]\), and define its depth \(K(d)=\min\{k\ge1:b^kd\in\mathbb Z\}\). Because \(|d|<1\), depth is well-defined and positive. Each contraction sends \(K\) to \(K+1\). Under expansion, if \(K\ge2\) then \(bd-m\ne0\) and its depth is \(K-1\), since subtracting an integer does not change whether successive powers of \(b\) make the difference integral. If \(K=1\), then \(bd\) is integral and the two fractional parts coincide: this is first meeting. Therefore, up to absorption at zero, \(K\) makes a downward step with probability \(p\) and an upward step with probability \(q\), independent of \(b\), the contracting-branch label, or the trajectory locations.

**First-passage enumeration and probability.** Starting at depth \(k\), a path first reaches zero at time \(n\) only if \(n\ge k\) and \(n-k\) is even. Such a path contains \((n+k)/2\) downward steps and \((n-k)/2\) upward steps. The classical cyclic ballot/reflection count gives the fraction \(k/n\) of these step words that hit zero for the first time at their endpoint, producing the displayed exact mass. Let \(r(z)\) be the defective first-passage generating function starting at depth one. First-step decomposition followed by the strong Markov property gives \(r(z)=z[p+qr(z)^2]\). Choosing the minimal nonnegative root gives
\[
r(z)=\frac{1-\sqrt{1-4pqz^2}}{2qz}.
\]
Successive downcrossings from \(k\) to \(k-1\) have the same generating function, so the depth-\(k\) transform is \(r(z)^k\). At \(z=1\), the root is \(\min(1,p/q)\). This proves the meeting probability. When \(p<q\), conditioning on absorption changes the probability of each downstep to \(q\) and each upstep to \(p\): for every successful word the Radon–Nikodym ratio to the reversed-drift walk equals \((p/q)^k\). Consequently, the conditioned hitting law is the ordinary walk with downward bias \(\max(p,q)\). Its generating-function derivatives give the stated conditional mean and variance.

**Critical tail.** For \(p=q=1/2\), reflection at the absorbing boundary yields
\[
\Pr(\tau>n)=\Pr(-k<S_n\le k),
\]
where \(S_n\) is the ordinary length-\(n\) simple symmetric random walk started at zero. The displayed interval contains exactly \(k\) lattice points of the allowed parity. The local central limit theorem therefore gives \(\Pr(\tau>n)\sim k\sqrt{2/(\pi n)}\). Since the tail is not summable, \(\mathbb E\tau=\infty\).

**Critical crossover.** Put \(z_\varepsilon=e^{-u\varepsilon^2}\), \(q_\varepsilon=1-p_\varepsilon\). For fixed \(u\ge0\), the quadratic root above satisfies
\[
r_{p_\varepsilon}(z_\varepsilon)
=1+\varepsilon\left(\theta-\sqrt{\theta^2+2u}\right)+o(\varepsilon),\qquad
r_{p_\varepsilon}(1)=1+\varepsilon(\theta-|\theta|)+o(\varepsilon).
\]
Raising the second expression to the \(k_\varepsilon\)-th power gives the limiting meeting probability. Dividing the first expression by the second, raising to the \(k_\varepsilon\)-th power, and taking logarithms gives the claimed conditional Laplace-transform limit. Continuity and uniqueness of Laplace transforms identify the Brownian first-passage distribution, including its driftless boundary. The countable dense simultaneous-meeting statement follows from \(\Pr(\tau<\infty)=1\) for every pair on the same \(b\)-adic coset and a countable intersection of probability-one events.

## Verification

Run `python verify.py` from the directory containing this document. The standalone script uses exact rational arithmetic to enumerate *both original trajectories*, rather than replacing them by the purported depth process. It compares their first exact-meeting probabilities with the ballot formula for bases \(2,3,4,6\), various depths, positions, and rational expansion probabilities. It also tests non-\(b\)-adic nonmeeting at finite horizons, and an irregular composite-base denominator case. The replay passed **511** exact-rational comparisons. Finite enumerations and finite-horizon nonmeeting tests are not proofs of the all-time classification or the limiting laws; these are derived above.

## Relationship to prior work

Homburg and Kalle [1] introduced this exact affine system for all integer base pairs and proved a Lyapunov-sign trichotomy for two-point trajectories: synchronization for negative exponent, intermittency at zero, and an absolutely continuous off-diagonal stationary measure for positive exponent. Their Section 2.3 also treats collapse of multivalued grid images, and Section 3 uses random walks on dyadic scale indices. Those results and classical one-dimensional first-passage theory are prior ingredients. The present claim concerns **exact coincidence of a specified pair**, the arithmetic classification of which pairs can coincide, their complete meeting-time law, and a base-universal critical conditional distribution. These conclusions do not follow as stated from the source's distance-convergence or stationary-measure theorems. The related random circle-endomorphism work [2] has a smooth circle map with continuously distributed additive noise, rather than these discrete affine contractions, and its main results concern recurrence and stationary measures, not this arithmetic exact-meeting law. The Pelikan random map [3] shares the doubling/halving mechanisms but its studied invariants are one-point stationary and correlation statistics, not first coincidence of common-noise pair trajectories.

The ballot count, biased-walk hitting probabilities, Brownian first-passage density, and Laplace-transform convergence are standard mathematical tools, not separately claimed as new. Searches and text comparisons found no explicit prior theorem packaging the exact arithmetic pair classification with its full law and critical crossover for this IFS. This is a best-knowledge priority assessment, not a uniqueness proof.

## Limitations

The claim is restricted to the equal-base subfamily \(M=N=b\), independent and identically distributed shared branch choices, and exact real-valued trajectories. It does not extend without new arguments to unequal bases, independently forced pairs, finite-precision rounding, perturbations of slopes, or random additive noise. For fixed \(p<1/2\), a \(b\)-adic pair has nonmeeting probability \(1-(p/q)^k\) even though the original paper proves almost-sure asymptotic synchronization. The inverse-Gaussian/Lévy limit is a conditional limit for a parameter-dependent family of gaps, not a finite-depth approximation error bound. Because the first-passage formulas are classical once the arithmetic reduction has been recognized, equivalent prior calculations in unindexed literature remain a priority risk. Independent mathematical review and priority review have not been carried out.

## References

[1] A. J. Homburg and C. Kalle, *Iterated function systems of affine expanding and contracting maps on the unit interval*, arXiv:2207.09987v1 (public 20 July 2022), https://arxiv.org/html/2207.09987v1 ; later published in *Advances in Mathematics* 482 (2025), 110605.

[2] V. P. H. Goverse, A. J. Homburg and J. S. W. Lamb, *Intermittent Two-Point Dynamics at the Transition to Chaos for Random Circle Endomorphisms*, *Communications in Mathematical Physics* 407 (2026), article 87, https://pmc.ncbi.nlm.nih.gov/articles/PMC13050346/ .

[3] J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck and R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269 (public 18 August 2023), https://arxiv.org/abs/2308.09269 .
