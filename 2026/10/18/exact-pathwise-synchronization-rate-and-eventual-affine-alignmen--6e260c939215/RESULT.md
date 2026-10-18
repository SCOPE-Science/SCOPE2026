# Exact pathwise synchronization rate and eventual affine alignment in random interval homeomorphisms

## Finding

Fix \(0<c<1/2\). For each infinite sequence of independent fair choices \(\omega_n\in\{0,1\}\), define \(F_\omega^{(0)}=\operatorname{id}\) and \(F_\omega^{(n)}=f_{\omega_{n-1}}\circ\cdots\circ f_{\omega_0}\), using the two increasing homeomorphisms specified below. There is a **single probability-one set** of driving sequences such that, simultaneously for **every** distinct \(x,y\in(0,1)\),

\[
\lim_{n\to\infty}\frac1n\log\left|F_\omega^{(n)}(y)-F_\omega^{(n)}(x)\right|=\lambda(c)=H(c)-\log2<0,
\]

where \(H(c)=-c\log c-(1-c)\log(1-c)\) is binary entropy in nats. Thus \(\lambda(c)=-D_{\mathrm{KL}}(\mathrm{Bern}(c)\|\mathrm{Bern}(1/2))\).

There is a stronger, **eventually exact affine relation**. In a two-sided Bernoulli extension let \(z_n=\varphi(\sigma^n\omega)\) be the measurable invariant graph of Alsedà–Misiurewicz and let

\[
D_0=1,\qquad D_n(\omega)=\prod_{j=0}^{n-1}f'_{\omega_j}(z_j).
\]

With probability one, for every distinct \(0<x<y<1\) there exist a finite integer \(N=N(\omega,x,y)\) and a number \(C=C(\omega,x,y)>0\) such that for **every** \(n\ge N\),

\[
F_\omega^{(n)}(y)-F_\omega^{(n)}(x)=C D_n(\omega).
\]

From time \(N\) onward the two trajectories and the invariant graph follow the same linearity branch of the map selected at each step. The distance asymptotic descends to the one-sided driving sequence because distances depend only on nonnegative-time symbols.

## Assumptions and scope

Put \(a=1/[2(1-c)]\) and \(b=1/(2c)\), so \(0<a<1<b\). On \([0,1]\) define

\[
 f_0(t)=\begin{cases}at,&0\le t\le1-c,\\1-b(1-t),&1-c\le t\le1,\end{cases}\qquad
 f_1(t)=\begin{cases}bt,&0\le t\le c,\\1-a(1-t),&c\le t\le1.\end{cases}
\]

Both are increasing endpoint-fixing piecewise-affine homeomorphisms. Their unique breakpoints are \(k_0=1-c\) and \(k_1=c\). The base is the two-sided Bernoulli shift \((\Omega,\mathbb P,\sigma)\), with fair independent symbols \(\omega_j\), \(j\in\mathbb Z\). The established invariant graph \(\varphi(\omega)\in(0,1)\) obeys \(f_{\omega_0}(\varphi(\omega))=\varphi(\sigma\omega)\), and its marginal is Lebesgue measure on \([0,1]\). In particular \(z_n=\varphi(\sigma^n\omega)\) is uniform for each \(n\), and the graph measure is ergodic. These are documented in [1], Sections 3, 5, and 6, including Theorem 5.10, Theorem 6.1, and Proposition 6.2.

The theorem concerns **all interior initial points**, each pair simultaneously for one typical driving realization. No assertion covers the fixed endpoints \(0,1\). The exact co-branching identity is stated with a two-sided extension because the invariant graph is intrinsically past-measurable; the numerical distance exponent is a property of the future-only sequence.

## Proof

**1. Negative stationary logarithmic slope.** The graph measure is ergodic because it is measurably isomorphic to the Bernoulli base [1]. Each \(z_j\) has the uniform distribution and is independent of the current symbol \(\omega_j\). Every breakpoint has zero probability of being hit. For either selected map the slope equals \(a\) on a subinterval of length \(1-c\) and \(b\) on the remaining subinterval of length \(c\). Thus the ergodic theorem applies to the bounded measurable logarithmic-slope observable and yields

