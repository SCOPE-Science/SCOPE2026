# Sharp block-norm compactness without positive near-directedness

## Finding

There is an explicit hereditary family \(\mathcal F\) of finite subsets of the positive integers such that all four conclusions hold:

1. Its combinatorial Banach space \(X_{\mathcal F}\) is \(\ell_1\) with an explicit equivalent norm, and the optimal comparison is
   \[\tfrac12\|x\|_1\leq\|x\|_{\mathcal F}\leq\|x\|_1.\]
2. Every bounded set \(A\subset X_{\mathcal F}\) is relatively norm-compact **if and only if** it is equinormed by finite subfamilies of \(\mathcal F\).
3. For each \(0\leq\lambda<1/2\) and each \(\gamma>0\), \(\mathcal F\) fails the \((\lambda,\gamma)\) weighted near-directedness condition of Gulgowski--Sawicki (2026). In particular no positive \((0,\gamma)\) sufficient condition from their Theorems 12--13 applies.
4. The block norm has the coordinatewise Kadec property: coordinatewise convergence together with convergence of the \(\mathcal F\)-norm implies convergence in that norm.

The finding is a concrete separation of a sufficient combinatorial directedness hypothesis from the compactness conclusion; it does **not** resolve the general open classification at vanishing directedness parameters.

## Assumptions and scope

The scalar field may be \(\mathbb R\) or \(\mathbb C\). Partition \(\mathbb N=\{1,2,\ldots\}\) into consecutive blocks
\[B_i=\{2^i-1,2^i,\ldots,2^{i+1}-2\},\quad i\geq1,\qquad |B_i|=2^i.\]
A finite set \(E\) is *admissible at anchor \(i\)* if \(E\cap B_h=\varnothing\) for \(h<i\), there is no restriction on \(E\cap B_i\), and
\[|E\cap B_j|\leq 2^{j-i}\qquad(j>i).\]
Let \(\mathcal F\) contain all such admissible finite sets for all anchors, including the empty set. This family is hereditary and covers the coordinates. Complete finitely supported scalar sequences in
\[\|x\|_{\mathcal F}=\sup_{E\in\mathcal F}\sum_{n\in E}|x_n|.\]
For a nonnegative list of \(m\) numbers, \(\Lambda_k\) denotes the sum of its \(k\) largest entries, where \(0\leq k\leq m\). For a finite subfamily \(\mathcal B\subset\mathcal F\), let
\[p_{\mathcal B}(x)=\max_{E\in\mathcal B}\sum_{n\in E}|x_n|,\qquad p_\varnothing=0.\]
A bounded \(A\) is *equinormed* when for every \(\varepsilon>0\) a finite \(\mathcal B\subset\mathcal F\) satisfies \(\|x\|_{\mathcal F}-p_{\mathcal B}(x)<\varepsilon\) for all \(x\in A\). No compactness of the combinatorial family itself is assumed.

## Proof

**1. Exact block formula and sharp comparison.** For \(x\in\ell_1\), write \(x^{(j)}=x|_{B_j}\) and put
\[A_i(x)=\|x^{(i)}\|_1+\sum_{j>i}\Lambda_{2^{j-i}}\bigl((|x_n|)_{n\in B_j}\bigr).\]
Because the admissibility caps are independent between blocks and only finitely many blocks are used at once, optimizing finite sets at each fixed anchor gives
\[\boxed{\ \|x\|_{\mathcal F}=\sup_{i\geq1}A_i(x).\ }\tag{1}\]
For \(x\ne0\), this supremum is attained: \(A_i(x)\leq\sum_{j\geq i}\|x^{(j)}\|_1\to0\), while the norm is positive. In any list of \(2^j\) nonnegative entries, the sum of the \(2^{j-1}\) largest is at least half the total. Hence \(A_1(x)\geq\frac12\|x\|_1\), and the opposite comparison follows from sums over subsets. Thus the completion is exactly \(\ell_1\) as a set, with an equivalent norm.

The upper comparison is attained on coordinate vectors. For \(k\geq1\), define a vector supported on \(B_1\cup\cdots\cup B_k\), with the value \(1/(k2^j)\) in each coordinate of \(B_j\). It has \(\ell_1\)-norm \(1\), and formula (1) gives
\[A_i(x)=\frac{1}{k}+\frac{k-i}{k2^i}\quad(1\leq i\leq k),\]
whose maximum is \((k+1)/(2k)\), at \(i=1\). Letting \(k\to\infty\) proves optimality of \(1/2\).

**2. Coordinatewise Kadec property.** Let \(x_m\to x\) coordinatewise and \(\|x_m\|_{\mathcal F}\to\|x\|_{\mathcal F}\). If \(x=0\), the norm equivalence immediately gives \(\ell_1\)-convergence. Otherwise choose an anchor \(i\) realizing \(A_i(x)=\|x\|_{\mathcal F}\). For any integer \(J>i\), write \(A_i^{\leq J}\) for the finite-block truncation. An average-of-largest-entries inequality says
\[\Lambda_{2^{j-i}}\bigl((|y_n|)_{n\in B_j}\bigr)\geq 2^{-i}\|y^{(j)}\|_1\qquad(j>i).\tag{2}\]
Consequently, for every \(m\),
\[2^{-i}\sum_{j>J}\|x_m^{(j)}\|_1\leq\|x_m\|_{\mathcal F}-A_i^{\leq J}(x_m).\]
The truncated term is continuous in finitely many coordinates. Taking the upper limit as \(m\to\infty\) yields
\[\limsup_m\sum_{j>J}\|x_m^{(j)}\|_1\leq 2^i\bigl(A_i(x)-A_i^{\leq J}(x)\bigr).\tag{3}\]
The right side tends to zero as \(J\to\infty\). The finite-block part already converges in \(\ell_1\); (3) and the \(\ell_1\) tail of \(x\) show \(\|x_m-x\|_1\to0\), hence \(\|x_m-x\|_{\mathcal F}\to0\).

