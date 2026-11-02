# Discounted hitting domination of biased cyclic walks and a sharp drift-induced coverage gain

## Finding

Let \(n\ge3\), \(0<p<1\), \(0<\lambda<1\), and \(0<\tau\le1\). On the labelled cycle with vertices \(\mathbb Z/n\mathbb Z\), let a walk jump clockwise with probability \(p\) and counterclockwise with probability \(1-p\). For a nonempty pinned set \(S\), put \(h_v(S)=\mathbb E_v[\lambda^{T_S}]\), where \(T_S\) is the first time the walk hits \(S\). A set is feasible when \(h_v(S)\ge\tau\) at every vertex. The discounted hitting domination number \(\delta_{\lambda,\tau,p}(C_n)\) is the minimum size of a feasible set.

Put \(q=1-p\), \(\Delta=\sqrt{1-4\lambda^2pq}\), and
\[
 r_- = \frac{1-\Delta}{2\lambda p},\qquad
 r_+ = \frac{1+\Delta}{2\lambda p}.
\]
For every integer \(L\ge2\), define
\[
 u_{L,j}=\frac{(r_+^L-1)r_-^j+(1-r_-^L)r_+^j}{r_+^L-r_-^L}
 \quad (1\le j<L),\qquad
 H(L)=\min_{1\le j<L}u_{L,j},\quad H(1)=1.
\]
Then \(H(1)>H(2)>H(3)>\cdots>0\) and \(H(L)\to0\). Consequently
\[
 R=\max\{L\ge1:H(L)\ge\tau\}
\]
is finite. A nonempty set \(S\) is feasible **if and only if** every positive clockwise gap between successive elements of \(S\) is at most \(R\), including the sole gap of length \(n\) when \(|S|=1\). In particular,
\[
 \delta_{\lambda,\tau,p}(C_n)=\left\lceil\frac nR\right\rceil.
\]
The complete labelled feasible-set cardinality polynomial is
\[
 \mathcal D_{n,\lambda,\tau,p}(z)=
 \sum_{k=1}^{n}\frac nk[x^n](x+x^2+\cdots+x^R)^k z^k.
\]
Every minimum set consists precisely of \(\lceil n/R\rceil\) cyclic gaps in \(\{1,\ldots,R\}\), and its number is the corresponding coefficient above. This is a complete answer for all real parameters in the stated ranges, not only rational parameters.

There is also a sharp **nonreversibility phenomenon** at the first gap where drift can help. For \(\lambda=1/2\), the largest achievable worst-vertex support on a four-edge gap, as the bias \(p\) varies, is
\[
 \max_{0<p<1}H(4)=\frac{7-\sqrt{17}}{16} > \frac17=H_{p=1/2}(4),
\]
and the only maximizers are
\[
 p=\frac{\sqrt{17}-1}{4}\quad\text{and}\quad
 p=\frac{5-\sqrt{17}}4.
\]
For gaps of lengths one through three, no bias beats the unbiased walk. At the concrete threshold \((\lambda,\tau)=(1/2,1/6)\), the unbiased and optimally biased cyclic walks have, for every \(n\ge3\), the genuinely different sharp source requirements
\[
 \delta_{1/2,1/6,1/2}(C_n)=\left\lceil n/3\right\rceil,
 \qquad
 \delta_{1/2,1/6,(\sqrt{17}-1)/4}(C_n)=\left\lceil n/4\right\rceil.
\]
Thus a homogeneous directional bias lowers the asymptotic minimum source density from \(1/3\) to \(1/4\) without changing the underlying cycle or fidelity.

## Assumptions and scope

The graph is a *labelled* simple cycle of order at least three; vertices are labelled by residues, so rotation or reflection does not identify source subsets. Transitions are nearest-neighbour and translation-invariant, with clockwise probability strictly between zero and one and identical per-step discount strictly between zero and one. Pinned vertices have support exactly one; all other supports satisfy the discounted hitting equation. The threshold lies in \((0,1]\). No assertion is made for arbitrary jump kernels, vertex-dependent discounts, or unpinned empty source sets.

