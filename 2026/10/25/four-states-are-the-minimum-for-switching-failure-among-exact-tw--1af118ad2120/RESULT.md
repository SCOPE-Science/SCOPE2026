# Four states are the minimum for switching failure among exact two-step mixers

## Finding

For an integer \(n\ge 1\), let \(J_n\) be the \(n\times n\) matrix with every entry equal to \(1/n\), and define
\[
\mathcal K_n=\{P\in[0,1]^{n\times n}:P\mathbf1=\mathbf1,\ P^2=J_n\}.
\]
Every member of \(\mathcal K_n\) has the uniform stationary distribution and reaches that distribution from every state **by its second step**. The following is a sharp dimension boundary for time-inhomogeneous switching:

**Theorem.** If \(n\le3\), there exists a constant \(\rho_n<1\), depending only on \(n\), such that for *every* sequence \(P_1,P_2,\ldots\) drawn from \(\mathcal K_n\), every initial law \(\mu\), and every integer \(t\ge1\),
\[
d_{\mathrm{TV}}(\mu P_1\cdots P_t,\pi_n)
\le \rho_n^t d_{\mathrm{TV}}(\mu,\pi_n),
\]
where \(\pi_n=(1/n,\ldots,1/n)\).

In contrast, when \(n=4\) there are two matrices \(P,Q\in\mathcal K_4\), with \(Q=P^{\mathsf T}\), such that alternating them never approaches uniformity. More sharply, for every \(0\le\varepsilon\le1\) there are kernels \(P_\varepsilon,Q_\varepsilon\in\mathcal K_4\), strictly positive when \(\varepsilon>0\), whose alternating product \(K_t\) of length \(t\ge1\) satisfies
\[
\max_{x\in\{1,2,3,4\}}
d_{\mathrm{TV}}(e_xK_t,\pi_4)
=\frac{(1-\varepsilon)^t}{2},
\qquad
\max_{x,y}\left|\frac{K_t(x,y)}{\pi_4(y)}-1\right|
=(1-\varepsilon)^t.
\]
The same formulas hold for either starting phase of the alternating sequence. At \(\varepsilon=0\), its total-variation distance stays equal to \(1/2\) for all positive times, while the two fixed kernels still individually mix perfectly in two steps. At every \(0<\varepsilon<1\), the alternating chain mixes but can be arbitrarily slow as \(\varepsilon\downarrow0\).

## Assumptions and scope

All matrices are row-stochastic, act on row probability distributions, and have nonnegative real entries. Switching is deterministic but arbitrary in the small-dimensional conclusion, and strictly alternating in the four-state construction. The result does **not** assert a positive dimension-independent contraction factor for every collection of nonreversible chains; the contraction factor for \(n\le3\) is a compactness constant for the precise condition \(P^2=J_n\). For the explicit family the parameter \(\varepsilon\) lies in \([0,1]\).

## Proof

**Uniform stationarity.** Fix \(P\in\mathcal K_n\). Because \(P\mathbf1=\mathbf1\), multiplication on the right by \(J_n\) gives \(PJ_n=J_n\). The identity \(P^2=J_n\) implies \(P^3=PJ_n=J_n\), but also \(P^3=J_nP\). Consequently \(J_nP=J_n\). Thus \(P\) is doubly stochastic and preserves \(\pi_n\).

**No deterministic row.** Suppose \(n\ge2\) and row \(r\) of a member \(P\in\mathcal K_n\) places all mass on a single state \(i\). Then row \(r\) of \(P^2\) equals row \(i\) of \(P\), so row \(i\) must equal the uniform row \(\pi_n\). If \(i=r\), this contradicts the deterministic row. If \(i\ne r\), the double-stochasticity proved above forces \(P_{ii}=0\), since column \(i\) already receives mass one from row \(r\). This again contradicts the uniform row \(i\). Therefore every row of \(P\) has at least two positive entries.

**Contraction in at most three states.** For any row-stochastic \(P\) write its Dobrushin coefficient as
\[
\delta(P)=\max_{r,s}d_{\mathrm{TV}}(e_rP,e_sP)
=1-\min_{r,s}\sum_j\min(P_{rj},P_{sj}).
\]
When \(n=2\) or \(3\), any two supports of size at least two intersect. Therefore \(\delta(P)<1\) for every \(P\in\mathcal K_n\). The set \(\mathcal K_n\) is nonempty (it contains \(J_n\)) and compact: its defining inequalities and polynomial equations are closed in the compact cube. Continuity of \(\delta\) gives
\[
\rho_n:=\max_{P\in\mathcal K_n}\delta(P)<1.
\]
The standard Dobrushin contraction inequality, proved by writing a signed mass-zero measure as its positive and negative parts and coupling their mixture rows, gives \(d_{\mathrm{TV}}(\alpha P,\beta P)\le\delta(P)d_{\mathrm{TV}}(\alpha,\beta)\). Apply this inequality successively, using \(\pi_nP_j=\pi_n\). For \(n=1\), every law is already uniform and the displayed bound holds with \(\rho_1=0\). This proves the claimed universal switched convergence for \(n\le3\).

