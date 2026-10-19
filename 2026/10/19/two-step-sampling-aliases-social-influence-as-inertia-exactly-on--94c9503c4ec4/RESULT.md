# Two-step sampling aliases social influence as inertia exactly on matching networks

## Finding

Consider a network of agents with binary opinions and strictly positive social influence. Sampling synchronous opinion updates only at even times can make real social influence **exactly observationally indistinguishable** from individual self-persistence. This happens on precisely the networks with no shared-neighbor structure: disjoint unions of edges. On every other graph, two-step observations retain a strict positive conditional correlation that forbids any explanation by independent pure-inertia updates.

**Theorem.** Let \(G=(V,E)\) be a finite, undirected, loopless simple graph, with \(|V|\ge2\), no isolated vertices, and positive symmetric edge weights \(w_{ij}=w_{ji}>0\). Fix a finite \(\beta>0\). For \(s\in\{-1,+1\}^{V}\), put
\[
 u_i(s)=\frac{\sum_{j\sim i}w_{ij}s_j}{\sum_{j\sim i}w_{ij}},
 \qquad \sigma(z)=\frac1{1+e^{-z}}.
\]
At each integer time, simultaneously and conditionally independently sample spins according to
\[
 \Pr\{S_i(t+1)=+1\mid S(t)=s\}=\sigma(\beta u_i(s)).
\]
Denote this one-step Markov kernel by \(K\).

The following conditions are equivalent:

1. For every starting spin configuration \(s\), the two-step output distribution \(K^2(s,\cdot)\) factors as a product across individual vertices.
2. The graph \(G\) is a disjoint union of edges.
3. The entire two-step kernel \(K^2\) is exactly the synchronous product kernel of a pure individual-inertia heat bath with no neighbor influence and field \(H_i=\lambda_{\rm eff}s_i\), where
\[
 \lambda_{\rm eff}=2\operatorname{artanh}\bigl(\tanh^2(\beta/2)\bigr)>0.
\]

In the matching case every spin survives a two-step interval independently with probability
\[
 \frac{1+\tanh^2(\beta/2)}2.
\]
On a nonmatching graph, for any vertex \(u\) with two different neighbors \(v,w\),
\[
 \operatorname{Cov}\bigl(S_v(t+2),S_w(t+2)\mid S(t)=s\bigr)>0
\]
for **every** configuration \(s\), so product factorization fails at every starting state. The two models in the matching case generate identical probability laws for every finite sequence of observations at times \(0,2,4,\ldots\), conditional on the same initial configuration.

## Assumptions and scope

The graph is fixed in time, finite, undirected, simple, and loopless. All weights are positive and finite, with no isolated vertices so that the normalized local field is well-defined. The coupling is a single finite number \(\beta>0\). An agent's new opinion does not depend directly on its own current opinion, and conditional update noise is independent across agents and time. The comparison inertia-only model updates each agent independently with \(\Pr(S_i'=+1\mid s)=\sigma(\lambda_{\rm eff}s_i)\). Its parameters do not depend on the graph's positive edge weights when the graph is a matching. Equivalence concerns **two-step transition kernels**, not one-step kernels or observed paths at every integer time.

## Proof

Put \(p_i(s)=\sigma(\beta u_i(s))\), and let \(Z=S(t+1)\) conditional on \(S(t)=s\). By the update rule, the coordinates of \(Z\) are independent, each has both possible values with strictly positive probability, and
\[
 f_i(z):=\mathbb E[S_i(t+2)\mid Z=z]
 =2p_i(z)-1=\tanh\!\left(\frac{\beta}{2}u_i(z)\right).
\]
The second-step outputs are independent conditional on \(Z\). Consequently, for distinct vertices \(v,w\), their conditional covariance given the original \(s\) is exactly
\[
 \operatorname{Cov}(f_v(Z),f_w(Z)\mid S(t)=s).
\]

**Matching sufficiency.** Suppose each vertex has exactly one neighbor, denoted \(j(i)\). Weight normalization then gives \(u_i(s)=s_{j(i)}\), regardless of weights. Let \(c=\tanh(\beta/2)\in(0,1)\). Conditional on an initial state, the first-step spins are independent with \(\mathbb E[Z_{j(i)}\mid s]=c s_i\). Distinct vertices have distinct partners \(j(i)\), so their second-step outputs depend on disjoint independent intermediate variables and independent second-step noise. They therefore are jointly independent, and their means are
\[
 \mathbb E[S_i(t+2)\mid s]=c\mathbb E[Z_{j(i)}\mid s]=c^2s_i.
\]
Their exact conditional laws are thus \(\Pr(S_i(t+2)=+1\mid s)=(1+c^2s_i)/2=\sigma(2\operatorname{artanh}(c^2)s_i)\). This is the asserted inertia-only heat bath. Equality of the two-step Markov kernels implies equality of all finite even-sampled path laws by multiplying transition probabilities, for every common initial distribution.

