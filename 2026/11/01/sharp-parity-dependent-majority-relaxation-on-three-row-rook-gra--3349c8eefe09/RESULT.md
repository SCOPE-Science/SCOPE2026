# Sharp parity-dependent majority relaxation on three-row rook graphs

## Finding
For every integer \(n\ge2\), let \(G_n=K_3\square K_n=L(K_{3,n})\). In synchronous binary neighbor-majority dynamics, a vertex adopts the strict majority of its \(n+1\) neighbors, retaining its state when their opinions tie. Every trajectory reaches a fixed point or a primitive two-cycle. With
\[
T(x)=\min\{t\ge0:F_n^{t+2}(x)=F_n^t(x)\},
\]
the **sharp** largest first-periodic-entry time is
\[
\max_x T(x)=\begin{cases}
2,&n=2,\\
3,&n=3,4\text{ or odd }n\ge5,\\
4,&\text{even }n\ge6.
\end{cases}
\]
In particular, the infinite-family iterate identities \(F_{2k+1}^{5}=F_{2k+1}^{3}\) for every \(k\ge1\), and \(F_{2k}^{6}=F_{2k}^{4}\) for every \(k\ge1\), hold on the **entire labelled configuration spaces**. The shorter bounds for the small even cases follow by exact enumeration.

There is also an **exact finite-sum formula for every first-entry layer and least period**. For each initial binary column type \(j\in\{0,\ldots,7\}\), encode its three bits as \(b_i(j)=(j/2^i)\bmod2\), \(i=0,1,2\). Given a frequency vector \(p=(p_0,\ldots,p_7)\) of nonnegative integers with \(\sum_jp_j=n\), define \(\eta_0(j;p)=j\) and recursively \(\eta_{t+1}(j;p)\) by updating each of its three bits using
\[
S_i(t;p)=\sum_{h=0}^{7}p_h b_i(\eta_t(h;p)),\qquad
h_{i,j}(t;p)=S_i(t;p)-b_i(\eta_t(j;p))+
\sum_{r\ne i}b_r(\eta_t(j;p)),
\]
\[
b_i(\eta_{t+1}(j;p))=
\begin{cases}
1,&2h_{i,j}(t;p)>n+1,\\
0,&2h_{i,j}(t;p)<n+1,\\
b_i(\eta_t(j;p)),&2h_{i,j}(t;p)=n+1.
\end{cases}
\]
Only the types with \(p_j>0\) are compared below. For \(t\ge0\), set
\[
R_t(n)=\sum_{\substack{p_0+\cdots+p_7=n\\p_j\ge0}}
\frac{n!}{\prod_{j=0}^7p_j!}
\prod_{j:p_j>0}[\eta_t(j;p)=\eta_{t+2}(j;p)],
\]
\[
Q_t(n)=\sum_{\substack{p_0+\cdots+p_7=n\\p_j\ge0}}
\frac{n!}{\prod_{j=0}^7p_j!}
\prod_{j:p_j>0}[\eta_t(j;p)=\eta_{t+1}(j;p)].
\]
Square brackets are indicator functions. Define \(R_{-1}(n)=Q_{-1}(n)=0\). The **exact numbers** of labelled initial configurations with first entry at time \(t\) and eventual least period \(1\) or \(2\) are respectively
\[
N_{1,t}(n)=Q_t(n)-Q_{t-1}(n),\qquad
N_{2,t}(n)=R_t(n)-R_{t-1}(n)-N_{1,t}(n).
\]
Only \(t\le3\) occurs for odd \(n\); only \(t\le4\) for even \(n\). This is an explicit \(\binom{n+7}{7}\)-term integer formula with a uniformly bounded number of updates per summand, rather than enumeration of \(2^{3n}\) labelled configurations. The number of distinct primitive two-cycle orbits is \(N_{2,0}(n)/2\).

For illustration, the nonzero pairs \((d,t):N_{d,t}\) for \(n=5\) are
\[
(1,0):88,\ (1,1):7000,\ (1,2):15600,\ (1,3):8280,\ (2,0):900,\ (2,1):900,
\]
whereas for \(n=6\) they are
\[
\begin{aligned}
&(1,0):28,\ (1,1):21096,\ (1,2):128580,\ (1,3):48420,\ (1,4):14040,\\
&(2,0):6960,\ (2,1):15300,\ (2,2):18000,\ (2,3):9720.
\end{aligned}
\]
Both totals equal \(2^{3n}\) at their respective orders.

## Assumptions and scope
The graph has three disjoint rows of \(n\) vertices; within each row all vertices are pairwise adjacent, and vertices in one column are pairwise adjacent. There are no other edges and no loops, so every degree is exactly \(n+1\). Columns are labelled. Time is measured in full simultaneous updates, starting at \(t=0\). The state alphabet is \(\{0,1\}\). If the neighbor count is tied, the vertex retains its current bit; this is essential when \(n\) is odd. No stochastic updating or asynchronous convention is assumed. The statement is for every \(n\ge2\), with small cases separated as above.

