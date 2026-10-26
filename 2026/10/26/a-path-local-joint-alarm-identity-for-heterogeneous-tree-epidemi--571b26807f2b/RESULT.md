# A path-local joint-alarm identity for heterogeneous tree epidemics

## Finding

For **every** finite undirected tree \(T=(V,E)\) with at least two vertices, every assignment of independent edge-transmission probabilities \(t_e\in(0,1)\), every probability distribution \(\pi\) of a **single** initial infection source, and every distinct pair of monitored vertices \(a,b\in V\), let \(B_v\) be the event that the epidemic ultimately reaches \(v\), and write \(b_v=\Pr(B_v)\). Denote the unique \(a\)-to-\(b\) path by \(P_{ab}\), and set

\[
\rho_{ab}=\prod_{e\in E(P_{ab})}t_e,\qquad
c_v(P_{ab})=1-\sum_{\substack{e\in E(P_{ab})\\e\ni v}}\frac{t_e}{1+t_e}.
\]

Then the **exact joint-alarm identity** is

\[
\boxed{\Pr(B_a\cap B_b)=
\rho_{ab}\sum_{v\in V(P_{ab})}c_v(P_{ab})\,b_v.}
\]

Every coefficient \(c_v(P_{ab})\) is strictly positive, even at internal path vertices with two incident path edges. The right-hand side depends only on single-vertex alarm marginals **on the connecting path**, regardless of source distribution, branches leaving that path, or their transmissions.

In particular, for a homogeneous transmission probability \(p\in(0,1)\), with \(d=d_T(a,b)\),

\[
\boxed{\Pr(B_a\cap B_b)=\frac{p^d}{1+p}
\left[b_a+b_b+(1-p)\sum_{v\in V(P_{ab})\setminus\{a,b\}}b_v\right].}
\]

For neighboring monitors, even in the heterogeneous model,

\[
\boxed{\Pr(B_a\cap B_b)=\frac{t_{\{a,b\}}}{1+t_{\{a,b\}}}(b_a+b_b).}
\]

Thus all \(\binom{|V|}{2}\) distinct pairwise co-detection probabilities are determined by the \(|V|\) one-monitor probabilities and the known tree and edge parameters, with no estimated source prior required.

## Assumptions and scope

The epidemic is an undirected **bond-percolation outbreak** on a known, finite, connected, acyclic graph: each edge \(e\) is independently open with probability \(t_e\in(0,1)\). Exactly one vertex \(S\) is chosen initially, independently of the edges, according to an arbitrary fixed distribution \(\pi=(\pi_s)_{s\in V}\). The infected set is the connected component of \(S\) in the open-edge graph. The event \(B_v\) is **ever infected**, not concurrently infectious, and detectors are perfect and passive. Distinct outbreaks are independent copies; all probabilities refer to population probabilities, not estimated finite-sample rates. No uniform-source, regular-tree, or homogeneous-transmission assumption is needed for the main identity.

## Proof

**Step 1: a pair event is a three-terminal path-product kernel.** Let \(P=P_{ab}\) and let \(\operatorname{pr}_P(s)\) be the unique attachment/projection of vertex \(s\) to \(P\). Define \(K_{vs}=\prod_{e\in E(P(v,s))}t_e\), with an empty product equal to one. For each source \(s\), edge independence and the uniqueness of tree paths show

\[
\Pr(B_v\mid S=s)=K_{vs},\quad
\Pr(B_a\cap B_b\mid S=s)=
\rho_{ab}\prod_{e\in E(P(s,\operatorname{pr}_P(s)))}t_e.
\]

Consequently \(b=K\pi\). Let \(f_s=\prod_{e\in E(P(s,\operatorname{pr}_P(s)))}t_e\), so the source-conditioned pair kernel is \(\rho_{ab}f_s\).

**Step 2: prove the needed inverse identity without assuming it.** Define a symmetric matrix \(Q\) by

\[
Q_{vv}=1+\sum_{e\ni v}\frac{t_e^2}{1-t_e^2},\quad
Q_{uv}=\begin{cases}
-\dfrac{t_{\{u,v\}}}{1-t_{\{u,v\}}^2},&\{u,v\}\in E,\\
0,&\text{otherwise},
\end{cases}
\quad(u\ne v).
\]

For every column \(s\), evaluate \((QK)_{vs}\). When \(s=v\), each neighbor \(u\) contributes \(K_{us}=t_{\{u,v\}}K_{vs}\), and all edge terms cancel leaving one. When \(s\ne v\), exactly one neighbor lies closer to \(s\), with \(K_{us}=K_{vs}/t_{\{u,v\}}\); all other neighbors give \(K_{us}=t_{\{u,v\}}K_{vs}\). The closer-edge contribution cancels the leftover diagonal term, giving zero. Thus \(QK=I\), so \(Q=K^{-1}\). This product-distance inverse formula was established in earlier matrix theory and is **not** claimed as new.

