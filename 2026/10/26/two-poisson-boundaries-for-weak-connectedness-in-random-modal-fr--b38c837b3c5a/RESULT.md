# Two Poisson boundaries for weak connectedness in random modal frames

## Finding

Let \(F_n=(W_n,R_n)\) be a loop-free directed Kripke frame with \(W_n=\{1,\ldots,n\}\). Each of its \(n(n-1)\) possible directed edges is independently present with probability \(p_n\in[0,1]\). Consider the modal formula
\[
\chi=(\Diamond p\land\Diamond q)\to
\bigl(\Diamond(p\land q)\lor\Diamond(p\land\Diamond q)\lor\Diamond(q\land\Diamond p)\bigr).
\]
Write \(V_n=\Pr(F_n\models\chi)\), where validity quantifies over all worlds and valuations. The following three regimes give the complete two-ended threshold diagram:

**Sparse window.** If \(n^{3/2}p_n\to c\in[0,\infty)\), then
\[
V_n\longrightarrow \exp(-c^2/2).
\]
The number of vertices having at least two outneighbors converges to \(\operatorname{Poisson}(c^2/2)\). With probability tending to one, every vertex of this kind witnesses a failure of \(\chi\).

**Dense window.** If \(n(1-p_n)\to c\in[0,\infty)\), then
\[
V_n\longrightarrow\exp(-c^2/2).
\]
The number of unordered vertex pairs lacking both possible connecting arcs converges to \(\operatorname{Poisson}(c^2/2)\). With probability tending to one, each such pair has a common predecessor and witnesses a failure.

**Intermediate region.** If \(n^{3/2}p_n\to\infty\) and \(n(1-p_n)\to\infty\), then \(V_n\to0\). Thus global validity is typical at the near-empty and near-complete ends but atypical throughout their intervening range. The different powers in the two critical scalings reflect clustering of many failing forks around one mutually nonadjacent successor pair near completeness.

## Assumptions and scope

Only finite **loop-free**, labelled directed frames sampled by independent Bernoulli arcs are considered. The arbitrary valuations in \(F_n\models\chi\) are not sampled. No transitivity, reflexivity, seriality, or symmetry is assumed. All limits are along integer \(n\to\infty\); the constant \(c\) is finite and nonnegative. The two probabilities are probabilities over frames, not satisfiability probabilities of randomly chosen formulas.

Define the weak-connectedness property \(\mathrm{WC}\) by
\[
\forall w,u,v:\quad (wRu\land wRv\land u\ne v)\Longrightarrow(uRv\lor vRu).
\]
It requires every outneighborhood to induce a semicomplete digraph. Its failure consists of a fork \((w;u,v)\) with two present arcs from \(w\) and both connecting arcs between \(u,v\) absent.

## Proof

**Modal correspondence.** If \(\mathrm{WC}\) holds and \(w\models\Diamond p\land\Diamond q\), choose successors \(u\models p\), \(v\models q\). If \(u=v\), the first disjunct in the consequent holds. If \(uRv\) or \(vRu\), respectively the second or third disjunct holds. Conversely, if \(wRu,wRv\) but neither connecting arc exists for distinct \(u,v\), give \(p\) the singleton extension \(\{u\}\) and \(q\) the singleton extension \(\{v\}\). The antecedent holds and each disjunct fails. Hence \(F_n\models\chi\) exactly when \(\mathrm{WC}\) holds.

**Sparse window.** Let \(D_w\) denote the outdegree of \(w\), and let \(S_n=\sum_w\mathbf1_{\{D_w\ge2\}}\). Since outgoing rows contain disjoint independent arcs, the indicators are independent. If \(n^{3/2}p_n\to c\), then \(np_n\to0\) and
\[
\Pr(D_w\ge2)=\binom{n-1}{2}p_n^2+O((np_n)^3),\qquad n\Pr(D_w\ge2)\longrightarrow c^2/2.
\]
The binomial-to-Poisson theorem gives \(S_n\Rightarrow\operatorname{Poisson}(c^2/2)\). A pair of successors \(u,v\) can fail to witness \(\mathrm{WC}\) only if at least one connecting arc is present. The expected number of such comparable forks is exactly
\[
n\binom{n-1}{2}p_n^2(2p_n-p_n^2)=O(n^3p_n^3)=o(1).
\]
By Markov's inequality, no such fork exists with probability tending to one. Thus \(F_n\models\chi\) iff \(S_n=0\), apart from an event of probability \(o(1)\). This proves the first Poisson window, including \(c=0\).

**Dense window.** Put \(q_n=1-p_n\) and let \(T_n\) count unordered pairs \(\{u,v\}\) for which neither \(uRv\) nor \(vRu\). These disjoint unordered dyads are independent, so
\[
T_n\sim\operatorname{Binomial}\left(\binom n2,q_n^2\right).
\]
If \(nq_n\to c\), then \(T_n\Rightarrow\operatorname{Poisson}(c^2/2)\). Conditional on any missing dyad, there is no common predecessor among the other \(n-2\) vertices with probability \((1-p_n^2)^{n-2}\). Hence the expected number of missing dyads without a common predecessor is
\[
\binom n2 q_n^2(1-p_n^2)^{n-2}=o(1).
\]
Almost surely every missing dyad supplies a forbidden fork, so \(F_n\models\chi\) iff \(T_n=0\) with probability \(1-o(1)\).