\[
\lim_{n\to\infty}n^{-1}\log D_n=(1-c)\log a+c\log b=H(c)-\log2=:\lambda(c).
\]

Strict concavity of binary entropy gives \(H(c)<\log2\) for \(0<c<1/2\), hence \(\lambda(c)<0\). The expression for the exponent itself is implicit in the stationary-slope computation of [1], Section 6; the new assertion is its equality to the **global finite-distance pathwise** exponent.

**2. Avoidance of the moving breakpoint at subexponential scales.** Let \(d_n=|z_n-k_{\omega_n}|\). For each fixed \(\eta>0\), stationarity of the Lebesgue marginal implies

\[
\mathbb P\{d_n<e^{-\eta n}\}\le2e^{-\eta n}\quad(n\ge1).
\]

No independence between these events is needed. Since their probabilities are summable, the first Borel–Cantelli lemma implies \(d_n\ge e^{-\eta n}\) for all sufficiently large \(n\), almost surely. In addition, \(d_n>0\) for every \(n\) almost surely, by a countable union of null events.

Choose \(0<\eta<-\lambda(c)/3\). By Step 1, for all sufficiently large \(n\), \(D_n\le\exp[(\lambda(c)+\eta)n]\). Therefore

\[
\frac{d_n}{D_n}\ge\exp[(-\lambda(c)-2\eta)n]\longrightarrow\infty.
\]

Consequently \(R(\omega):=\tfrac12\min\{z_0,1-z_0,\inf_{n\ge0}d_n/D_n\}\) is strictly positive almost surely. Work on a shift-invariant probability-one set on which this assertion, the graph identity, and the ergodic limit hold at every integer shift.

**3. An exact random affine stable neighborhood.** If \(|u-z_0|<R(\omega)\), then

\[
F_\omega^{(n)}(u)=z_n+D_n(u-z_0)\qquad\text{for every integer }n\ge0.
\]

This follows inductively. At time \(n\), the induction hypothesis puts the orbit displacement at \(D_n|u-z_0|<d_n/2\); thus \(u\)'s orbit and \(z_n\) lie strictly on the same side of \(k_{\omega_n}\), and the selected map is affine with identical slope at both points. The induction extends exactly, not approximately, through the next step. The distance to the interval endpoints in the definition of \(R\) ensures that the initial neighborhood remains in \((0,1)\).

**4. Every interior orbit enters such an affine neighborhood.** Since \(R>0\) almost surely, there is a fixed number \(\varepsilon_0>0\) for which \(\mathbb P\{R>\varepsilon_0\}>0\). Ergodicity of the two-sided Bernoulli shift gives, almost surely, infinitely many integers \(m\ge0\) with \(R(\sigma^m\omega)>\varepsilon_0\). By Theorem 5.10 of [1], there exists a probability-one set of \(\omega\) for which the images of **any** two interior initial points approach each other. Since the graph point \(z_0\in(0,1)\), this gives, simultaneously for all \(u\in(0,1)\),

\[
|F_\omega^{(m)}(u)-z_m|\longrightarrow0.
\]

Fix one such \(\omega\) and an arbitrary \(u\). At a sufficiently late recurrent time \(m\), the difference is below \(\varepsilon_0\), while \(R(\sigma^m\omega)>\varepsilon_0\). Applying Step 3 to the shifted sequence gives **for every** \(n\ge m\)

\[
F_\omega^{(n)}(u)-z_n=
D_{n-m}(\sigma^m\omega)\,[F_\omega^{(m)}(u)-z_m].
\]

Thus this orbit follows the graph's affine branch at every future step. The underlying event is independent of \(u\), so the conclusion holds for all uncountably many interior points, with entrance times allowed to vary.

**5. Pairwise exact formula and exponent.** Apply Step 4 to a fixed pair \(x<y\), and take \(N\) no smaller than both entrance times. Each trajectory and the graph follow identical branches at all steps starting at \(N\); hence for every \(n\ge N\),

