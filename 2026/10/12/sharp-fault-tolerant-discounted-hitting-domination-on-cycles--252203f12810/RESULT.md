# Sharp fault-tolerant discounted hitting domination on cycles

## Finding

Let \(C_n\) be the simple cycle on \(n\ge 3\) labeled vertices, let \(0<\lambda<1\), \(0<\tau\le 1\), and fix an integer \(1\le f\le n-1\). For a nonempty source set \(S\), let \(T_S\) be the first hitting time of \(S\) by the simple random walk and put
\[
h_v(S)=\mathbb E_v[\lambda^{T_S}],\qquad v\in V(C_n).
\]
Define \(\delta^{[f]}_{\lambda,\tau}(C_n)\) as the minimum \(|S|\), over sets with \(|S|\ge f+1\), for which \(\min_v h_v(S\setminus F)\ge\tau\) for **every** \(f\)-element subset \(F\subseteq S\). Set the value to \(+\infty\) if no such set exists. Thus a failed source ceases to be a source but its vertex and incident edges remain in the graph.

Put \(\theta=\operatorname{arcosh}(1/\lambda)>0\), and, for every integer \(g\ge1\), define
\[
\psi_1=1,\qquad
\psi_g=\begin{cases}
1/\cosh(g\theta/2),&g\text{ even},\\
\cosh(\theta/2)/\cosh(g\theta/2),&g\text{ odd}.
\end{cases}
\]
The numbers \(\psi_g\) strictly decrease to zero. Consequently
\[
L=L(\lambda,\tau)=\max\{g\ge1:\psi_g\ge\tau\}
\]
is a well-defined positive integer. The **complete fault-tolerance formula** is
\[
\boxed{\displaystyle
\delta^{[f]}_{\lambda,\tau}(C_n)=
\begin{cases}
+\infty,&L\le f,\\
\max\bigl\{f+1,\lceil (f+1)n/L\rceil\bigr\},&L\ge f+1.
\end{cases}}
\]
In particular, feasibility has the sharp threshold \(\tau\le\psi_{f+1}\). For one failed source this reads \(\tau\le\lambda\), since \(\psi_2=\lambda\).

The formula comes with a characterization of **all** feasible and optimal sets. If \(S\) has \(k\ge f+1\) vertices in cyclic order, and \(g_1,\ldots,g_k\ge1\) are the intervening numbers of edges (so \(\sum_i g_i=n\)), then \(S\) survives every \(f\)-source failure if and only if
\[
\sum_{j=0}^{f}g_{i+j}\le L\quad\text{for every }i,
\]
where subscripts on the gaps are read modulo \(k\). The optimal sets are exactly those satisfying these inequalities with \(k=\delta^{[f]}_{\lambda,\tau}(C_n)\), whenever the latter is finite.

There is also an **exact labeled optimum-count formula**. Suppose \(L\ge f+1\), put \(k=\delta^{[f]}_{\lambda,\tau}(C_n)\), and form the finite state set
\[
\mathcal Q_{L,f}=\{(a_1,\ldots,a_f)\in\mathbb Z_{>0}^f:\ a_1+\cdots+a_f\le L-1\}.
\]
The matrix \(M_{L,f}(z)\), indexed by this set, has entry \(z^{a_1}\) from \((a_1,\ldots,a_f)\) to \((a_2,\ldots,a_f,b)\) exactly when \(a_1+\cdots+a_f+b\le L\), and entry zero otherwise. If \(\mathfrak N_{n,f}(\lambda,\tau)\) denotes the number of labeled minimum robust source sets, then
\[
\boxed{\displaystyle
\mathfrak N_{n,f}(\lambda,\tau)
=\frac nk[z^n]\operatorname{tr}\!\bigl(M_{L,f}(z)^k\bigr).}
\]
Equivalently, the trace coefficient counts ordered cyclic compositions \(g_1+\cdots+g_k=n\) satisfying the \((f+1)\)-gap constraints. When \(L\ge n\), all \(\binom{n}{f+1}\) subsets of size \(f+1\) are optimal; when \(L=f+1\), the entire vertex set is the unique robust set.

## Assumptions and scope

