# A densest-subgraph threshold and finite excitation budget for three-state graph dynamics

## Finding
For any finite simple undirected graph \(G=(V,E)\) and integer \(q\ge2\), define its maximum induced edge density by
\[
\rho(G)=\max_{\varnothing\ne S\subseteq V}\frac{|E(G[S])|}{|S|}.
\]
In synchronous three-state Greenberg–Hastings excitation at threshold \(q\), if \(\rho(G)<q\), all trajectories extinguish. More quantitatively, when \(m\) vertices are initially excited, the total number \(N\) of excited vertex-time occurrences, over all times, satisfies
\[
N\le\left\lfloor\frac{qm}{q-\rho(G)}\right\rfloor,
\qquad
F^{\left\lfloor qm/(q-\rho(G))\right\rfloor+1}(x_0)=\mathbf0.
\]
The coefficient concerns the *number of excitations*, not merely the number of distinct ever-excited vertices. The density boundary is sharp for a universal extinction criterion: for every integer \(q\ge2\), the graph \(K_{2q,2q}\) has \(\rho=q\) and admits a primitive nonzero orbit of length four. This does not assert that density at least \(q\) suffices for persistence on every graph.

## Assumptions and scope
Write a vertex state as \(0\) (resting), \(1\) (excited), or \(2\) (refractory). Every vertex updates simultaneously. The map sends \(1\mapsto2\mapsto0\). A resting vertex changes to \(1\) if and only if at least \(q\) *distinct* neighbours are in state \(1\) immediately before the update; otherwise it stays \(0\). Graphs are finite, simple and undirected. The proof works also for \(q=1\), though that extension is not required for the principal statement. The empty graph has \(\rho=0\). A vertex initially refractory is not counted in \(m\); such a vertex becomes resting after one update unless excited afresh at a later time.

## Proof
Let \(x_t=F^t(x_0)\), and \(I_v(t)=1\) exactly when vertex \(v\) is excited at time \(t\). A vertex cannot be excited at two times differing by one or two, because its immediate post-excitation states are refractory and then resting. Thus distinct excitation events at the same vertex are separated by at least three updates.

Fix a finite horizon \(T\ge0\). Put \(a_v=\sum_{t=0}^T I_v(t)\), \(N_T=\sum_v a_v\), and \(m=\sum_v I_v(0)\). For each edge \(\{u,v\}\), call a transmission an ordered pair of endpoint excitation events at consecutive times: either \((u,t-1)\to(v,t)\) or \((v,t-1)\to(u,t)\) for \(1\le t\le T\). Any excitation event on a fixed endpoint participates in **at most one** transmission along that edge. Indeed, a given event cannot participate twice as sender (its neighbour would have to be excited simultaneously at two times), or twice as receiver; participating once as sender and once as receiver would force the other endpoint to be excited at times separated by two updates. This is impossible by the refractory separation property. Consequently transmissions along \(\{u,v\}\) form a matching between its endpoints' excitation-event sets and number at most \(\min(a_u,a_v)\).

Every excitation after time zero requires at least \(q\) excited neighbours one update earlier, hence at least \(q\) distinct transmissions into that event. Therefore
\[
q(N_T-m)\le \sum_{\{u,v\}\in E}\min(a_u,a_v).
\]
For each integer \(j\ge1\), put \(S_j=\{v:a_v\ge j\}\). The integer layer-cake identity gives
\[
\sum_{\{u,v\}\in E}\min(a_u,a_v)
 =\sum_{j\ge1}|E(G[S_j])|
 \le\rho(G)\sum_{j\ge1}|S_j|
 =\rho(G)N_T.
\]
Combining these bounds shows \((q-\rho(G))N_T\le qm\) for every finite horizon \(T\). If \(\rho(G)<q\), all nondecreasing integer values \(N_T\) are bounded by \(\lfloor qm/(q-\rho(G))\rfloor\), so finitely many excitation events occur. Once one time slice contains no excited vertex, no future excitation is possible. In particular, the nonempty excitation-time slices occur consecutively from time zero through their last time \(L\). If \(m>0\), then \(L+1\le N\), and two further state updates make the last excited vertices refractory and then resting. Thus extinction occurs by update \(N+1\). If \(m=0\), no later vertex becomes excited and any initial refractory states clear at update one; the same bound holds. This proves the theorem.

To prove sharpness of the *strict threshold*, partition each shore of \(K_{2q,2q}\) into equal sets \(A_0,A_1\) and \(B_0,B_1\), each of size \(q\). At time zero assign states \(A_0=1\), \(A_1=0\), \(B_0=0\), \(B_1=2\). At time one the four classes have states \((2,0,1,0)\), at time two \((0,1,2,0)\), at time three \((0,2,0,1)\), and at time four return to \((1,0,0,2)\). The intermediate four states are distinct, so the period is exactly four. Every nonempty induced subgraph on \(a\) left and \(b\) right vertices has edge density \(ab/(a+b)\le q\), attaining \(q\) at \(a=b=2q\). Hence \(\rho(K_{2q,2q})=q\).

## Verification
The reproducible Python script `verify_density.py` implements the stated update rule and calculates maximum induced edge density with exact rational arithmetic. It enumerates all \(11{,}259\) initial configurations across nine small-graph/threshold instances, checks actual event-level transmission matching, verifies the derived inequalities and extinction-time bound, and explicitly checks primitive period four on \(K_{2q,2q}\) for \(q\in\{1,2,3\}\). The recorded stdout is `verification_output.txt`; run `python3 verify_density.py` with Python 3.9 or later and compare stdout to this file. These finite checks corroborate, but do not replace, the preceding proof for arbitrary graphs.

## Relationship to prior work
Durrett and Griffeath's 1993 work develops threshold-range excitable cellular automata, chiefly in spatially extended settings; the result here instead uses a maximum induced-edge-density obstruction valid on arbitrary finite graphs with nonuniform degrees and for **every** initial configuration. Doba's 2018 full-text study of the finite-graph Greenberg–Hastings map uses excitation triggered by one excited neighbour, characterizing cycle-geometry phenomena rather than giving this multi-neighbour density budget. Bello and Sivakoff analyze infinite regular-tree cyclic automata and Greenberg–Hastings models with probabilistic starting states, not this deterministic finite-graph bound. The density theorem implies extinction for all graphs of maximum degree below \(2q\), since \(\rho(G)\le\Delta(G)/2\), and also applies to many graphs with larger maximum degree. For example, a wheel with \(n\) rim vertices has \(\rho=2n/(n+1)<2\), despite its unbounded hub degree. It explains extinction for certain graph families but does not yield their previously established sharp, size-independent extinction times.

## Limitations
The budget can be loose, particularly when \(q-\rho(G)\) is small. It does not classify transient lengths exactly, and it is not a necessary-and-sufficient criterion for any fixed graph: dense graphs may nevertheless extinguish. Universal sharpness is a family of examples at equality, not an assertion that every graph at equality persists. Historical equivalence in unindexed literature cannot be categorically excluded. The computational tests are finite; the arbitrary-graph assertion is proved by the event-matching and layer-cake argument above.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata* (public preprint dated 1993-03-22), arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002.
2. J. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–135, https://doi.org/10.25088/ComplexSystems.27.2.101.
3. D. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees*, arXiv:2108.06404 (2021), https://arxiv.org/abs/2108.06404.
