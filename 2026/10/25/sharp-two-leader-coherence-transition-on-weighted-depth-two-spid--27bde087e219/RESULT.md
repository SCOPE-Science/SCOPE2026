# Sharp two-leader coherence transition on weighted depth-two spiders

## Finding

Let \(k\ge3\) and \(t>0\). Form a weighted tree with one central vertex \(c\), branch vertices \(u_1,\ldots,u_k\), and leaves \(v_1,\ldots,v_k\). The edge \(cu_i\) has conductance \(1\), and \(u_iv_i\) has conductance \(1/t\). Let \(L\) be the weighted Laplacian. For each unordered pair \(S\) of *noise-free leaders*, let \(F=V\setminus S\) and minimize the unnormalized follower coherence \(C(S)=\operatorname{tr}((L_{FF})^{-1})\).

**Theorem (complete optimal-set classification).** If \(k=3\), then the minimizing sets are exactly:

- \(0<t<1\): the three pairs \(\{u_i,u_j\}\) with \(i\ne j\); the minimum is \(3t+7/2\).
- \(t=1\): those three pairs and the three pairs \(\{c,v_i\}\); the minimum is \(13/2\).
- \(t>1\): the three pairs \(\{c,v_i\}\); the minimum is \(2t+5-1/(t+1)\).

If \(k\ge4\), then **for every \(t>0\)** the only minimizing sets are the \(k\) pairs \(\{c,v_i\}\), and the minimum equals
\[
C_{\min}(k,t)=(k-1)(t+2)+\frac{t}{t+1}.
\]
All other leader pairs have strictly greater coherence in the respective strict regimes.

Thus a three-branch network has a sharp conductance-ratio transition, whereas four or more branches enforce a resistance-independent center-and-leaf design. The theorem optimizes over *all* pairs, not just selected symmetry types.

## Assumptions and scope

The vertex set is exactly \(\{c,u_1,\ldots,u_k,v_1,\ldots,v_k\}\) and there are no edges except \(cu_i\) and \(u_iv_i\). Conductance is reciprocal to electrical resistance, so the outer-link resistance is \(t\), not \(1/t\). Leaders are pinned without noise. The weighted Laplacian is \(L_{xx}=\sum_{y\ne x}w_{xy}\) and \(L_{xy}=-w_{xy}\). The grounded principal submatrix \(L_{FF}\) is positive definite. The objective is \(\operatorname{tr}(L_{FF}^{-1})\); if the noise covariance is the identity, the physical stationary total variance is one half of this objective, which does not change its minimizers.

The theorem covers all integers \(k\ge3\) and all real \(t>0\), including exactly the transition \(k=3,t=1\). It makes no claim about arbitrary nonidentical branch weights, longer branches, or noise-corrupted leaders. The two-branch case is a weighted five-vertex path and is excluded from this new classification.

## Proof

**1. Diagonal Green function on a tree.** Short all vertices of a leader pair \(S=\{a,b\}\) to a common electrical ground. For a vertex \(x\) let \(y\) be its unique projection onto the \(a\)-to-\(b\) path, i.e., the point where the paths from \(x\) to \(a\) and \(b\) first meet that path. Write \(d(x,y)\) for the sum of edge resistances to \(y\), \(A=d(a,y)\), and \(B=d(y,b)\). The two portions of the path from \(y\) to the grounded terminals are parallel, and the branch from \(x\) to \(y\) is in series. Therefore
\[
(L_{FF}^{-1})_{xx}=d(x,y)+\frac{AB}{A+B},
\]
where \(A+B=d(a,b)>0\), and the expression is zero for leaders. This follows equally from the Dirichlet network potential with one unit of current injected at \(x\). Summing over the vertices gives \(C(S)\), with no spectral approximation or probabilistic assumption.

**2. Exhaustive orbit reduction.** Every unordered pair belongs to exactly one of six classes under permutation of the branches. Direct substitution into the preceding resistance formula yields the following complete table (the displayed pair is representative, with \(i\ne j\)):

| Leader pair | Coherence |
|---|---|
| \(\{c,u_i\}\) | \(k(t+2)-2\) |
| \(\{c,v_i\}\) | \(k(t+2)-(t+1)-1/(t+1)\) |
| \(\{u_i,v_i\}\) | \(k(t+4)-t-3\) |
| \(\{u_i,u_j\}\) | \(k(t+3)-11/2\) |
| \(\{u_i,v_j\}\) | \([k(t^2+6t+6)-(t^2+7t+11)]/(t+2)\) |
| \(\{v_i,v_j\}\) | \([k(4t^2+10t+6)-(5t^2+14t+11)]/[2(t+1)]\) |

For example, if \(S=\{c,v_1\}\), every other branch contributes \(t+2\) to the trace, while \(u_1\) contributes the parallel resistance \(t/(t+1)\). Thus \(C(S)=(k-1)(t+2)+t/(t+1)\), independently confirming the second table row. If \(S=\{u_1,u_2\}\), the center contributes \(1/2\), the two leader-branch leaves contribute \(2t\), and each remaining branch contributes \(t+3\), giving \(k(t+3)-11/2\).

