# Ten species are sharp for a variance reversal under one degree-preserving ecological swap

## Finding
For connected simple bipartite plant–pollinator graphs, one degree-preserving checkerboard switch can reverse the ranking of the **variance** of the number of plants lost to independent pollinator extinction as the pollinator-failure probability changes. The smallest possible total number of plant and pollinator species is **ten**. The lower bound applies without degree restrictions beyond connectivity. A witness at ten has minimum degree two in both guilds.

For the explicitly displayed pair below, letting \(Z_G(q)\) count lost plants at independent pollinator-failure probability \(q\),
\[
\operatorname{Var}(Z_H(q))-\operatorname{Var}(Z_G(q))
=-2q^2(1-q)^2(1-2q).
\]
It is negative on \(0<q<1/2\), zero at \(q=1/2\), and positive on \(1/2<q<1\). The expected losses are identical for every probability.

## Assumptions and scope
Let \(G=(P\sqcup A,E)\) be a finite connected simple bipartite graph with labeled nonempty plant guild \(P\) and pollinator guild \(A\). Each pollinator is independently removed with probability \(q\in(0,1)\); a plant is lost if and only if all adjacent pollinators are removed. Pollinators do not rewire dynamically during the failures. A *checkerboard swap* chooses distinct plants \(i,j\) and pollinators \(a,b\) with edges \(ia,jb\) present and \(ib,ja\) absent, replaces the two present edges with the two absent edges, and preserves all other incidences. Both pre-swap and post-swap networks must be connected. Such a switch preserves each labeled vertex's degree.

For the witness, label five pollinators \(a,b,c,d,e\) by bit positions \(0,1,2,3,4\); a row bitmask specifies one plant's pollinator neighbors. Use
\[
G=(22,3,12,25,3),\qquad H=(22,6,9,25,3).
\]
Equivalently their plant neighborhoods are
\[
\begin{aligned}
G &: (\{b,c,e\},\{a,b\},\{c,d\},\{a,d,e\},\{a,b\}),\\
H &: (\{b,c,e\},\{b,c\},\{a,d\},\{a,d,e\},\{a,b\}).
\end{aligned}
\]
The swap is on plants two and three and pollinators \(a,c\). Both connected graphs have plant-degree sequence \((3,2,2,3,2)\) and pollinator-degree sequence \((3,3,2,2,2)\), with no vertex of degree one. The sample size here is total network order, **not** the number of extinction trials.

## Proof
Let \(N_i\subseteq A\) be the pollinator neighborhood of plant \(i\), \(d_i=|N_i|\), and \(u_{ij}=|N_i\cup N_j|\). Write \(X_i\) for the indicator that all pollinators adjacent to plant \(i\) have failed. The exact independent-failure identities are
\[
\mathbb E[X_i]=q^{d_i},\qquad
\mathbb E[X_iX_j]=q^{u_{ij}}.
\]
Therefore for \(Z=\sum_i X_i\),
\[
\operatorname{Var}(Z)=
\sum_i(q^{d_i}-q^{2d_i})
+2\sum_{i<j}(q^{u_{ij}}-q^{d_i+d_j}).
\]
A checkerboard swap fixes all \(d_i\). Define the *pair-union histogram* \(h_k(G)=|\{\{i,j\}:i<j,\ |N_i\cup N_j|=k\}|\). For two graphs related by a switch,
\[
\frac{\operatorname{Var}(Z_H(q))-\operatorname{Var}(Z_G(q))}{2}
=P(q)=\sum_{k=0}^{|A|}(h_k(H)-h_k(G))q^k.
\]
The witness histograms have difference coefficients \((0,0,-1,4,-5,2)\). Hence
\[
P(q)=-q^2+4q^3-5q^4+2q^5
=-q^2(1-q)^2(1-2q).
\]
The stated strict sign reversal follows, while matching degree sequences imply equal means \(3q^2+2q^3\).

