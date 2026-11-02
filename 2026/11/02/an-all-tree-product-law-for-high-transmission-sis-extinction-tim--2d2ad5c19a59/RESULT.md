# An all-tree product law for high-transmission SIS extinction times

## Finding

Consider an exact, finite, absorbing susceptible–infected–susceptible (SIS) process, begun with infection at every vertex. As the common transmission-intensity parameter \(\lambda\) tends to infinity on a fixed connected bidirected network, its mean time to complete extinction has an explicit leading coefficient. For arbitrary positive heterogeneous recovery rates and directional transmission weights, this coefficient is a sum over inverse boundary cuts, and equivalently a finite-dimensional integral. **For every tree**, the integral factors into one contribution per edge, irrespective of the branching arrangement:

\[
\mathbb E_V[\tau_\varnothing]
=\frac{\lambda^{n-1}}{\prod_{v\in V}\mu_v}
 \prod_{\{u,v\}\in E}\frac{w_{uv}w_{vu}}{w_{uv}+w_{vu}}
 \bigl(1+O_G(\lambda^{-1})\bigr).
\]

Consequently, with unit recovery rates and unit transmission weights in both directions, **all trees with \(n\) vertices have the same leading mean extinction time**,

\[
\mathbb E_V[\tau_\varnothing]\sim(\lambda/2)^{n-1}.
\]

For a general connected bidirected graph, adding a genuinely new positive bidirectional contact strictly increases the leading mean extinction-time coefficient. These assertions concern fixed finite graphs in the high-transmission limit, not increasing network size at fixed transmission intensity.

## Assumptions and scope

Let \(G=(V,E)\) be a finite, simple, connected undirected graph with \(n=|V|\ge2\); its edges indicate the *presence* of two directed transmission arcs. Give each directed arc \(u\to v\) on \(\{u,v\}\in E\) a positive fixed transmission weight \(w_{uv}>0\), and give each vertex \(v\) a positive fixed recovery rate \(\mu_v>0\). The state \(S\subseteq V\) is the currently infected set. Each \(v\in S\) recovers at rate \(\mu_v\), and each \(v\notin S\) becomes infected at rate \(\lambda\sum_{u\in S:\{u,v\}\in E}w_{uv}\). The empty state is absorbing; initially \(S=V\). All rates are continuous-time exponential-clock rates. The network and all weights are held fixed as \(\lambda\to+\infty\).

For every nonempty proper subset \(S\subsetneq V\), define its outgoing infection cut

\[
c(S)=\sum_{u\in S}\sum_{v\in V\setminus S}w_{uv}>0,
\qquad M(S)=\sum_{v\in S}\mu_v.
\]

For any ordering \(\pi=(\pi_1,\ldots,\pi_n)\) of \(V\), put \(S_k(\pi)=\{\pi_1,\ldots,\pi_k\}\), and let

\[
C_G=\sum_{\pi\in\operatorname{Sym}(V)}
\prod_{k=1}^{n-1}\frac{1}{c(S_k(\pi))}.
\]

The leading general-graph formula is

\[
\mathbb E_V[\tau_\varnothing]
=\frac{\lambda^{n-1}}{\bigl(\prod_{v\in V}\mu_v\bigr) C_G}
\bigl(1+O_G(\lambda^{-1})\bigr).
\tag{1}
\]

Here \(O_G\) may depend on the fixed graph and all its fixed positive rates, and the asymptotics do not assert uniformity in graph size or in degenerating positive weights.

## Proof

**1. Rare extinction before a return to full occupancy.** For a nonempty proper \(S\), write

\[
h_\lambda(S)=\mathbb P_S(\tau_\varnothing<\tau_V),
\qquad h_\lambda(\varnothing)=1,\quad h_\lambda(V)=0.
\]

The first-step equations of the finite Markov chain are

\[
\bigl(M(S)+\lambda c(S)\bigr)h_\lambda(S)
=\sum_{v\in S}\mu_v h_\lambda(S\setminus\{v\})
+\lambda\sum_{v\notin S}
\left(\sum_{u\in S}w_{uv}\right)
 h_\lambda(S\cup\{v\}). \tag{2}
\]

The latter summand vanishes for \(S\cup\{v\}=V\). To bound the solution uniformly, take \(K>\max_{\varnothing\ne S\subsetneq V}M(S)/c(S)\) and \(\lambda>K\). For \(f(S)=(K/\lambda)^{|S|}\), the Markov generator satisfies, at every proper nonempty state,

\[
\frac{\mathcal L f(S)}{f(S)}
=(\lambda-K)\left(\frac{M(S)}K-c(S)\right)<0.
\]