The graph is the undirected simple cycle, the walk chooses either neighbor with probability \(1/2\), fidelity is homogeneous, and the floor is imposed at **every** vertex after each adversarial removal of exactly \(f\) original sources. Only the source status fails: the underlying edges and the random-walk transition matrix are unchanged. Both parameters \(\lambda\) and \(\tau\) may be arbitrary real numbers in their stated ranges; no rationality hypothesis is needed for the proof. For a finite labeled cycle the counting formula counts subsets of the fixed labeled vertex set, not rotational equivalence classes. The result does not cover edge failures, simultaneous graph damage, arbitrary graphs, or heterogeneous fidelity.

## Proof

**1. The pinned segment.** Let two consecutive surviving sources bound a directed arc of \(g\) edges, at positions \(0,g\). Both endpoints have potential one. At each interior vertex the first-step equation is
\[
u_i=\frac\lambda2(u_{i-1}+u_{i+1}),\qquad u_0=u_g=1.
\]
Its unique solution is
\[
u_i=\frac{\cosh\bigl(\theta(i-g/2)\bigr)}{\cosh(g\theta/2)}.
\]
The displayed expression satisfies the recurrence because \(\lambda\cosh\theta=1\). Uniqueness follows directly: the interior linear operator is a strict contraction in the sup norm since \(0<\lambda<1\). The minimum along the arc is attained at its middle position(s), and equals \(\psi_g\); for \(g=1\) both vertices are sources, giving \(\psi_1=1\). The formula also applies when there is only one surviving source: the whole cycle is an arc of length \(n\) whose two endpoint labels represent the same pinned vertex.

The strict decrease of \(\psi_g\) follows, for example, from
\[
\psi_{2r-1}>\psi_{2r}>\psi_{2r+1}\quad(r\ge1),
\]
which is obtained by expanding the products of hyperbolic cosines using the addition identity. All terms tend to zero since \(\theta>0\). Hence an arc is feasible exactly when its edge length is at most \(L\). This segment criterion agrees with the ordinary two-boundary gap result in Allagan--Pereyra--Massey, Lemma 5.5; it is used here as an input to a different, failure-resilient optimization problem.

**2. The adversarial-window criterion.** Fix \(k=|S|\ge f+1\) and list the original gaps \(g_1,\ldots,g_k\) cyclically. Removing a run of \(r\) consecutive original sources merges \(r+1\) consecutive original gaps into one surviving-source arc. For any deletion of \(f\) sources, every newly formed arc therefore contains at most \(f+1\) consecutive original gaps. Positivity implies its length is no greater than that of an encompassing \((f+1)\)-gap window. Thus all \((f+1)\)-gap sums at most \(L\) are sufficient for robustness.

Conversely, take a particular \((f+1)\)-gap window. If \(k\ge f+2\), remove precisely the \(f\) original source vertices between its two endpoints. The resulting surviving arc is that window. If \(k=f+1\), remove all sources except the one at either endpoint: the sole surviving arc has length \(n\), exactly the sum of the window. Hence violation of any window inequality produces a failing deletion. This proves necessity, including the singleton-survivor boundary.

**3. Sharp cardinality and existence.** Write \(w=f+1\). Summing the \(k\) necessary window inequalities gives
\[
wn\le kL.
\]
Since \(k\ge w\), every robust set has
\[
k\ge\max\{w,\lceil wn/L\rceil\}.
\]
If \(L<w\), even the full vertex set fails after deleting \(f\) consecutive vertices, and deleting other original sources cannot improve support. Thus robustness is impossible.

Suppose \(L\ge w\) and take \(k=\max\{w,\lceil wn/L\rceil\}\). Then \(w\le k\le n\). Define a cyclic integer gap sequence by
\[
g_i=\left\lfloor\frac{(i+1)n}{k}\right\rfloor-\left\lfloor\frac{in}{k}\right\rfloor,
\qquad i=0,\ldots,k-1.
\]
Because \(n\ge k\), these gaps are positive and sum to \(n\). Extending the sequence periodically, every \(w\)-gap window has sum
\[
\left\lfloor\frac{(i+w)n}{k}\right\rfloor-\left\lfloor\frac{in}{k}\right\rfloor
\le\left\lceil\frac{wn}{k}\right\rceil\le L.
\]
Thus placing sources at the cumulative gap positions constructs a robust set attaining the lower bound. This proves the complete cardinality and feasibility formula and characterizes the optimal sets.

