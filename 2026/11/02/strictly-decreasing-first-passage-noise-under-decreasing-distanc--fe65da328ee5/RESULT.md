# Strictly decreasing first-passage noise under decreasing-distance resetting

## Finding
Consider one-dimensional Brownian search, restarted at a constant Poisson rate, with a fresh independently sampled restart position after every restart. If the distance from each restart position to a fixed absorbing target has a bounded, nonincreasing probability density on the nonnegative half-line, then the **coefficient of variation of the complete first-passage time is strictly decreasing in the resetting rate**. For every positive rate it exceeds one, and its exact endpoint limits are infinity under vanishing reset rate and one under arbitrarily rapid resetting.

This applies, in particular, when restart positions are uniformly sampled from an interval containing the target. It proves for that geometry, including off-center targets, the reset-rate monotonicity previously supported by numerical evidence in Méndez–Flaquer-Galmés–Campos [1], and extends it to a full distributional shape class.

## Assumptions and scope
Fix a diffusivity \(D>0\), a target position \(x_T\in\mathbb R\), and a rate \(r>0\). In each attempt, start Brownian motion with generator \(D\partial_{xx}\) at an independent position \(R\), drawn from the same law at time zero and at each Poisson reset of rate \(r\). The target absorbs the particle when it is first reached. All Brownian motions, waiting times, and starting positions are mutually independent between attempts; resets are instantaneous. Let \(U=|R-x_T|\).

Assume \(U\) has a Lebesgue probability density \(g:(0,\infty)\to[0,\infty)\) which admits a finite, strictly positive right limit \(c=g(0+)>0\) and has a nonincreasing right-continuous version. No moment assumption on \(U\) is needed. Write \(T_r\) for the total absorption time and \(\operatorname{CV}(r)=\sqrt{\operatorname{Var}(T_r)}/\mathbb ET_r\).

**Theorem.** For every such density and all \(0<r_1<r_2\),
\[
1<\operatorname{CV}(r_2)<\operatorname{CV}(r_1)<\infty.
\]
Moreover,
\[
\lim_{r\downarrow0}\operatorname{CV}(r)=\infty,
\qquad
\lim_{r\uparrow\infty}\operatorname{CV}(r)=1.
\]
These statements concern the first-passage time *averaged over the independently redrawn initial and reset positions*, not a quenched single location or a fixed initial location different from the reset law.

For uniformly distributed positions \(R\) on \([-L,L]\), \(L>0\), every target \(x_T\in[-L,L]\) satisfies the assumption. For \(|x_T|<L\), writing \(a=L-|x_T|\) and \(b=L+|x_T|\), the distance density equals \(1/L\) on \((0,a)\), \(1/(2L)\) on \((a,b)\), and zero beyond \(b\); at the endpoints it is uniform on \((0,2L)\).