**Step 3: localized action of the inverse on the pair kernel.** For \(v\notin V(P)\), one neighbor points toward \(P\), with \(f_u=f_v/t_{\{u,v\}}\); all other neighbors satisfy \(f_u=t_{\{u,v\}}f_v\). Exactly the same cancellation gives \((Qf)_v=0\). For \(v\in V(P)\), \(f_v=1\), each neighbor along \(P\) has \(f_u=1\), and each neighbor off \(P\) has \(f_u=t_{\{u,v\}}\). Substitution into the explicit \(Q\) gives

\[
(Qf)_v=1-\sum_{\substack{e\in E(P)\\e\ni v}}\frac{t_e}{1+t_e}
=c_v(P).
\]

An endpoint meets one path edge and an interior path vertex two. Since \(0<t_e/(1+t_e)<1/2\), every \(c_v(P)>0\).

**Step 4: eliminate the unknown source distribution.** Because \(Q\) is symmetric and \(b=K\pi\), one has \(\pi=Qb\). Therefore

\[
\Pr(B_a\cap B_b)=\rho_{ab}\sum_s \pi_s f_s
=\rho_{ab}\,b^{\mathsf T}Qf
=\rho_{ab}\sum_{v\in V(P)}c_v(P)b_v,
\]

proving the identity. The homogeneous and adjacent-endpoint formulas follow by substitution.

## Verification

The accompanying standalone exact-rational checker `verify_tree_joint_path_identity.py` enumerates all labeled trees through five vertices by Prüfer sequences, with two distinct rational edge-parameter families and one nonuniform rational source distribution on each tree. For each monitor pair, it compares the stated right-hand side with direct summation over all possible source vertices and all \(2^{|E|}\) edge configurations, without using the inverse formula. It reports 290 tree/weight scenarios, 2,712 exact pair comparisons, and 206,368 source–edge–pair weighted evaluations. The included `verification_certificate.json` captures the successful execution; a finite check is **not** the proof for arbitrary trees. The four-step analytical argument proves the theorem for all specified cases.

## Relationship to prior work

Bapat, Lal and Pati (2006) gave the homogeneous exponential-distance inverse of a tree. Bapat and Sivasubramanian (2012), especially Theorem 2.2, establish the more general weighted product-distance inverse underlying **Step 2**; that matrix formula is prior work, not a new claim. The present result additionally identifies the *two-alarm stochastic event kernel* as the product of the monitor-path reliability and the source-to-path reliability, then proves the inverse of that kernel is exactly supported on the monitor path; this yields an explicit positive-coefficient reconstruction of joint monitoring probabilities from only marginal monitoring probabilities.

Antulov-Fantulin et al. (2013) study estimation of an outbreak source from partial epidemic realizations. Sharkey et al. (2013/2015) derive exact pair-based time-dependent moment equations for Markovian SIR dynamics on trees. These settings and results do not directly state the exact joint-ever-infected versus marginal-ever-infected path identity under an arbitrary random source law. An equivalent identity in other reliability or tree-process literature is a residual originality risk.

## Limitations

The formula concerns eventual cluster membership in an independent-edge, **single-source** model on a **tree**; it need not hold for graphs with cycles, correlated transmissions, multiple simultaneous sources, epidemic observation deadlines, time-dependent infectious-state events, or noisy empirical estimates. It does not identify the distribution of infection times, nor infer pairwise co-detection on an unknown contact graph. The inverse-matrix lemma is established prior art. Independent verification and independent literature certification have not been performed.

## References

1. R. B. Bapat, A. K. Lal and S. Pati (2006), *A q-analogue of the distance matrix of a tree*, Linear Algebra and its Applications **416**, 799–814. DOI: `10.1016/j.laa.2005.12.023` (earliest indexed online source date: 2006-02-11).
2. R. B. Bapat and S. Sivasubramanian (2012), *The product distance matrix of a tree and a bivariate zeta function of a graph*, Electronic Journal of Linear Algebra **23**, 275–286, Theorem 2.2. Open full text: `https://journals.uwyo.edu/index.php/ela/article/download/1041/1041/1041`.
3. N. Antulov-Fantulin, A. Lančić, H. Štefančić, M. Šikić and T. Šmuc (2013), *Statistical inference framework for source detection of contagion processes on arbitrary network structures*, arXiv:1304.0018 (first posted 2013-03-29).
4. K. J. Sharkey, I. Z. Kiss, R. R. Wilkinson and P. L. Simon (first published online 2013-12-18), *Exact Equations for SIR Epidemics on Tree Graphs*, Bulletin of Mathematical Biology **77**, 614–645. DOI: `10.1007/s11538-013-9923-5`.
