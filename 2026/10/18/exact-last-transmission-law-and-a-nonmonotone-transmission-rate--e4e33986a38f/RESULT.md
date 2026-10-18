# Exact last-transmission law and a nonmonotone transmission-rate optimum in a spatial rumor

## Finding

For the continuous-time classical Maki–Thompson rumor process on the infinite nearest-neighbor line with transmission rate \(\lambda>0\) and unit stifling intensity, start with one spreader at the origin and every other site ignorant. Define \(T_{\mathrm{new}}\) as the time of the *last transition from ignorant to spreader*, not the time at which the last spreader becomes a stifler. Then \(T_{\mathrm{new}}<\infty\) almost surely. Put \(a=\lambda/(1+\lambda)\). There is an exact representation

\[
T_{\mathrm{new}}\ \overset{d}{=}\ E_{2\lambda}+\max\{Z_1,Z_2\},
\]

where \(E_{2\lambda}\) has exponential rate \(2\lambda\), is independent of \(Z_1,Z_2\), and \(Z_1,Z_2\) are independent with

\[
\Pr(Z_i\le t)=1-ae^{-t}\quad(t\ge0),\qquad
\Pr(Z_i=0)=1-a.
\]

In particular, for every \(t\ge0\),

\[
\Pr(T_{\mathrm{new}}\le t)
=\int_0^t2\lambda e^{-2\lambda s}\bigl(1-a e^{-(t-s)}\bigr)^2\,ds,
\]

and for every \(s\ge0\),

\[
\mathbb E e^{-sT_{\mathrm{new}}}
=\frac{2\lambda}{2\lambda+s}
\left((1-a)^2+\frac{2a}{s+1}-\frac{2a^2}{s+2}\right).
\]

The expected time of the last new transmission is

\[
\mathbb E T_{\mathrm{new}}
=\frac{1}{2\lambda}+2a-\frac{a^2}{2}
=\frac{3\lambda^3+5\lambda^2+2\lambda+1}{2\lambda(1+\lambda)^2}.
\]

**A nonmonotone rate effect:** this expectation has a unique global minimum for \(\lambda>0\), attained at the unique positive root of
\[
\lambda^3+\lambda^2-3\lambda-1=0,
\]
namely \(\lambda_*=1.481194304092\ldots\), with minimum \(1.353316436162\ldots\). The mean diverges as \(\lambda\downarrow0\), but approaches \(3/2\) *from below* as \(\lambda\to\infty\). Therefore transmission rates above \(\lambda_*\) increase the expected time of the last newly informed site, despite generating more transmissions.

## Assumptions and scope

Each site has state \(0\) (ignorant), \(1\) (spreader), or \(2\) (permanent stifler). An ignorant site changes to state \(1\) at rate \(\lambda\) times its number of neighboring spreaders. A spreader changes to state \(2\) at rate equal to the number of its neighboring sites in states \(1\) or \(2\). Stiflers never change state. The underlying graph is \(\mathbb Z\), with nearest-neighbor edges and one initial spreader at \(0\). All stated rates are rates per neighbor in physical continuous time, and \(\lambda\in(0,\infty)\). This is the MT-zero (no-forgetting) dynamics in the cited source, with its stifling time scale set to one. Time zero is the initial configuration; the initial spreader itself is not counted as a newly informed site.

## Proof

**Step 1 (initial branching).** Initially the origin has two ignorant neighbors and no informed neighbors. Its first successful transmission occurs after an exponential waiting time \(\tau\sim\operatorname{Exp}(2\lambda)\). No stifling is possible before \(\tau\). Symmetry chooses the first direction; the exponential waiting time and the direction are independent. The rest of the graphical construction uses independent fresh Poisson marks and is independent of \(\tau\).

**Step 2 (one advancing front).** Immediately after the first transmission, the newly infected neighbor is the tip of an active front: it has one permanently informed neighbor behind and one ignorant neighbor ahead. At that tip forward successful transmissions occur at rate \(\lambda\) and stifling occurs at rate \(1\). Whenever forward transmission succeeds the next site becomes the new tip with the same two competing rates. An older spreader may stifle later, but it cannot infect a vertex ahead of the new tip and hence does not affect new transmissions. Thus the successive front transmissions can be coupled to a rate-\(\lambda\) Poisson process killed at an independent \(\operatorname{Exp}(1)\) time. The number of transmissions is geometric and finite almost surely.

Let \(X\) be the elapsed time from the front's creation to its last *subsequent* successful transmission, putting \(X=0\) if it makes none. If the exponential killing time is \(D\), then, for \(u\ge0\),

\[
\begin{aligned}
\Pr(X\le u)
&=\Pr(D\le u)+\mathbb E[\mathbf1_{\{D>u\}}e^{-\lambda(D-u)}]\\
&=1-e^{-u}+\frac{e^{-u}}{1+\lambda}=1-ae^{-u}.
\end{aligned}
\]

Write \(X_R\) for the first front's \(X\).

**Step 3 (the delayed opposite front).** After the first transmission, the origin has one informed neighbor, and can either stifle at rate \(1\) or inform its still-ignorant opposite neighbor at rate \(\lambda\). Let \(L\sim\operatorname{Exp}(\lambda)\) and \(D_0\sim\operatorname{Exp}(1)\) be independent clocks. If \(L\ge D_0\), no opposite-side transmission occurs; set its last-transmission offset \(Y=0\). If \(L<D_0\), the new opposite tip starts at time \(L\) and has an independent copy \(X'\) of \(X\), so \(Y=L+X'\). For \(u\ge0\),