**Intermediate region.** Assume \(n^3p_n^2\to\infty\) and \(n^2(1-p_n)^2\to\infty\). Let \(Y_n=\sum_w\binom{D_w}{2}\). Writing \(m=n-1\), independence of outgoing rows gives
\[
\mathbb EY_n=n\binom m2p_n^2,
\quad
\operatorname{Var}Y_n=n\left[\binom m2(p_n^2-p_n^4)+6\binom m3(p_n^3-p_n^4)\right].
\]
Thus \(\operatorname{Var}(Y_n)/(\mathbb EY_n)^2\to0\), since this ratio is \(O((n^3p_n^2)^{-1}+(n^2p_n)^{-1})\), with \(n^2p_n\to\infty\). Let \(C_n\) count the forks in \(Y_n\) for which at least one connecting arc is present. Then
\[
\mathbb EC_n=(2p_n-p_n^2)\mathbb EY_n.
\]
If \(p_n<\varepsilon\), Chebyshev and Markov yield
\[
\Pr(F_n\models\chi)\le\Pr(Y_n<\tfrac12\mathbb EY_n)+\Pr(C_n\ge\tfrac12\mathbb EY_n)
=o(1)+4\varepsilon,
\]
uniformly for any fixed \(\varepsilon>0\).

If \(p_n\ge\varepsilon\), use the missing-dyad count \(T_n\) above. Its mean is \(\binom n2(1-p_n)^2\to\infty\), so \(\Pr(T_n=0)\to0\). The probability that *any* missing dyad has no common predecessor is bounded by
\[
\binom n2(1-p_n)^2(1-p_n^2)^{n-2}\le n^2 e^{-\varepsilon^2(n-2)}\to0.
\]
Therefore \(\Pr(F_n\models\chi)=o(1)\) in this range. Taking \(\limsup\) and then \(\varepsilon\downarrow0\) proves the intermediate result without imposing monotonicity on \(p_n\).

## Verification

The accompanying standalone `verify.py` checks the exact frame correspondence by independently evaluating the modal formula under **all** valuations of two propositional variables. It enumerates all \(2^{n(n-1)}\) loop-free directed frames for each \(n=1,2,3,4\). The valid-frame totals are, respectively, \(1,4,52,1907\), out of \(1,4,64,4096\). The full coefficients by edge count are printed by the checker. This finite verification tests correspondence, not the infinite Poisson limits, which follow from the proof above.

## Relationship to prior work

Weak connectedness, its first-order correspondent, and its relationship to modal linearity and the logics \(\mathsf{K4.3}\) and \(\mathsf{S4.3}\) are classical; they are not claimed as new. In particular, the Kikot--Kurucz--Tanaka--Wolter--Zakharyaschev treatment explicitly writes the weak-connectedness condition and analyzes its positive-modal definability. Santschi--Vooijs (2026) develops finite-width and finite-model methods in weakly transitive modal logic; it does not present this independent-arc random-frame phase diagram. Bang-Jensen (1990) defines locally semicomplete digraphs, imposing semicompleteness on both out- and inneighborhoods, which is stronger than the one-sided condition considered here. Erdős--Palmer--Robinson (1983) studies local connectivity in undirected random graphs, a different neighborhood property with a logarithmic threshold. The contribution here is the complete probability phase diagram for modal weak connectedness, including its two distinct Poisson scales and shared limiting function. General Poisson approximation methods are standard and are not claimed as novel.

## Limitations

The assertion is confined to loop-free directed independent-edge frames. It does **not** describe the distribution on transitive or reflexive frames of \(\mathsf{K4.3}\) or \(\mathsf{S4.3}\). An analogous two-sided law for the stronger graph-theoretic condition requiring *both* out- and inneighborhoods to be semicomplete is not proved. General theories of rare forbidden induced patterns may cover individual limiting arguments; complete historical priority of the combined modal-phase statement has not been established. No independent audit has been performed.

## References

1. Santschi, S. and Vooijs, N. (2026), *Logics Containing wK4: Selection à la Fine*, arXiv:2606.31920, initial release 2026-06-30, https://arxiv.org/abs/2606.31920 .
2. Kikot, S., Kurucz, A., Tanaka, Y., Wolter, F., and Zakharyaschev, M., *Kripke Completeness of Strictly Positive Modal Logics over Meet-Semilattices with Operators*, Section 9, https://intranet.csc.liv.ac.uk/~frank/publ/EL-JSL-final.pdf .
3. Bang-Jensen, J. (1990), *Locally semicomplete digraphs: A generalization of tournaments*, Journal of Graph Theory 14, 371--390, https://doi.org/10.1002/jgt.3190140310 .
4. Erdős, P., Palmer, E. M., and Robinson, R. W. (1983), *Local connectivity of a random graph*, Journal of Graph Theory 7, 411--417, https://doi.org/10.1002/jgt.3190070405 .