\[
F_\omega^{(n)}(y)-F_\omega^{(n)}(x)=
\big(F_\omega^{(N)}(y)-F_\omega^{(N)}(x)\big)
\frac{D_n}{D_N}.
\]

Strict monotonicity makes the parenthesized quantity positive. Set \(C=[F_\omega^{(N)}(y)-F_\omega^{(N)}(x)]/D_N>0\). Step 1 now gives the stated logarithmic asymptotic. For \(x>y\), exchange labels. The event is already common to all initial pairs, and the future-only distance assertion descends to the one-sided Bernoulli law. This completes the proof.

## Verification

The reproducible file `verify.py` checks exact parameter normalization, exact continuity and endpoint identities, the slope and entropy relations, and finite rational-iteration examples using exact fractions. In those examples it identifies a final observed cross-branch time and verifies the resulting exact multiplicative gap relation thereafter; the checker prints `VERIFY_OK`. These finite checks **do not establish** the infinite almost-sure theorem. The infinite steps are the ergodic theorem, Borel–Cantelli, recurrence, and the prior all-interior synchronization theorem, as explicitly proved or cited above.

## Relationship to prior work

Alsedà and Misiurewicz [1] constructed this exact one-parameter family; their Theorem 5.10 gives qualitative synchronization simultaneously for all interior points, and their Section 6 calculates the stationary Lyapunov exponent. The paper explicitly records uncertainty about exponential synchronization. The present theorem is **not** a discovery of the stationary marginal or the slope exponent alone: it upgrades them to the sharp pathwise distance exponent and to eventual **exact equality** with the affine derivative cocycle.

Malicet [2] subsequently proved broad local exponential contraction results for random interval homeomorphisms, so exponential contraction *without a sharp exponent* is not claimed as new. Those statements do not give the model-specific almost-sure equality of the finite-distance rate to the stationary Lyapunov exponent or eventual exact common-branch dynamics. Gharaei and Homburg [3] analyze mostly smoother random interval diffeomorphisms, and Barański and Śpiewak [4] classify stationary measures for a broader piecewise-affine family. Czudek [5] proves average exponential synchronization/mixing for \(C^2\) diffeomorphisms. None of the inspected theorems establishes the present eventual exact affine identity. The proof uses the special finite-breakpoint geometry and the uniform stationary marginal; it is not presented as a general consequence for smooth random systems.

## Limitations

The parameter \(c\) must be fixed strictly between \(0\) and \(1/2\). The endpoints of the interval are common fixed points and are excluded. The theorem asserts almost-sure pointwise rates simultaneously for all interior starting pairs, not a deterministic entrance-time estimate, a uniform contraction bound over the whole open interval, an annealed moment rate, or a statement about nonstationary driving. The exact identity uses a typical two-sided graph extension. An earlier unindexed explicit derivation of the same exact affine property cannot be absolutely ruled out.

## References

[1] L. Alsedà and M. Misiurewicz, *Random interval homeomorphisms*, arXiv:1212.4440v1 (first public 2012-12-18), especially Theorem 5.10, Theorem 6.1, and Proposition 6.2. https://arxiv.org/abs/1212.4440

[2] D. Malicet, *Random walks on Homeo(S¹)*, arXiv:1412.8618v1 (2014-12-30), Section 2.4 and Theorem F. https://arxiv.org/abs/1412.8618

[3] S. Gharaei and A. J. Homburg, *Random interval diffeomorphisms*, arXiv:1611.07248v1 (2016-11-22), Theorem 4.1 and Lemma 4.1. https://arxiv.org/abs/1611.07248

[4] K. Barański and A. Śpiewak, *Singular stationary measures for random piecewise affine interval homeomorphisms*, arXiv:1905.11048v1 (2019-05-27), Theorem 2.4 and related measure results. https://arxiv.org/abs/1905.11048

[5] K. Czudek, *Exponential decay of correlations for random interval diffeomorphisms*, arXiv:2504.16549 (first public 2025-04-23), Introduction and Theorem 1. https://arxiv.org/abs/2504.16549