## Proof
**Renewal moments.** Put \(q=\sqrt{r/D}>0\), and define
\[
p(q)=\mathbb E[e^{-qU}].
\]
For Brownian motion started at distance \(u>0\) from the absorbing target, the unreset hitting-time Laplace transform is \(e^{-u\sqrt{s/D}}\) for \(s>0\). Conditioning a single attempt on whether target absorption precedes an independent rate-\(r\) reset, and summing the independent attempts, gives the exact transform
\[
\mathbb E[e^{-sT_r}]
=\frac{(r+s)p(\sqrt{(r+s)/D})}
{s+r p(\sqrt{(r+s)/D})},\qquad s\ge0.
\]
In particular, \(p(q)>0\), and differentiation at \(s=0\) yields
\[
\mathbb ET_r=\frac{1-p(q)}{r p(q)},
\qquad
\operatorname{CV}(r)^2
=\frac{1-p(q)^2+q p'(q)}{(1-p(q))^2}.
\tag{1}
\]
All these moments are finite for each fixed positive \(r\): the success probability of an attempt is positive, and each attempt is bounded by an independent exponential restart clock upon failure.

**Positive mixture of uniform distances.** Let \(m=1/c\). Monotonicity of \(g\) allows the construction of a strictly positive random variable \(V\) with tail
\[
\mathbb P(V>u)=g(u)/c\qquad (u\ge0).
\]
The normalization of \(g\) gives \(\mathbb EV=m\). Fubini's theorem then gives
\[
p(q)=\frac{\mathbb E[1-e^{-qV}]}{mq}.
\]
Define the Bernstein-type function
\[
b(q)=\frac{\mathbb E[1-e^{-qV}]}m,
\]
so \(p(q)=b(q)/q\) and \(0<b(q)<q\). From (1), writing \(\mathcal F(q)=\operatorname{CV}(Dq^2)^2\), we obtain
\[
\mathcal F(q)=
\frac{q^2+q^2b'(q)-qb(q)-b(q)^2}{[q-b(q)]^2}.
\tag{2}
\]
Differentiating (2) gives
\[
\mathcal F'(q)=\frac{G(q)}{[q-b(q)]^3},
\]
where
\[
G(q)=3b^2-5qbb'-q^2bb''-qb+2q^2(b')^2+q^2b'+q^3b''.
\tag{3}
\]
Every derivative exists at \(q>0\), without requiring higher moments of \(V\), since exponentially weighted powers are bounded.

**A strictly negative pair kernel.** Let \(V'\) be an independent copy of \(V\). Directly substituting
\[
b=\frac{\mathbb E(1-e^{-qV})}m,
\quad b'=\frac{\mathbb E(Ve^{-qV})}m,
\quad b''=-\frac{\mathbb E(V^2e^{-qV})}m
\]
into (3), and pairing the terms linear in expectations with \(m=\mathbb EV'\), yields
\[
m^2G(q)=\mathbb E[K(qV,qV')].
\tag{4}
\]
For \(x,y>0\), put \(A(x)=1-e^{-x}\) and \(\ell(x)=1-(1+x)e^{-x}>0\). The fully expanded kernel, subsequently collected, is
\[
K(x,y)=
-\frac{xy}{2}\big[x e^{-x}A(y)+y e^{-y}A(x)\big]
+\frac{6-x-y}{2}\ell(x)\ell(y).
\tag{5}
\]
Set
\[
R(x)=\frac{x^2e^{-x}}{\ell(x)},
\qquad S(x)=\frac{x(1-e^{-x})}{\ell(x)}.
\]
The following two strict scalar inequalities hold for every \(x>0\):
\[
S(x)>2,\qquad R(x)>\frac{3-x}{2}.
\tag{6}
\]
Indeed, \(S(x)>2\) is equivalent to
\(x-2+(x+2)e^{-x}>0\). This expression vanishes at zero and has derivative \(1-(1+x)e^{-x}=\ell(x)>0\). The second inequality is equivalent to
\[
H(x):=x^2+2x+3-(3-x)e^x>0.
\]
Here \(H(0)=H'(0)=0\), \(H''(0)=1\), and \(H'''(x)=xe^x>0\), proving the claim for all positive \(x\).

Dividing (5) by \(\ell(x)\ell(y)\) now gives
\[
\frac{2K(x,y)}{\ell(x)\ell(y)}
=6-x-y-R(x)S(y)-R(y)S(x)<0,
\]
because \(S>2\) and \(R>(3-x)/2\). Since \(V,V'>0\) almost surely, equations (3)–(5) imply \(G(q)<0\) for every \(q>0\). The denominator of \(\mathcal F'(q)\) is strictly positive, so \(\mathcal F'(q)<0\). As \(q=\sqrt{r/D}\) increases strictly with \(r\), the coefficient of variation decreases strictly.

**Endpoint limits.** Write \(h(q)=1-p(q)\), so \(h(0+)=0\). Being an average of \(1-e^{-qU}\), this function is concave, increasing, and satisfies \(q h'(q)\le h(q)\). From (1),
\[
\mathcal F(q)=\frac{2h-h^2-qh'}{h^2}
\ge\frac{1-h}{h}\longrightarrow\infty\quad(q\downarrow0).
\]
At the other endpoint, monotonicity and boundedness of \(g\) at zero give, by dominated convergence,
\(q p(q)\to c\) and \(q^2\mathbb E[Ue^{-qU}]\to c\). Therefore \(p(q)\to0\), \(q p'(q)\to0\), and \(\mathcal F(q)\to1\) as \(q\to\infty\). The strict inequality \(\operatorname{CV}(r)>1\) follows from its strict decrease to one. This completes the proof.

## Verification
The standalone file `verify_monotone_cv.py` evaluates the exact closed-form expression (2), its analytic derivative (3), and the independent two-variable expectation (4) for 300 randomly generated finite mixtures of positive \(V\)-laws. It checks the identity \(m^2G(q)=\mathbb EK(qV,qV')\), strict negativity, and agreement of the analytic derivative with a centered numerical difference. It additionally checks 24 interval-target configurations and reports representative endpoint approach for centered uniform restarting. These finite checks are **not** a proof of the infinite-dimensional density-class statement; the strict kernel inequalities (5)–(6) provide that proof.

Reproduce with `python3 verify_monotone_cv.py` in an environment providing only the Python standard library.

## Relationship to prior work
Méndez, Flaquer-Galmés, and Campos [1], first publicly posted January 2, 2024, derive the distributed-reset mean and coefficient of variation. Section VII.B examines a uniform reset interval containing a target, explicitly reports numerical verification that the coefficient of variation decreases with reset rate, but does not prove the claim. The present theorem proves that strict monotonicity for **all** target positions in the closed interval and gives the broader nonincreasing-distance-density sufficient condition. The underlying renewal first-moment calculation is not new.

Evans and Majumdar [2] treat resetting to random positions and optimize mean first-passage times; they do not state a monotonicity theorem for the coefficient of variation over this density class. Reuveni [3] proves that the coefficient of variation equals one at a nonzero optimal restart rate, but does not imply a strict all-rate decreasing law for the nonincreasing-distance class, which has no nonzero mean-optimal rate. Consequently, the theorem is a distribution-shape classification, not a restatement of the universal optimal-restart identity.

## Limitations
The criterion is sufficient, not necessary. Distance densities that rise away from zero or have an initial gap can exhibit different fluctuation behavior; no classification of all such laws is claimed. The initial position must be sampled from the same law used at each reset. The result does not concern correlated reset locations, finite reset-return costs, drifting diffusion, higher-dimensional hitting, or quenched reset positions. A general theorem in broader restart literature could subsume this kernel inequality; publication priority beyond the inspected sources remains uncertain. The numerical checks cannot establish mathematical priority or replace the proof.

## References
[1] V. Méndez, R. Flaquer-Galmés, D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125v1 (January 2, 2024); Phys. Rev. E 109, 044134 (2024), DOI: 10.1103/PhysRevE.109.044134. Relevant material: Secs. II and VII, especially equations (14)–(16), (59), and Sec. VII.B.

[2] M. R. Evans, S. N. Majumdar, *Diffusion with Optimal Resetting*, arXiv:1107.4225 (2011), DOI: 10.1088/1751-8113/44/43/435001. Relevant material: Sec. 4, including equations (45)–(49).

[3] S. Reuveni, *Optimal stochastic restart renders fluctuations in first passage times universal*, arXiv:1512.01600 (2015), Phys. Rev. Lett. 116, 170601 (2016). Relevant material: renewal transforms and optimal-rate coefficient of variation identity.
