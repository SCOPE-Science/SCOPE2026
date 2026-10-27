# Sharp nine-block onset and exact entropy loss after a second Rule 54 update

## Finding
Let \(F\) be elementary binary cellular automaton Rule 54 on \(X=\{0,1\}^{\mathbb Z}\), and let \(Y_t=F^t(X)\), for \(t=1,2\). Write \(\mathcal L_n(Y)\) for the set of length-\(n\) words occurring in a configuration of \(Y\), and \(h(Y)\) for spatial-shift topological entropy. Then:

1. For every integer \(1\le n\le8\), \(\mathcal L_n(Y_1)=\mathcal L_n(Y_2)\). The first difference occurs at length nine and consists of exactly four words:
   \[
   \mathcal L_9(Y_1)\setminus\mathcal L_9(Y_2)
   =\{\mathtt{011001110},\mathtt{011100101},\mathtt{011100110},\mathtt{101001110}\}.
   \]
   In particular, \(Y_2\subsetneq Y_1\), and the observation length nine is sharp for witnessing this strict inclusion.

2. The respective spatial entropies are \(h(Y_1)=\log\lambda_1\) and \(h(Y_2)=\log\lambda_2\). Here \(\lambda_1\) is the Perron root of
   \[
   p_1(z)=z^4-2z^3+z-1,
   \]
   while \(\lambda_2\) is the Perron root of
   \[
   \begin{aligned}
   p_2(z)={}&z^{15}-4z^{14}+6z^{13}-5z^{12}+2z^{11}+2z^{10}\\
   &-5z^9+6z^8-2z^7-4z^6+8z^5-4z^4\\
   &-2z^3+5z^2-4z+1.
   \end{aligned}
   \]
   The certified rational bounds are \(1.86675<\lambda_1<1.86677\) and \(1.82767<\lambda_2<1.82770\). Thus \(h(Y_2)<h(Y_1)\) rigorously: the extra update causes a strict reduction in spatial information complexity despite no detectable language loss at lengths at most eight. Numerically, \(h(Y_1)\approx0.624204522\) and \(h(Y_2)\approx0.603049683\).

## Assumptions and scope
Rule 54 is the simultaneous update with local function \(f:\{0,1\}^3\to\{0,1\}\) equal to one precisely on \(\{001,010,100,101\}\). Inputs are *all* bi-infinite binary configurations, with no periodicity or boundary conditions imposed. Images are taken after **exactly one** or **exactly two** temporal updates; entropy is that of the **spatial shift** on the resulting closed shift-invariant image. A word of length \(n\) belongs to \(\mathcal L_n(Y_t)\) precisely when it is the \(t\)-step image of some finite input word of length \(n+2t\), because any finite input block extends to a configuration in \(X\).

## Proof
**Finite-state recognition.** For each \(t\in\{1,2\}\), derive the length-\((2t+1)\) local map \(f^{[t]}\) by applying \(f\) simultaneously \(t\) times. Form the full binary de Bruijn graph on the \(2^{2t}\) states \(\{0,1\}^{2t}\). Its edge from \(u\) to the last \(2t\) bits of \(ub\) is labeled \(f^{[t]}(ub)\), for \(b\in\{0,1\}\). Starting from the complete set of de Bruijn states, process an output word by the union of every edge bearing its next symbol. This gives a deterministic subset automaton; a word is in \(\mathcal L(Y_t)\) if and only if the final subset is nonempty. The reachable state counts, including the dead empty subset, are exactly \(11\) and \(39\) for \(t=1\) and \(t=2\), respectively.

**Earliest discrepancy.** Exhausting the binary words through length ten with the subset transitions gives the following counts for lengths \(n=1,\ldots,10\):

\[
\begin{aligned}
|\mathcal L_n(Y_1)| &: (2,4,8,16,29,53,100,187,348,649),\\
|\mathcal L_n(Y_2)| &: (2,4,8,16,29,53,100,187,344,635).
\end{aligned}
\]

Because \(Y_2\subseteq Y_1\), equal cardinalities imply equal languages at each length \(1\le n\le8\). Exhaustive subset transition at length nine gives the displayed four words in the difference. An independent enumeration of all \(2^{n+2t}\) finite predecessors for every \(n\le10\) agrees **word for word** with the subset automata, rather than just comparing counts. The finite computation here is exhaustive, not a sampled inference.

**Exact entropies.** Deterministic finite automata for factorial block languages count every output word once, so the exponential growth of accepted words equals the spectral radius of the accessible productive transition graph. Refining right-language equivalence classes (Moore minimization) yields complete \(10\)- and \(18\)-state automata, including the dead state. Each has precisely one nontrivial recurrent strongly connected component, of size \(8\) and \(16\), respectively; the remaining productive state is transient. Reading the component matrices from `automata.csv` and their labeled transition pairs gives exact characteristic polynomials

\[
\det(zI-A_1)=z^2(z^2+1)p_1(z),\qquad
\det(zI-A_2)=z\,p_2(z).
\]

The matrices are nonnegative and irreducible. Their Perron–Frobenius eigenvalues therefore determine the entropy of their respective image languages; lower-growth transient contributions do not alter the rate. Exact Faddeev–LeVerrier arithmetic verifies both characteristic polynomials and Cayley–Hamilton identities. The rational Collatz–Wielandt inequalities applied to positive integer vectors obtained from \(A_t^{110}\mathbf1\) give the strict rational bounds stated above. Their disjointness proves strict entropy loss without relying on floating-point root computations.

## Verification
Run `python3 verify.py` in a directory containing `automata.csv` (Python standard library only). The program reconstructs the local maps, de Bruijn subset transitions, all reachable sets, minimal deterministic automata, recurrent graph components, exact characteristic polynomials, and rational Perron bounds. It also independently enumerates finite input blocks up to length \(n+2t\) for all \(n\le10\), verifies the exact four nine-symbol witnesses, and reproduces every byte of `automata.csv`. A successful run prints `VERIFY_OK`.

## Relationship to prior work
Redeker's *Gliders and Ether in Rule 54* (2010) establishes flexible-time expressions for particular persistent and moving patterns. Martínez, Adamatzky, and McIntosh (2014) construct Rule 54 de Bruijn and subset diagrams, describe its gliders and its one-step Garden-of-Eden patterns. These methods provide important antecedents for finite-state treatment. The present finding concerns the **change of the entire spatial image language under the second update**, the sharp nine-symbol onset, and a pair of complete exact entropy evaluations; these are not assertions of those cited glider classifications. General one-step entropy tables do not logically determine a second-time image's entropy or its first language discrepancy.

## Limitations
The result does not describe images at \(t\ge3\), their eventual intersection, entropy of temporal trajectories under \(F\), glider collision statistics, or a classification across all elementary rules. The algebraic roots are specified exactly by polynomials plus rigorous rational spectral bounds; decimal displays are approximations. All source originality comparisons are limited to material actually inspected and indexed records; an unindexed prior equivalent evaluation remains possible.

## References
- M. Redeker, *Gliders and Ether in Rule 54*, arXiv:1007.2920v1, first public 2010-07-17. https://arxiv.org/abs/1007.2920
- G. J. Martínez, A. Adamatzky, H. V. McIntosh, *Complete Characterization of Structure of Rule 54*, *Complex Systems* 23 (2014), 259–293, arXiv:1410.3096v1, first public 2014-10-12. https://arxiv.org/abs/1410.3096
- S. Wolfram, *Statistical Mechanics of Cellular Automata*, *Reviews of Modern Physics* 55 (1983), 601–644. https://doi.org/10.1103/RevModPhys.55.601
