# Compact transversal profiles in sparse-shift asymptotic modulus limits

## Finding
Let \(K\subset(0,\infty)\) be any nonempty compact set, and set \(b=\max K\). Choose a sequence \((\alpha_j)_{j\ge1}\) in \(K\) whose subsequential limit set is exactly \(K\). Put \(p_j=2^{2^j}+1\) for integers \(j\ge1\). On the complex Hilbert space \(H=\ell_2(\mathbb N)\), with canonical basis \((e_k)_{k\ge1}\), define the unilateral weighted shift \(W e_k=w_ke_{k+1}\), where
\[
w_k=\begin{cases}\exp(-\alpha_j(p_j-1)),&k=p_j,\\1,&\text{otherwise}.\end{cases}
\]
Write \(Q_r\) for the orthogonal projection onto \(\operatorname{span}\{e_1,\ldots,e_r\}\), and let \(D_{r,\alpha}=Q_r+e^{-\alpha}(I-Q_r)\) for integers \(r\ge1\) and \(\alpha\in K\). The weak-operator cluster set of the sequence \(A_n=|W^n|^{1/n}\) is **exactly**
\[
\mathcal C_K=\{sI:e^{-b}\le s\le1\}\;\cup\;\bigcup_{r=1}^{\infty}\{D_{r,\alpha}:\alpha\in K\}.
\]
The strong-operator cluster set is the same. Moreover, for every unit vector \(x\in H\), the cluster set of \((\langle A_nx,x\rangle)_{n\ge1}\) is the **same** interval \([e^{-b},1]\), regardless of the finer compact set \(K\). The shift \(W\) is injective, contractive, and not bounded below, and \(\|W^n\|=1\) for all integers \(n\ge1\).

The scalar interval \(\{sI:e^{-b}\le s\le1\}\) is one connected component of \(\mathcal C_K\). For each \(r\ge1\), the set \(\{D_{r,\alpha}:\alpha\in K\}\) is a clopen copy of \(K\), and these copies accumulate at \(I\) as \(r\to\infty\). Thus one can realize an arbitrary compact positive transversal profile in a non-bounded-below shift's operator cluster set while keeping all scalar asymptotic numerical ranges unchanged when \(b\) is fixed. For example, \(K=\{b\}\) and \(K=[b/2,b]\) give nonhomeomorphic cluster sets with identical scalar asymptotic numerical ranges for every unit vector.

## Assumptions and scope
All spaces and operators are over \(\mathbb C\). Cluster sets mean limits along subsequences whose indices tend to infinity, not closure of the finite initial terms. The symbol \(|W^n|\) means \(((W^n)^*W^n)^{1/2}\), followed by the positive \(n\)-th root. All operator limits are on the fixed \(H=\ell_2(\mathbb N)\). Compactness of \(K\subset(0,\infty)\) supplies \(0<a=\min K\le b=\max K<\infty\). Such an \((\alpha_j)\) exists: concatenate finite \(1/m\)-nets of \(K\) for \(m=1,2,\ldots\).

## Proof
**1. Exact diagonal coordinates and scale separation.** For all integers \(k,n\ge1\), the weighted-shift identity gives
\[
A_ne_k=\exp(-E_k(n))e_k,\qquad
E_k(n)=\frac1n\sum_{i:\,k\le p_i\le k+n-1}\alpha_i(p_i-1).
\]
Define \(E(n)=E_1(n)=n^{-1}\sum_{p_i\le n}\alpha_i(p_i-1)\). For every fixed \(k\),
\[
E_k(n)-E(n)=\frac1n\left(\sum_{i:\,n<p_i\le n+k-1}\alpha_i(p_i-1)-\sum_{i:\,p_i<k}\alpha_i(p_i-1)\right).
\tag{1}
\]
The second sum is a fixed finite constant for fixed \(k\). The chosen superlacunary sequence obeys \(p_{j+1}/p_j\to\infty\) and \(\sum_{i<j}p_i/p_j\to0\). Consequently, with \(b=\max K\),
\[
0\le E(n)\le b+o(1)\qquad(n\to\infty).
\tag{2}
\]
Indeed, for \(p_j\le n<p_{j+1}\), the numerator is at most \(b\sum_{i\le j}p_i=b p_j(1+o(1))\).