**3. Four or more branches.** Subtract the center-and-leaf value from each competing orbit cost. At \(k=4\), the five differences, in the table's order excluding the center-and-leaf row, are
\[
\frac{t^2}{t+1},\quad
\frac{6t+7}{t+1},\quad
\frac{2t^2+t+1}{2(t+1)},\quad
\frac{4t^2+4t+1}{(t+1)(t+2)},\quad
\frac{5t+1}{2}.
\]
All are strictly positive for \(t>0\). As \(k\) increases by one, the corresponding differences increase by, respectively,
\[
0,\quad 2,\quad 1,\quad \frac{2(t+1)}{t+2},\quad t+1,
\]
all nonnegative. Hence the center-and-leaf pairs are the **only** optimizers for every \(k\ge4\), proving the stated minimum.

**4. Exactly three branches.** Let \(U=C(\{u_i,u_j\})\) for distinct branch indices and \(V=C(\{c,v_i\})\). The table gives
\[
U-V=\frac{(t-1)(2t+1)}{2(t+1)}.
\]
For \(0<t\le1\), the differences between the other four pair types and \(U\) are, respectively,
\[
\frac12,\quad \frac{11-2t}{2},\quad
\frac{t(3-2t)}{2(t+2)},\quad
\frac{t(t+3)}{2(t+1)}.
\]
All are strictly positive. For \(t\ge1\), the differences between those same four types and \(V\) are
\[
\frac{t^2}{t+1},\quad\frac{4t+5}{t+1},\quad
\frac{2t^2-1}{(t+1)(t+2)},\quad
\frac{3t-1}{2},
\]
again strictly positive. Accordingly the two candidate types exchange global optimality only at \(t=1\). There are \(\binom32=3\) distinct inner-inner pairs and three center-leaf pairs, establishing the counts and all equality cases. This completes the proof.

## Verification

Run `python verify_spider.py` with SymPy installed (`requirements.txt`). The checker builds the actual weighted grounded Laplacian, inverts its principal submatrix **exactly over rational numbers**, and verifies the six formulas and all claimed minimizers for \(k=3,4,5,6\) and \(t\in\{1/7,1/2,1,3/2,7/2\}\). It performs 950 exact inversions and separately checks the symbolic strict-difference identities used in the universal proof. Expected successful output begins with `VERIFY_OK`.

The finite matrix tests are consistency checks, not proofs for all \(k\) and \(t\); the all-parameter argument is the explicit resistance calculation and algebraic sign proof above.

## Relationship to prior work

Patterson and Bamieh formulate noise-free leader selection through Laplacian principal submatrices and network coherence. Fitch and Leonard (arXiv:1407.1569, first public 2014-07-07) develop joint centrality for multiple leaders and give complete solutions for paths and cycles (in particular, their Section V and Appendix C). The present theorem concerns a different branching family and classifies **every** two-leader pair over a continuous outer-resistance parameter. General leader-selection relaxations such as Lin, Fardad, and Jovanović's do not provide this explicit all-parameter spider classification in the material inspected.

A later paper by Sun, Li, and Zheng, *Leader selection for coherence in symmetric and asymmetric trees* (2021, DOI 10.1088/1742-5468/ac0f66), is especially relevant. Only its abstract and bibliography were available for inspection. Its abstract describes three prescribed assignment schemes on a tree family but does not establish whether it includes the present weighted depth-two spider or the exhaustive comparison of all leader pairs. **No claim of noncoverage based on its unseen full text is made.** This is the principal outstanding overlap risk.

## Limitations

This result is a self-contained analytical claim, not an independent mathematical audit or a guarantee of priority. The theorem does not encompass longer or irregular branches, imperfect leaders, or a different robustness metric such as the smallest grounded-Laplacian eigenvalue. The absence of a complete inspection of the 2021 tree paper leaves residual priority uncertainty. The objective is unnormalized trace, so comparisons with conventions using \(\frac12\operatorname{tr}\) require that scalar factor.

## References

1. S. Patterson and B. Bamieh, *Leader Selection for Optimal Network Coherence*, 49th IEEE Conference on Decision and Control (2010), DOI 10.1109/CDC.2010.5718151.
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569v1 (first public 2014-07-07), https://arxiv.org/abs/1407.1569.
3. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (2013), https://arxiv.org/abs/1302.0450.
4. S. Patterson, N. McGlohon, and K. Dyagilev, *Optimal k-leader selection for coherence and convergence rate in one-dimensional networks*, DOI 10.1109/TCNS.2016.2520201 (public 2016); applies to paths and rings, rather than the branching network studied here.
5. W. Sun, L. Li, and S. Zheng, *Leader selection for coherence in symmetric and asymmetric trees*, Journal of Statistical Mechanics (2021), DOI 10.1088/1742-5468/ac0f66. Full-text comparison outstanding.
