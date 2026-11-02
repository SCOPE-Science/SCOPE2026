# The sharp seven-point theorem and eleven spectra of two-noun cardinality syllogistic

## Finding

Fix the original syllogistic \(\mathsf S^\dagger(\mathrm{card})\) with just two raw nouns \(p,q\), their complements, and no noun-level union or sentence-level Boolean connectives. A theory is any collection of permitted sentences, interpreted on nonempty finite universes. Write \(T_k=\{n\in\mathbb N_{>0}:n\ge k\}\) and \(E_k=\{n\in\mathbb N_{>0}:n\ge k,\ n\equiv0\pmod2\}\).

**Theorem.** There are exactly \(67\) complete semantic types of finite models in this language. Every one has a representative with at most \(7\) elements, and \(7\) is best possible. The finite spectra of *arbitrary* theories over the two raw nouns are precisely the following eleven sets:
\[
\varnothing,\qquad T_1,T_2,T_3,T_4,T_5,T_6,T_7,\qquad E_2,E_4,E_6.
\]
Each spectrum is realized by a finite theory in this same two-noun language.

## Assumptions and scope

The available nouns are exactly \(p,\bar p,q,\bar q\). For each pair of nouns \(x,y\), the only atomic sentence forms are \(\forall(x,y)\), \(\exists(x,y)\), \(\exists^{\ge}(x,y)\), and \(\exists^>(x,y)\), respectively asserting inclusion, nonempty intersection, weak size inequality and strict size inequality. A theory is a set of such sentences; no first-order object variables or arbitrary Boolean combinations of nouns are allowed. Models are nonempty finite sets with interpretations of \(p,q\). The complete type of a model is its truth assignment to *all* permitted sentences, not its isomorphism type as a coloured finite set.

For a model, put
\[
a=|p\cap q|,\quad b=|p\cap\bar q|,\quad c=|\bar p\cap q|,\quad d=|\bar p\cap\bar q|,\quad u=a-d,\quad v=b-c.
\]
All four cell counts are nonnegative integers and their sum is positive.

## Proof

**1. Exact observational invariant.** An inclusion or nonempty-intersection sentence is true solely from the support of the vector \((a,b,c,d)\), and the four cell-nonemptiness tests \(\exists(p,q)\), \(\exists(p,\bar q)\), \(\exists(\bar p,q)\), \(\exists(\bar p,\bar q)\) recover that support. The four literal sizes are \(a+b,a+c,c+d,b+d\). Their six pairwise differences, up to order and sign, are \(u,v,u+v,u-v\). Therefore every cardinal comparison is decided by, and all four signs are recoverable from, the sign vector
\[
(\operatorname{sgn}u,\operatorname{sgn}v,\operatorname{sgn}(u+v),\operatorname{sgn}(u-v)).
\]
Thus two models satisfy exactly the same sentences if and only if their cell supports and these four signs agree.

**2. Seven-point reduction.** For any integer pair \((u,v)\) choose a new integer pair \((U,V)\) with the identical four-sign vector according to the following exhaustive cases. If both are zero, choose \((0,0)\). If exactly one is zero, replace the other by its sign. If both are nonzero with equal magnitudes, replace each by its sign. If \(0<|v|<|u|\), use \((2\operatorname{sgn}u,\operatorname{sgn}v)\); if \(0<|u|<|v|\), reverse the coefficients. Always \(|U|+|V|\le3\).

Reconstruct \((A,D)\) from \(U\) while preserving the positivity pattern of \((a,d)\). If both old coordinates were positive, take \(A=1+\max(U,0)\) and \(D=1+\max(-U,0)\). If exactly one was positive, its new value is \(|U|\) and the other remains zero; this is possible because its sign equals the sign of \(U\). If neither was positive, use \((0,0)\), necessarily with \(U=0\). Reconstruct \((B,C)\) analogously from \(V\) and the support of \((b,c)\). The new model preserves support and every comparison sign and has
\[
A+B+C+D\le |U|+|V|+4\le 7.
\]
The construction also preserves nonemptiness. Hence *every* model of *every* two-noun theory admits a truth-equivalent model of size at most seven.

**3. Count of complete types.** Classify supports of \((a,b,c,d)\) by size. A single occupied cell admits one sign pattern, giving \(4\) types. Of the six two-cell supports, two are opposite-pair supports \(\{a,d\}\) or \(\{b,c\}\), each allowing three comparison patterns; the other four are adjacent-pair supports, each allowing three. These contribute \(2\cdot3+4\cdot3=18\). Each three-cell support admits seven comparison patterns, according as its free difference lies in one of seven intervals or boundary rays relative to the nonzero fixed-sign difference, contributing \(4\cdot7=28\). With all four cells occupied, the four lines \(u=0\), \(v=0\), \(u=v\), \(u=-v\) yield eight open sectors, eight nonzero rays and the origin: \(17\) patterns. All are attained with positive integer cell counts. Total:
\[
4+18+28+17=67.
\]
As each support condition and each sign comparison is an available sentence or its semantic negation, these are precisely the complete semantic types.