\[
\begin{aligned}
\Pr(Y\le u)
&=\frac{1}{1+\lambda}
+\int_0^u\lambda e^{-(1+\lambda)v}
\bigl(1-ae^{-(u-v)}\bigr)\,dv\\
&=1-ae^{-(1+\lambda)u}
-ae^{-u}\bigl(1-e^{-\lambda u}\bigr)\\
&=1-ae^{-u}.
\end{aligned}
\]

The Poisson marks driving the first advancing front and those driving the origin/opposite front occur on disjoint directed space-time edges; by the graphical construction and strong Markov property, \(X_R\) and \(Y\) are independent and independent of \(\tau\). The last new infection occurs at \(\tau+\max\{X_R,Y\}\); in particular every side performs finitely many transmissions almost surely. This proves the distributional representation and the stated convolution CDF.

**Step 4 (transform and expectation).** With \(H=\max(X_R,Y)\), its CDF is \((1-ae^{-u})^2\) for \(u\ge0\). It has an atom \((1-a)^2\) at zero and density \(2ae^{-u}-2a^2e^{-2u}\) for \(u>0\). Integration gives

\[
\mathbb E e^{-sH}=(1-a)^2+\frac{2a}{s+1}-\frac{2a^2}{s+2},
\qquad
\mathbb EH=\int_0^\infty(2ae^{-u}-a^2e^{-2u})\,du=2a-\frac{a^2}{2}.
\]

Independence of \(\tau\) yields the Laplace transform and expected time in the finding.

**Step 5 (unique rate optimum).** Direct differentiation gives

\[
\frac{d}{d\lambda}\mathbb ET_{\mathrm{new}}
=\frac{\lambda^3+\lambda^2-3\lambda-1}{2\lambda^2(1+\lambda)^3}.
\]

The cubic has precisely one positive root by Descartes' rule of signs; it is negative at zero and positive at two. The derivative is therefore negative before its root and positive afterwards. The mean diverges as \(\lambda\downarrow0\) and tends to \(3/2\) from below as \(\lambda\to\infty\), establishing the unique global minimizer and stated contrast.

## Verification

Run `python verify.py` using Python 3. The included standalone program reconstructs the sitewise continuous-time Markov chain independently from its local transition rates, simulates 11,000 paths at each of four positive rates, and checks sample means and CDFs against the exact formulas with conservative explicit stochastic tolerances and a fixed seed. It also checks rational moment/normalization identities and brackets the unique positive cubic root. On execution, all tests passed. The proof does not depend on simulation; these checks can detect simple rate, normalization, and timing errors but cannot establish the infinite-state theorem or its originality.

## Relationship to prior work

Marić, Minić and Rodriguez (2026) define the exact infinite-line MT-zero model, prove almost-sure extinction and calculate the expected final number of informed vertices, \(2(1+\lambda)\), via independent geometric directional ranges (Theorem 1). Their displayed theorem and proof concern spatial reach, not the physical time of the *last successful transmission*, its Laplace transform or its nonmonotone dependence on the transmission rate. The present result uses the same model and its frontier geometry but adds a temporal graphical decomposition: geometric range alone does not determine the holding times.

Díaz Bacca, Rodriguez and Rúa-Alvarez (2025/2026, first posted July 2025) study rumor size and the transition count on finite ring lattices, with a cycle limit. Their Section 2.2 establishes a final-size statement; their reported “duration” in Section 3.2 is the count of transitions of a discrete skeleton, not elapsed continuous time to the final new transmission. The 2017 small-world-network analysis concerns final population reach in a different network. Mocquard, Sericola and Anceaume (2019) study complete-network dissemination times with a different stopping objective. Standard competing-exponential and Poisson-killing identities are not claimed as new: the claim is their exact assembly for the two spatial rumor fronts and the resulting nonmonotone physical-time optimum.

## Limitations

This result concerns final **new infection**, not total absorption/extinction time, and applies only to the one-dimensional nearest-neighbor no-forgetting MT process with unit stifling per informed neighbor. It does not cover ring wrap-around at finite size, long-range edges, forgetting, nonconstant rates, multiple initially informed sites, or asymptotics of the number of spreaders. Claims of novelty are a best-knowledge comparison with inspected sources; a more general earlier temporal decomposition may exist. Independent priority review has not been performed.

## References

1. Nevena Marić, Aleksandar Minić, and Pablo M. Rodriguez, *Critical behavior of stochastic rumors on the one-dimensional integer lattice* (2026), arXiv:2610.02533v1, first posted 2026-10-01, especially §2.1 and Theorem 1. https://arxiv.org/html/2610.02533v1
2. Ana C. Díaz Bacca, Pablo M. Rodriguez, and Catalina M. Rúa-Alvarez, *How far can a rumor travel without shortcuts?* (2025/2026), arXiv:2507.02141v2, first posted July 2025, especially §2.2–3.2. https://arxiv.org/html/2507.02141v2
3. Elena Agliari, Angelica Pachon, Pablo M. Rodriguez, and Flavia Tavani, *Phase Transition for the Maki–Thompson Rumour Model on a Small-World Network*, Journal of Statistical Physics 169 (2017), 846–875, DOI:10.1007/s10955-017-1892-x.
4. Yves Mocquard, Bruno Sericola, and Emmanuelle Anceaume, *Probabilistic Analysis of Rumor-Spreading Time*, INFORMS Journal on Computing 32 (2020), 172–181, DOI:10.1287/ijoc.2018.0845.
