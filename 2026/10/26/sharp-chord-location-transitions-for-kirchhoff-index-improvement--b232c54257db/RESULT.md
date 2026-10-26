# Sharp chord-location transitions for Kirchhoff-index improvement of a path

## Finding
Let \(P_n\) be the path on labeled vertices \(1,\ldots,n\), with unit conductance on each original edge, where \(n\ge4\). Install exactly one additional edge of arbitrary prescribed conductance \(t>0\), connecting nonadjacent vertices \(i<j\). Let \(\mathcal K\) be the sum of all unordered-pair effective resistances. Define
\[
C_n(d)=\frac{d(3nd-2d^2+2)}{12},\quad
\mathcal D_n=\{n-1,n-3,n-5,\ldots\}\cap\{2,\ldots,n-1\}.
\]
Every minimizer places its new edge symmetrically: its endpoints are exactly
\[
(i,j)=\left(\frac{n-d+1}{2},\frac{n+d+1}{2}\right),
\]
where \(d\) maximizes \(C_n(d)/(d+1/t)\) over \(\mathcal D_n\). No asymmetric chord is ever optimal. The minimal index is
\[
\min_{i<j,\ j-i\ge2}\mathcal K
=\frac{n(n^2-1)}6-n\max_{d\in\mathcal D_n}\frac{C_n(d)}{d+1/t}.
\]

All transitions are explicit. For consecutive lengths \(d,d-2\in\mathcal D_n\), a positive crossing exists precisely when \(4d>3n+4\); then it occurs at
\[
t_d=\frac{6(d-1)(n+1-d)}{d(d-2)(4d-3n-4)}.
\]
These thresholds occur in *strictly increasing order* as the selected length descends by two. The optimal length starts at \(n-1\), switches to \(n-3\) at \(t_{n-1}\) if defined, then to successive lengths at the remaining positive thresholds. At each threshold exactly the two adjacent symmetric chords tie; away from thresholds the optimizer is unique. In particular, for \(4\le n\le8\) the endpoint-to-endpoint edge is uniquely optimal for every \(t>0\), whereas for every \(n\ge9\) it ceases to be optimal once
\[
t>\frac{12(n-2)}{(n-1)(n-3)(n-8)}.
\]
For example, with \(n=9\), the choice changes from endpoints \((1,9)\) to \((2,8)\) at \(t=7/4\), with both optimal exactly at the threshold.

## Assumptions and scope
The original path edges remain at conductance \(1\). Exactly one new nonexisting edge has fixed conductance \(t>0\); no other edge weight is adjustable. The graph has \(n\ge4\) labeled vertices. The Kirchhoff index is the sum over distinct unordered vertex pairs of effective resistance. The theorem includes every real positive conductance and every integer path size in the specified range; no asymptotic approximation is used.

## Proof
Put \(d=j-i\), \(l=i-1\), and \(r=n-j\); hence \(l+r=n-d-1\). Let \(L\) be the unweighted path Laplacian and \(b=e_i-e_j\). The rank-one inverse formula on the mean-zero subspace gives
\[
\mathcal K(P_n)-\mathcal K(P_n+tbb^\top)
=\frac{nt\,\lVert L^+b\rVert_2^2}{1+t\,b^\top L^+b}
=\frac{nt\,S_n(d,l,r)}{1+td},
\]
since \(b^\top L^+b=d\) for the unit-resistance path and \(\mathcal K(P_n)=n(n^2-1)/6\). The centered solution of \(Lx=b\) is obtained from the ramp taking value \(d\) to the left of \(i\), decreasing by one at every edge from \(i\) to \(j\), and equaling zero to the right of \(j\). Summing its squared centered values gives the exact identity
\[
S_n(d,l,r)=C_n(d)-\frac{d^2(l-r)^2}{4n}.
\]
For fixed \(d\), the squared imbalance is uniquely minimized by \(l=r\), when \(n-d-1\) is even, or by \(|l-r|=1\), otherwise. In the first case the symmetric chord is unique. In the second case \(S_n(d,l,r)=C_n(d)-d^2/(4n)\).

We show that every parity-mismatched length is strictly dominated. When \(d\ge3\), both neighboring lengths \(d-1\) and \(d+1\) are permitted, are parity-matched, and have unique symmetric chords. Direct calculation gives
\[
\frac{C_n(d-1)+C_n(d+1)}2-
\left(C_n(d)-\frac{d^2}{4n}\right)
=\frac{(n-d)^2}{4n}>0.
\]
Their denominators \(d-1+1/t\) and \(d+1+1/t\) average to \(d+1/t\). If both neighboring ratios were at most the mismatched ratio, averaging the inequalities after cross-multiplication would contradict this strict numerator inequality. The boundary case \(d=2\) with wrong parity requires even \(n\). Here the symmetric \(d=3\) chord strictly dominates: with \(S_2=C_n(2)-1/n\) and \(S_3=C_n(3)\), direct calculation yields
\[
S_3-S_2=\frac{(n-2)(5n-2)}{4n}>0,
\qquad \frac{S_3}{3}-\frac{S_2}{2}
=\frac{3n^2-10n+6}{12n}>0.
\]
Thus the complete optimization reduces, strictly, to the stated set \(\mathcal D_n\), proving the maximizing formula and absence of asymmetric optimizers.