At the hitting boundary \(\{\varnothing,V\}\), \(h_\lambda\le f\); optional stopping for the bounded finite-state chain therefore gives

\[
0\le h_\lambda(S)\le(K/\lambda)^{|S|}.
\tag{3}
\]

Induction on \(|S|\), using (2), (3), and \(c(S)>0\), yields for every proper nonempty \(S\)

\[
h_\lambda(S)=\lambda^{-|S|}\bigl(H(S)+O_G(\lambda^{-1})\bigr),
\qquad
H(\varnothing)=1,
\quad H(S)=\frac{\sum_{v\in S}\mu_v H(S\setminus\{v\})}{c(S)}.
\tag{4}
\]

Indeed, for a state with \(|S|=k\), the recovery terms in (2) are of order \(\lambda^{-(k-1)}\) with their stated leading terms, while all infection terms are at most \(O_G(\lambda^{-k})\). Division by \(M(S)+\lambda c(S)\) proves (4). This argument also includes \(k=n-1\).

Factoring out \(\prod_{v\in S}\mu_v\) from (4), define \(F(S)=H(S)/(\prod_{v\in S}\mu_v)\). It obeys

\[
F(\varnothing)=1,
\qquad F(S)=\frac{\sum_{v\in S}F(S\setminus\{v\})}{c(S)}.
\]

Unrolling the recursion across all deletion orderings shows

\[
\sum_{v\in V}\mu_v H(V\setminus\{v\})
=\Bigl(\prod_{v\in V}\mu_v\Bigr)C_G.
\tag{5}
\]

**2. Excursion renewal.** Write \(m=M(V)\). Upon leaving the fully infected state, a recovery of \(v\) occurs at rate \(\mu_v\). The probability that this excursion reaches extinction before returning to full occupancy is, by (4)–(5),

\[
p_\lambda=\frac1m\sum_{v\in V}\mu_v h_\lambda(V\setminus\{v\})
=\frac{\prod_v\mu_v}{m}C_G\lambda^{-(n-1)}
\bigl(1+O_G(\lambda^{-1})\bigr).
\tag{6}
\]

Every such excursion takes expected time \(O_G(\lambda^{-1})\), uniformly over its initial state. To see this, put \(g(S)=n-|S|\); in every proper nonempty state, \(\mathcal Lg=M(S)-\lambda c(S)\le M(V)-\lambda c_{\min}<0\), with \(c_{\min}>0\) the minimum nontrivial cut. Dynkin's formula stopped on \(\{\varnothing,V\}\) bounds the excursion duration by \(n/(\lambda c_{\min}-M(V))\). Each cycle also has a waiting time of mean \(1/m\) in state \(V\). The strong Markov property gives

\[
\mathbb E_V[\tau_\varnothing]
=\frac{1/m+O_G(\lambda^{-1})}{p_\lambda},
\]

which proves (1).

**3. An integral of directed cuts.** Fix any reference vertex \(r\) and set \(t_r=0\). For each directed arc define a positive-part term, and let

\[
J_G(t)=\sum_{(u,v):\{u,v\}\in E}w_{uv}(t_v-t_u)_+,
\qquad (z)_+=\max(z,0).
\]

Then the exact identity

\[
C_G=\int_{\mathbb R^{V\setminus\{r\}}}
\exp\bigl(-J_G(t)\bigr)\prod_{v\ne r}dt_v
\tag{7}
\]

holds. To prove it, ignore the measure-zero hyperplanes where two \(t_v\) coincide, order all coordinates as \(t_{\pi_1}<\cdots<t_{\pi_n}\), subtract the minimum, and set the \(n-1\) consecutive gaps \(d_k=t_{\pi_{k+1}}-t_{\pi_k}>0\). The affine change from the \(n-1\) free pinned coordinates to the gaps has absolute determinant one. For any directed arc, its contribution across a gap is precisely its weight if it runs from the lower-coordinate side \(S_k(\pi)\) to the higher-coordinate complement. Consequently \(J_G(t)=\sum_{k=1}^{n-1}c(S_k(\pi))d_k\). Integrating the independent positive gaps gives the corresponding term in \(C_G\); summing all orderings proves (7). Finiteness follows because every proper cut is positive.

**4. Factorization for trees and strict extra-edge effect.** If \(G=T\) is a tree, choose any root \(r\). The \(n-1\) signed edge differences \(d_{uv}=t_v-t_u\), with an arbitrary orientation for each tree edge, are independent linear coordinates with Jacobian determinant of absolute value one. Every edge contributes exactly