## Proof

**Step 1 (local first-hitting solution).** If consecutive pinned vertices have positive clockwise separation \(L\), an interior point with offset \(j\) cannot hit any other pinned vertex before hitting one of these endpoints: every nearest-neighbour path leaving that arc first encounters an endpoint. Its support satisfies
\[
 u_0=u_L=1,\qquad
 u_j=\lambda\bigl(q u_{j-1}+p u_{j+1}\bigr)
 \quad(1\le j<L).
\]
The associated characteristic equation is \(\lambda p r^2-r+\lambda q=0\). Its discriminant is positive and its roots satisfy \(0<r_-<1<r_+\), as follows from the polynomial's positive value at zero, negative value at one, and positive leading coefficient. Substitution of \(A r_-^j+B r_+^j\), with \(A+B=1\) and \(A r_-^L+B r_+^L=1\), gives exactly \(u_{L,j}\) displayed above. Strict diagonal dominance of the tridiagonal system, or contraction of the discounted transition map, proves uniqueness. The argument also works for a singleton source: the two formal endpoints represent the same pinned vertex and the unique intervening arc traverses the whole cycle.

**Step 2 (strict decrease and existence of \(R\)).** For \(L=1\) there are no interior points and \(H(1)=1\), whereas \(H(2)=\lambda<1\). For \(L\ge2\), compare the Dirichlet solutions on \([0,L]\) and \([0,L+1]\), both with terminal support one. In the larger interval the value at position \(L\) is strictly below one because its first hitting time is positive. The maximum principle (equivalently, the positive first-hit interpolation weights) shows that at every common interior position the longer-interval solution is strictly below the shorter-interval solution. Hence \(H(L+1)<H(L)\). From a middle vertex of a gap of length \(L\), hitting either endpoint requires at least \(\lfloor L/2\rfloor\) jumps. Therefore \(H(L)\le\lambda^{\lfloor L/2\rfloor}\to0\), establishing a unique finite admissible-gap cutoff \(R\).

**Step 3 (global feasibility and extremum).** The source vertices partition the cycle into clockwise arcs. First hits from an interior vertex occur at the endpoints of its arc, so its support equals the local solution from Step 1. Thus the uniform threshold holds exactly when every arc has length at most \(R\). For a set of \(k\) sources, the \(k\) positive arc lengths sum to \(n\). Feasibility requires \(n\le kR\), whereas \(k=\lceil n/R\rceil\) positive parts of \(n\), each at most \(R\), always exist. This proves the formula for \(\delta\) and characterizes every minimizer.

**Step 4 (full enumeration).** Ordered compositions of \(n\) into \(k\) parts between one and \(R\) are counted by \([x^n](x+\cdots+x^R)^k\). Choose any of \(n\) labels as the initial marked source and follow the ordered parts clockwise. Each actual labelled set of size \(k\) is represented exactly \(k\) times, once per marked source. This proves the polynomial coefficient formula, including the singleton case and the all-vertices case.

**Step 5 (the sharp four-gap bias).** Fix \(\lambda=1/2\). Reversal of the cycle exchanges \(p\) and \(1-p\), so assume \(p\ge1/2\). Direct solution of the three internal equations for a four-edge gap yields
\[
 u_{4,1}=\frac{2p^2-5p+4}{4(p^2-p+2)},\quad
 u_{4,2}=\frac{2p^2-2p+1}{2(p^2-p+2)},\quad
 u_{4,3}=\frac{2p^2+p+1}{4(p^2-p+2)}.
\]
Now \(u_{4,3}-u_{4,1}=3(2p-1)/[4(p^2-p+2)]\ge0\), so \(H(4)=\min(u_{4,1},u_{4,2})\). Their derivatives are
\[
 u'_{4,1}=\frac{3(p^2-2)}{4(p^2-p+2)^2}<0,
 \qquad
 u'_{4,2}=\frac{3(2p-1)}{2(p^2-p+2)^2}\ge0.
\]
Their unique crossing in \([1/2,1]\) solves \(2p^2+p-2=0\), giving \(p_*=(\sqrt{17}-1)/4\) and \(H_{p_*}(4)=(7-\sqrt{17})/16\). Reversal gives the other maximizer. For gap length two, \(H(2)=1/2\) independent of \(p\). For gap three, \(H(3)=(p^2-2p+2)/(p^2-p+4)\) on \([1/2,1]\), whose derivative \((p^2+4p-6)/(p^2-p+4)^2\) is negative there. Thus no shorter gap benefits from drift.

