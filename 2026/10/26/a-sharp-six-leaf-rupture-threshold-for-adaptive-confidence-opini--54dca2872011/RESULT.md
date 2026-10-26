# A sharp six-leaf rupture threshold for adaptive-confidence opinion averaging

## Finding
Consider synchronous adaptive-confidence Hegselmann–Krause opinion dynamics on a connected undirected graph. All opinions lie in \([0,1]\), each original graph edge starts with the same confidence bound \(c\), and each edge is receptive exactly when its endpoint opinions differ by less than its current bound. A receptive edge's bound increases by \(\gamma\) times its distance from \(1\); an unreceptive edge's bound is multiplied by \(\delta\). Every agent synchronously averages its own opinion with those of its currently receptive neighbors.

For every finite connected graph \(G\) of diameter \(D\), whenever \(0<c\le 1/D\), the property

> Every initial opinion profile in \([0,1]^{V(G)}\) for which all graph edges are initially receptive keeps **all** edges receptive at **every** subsequent time

holds if and only if, for each integer \(t\ge1\),
\[
 c\,\Lambda_G(t)\le 1-(1-c)(1-\gamma)^t,
 \qquad
 \Lambda_G(t)=\max_{\{u,v\}\in E(G)}W_1^G\bigl(P^t(u,\cdot),P^t(v,\cdot)\bigr).
\]
Here \(P\) is the self-inclusive uniform-neighbor averaging Markov kernel on \(G\) and \(W_1^G\) is first Wasserstein distance for ordinary graph distance. The condition is independent of \(\delta\). Under it all agents converge to consensus with value
\[
 \frac{\sum_{v\in V(G)}(\deg(v)+1)x_v(0)}{\sum_{v\in V(G)}(\deg(v)+1)}.
\]

For the star \(K_{1,k}\), with \(k\ge1\) leaves and \(0<c\le1/2\) (for the one-edge star, the same statement holds for every \(0<c<1\)), the above *infinite family* of requirements reduces to a single, sharp threshold:
\[
 \boxed{\gamma\ge\gamma_*(k,c)
 =\max\!\left\{0,\frac{k-5}{2(k+1)}\frac{c}{1-c}\right\}.}
\]
Thus every initially receptive star with at most five leaves stays fully receptive even at zero reinforcement. Starting at **six leaves**, and for every \(\gamma<\gamma_*(k,c)\), some strictly initially receptive profile loses an edge at the **very first update**, regardless of \(\delta\). At equality with the threshold, all edges still persist and the agents reach consensus. For a star, the consensus equals
\[
 \frac{(k+1)x_o(0)+2\sum_{i=1}^{k}x_i(0)}{3k+1},
\]
where \(o\) is the hub.

## Assumptions and scope
The graph \(G=(V,E)\) is finite, simple, connected and undirected, with at least two vertices, and graph distance \(d_G\). At integer time \(t\ge0\), an agent \(v\) has opinion \(x_v(t)\in[0,1]\) and an edge \(\{u,v\}\) has bound \(c_{uv}(t)\). At time zero all edge bounds equal \(c\in(0,1)\). The parameters satisfy \(\gamma,\delta\in[0,1]\). Define the receptive neighbors \(N_v(t)=\{u:\{u,v\}\in E,\ |x_u(t)-x_v(t)|<c_{uv}(t)\}\). The update is
\[
 x_v(t+1)=\frac{x_v(t)+\sum_{u\in N_v(t)}x_u(t)}{1+|N_v(t)|},
\quad c_{uv}(t+1)=\begin{cases}
 c_{uv}(t)+\gamma[1-c_{uv}(t)]&\text{if receptive at time }t,\\
 \delta c_{uv}(t)&\text{otherwise.}
 \end{cases}
\]
All claims about uniform edge persistence quantify over **every** initially fully receptive opinion profile. The diameter restriction on \(c\) is needed for the stated **necessity** of the graph-wide Wasserstein criterion; its sufficiency holds without that restriction. The star claim is sharp in the stated range, not an assertion about arbitrary initial partial receptivity or other network classes.

