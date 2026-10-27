# A parity bifurcation in the recurrent-state census of crown-graph majority dynamics

## Finding

Let \(n\ge3\). On the labelled crown graph \(G_n=K_{n,n}-M_n\), with vertices \(L_1,\ldots,L_n,R_1,\ldots,R_n\) and edges \(L_iR_j\) precisely when \(i\ne j\), synchronously update each binary vertex state to the strict majority of its neighbours, retaining the current state when neighbours tie. Let \(F_n\) be the resulting finite-state map, \(Q_n=|\{x:F_n(x)=x\}|\), and \(P_n=|\{x:F_n^2(x)=x\}|\). Every orbit eventually reaches a fixed point or primitive two-cycle. The numbers of fixed configurations, recurrent configurations, and distinct primitive two-cycles have the following exact formulas.

For even \(n=2m\), writing \(s_m=\binom{2m}{m}+2\),
\[
 Q_{2m}=s_m,\qquad P_{2m}=s_m^2,\qquad C_{2m}=\frac{s_m(s_m-1)}2.
\]
Every initial state has entered its eventual one- or two-cycle **after at most one update**: \(F_{2m}^3=F_{2m}\).

For odd \(n=2m+1\),
\[
 Q_{2m+1}=2(m+2)\binom{2m+1}{m}+2,\qquad
 P_{2m+1}=2(m+2)\binom{2m+1}{m}+4,\qquad C_{2m+1}=1.
\]
The sole primitive two-cycle in the odd case is the alternating pair of configurations monochromatic on each bipartition class, with opposite colors. All other recurrent configurations are fixed.

Consequently, for uniformly sampled binary initial configurations, the fraction which are **already recurrent** obeys the parity-divergent asymptotics
\[
 \frac{P_n}{2^{2n}}\sim\frac{2}{\pi n}\quad(n\to\infty,\ n\text{ even}),\qquad
 \frac{P_n}{2^{2n}}\sim\sqrt{\frac{2n}{\pi}}\,2^{-n}\quad(n\to\infty,\ n\text{ odd}).
\]
Thus the even-degree crown graphs have exponentially fewer recurrent configurations (as a fraction of all configurations) than their odd-degree counterparts, despite differing in vertex count by just two.

## Assumptions and scope

The graph is simple, connected for \(n\ge3\), and has two labelled classes of \(n\) vertices each. Each vertex has degree \(n-1\). States are \(0\) or \(1\), all vertices update simultaneously, and a tie is broken by retaining that vertex's current state. The counts distinguish vertex labels: no quotient by automorphisms or global color-complementation is taken. Here \(P_n\) counts **periodic configurations**, not the number of periodic orbits; \(C_n=(P_n-Q_n)/2\) counts primitive two-cycles.

## Proof

**1. Every recurrent state has period at most two.** Encode the binary state by spins \(x_i(t)\in\{-1,1\}\). Let \(W\) be the symmetric adjacency matrix of \(G_n\) if \(n\) is even; if \(n\) is odd, add the identity matrix to the adjacency matrix. The extra diagonal spin implements tie retention because \(n-1\) is even. Each row of \(W\) then has an odd number of unit entries, so each local field \(h_i(t)=\sum_jW_{ij}x_j(t)\) is nonzero and \(x_i(t+1)=\operatorname{sgn}h_i(t)\).

The integer-valued, bounded cross-time energy \(E_t=x(t+1)^T W x(t)\) satisfies, by symmetry,
\[
 E_{t+1}-E_t=\sum_i\bigl(x_i(t+2)-x_i(t)\bigr)h_i(t+1)\ge0.
\]
Each summand is zero when \(x_i(t+2)=x_i(t)\) and is \(2|h_i(t+1)|>0\) otherwise. Hence strictly increasing energy occurs whenever \(x(t+2)\ne x(t)\); since the energy is a bounded integer, eventually \(x(t+2)=x(t)\). This also directly supplies the standard finite symmetric-threshold period-two principle without assuming it.

**2. Even \(n=2m\).** Write each configuration as \((a,b)\in\{0,1\}^n\times\{0,1\}^n\), using the deleted matching to align coordinates. Each vertex sees all of the opposite class except its matched partner. Since degree \(2m-1\) is odd, define
\[
 f(v)=\begin{cases}
 0^n,&|v|<m,\\
 \overline v,&|v|=m,\\
 1^n,&|v|>m.
 \end{cases}
\]
Then \(F_n(a,b)=(f(b),f(a))\). Its one-step image is \(S\times S\), where \(S=\{0^n,1^n\}\cup\{v:|v|=m\}\) has size \(s_m\). Every element of \(S\) is mapped within \(S\), and \(f^2\) is the identity on \(S\). Therefore \(F_n^3=F_n\), and exactly \(s_m^2\) states are periodic. A state is fixed if and only if \((a,b)=(f(b),b)\) with \(b\in S\), yielding \(s_m\) fixed states. The remaining \(s_m^2-s_m\) states split into two-cycles.

