# Exact star fixation and opposing selection regimes in context-dependent opinion adoption

## Finding

**Theorem.** Let \(m\ge2\) be any integer and let \(G=K_{1,m}\) be a loopless undirected star with a center and \(m\) leaves. The agents carry colors \(0\) and \(1\). At each discrete time one agent is selected uniformly, samples a neighbor uniformly, and adopts that neighbor's differing color with probability \(a\) for the move \(0\to1\), or \(b\) for the move \(1\to0\), where \(0<a,b\le1\). Put
\[
q=\frac ba,\qquad
R_m(q)=\frac{1+q/m}{1+1/(qm)},\qquad
Z_m(q)=1+\frac qm\sum_{j=0}^{m-1}R_m(q)^j.
\]
For \(c\in\{0,1\}\) and \(0\le k\le m\), the probability \(H_{c,k}\) of eventual all-\(1\) consensus, conditional on center color \(c\) and exactly \(k\) leaves colored \(1\), is
\[
H_{0,k}=\frac{\sum_{j=1}^{k}R_m(q)^j}{qmZ_m(q)},\qquad
H_{1,k}=\frac{1+(q/m)\sum_{j=0}^{k-1}R_m(q)^j}{Z_m(q)}.
\]
An empty sum is \(0\). If initially one uniformly selected agent carries color \(1\), the unconditional fixation probability is exactly
\[
\rho_{\mathrm{star},m}(q)=\frac{1+R_m(q)/q}{(m+1)Z_m(q)}.
\]
For each fixed \(q>0\), define \(F(t)=(e^t-1)/t\) for \(t\ne0\) and \(F(0)=1\). Then
\[
\lim_{m\to\infty}(m+1)\rho_{\mathrm{star},m}(q)
=C(q):=\frac{1+1/q}{1+qF(q-1/q)}>0.
\]
For a loopless complete graph with the same \(n=m+1\) agents and the same update rule, the uniformly seeded fixation probability is
\[
\rho_{\mathrm{clique},n}(q)=
\begin{cases}(1-q)/(1-q^n),&q\ne1,\\1/n,&q=1.\end{cases}
\]
Thus for fixed \(q<1\) an advantageous opinion fixes with probability tending to \(1-q\) on the clique but only \(C(q)/n+o(1/n)\) on the star. For fixed \(q>1\), a disadvantageous opinion fixes at order \(q^{-n}\) on the clique but at order \(1/n\) on the star. For \(q=1\), both probabilities equal \(1/n\). More precisely, in the weak-bias window \(q_n=1+\lambda/n>0\), for each fixed real \(\lambda\) and sufficiently large \(n\), the star has \(n\rho_{\mathrm{star},n-1}(q_n)\to1\), whereas the clique has \(n\rho_{\mathrm{clique},n}(q_n)\to\lambda/(e^\lambda-1)\), interpreted as \(1\) at \(\lambda=0\).

## Assumptions and scope

All vertices are activated with probability \(1/(m+1)\) in each independent discrete step. The center samples one of its \(m\) leaves uniformly and each leaf samples the center. Sampling a like-colored neighbor leaves the state unchanged. The acceptance probabilities are constant across vertices and strictly positive. Both unanimous configurations are absorbing, and the chain reaches one of them almost surely: from any nonunanimous state, a finite sequence of positive-probability updates makes every vertex agree with a chosen existing color. This is an asynchronous *pull* update, not a push or state-weighted neighbor-choice rule.

The large-star asymptotic assumes \(a\) and \(b\) fixed through \(q=b/a\), or more generally fixed \(q\); the weak-bias statement permits \(q_n\) to vary with \(n\). The result concerns a uniformly placed single opinion-\(1\) seed for comparisons with the complete graph, and determines fixation probabilities from arbitrary configurations on a star.

## Proof

