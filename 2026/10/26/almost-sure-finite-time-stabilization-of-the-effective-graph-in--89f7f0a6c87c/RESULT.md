# Almost-sure finite-time stabilization of the effective graph in adaptive-confidence Deffuant–Weisbuch dynamics

## Finding

**Theorem.** In the adaptive-confidence Deffuant–Weisbuch (DW) model of Li, Luo, and Porter [1], on every finite simple undirected graph with at least one edge, for every fixed \(0<\mu\le 1/2\), \(0<\gamma\le 1\), \(0\le\delta<1\), and every deterministic initial opinion and common initial confidence state in the model's domain, the effective graph becomes exactly constant after an almost-surely finite random time. More precisely, writing

\[
E_{\mathrm{eff}}(t)=\{e=\{i,j\}\in E: |x_i(t)-x_j(t)|<c_e(t)\},
\]

there exists an almost-surely finite integer-valued random variable \(T\) such that, simultaneously for all \(t\ge T\),

\[
E_{\mathrm{eff}}(t)=E_\infty:=\{e\in E:\lim_{s\to\infty}c_e(s)=1\}.
\]

Equivalently, every edge with eventual confidence limit zero is receptive at only finitely many times, while every edge with confidence limit one is permanently receptive from some finite time onward. This conclusion applies even when the endpoints of a confidence-zero edge converge to **the same opinion**; distinct limit opinions are not required. Moreover, an edge belongs to \(E_\infty\) if and only if it is selected while receptive infinitely often.

## Assumptions and scope

Let \(G=(V,E)\) be any fixed finite, loopless, undirected graph with \(m=|E|\ge1\). At discrete time \(t\ge0\), the opinions satisfy \(x_i(t)\in[0,1]\), and every edge has confidence \(c_e(t)\in[0,1]\) with a common initial confidence \(c_e(0)=c_0\) satisfying \(0<c_0<1\). Independently of the past, select one edge \(U_t\) uniformly from \(E\). For its endpoints \(i,j\), define the pre-selection receptiveness indicator

\[
A_e(t)=\mathbf1\{|x_i(t)-x_j(t)|<c_e(t)\}.
\]

If \(A_{U_t}(t)=1\), replace the pair of opinions by the symmetric compromise

\[
(x_i,x_j)\longmapsto((1-\mu)x_i+\mu x_j,\;\mu x_i+(1-\mu)x_j),
\]

and replace the selected confidence by \(c_{U_t}+\gamma(1-c_{U_t})\). Otherwise leave the opinions unchanged and replace the selected confidence by \(\delta c_{U_t}\). Every unselected confidence and opinion stays fixed. The strict inequality at the receptiveness boundary is essential and is retained throughout. The result does not assume that \(G\) is connected, that limit opinion clusters are distinct on adjacent vertices, or that receptiveness is monotone in time. The edge choices are independent and uniformly distributed; a generalization to a uniformly positive conditional selection probability follows from the same proof, provided the preliminary confidence-limit conclusions remain valid.

The convergence of all opinions and the confidence dichotomy \(\lim_t c_e(t)\in\{0,1\}\) almost surely, together with the implication \(\lim_t c_e(t)=1\Rightarrow \lim_t(x_i(t)-x_j(t))=0\), are **preexisting results**: see [1], Section 3.2, Theorem 5 and its preparatory convergence theorem. These are used as proven premises, not claimed as new.

## Proof

**Lemma (predictable receptive-time sampling).** Fix any edge \(e\). With probability one, if \(A_e(t)=1\) at infinitely many integer times, then \(U_t=e\) and \(A_e(t)=1\) simultaneously at infinitely many times.

*Proof of the lemma.* Let \(\mathcal F_t\) contain all random choices strictly before time \(t\). The states, and hence \(A_e(t)\), are \(\mathcal F_t\)-measurable, whereas \(U_t\) is independent of \(\mathcal F_t\) and has probability \(p=1/m\) of equaling \(e\). The conditional Borel–Cantelli lemma applied to \(B_t=\{A_e(t)=1,U_t=e\}\) gives

\[
\sum_{t=0}^{\infty}\mathbf1_{B_t}=\infty\quad\text{on}\quad
\left\{\sum_{t=0}^{\infty}A_e(t)=\infty\right\},
\]

almost surely, since \(\mathbb P(B_t\mid\mathcal F_t)=pA_e(t)\). For completeness, the conditional form also follows by examining successive stopping times at which \(A_e(t)=1\): conditional on the past at each such time, a fresh independent draw selects \(e\) with probability \(p\); the probability of missing the next \(k\) such occasions is at most \((1-p)^k\). Repeating after each deterministic starting time excludes finitely many successes among infinitely many occasions. \(\square\)

**Case 1: confidence tends to zero.** Fix an edge \(e\) in the probability-one event where [1, Theorem 5] gives \(c_e(t)\to0\). Every time \(U_t=e\) and \(A_e(t)=1\), the confidence update satisfies

