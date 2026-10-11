# Complete zero-set classification for two-tap Gabor windows on finite abelian groups

## Finding
Let \(G\) be a finite abelian group of order \(N\geq2\), let \(0\neq a\in G\) have order \(m\geq2\), and put \(h=N/m\). Fix nonzero complex numbers \(c,d\), and use the two-tap window \(g=c\delta_0+d\delta_a\). Let \(f:G\to\mathbb C^\times\) be any nowhere-zero signal. Write
\[
V_g f(x,\chi)=\sum_{y\in G}f(y)\overline{g(y-x)}\,\overline{\chi(y)},
\qquad
\alpha=-\frac{\overline c}{\overline d},
\qquad
\mu_m=\{\zeta\in\mathbb C:\zeta^m=1\}.
\]
For each \(x\in G\), every short-time Fourier zero, if present, belongs to a **single** frequency fibre
\[
Z_x(f)=\{\chi\in\widehat G: V_gf(x,\chi)=0\}
=\{\chi:\chi(a)=\zeta_x\},\qquad\zeta_x\in\mu_m,
\]
and this fibre has exactly \(h\) frequencies. Otherwise \(Z_x(f)\) is empty.

The complete classification of **all attainable time-frequency zero sets** is as follows. Specify independently at each \(x\in G\) either an empty fibre or one label \(\zeta_x\in\mu_m\), defining a candidate zero set \(\{(x,\chi):\chi(a)=\zeta_x\}\) over labeled positions. For each of the \(h\) cycles \(C\) of \(x\mapsto x+a\), put \(t_C\) equal to its number of labeled positions. A nowhere-zero signal has **exactly** these prescribed zeros if and only if, for every cycle, one of the following holds:

1. \(0\leq t_C\leq m-2\), with arbitrary labels;
2. \(t_C=m-1\), with arbitrary labels, and \(\alpha^{m^2}\neq1\);
3. \(t_C=m\), with \(\alpha^{m^2}=1\) and \(\prod_{x\in C}\zeta_x=\alpha^{-m}\).

There are no further restrictions between cycles. In particular, the number of distinct attainable time-frequency zero sets is exactly
\[
\boxed{\begin{cases}
\bigl((m+1)^m-2m^m+m^{m-1}\bigr)^h,&\alpha^{m^2}=1,\\[2mm]
\bigl((m+1)^m-m^m\bigr)^h,&\alpha^{m^2}\neq1.
\end{cases}}
\]
If frequency-fibre labels are discarded, the number of attainable **zero-bearing translation-index sets** is respectively \((2^m-m)^h\) or \((2^m-1)^h\). For a particular attainable pattern with \(t_C\) labels in each cycle, the short-time Fourier support size is
\[
\left|\operatorname{supp}V_gf\right|=N^2-h\sum_C t_C.
\]
For example, equal positive taps give \(\alpha=-1\); the cycle transition then occurs exactly at even \(m\). Unequal tap magnitudes always lie in the nonresonant regime.

The complete coefficient family realizing a labeled pattern is described by arbitrary nonzero starting values on each cycle and nonzero edge ratios \(r_x=f(x+a)/f(x)\), subject exactly to \(r_x=\alpha\zeta_x\) at labeled positions, \(r_x\notin\alpha\mu_m\) at unlabeled positions, and \(\prod_{x\in C}r_x=1\) around every cycle. All such choices realize that pattern. The resulting smallest possible support for a nowhere-zero signal is \(N^2-Nh\) when \(\alpha^{m^2}=1\), and \(N^2-h(N-h)\) otherwise. Equality requires respectively that every position be labeled or that each cycle have exactly one unlabeled position.

## Assumptions and scope
The theorem holds for **every** finite abelian group, arbitrary nonidentity step \(a\), arbitrary nonzero complex tap weights, and signals satisfying \(f(x)\neq0\) for all \(x\). Character values have modulus one, and \(\widehat G\) is the full finite Pontryagin dual. No restriction is imposed on the group being cyclic, on the tap magnitudes being equal, or on signal magnitudes. The STFT above is unnormalized; multiplying it by a nonzero scalar has no effect on zero sets. A zero pattern records each actual subset of \(G\times\widehat G\), not just its cardinality; labels on occupied fibres are part of the data.

## Proof
**Fourier-fibre reduction.** Since \(g\) vanishes outside \(\{0,a\}\), factor \(\overline{\chi(x)}\) to get
\[
V_gf(x,\chi)=\overline{\chi(x)}\bigl(\overline c f(x)+\overline d f(x+a)\overline{\chi(a)}\bigr).
\]
For \(r_x=f(x+a)/f(x)\), a zero therefore occurs precisely when \(r_x=\alpha\chi(a)\). The restriction homomorphism \(\widehat G\to\widehat{\langle a\rangle}\cong\mu_m\) is surjective by finite abelian character duality. Its kernel has \(h=N/m\) elements. Consequently a row has either no zeros or precisely one \(h\)-point fibre; for a labeled row the ratio is **forced** to be \(r_x=\alpha\zeta_x\).