**1. Lumped Markov chain.** Permuting the leaves leaves all transition probabilities invariant, so a state is summarized by center color \(c\) and the number \(k\) of opinion-\(1\) leaves. Consider \(0<k\le m\) with center color \(0\). Ignoring the common activation probability \(1/(m+1)\), there is rate \(bk\) of a leaf changing from \(1\) to \(0\), and rate \(ak/m\) of the center changing from \(0\) to \(1\). The harmonicity equation for the fixation probability is therefore
\[
b(H_{0,k}-H_{0,k-1})=\frac am(H_{1,k}-H_{0,k}).\tag{1}
\]
Similarly, for center color \(1\) and \(0\le k<m\), changes from \(0\) to \(1\) occur at leaf rate \(a(m-k)\), while the center changes from \(1\) to \(0\) at rate \(b(m-k)/m\). Therefore
\[
a(H_{1,k+1}-H_{1,k})=\frac bm(H_{1,k}-H_{0,k}).\tag{2}
\]
These hold with boundary data \(H_{0,0}=0\) and \(H_{1,m}=1\).

**2. Solve exactly.** Write \(d_k=H_{1,k}-H_{0,k}\). Equation (1) implies \(H_{0,k}-H_{0,k-1}=d_k/(qm)\) for \(1\le k\le m\). Equation (2) implies \(H_{1,k+1}-H_{1,k}=qd_k/m\) for \(0\le k<m\). Subtracting successive expressions gives
\[
\left(1+\frac{1}{qm}\right)d_{k+1}
=\left(1+\frac qm\right)d_k,
\qquad d_k=d_0R_m(q)^k.
\]
Starting from \(H_{0,0}=0\), summation yields \(H_{0,k}=d_0\sum_{j=1}^k R_m(q)^j/(qm)\). Likewise \(H_{1,k}=d_0[1+(q/m)\sum_{j=0}^{k-1}R_m(q)^j]\). Setting \(H_{1,m}=1\) forces \(d_0=1/Z_m(q)\), which proves the advertised two formulas. Because the absorbing chain is finite and absorption is almost sure, its harmonic solution with these two boundaries is uniquely the fixation probability.

**3. Initial location and fixed-bias asymptotics.** With one opinion-\(1\) seed, the center placement has probability \(H_{1,0}=1/Z_m(q)\), while each leaf placement has probability \(H_{0,1}=R_m(q)/(qmZ_m(q))\). Their uniform average gives the exact \(\rho_{\mathrm{star},m}\). With fixed \(q\), direct expansion gives \(m\log R_m(q)\to q-1/q\). Consequently
\[
\frac1m\sum_{j=0}^{m-1}R_m(q)^j\longrightarrow
\int_0^1 e^{(q-1/q)t}\,dt=F(q-1/q).
\]
The displayed value \(C(q)\) follows, strictly positive and finite for each positive \(q\).

**4. Clique and comparison.** On \(K_n\), given \(k\) opinion-\(1\) agents, the per-step birth and death probabilities are respectively \(ak(n-k)/(n(n-1))\) and \(bk(n-k)/(n(n-1))\). A birth-death harmonic recurrence with constant death-to-birth ratio \(q\) and boundaries \(0,1\) gives \((1-q^k)/(1-q^n)\) when \(q\ne1\) and \(k/n\) when \(q=1\). Use \(k=1\). When \(0<q<1\), the clique formula tends to \(1-q\). When \(q>1\), it equals \((q-1)/(q^n-1)\sim(q-1)q^{-n}\). By the star limit, both contrasting regimes follow. At \(q=1\), \(R_m=1\) and \(Z_m=2\), giving \(\rho_{\mathrm{star},m}=1/(m+1)\).

**5. Weak-bias window.** For \(q_n=1+\lambda/n\) and \(m=n-1\), we have \(m\log R_m(q_n)\to0\), so \(Z_m(q_n)\to2\) and \(1+R_m(q_n)/q_n\to2\). Hence \(n\rho_{\mathrm{star},n-1}(q_n)\to1\). The clique expression gives \(q_n^n\to e^\lambda\) and the stated limit when \(\lambda\ne0\); the unbiased case handles \(\lambda=0\). This completes the proof.

## Verification

