# An exact critical-relaxation gap between discrete epidemic models with and without same-step reinfection

## Finding
For every finite connected, undirected, simple network with at least two vertices, the discrete-time susceptibility–infection–susceptibility (SIS) independence closures with and without same-step reinfection have the same epidemic threshold, yet they have different universal critical relaxation amplitudes. At that threshold, every nonzero trajectory in the probability cube converges to extinction and approaches a strictly positive multiple of the graph's Perron eigenvector at the exact order \(1/t\). The version permitting same-step reinfection has a strictly larger leading prevalence at every vertex, independent of initial condition.

Precisely, let \(A\) be the adjacency matrix, \(\rho>0\) its Perron root, and \(Av=\rho v\) with \(v_i>0\). Define \(w=v/(v^{\mathsf T}v)\), so \(w^{\mathsf T}v=1\). Fix \(0<\delta<1\) and the critical per-edge infection probability \(\beta=\delta/\rho\). Set
\[
S=\sum_i w_i v_i^2,\qquad
T=\beta^2\sum_i w_i\!\sum_{\{j,k\}\subset N(i)}v_jv_k,
\]
where the inner sum is over unordered pairs of distinct neighbors and is zero for degrees below two. Define
\[
\kappa_{\rm WIR}=\delta(1-\delta)S+T,\qquad
\kappa_{\rm WOR}=\delta S+T.
\]
Then for both models, for every initial vector in \([0,1]^n\setminus\{0\}\),
\[
\lim_{t\to\infty}t\,p_i^{\rm WIR}(t)=\frac{v_i}{\kappa_{\rm WIR}},\qquad
\lim_{t\to\infty}t\,p_i^{\rm WOR}(t)=\frac{v_i}{\kappa_{\rm WOR}}
\quad (i=1,\ldots,n).
\]
In particular, \(\kappa_{\rm WOR}-\kappa_{\rm WIR}=\delta^2S>0\); hence
\[
\lim_{t\to\infty}\frac{p_i^{\rm WIR}(t)}{p_i^{\rm WOR}(t)}
=\frac{\kappa_{\rm WOR}}{\kappa_{\rm WIR}}>1.
\]
The ratio concerns separately evolved, arbitrary nonzero initial states for the two models.

## Assumptions and scope
The graph is finite, simple, undirected and connected, with \(n\ge2\). At time \(t\), the coordinate \(p_i(t)\in[0,1]\) is an infection probability in an *independence-closure deterministic recurrence*, not a sample path of an exact finite stochastic SIS Markov chain. Define the infection-from-neighbors probability
\[
q_i(p)=1-\prod_{j\in N(i)}(1-\beta p_j).
\]
The two maps on \([0,1]^n\) are
\[
F_i(p)=(1-\delta)p_i+[1-(1-\delta)p_i]q_i(p)
\quad\text{(with same-step reinfection, WIR)},
\]
\[
H_i(p)=(1-\delta)p_i+(1-p_i)q_i(p)
\quad\text{(without same-step reinfection, WOR)}.
\]
They have identical derivative at the zero state, \(B=(1-\delta)I+\beta A\), whose largest eigenvalue is exactly one at \(\beta=\delta/\rho\). For different choices of the positive Perron-vector normalization, both \(v_i/\kappa\) quantities are unchanged. Neither \(\delta=0\) nor \(\delta=1\) is covered by the universal relaxation theorem.

## Proof
**1. Invariance, spectral geometry, and extinction.** Since \(0\le q_i(p)\le1\), both maps preserve the probability cube. The inequality \(q_i(p)\le\beta(Ap)_i\) gives the coordinate bounds \(F(p)\le Bp\) and \(H(p)\le Bp\). By connectedness, \(A\) has a simple positive Perron eigenvector \(v\); all other eigenvalues \(\lambda\) of \(B\) satisfy
\[
|1-\delta+\beta\lambda|<1.
\]
Indeed, \(-\rho\le\lambda<\rho\) and \(0<\delta<1\), including the bipartite lower endpoint \(1-2\delta>-1\).