To identify the transitions, compare \(d\) and \(d-2\) in \(\mathcal D_n\). Elementary expansion gives
\[
C_n(d)-C_n(d-2)=(d-1)(n+1-d)>0,
\]
\[
dC_n(d-2)-(d-2)C_n(d)
=\frac{d(d-2)(4d-3n-4)}6.
\]
Consequently, \(C_n(d)/(d+1/t)\) strictly exceeds \(C_n(d-2)/(d-2+1/t)\) for every \(t>0\) when \(4d\le3n+4\). Otherwise the higher length wins precisely when \(t<t_d\), ties at \(t_d\), and loses for \(t>t_d\).

It remains to justify that transitions cannot skip lengths. Set \(h=1/t>0\) and \(f_h(x)=C_n(x)/(x+h)\) on \(2\le x\le n-1\). Its derivative has the sign of
\[
G_h(x)=\frac{x^2(3n-4x)+h(6nx-6x^2+2)}{12}.
\]
For \(x\le3n/4\), this is positive. For \(x>3n/4\), its derivative is \(G_h'(x)=(n/2-x)(x+h)<0\). Thus \(f_h\) is strictly increasing and then, if its unique turning point falls in the interval, strictly decreasing. Samples two apart are strictly unimodal: a tie **for the maximum** is possible only between adjacent sample lengths, and any such tie is their joint global maximum. For each positive \(t_d\), the adjacent pair ties and therefore dominates all other admissible lengths. Distinct such crossings necessarily occur in increasing order as \(d\) decreases (three consecutive sampled lengths cannot tie under strict unimodality). This completes the exact staircase classification. Finally \(4(n-1)>3n+4\) is equivalent to \(n>8\), giving the nine-vertex onset and stated first threshold.

## Verification
The standalone script `verify.py` constructs each augmented graph's grounded Laplacian, performs independent Gauss–Jordan inversion over exact rational numbers, and sums all pair resistances using \(\mathcal K=n\operatorname{tr}(L_{\mathrm{ground}}^{-1})-\mathbf1^\top L_{\mathrm{ground}}^{-1}\mathbf1\). It checks the derived closed form and *the complete set of optimal chords*, including exact transition conductances and values immediately on either side, for all \(4\le n\le12\). In the recorded execution it checked 1,587 graph/conductance configurations and returned `VERIFY_OK`. These finite checks supplement, but do not replace, the analytic proof covering all \(n\) and \(t\).

## Relationship to prior work
Ghosh, Boyd, and Saberi study minimizing effective resistance by allocating a total conductance over edges of a fixed topology; their unit-path examples and fixed-graph convex optimization do not specify which nonedge of a unit path should be added under a separately fixed conductance. Yang and Jiang give extremal Kirchhoff indices among all unweighted unicyclic graphs, using other feasible graph families and without a free added-edge conductance. Zhou, Zehmakan, and Zhang derive rank-one marginal-gain formulas and algorithms for adding edges in general graphs; the full paper does not state a path-specific exact maximizing-chord classification or the rational conductance phase thresholds. A recent one-chord weighted-cycle study by Deng, Chang, and Yang addresses a distinct ring topology and near-optimality/Pareto screening; it does not provide the exact path-family classification in the inspected statements. The generic rank-one identity here is prior work, not the claimed original contribution. The new claim is the symmetric-chord exclusion, complete optimal-location classification, and strictly ordered sharp thresholds for all path orders and positive added-edge weights.

## Limitations
No claim is made for multiple added edges, adjustable original path conductances, additional vertex weights, other resistance objectives, or arbitrary base graphs. Priority beyond the examined primary literature is not independently certified. The earliest exactly evidenced journal publication day for the 2008 foundational source is 2008-02-01; an earlier conference proceedings version is dated July 24–28, 2006 but the precise first public release day of that version is not established here.

## References
1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66; DOI 10.1137/050645452; full paper https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf ; 2006 conference version https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf .
2. Y. Yang, X. Jiang, *Unicyclic graphs with extremal Kirchhoff index*, MATCH Commun. Math. Comput. Chem. 60 (2008), 107–120; full paper https://match.pmf.kg.ac.rs/electronic_versions/Match60/n1/match60n1_107-120.pdf .
3. X. Zhou, A. N. Zehmakan, Z. Zhang, *Efficient Algorithms for Minimizing the Kirchhoff Index via Adding Edges*, arXiv:2503.21409 (2025); full paper https://arxiv.org/pdf/2503.21409 .
4. J. Deng, L. Chang, Q. Yang, *Single-Chord Augmentation of Weighted Cycles for Algebraic Connectivity and Network Coherence*, arXiv:2605.24479 (2026); https://arxiv.org/pdf/2605.24479 .
