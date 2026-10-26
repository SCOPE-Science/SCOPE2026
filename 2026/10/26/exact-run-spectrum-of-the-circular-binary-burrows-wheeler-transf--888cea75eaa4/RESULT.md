# Exact run spectrum of the circular binary Burrows–Wheeler transform at weight four

## Finding

For any binary word of length \(n\ge4\) with exactly four ones, sort all \(n\) circular rotations lexicographically (allowing repeated rows), and concatenate their preceding bits in sorted order. This is the circular Burrows–Wheeler transform, denoted \(\mathrm{BWT}(w)\). Let \(r(w)\) be the number of maximal constant-letter runs in this linear output. Let \(N_r(n)\) be the number of *linear* binary words of length \(n\), of weight four, with \(r(w)=r\).

Define \(h_r(m)=4N_r(m+4)/(m+4)\), where \(m\ge0\), and \(H_r(z)=\sum_{m\ge0}h_r(m)z^m\). The factor is integral because these are equivalently the numbers of ordered zero-gap quadruples with total gap length \(m\). Write \(D(z)=(1-z^2)(1-z^3)(1-z^4)\). The complete spectrum is

\[
\begin{aligned}
H_1(z)&=1,\\
H_2(z)&=\frac{4z+2z^2+4z^3+z^4}{1-z^4},\\
H_4(z)&=\frac{2z^2(1-z)(4+10z+13z^2+17z^3+11z^4+6z^5)}{D(z)},\\
H_6(z)&=\frac{4z^3(1+5z+3z^2+7z^3+4z^4+3z^5)}{D(z)},\\
H_8(z)&=\frac{4z^5(2+2z^2+z^3+z^4)}{(1-z)D(z)}.
\end{aligned}
\]

For all other run counts \(r\), \(H_r(z)=0\). Thus \(N_r(n)=(n/4)[z^{n-4}]H_r(z)\) for every \(n\ge4\), with exact ordinary generating functions, not asymptotic approximations. Eight runs first occur at \(n=9\). For example the counts for \(n=9\) are \(N_2=9,N_4=63,N_6=36,N_8=18\), totaling \(126\).

## Assumptions and scope

The alphabet order is \(0<1\). The transform is *circular*, without a terminal sentinel; equal rotations may appear as separate sorted rows. The run count concerns the *linear* BWT output, not a circular wrapping of its final and initial positions. The enumeration counts all linear words with four ones, *not* necklaces. Periodic words are included. Only the fixed-weight-four stratum is asserted.

## Proof

Write a representative of the circular word as \(w=10^{g_0}10^{g_1}10^{g_2}10^{g_3}\) with all \(g_i\ge0\) and \(\sum_i g_i=m=n-4\). Each of the four marked ones determines an ordered gap quadruple. Counting the marked one in two ways gives \(4N_r(n)=n h_r(n-4)\): for each word and chosen one there is exactly one marked gap tuple, and each ordered gap tuple specifies a word whose marked one can occupy any of the \(n\) linear positions.

The rows in the sorted rotation matrix separate into layers \(t=\max_i g_i,\ldots,0\). Layer \(t\) consists of the rows beginning with exactly \(t\) zeros before their next one, indexed by those \(i\) with \(g_i\ge t\). They are ordered by decreasing lexicographic cyclic successor-gap tuples \((g_{i+1},g_{i+2},g_{i+3},g_i)\), indices modulo four. Each row contributes BWT bit \(1\) exactly when \(g_i=t\), and contributes \(0\) otherwise. Ties correspond to identical rotations and contribute equal preceding bits. This completely specifies the BWT from the ordered gaps.

