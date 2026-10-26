# Exact interval geometry and sharp stability of the continuous proportional veto core on a line

## Finding

**Theorem (complete line-continuum proportional veto core).** Fix an integer \(n\ge 1\) and voter peaks \(0\le p_1\le\cdots\le p_n\le1\), with repetitions permitted. Alternatives are all real points in \([0,1]\), supplied with uniform Lebesgue probability. Each voter strictly prefers an alternative \(y\) to \(x\) precisely when \(|y-p_i|<|x-p_i|\). For any \(\varepsilon\ge0\), define
\[
q_j=1-\frac jn+\varepsilon,\qquad r_j=\frac{j-1}{n}+\varepsilon\quad (1\le j\le n).
\]
Then the complete \(\varepsilon\)-proportional veto core is **exactly** the nonempty closed interval
\[
\mathcal C_\varepsilon=[L_\varepsilon,U_\varepsilon],\qquad
L_\varepsilon=\max\!\left\{0,\max_{1\le j\le n}\min\!\left(1-r_j,p_j-\frac{r_j}{2}\right)\right\},
\]
\[
U_\varepsilon=\min\!\left\{1,\min_{1\le j\le n}\max\!\left(q_j,p_j+\frac{q_j}{2}\right)\right\}.
\]
For initially unsorted peaks, these endpoints and the whole core can be computed with \(O(n\log n)\) comparisons and arithmetic operations, or with \(O(n)\) operations after sorting.

