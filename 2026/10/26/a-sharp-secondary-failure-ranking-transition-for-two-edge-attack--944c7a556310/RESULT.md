# A sharp secondary-failure ranking transition for two-edge attacks on crown graphs

## Finding

For every integer \(n\ge4\), consider the **unweighted** crown graph \(\mathrm{Cr}_n=K_{n,n}-M\): its vertices are \(L_i,R_i\), indexed by \(i\in\{0,\ldots,n-1\}\), and \(L_iR_j\) is an edge precisely when \(i\ne j\). Write \(\mathrm{Kf}(G)=\sum_{\{u,v\}\subset V(G)}R_{uv}(G)\) for the Kirchhoff index (the sum of unit-resistance effective resistances). For two distinct present edges \(e,f\), set

\[
\Delta(e,f)=\mathrm{Kf}(\mathrm{Cr}_n-\{e,f\})-\mathrm{Kf}(\mathrm{Cr}_n).
\]

All two-edge deletions are connected. Every unordered pair of distinct present edges belongs to exactly one of the following four types. A canonical representative of each type consists of \(e=L_0R_1\) and a second edge:

| Type | Second edge | Description |
| --- | --- | --- |
| Incident \(I\) | \(L_0R_2\) | Shared actual vertex |
| Reciprocal \(R\) | \(L_1R_0\) | Disjoint vertices, the same two matched labels reversed |
| Linked \(L\) | \(L_1R_2\) | Disjoint vertices, exactly one cross-matched label |
| Independent \(D\) | \(L_2R_3\) | Disjoint vertices, four distinct matching labels |

The exact damages, with argument \(n\) suppressed on the left, are

\[
\begin{aligned}
\Delta_I&=\frac{2(4n^4-21n^3+38n^2-32n+12)}{(n-3)(n-2)(n-1)(n^2-3n+1)},\\
\Delta_R&=\frac{2(4n-3)}{(n-3)(n-1)},\\
\Delta_L&=\frac{2(4n^5-31n^4+89n^3-116n^2+68n-12)}{(n-3)(n-2)(n-1)(n^3-5n^2+7n-1)},\\
\Delta_D&=\frac{2(4n^6-35n^5+120n^4-202n^3+184n^2-88n+16)}{(n-2)(n-1)(n^2-4n+2)(n^3-5n^2+8n-2)}.
\end{aligned}
\]

For \(4\le n\le11\), the strict ranking is

\[\Delta_I>\Delta_D>\Delta_R>\Delta_L.\]

For every \(n\ge12\), the strict ranking is

\[\Delta_I>\Delta_R>\Delta_D>\Delta_L.\]

Consequently the global maximum is achieved **if and only if** the two removed edges share a vertex, giving exactly \(2n\binom{n-1}{2}=n(n-1)(n-2)\) maximizing unordered failure pairs. Although the worst class does not change, the most damaging **disjoint** configuration switches sharply from independent to reciprocal at dimension \(n=12\).

## Assumptions and scope

All edges have resistance and conductance equal to one. Vertices are individually labeled only to describe orbits; the results are invariant under permutations of matching labels and exchanging the bipartition classes. The Kirchhoff index is finite because all two-edge deletions are connected (proved below). The quantifier covers every integer \(n\ge4\) and every unordered two-element subset of the \(n(n-1)\) present edges. The \(n=3\) crown is a cycle, and adjacent two-edge removal disconnects it, so it is deliberately excluded. No assumption of random independent failures or variable edge weights is made.

## Proof

**1. Spectral kernel.** Put \(N=2n\) and let \(\mathcal L\) be the combinatorial Laplacian of the undeleted crown graph. On the constant symmetric, constant antisymmetric, zero-sum symmetric, and zero-sum antisymmetric subspaces, its eigenvalues are respectively \(0\), \(2(n-1)\), \(n\), and \(n-2\), the last two each of multiplicity \(n-1\). These are also the eigenvalues in [2, Proposition 8]. Fix the orientation \(b_{ij}=e_{L_i}-e_{R_j}\) of edge \(L_iR_j\). For \(m=1,2\), define

\[K_m((i,j),(p,q))=b_{ij}^{\mathsf T}(\mathcal L^+)^m b_{pq}.\]

Orthogonally projecting onto the three nonconstant eigenspaces gives the following **exact** formula (\(\delta_{ab}\) is the Kronecker delta):