**Nonmatching necessity.** If the graph is not a matching, some vertex \(u\) has distinct neighbors \(v,w\). Each \(f_v\) and \(f_w\) is coordinatewise nondecreasing on the independent intermediate spins \(Z\), and is **strictly increasing in \(Z_u\)**, since \(w_{vu},w_{wu},\beta\) are positive and \(\tanh\) is strictly increasing. For independent Bernoulli coordinates, coordinatewise increasing functions have nonnegative covariance; this follows by induction from the law of total covariance: conditioning on one Bernoulli coordinate, the conditional covariance is nonnegative by induction, and the covariance of the two conditional means is nonnegative because both conditional means increase with that coordinate.

Apply the law of total covariance conditional on \(Z_u\). The first term is nonnegative by the same independent-product association inequality. For the second term, the conditional means
\[
 g_v(a)=\mathbb E[f_v(Z)\mid Z_u=a,S(t)=s],\quad
 g_w(a)=\mathbb E[f_w(Z)\mid Z_u=a,S(t)=s]
\]
are both strictly increasing from \(a=-1\) to \(a=+1\). Their covariance is exactly
\[
 p_u(s)(1-p_u(s))\,[g_v(+1)-g_v(-1)]\,[g_w(+1)-g_w(-1)]>0.
\]
Thus the total conditional covariance is strictly positive for every starting state \(s\), contradicting any product output law. In particular, the two-step kernel cannot equal an independent inertia-only kernel. This proves all implications.

**Exact three-agent witness.** For the path on three vertices with its middle vertex attached to both leaves and unit edge weights, write \(c=\tanh(\beta/2)\). The two leaves at time \(t+2\) both receive their information from the middle vertex at time \(t+1\). Hence their conditional covariance equals
\[
 c^2\Bigl[1-\tanh^2\!\left(\frac{\beta}{4}(s_\mathrm{left}+s_\mathrm{right})\right)\Bigr]>0.
\]
This is an explicit finite-size witness to the sharp graph boundary. For \(\beta=\log9\), the covariance equals \(16/25\) when the starting leaves disagree and \(144/625\) when they agree.

## Verification

The standalone standard-library script `verify.py` evaluates exact transition probabilities using `fractions.Fraction` at \(\beta=\log9\), for which the tested degrees one and two give rational heat-bath probabilities. It constructs the full one-step kernel, multiplies it to obtain the complete two-step kernel, checks **all 272 conditional two-step entries** for a single edge and for a disjoint union of two edges against the inertia-only product formula, and computes covariance for every initial state on a three-vertex path and a four-vertex cycle. It checks strict positivity in all 24 nonmatching starting configurations and the explicit three-agent rational formulas. Run `python verify.py` with Python 3.10 or later; no external packages or data files are needed.

## Relationship to prior work

Achitouv, Chavalarias and Lahoche (2026) introduced empirical simultaneous heat-bath social-influence and persistence models, with the memoryless model M1 and self-persistence model M3 defined in their Section III. The present theorem concerns temporal coarsening of exactly those two microscopic mechanisms for fixed, undirected network data; it is not a rederivation of the empirical estimates.

Nareddy and Machta (2019), especially their Section II parallel update equation and Section IV.1, studied stationary parallel kinetic Ising models with self-interaction on square lattices. Their zero-self-interaction stationary sublattice factorization is established prior knowledge. That fact concerns stationary ensembles and does not itself give the all-initial-state two-step kernel equality with independent inertia, or characterize precisely the graph class for which it holds. Cirillo and collaborators (2014) studied reversible probabilistic cellular automata and their stationary phases; we do not claim a new general theory of parallel updates or reversibility. The basic positive association inequality is standard, while its application to the **if-and-only-if two-step aliasing boundary** is the claimed addition.

## Limitations

The theorem does not say the underlying one-step models are identical. One-step observations of labeled agents separate pure neighbor copying from pure self-persistence, and observing only stationary histograms is not the same as observing two-step transition kernels. Nonmatching graphs can be distinguished from *independent* pure-inertia kernels by nonzero conditional covariance; equivalence with a more general correlated-noise, latent-variable or interaction-plus-inertia model is not ruled out. A time-varying graph, asynchronous updates, arbitrary external fields, zero or signed edges, self-loops, noise dependence across agents, or infinite zero-temperature coupling are outside the theorem. The literature-priority comparison remains subject to independent verification against the broader graphical-model and stochastic-process literature.

## References

1. I. Achitouv, D. Chavalarias and V. Lahoche, *Inferring the microscopic mechanisms of opinion dynamics using a kinetic Ising model*, arXiv:2609.23690v1 (2026-09-20), https://arxiv.org/abs/2609.23690 . Section III, models M1 and M3, and Section IV.
2. V. R. Nareddy and J. Machta, *Kinetic Ising Models with Self-interaction: Sequential and Parallel Updating*, arXiv:1911.03289v1 (2019), https://arxiv.org/abs/1911.03289 . Sections II and IV.1.
3. E. N. M. Cirillo, P.-Y. Louis, W. M. Ruszel and C. Spitoni, *Effect of self-interaction on the phase diagram of a Gibbs-like measure derived by a reversible Probabilistic Cellular Automata*, arXiv:1307.8234 (2013), https://arxiv.org/abs/1307.8234 .