**Sharp stability.** If two labeled peak lists of equal length obey \(\max_i|p_i-p_i'|\le\delta\), the two resulting cores obey
\[
d_{\rm H}(\mathcal C_\varepsilon,\mathcal C_\varepsilon')\le\delta
\qquad\text{for every }\varepsilon\ge0,
\]
where \(d_{\rm H}\) is Hausdorff distance on nonempty compact subsets of the line. The coefficient \(1\) is optimal even at \(\varepsilon=0\).

## Assumptions and scope

A coalition \(T\) is a **blocking coalition** for alternative \(x\) if it is nonempty and the Lebesgue probability of its set of unanimously strictly preferred alternatives exceeds \(1-|T|/n+\varepsilon\). The \(\varepsilon\)-proportional veto core consists of all alternatives with no blocking coalition. Importantly, the blocking inequality is **strict**. At a boundary with equality, the coalition does *not* block. This convention matches the definition of the \(\varepsilon\)-proportional veto core in the motivating work.

The alternative space is the full closed interval and the alternative distribution is uniform; voters' distances are one-dimensional Euclidean distances. Multiplicities of identical peaks and voters whose peak equals \(x\) are allowed. Ties at a finite number of alternatives do not affect the preferred-set probability because Lebesgue measure is atomless. No assertion is made for nonuniform alternative distributions, multidimensional spaces, other preference metrics, or alternative distributions having atoms.

## Proof

**Step 1: Characterize unanimous improvements.** For a voter at peak \(p<x\), the alternatives strictly preferred to \(x\) form the interval \((2p-x,x)\cap[0,1]\), whose length is \([\min(x,2(x-p))]_+\), where \([t]_+=\max(t,0)\). A voter with \(p>x\) strictly prefers \((x,2p-x)\cap[0,1]\), of length \([\min(1-x,2(p-x))]_+\). A voter with \(p=x\) has no strict improvement. If a coalition contains peaks strictly on both sides of \(x\), its common strictly preferred set is empty. Thus any coalition that blocks has every member strictly on the same side of \(x\).

**Step 2: Reduce arbitrary coalitions to ordered prefixes or suffixes.** Let \(T\) be a coalition with peaks left of \(x\), and let \(j\) index its rightmost peak. Replacing \(T\) by the first \(j\) voters does not shrink its unanimous improvement interval: each additional peak is no farther right, so its left interval includes the rightmost peak's interval. The replacement weakly increases the size of the coalition, lowering the threshold for blocking. Accordingly, a left coalition blocks if and only if one of the first-\(j\) prefixes blocks. Dually, for right-side coalitions, it suffices to examine suffixes from voter \(j\) to voter \(n\).

Define for all \(j\) and \(x\)
\[
\lambda_j(x)=\bigl[\min\{x,2(x-p_j)\}\bigr]_+,
\qquad
\rho_j(x)=\bigl[\min\{1-x,2(p_j-x)\}\bigr]_+.
\]
For a prefix of length \(j\), the blocking threshold is \(1-j/n+\varepsilon=q_j\). For a suffix of length \(n-j+1\), it is \(1-(n-j+1)/n+\varepsilon=r_j\). Checking also the artificial prefixes/suffixes when their extreme peak is on the wrong side is harmless: the corresponding \(\lambda_j\) or \(\rho_j\) is zero and the threshold is nonnegative. Thus \(x\) is in the core precisely when
\[
\lambda_j(x)\le q_j\quad\text{and}\quad \rho_j(x)\le r_j\qquad(1\le j\le n).
\]
These are equivalences, not merely sufficient conditions.

**Step 3: Solve every inequality exactly.** Since \(q_j\ge0\),
\[
\bigl[\min\{x,2(x-p_j)\}\bigr]_+\le q_j
\iff\min\{x,2(x-p_j)\}\le q_j
\iff x\le\max\!\left(q_j,p_j+\frac{q_j}{2}\right).
\]
Likewise, since \(r_j\ge0\),
\[
\bigl[\min\{1-x,2(p_j-x)\}\bigr]_+\le r_j
\iff x\ge\min\!\left(1-r_j,p_j-\frac{r_j}{2}\right).
\]
Intersection with \([0,1]\) gives exactly the displayed interval. In particular, no possible non-prefix or mixed coalition imposes another restriction.

**Step 4: Prove the interval is never empty.** Write \(a_j=\min(1-r_j,p_j-r_j/2)\) and \(b_k=\max(q_k,p_k+q_k/2)\). For any \(j\le k\), we have \(a_j\le p_j\le p_k\le b_k\). For any \(j>k\), using \(\varepsilon\ge0\),
\[
a_j\le1-r_j=1-\frac{j-1}{n}-\varepsilon
\le1-\frac kn+\varepsilon=q_k\le b_k.
\]
Therefore \(a_j\le b_k\) for all pairs \(j,k\). Also \(a_j\le1\) and \(b_k\ge0\), so \(L_\varepsilon\le U_\varepsilon\). This establishes nonemptiness, including the unrelaxed case \(\varepsilon=0\), even though unrelaxed cores may be empty for general infinite alternative spaces.

**Step 5: Compute and establish sharp perturbation stability.** Sorting is nonexpansive under coordinatewise \(\ell_\infty\) perturbations: if every labeled peak moves by at most \(\delta\), each order statistic moves by at most \(\delta\). Each function \(p\mapsto\min(1-r_j,p-r_j/2)\) and \(p\mapsto\max(q_j,p+q_j/2)\) is \(1\)-Lipschitz. Taking finite minima, maxima, and the constant cutoffs \(0,1\) preserves the same bound. Therefore both endpoints shift by at most \(\delta\). For nonempty closed intervals, their Hausdorff distance is the maximum absolute displacement of corresponding endpoints, proving the inequality. If all voters share a peak \(p\), then \(\mathcal C_0=\{p\}\): the first suffix gives lower bound \(p\), and the last prefix gives upper bound \(p\). Moving all peaks from \(p\) to \(p+\delta\) within \([0,1]\) attains distance \(\delta\), proving optimality.

## Verification

The accompanying `pvc_interval_checker.py` uses exact rational arithmetic. It enumerates all nonempty coalitions over small finite grids, computes their common strictly preferred interval lengths, and compares the resulting core-membership decisions to the closed-form endpoint test. It also checks rational randomly sampled larger configurations and perturbation inequalities, producing **26,874 exact checks**. Execute `python pvc_interval_checker.py` with the standard Python library; no other dependencies are needed. Finite checks corroborate the proof and are not substituted for the universal arguments above.

Exact illustrations for \(\varepsilon=0\): three peaks \((0,0,1)\) give the singleton \(\{1/3\}\); two extreme peaks \((0,1)\) give \(\{1/2\}\); peaks \((2/5,3/5)\) give \([2/5,3/5]\); peaks \((1/4,1/2,3/4)\) give \([1/3,2/3]\).

## Relationship to prior work

Chooi, Gölz, Procaccia, Schiffer, and Zhang introduce \(\varepsilon\)-PVC over potentially infinite alternatives, establish an existence/measure guarantee for positive relaxation, and provide a general infinite-alternative example with empty unrelaxed core. Their finite-alternative computation does not imply this continuum line formula. This theorem resolves the structural case of Euclidean single-peaked voters and uniformly distributed alternatives, including the exact unrelaxed core and optimal perturbation constant.

Kizilkaya and Kempe study finite weighted generalized-veto cores and convexity of particular matched-winner sets. This does not entail convexity, explicit endpoints, or Lipschitz stability for the *whole* continuous interval-alternative PVC. Ianovski and Kondratev, and Kondratev and Ianovski, analyze computation and axioms for finite alternatives. Moulin's classical proportional-veto work underlies the concept; its full original text was not available for direct inspection, so historical priority cannot be declared certain. No independence or external verification is asserted.

## Limitations

The interval conclusion uses both one-dimensional distance preferences and uniform Lebesgue alternatives. No claim is made for arbitrary voter rankings or higher-dimensional Euclidean spaces. Hausdorff robustness concerns changes to peaks with fixed electorate size and fixed uniform alternative distribution, not variation in the distribution or voter count. The mathematical proof is complete under its assumptions, while novelty remains subject to historical-priority research and independent review.

## References

1. J. Chooi, P. Gölz, A. D. Procaccia, B. Schiffer, and S. Zhang, *Finding Common Ground in a Sea of Alternatives*, arXiv:2603.16751v1, first public March 17, 2026. https://arxiv.org/abs/2603.16751
2. F. E. Kizilkaya and D. Kempe, *Generalized Veto Core and a Practical Voting Rule with Optimal Metric Distortion*, arXiv:2305.19632. https://arxiv.org/abs/2305.19632
3. E. Ianovski and A. Kondratev, *Computing the Proportional Veto Core*, arXiv:2003.09153. https://arxiv.org/abs/2003.09153
4. A. Kondratev and E. Ianovski, *Veto Core Consistent Preference Aggregation*, AAMAS 2024.
5. H. Moulin, *The Proportional Veto Principle*, Review of Economic Studies 48 (1981), 407–416. DOI: 10.2307/2297154. Original full text not inspected.