\[
K_m=\frac{\delta_{ip}-\delta_{iq}-\delta_{jp}+\delta_{jq}}{2n^m}
+\frac{\delta_{ip}+\delta_{iq}+\delta_{jp}+\delta_{jq}-4/n}{2(n-2)^m}
+\frac{2/n}{[2(n-1)]^m}.
\]

For any present edge \(e\), define \(R=K_1(e,e)=(2n-1)/(n(n-1))\) and \(Q=K_2(e,e)\). For a second edge \(f\), let \(r=K_1(e,f)\) and \(q=K_2(e,f)\).

**2. Exact effect of two failures and connectivity.** Writing \(B=[b_e,b_f]\), the two-edge-deleted Laplacian on the subspace perpendicular to constants is \(\mathcal L-BB^{\mathsf T}\). The two-dimensional Woodbury identity and \(\mathrm{Kf}(G)=N\operatorname{tr}(\mathcal L_G^+)\) yield

\[
\begin{aligned}
\Delta(e,f)
&=2n\operatorname{tr}\left[(I-B^{\mathsf T}\mathcal L^+B)^{-1}B^{\mathsf T}(\mathcal L^+)^2B\right]\\
&=\frac{4n\big((1-R)Q+rq\big)}{(1-R)^2-r^2}.
\end{aligned}
\]

The positive eigenvalues of \(I-B^{\mathsf T}\mathcal L^+B\) are \(1-R-r\) and \(1-R+r\). For the four representative pairs, their factors are

| Class | \(1-R-r\) | \(1-R+r\) |
| --- | --- | --- |
| \(I\) | \(\frac{(n-3)(n^2-3n+1)}{n(n-2)(n-1)}\) | \(\frac{n^2-3n+1}{n(n-2)}\) |
| \(R\) | \(\frac{n-3}{n-1}\) | \(\frac{n-2}{n}\) |
| \(L\) | \(\frac{n^3-5n^2+7n-1}{n(n-2)(n-1)}\) | \(\frac{(n-3)(n-1)}{n(n-2)}\) |
| \(D\) | \(\frac{n^3-5n^2+8n-2}{n(n-2)(n-1)}\) | \(\frac{n^2-4n+2}{n(n-2)}\) |

They are all strictly positive when \(n\ge4\). For instance, substituting \(n=t+4\), \(t\ge0\), gives \(n^2-3n+1=t^2+5t+5\), \(n^2-4n+2=t^2+4t+2\), \(n^3-5n^2+7n-1=t^3+7t^2+15t+11\), and \(n^3-5n^2+8n-2=t^3+7t^2+16t+14\). The positive definite update matrix proves \(\mathcal L-BB^{\mathsf T}\) positive definite on constants' orthogonal complement; hence every two-edge deletion stays connected.

**3. Only four classes.** Permuting the matching labels and optionally swapping the two sides sends the first edge to \(L_0R_1\). Every remaining edge is either incident to it, reciprocal, disjoint sharing exactly one matching label across opposite endpoints, or disjoint with four distinct labels. These are precisely the four listed orbit types. Substituting their Kronecker deltas in the kernel and then in the two-failure formula yields the four rational functions above; no other configuration is omitted.

**4. Strict inequalities and the sharp transition.** All denominators in the four damages and comparisons below are positive for \(n\ge4\), by the shifted polynomial identities from step 2. Algebraic cancellation gives

\[
\begin{aligned}
\Delta_I-\Delta_D
&=\frac{2n P(n)}{(n-3)(n^2-4n+2)(n^2-3n+1)(n^3-5n^2+8n-2)},\\
\Delta_I-\Delta_R
&=\frac{2(2n^2-3n-6)}{(n-3)(n-2)(n^2-3n+1)},\\
\Delta_R-\Delta_L
&=\frac{2(5n^2-15n+6)}{(n-3)(n-2)(n-1)(n^3-5n^2+7n-1)},\\
\Delta_D-\Delta_L
&=\frac{2n(n-2)T(n)}{(n-3)(n-1)(n^2-4n+2)(n^3-5n^2+7n-1)(n^3-5n^2+8n-2)},
\end{aligned}
\]

