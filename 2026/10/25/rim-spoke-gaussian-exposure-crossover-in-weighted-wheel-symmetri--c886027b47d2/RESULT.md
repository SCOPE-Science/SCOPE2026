# Rim–spoke Gaussian exposure crossover in weighted wheel symmetric edge polytopes

## Finding

Let \(m\ge4\) and let \(H_m=\{x\in\mathbb R^{m+1}:\sum_{i=0}^{m}x_i=0\}\) with its inherited Euclidean metric. Define the weighted wheel symmetric edge polytope
\[
P_m(a)=\operatorname{conv}\Big(\{\pm(e_i-e_{i+1}):1\le i\le m\}\cup\{\pm a(e_0-e_i):1\le i\le m\}\Big),\qquad a>0,
\]
where \(e_{m+1}=e_1\). The outer-cycle roots have weight one and all hub-to-rim roots have weight \(a\). Let \(U\) be uniform on the unit sphere of \(H_m\), and write \(W_{m,a}=\max_{x\in P_m(a)}\langle U,x\rangle-\min_{x\in P_m(a)}\langle U,x\rangle\). Set
\[
r_m=\sqrt{2\log m},\qquad
\eta_m=\sqrt2\,\frac{\Gamma((m+1)/2)}{\Gamma(m/2)}.
\]

**The rim–spoke exposure transition.** Fix any real \(c\), and put \(a_m=\sqrt2+c/r_m\), for all sufficiently large \(m\) for which \(a_m>0\). Then
\[
\boxed{\ \frac{\eta_m}{2}W_{m,a_m}-\sqrt2\,r_m\ \Longrightarrow\ (c+\sqrt2|Z|)_+,\qquad Z\sim N(0,1).\ }
\]
Here \(x_+=\max(0,x)\). Expectations converge after the same centering:
\[
\lim_{m\to\infty}\left(\frac{\eta_m}{2}\mathbb EW_{m,a_m}-\sqrt2r_m\right)
=\begin{cases}
2c\Phi(c/\sqrt2)+\frac2{\sqrt\pi}e^{-c^2/4},&c<0,\\
c+\frac2{\sqrt\pi},&c\ge0.
\end{cases}
\]
Almost surely there is a unique maximizer among the signed generating roots. The probability that it is a hub-to-rim (spoke) root has limit
\[
\boxed{\ \lim_{m\to\infty}\Pr(\text{spoke root exposed})
=\begin{cases}2\Phi(c/\sqrt2),&c<0,\\ 1,&c\ge0.\end{cases}\ }
\]
When \(c<0\), the displayed limiting width correction has a positive atom at zero, of mass \(1-2\Phi(c/\sqrt2)\).

**The regimes on either side.** Put
\[
b_N=\sqrt{2\log N}-\frac{\log\log N+\log(4\pi)}{2\sqrt{2\log N}},\qquad s_N=\frac1{\sqrt{2\log N}}.
\]
For every fixed \(0<a<\sqrt2\),
\[
\boxed{\ \frac{\eta_m W_{m,a}/2-\sqrt2 b_{2m}}{\sqrt2 s_{2m}}
\Longrightarrow\mathcal G,\qquad\Pr(\mathcal G\le x)=\exp(-e^{-x}).\ }
\]
For every fixed \(a>\sqrt2\),
\[
\boxed{\ \frac{\eta_m}{2}W_{m,a}-a r_m\Longrightarrow a|Z|.\ }
\]
For any fixed \(a>0\), \(\eta_m W_{m,a}/(2r_m)\to\max(\sqrt2,a)\) in probability. The ordinary (unweighted) wheel belongs to the first, Gumbel regime.

## Assumptions and scope

These are full-dimensional centrally symmetric polytopes in \(H_m\), not in all of \(\mathbb R^{m+1}\). The limit is taken along integer \(m\to\infty\) with one hub and a single outer cycle. Gaussian samples in the proof have \(m+1\) independent variance-one coordinates. The exposure probability refers to an actual unique supporting *vertex* (a signed generator), with ties having probability zero. The spoke weights are allowed to depend on \(m\) only as stated in the critical regime; the two off-critical statements take \(a\) fixed. The stated Gaussian-width normalizer is the exact mean Euclidean norm of an \(m\)-variate standard Gaussian, not \(\sqrt{m+1}\).

## Proof

**1. Gaussian support identity and radial normalization.** Let \(G_0,\ldots,G_m\) be independent \(N(0,1)\), cyclically setting \(G_{m+1}=G_1\). Put
\[
R_m=\max_{1\le i\le m}|G_i-G_{i+1}|,\qquad T_m=\max_{1\le i\le m}|G_i-G_0|.
\]
By evaluating every generating root, the Gaussian support is exactly
\[
H_{m,a}=h_{P_m(a)}(G)=\max\{R_m,aT_m\}.
\]
Projection of \(G\) onto \(H_m\) changes no edge pairing. Its length \(Q_m\) has the \(\chi_m\) law and is independent of its uniform intrinsic direction. Since \(P_m(a)\) is centrally symmetric, \(H_{m,a}=Q_m W_{m,a}/2\) under this coupling and \(\mathbb EH_{m,a}=\eta_m\mathbb EW_{m,a}/2\) exactly. For bounded positive weights, \(H_{m,a}=O_{\Pr}(r_m)\), while \(Q_m/\eta_m=1+O_{\Pr}(m^{-1/2})\). Therefore \(\eta_mW_{m,a}/2-H_{m,a}=O_{\Pr}(r_m/\sqrt m)=o_{\Pr}(1/r_m)\). All distributional claims below transfer to the sphere; the expectation is already an exact identity.