**2. Exhaustion of possible subsequential limits.** Let \((n_\ell)\) tend to infinity along a subsequence on which \(A_{n_\ell}\) converges in the weak operator topology. For each \(\ell\), let \(p_{j(\ell)}\) be the first spike position strictly larger than \(n_\ell\), and put \(d_\ell=p_{j(\ell)}-n_\ell\ge1\). Passing to a further subsequence, either \(d_\ell\to\infty\) or \(d_\ell=r\) is constant for some integer \(r\ge1\).

In the first case, for each fixed \(k\), the first sum on the right of (1) is eventually empty. Thus \(E_k(n_\ell)-E(n_\ell)\to0\), and weak convergence forces every diagonal coordinate to have a common limit \(s\in[e^{-b},1]\) by (2). The limit is \(sI\).

In the second case, \(n_\ell=p_{j(\ell)}-r\). The previous-spike sum divided by \(n_\ell\) tends to zero, hence \(E(n_\ell)\to0\). Pass to a further subsequence with \(\alpha_{j(\ell)}\to\alpha\in K\). For fixed \(k\), the first sum on the right of (1) is eventually empty when \(k\le r\) and consists of the single current-spike term \(\alpha_{j(\ell)}(p_{j(\ell)}-1)\) when \(k\ge r+1\). Since \(p_{j(\ell)}/n_\ell\to1\), the limiting diagonal is precisely \(D_{r,\alpha}\). The two cases exhaust all weak-operator cluster points.

**3. Every listed operator occurs.** For \(r\ge1\) and \(\alpha\in K\), choose \(j_\ell\to\infty\) with \(\alpha_{j_\ell}\to\alpha\) and take \(n_\ell=p_{j_\ell}-r\). The preceding calculation yields \(A_{n_\ell}\to D_{r,\alpha}\) coordinatewise.

For a scalar target \(s=e^{-t}\), with \(0<t<b\), choose \(j_\ell\to\infty\) such that \(\alpha_{j_\ell}\to b\), and take \(n_\ell=\lfloor\alpha_{j_\ell}(p_{j_\ell}-1)/t\rfloor\). Eventually \(p_{j_\ell}\le n_\ell<p_{j_\ell+1}\), while \(E(n_\ell)\to t\). For \(t=b\), use \(n_\ell=p_{j_\ell}\); for \(t=0\), use \(n_\ell=\lfloor\sqrt{p_{j_\ell}p_{j_\ell+1}}\rfloor\). In all three cases the next spike is farther than every fixed \(k\) from \(n_\ell\), so (1) yields the scalar limit \(e^{-t}I\).

Because \(0\le A_n\le I\) and all \(A_n\) are diagonal, coordinatewise convergence implies strong-operator convergence by approximation with finite-support vectors. Thus the constructed cluster limits are strong as well, while every weak cluster limit was already classified. The WOT and SOT cluster sets coincide.

**4. Scalar ranges and topology.** Every member of \(\mathcal C_K\) lies between \(e^{-b}I\) and \(I\). The scalar segment supplies every value in \([e^{-b},1]\) to \(\langle Ax,x\rangle\) for each unit \(x\). Compactness of the bounded diagonal sequence supplies the reverse inclusion for every scalar cluster. Thus the scalar asymptotic numerical range at every unit vector is precisely \([e^{-b},1]\).