It remains to prove **minimality**, uniformly over all \(q\in(0,1)\), not merely over sampled probabilities. For each positive integer pair \((m,n)\) with \(m+n\le 9\), enumerate every one of the \(2^{mn}\) binary \(m\times n\) incidence matrices exactly once. Retain those whose full bipartite graph is connected, and enumerate all unordered pairs of plant rows and ordered private-column choices generating a valid checkerboard switch with a connected output. Compute \(P(q)\) as an integer coefficient vector. For each polynomial, put \(q=x/(1+x)\), where \(x>0\), and set
\[
Q(x)=(1+x)^nP\!\left(\frac{x}{1+x}\right)
=\sum_{j=0}^n H_jx^j,
\quad H_j=\sum_{k=0}^j (h_k(H)-h_k(G))\binom{n-k}{j-k}.
\]
All \(H_j\) are integers. The exhaustive certificate verifies for **every admissible switch** in this entire bounded domain that the coefficient list \((H_0,\ldots,H_n)\) is either componentwise nonnegative or componentwise nonpositive (including identically zero). Thus \(Q(x)\), and therefore \(P(q)\), cannot change sign on the positive real line. This is an exact proof of the continuum-in-\(q\) statement; finite sampling alone would not suffice.

The program independently checks the number of connected matrices against the standard component-of-first-plant recurrence. If \(C(m,n)\) counts connected labeled bipartite graphs with the specified guild sizes, put \(C(1,0)=1\) and \(C(m,0)=0\) for \(m>1\), and use
\[
C(m,n)=2^{mn}-
\sum_{\substack{1\le i\le m,\ 0\le j\le n\\ (i,j)\ne(m,n)}}
\binom{m-1}{i-1}\binom{n}{j}C(i,j)2^{(m-i)(n-j)}.
\]
The summand chooses the component containing the first plant; all edges between that component and its complement must be absent, while incidences within the complement are arbitrary. All enumerated connected counts equal the independently computed recurrence counts.

## Verification
The included standalone `rewiring_verifier.cpp` is C++17. Compile with `g++ -O3 -std=c++17 rewiring_verifier.cpp -o verify` and run `./verify`. It enumerates every required guild-size combination through total order nine, tests **every connected-output checkerboard switch**, calculates the substitution-certificate coefficients with integer arithmetic, and checks the connected-graph counts using the separate recurrence. The largest two cases each contain exactly \(636331\) connected labeled incidence networks and \(5246640\) admissible directed switches; all passed the fixed-sign test. The witness check recomputes exact pair-union coefficients and independently enumerates all \(32\) pollinator-failure subsets at probabilities \(1/4\) and \(3/4\). It reports `ALL_EXACT_CHECKS_PASSED`.

## Relationship to prior work
Staniczenko, Lewis, Jones, and Reed-Tsochas (2010) motivate ecology's interest in rewiring and robustness following primary extinctions. Ramos-Jiliberto and coauthors (2012) model adaptive rewiring in plant–pollinator networks and compare persistence under several ecological rewiring rules. The latter complete article was inspected: its model includes time-evolving interactions and abundance dynamics and reports persistence/robustness measures; it does not give the exact one-swap, static-failure, plant-extinction-count variance classification proved here. The complete Staniczenko article was not available for inspection; its accessible abstract concerns dynamically rewired food webs and species persistence, not an established exact comparison of the present objects. A related degree-matched variance reversal for **arbitrary pairs** of networks on nine total species does not determine the threshold under the stricter *single-switch* requirement; the latter condition is the specific additional conclusion here.

## Limitations
This is a finite sharp-order theorem for static, binary, connected mutualistic interaction networks and independent identically distributed primary failures. It does not model abundance-dependent persistence, adaptive switching during an extinction process, correlated extinctions, or observed real-world ecosystem risk. The finite verification is complete only for total order at most nine; no unrestricted classification of all larger-network variance-difference polynomials is claimed. Independent scientific audit and complete inspection of every potentially equivalent paper remain outstanding.

## References
1. Staniczenko, P. P. A., Lewis, O. T., Jones, N. S., and Reed-Tsochas, F. (2010). *Structural dynamics and robustness of food webs*. Ecology Letters 13:891–899. DOI: 10.1111/j.1461-0248.2010.01485.x. Public online record dated 2010-05-12.
2. Ramos-Jiliberto, R., Valdovinos, F. S., Moisset de Espanés, P., and Flores, J. D. (2012). *Topological plasticity increases robustness of mutualistic networks*. Journal of Animal Ecology 81:896–904. DOI: 10.1111/j.1365-2656.2012.01960.x. Public online text dated 2012-02-07.