## Proof
**1. Fixed fully receptive dynamics and exact graph criterion.** Let \(P(v,u)=1/(\deg(v)+1)\) for \(u=v\) or \(\{u,v\}\in E\), and zero otherwise. As long as every edge remains receptive, \(x(t)=P^t x(0)\), and every bound is
\[
 c_t=1-(1-c)(1-\gamma)^t.
\]
Let \(L(f)=\max_{\{u,v\}\in E}|f(u)-f(v)|\). The shortest-path property makes \(L(f)\) the graph-metric Lipschitz constant. Finite Kantorovich–Rubinstein duality yields the **exact** operator norm
\[
 \sup_{L(f)\le1}L(P^t f)
 =\max_{\{u,v\}\in E}W_1^G(P^t(u,\cdot),P^t(v,\cdot))
 =\Lambda_G(t).
\]
For every strictly initially receptive profile, \(L(x(0))<c\); consequently \(L(P^t x(0))\le\Lambda_G(t)L(x(0))<c_t\) whenever \(c\Lambda_G(t)\le c_t\). Induction proves that all edges are receptive at every time.

Conversely suppose that for some \(t\ge1\), \(c\Lambda_G(t)>c_t\). Because \(G\) is finite, duality supplies a graph-distance \(1\)-Lipschitz real function \(f\) achieving \(\Lambda_G(t)\) for an edge. Shift \(f\) to have minimum zero; its range is at most the diameter \(D\). Choose \(s\in(0,1)\) sufficiently close to one so that \(sc\Lambda_G(t)>c_t\). The initial opinions \(x_v(0)=sc(f(v)-\min f)\) lie in \([0,1]\) since \(cD\le1\), and all initial edges are **strictly** receptive. If all edges stayed receptive through time \(t\), their gap at that time on the maximizing edge would equal \(sc\Lambda_G(t)>c_t\), a contradiction. Thus uniform persistence fails. This proves both directions, including equality in the safe criterion.

**2. Reduction on the star.** Put \(d_i(t)=x_o(t)-x_i(t)\), so \(\|d(t)\|_\infty\) is the maximum opinion gap across its edges. If all edges are receptive then
\[
 d(t+1)=B_kd(t),\qquad
 B_k=\tfrac12 I_k-\tfrac1{k+1}J_k,
\]
where \(J_k\) is the all-ones matrix. The exact row-sum norm is
\[
 \|B_k\|_{\infty\to\infty}=\frac{3(k-1)}{2(k+1)}=:\kappa_k.
\]
For \(k\ge2\), direct multiplication gives
\[
 B_k^2=\tfrac14I_k-\tfrac1{(k+1)^2}J_k,\qquad
 \|B_k^2\|_{\infty\to\infty}=\tfrac14+\frac{k-2}{(k+1)^2}\le\tfrac13.
\]
Since \(\kappa_k<3/2\), for all \(t\ge2\) the matrix norm \(\|B_k^t\|_{\infty\to\infty}\) is strictly smaller than one: for even \(t=2m\) it is at most \((1/3)^m\), and for odd \(t=2m+1\ge3\) it is at most \(\kappa_k(1/3)^m<1/2\). When \(k=1\), \(B_1=0\) directly. Each star edge-difference vector can be chosen freely up to its sup norm, so its exact Wasserstein/Lipschitz amplification at time \(t\) is \(\|B_k^t\|_{\infty\to\infty}\). All times \(t\ge2\) are harmless because \(c_t\ge c\); the sole restriction is \(\kappa_kc\le c_1=c+\gamma(1-c)\), equivalent to the stated \(\gamma_*\).

**3. Sharpness and the six-leaf onset.** If \(k\le5\), \(\kappa_k\le1\) and the threshold is zero. If \(k\ge6\), \(\kappa_k>1\). Given \(\gamma<\gamma_*\), choose a sufficiently small \(\varepsilon\in(0,1)\) and set the hub opinion to \(1/2\), one distinguished leaf's opinion to \(1/2-(1-\varepsilon)c\), and all the other leaves' opinions to \(1/2+(1-\varepsilon)c\). Because \(c\le1/2\), these are valid opinions and every edge is initially receptive. The distinguished edge's gap after one synchronous update is exactly \(\kappa_k(1-\varepsilon)c>c+\gamma(1-c)\); it is then unreceptive. The parameter \(\delta\) has not entered because no edge was unreceptive at time zero.

**4. Consensus when all edges persist.** The matrix \(P\) is irreducible and aperiodic because \(G\) is connected and every vertex has positive holding probability. It is reversible with stationary distribution \(\pi_v\propto\deg(v)+1\), as detailed balance follows by comparing \(\pi_vP(v,u)\) on either orientation of an edge. Hence \(P^t x(0)\) converges to the stationary-weighted mean, yielding both consensus formulas. For the star, the hub degree plus one is \(k+1\) and each leaf degree plus one is \(2\).

