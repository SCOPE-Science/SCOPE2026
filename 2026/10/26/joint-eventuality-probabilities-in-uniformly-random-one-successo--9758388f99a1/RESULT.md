# Joint eventuality probabilities in uniformly random one-successor Kripke frames

## Finding

In a uniformly random deterministic transition system on \(n\) states, the probability that **every state** eventually reaches each of \(r\) independent atomic labels has an exact finite-size exponential generating function and a simple, generally nonzero limit. For two independent labels it is a strictly increasing function of the state count, despite each single-label eventuality having size-independent probability.

Fix \(r\ge1\), \(n\ge1\), and \(0<p_j<1\). Put
\[
 a_J=\prod_{j\in J}(1-p_j),\qquad T(z)=\sum_{k\ge1}\frac{k^{k-1}}{k!}z^k,\quad T(z)=ze^{T(z)}.
\]
For the event \(L_n\) defined below,
\[
 \Pr(L_n)=\frac{n!}{n^n}[z^n]\frac1{1-T(z)}
 \prod_{\varnothing\ne J\subseteq[r]}(1-a_JT(z))^{(-1)^{|J|+1}},
\]
\[
 \lim_{n\to\infty}\Pr(L_n)
 =\prod_{\varnothing\ne J\subseteq[r]}(1-a_J)^{(-1)^{|J|+1}}.
\]
When \(r=1\), \(\Pr(L_n)=p_1\) for every \(n\). For \(r=2\), write \(p=p_1\), \(q=p_2\), \(c=(1-p)(1-q)\), and \(\lambda=pq/(p+q-pq)\). Then
\[
 \Pr(L_n)=\lambda\left(1-\sum_{k=1}^n\frac{k}{n}\frac{(n)_k}{n^k}c^k\right),
 \qquad \Pr(L_1)=pq,
\]
and this probability **strictly increases** with \(n\) to \(\lambda\). The limit \(\lambda\) exceeds \(pq\) whenever \(p,q\in(0,1)\).

## Assumptions and scope

The state set is \([n]\). Choose independently and uniformly \(f(v)\in[n]\) for each state \(v\), permitting fixed points. The directed transition relation is precisely \(v\to f(v)\). All states are considered initial, so validity means satisfaction at every state. Independently of \(f\), label each \(v\) by propositions \(P_1,\ldots,P_r\), with independent Bernoulli incidences of fixed probabilities \(p_j\). The usual CTL \(\mathrm{AF}\,P_j\) means that on every infinite trajectory, some state eventually satisfies \(P_j\); the current state may satisfy it. Define
\[
 L_n=\{\forall v\in[n]\ \forall j\in[r]: v\models\mathrm{AF}\,P_j\}.
\]
There is one infinite path from each state. Because a finite functional digraph decomposes into directed cycles with in-arborescences, \(L_n\) holds **if and only if every directed cycle contains at least one marked vertex of each of the \(r\) proposition types**. The statement does not apply to independently sampled directed edges or arbitrary nondeterministic branching.

## Proof

**Weighted-cycle count.** A functional digraph is a set of disjoint connected components, each a directed cycle of rooted labelled trees. The tree EGF is \(T(z)=ze^{T(z)}\). A component whose cycle has length \(\ell\) contributes \(T(z)^\ell/\ell\). Conditional on its distinct cycle vertices, the probability that this cycle carries all \(r\) labels is
\[
 w_\ell=\prod_{j=1}^r\bigl(1-(1-p_j)^\ell\bigr).
\]
Tree-vertex labels integrate to probability one and do not affect the event. Therefore the probability-weighted EGF of accepted mappings is
\[
 F(z)=\exp\left(\sum_{\ell\ge1}\frac{w_\ell}{\ell}T(z)^\ell\right).
\]
Inclusion-exclusion gives \(w_\ell=\sum_{J\subseteq[r]}(-1)^{|J|}a_J^\ell\), with \(a_\varnothing=1\). Using \(\sum_{\ell\ge1}u^\ell/\ell=-\log(1-u)\), this reduces to the claimed product formula. There are \(n^n\) total mappings, while their EGF is \(1/(1-T(z))\), proving the finite formula.

**Limit.** Let \(C_{\ell,n}\) count directed cycles of length \(\ell\) in the random mapping. For fixed distinct positive integers \(\ell_1,\ldots,\ell_s\) and fixed nonnegative integers \(m_1,\ldots,m_s\), directly counting ordered disjoint cycles yields
\[
 \mathbb E\prod_i(C_{\ell_i,n})_{m_i}
 =\frac{(n)_{\sum_i\ell_i m_i}}{n^{\sum_i\ell_i m_i}\prod_i\ell_i^{m_i}}
 \longrightarrow \prod_i\ell_i^{-m_i},
\]
where the falling factorial \((x)_m\) counts ordered choices. Hence any finite family of cycle counts converges to independent Poisson variables with respective means \(1/\ell\). For cycles longer than \(L\), the expected number that fail at least one label is at most
\[
 \sum_{\ell>L}\frac1\ell\sum_j(1-p_j)^\ell,
\]
since \(\mathbb EC_{\ell,n}=(n)_\ell/(\ell n^\ell)\le1/\ell\). This tends to zero uniformly in \(n\), justifying passage from finitely many cycles to all cycles. Therefore
\[
 \Pr(L_n)\longrightarrow\exp\left(\sum_{\ell\ge1}\frac{w_\ell-1}{\ell}\right).
\]
The series is absolutely convergent and inclusion-exclusion of its geometric series logarithms yields exactly the stated finite product over nonempty subsets \(J\).

