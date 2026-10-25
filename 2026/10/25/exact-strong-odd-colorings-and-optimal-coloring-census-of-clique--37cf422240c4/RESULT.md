# Exact strong odd colorings and optimal-coloring census of clique windmills

## Finding

For every pair of integers \(m\ge1\) and \(s\ge2\), let the clique windmill \(W_{m,s}=K_1\vee(mK_s)\) consist of \(m\) pairwise vertex-disjoint labeled cliques on \(s\) vertices and one universal hub. Put
\[
q_{m,s}=\begin{cases}s,&m\text{ odd},\\2\left\lceil\dfrac{ms}{2(m-1)}\right\rceil,&m\text{ even}.\end{cases}
\]
Then its strong odd chromatic number is \(\chi_{\mathrm{so}}(W_{m,s})=q_{m,s}+1\). Moreover, the number of optimal colorings with a fixed palette of \(q_{m,s}+1\) *named* colors (all used) is
\[
N_{m,s}=\frac{(q+1)(s!)^m}{2^q}\sum_{j=0}^q(-1)^j\binom qj\left(\sum_{\ell=0}^s(-1)^\ell\binom j\ell\binom{q-j}{s-\ell}\right)^m,\qquad q=q_{m,s}.
\]
Out-of-range binomial coefficients vanish. In particular, for odd \(m\), \(N_{m,s}=(s+1)(s!)^m\). For \(m=2\), \(N_{2,s}=(2s+1)!\). For even \(m\ge2\) with \(s=2\), \(N_{m,2}=\frac58(12^m+3\cdot4^m)\).

## Assumptions and scope

Graphs are finite, simple, and vertex-labeled. A strong odd coloring is a proper vertex coloring in which, at each vertex, the multiplicity of every color occurring in its open neighborhood is odd. The hub and every clique vertex are distinct labeled vertices, and palette labels are also distinct. The statement is valid for every integer \(m\ge1\), \(s\ge2\); no asymptotic or probabilistic hypotheses occur. The count distinguishes color names, rather than quotienting by color permutations or graph automorphisms.

## Proof

The hub is adjacent to every other vertex, so its color is excluded from all blades. Inside each clique of order \(s\), properness requires \(s\) distinct non-hub colors. At a blade vertex, all its neighbors—its \(s-1\) clique mates and the hub—have pairwise distinct colors. Hence the strong odd condition holds automatically at all non-hub vertices.

With \(q\) non-hub colors, let \(B\) be the \(m\)-by-\(q\) binary matrix whose row \(i\) indicates the colors used on blade \(i\). Each row has sum \(s\). At the hub, the strong odd condition says every column sum is either zero or odd; for a palette that uses all \(q\) non-hub colors, every column sum is *positive and odd*. Thus the coloring problem is exactly the existence and enumeration of such matrices, multiplied by \((s!)^m\) ways to assign a chosen row's colors to labeled clique vertices and \(q+1\) choices of hub color.

If \(m\) is odd, each row requires \(q\ge s\), and \(q=s\) works by using the same \(s\) colors on all \(m\) blades: each column has odd sum \(m\). If \(m\) is even, every positive odd column sum is at most \(m-1\), whence \(ms\le q(m-1)\); furthermore \(q\equiv ms\equiv0\pmod2\), since the sum of \(q\) odd integers has parity \(q\). Therefore \(q\ge2\lceil ms/(2(m-1))\rceil\). This bound is at least \(s\), and equality can be attained: choose \(q\) odd column sums in \([1,m-1]\) totaling \(ms\). They exist because \(q\le ms\le q(m-1)\) and the difference \(ms-q\) is even; start all at \(1\) and distribute units of \(2\) up to \(m-1\).

These prescribed column sums are realizable with all \(m\) row sums equal to \(s\). Indeed, the Gale–Ryser degree-sequence criterion for a binary matrix requires, besides equal total sums, \(ks\le\sum_{j=1}^q\min(k,d_j)\) for each \(1\le k\le m\). Because \(0\le d_j\le m\), \(\min(k,d_j)\ge kd_j/m\); summing gives \(\sum_j\min(k,d_j)\ge (k/m)ms=ks\). This proves existence and therefore the asserted sharp chromatic number.