**4. Exact number of optimizers.** The allowed cyclic gap words are precisely the closed walks of length \(k\) in the finite state graph defining \(M_{L,f}(z)\): the state remembers the latest \(f\) gaps, and each transition checks their sum with the next gap. The transition weight records the first gap, so a closed walk's weight is \(z^{g_1+\cdots+g_k}\). The coefficient \([z^n]\operatorname{tr}(M_{L,f}(z)^k)\) therefore counts indexed cyclic gap words of total \(n\), including periodic ones with their correct multiplicity.

There are \(n\) choices of the first labeled source vertex for each indexed cyclic gap word, while each labeled source set of cardinality \(k\) occurs exactly \(k\) times in these rooted descriptions. Division by \(k\) gives the count formula. For \(L\ge n\) every \(w\)-element set survives because after failure a singleton source remains and its one arc has length \(n\); for \(L=w\), the lower bound forces \(k=n\).

## Verification

The standalone program `verify_faults.py` enumerates every nonempty source set of every labeled cycle of orders \(3\) through \(9\), using exact rational linear systems for \(\lambda\in\{1/2,2/3,4/5\}\). It tests every adversarial removal of \(f\) sources for \(f=1,2,3\) where admissible and also the extreme \(f=n-1\). The threshold set includes each rational gap boundary and interior midpoints, ensuring equality cases are checked. It verifies feasibility, the minimum cardinality, and the labeled-optimum count by independently enumerated cyclic compositions. The executed program reports 3,027 pinned systems, 57,345 failure cases, 948 threshold profiles, and 194,796 set-membership comparisons, all passing.

A second standalone program, `verify_transfer.py`, independently computes finite transfer-matrix traces and compares them with cyclic-composition coefficients across 374 parameter profiles (229 nonzero cases). These checks corroborate the algebra and boundary conventions; the proof above covers all permitted orders, failures, and real parameters without relying on finite enumeration.

Reproduce using `python3 verify_faults.py` and `python3 verify_transfer.py` with the standard Python library. The recorded outputs are in `faults_verification_output.txt` and `transfer_verification_output.txt`.

## Relationship to prior work

Allagan, Pereyra and Massey introduced discounted hitting domination as a minimax source-placement invariant. Their Lemma 5.5 obtains the two-pinned-source gap threshold \(L\), Sections 6 and 7 study spiders, stars, and complete graphs, and Section 9 explicitly identifies survival under removal of sources as a further direction. The segment potential and ordinary gap cutoff are **not** claimed as new here. The result above converts them into an exact all-\(f\) failure theorem for cycles: a cyclic-window characterization, sharp feasibility boundary, closed optimal cardinality, balanced construction, and transfer-matrix enumeration of all optimum labeled placements. General mixed-integer formulations for the no-failure problem do not imply the fault-resilient cyclic classification without further analysis.

Targeted comparisons of source failure, probabilistic hitting coverage, circular placement, cyclic window constraints, ordinary distance domination, and related published results found no covering statement. That negative search result is not a uniqueness proof. Earlier work on ordinary distance or weighted domination applies to different predicates; some special threshold regimes agree numerically but do not imply the full parameter-and-failure classification. Related published results about fragile power-domination placements concern a different process on multipartite graphs.

## Limitations

This result is a mathematical theorem with exact finite tests, not an independent external certification. Its novelty assessment is limited to the sources inspected and may miss unindexed equivalent work. The transfer matrix can grow quickly with the failure budget and allowable gap length; it is a finite exact count, not a uniform polynomial-time guarantee when these parameters vary. Failure removes source status only, not network vertices or transitions. The theorem makes no claim for heterogeneous fidelities, directed or irregular graphs, or an adversary that can alter the walk.

## References

1. J. D. Allagan, K. Pereyra, and W. A. Massey, *Discounted Hitting Domination on Graphs with Submodularity, Complexity and Exact Algorithms*, arXiv:2609.31535v1 (first public version September 25, 2026), especially Definition 2.5, Lemma 5.5, Sections 6–7 and 9. https://arxiv.org/abs/2609.31535
2. The same paper, Theorem 2.3, for the interpretation of pinned equilibria as discounted random-walk hitting potentials.