\[
\int_{-\infty}^{\infty}
\exp\bigl(-w_{uv}(d)_+-w_{vu}(-d)_+\bigr)\,dd
=\frac1{w_{uv}}+\frac1{w_{vu}}.
\]

Thus

\[
C_T=\prod_{\{u,v\}\in E(T)}
\left(\frac1{w_{uv}}+\frac1{w_{vu}}\right),
\tag{8}
\]

and substitution into (1) proves the claimed tree product and universal unit-weight conclusion.

More generally, if a positive bidirectional edge is added between previously nonadjacent vertices \(u,v\), its contribution to \(J_G\) is nonnegative and strictly positive whenever \(t_u\ne t_v\). The latter condition holds almost everywhere in (7), and the original integrand is positive and integrable. Therefore \(C_{G+\{u,v\}}<C_G\); by (1), the leading mean extinction-time coefficient strictly increases. This is a statement about fixed graphs as \(\lambda\to\infty\), not about ordering survival times at all finite \(\lambda\).

## Verification

Run the included Python 3 standard-library checker as `python3 verify.py`. It independently evaluates the exact finite inverse-cut recurrence and all permutation terms; checks connected graphs through four labelled vertices, all 1,441 labelled trees of orders two through six with asymmetric directed weights, and exact-rational finite-state Markov-chain hitting times on selected networks. Its recorded output is `ALL_CHECKS_PASSED`, with `total_exact_checks: 1576` and `tree_product_checks: 1441`. These checks are finite corroboration, not a substitute for the analytical proof above.

With unit rates, a three-vertex path has \(C_G=4\) and hence \(\mathbb E\tau\sim\lambda^2/4\); a triangle has \(C_G=3/2\) and \(\mathbb E\tau\sim 2\lambda^2/3\). Every four-vertex tree has \(\mathbb E\tau\sim\lambda^3/8\). With heterogeneous rates \((\mu_1,\mu_2,\mu_3)=(2,3,5)\) and opposite directed weights \((2,3)\), \((4,5)\) along a three-vertex path, the leading coefficient is exactly \(4/45\).

## Relationship to prior work

Mountford, Mourrat, Valesin and Yao established exponential persistence for growing bounded-degree finite trees at fixed supercritical infection intensity. Schapira and Valesin extended graph-size asymptotics to general finite connected graphs. The limit here is different: **a fixed finite graph** with \(\lambda\to\infty\), yielding an exact topology-sensitive prefactor and a universal tree factorization, not merely a graph-size growth bound.

Van de Bovenkamp and Van Mieghem derived exact finite-state survival-time formulas for the complete graph and the star. Those results motivate a topology-uniform comparison but do not, in their accessible abstract, state the all-tree, unequal-weight product or the general directed-cut integral. Since the complete 2015 paper could not be inspected, possible overlap with its additional formulas remains a historical-priority risk. Qu, Hanjalic and Wang treat recovery heterogeneity on directed SIS networks but optimize mean-field infection prevalence rather than finite-chain absorption-time asymptotics.

A previously published general first-passage or directed-cut integral theorem might imply this result without using the same vocabulary. Novelty is assessed only against the identified and inspectable material, not claimed as independently certified.

## Limitations

The theorem concerns exact finite-state continuous-time Markov SIS dynamics, full initial infection, positive rates in both directions on every present edge, and fixed finite graph as \(\lambda\to\infty\). For a growing graph, an edge weight tending to zero, one-way-only networks, stochastic contact durations, or approximated mean-field SIS equations, none of the stated uniform conclusions follows directly. The error term may depend strongly on network size and weights. The edge-addition conclusion is asymptotic, not an all-\(\lambda\) ordering. The 2015 survival-time paper could not be read in full, leaving specific historical overlap unresolved; no independent audit has been performed.

## References

1. T. Mountford, J.-C. Mourrat, D. Valesin, and Q. Yao, *Exponential extinction time of the contact process on finite graphs*, arXiv:1203.2972v1, first posted 2012-03-13. https://arxiv.org/abs/1203.2972
2. B. Schapira and D. Valesin, *Extinction time for the contact process on general graphs*, arXiv:1509.04133v1, first posted 2015-09-14. https://arxiv.org/abs/1509.04133
3. R. van de Bovenkamp and P. Van Mieghem, *Survival time of the susceptible-infected-susceptible infection process on a graph*, Physical Review E 92, 032806 (2015), first published 2015-09-15. https://doi.org/10.1103/PhysRevE.92.032806
4. B. Qu, A. Hanjalic, and H. Wang, *Heterogeneous Recovery Rates against SIS Epidemics in Directed Networks*, arXiv:1408.6959v1, first posted 2014-08-29. https://arxiv.org/abs/1408.6959