**2. Two competing extremal scales.** Gaussian maximum and minimum asymptotics give
\[
\max_{1\le i\le m}G_i=r_m+o_{\Pr}(1),\qquad\min_{1\le i\le m}G_i=-r_m+o_{\Pr}(1).
\]
It follows that \(T_m=r_m+|G_0|+o_{\Pr}(1)\). For the cycle edges, the Gaussian differences have marginal \(N(0,2)\). The union bound yields \(R_m\le\sqrt2r_m+o_{\Pr}(1)\) in the upper-tail sense. Using the disjoint edges \((1,2),(3,4),\ldots\), a collection of \(\lfloor m/2\rfloor\) independent \(N(0,2)\) variables, yields the matching lower-tail estimate. Hence
\[
R_m=\sqrt2r_m+o_{\Pr}(1).
\]
These conclusions also hold in \(L^1\) at this unscaled error level: their deviations are tight with uniformly integrable Gaussian-maximal tails (for \(T_m\), also use integrability of \(|G_0|\)).

**3. Critical crossover, mean and angular exposure.** Under \(a_m=\sqrt2+c/r_m\),
\[
a_mT_m-\sqrt2r_m=c+\sqrt2|G_0|+o_{\Pr}(1),\qquad R_m-\sqrt2r_m=o_{\Pr}(1).
\]
The maximum identity proves the limit \((c+\sqrt2|Z|)_+\). The \(L^1\) control from step 2 yields expectation convergence. Integrating the half-normal density gives the displayed two-branch expression. A spoke root is exposed if and only if \(a_mT_m>R_m\). Since \(\Pr(c+\sqrt2|Z|=0)=0\), the strict-comparison limit gives the asserted angular probability. At \(c=0\), the probability is one because \(|Z|>0\) almost surely.

**4. Fixed-weight rim Gumbel law.** Let \(Y_i=(G_i-G_{i+1})/\sqrt2\), indexed cyclically. The field is stationary and one-dependent off the cycle closure: two edge variables are independent unless they share a vertex; adjacent correlations equal \(-1/2\). At level \(u_m(x)=b_{2m}+s_{2m}x\),
\[
m\Pr(|Y_1|>u_m(x))\longrightarrow e^{-x}.
\]
For adjacent edges and any choices of signs, a Gaussian two-coordinate tail bound gives
\[
\Pr(|Y_i|>u,\ |Y_{i+1}|>u)\le4e^{-2u^2/3},
\]
**when \(u\) measures the standardized variables \(Y_i\)**: the worst signed correlation is \(1/2\), and the relevant normalized sum has variance three, yielding \(\Pr(Y_i>u,Y_{i+1}<-u)\le e^{-2u^2/3}\). As \(u_m(x)^2\sim2\log m\), the sum over all \(m\) neighbor pairs tends to zero. The Poisson approximation for rare events with a degree-two dependency graph now implies
\[
\Pr(R_m/\sqrt2\le u_m(x))\to\exp(-e^{-x}).
\]
For fixed \(a<\sqrt2\), step 2 gives \(\Pr(aT_m>R_m)\to0\), so the same Gumbel limit holds for \(H_{m,a}\). The spherical radial error in step 1 is \(o_{\Pr}(s_{2m})\).

**5. Fixed-weight spoke half-normal law.** For fixed \(a>\sqrt2\), the gap between \(aT_m\) and \(R_m\) is \((a-\sqrt2)r_m+O_{\Pr}(1)\to\infty\). Thus \(H_{m,a}=aT_m\) with probability tending to one. Step 2 gives \(H_{m,a}-ar_m\Rightarrow a|G_0|\). This completes the phase theorem.

## Verification

The accompanying `verify_wheel.py` checks the support identity by evaluating all signed generating roots directly for four dimensions, four positive spoke weights and 100 independent Gaussian directions per setting (1600 exact-formula comparisons with floating-point tolerance \(10^{-12}\)). It also simulates the spoke-exposure fraction at three finite sizes and three critical-window parameters. The latter exhibits notably slow convergence and is used only as a diagnostic; asymptotic assertions are established by the preceding proof. Run `python verify_wheel.py` with NumPy and SciPy. The output begins `VERIFY_OK support= 1600`.

## Relationship to prior work

D’Alì, Delucchi and Michałek establish the symmetric-edge-polytope construction, its graph/metric interpretation and explicit wheel-graph facet and volume data; none of these combinatorial enumerations implies the Gaussian directional-width competition in the statement. Kabluchko, Litvak and Zaporozhets establish mean-width and Gumbel limits for regular simplices, crosspolytopes and cubes. Their results explain the Gaussian-width method but do not specialize to the wheel's mixture of a one-dependent rim field and a hub-shared spoke field. The present family is a real-weight deformation of the standard wheel symmetric edge polytope, and the claim is the nontrivial transition in random exposed edge class and associated width law, not a new vertex/facet enumeration.

## Limitations

The results concern one homogeneous cycle and one uniformly weighted spoke class; they do not assert analogous laws for arbitrary irregular graphs, unequal rim weights, or general correlated Gaussian fields. The finite checker is not a proof of limiting distributions. At moderate sizes, convergence to the critical angular probabilities is slow. A semantically equivalent presentation elsewhere in Gaussian extreme-value literature remains possible. All scientific assessment in the accompanying review is non-independent.

## References

1. A. D’Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1, October 11, 2019. See Definition 2.1 and Section 4.3 on wheel graphs. https://arxiv.org/abs/1910.05193
2. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479v1, November 26, 2015; Journal of Mathematical Sciences 225 (2017), 770–787. See Sections 2–3. https://arxiv.org/abs/1511.08479
3. Classical Gaussian extreme-value and rare-event Poisson approximations are used only for the stated probabilistic limit arguments; their hypotheses for this one-dependent sequence are verified in step 4.