**3. Compactness criterion.** Suppose \(A\) is bounded and equinormed. Any sequence in \(A\) has a coordinatewise convergent subsequence by diagonal extraction. Norm equivalence and Fatou's lemma ensure the coordinatewise limit \(x\) belongs to \(\ell_1\). On this subsequence, for every \(\varepsilon>0\), choose \(\mathcal B\) equinorming all of \(A\). Since \(p_{\mathcal B}\) depends on finitely many coordinates,
\[\limsup_m\|x_m\|_{\mathcal F}\leq p_{\mathcal B}(x)+\varepsilon\leq\|x\|_{\mathcal F}+\varepsilon.\]
Coordinatewise lower semicontinuity of (1) gives \(\|x\|_{\mathcal F}\leq\liminf_m\|x_m\|_{\mathcal F}\). Thus norms converge, and step 2 gives norm convergence. Every sequence has a convergent subsequence: \(A\) is relatively compact. Conversely, any relatively compact \(A\) has a finite small norm-net; approximate each net point's norm by one admissible set, take their finite union, and use \(|p_{\mathcal B}(y)-p_{\mathcal B}(z)|\leq\|y-z\|_{\mathcal F}\) to obtain uniform equinorming.

**4. Failure of positive near-directedness.** Fix \(0\leq\lambda<1/2\) and \(\gamma>0\). Choose \(i\) so large that \(2^{-i}<\gamma\), and let \(D=B_i\in\mathcal F\). Given any cutoff \(N\), take \(j>i\) with \(B_j\subset(N,\infty)\) and \(B=B_j\in\mathcal F\). Assign uniform normalized weight to each of \(D\) and \(B\). Any \(C\in\mathcal F\) with
\[|C\cap D|/|D|\geq1-\lambda>1/2\]
can only be admissible at anchor \(i\): anchors \(h<i\) capture at most \(2^{i-h}\leq2^{i-1}\) points of \(D\), and anchors \(h>i\) capture none. At anchor \(i\), however, \(|C\cap B|/|B|\leq2^{j-i}/2^j=2^{-i}<\gamma\). So no \(C\) has both required weighted captures, even with arbitrarily remote \(B\). This contradicts the \((\lambda,\gamma)\) condition for all such parameters.

## Verification

A standalone Python 3 checker (`checker.py`) enumerates all \(7{,}450\) admissible subsets of three blocks of sizes \(2,4,8\), compares the exact formula to exhaustive maxima for deterministic signed vectors, and checks rational sharpness witnesses and combinatorial capacity inequalities. It reports 693 exact assertions. These finite experiments are supplementary; equations (1)--(3) and the anchor argument prove the universal statements. Run with `python checker.py`.

## Relationship to prior work

Gulgowski and Sawicki (2026, arXiv:2610.09810v1), Sections 5--7, study equinormed compactness for combinatorial spaces. Their Theorems 12--13 give sufficient positive near-directedness hypotheses and their Example 1 shows that an \(\ell_1\)-equivalent combinatorial space need not satisfy the equinormed compactness implication. The present family has the implication while **failing every** positive \((\lambda,\gamma)\) condition with \(\lambda<1/2\); the direct coordinatewise Kadec proof supplies the mechanism missing from those sufficient criteria. The abstract seminorm theory of Gulgowski, Kasprzak and Maćkowiak (arXiv:2111.10547) establishes general criteria involving difference sets, not the special one-set criterion here. The combinatorial-space survey by Borodulin-Nadzieja and collaborators (arXiv:2404.01733) treats related block families and \(\ell_1\)-equivalence without this weighted-directedness/compactness separation.

## Limitations

The construction is an explicit example, not a characterization of all hereditary families. Its coordinatewise Kadec property is proved for this particular norm, not for all norms equivalent to \(\ell_1\). The no-directedness assertion concerns \(0\leq\lambda<1/2\) and positive \(\gamma\) only; it makes no claim about all larger \(\lambda\) or about the unresolved general boundary as \(\gamma\to0\). Older equivalent constructions may exist, so independent historical-priority examination is warranted. No external independent audit has occurred.

## References

1. J. Gulgowski and P. Sawicki, *Compactness in Combinatorial Banach Spaces and Beyond*, arXiv:2610.09810v1 (first public 2026-10-07), Sections 2 and 5--7, especially Theorems 9 and 12--14 and Example 1.
2. J. Gulgowski, P. Kasprzak and P. Maćkowiak, *Compactness in normed spaces: a unified approach through semi-norms*, arXiv:2111.10547v1 (2021), Section 3.
3. P. Borodulin-Nadzieja, B. Farkas, S. Jachimek and A. Pelczar-Barwacz, *The ZOO of combinatorial Banach spaces*, arXiv:2404.01733v1 (2024), Sections 1 and 4.