For the claimed threshold, the unbiased walk has \(H(3)=1/3\) and \(H(4)=1/7\), hence \(R=3\). At \(p=p_*\), \(H(4)=(7-\sqrt{17})/16>1/6\). The value at interior offset two of a five-edge gap is
\[
 u_{5,2}(p_*)=\frac{4097-731\sqrt{17}}{13324}<\frac16.
\]
Therefore \(H(5)\le u_{5,2}(p_*)<1/6\). By strict decrease, \(R=4\). Substitution into Step 3 gives the two exact source requirements.

## Verification

Run the standalone, standard-library-only program `python3 verify_biased_cycles.py`. It independently solves the full pinned cycle system by exact rational Gaussian elimination and checks every nonempty source subset for \(3\le n\le9\) at four rational \((p,\lambda)\) pairs, comparing its floor with the separate interval solution. It checks all cardinality coefficients at seven rational thresholds, independently verifies the characteristic-root formula numerically against those exact rational values, and checks the algebraic critical-bias inequalities at high decimal precision. The successful check covered 4,036 source subsets and 196 cycle/parameter/threshold combinations. These bounded calculations corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work

Allagan, Pereyra, and Massey introduced the discounted hitting domination parameter and developed exact transfer methods for homogeneous *unbiased* walks on paths and spider trees, together with results for complete graphs, stars, algorithms, and complexity. Their first-public version is arXiv:2609.31535v1, dated September 25, 2026. Its gap threshold for unbiased paths motivates the problem; the present new result covers the nonreversible translation-invariant biased walk on cycles, provides a complete labelled feasible-set enumerator, and identifies an exact algebraic bias that improves worst-case uniform coverage and the required source density. The classical birth-death Dirichlet recurrence and the cyclic-composition count are acknowledged as standard ingredients, not independent innovations.

Earlier literature on group hitting probability and random-walk target selection addresses evaluating or optimizing different hitting objectives. No assertion of exhaustive historical priority is made; non-indexed results or equivalents under other terminology remain a residual risk. The direct comparison is between theorem statements and implications: the published unbiased transfer threshold does not determine \(u_{4,j}\) or the optimized \(p_*\) for nonreversible walks.

## Limitations

The exact classification assumes a homogeneous clockwise bias on a one-dimensional nearest-neighbour cycle. It does not establish the same source density for general directed graphs, inhomogeneous transition kernels, or variable discount factors. The numerical verifier checks only the stated finite domain; independence of external mathematical review has not been claimed. The result's historical-priority status remains provisional pending broader expert evaluation.

## References

1. J. D. Allagan, K. Pereyra, and W. A. Massey, *Discounted Hitting Domination on Graphs with Submodularity, Complexity and Exact Algorithms*, arXiv:2609.31535v1 (first public September 25, 2026), https://arxiv.org/abs/2609.31535.
2. Q. Guo, D. Lin, S. Wang, R. C.-W. Wong, and W. Lin, *Efficient Algorithms for Group Hitting Probability Queries on Large Graphs*, IEEE Transactions on Knowledge and Data Engineering 36 (2024), 2995–3008, doi:10.1109/TKDE.2023.3349164.
3. R.-H. Li, J. X. Yu, X. Huang, and H. Cheng, *Random-walk domination in large graphs: problem definitions and fast solutions*, arXiv:1302.4546 (2013), https://arxiv.org/abs/1302.4546.
