# A mod-four census of minimum signed double Roman functions on even prisms

## Finding

Let \(P_m=C_m\square K_2\), where \(m\ge4\) is even and each of the \(2m\) vertices is distinguished by its cycle coordinate and its layer. Let \(N_m\) be the number of signed double Roman dominating functions on \(P_m\) of minimum possible weight, with the four labels distinguished and without identifying functions under graph automorphisms. Then

\[
N_m=\begin{cases}
2,&m\equiv2\pmod4,\\
14+4L_{m/4},&m\equiv0\pmod4,
\end{cases}
\qquad
L_0=2,\quad L_1=7,\quad L_{k+2}=7L_{k+1}-L_k.
\]

In particular, the numbers for \(m=4,6,8,10,12,14,16\) are respectively \(42,2,202,2,1302,2,8842\). For multiples of four the number of minimum functions grows exponentially, while for \(m\equiv2\pmod4\) it is identically two. The already known minimum weight \(\gamma_{\mathrm{sdR}}(P_m)=m\) is not part of the novelty claim.

## Assumptions and scope

The graph is undirected and simple, with vertices \((i,r)\), where \(i\in\mathbb Z/m\mathbb Z\) and \(r\in\{0,1\}\). Its three neighbors are \((i-1,r),(i+1,r),(i,1-r)\). A signed double Roman dominating function is \(f:V(P_m)\to\{-1,1,2,3\}\) with all of the following properties: every vertex labeled \(-1\) has a neighbor labeled \(3\), or at least two distinct neighbors labeled \(2\); every vertex labeled \(1\) has a neighbor labeled \(2\) or \(3\); and every vertex has closed-neighborhood sum \(f(v)+\sum_{u\sim v}f(u)\ge1\). Its weight is \(\sum_v f(v)\). No assertion is made for odd \(m\), where the optimum need not equal \(m\).

## Proof

**1. Equality rigidity from discharging.** The following argument works on any cubic graph. Each vertex with positive label \(q\in\{1,2,3\}\) sends \((2q-1)/4\) to every adjacent vertex labeled \(-1\); vertices with label \(-1\) send nothing. Let \(g(v)\) denote the resulting weight at \(v\). The total sum is unchanged.

For positive \(v\) with \(a\) negative neighbors,
\[
g(v)=q-a(2q-1)/4.
\]
The closed-neighborhood condition rules out \(a=3\), so \(a\le2\), and \(g(v)\ge1/2\), with equality exactly when \(a=2\). In that equality case the unique positive neighbor of a vertex labeled \(1\) must have label at least \(2\), by the defending condition.

For a negative vertex, if exactly two neighbors are positive, their labels \(p,q\) must be either two \(2\)'s or include a \(3\), and its retained weight is
\[
g(v)=-1+\frac{2p-1}{4}+\frac{2q-1}{4}=\frac{p+q-3}{2}\ge1/2.
\]
The equality pairs are precisely \(\{p,q\}=\{2,2\}\) and \(\{1,3\}\). At least two positive neighbors are necessary because a single positive \(3\) beside two negative neighbors would give closed sum zero. If all three neighbors are positive, the defending rule forces either one \(3\) or two \(2\)'s; consequently the transferred weight is at least \(3/4>1/2\). Thus \(g(v)\ge1/2\) for every vertex.

It follows that every feasible \(f\) on \(P_m\) has total weight at least \(m\). Equality holds if and only if **(E+)** each positively labeled vertex has exactly two negative neighbors and one positive neighbor, with a \(1\) paired with a positive label at least \(2\); and **(E−)** each negatively labeled vertex has exactly one negative neighbor and its two positive neighbors form either \(\{2,2\}\) or \(\{1,3\}\). These conditions are also sufficient for feasibility: (E+) supplies the required defense for label \(1\); (E−) supplies the required defense for \(-1\); closed-neighborhood sums at positive vertices are at least \(1\), and at negative vertices are exactly \(2\). Every such function has weight \(m\) because all final weights equal \(1/2\).

When \(m\) is even, alternating the columns \((2,2)\) and \((-1,-1)\) around the cycle satisfies (E+) and (E−), proving \(\gamma_{\mathrm{sdR}}(P_m)=m\) without needing an external optimality premise.

**2. A completely specified finite transfer.** Put \(\mathcal A=\{-1,1,2,3\}^2\), consisting of \(16\) ordered column-label pairs. Form a directed graph with \(256\) states \((a,b)\in\mathcal A^2\). For each triple \(a,b,c\in\mathcal A\), place the directed edge
\[
(a,b)\longrightarrow(b,c)
\]
precisely when, for each row \(r\in\{0,1\}\), the center label \(b_r\) satisfies (E+) or (E−) with the three neighbor labels \(a_r,c_r,b_{1-r}\), as appropriate. In particular, a positive center must see exactly two \(-1\)'s and a positive third label, which must be at least \(2\) when the center is \(1\); a negative center must see exactly one \(-1\) and its positive pair must have sum \(4\). This fully specifies the adjacency matrix \(T\) over the integers without any undocumented data.