## Proof
**Exact column reduction.** Given any initial state, let \(p_j\) be the number of its columns of type \(j\). At time \(t\), columns that began with the same type have the same current three bits: all rows are permutation-symmetric in their column indices, and an individual vertex sees only its current row total and the other two bits of its column. The displayed recurrence follows by subtracting its own bit from the row total and adding the other two column bits. Induction proves this description is exact for every labelled initial state and every time. There are \(\binom{n+7}{7}\) possible frequency vectors; each has multiplicity \(n!/\prod p_j!\). Comparing the active types at times \(t,t+1,t+2\) gives the two displayed first-entry identities without approximation or overcounting.

**Uniform recurrence bound.** For arbitrary \(k\ge1\), introduce the eight symbolic counts \(p_j\ge0\), with sum \(2k+1\) or \(2k\). Introduce three bit variables for each of the eight initial types at each step. Constrain their values to be bits, their initial values to encode their types, and each subsequent update by the above exact threshold rule. The two complete Presburger queries `artifacts/odd_counterexample.smt2` and `artifacts/even_counterexample.smt2` assert, respectively, the existence of an active column whose state differs at times \(3\) and \(5\), or at times \(4\) and \(6\). Both queries were checked **unsatisfiable** by the exact integer-linear-arithmetic decision procedure implemented in Z3. Their generation, complete constraints and invocation are supplied in `scripts/verify_symbolic.py`. No bound on \(k\) or on \(p_j\) is imposed. Since the reduction covers every labelled configuration and the displayed formulas encode the true update, unsatisfiability establishes the two universal iterate identities and excludes longer eventual periods. This is a solver-assisted finite logical proof, not an extrapolation from finite state-space sampling.

**Sharpness.** Write the column types as integers \(0\) through \(7\) as in the statement, and record the types in three initially occupied groups in the order \((3,4,6)\). When \(n=2k+1\), take respective group multiplicities \((k,1,k)\). For every \(k\ge1\), their successive triples of types are
\[
(3,4,6)\to(6,2,7)\to(7,6,7)\to(7,7,7).
\]
The first periodic entry is at time three. When \(n=2k\) with \(k\ge3\), take multiplicities \((k-1,2,k-1)\); then the successive group triples are
\[
(3,4,6)\to(6,2,7)\to(7,6,6)\to(6,7,7)\to(7,7,7).
\]
This has first entry at time four. Every displayed transition follows directly from the row totals and the exact majority rule, with the inequalities valid in the indicated parameter ranges. Finally the complete labelled computations for \(n=2,4\) establish sharp entry times two and three, respectively. These witnesses and the universal upper bounds prove the claimed maximum exactly.

## Verification
From this directory run `python3 scripts/verify_symbolic.py artifacts` on a machine with a standard `libz3` installation. It regenerates both universal counterexample formulas and reports `unsat` for each; alternatively run `z3 -smt2 artifacts/odd_counterexample.smt2` and analogously for `even_counterexample.smt2`. These are unbounded Presburger statements, not finite experiments. `python3 scripts/count_profiles.py 2 3 4 5 6 7 8 9 10` evaluates the exact multilayer formulas. `python3 scripts/verify_direct.py` separately evolves all \(2^{3n}\) individually labelled states for \(2\le n\le6\), using a vertex-level implementation, and checks equality with the profile census; 299,584 labelled states were directly checked in total. Actual output appears in `artifacts/verification_results.txt`. All files referenced here are embedded in the accompanying record.

## Relationship to prior work
The Goles–Olivos period-two theorem establishes eventual periods dividing two for finite symmetric threshold networks; it does not give the size-independent sharp first-entry times here. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486, first submitted May 11, 2014) discuss majority dynamics and period two for finite and infinite graphs. Their inspected sections establish general convergence statements, not this exact three-row first-entry distribution. Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519, first submitted August 14, 2015) provide module-sensitive and general voting-time bounds, not this particular sharp \(3\)-versus-\(4\) parity law. A known two-row matched-clique calculation concerns \(K_2\square K_n\), a different adjacency graph with a different threshold response; its two-row exact counts neither give the eight-type three-row census nor the three-row four-update witnesses. Exact fixed-point and attraction counts for the isolated \(4\times4\) rook graph also do not imply the stated infinite-family parity law.

## Limitations
The sharp universal bound relies on a reproducible Presburger unsatisfiability check and on the correctness of the stated translation from column dynamics to linear-integer constraints. A hand-written case-by-case elimination of every constraint is not supplied; solver independence has not been established. The explicit census is a polynomial-size finite sum, not a simplified closed elementary expression for each layer. The result does not cover four or more rows, asynchronous updating, other tie rules or other majority thresholds. Historical priority cannot be guaranteed from the accessible literature and similarity searches alone; unindexed equivalent results may exist. No independent audit has been performed.

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1 (year-verified foundational source; exact release day not established).
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486, May 11, 2014, https://arxiv.org/abs/1405.2486 .
3. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519, August 14, 2015, https://arxiv.org/abs/1508.03519 .
