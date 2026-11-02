# Exact length-26 cyclic cover of all four-letter complement-tandem DNA motifs

## Finding

Let \(\Sigma=\{0,1,2,3\}\), with a fixed-point-free complementation involution \(\overline{0}=1\), \(\overline{1}=0\), \(\overline{2}=3\), \(\overline{3}=2\). The complete set of complement-tandem four-mers is
\[
\mathcal T=\{ab\overline a\overline b:a,b\in\Sigma\}.
\]
It contains sixteen distinct motifs. **The minimum length of a circular word containing every member of \(\mathcal T\) as a cyclic consecutive four-mer is exactly \(26\).** An optimal circular word, written from one arbitrary starting point, is

`00110013021303120312233223`.

With \(0=A\), \(1=T\), \(2=C\), and \(3=G\), the same statement applies to the Watson–Crick alphabet. This result is for complement-tandem motifs \(ab\overline a\overline b\), not the reverse-complement palindromes \(ab\overline b\overline a\), and not ordinary tandem squares \(abab\).

## Assumptions and scope

A *circular word* of length \(L\) is a sequence of \(L\) symbols with indices taken modulo \(L\); a target occurs when four consecutive cyclic symbols, in order, equal that target. Repeated occurrences are allowed. Complementation is a symbolwise fixed-point-free involution, not sequence reversal. The result concerns the four-letter alphabet and every one of its sixteen prescribed four-mers, with no multiplicity requirements. An arbitrary fixed-point-free involution on any other labeled four-symbol alphabet is obtained by relabeling.

For two different four-mers \(u,v\), define their *overlap shift* \(c(u,v)\) as the least \(s\in\{1,2,3,4\}\) such that the final \(4-s\) symbols of \(u\) are the initial \(4-s\) symbols of \(v\), where the empty overlap \(s=4\) is permitted. This is a finite, exact combinatorial cost.

## Proof

**Overlap structure.** Write \(P(a,b)=ab\overline a\overline b\) and define
\[
F(a,b)=(b,\overline a).
\]
The three-letter suffix of \(P(a,b)\) equals the three-letter prefix of another target exactly when that target is \(P(F(a,b))\). Its two-letter suffix equals another target's two-letter prefix exactly for \(P(F^2(a,b))\), because \(F^2(a,b)=(\overline a,\overline b)\). Thus a shift-one or shift-two transition never changes the orbit of \(F\). Since \(F^4\) is the identity and \(F^2\) has no fixed pair, all orbits have size four. There are precisely four orbits, and any transition between distinct orbits has shift cost at least three.

**Lower bound.** Consider any cyclic cover of length \(L\) and select one occurrence of each of its sixteen distinct targets. List these starts in cyclic order, and let the positive gaps between successive starts sum to \(L\). The gap between starts is at least the overlap shift cost of the corresponding target pair. Consequently, \(L\) is no smaller than the cost of a cyclic tour through all sixteen targets.

At least four tour transitions join different orbits: every one of the four orbits must be exited. If at least five transitions join different orbits, the cost is at least \(16+2\cdot5=26\), since every transition costs at least one and each inter-orbit transition costs at least three.

Suppose instead exactly four transitions join different orbits. Each orbit then occurs in one consecutive run of four vertices in the tour. There are twelve within-orbit transitions and four between-orbit transitions, with baseline total cost \(12+4\cdot3=24\). If the tour had cost at most twenty-five, the sum of all costs in excess of this baseline would be at most one.

In particular, no within-orbit transition could have cost more than two, and at most one could have cost two. A run of four distinct vertices in an \(F\)-orbit cannot use one shift-two transition and two shift-one transitions: such moves have total exponent \(2+1+1=4\), and therefore return to the starting vertex under \(F^4=1\), contradicting distinctness of the four visited vertices. Hence under the putative cost bound, all three transitions within every orbit must be shifts of one: each orbit run is a full forward \(F\)-cycle with its final return edge omitted.

Such a run begins with some target \(P(a,b)\) and consists of four successive four-mers with one-symbol shifts. The seven-letter concatenation is
\[
a\,b\,\overline a\,\overline b\,a\,b\,\overline a,
\]
so its first and last symbols \(a\) and \(\overline a\) lie in the same complementation pair. There are two pairs of alphabet symbols, \(X=\{0,1\}\) and \(Y=\{2,3\}\). Of the four \(F\)-orbits, one has both coordinates confined to \(X\) and another has both coordinates confined to \(Y\). Hence their respective runs must be labeled \(X\) and \(Y\). The cyclic succession of four runs consequently makes at least two changes of complementation-pair label.

A transition of shift three requires the last character of the previous run to equal the first character of the next. At each change of pair label these characters belong to disjoint pairs, so shift three is impossible and the inter-orbit transition costs four. There are therefore at least two extra units beyond the baseline twenty-four, forcing \(L\ge26\). This contradicts a tour of cost at most twenty-five and proves the lower bound for every cyclic cover.

**Attainment.** The 26-letter word `00110013021303120312233223`, interpreted cyclically, has all sixteen members of \(\mathcal T\) among its twenty-six cyclic four-grams. This can be checked directly or using the standalone verifier. Hence \(L=26\) is attainable, proving equality.

## Verification

The included standard-library Python program `verify.py` independently checks the target set and the explicit length-26 witness; enumerates all four overlap orbits and checks the overlapping-pair restrictions; and calculates the exact minimum cost of a sixteen-target cyclic tour using a Held–Karp dynamic program with one distinguished starting target. Its result is \(26\). The dynamic program is finite and exhaustive for these sixteen targets, and uses integer costs throughout. This computational check is corroboration; the lower bound above is an independent mathematical proof.

To reproduce, run `python3 verify.py` from the directory containing this report and that script; success ends with `VERIFY_OK`.

## Relationship to prior work

Yohananov and Schwartz investigate coding capacities under reverse-complement and palindromic duplication errors (arXiv:2312.00394, first publicly posted 2023-12-01); their transformations apply sequence reversal, unlike the symbolwise complement-tandem targets here. Gardner and Godbole (arXiv:1711.07029) study universal cycles for restricted word sets, whereas this result optimizes a cyclic **cover**, allowing motif repetitions. Neither inspected work establishes this sixteen-motif minimum. Related exact optimal covers for ordinary squares \(abab\) and reverse-complement palindromes \(ab\overline b\overline a\) use different motif languages; neither is an instance of the statement proved here.

## Limitations

The theorem is exact for four-letter alphabets with fixed-point-free complementation and motifs of length four. It does not prove a formula for larger alphabets, longer motifs, or biologically validated motif usefulness. The literature comparisons do not prove absolute priority: an equivalent unindexed superstring or constrained-universal-cycle computation could exist. No independent external scientific audit has been performed.

## References

1. L. Yohananov and M. Schwartz, *On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes*, arXiv:2312.00394v1 (2023-12-01), https://arxiv.org/abs/2312.00394 .
2. K. B. Gardner and A. Godbole, *Universal Cycles of Restricted Words*, arXiv:1711.07029v1 (2017-11-19), https://arxiv.org/abs/1711.07029 .
3. H. Z. Q. Chen, S. Kitaev and B. Y. Sun, *Lower Bounds, and Exact Enumeration in Particular Cases, for the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, Mathematics 8 (2020), 778, https://doi.org/10.3390/math8050778 (bibliographic and abstract comparison only; full text was not accessible during this review).