A labeled cyclic arrangement of \(m\) columns is a closed walk of length \(m\) in \(T\) starting at the distinguished state of columns \(0,1\). Conversely every such walk gives exactly one cyclic arrangement. There is no division by \(m\), because the cycle positions are distinguished. Consequently \(N_m=\operatorname{tr}(T^m)\).

**3. Exact integer certificate for the transfer graph.** Constructing its edges from the preceding predicate produces \(81\) edges, with exactly five strongly connected components containing directed cycles; they have \(22,4,4,4,2\) states. All other states lie in acyclic components and do not contribute to the trace. The three four-state components are simple directed four-cycles, and the two-state component is a directed two-cycle. The \(22\)-state core has \(32\) internal edges; let its adjacency matrix be \(B\). Its characteristic polynomial is
\[
\det(tI-B)=t^{14}(t^8-7t^4+1).
\]
These exact finite claims are verified by the standalone `verify.py`, which specifies the graph, decomposes it by Tarjan's algorithm, and calculates the entire characteristic polynomial using exact integer Newton identities. The certificate is a finite exact computation, not an inference from a finite initial sequence of values.

**4. Trace calculation for all orders.** Let \(\alpha,\beta\) be the roots of \(z^2-7z+1\); thus \(\alpha+\beta=7\) and \(\alpha\beta=1\). The nonzero eigenvalues of \(B\) consist, with multiplicity, of the four fourth roots of \(\alpha\) and the four fourth roots of \(\beta\). Thus
\[
\operatorname{tr}(B^m)=\begin{cases}0,&4\nmid m,\\4(\alpha^{m/4}+\beta^{m/4}),&4\mid m.\end{cases}
\]
The three directed four-cycles contribute \(12\) if \(4\mid m\) and zero otherwise. The two-cycle contributes \(2\) for even \(m\). Therefore \(N_m=2\) for \(m\equiv2\pmod4\), and \(N_m=14+4(\alpha^{m/4}+\beta^{m/4})\) for \(4\mid m\). The sequence \(L_k=\alpha^k+\beta^k\) has initial values \(2,7\) and satisfies the stated recurrence. This completes the all-order proof.

## Verification

Run `python3 verify.py` using Python 3 and only its standard library. It builds all \(16^3=4096\) possible local column triples and independently compares the tight conditions against the original signed-double-Roman rules together with exact discharging equality. It checks the five recurrent components, their exact internal edge counts, and every coefficient of the \(22\)-state characteristic polynomial using integer arithmetic. An independent weighted transfer counts unrestricted minimum functions at orders \(4,6,8\); direct brute force checks all \(4^8=65536\) vertex assignments at order \(4\); and traces are checked at twelve further even orders through \(40\). The recorded execution is in `verification_output.txt`. The mathematical conclusion for unbounded \(m\) uses the proven discharging rigidity and the exact finite characteristic polynomial.

## Relationship to prior work

Iurlano, Zec, Djukanovic, and Raidl established the **minimum weight** for the prism family, as Theorem 6 of *Signed double Roman domination on cubic graphs* (2023 preprint, 2024 journal version). The present result begins with that setting but counts every minimizing four-label function; their exhibited configurations and scalar extremal value do not determine this count. The foundational literature of Ahangar, Chellali and Sheikholeslami gives the definition and broad graph-family bounds. Generic Roman domination, Roman \(\{3\}\)-domination, and ordinary domination enumerations have different feasible-label rules and do not imply this formula. An unindexed equivalence of the optimizer transfer graph to some previously enumerated cyclic-word system remains a genuine priority risk.

## Limitations

The formula applies only to even cyclic prisms with \(m\ge4\); it does not count nonminimum functions, classify optimum functions up to graph automorphisms, or claim corresponding formulas for odd prisms or more general generalized Petersen graphs. The algorithmic certificate is fully reproducible exact finite arithmetic, but not an independent external validation. Exhaustive bibliographic priority verification is not claimed.

## References

1. E. Iurlano, T. Zec, M. Djukanovic, G. R. Raidl, *Signed double Roman domination on cubic graphs*, arXiv:2308.01109v1 (first public 2 August 2023), Theorem 6 and sections on cubic discharging and generalized Petersen graphs. https://arxiv.org/abs/2308.01109 ; https://arxiv.org/pdf/2308.01109 ; journal DOI: 10.1016/j.amc.2024.128612.
2. H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami, *Signed double Roman domination in graphs*, Discrete Applied Mathematics 257 (2019), DOI: 10.1016/j.dam.2018.09.009.
3. *Signed Double Roman Domination of Graphs*, Filomat 33(1) (2019), accessible primary full text: https://www.pmf.ni.ac.rs/filomat-content/2019/33-1/33-1-10-7257.pdf.