\[
c_e(t+1)=(1-\gamma)c_e(t)+\gamma\ge\gamma>0.
\]

There can therefore be only finitely many selected receptive interactions on this edge. By the lemma, there can only be finitely many times at which the edge is receptive at all, including times when other edges happen to be selected. Thus there is a finite \(T_e\) with \(A_e(t)=0\) for all \(t\ge T_e\).

**Case 2: confidence tends to one.** Fix an edge \(e=\{i,j\}\) with \(c_e(t)\to1\). The previously established convergence results [1, Theorem 5] imply \(x_i(t)-x_j(t)\to0\). Consequently, for all sufficiently large \(t\), both \(c_e(t)>1/2\) and \(|x_i(t)-x_j(t)|<1/2\), so \(A_e(t)=1\) permanently. Because an independently selected fixed edge is drawn infinitely often almost surely, these edges also have infinitely many selected receptive interactions.

There are only finitely many edges. Intersect the finitely many probability-one events just used and take the maximum of the finitely many stabilization times \(T_e\). Then for every \(t\ge T\), the receptive edges are exactly those with confidence limit one. The operational characterization by infinitely many selected receptive interactions follows from the two cases. \(\square\)

## Verification

The proof's only new probabilistic ingredient is the predictable-selection lemma. Its hypothesis uses the **pre-selection** effective graph, so it directly addresses edges that repeatedly become receptive while some other edge is drawn. The confidence-update inequality is uniform over the full allowed parameter ranges, including \(\gamma=1\) and \(\delta=0\). The implication from confidence-one to equal limiting opinions is exactly the previously established part of [1, Theorem 5]; it is not inferred from simulations.

Run the included standalone script using a standard Python 3 interpreter: `python verify.py`. It checks exact-rational compromise energy identities, selected-edge confidence-update inequalities, and sample trajectories with permanently receptive and permanently unreceptive edges, together with randomized conservation and monotone-energy checks. Finite computation is solely a consistency check and is not evidence of the almost-sure infinite-time assertion.

## Relationship to prior work

Li, Luo, and Porter [1, Section 3.2, Theorems 5–7 and Appendix A.2] prove almost-sure confidence convergence to zero or one and exclusion of edges joining distinct limiting opinion clusters. They prove eventual graph constancy for the **baseline** DW dynamics, and for their **synchronous** adaptive HK model, but explicitly leave even almost-sure eventual constancy of the **asynchronous adaptive-confidence DW** effective graph unestablished [1, Section 6.2 and Appendix A.2]. Their obstruction involves short receptive episodes between selections of a particular edge. The predictable-selection lemma excludes infinitely many such episodes for edges whose confidence tends to zero. This is the substantive new implication; it is not a renaming of confidence convergence.

Thompsky, Wu, Porter, and Luo [2] examine **adaptive edge-selection weights with a fixed confidence threshold**. Their model samples edges according to evolving weights and differs from the present model, which has uniform edge selection and evolving confidence thresholds. Its conditional effective-graph theorem does not imply this confidence-adaptive result. General random-network Borel–Cantelli techniques, including [3], supply background to the sampling argument, not a statement about the particular adaptive-confidence DW process.

## Limitations

This is an almost-sure, eventual structural result, not a deterministic uniform bound on the stabilization time, an expected-time estimate, or an assertion of global opinion consensus. Edges joining nodes with equal limiting opinions may be absent from the limiting effective graph. The theorem assumes finitely many edges, a strictly positive confidence-increase parameter, a strictly subunit confidence-decrease multiplier, and independent uniform edge selections. A selection mechanism that assigns an edge vanishingly small sampling probability could defeat the predictable-sampling argument. The result does not establish stabilization of related synchronous adaptive rules or other stochastic learning systems without these hypotheses. No independent audit or validation is claimed.

## References

[1] Grace J. Li, Jiajie Luo, and Mason A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563v3 (27 July 2024), first version 14 March 2023, Sections 2.4, 3.2, 6.2, and Appendix A.2. https://arxiv.org/html/2303.07563v3 . DOI: 10.1137/23M1558951.

[2] Leila Thompsky, Yuexuan Wu, Mason A. Porter, and Jiajie Luo, *A Bounded-Confidence Model of Opinion Dynamics with Adaptive Interaction Probabilities*, arXiv:2605.20418v1 (19 May 2026), Sections III–IV. https://arxiv.org/html/2605.20418v1 .

[3] Guodong Shi, Brian D. O. Anderson, and Karl H. Johansson, *Consensus over Random Graph Processes: Network Borel–Cantelli Lemmas for Almost Sure Convergence*, IEEE Transactions on Information Theory 61 (2015), 5690–5707. DOI: 10.1109/TIT.2015.2468584.