For enumeration, choose an unordered \(s\)-element subset of \(q\) colors in each row. For a sign vector \(\epsilon=(\epsilon_1,\ldots,\epsilon_q)\in\{\pm1\}^q\), put \(E_s(\epsilon)=\sum_{|S|=s}\prod_{i\in S}\epsilon_i\). The indicator that *every* color appears an odd number of times in the \(m\) chosen subsets equals \(2^{-q}\sum_{\epsilon}\prod_i\epsilon_i\prod_{\text{rows }S}\prod_{i\in S}\epsilon_i\). Summing over all row subsets yields \(2^{-q}\sum_{\epsilon}(\prod_i\epsilon_i)E_s(\epsilon)^m\). Grouping sign vectors by the number \(j\) of their negative coordinates gives the displayed double binomial sum. Since positive odd occurrences imply every non-hub palette color is used, every counted coloring uses all \(q+1\) colors. Multiplication by the hub choice and the \((s!)^m\) within-blade permutations completes the enumeration.

When \(m\) is odd, \(q=s\) forces every row to be the full palette, yielding \((s+1)(s!)^m\). When \(m=2\), odd positive column counts must all equal one, so the two blade palettes are disjoint and all \(2s\) colors are used exactly once, yielding \((2s+1)!\). When \(s=2\) and \(m\) is even, \(q=4\). In the sign sum, \(E_2=6\) for zero or four negative signs, \(E_2=0\) for one or three, and \(E_2=-2\) for two. The formula simplifies to \(5\cdot2^m(2\cdot6^m+6\cdot2^m)/16=5(12^m+3\cdot4^m)/8\).

## Verification

The standalone `verify.py` uses exact-integer arithmetic and standard-library routines only. It computes the parity-mask dynamic program (independently of the sign-sum formula), evaluates the Fourier formula, excludes smaller palettes, and performs direct enumeration of assignments to labeled vertices in selected small cases. Running `python verify.py` yields `VERIFICATION_OK`. These finite checks corroborate rather than replace the all-parameter proof.

## Relationship to prior work

Kwon and Park introduced strong odd coloring and proved bounds for sparse graphs [1]. Caro, Petruševski, Škrekovski, and Tuza investigated the invariant in planar, unicyclic, and product graph classes [2]. The present result addresses a distinct clique-bouquet family and gives a complete formula and labeled optimum census. The later block-graph algorithm of Pradhan, Sharma, and Verma [3] encompasses windmills algorithmically; the available abstract guarantees computability of an optimum, not the displayed exact two-parameter count. This is a substantive scope overlap, and the full content of [3] was not available for conclusive theorem-by-theorem comparison. The same graph family has been studied for dissociation polynomials, a different invariant [4].

## Limitations

No statement of independent certification or exhaustive literature priority is made. Work not indexed or not fully accessible, particularly [3], could contain stronger or equivalent windmill statements. The result is for one-hub clique windmills, not arbitrary block graphs. The numerical verifier checks finitely many parameter pairs and is not an infinite proof.

## References

[1] H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653, first posted 2024-01-22, https://arxiv.org/abs/2401.11653.

[2] Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336, first posted 2024-10-03, https://arxiv.org/abs/2410.02336.

[3] D. Pradhan, V. Sharma and S. Verma, *On the Classical and Parameterized Complexity of Strong Odd Coloring*, arXiv:2610.01441, first posted 2026-10-01, https://arxiv.org/abs/2610.01441.

[4] *Dissociation polynomial and all maximal dissociation sets of generalized windmills*, published-finding corpus record `2026/10/4/SCOPE-dissociation-polynomial-and-all-maximal-dissociation-sets-of-gen--2c55298c97bc` (separate graph invariant).