The included standalone program `verify.py` uses exact fractions to evaluate the proposed harmonic function on every labeled configuration of stars with \(m=2,\ldots,8\) leaves for five distinct positive rational acceptance pairs. It checks the one-step mean-zero drift and both absorbing boundaries on every labeled configuration, as well as the hub/leaf single-seed identities and neutral limit. It reports \(35\) exact parameter/star cases, \(5080\) labeled configurations, and \(35840\) exact transition-drift terms. The all-size proof is algebraic and independent of this finite enumeration. Reproduction: `python verify.py` (Python standard library only).

## Relationship to prior work

Becchetti, Bonifaci, Cruciani, and Pasquale introduced precisely this context-dependent acceptance rule and derived biased fixation results on regular graphs (including cliques). Their analysis does not imply the displayed star equations, since unequal center/leaf degrees destroy the constant birth-to-death ratio; the general-topology case is explicitly identified as harder. The clique comparison uses their already-known regular-graph calculation and is not independently claimed as a discovery.

Kátai-Urbán, Pongrácz, and Szabó study discordant push/pull voting on stars, concentrating on consensus times; their activated-vertex sampling conditions and absence of color-dependent rejection differ from the present stochastic rule. Petsinis, Pavlogiannis, and Karras allow spatially biased voter updates but select a neighbor with probability weighted by its opinion's fitness, instead of sampling first and applying a fixed acceptance probability; those transition kernels are distinct on mixed-neighbor vertices. Durocher, Karras, Pavlogiannis, and Tkadlec likewise address fitness-weighted bias and seed optimization. A more directly related precedent is Sood, Antal, and Redner (2008), whose biased voter model samples a receiver with probability proportional to its inverse fitness. **Its embedded jump chain is equivalent to the present accept/reject process**, for inverse relative fitness \(q=b/a\): at any fixed configuration their probabilities of each actual color-changing transition differ only by the same positive state-dependent multiplier. This equivalence preserves fixation probabilities, though it changes holding times. Their paper gives a diffusion/degree-moment approximation in the weak-selection regime on heterogeneous networks, not the exact arbitrary-bias all-configuration star formula or its fixed-/weak-bias star-versus-clique limits. The present statement is therefore a precise exact solution for a specific heterogeneous graph family of a known more general biased-copying jump mechanism, not a novel general voter update rule. These related results do not directly give the complete star harmonic function or asymptotic comparison here. A comprehensive priority claim beyond the inspected sources is not made.

## Limitations

The result treats simple stars, a binary opinion set, uniform vertex activation, and asynchronous uniform-neighbor pull; it does not describe synchronous dynamics, arbitrary heterogeneous acceptance rates, general graph families, or consensus times. The fixed-bias limit is not uniform over arbitrary varying bias ratios, and the weak-bias statement only covers the specified \(1/n\) window. The fixation analysis proves no global graph extremality among all graphs. Broader uninspected opinion-dynamics literature could contain equivalent conclusions.

## References

1. L. Becchetti, V. Bonifaci, E. Cruciani, F. Pasquale, *On a Voter Model with Context-Dependent Opinion Adoption*, IJCAI 2023, pp. 38–45; arXiv:2305.07377 (first submitted 2023-05-12), DOI:10.24963/ijcai.2023/5. Full text: https://arxiv.org/html/2305.07377v2.
2. K. Kátai-Urbán, A. Pongrácz, C. Szabó, *Voting protocols on the star graph*, Acta Sci. Math. 90 (2024), pp. 41–51, DOI:10.1007/s44146-024-00125-x.
3. P. Petsinis, A. Pavlogiannis, P. Karras, *Maximizing the Probability of Fixation in the Positional Voter Model*, AAAI 2023, pp. 12269–12277, arXiv:2211.14676, DOI:10.1609/aaai.v37i10.26446.
4. L. Durocher, P. Karras, A. Pavlogiannis, J. Tkadlec, *Invasion Dynamics in the Biased Voter Process*, arXiv:2201.08207 (2022).
5. V. Sood, T. Antal, S. Redner, *Voter Models on Heterogeneous Networks*, Physical Review E 77, 041121 (2008), arXiv:0712.4288, DOI:10.1103/PhysRevE.77.041121, especially Section VI and Eq. (62).