The weighted mass \(a(p)=w^{\mathsf T}p\) is nonincreasing under both recurrences, since \(w^{\mathsf T}B=w^{\mathsf T}\). A strictly positive coordinate persists for one step because \(1-\delta>0\). Its neighbors become strictly positive at the next step because \(\beta>0\). Thus, for any nonzero \(p\), within one update an edge has both endpoint probabilities strictly positive. For each such edge, \(p_i q_i(p)>0\) at one of its endpoints. Consequently at the next update the weighted mass decreases strictly: this follows from the exact nonnegative losses
\[
(Bp-F(p))_i=\beta(Ap)_i-q_i(p)+(1-\delta)p_iq_i(p),
\]
\[
(Bp-H(p))_i=\beta(Ap)_i-q_i(p)+p_iq_i(p).
\]
Hence \(a(F^2(p))<a(p)\) and \(a(H^2(p))<a(p)\) for every nonzero \(p\). The mass along either trajectory has a limit \(L\ge0\). If \(L>0\), compactness supplies a nonzero accumulation point, and continuity of the strict two-step decrease contradicts convergence of masses to \(L\). Therefore \(L=0\), and positivity of \(w\) implies \(p(t)\to0\) for every nonzero initial vector.

**2. Exact quadratic loss.** Uniformly as \(p\to0\), finite-product expansion gives
\[
q_i(p)=\beta(Ap)_i-\beta^2\!\sum_{\{j,k\}\subset N(i)}p_jp_k+O(\|p\|^3).
\]
Hence for either map \(M\in\{F,H\}\),
\[
M(p)=Bp-Q_M(p)+O(\|p\|^3),
\]
where the homogeneous quadratic form is
\[
(Q_F(p))_i=(1-\delta)\beta p_i(Ap)_i+\beta^2\!\sum_{\{j,k\}\subset N(i)}p_jp_k,
\]
\[
(Q_H(p))_i=\beta p_i(Ap)_i+\beta^2\!\sum_{\{j,k\}\subset N(i)}p_jp_k.
\]
Because \(\beta\rho=\delta\), the Perron projections of these quadratic forms at \(v\) are precisely
\[
w^{\mathsf T}Q_F(v)=\kappa_{\rm WIR}>0,
\qquad w^{\mathsf T}Q_H(v)=\kappa_{\rm WOR}>0.
\]

**3. Directional alignment and the rate.** For either trajectory write \(a_t=w^{\mathsf T}p(t)>0\) and \(p(t)=a_t v+r_t\), with \(w^{\mathsf T}r_t=0\). Positivity gives \(\|p(t)\|\le C a_t\). Since the maps are \(Bp+O(\|p\|^2)\),
\[
a_{t+1}=a_t+O(a_t^2),\qquad a_t/a_{t+1}\to1.
\]
Let \(P=vw^{\mathsf T}\). The non-Perron component obeys
\[
r_{t+1}=Br_t+(I-P)O(a_t^2).
\]
On \(w^\perp\) the symmetric matrix \(B\) has norm \(\theta<1\). Defining \(u_t=r_t/a_t\) yields, for all sufficiently large \(t\),
\[
\|u_{t+1}\|\le\theta'\|u_t\|+Ca_t,
\quad\theta<\theta'<1.
\]
Because \(a_t\to0\), this contraction inequality forces \(u_t\to0\). Thus \(p(t)/a_t\to v\). Substitution into the quadratic expansion yields
\[
a_{t+1}=a_t-\kappa_M a_t^2+o(a_t^2).
\]
Therefore \(a_{t+1}^{-1}-a_t^{-1}\to\kappa_M\), and Cesàro summation gives \(a_t^{-1}/t\to\kappa_M\). Consequently \(t a_t\to1/\kappa_M\), proving both vector limits and their ratio. The amplitude gap simplifies exactly to \(\delta^2S\).

**4. Regular graphs and the excluded endpoint.** On a \(d\)-regular connected graph choose \(v=\mathbf1\), \(w=\mathbf1/n\); direct counting yields
\[
\kappa_{\rm WIR}=\delta-\frac{d+1}{2d}\delta^2,
\qquad \kappa_{\rm WOR}=\delta+\frac{d-1}{2d}\delta^2.
\]
For the two-vertex graph, these specialize to \(\delta(1-\delta)\) and \(\delta\), and the limiting WIR/WOR prevalence ratio is \(1/(1-\delta)\), diverging as \(\delta\uparrow1\). At the excluded endpoint \(\delta=\beta=1\), WIR swaps the two infection probabilities forever, whereas WOR on the nonzero symmetric orbit \(p_1=p_2=u\) follows \(u_{t+1}=u_t(1-u_t)\) and has \(t u_t\to1\). Hence the restriction \(\delta<1\) is essential.