Sort the distinct gap values as \(x_0<\cdots<x_{s-1}\), where \(1\le s\le4\). Their *weak order* is the surjective rank pattern \(p=(p_0,p_1,p_2,p_3)\) with \(g_i=x_{p_i}\); set \(c_j=|\{i:p_i\ge j\}|\) for \(1\le j<s\). For each difference \(x_j-x_{j-1}\), record whether it equals one or is at least two, as \(e_j\in\{1,2\}\). For every nonconstant rank pattern, the BWT run count depends only on \(p\) and these binary difference categories. Indeed, the order within each layer depends only on the rank pattern; expanding a difference already at least two only inserts additional all-zero layers between two already separated active levels, and shifting all gaps up equally appends zero-only layers to a BWT that already ends in zero. Neither operation changes its run boundaries. Conversely, every choice of \(p\), \(e\), the minimum \(x_0\ge0\), and independent nonnegative increments for differences tagged \(e_j=2\) gives one distinct ordered gap tuple.

For a nonconstant cell \((p,e)\), let \(r(p,e)\) be the BWT run count of its representative with \(x_0=0\) and successive differences equal to the displayed values \(e_j\). Its exact enumerator is

\[
\frac{z^{\sum_{j=1}^{s-1}c_je_j}}{(1-z^4)\prod_{\{j:e_j=2\}}(1-z^{c_j})}.
\]

The constant rank pattern is handled separately: \((0,0,0,0)\) has BWT \(1111\), hence one run; each positive constant gap has BWT \(1^4 0^{4x_0}\), hence two runs, contributing respectively \(1\) and \(z^4/(1-z^4)\). There are \(1+14\cdot2+36\cdot4+24\cdot8=365\) rank-and-difference cells in all. Their run-count distribution at representatives is \(1,10,70,172,112\) for \(r=1,2,4,6,8\) respectively. Summing the above rational cell enumerators, correcting the constant case, and clearing the common denominator \(T(z)=(1-z)(1-z^2)(1-z^3)(1-z^4)\) yields the five displayed identities. In particular \(\sum_r H_r(z)=(1-z)^{-4}\), the generating function of all nonnegative four-tuples. Each calculation is an exact finite integer-polynomial identity reproduced by the standalone verifier. This completes the proof for all lengths.

## Verification

The included file `verify_bwt4.py` uses Python's standard library alone. It enumerates every rank-and-difference cell, constructs the common-denominator numerator by integer-polynomial convolution, compares it coefficient-for-coefficient with each closed form, and checks the sum identity. It separately compares the gap-layer transform with the transform from directly sorting all rotations on each of the \(7^4=2401\) gap quadruples with entries at most six. Finally it computes the length-by-length histograms directly for lengths \(4\) through \(19\); those finite checks are corroboration, while the symbolic 365-cell identity supplies the all-length argument.

## Relationship to prior work

Circular rotation sorting and bijective BWT variants were treated by Kufleitner in 2009. The 2017 analysis of BWT fixed points includes formulas for words containing three or four ones, but addresses the constraint that a word is a *fixed point* of the transform, rather than counting *all* words of weight four according to the number of transform runs. Fici and collaborators (2023) study how morphisms change the number of BWT runs and prove general facts about balanced transforms, including the two-run case. Those statements neither provide nor directly imply the four-run-class all-length weight-four enumerator proved here. The new contribution is the joint fixed-weight/all-run distribution, not the definition of the transform or the general relevance of runs.

## Limitations

No claim is made about higher Hamming weights, arbitrary alphabets, or a closed expression for individual cyclic equivalence classes. The 365-cell proof classifies run counts only, not all possible BWT outputs. Literature priority remains subject to specialized results not located in the examined sources. The computation has not undergone independent external audit.

## References

1. M. Kufleitner, *On Bijective Variants of the Burrows–Wheeler Transform*, arXiv:0908.0239 (public 2009-08-03), https://arxiv.org/abs/0908.0239 .
2. S. Mantaci et al., *On Fixed Points of the Burrows–Wheeler Transform* (2017), open-access PDF https://pages.di.unipi.it/rosone/Papers/MRRRS_FI2017.pdf .
3. G. Fici et al., *On the Impact of Morphisms on BWT-Runs*, CPM 2023, DOI:10.4230/LIPIcs.CPM.2023.10 .