**4. Exact finite spectra.** The unrestricted-vocabulary spectrum classification of Jiang (Theorem 3.16) proves that any consistent theory of the original language has spectrum of type \(T_k\) or \(E_k\). The reduction in step 2 forces its least size to be at most seven; hence only \(T_1,\ldots,T_7\) and the distinct even tails \(E_2,E_4,E_6\) can occur, besides the empty spectrum.

Each allowed set occurs. Denote by \(\mathcal F\) the conjunction-as-a-theory of the four sentences asserting all four cells nonempty. For \(T_1\), use the empty theory; for \(T_2\), require the cells \(a,b\) nonempty; for \(T_3\), require \(a,b,c\) nonempty; for \(T_4\), use \(\mathcal F\); for \(T_5\), use \(\mathcal F\) and \(|p|>|\bar p|\); for \(T_6\), use \(\mathcal F\), \(|p|>|q|\), and \(|q|>|\bar p|\); for \(T_7\), use \(\mathcal F\), \(|p|>|q|\), and \(|q|>|\bar q|\). Each written comparison is an allowed strict comparison sentence. The first four cases require the indicated number of nonempty cells. The \(T_5\) case needs at least five points, attained for every \(n\ge5\) by \((a,b,c,d)=(n-3,1,1,1)\). The \(T_6\) conditions amount to \(b>c\) and \(a>d\), requiring six points and attained for every \(n\ge6\) by \((n-4,2,1,1)\). For \(T_7\), \(b>c\) and \(a+c>b+d\) imply \(u>v>0\), hence at least seven points when every cell is positive; \((n-4,2,1,1)\) works for every \(n\ge7\).

For \(E_2\), use \(|p|=|\bar p|\), expressed by both weak comparisons. For \(E_4\), add \(\mathcal F\); for \(E_6\), additionally require \(|p|>|q|\), equivalently \(b>c\). For each even \(n\ge4\), \((a,b,c,d)=(1,n/2-1,1,n/2-1)\) realizes \(E_4\), and for each even \(n\ge6\) the same construction realizes \(E_6\). The same size equation alone realizes \(E_2\) for every positive even \(n\). A contradiction such as \(\exists^>(p,p)\) realizes \(\varnothing\).

Finally, the \(T_7\) witness above has no model below seven points, so the uniform small-model bound in step 2 is sharp.

## Verification

Run `python3 checker.py`. The standalone program independently evaluates all \(64\) permitted atomic sentence truth values on each four-cell vector through size \(10\), confirms equivalence with the claimed support-and-sign normal form, and then enumerates all four-cell compositions of each universe size through \(30\) (\(46{,}375\) cases), checks that the reduction preserves the semantic support and sign invariant, finds exactly \(67\) profiles, and tests the eleven stated theory spectra on all sizes through \(28\). It prints `ALL_CHECKS_OK`. This is finite corroboration; the quantified claims for arbitrary finite sizes and arbitrary theories follow from the symbolic arguments above plus Jiang's general spectrum theorem.

## Relationship to prior work

Jiang (2026, Theorem 3.16) determines all possible finite spectra for the original language with *unrestricted* raw nouns: empty, integer tails and even tails. This supplies the global shape restriction but does not determine the exact vocabulary-two cutoff, complete two-noun types or eleven-spectrum list; Jiang's exhibited thresholds use increasingly many nouns. A separately published one-raw-noun classification proves exactly five spectra \(\varnothing,T_1,T_2,T_3,E_2\), not this two-noun result. Moss (2016) developed the underlying finite-model logic and proof theory. Moss and Topal (2018/2020) study infinite-model semantics; that setting cannot entail this finite census. Known general two-variable first-order counting-spectrum theorems concern a richer language and do not give these exact bounds for the bare noun syllogistic. A noun-*union* extension is also strictly more expressive and its general additive-spectrum classification does not determine this fixed-vocabulary original-language restriction.

## Limitations

No claim concerns three or more raw nouns, arbitrary Boolean noun operations, or the number of *syntactic* theories. The classification of the shapes \(T_k,E_k\) is Jiang's prior theorem; only the sharp two-noun threshold, exact finite-vocabulary list and complete-profile count are assessed here. A possible equivalent older result in finite syllogistic proof theory remains an originality risk; full text of Moss (2016) was not available for complete examination. No independent audit has been performed.

## References

[1] Ruiting Jiang, “Finite Spectra of Syllogistic Logic with Cardinality Comparisons,” arXiv:2609.24902v1, posted 21 September 2026, particularly Definitions 2.2–2.4 and Theorem 3.16. https://arxiv.org/abs/2609.24902

[2] Lawrence S. Moss, “Syllogistic Logic with Cardinality Comparisons,” in *J. Michael Dunn on Information Based Logics*, Springer (2016), pp. 391–415, DOI 10.1007/978-3-319-29300-4_18.

[3] Lawrence S. Moss and Selçuk Topal, “Syllogistic Logic with Cardinality Comparisons, On Infinite Sets,” *Review of Symbolic Logic* 13(1) (2020), pp. 1–22, arXiv:1705.03037.

[4] “The one-variable cardinality syllogistic has exactly five finite spectra,” published research result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-one-variable-cardinality-syllogistic-has-exactly-five-finite--115eacbc2bad.