**One and two labels.** With \(r=1\), \(F(z)=(1-(1-p_1)T(z))/(1-T(z))\); for every positive coefficient index the numerator removes a fraction \(1-p_1\) of the total, proving \(\Pr(L_n)=p_1\) exactly. With \(r=2\), put \(a=1-p\), \(b=1-q\), \(c=ab\), and \(\lambda=pq/(1-c)\). An exact partial-fraction identity gives
\[
 F(z)=\frac{(1-aT(z))(1-bT(z))}{(1-T(z))(1-cT(z))}
 =1+\lambda\left(\frac1{1-T(z)}-\frac1{1-cT(z)}\right).
\]
The factor \(1/(1-cT(z))\) weights a functional mapping by \(c\) for every cyclic **vertex**, not for every component. For \(1\le k\le n\), a uniform mapping has exactly \(k\) cyclic vertices with probability
\[
 \Pr(K_n=k)=\frac{k}{n}\frac{(n)_k}{n^k}.
\]
Indeed choose the cyclic vertex set, choose a permutation of those vertices, and attach all other vertices by a rooted forest leading to that set (or, equivalently, count the first-repeat time of the trajectory starting at a designated state). This identifies the ratio of the \(z^n\) coefficients of \(1/(1-cT)\) and \(1/(1-T)\) with \(\mathbb E[c^{K_n}]\), proving the exact two-label formula. For each fixed \(k\ge2\),
\[
 \Pr(K_n\ge k)=\frac{(n)_k}{n^k}
 =\prod_{i=0}^{k-1}\left(1-\frac{i}{n}\right)
\]
is strictly increasing with \(n\) for \(n\ge k\); hence \(K_n\) is strictly stochastically increasing with the size parameter. Since \(0<c<1\), \(\mathbb E[c^{K_n}]\) strictly decreases. Moreover \(K_n\to\infty\) in probability (each fixed finite threshold eventually has survival probability one), so \(\mathbb E[c^{K_n}]\to0\). Thus the two-label success probability increases strictly to \(\lambda\), while \(K_1=1\) gives \(\Pr(L_1)=\lambda(1-c)=pq\).

## Verification

The accompanying standalone Python 3 file `verify_joint_liveness.py` independently enumerates every successor map and every Boolean atomic valuation for two proposition types through four states, and three proposition types through three states. It compares direct cycle-based CTL satisfaction against the finite generating-function coefficient and a second mapping-first probability calculation, using rational arithmetic. Additional exact comparisons test the two-event cyclic-vertex/birthday formula through eight states and the single-label identity through six states. Run `python3 verify_joint_liveness.py`. Expected final marker: `JOINT_RANDOM_MAPPING_LIVENESS_OK`. These finite checks do not certify infinite convergence; the probabilistic proof above does.

## Relationship to prior work

Lopuhaä-Zwakenberg (arXiv:2607.15029, first public July 16, 2026) studies 0–1 and convergence laws for CTL/LTL on independent-edge random transition systems with typical outdegree on the order of \(\log n\), rather than the outdegree-exactly-one distribution used here. Dong, Lopuhaä-Zwakenberg and Stoelinga (2025) similarly analyze independent-edge Kripke systems; their accessible abstract does not furnish these functional-digraph formulas. Flajolet and Odlyzko's *Random Mapping Statistics* supplies the classical mapping/labelled-tree generating-function methodology; that general methodology and the single-label identity are not claimed as novel. The proposed contribution is the precise **joint temporal-liveness** model, its multi-label probability law, and the strict finite-size two-event interpolation. The general weighted-cycle method could imply some formulas by specialization, and no absolute historical priority is asserted.

## Limitations

All labels are independent Bernoulli assignments with fixed probabilities strictly between zero and one, and there is exactly one randomly and independently chosen successor at each state. The strict size monotonicity is proved for exactly two labels; no such assertion is made for three or more. The source model and its formulas are different from the independent-edge models in the motivating literature. Classical cycle-index enumeration potentially subsumes portions of the calculation, and older random-mapping literature was not fully inspected. A self-review does not constitute an independent mathematical audit.

## References

1. M. Lopuhaä-Zwakenberg, *Towards realistic large random models of labeled transition systems and their 0-1 laws*, arXiv:2607.15029 (first submitted July 16, 2026), https://arxiv.org/abs/2607.15029.
2. Y. Dong, M. Lopuhaä-Zwakenberg, and M. Stoelinga, *0-1 Laws for LTL and CTL over Random Transition Systems*, SPIN 2025, DOI 10.1007/978-3-032-06847-7_4.
3. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, EUROCRYPT 1989, Lecture Notes in Computer Science 434, pp. 329–354 (1990), DOI 10.1007/3-540-46885-4_34.