where \(P(n)=2n^5-17n^4+49n^3-60n^2+34n-4\) and \(T(n)=3n^4-8n^3-13n^2+40n-14\). Each numerator is positive for \(n\ge4\): after replacing \(n\) by \(t+4\), the respective polynomial factors have positive coefficient vectors

\[(2,23,97,176,114,4),\quad(2,13,14),\quad(5,25,26),\quad(3,40,179,320,194).\]

(Each vector is ordered from highest to constant power of \(t\).) Consequently \(\Delta_I\) is always strictly greatest and \(\Delta_L\) strictly least, and it remains only to compare the two middle classes. Direct cancellation gives

\[
\Delta_D-\Delta_R=
-\frac{4(n^3-14n^2+34n-12)}{(n-3)(n-2)(n^2-4n+2)(n^3-5n^2+8n-2)}.
\]

The cubic \(p(n)=n^3-14n^2+34n-12\) is negative at each integer \(n=4,\ldots,11\), with \(p(11)=-1\), whereas

\[p(12+t)=t^3+22t^2+130t+108>0\quad(t\ge0).\]

This establishes both strict rankings and the sharp transition at \(n=12\). Finally, choosing an incident pair means choosing its shared vertex among \(2n\) vertices and two distinct incident edges among \(n-1\); each pair is counted exactly once, so the number of maximizers is \(2n\binom{n-1}{2}\). \(\square\)

## Verification

The accompanying `crown_verify.py` uses exact SymPy rational arithmetic. It independently regenerates all four rational functions from the spectral projection kernel, checks the positive coefficient certificates and the \(n=12\) cubic sign, and performs **every unordered two-edge deletion** for \(n=4,5,6,7\) using direct inverses of reduced Laplacians (respectively 66, 190, 435, and 861 pairs). Every direct inverse agrees with the appropriate formula. Run `python crown_verify.py` after installing the dependency in `requirements.txt`; the execution output is in `VERIFY_OUTPUT.txt`. These finite instances are independent consistency checks, not a substitute for the proof for every \(n\).

## Relationship to prior work

Schaub–Lehmann–Yaliraki–Barahona [1], sections 2 and A, develop edge-failure flow redistribution through Laplacian pseudoinverses and Sherman–Morrison updates. Their object is the transfer of network flows after line outages; the inspected full text does not present a four-class crown-graph Kirchhoff-index damage ranking. Klee–Stamps [2], Proposition 8, derive the **undeleted** crown Laplacian spectrum, used as an input here; it does not order or calculate the four joint deletion damages. The general complete-graph-with-defects treatment [3] uses related resolvent methods, but its complete-graph baseline, optimization parameters, and stated conclusions differ; no statement there gives the present fixed crown graph's sharp second-place switch. The formula for pairwise effective resistance or a single-edge failure alone is not the same optimization as the two-edge damage comparison. The three-dimensional hypercube, isomorphic to \(\mathrm{Cr}_4\), is a known special case of earlier two-link work and is not represented as independently new; the claim includes a distinct infinite-family ranking and a threshold at 12.

## Limitations

The claim assumes equal positive unit conductances, exactly two existing edge failures, and \(n\ge4\); it does not classify weighted crowns, three failures, or disconnected Kirchhoff indices. The positive review here is a mathematical self-review, not independent audit. Exhaustive electronic checks stop at \(n=7\); the analytical proof handles all larger dimensions. Although the cited core primary results have been inspected in full text and multiple relevant records compared, unindexed or otherwise unidentified equivalent literature remains possible.

## References

1. M. T. Schaub, J. Lehmann, S. N. Yaliraki, and M. Barahona, *Structure of complex networks: Quantifying edge-to-edge relations by failure-induced flow redistribution*, arXiv:1303.6241, first publicly submitted 2013-03-25, section 2 and Appendix A. https://arxiv.org/html/1303.6241v3
2. S. Klee and M. T. Stamps, *Eigenvalues of graph Laplacians via rank-one perturbations*, arXiv:2008.01669, first publicly submitted 2020-08-04, Proposition 8 (crown spectrum). https://arxiv.org/html/2008.01669v1
3. S. Tamura, *Edge-defect matrices and stability of the Kirchhoff index for complete graphs with deleted edges*, arXiv:2608.05924 (2026); paper's general complete-graph defect framework and distinct global extremal problem. https://arxiv.org/abs/2608.05924