**Explicit four-state obstruction.** Label four states by ordered bits \((a,b)\in\{0,1\}^2\), in lexicographic order. Let \(P\) update \((a,b)\) to \((b,U)\), where \(U\) is an independent fair bit. Let \(Q=P^{\mathsf T}\), which updates \((a,b)\) to \((U,a)\). Explicitly,
\[
P=\frac12\begin{pmatrix}
1&1&0&0\\
0&0&1&1\\
1&1&0&0\\
0&0&1&1
\end{pmatrix},\qquad Q=P^{\mathsf T}.
\]
Two successive forward shifts discard both original bits; likewise for two reverse shifts. Hence \(P^2=Q^2=J_4\). But a forward shift followed by a reverse shift leaves the original **second** bit unchanged: \(PQ\) maps \((a,b)\) to \((V,b)\) for a new fair bit \(V\). Put \(R=PQ\). Then \(R^2=R\ne J_4\), and every row of \(R\) is uniform on two states, so its total-variation distance to \(\pi_4\) is exactly \(1/2\). Moreover \(RP\) maps \((a,b)\) to \((b,V)\) and has the same two-point-uniform row property.

**Positive perturbation and exact profile.** Let \(d=1-\varepsilon\) and set
\[
P_\varepsilon=dP+(1-d)J_4,\qquad
Q_\varepsilon=dQ+(1-d)J_4.
\]
Because \(PJ_4=J_4P=QJ_4=J_4Q=J_4\), both squares equal \(J_4\) identically; all entries are at least \(\varepsilon/4\). Direct multiplication gives
\[
P_\varepsilon Q_\varepsilon=J_4+d^2(R-J_4).
\]
Since \(R^2=R\) and \(RJ_4=J_4R=J_4\), induction yields
\[
(P_\varepsilon Q_\varepsilon)^m=J_4+d^{2m}(R-J_4)
\quad(m\ge1),
\]
and
\[
(P_\varepsilon Q_\varepsilon)^m P_\varepsilon
=J_4+d^{2m+1}(RP-J_4)
\quad(m\ge0).
\]
The row distributions of both \(R\) and \(RP\), as well as \(P\), are uniform on two of the four states. For a row \(v\) of any of these matrices, \(d_{\mathrm{TV}}(\pi_4+d^t(v-\pi_4),\pi_4)=d^t/2\). The maximal relative entrywise discrepancy is \(d^t\). This proves both exact formulas; transpose symmetry supplies the reversed starting phase. In particular, \(\varepsilon=0\) does not mix at any positive time. Thus dimension four is minimal.

## Verification

The accompanying standard-library script `verify.py` checks the four-state matrices and their squares using exact rational arithmetic, checks both switching phases for seven rational perturbation parameters and twenty time steps, and tests the claimed total-variation and relative entrywise profiles in every case. It additionally exhausts all three-state doubly stochastic rational grids with denominator at most six that satisfy \(P^2=J_3\), and checks strict Euclidean contraction for those instances. Its expected success markers are `EXACT_FOUR_STATE_ALGEBRA_PASS`, `THREE_STATE_FINITE_GRID_PASS`, and `VERIFY_OK`. The finite rational grid is a diagnostic only: the all-real, all-switching, all-time conclusions follow from the analytic arguments above.

## Relationship to prior work

Shimizu and Shiraga establish dynamic random-walk mixing results for reversible kernels sharing a stationary measure; their assumptions exclude the nonreversible matrices here. The result above identifies a sharp four-state failure when reversibility is replaced by the seemingly stronger requirement that each fixed kernel reaches its stationary distribution *by* two steps. Chevalier, Gusev, Hendrickx, and Jungers investigate products of stochastic matrices, SIA-type convergence, and combinatorial index bounds, but those results do not provide this minimal-size, finite-time-mixing witness or its exact positive-perturbation profile. Classical constructions of nondiagonalizable doubly stochastic matrices, including a three-state square-root-of-uniform example, already exhibit nilpotent centered dynamics for a fixed kernel; existence of such fixed-kernel roots is not claimed as new. The specific sharp switchability boundary and positive-perturbation dependence law are the contribution considered here.

## Limitations

The claim is for exact static two-step mixing, not all fast-mixing kernels. It does not imply that a switch among arbitrary nonreversible chains diverges, nor does it classify higher-dimensional square roots of \(J_n\). The four-state example is an explicit deterministic periodic switch rather than an arbitrary-switch classification in dimension four. The algebra of products of nilpotent centered operators is classical; the possibility of an earlier, equivalent formulation of this sharp stochastic dimension boundary is a residual bibliographic risk. No independent scientific validation is claimed.

## References

- Nobutaka Shimizu and Takeharu Shiraga, *Reversible Random Walks on Dynamic Graphs*, first public preprint 2021-02-16, https://arxiv.org/abs/2102.08002.
- Pierre-Yves Chevalier, Vladimir Gusev, Julien M. Hendrickx, Raphaël M. Jungers, *Sets of Stochastic Matrices with Converging Products: Bounds and Complexity*, first public preprint 2017-12-07, https://arxiv.org/abs/1712.02614.
- Apostolos Vourdas, *Markov chains with doubly stochastic transition matrices and application to a sequence of non-selective quantum measurements*, https://arxiv.org/abs/2203.09468.
- David E. Speyer, answer to *Non-diagonalizable doubly stochastic matrices*, 2011-01-13, https://mathoverflow.net/questions/51887/non-diagonalizable-doubly-stochastic-matrices.