**3. Odd \(n=2m+1\): the local rule.** For \(A=|a|\) and \(B=|b|\), the left-class update is
\[
 a'=\begin{cases}
 0^n,&B\le m-1,\\
 a\setminus b,&B=m,\\
 a\cup\overline b,&B=m+1,\\
 1^n,&B\ge m+2,
 \end{cases}
\]
where subsets denote coordinates carrying state \(1\); the right-class rule is identical with \(a,b\) interchanged. This is exactly strict open-neighbourhood majority with tie retention, not an approximation by class means.

**4. Odd case: outside the two central weight layers.** If \(A\le m-1\), then \(b'=0^n\), which forces \(a''=0^n\). Thus a state satisfying \(F_n^2(a,b)=(a,b)\) in this region has \(a=0^n\). When \(a=0^n\), direct substitution gives \(F_n^2(a,b)=(0^n,0^n)\) for \(B\le m+1\), and \(F_n^2(a,b)=(0^n,1^n)\) for \(B\ge m+2\). Only \((0^n,0^n)\) and \((0^n,1^n)\) are periodic here. Similarly, \(A\ge m+2\) forces \(a=1^n\) for a periodic state; direct substitution gives only \((1^n,0^n)\) and \((1^n,1^n)\). Interchanging left and right handles cases when \(B\) is noncentral. Two corners are fixed and the remaining two form one primitive two-cycle.

**5. Odd case: the central layers.** It remains to examine \(A,B\in\{m,m+1\}\). Put \(t=|a\cap b|\). If \(A=B=m\), then \((A',B')=(m-t,m-t)\). For \(t=0\), the state is fixed (disjoint supports); for \(t>0\), both counts drop below \(m\), and the next image is \((0^n,0^n)\). If \(A=B=m+1\), then \(t\ge1\) and \((A',B')=(m+t,m+t)\). For \(t=1\), the supports cover every coordinate, so the state is fixed; for \(t>1\), the next image is \((1^n,1^n)\).

Finally, if \(A=m\), \(B=m+1\), then \((A',B')=(m+t,m+1-t)\). For \(t=0\) the two supports are complementary and the state is fixed. For \(t=1\), the new supports are disjoint and have weights \((m+1,m)\), hence the image is fixed and the original state is not a two-cycle. For \(t\ge2\), the counts leave the central range in opposite directions; the second iterate is a corner, so no original central configuration is periodic. The case \((m+1,m)\) follows by swapping the two classes.

Counting the fixed central configurations: the disjoint \((m,m)\) pairs contribute \((m+1)\binom{2m+1}{m}\); the covering \((m+1,m+1)\) pairs contribute the same number; and the two complementary mixed-weight cases each contribute \(\binom{2m+1}{m}\). Together with the two fixed corners this yields exactly \(Q_{2m+1}=2(m+2)\binom{2m+1}{m}+2\). The two other corners form the unique primitive two-cycle, yielding \(P_{2m+1}=Q_{2m+1}+2\). The energy argument in step 1 excludes periods longer than two.

**6. Fractions.** Each labelled graph has \(2^{2n}\) binary configurations. Apply \(\binom{2m}{m}\sim4^m/\sqrt{\pi m}\) and \(\binom{2m+1}{m}\sim2^{2m+1}/\sqrt{\pi(m+1/2)}\) to the exact formulas. The two stated asymptotic laws follow.

## Verification

Run `python3 verify_crown.py` in a directory containing the accompanying standalone script. It enumerates every one of the \(2^{2n}\) labelled states for each \(3\le n\le9\), directly implements neighbour majority on the graph, and checks the exact fixed/periodic counts and the even one-step identity. The recorded output is in `verification_output.txt`. Finite checks corroborate but do not replace the proof for all \(n\).

## Relationship to prior work

The classical finite symmetric-threshold theorem guarantees eventual period at most two but leaves the graph-dependent recurrent-state census open. Benjamini et al., arXiv:1405.2486v1 (2014), study global finite/infinite majority behaviour and probabilistic consensus on random graphs, not exact labelled crown-graph periodic counts. Turau, arXiv:2202.01580v1 (2022), develops fixed/two-cycle characterizations specifically for trees, whereas crown graphs for \(n\ge3\) contain cycles. Existing crown-graph combinatorics concerns different graph invariants. The present exact binomial formulas and the polynomial-versus-exponential parity change in the periodic-state fraction are not implied by those results. The general eventual-period-two principle is explicitly **not** claimed as new.

## Limitations

The finding classifies the recurrent set and its cardinalities, not the sizes of individual basins, the full distribution of transient depths for odd \(n\), or random initial consensus probabilities. The statement concerns synchronous majority with tie retention; it does not apply automatically to stochastic/asynchronous updates or different tie conventions. Searches did not identify an equivalent crown-graph enumeration, but cannot rule out unindexed publications. The classical 1980 article's full text was not available in the inspected sources; its period-two premise is re-proved above for this particular map.

## References

1. Itai Benjamini, Siu-On Chan, Ryan O'Donnell, Omer Tamuz and Li-Yang Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (publicly posted 2014-05-11), https://arxiv.org/html/1405.2486v1.
2. Volker Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580v1 (publicly posted 2022-02-03), https://arxiv.org/html/2202.01580v1.
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI:10.1016/0012-365X(80)90121-1. Publication year known; exact first-public day not established here.
4. *Crown Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/CrownGraph.html (graph definition only).