**Holonomy necessity.** The map \(x\mapsto x+a\) partitions \(G\) into \(h\) disjoint directed \(m\)-cycles. On each cycle the ratios telescope:
\[
\prod_{x\in C}r_x=1.
\]
If all \(m\) positions are labeled, this becomes \(\alpha^m\prod_{x\in C}\zeta_x=1\), proving the third condition. In particular it implies \(\alpha^{m^2}=1\), because the product of labels is an \(m\)-th root of unity. If precisely one position \(u\) is unlabeled, all the other ratios are prescribed and
\[
r_u=\bigl(\alpha^{m-1}\prod_{x\in C\setminus\{u\}}\zeta_x\bigr)^{-1}.
\]
This belongs to the forbidden good-ratio coset \(\alpha\mu_m\) exactly when \(\alpha^{-m}\in\mu_m\), equivalently \(\alpha^{m^2}=1\). Thus a single unlabeled row is possible exactly in the complementary weight regime.

**Sufficiency and all coefficients.** With no unlabeled position, the displayed label-product condition makes the ratios telescope. With precisely one unlabeled position, the forced ratio above is outside \(\alpha\mu_m\) exactly in the asserted regime. With at least two unlabeled positions, first assign their other ratios arbitrary nonzero complex values outside the finite set \(\alpha\mu_m\), retaining two free ratios. Choose the penultimate free ratio outside that finite set **and** outside the finite set which would make the last, product-forced ratio belong to \(\alpha\mu_m\). This is always possible because \(\mathbb C^\times\) is infinite and the excluded union is finite. Thus all labeled/unlabeled requirements and the cycle product hold. Choose one arbitrary nonzero base coefficient on each cycle and propagate around its edges using these ratios; the cycle-product equation ensures consistency and every coefficient remains nonzero. Conversely, the Fourier-fibre reduction shows that every realizing signal arises exactly from this description. The constructions on distinct cycles are independent, completing the if-and-only-if classification.

**Counting and sharp support.** At any position the candidate choice is empty or one of \(m\) labels, giving \((m+1)^m\) candidates per cycle. There are \(m^m\) candidate patterns with precisely one empty position (\(m\) choices for its location and \(m^{m-1}\) labels), and \(m^m\) all-labeled patterns. If \(\alpha^{m^2}=1\), all one-empty patterns are forbidden while precisely \(m^{m-1}\) all-labeled patterns satisfy the single product condition; the cycle count is \((m+1)^m-2m^m+m^{m-1}\). Otherwise all-labeled patterns are forbidden and all one-empty patterns are permitted, yielding \((m+1)^m-m^m\). Multiply across the \(h\) cycles. Discarding labels, the only forbidden occupied-index count is \(m-1\) in the first regime or \(m\) in the second, giving \((2^m-m)^h\) and \((2^m-1)^h\). Every occupied row contributes exactly \(h\) zero frequencies, so the support-size identity and both sharp endpoints, including their full equality patterns, follow.

## Verification
Run `python3 verify_zero_patterns.py` with the Python 3 standard library. The script represents amplitudes and roots of unity by exact rational scale-and-angle pairs. It enumerates admissible and forbidden labeled patterns for cyclic groups of orders \(2\) through \(5\), verifies the closed formulas by exact integer counts, constructs all realizable coefficient ratios, and compares selected witnesses with **independent direct complex Fourier slices**. Further examples check cyclic orders through \(7\) and six noncyclic product-group families, as well as the polynomial counting identities through cycle order \(23\). The expected output starts with `VERIFY_OK` and ends with `exact_root_cosets=PASS holonomy=PASS pattern_count=PASS`. These are finite consistency checks; they do not replace the all-groups proof.

## Relationship to prior work
Krahmer–Pfander–Rashkov prove finite-group STFT uncertainty inequalities and analyze support-cardinality constraints, which motivate asking which complete zero configurations are possible. Fernández–Galbis–Martínez and Nicola study the much lower **global minimum** of STFT support and its extremizers; neither gives the all-pattern zero-fibre classification here. The closely related published result *Exact support geometry for a two-point cyclic short-time Fourier window* treats the minimum support for a **fixed signal support** and the equal-tap cyclic window; its good-edge argument motivates the present extension, but it does not imply arbitrary labeled full time-frequency zero sets, their exact numbers, unequal-tap torsion transitions, or all finite abelian groups. Other nearby published results on two-sparse signal pairs, generic windows, and magnitude phase-retrieval fibres likewise concern different observables and hypotheses. The \(\alpha^{m^2}\) transition and the frequency-label product constraint distinguish the present classification.

## Limitations
No statement is made for signals with zero coordinates, windows having more than two nonzero taps, or STFT magnitudes other than their exact zeros. The number of patterns counts distinct subsets of the full discrete time-frequency plane, not signals realizing them; each admissible pattern usually has infinitely many realizing signals. An unindexed older characterization in graph-ratio or short-filter terminology remains a historical priority risk.

## References
1. F. Krahmer, G. E. Pfander and P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1, first public 2006-11-16; *Applied and Computational Harmonic Analysis* 25 (2008), 209–225, DOI 10.1016/j.acha.2007.09.008.
2. C. Fernández, A. Galbis and J. Martínez, *Localization Operators and an Uncertainty Principle for the Discrete Short Time Fourier Transform*, *Abstract and Applied Analysis* 2014, Article 131459, DOI 10.1155/2014/131459.
3. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1 (2022-04-29), *Journal of Functional Analysis* 284 (2023), 109924.
4. *Exact support geometry for a two-point cyclic short-time Fourier window*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-support-geometry-for-a-two-point-cyclic-short-time-fourier--f7682ff5d741.
5. *Exact support trichotomy for two-sparse prime cyclic STFTs*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-support-trichotomy-for-two-sparse-prime-cyclic-stfts--5b84852d543c.