Fix \(a=\min K>0\), and choose a real \(\theta\) satisfying \(e^{-a}<\theta<1\). Within \(\mathcal C_K\), for every integer \(r\ge1\), the pair of strict inequalities
\[
\langle Be_r,e_r\rangle>\theta,\qquad \langle Be_{r+1},e_{r+1}\rangle<\theta
\]
is satisfied precisely by \(B=D_{r,\alpha}\) with \(\alpha\in K\). Consequently every \(r\)-fiber is both open and closed in \(\mathcal C_K\). The continuous injection \(\alpha\mapsto D_{r,\alpha}\) is a homeomorphism from compact \(K\) onto that fiber. No connected subset can meet both a fiber and the scalar segment, so the connected scalar interval is itself a connected component. Moreover,
\[
\|(D_{r,\alpha}-I)x\|\le(1-e^{-b})\|(I-Q_r)x\|\longrightarrow0
\]
uniformly in \(\alpha\in K\) for each \(x\in H\). The fibers therefore accumulate at \(I\) as their indices tend to infinity, and at no other scalar point. Each fiber's connected components are exactly the images of those of \(K\).

Finally, every weight is strictly positive, while the spike weights tend to zero, so \(W\) is injective and not bounded below. Since arbitrarily long consecutive blocks of weights equal one, \(\|W^n\|=1\) for each fixed positive integer \(n\). The operator is a contraction because all weights are at most one. This completes the proof.

## Verification
The exact finite-coordinate formula in Step 1 follows by applying \(W^n\) to basis vectors and taking the positive root of the diagonal operator \((W^n)^*W^n\). All subsequent limits use only \(\sum_{i<j}p_i=o(p_j)\), \(p_{j+1}/p_j\to\infty\), and compactness of \(K\). No finite numerical sampling is used to assert a property of infinite subsequences. The two disjoint limit mechanisms (a far-away next spike versus a next spike at fixed offset) form an exhaustive dichotomy after extraction of a subsequence.

## Relationship to prior work
Youqing Ji and Bangyuan Yang, *Asymptotic Numerical Ranges and Invariant Subspaces of Operators*, arXiv:2608.21553v1 (first posted August 21, 2026), v2, Question 3 and Section 4. Their Proposition 4.1 determines the weak-operator cluster set for shifts bounded below. Their Example 4.3 constructs a sparse-spike shift not bounded below and proves disconnectedness by examining one matrix coefficient. The present theorem is a full limit-set classification for a parametrized sparse-spike family, together with an inverse realization result for all compact positive transversal profiles and the invisibility of these profiles to all scalar asymptotic numerical ranges. It neither claims the original disconnectedness example nor the general interval theorem for scalar asymptotic numerical ranges as new.

Published comparisons also included the distinct problems of norm/essential-norm power profiles of irreducible weighted shifts, and local-resolvent power sets of quasinilpotent shifts; neither concerns these weak/strong operator cluster sets of positive roots. Finding an equivalent earlier result under a different limit-operator or moving-average vocabulary remains a literature-priority risk.

## Limitations
The construction is specific to strictly positive sparse-spike unilateral shifts on \(\ell_2\). It does not classify all non-bounded-below weighted shifts or establish a general realization theorem for arbitrary compact subsets of the full operator space. The statement is about WOT/SOT subsequential cluster sets, not operator-norm convergence. Originality is assessed against the sources inspected and may change if an equivalent prior formulation is found. No independent audit or external proof validation has been performed.

## References
1. Y. Ji and B. Yang, *Asymptotic Numerical Ranges and Invariant Subspaces of Operators*, arXiv:2608.21553v1 (2026-08-21), and v2, https://arxiv.org/html/2608.21553v2 .
2. E. Ignatev, *The power set of a quasinilpotent backward weighted shift*, arXiv:2607.16743 (2026-07-18), https://arxiv.org/abs/2607.16743 .
3. *Exact norm and essential-norm power profiles for irreducible weighted shifts*, publicly posted September 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-irreducible-weighted-shift-essential-power-profiles--d5ae263f185c .