## Verification
A standalone standard-library Python program, `verify.py`, performs exact-rational checks of the star edge-difference matrix and its first powers for all degrees from one through twenty-five; checks the exact squared-matrix norm; tests threshold persistence for all \(2^k\) signs of initial leaf gaps for degrees through nine and twelve updates; checks explicit subcritical first-step counterexamples, and checks invariance of the stationary weighted mean. The program reports **24,931** recorded exact-rational checks passed. These finite checks are corroboration; the proof above, including Kantorovich duality, is what establishes the all-graphs and all-degrees quantifiers.

For a completely explicit sharpness witness with six leaves, take \(c=1/4\), \(\gamma=0\), hub opinion \(1/2\), one leaf opinion \(101/400\), and each other leaf opinion \(299/400\). Initially all six edge gaps are \(99/400<1/4\). After one update the hub is at \(449/700\), the singled leaf is at \(301/800\), and their gap is \(297/1120>1/4\). The critical reinforcement for this six-leaf star is exactly \(\gamma_*=1/42\).

Reproduce with `python3 verify.py`; no third-party package is required.

## Relationship to prior work
Li, Luo and Porter (first public preprint 14 March 2023, full open preprint version of 27 July 2024) define exactly the dyadic adaptive-confidence HK update used here and establish asymptotic confidence-bound and effective-graph stabilization results. Their relevant modeling equations are (2.2) and (2.3), and their graph-theoretic statements include Theorems 2–4. The present claim instead concerns a **universal, all-initial-profiles, all-time preservation criterion** and its exact star-degree/reinforcement phase transition; it neither claims to introduce the model nor to reprove its general eventual-stabilization theorem.

Bauer, Jost and Liu study Kantorovich transport and Ollivier curvature of graph-walk kernels, including higher-step transportation contraction. Their framework includes the transport quantities used in the first part of the proof, but does not state a confidence-adaptation criterion or the sharp star-degree threshold. The exact finite Kantorovich duality used here is standard prior mathematics, not claimed as a novel lemma.

Sun's 2009 conference paper concerns a sufficient initial-connectivity criterion for consensus of a Krause–Hegselmann model. Only its abstract could be inspected in this round. A sufficient consensus condition in the baseline setting does not, from its abstract alone, establish the present necessary-and-sufficient persistence threshold; nevertheless this remains a publication-priority risk requiring source access before any external novelty claim.

## Limitations
The result concerns synchronous, self-inclusive, equal-neighbor averaging on a fixed undirected graph, homogeneous initial dyadic bounds, scalar opinions, and **initially fully receptive** networks. The exact *necessity* of the graph-general Wasserstein test is established for \(c\le1/D\). The star phase boundary is sharp for \(c\le1/2\), not claimed to remain sharp at larger initial bounds. Rupture means an edge is unreceptive at some time; no claim is made that a broken edge never reforms or that consensus is impossible below the threshold. This result does not concern asynchronous Deffuant updates, directed networks, heterogeneous initial confidence bounds, or stochastic tie formation. The theoretical proof has not received an independent scientific audit. The originality comparison is necessarily non-exhaustive, particularly for the inaccessible full text of the earlier consensus criterion.

## References
1. G. J. Li, J. Luo, and M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563 (initial submission 14 March 2023; open full-text version 3, 27 July 2024), https://arxiv.org/abs/2303.07563 ; full-text mirror https://pdfs.assets.alphaxiv.org/2303.07563v3.pdf .
2. F. Bauer, J. Jost, and S. Liu, *Ollivier-Ricci Curvature and the Spectrum of the Normalized Graph Laplace Operator*, arXiv:1105.3803, https://arxiv.org/pdf/1105.3803 .
3. Z. Sun, *A Verifiable Criterion for Consensus of K-H Model*, IEEE CCA/ISIC 2009, pp. 1610–1612, https://doi.org/10.1109/CCA.2009.5280700 (abstract inspected; full text not accessed).
4. R. Hegselmann and U. Krause, *Opinion Dynamics and Bounded Confidence Models, Analysis, and Simulation*, J. Artif. Soc. Soc. Simul. 5(3) (2002), article 2 (background model).
