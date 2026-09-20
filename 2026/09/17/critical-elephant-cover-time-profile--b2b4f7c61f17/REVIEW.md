# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.**

The argument was checked against the critical Brownian embedding and clock estimates stated in Qin's arXiv:2609.17264v1.

The key scaling identity is consistent. If \(n=\lfloor L^2t\rfloor\),
\(u_k=A_n-A_k\), and \(H=A_n-A_\ell\), then

\[
\frac{1}{La_k}
=
\sqrt t\,e^{-u_k/2}(1+o(1))
\]

uniformly for \(k\ge\ell\), because \(a_k=k^{-1/2}(1+O(k^{-1/2}))\) and
\(A_n-A_k=\log(n/k)+O(k^{-1/2})\). Thus the \(L^2\)-scale rare path is exactly a
time-reversed Brownian path multiplied by the exponential damping factor.

The factor in the limiting profile was checked separately: the Brownian endpoint
density contributes \(1/\sqrt{2\pi H}\), while
\(H\sim2\log L\). Hence

\[
\sqrt{\log L}/\sqrt{2\pi H}\to1/(2\sqrt\pi),
\]

which matches the stated formula.

The approximation must be valid at absolute probability error
\(o(H^{-1/2})\), not merely in probability. The proof supplies this stronger
control. With \(\ell=(\log n)^{16}\), the critical concentration bound makes
\(|M_\ell|>(\log n)^{1/4}\) exponentially smaller than \(H^{-1/2}\). Qin's
Lemma 3.9 then gives a polynomially smaller clock-error probability after using
a tolerance \(H^{-4}\). Standard Brownian reflection/modulus bounds make both the
clock interpolation and the deterministic \(A_k\)-grid interpolation errors
\(o(H^{-1/2})\). The early segment is deterministically \(o(L)\).

The Brownian rare-path lemma was checked by conditioning on the terminal endpoint.
On the event of bounded supremum or bounded oscillation, the terminal endpoint lies
in a fixed compact interval. Conditional reversal gives a Brownian bridge. After
exponential damping, its bridge correction is \(O_{\mathbb P}(H^{-1/2})\), its
starting-point drift vanishes uniformly for \(x_H=o(\sqrt H)\), and its tail at
large reversed time vanishes. This yields the stated endpoint mixture.

The cover-time identity is exact for nearest-neighbor paths:
covering the one-dimensional torus is equivalent to the lifted running range reaching \(L-1\).
The exit event is likewise exactly the running-supremum event. The
\(1-1/L\) cover threshold does not change the limiting profile.

Qin's Proposition 3.5 gives the required integrable envelope, so the a.e. tail
limit legitimately transfers to the first moment. Tonelli's identity
\(\int_0^\infty {\bf1}_{\{Z<t^{-1/2}\}}dt=Z^{-2}\) verifies the negative-second-
moment representation of the constants.

No hidden assumption of independence between the ERW and the embedding was used:
the future Brownian motion is invoked conditionally after the stopping time
\(T_\ell\), and the required clock estimate is itself conditional on the same
Brownian filtration.

## Originality

**PASS, to the best of our knowledge.**

The closest source is Qin, arXiv:2609.17264v1, submitted 15 September 2026.
Its Theorem 1.1 gives only
\(\Theta(L^2/\sqrt{\log L})\) for the critical mean cover time, and its
Question 1 explicitly asks whether the normalized mean converges to a positive
finite constant. The paper states that an a.e. limit of the rescaled
\(L^2\)-time tail would settle the question. The present theorem supplies exactly
that tail limit and an explicit Brownian path-integral representation.

Qin's Proposition 3.1 similarly gives only order bounds for the critical
symmetric-interval exit-time mean. The present argument yields its exact
first-order constant as well.

André and Zuaznábar, arXiv:2602.18953, prove exact expected escape-time asymptotics
in the diffusive regime and tail estimates, but their exact-mean statement stops
before criticality. Fang's 2024 paper studies critical return times and provides
embedding estimates used in later ERW work. The 2017 strong invariance principle
establishes Brownian approximation for the critical walk but does not identify
these \(L^2\)-scale rare-event profiles.

Searches using `critical elephant random walk`, `cover time`, `mean cover time at
criticality`, `exact exit time`, `Brownian bridge`, `exponential boundary`,
`damped Brownian`, and the source arXiv identifier did not locate a prior theorem
equivalent to the displayed profile or mean constants. The current public arXiv
record for 2609.17264 remains version 1 and still contains Question 1.

Residual originality risk remains because general Brownian boundary-crossing or
rare-bridge theory may contain an abstract theorem implying the Brownian lemma
under different terminology. Such a theorem would not by itself identify the
critical elephant cover-time profile; nevertheless, originality is claimed only
to the best of our knowledge, not as exhaustive literature certainty.

No inaccessible source was identified whose title or abstract specifically
indicates a solution of Qin's critical cover-time question.

## Value

**PASS.**

The result resolves an explicit recent open question and strengthens the associated
critical exit-time estimate from order notation to exact first-order asymptotics.
It also explains why the ordinary critical functional limit does not control the
mean: the expectation is generated by rare \(L^2\)-scale paths whose reversed
Brownian shape has an endpoint-mixture limit.

The profile formulas are reusable. They separate the universal Brownian rare-path
object from the ERW-specific clock transfer and provide a concrete target for
future analytic or certified numerical evaluation of the constants.

## Sources inspected

- Shuo Qin, *Cover times and ranges of elephant random walks*, arXiv:2609.17264v1, including Theorem 1.1, Proposition 1.2, Proposition 3.1, Proposition 3.5, Corollary 3.6, Lemmas 3.9-3.10, and Question 1.
- Morgan André and Leonel Zuaznábar, *Estimates on Escape Times for the Elephant Random Walk*, arXiv:2602.18953.
- Zheng Fang, *How often does a critical elephant random walk return to origin*, Electronic Communications in Probability 29 (2024).
- Cristian F. Coletti, Renato Gava and Gunter M. Schütz, *A strong invariance principle for the elephant random walk*, arXiv:1707.06905.
- Searches for equivalent critical cover/exit and Brownian rare-path formulations.

## Scientific limitations retained

The result is specific to the one-dimensional critical parameter. The Brownian
integrals are not evaluated in closed form, continuity is asserted only at the
points needed for the a.e. tail limit, and no quantitative convergence rate or
second-order asymptotic is proved.