## Verification
The accompanying `verify.py` uses only Python's standard library. It reimplements both maps from their product definitions, calculates the quadratic Perron coefficients independently for a two-vertex edge, a triangle, and a three-vertex path, and checks the predicted critical amplitudes after one hundred thousand steps from nonsymmetric, strictly positive initial vectors. All six relative errors are below \(0.00019\). It also checks the regular-graph simplification algebraically and the two-vertex exceptional endpoint. These are supplementary finite checks, not proofs of infinite-time assertions. The proof above independently establishes all asymptotic and global claims.

## Relationship to prior work
Dung and Phuc (2026) study exactly the WIR recurrence and introduce a community-level epidemic threshold set. Their publicly accessible complete preprint establishes threshold comparisons, but does not give the equality-case global asymptotic rate. Granell, Gómez, Gómez-Gardeñes, and Arenas (2024), Section 4.1, explicitly distinguish WIR and WOR, compare steady states, and show that their linear epidemic thresholds coincide. This establishes that the model distinction and its threshold equality are **prior knowledge**. The present theorem instead establishes the exact *critical-time* Perron amplitudes, their quantitative difference for every connected graph, and a singular boundary at the two-vertex endpoint. Chakrabarti and colleagues (2008) give the earlier WIR recurrence and spectral threshold. Arenas, Garijo, Gómez, and Villadelprat (2023) already explicitly calculate the WIR second derivative at threshold to establish a transcritical bifurcation; that curvature and bifurcation are not claimed as new, and their Theorem A states only strict sub- and supercritical global conclusions, not equality-case decay amplitudes or a WIR/WOR comparison. Prasse and Van Mieghem (2020) analyze near-threshold *continuous-time* NIMFA, not the two discrete-time closures together. Standard Perron–Frobenius and one-dimensional parabolic iteration principles underlie the proof.

## Limitations
The statement is for deterministic network independence closures, not for exact finite-state stochastic SIS extinction times or correlated infections. Connectedness, undirectedness, simplicity, uniform probabilities, and \(0<\delta<1\) are essential to the stated general theorem; extensions to directed, disconnected, weighted, or time-varying graphs require separate analysis. The result is first-order in inverse time; it does not identify logarithmic corrections. Historical priority of the exact amplitude comparison is not independently certified. In particular, Wang, Wang, and Shen (2019) on discrete-time SIS global stability was located but its full text could not be inspected; its exact relation to this calculation remains a residual literature risk.

## References
1. H. P. Dung and N. H. Phuc, *An Epidemic Threshold Set for Networks*, arXiv:2607.14048 (first public version 15 July 2026), https://arxiv.org/abs/2607.14048 .
2. C. Granell, S. Gómez, J. Gómez-Gardeñes and A. Arenas, *Probabilistic Discrete-Time Models for Spreading Processes in Complex Networks: A Review*, Annalen der Physik 536 (2024), 2400078, https://doi.org/10.1002/andp.202400078 .
3. D. Chakrabarti et al., *Epidemic Thresholds in Real Networks*, ACM Transactions on Information and System Security 10 (2008), https://doi.org/10.1145/1284680.1284681 .
4. B. Prasse and P. Van Mieghem, *Time-dependent solution of the NIMFA equations around the epidemic threshold*, Journal of Mathematical Biology (2020), https://doi.org/10.1007/s00285-020-01542-6 .
5. A. Arenas, A. Garijo, S. Gómez and J. Villadelprat, *Bifurcation analysis of the Microscopic Markov Chain Approach to contact-based epidemic spreading in networks*, Chaos, Solitons & Fractals 166 (2023), 112921, https://doi.org/10.1016/j.chaos.2022.112921 .
6. X. Wang, Z. Wang and H. Shen, *Dynamical analysis of a discrete-time SIS epidemic model on complex networks*, Applied Mathematics Letters 94 (2019), 292–299, https://doi.org/10.1016/j.aml.2019.03.011 (full text not inspected).
