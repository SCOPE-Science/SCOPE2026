# Modal parking fibers in the Schröder avoidance class

## Finding

Let \(\mathcal A_n=\operatorname{Av}_n(1234,2134)\) be the set of permutations avoiding both indicated classical four-letter patterns. Under the classical one-way parking rule, write \(F(\pi)\) for the number of successful preference sequences with final car-order permutation \(\pi\), and define
\[
M_n=\max_{\pi\in\mathcal A_n}F(\pi).
\]
Then the exact maxima for \(1\le n\le7\) are, in order,
\[
(M_1,M_2,M_3,M_4,M_5,M_6,M_7)=(1,2,6,8,20,36,56).
\]
For every integer \(n\ge8\), there is a unique pair of nonnegative integers \((a,b)\) satisfying \(5a+3b=n\) and \(0\le b\le4\), and
\[
\boxed{M_n=20^a6^b.}
\]
Consequently \(M_{n+5}=20M_n\) for every \(n\ge8\), and \(\lim_{n\to\infty}M_n^{1/n}=20^{1/5}\). The result also supplies a constructive maximizing parking permutation of every order. It does **not** claim to classify all maximizing permutations.

## Assumptions and scope

Cars \(1,\ldots,n\) arrive in that order at spaces \(1,\ldots,n\). Car \(i\) has a preference in \(\{1,\ldots,n\}\), parks at the first available space at or to the right of it, and fails if none exists. A successful sequence fills all spaces. Its *parking permutation* \(\pi=(\pi_1,\ldots,\pi_n)\) records the car label in space \(i\).

Avoidance refers to subsequences with distinct positions (not necessarily consecutive). For every \(\pi\in S_n\), let
\[
\ell_i(\pi)=1+\max\{t:0\le t\le i-1,\ \pi_{i-s}<\pi_i\ \text{for }1\le s\le t\}.
\]
Thus \(\ell_i\) is the length of the longest contiguous segment ending at position \(i\) whose entries other than its last are all smaller than the last. The classical fiber formula is \(F(\pi)=\prod_{i=1}^n\ell_i(\pi)\); a short independent explanation is included below. Empty words have fiber weight one.

The motivating primary source appeared publicly on 2026-09-23 (arXiv:2609.28650v1) and studies the total number of parking functions with outcomes in this avoidance class. The present claim concerns the **maximum individual outcome fiber** rather than that total.

## Proof

**1. Fiber product.** Fix the final permutation \(\pi\). When car \(\pi_i\) arrives, exactly the spaces \(h\) with \(\pi_h<\pi_i\) are occupied. In order to end at position \(i\), its preferred position must be one of the \(\ell_i\) positions from \(i-\ell_i+1\) through \(i\), and each such preference does land at \(i\). These choices can be made independently for each car when a final outcome is fixed, proving \(F(\pi)=\prod_i\ell_i\).

**2. Prefix extremum.** Let \(\mathcal B_m=\operatorname{Av}_m(123,213)\), and let \(B_m\) be the maximum of \(\prod_i\ell_i\) on \(\mathcal B_m\), with \(B_0=1\). In such a permutation \(\ell_i\le2\): three consecutive entries ending in a largest entry would contain \(123\) or \(213\). Moreover, two consecutive indices cannot both have \(\ell_i=2\), since that would create three consecutive increasing entries. Hence at most \(\lfloor m/2\rfloor\) indices contribute a factor two. A skew concatenation of increasing blocks of size two, together with a possible singleton, achieves that bound and avoids both patterns. Thus
\[
B_m=2^{\lfloor m/2\rfloor}\qquad(m\ge0).
\]

**3. Exact recurrence at the maximum entry.** Take \(\pi\in\mathcal A_n\), and let its largest entry \(n\) occur at position \(j\). The preceding \(j-1\) entries must avoid \(123\) and \(213\), since any such triple followed by \(n\) would create one of the forbidden four-letter patterns. The \(n-j\) entries to the right form a member of \(\mathcal A_{n-j}\) after standardization. At the maximum entry, \(\ell_j=j\); every \(\ell_i\) to its right depends only on the right subword because the intervening \(n\) is larger than all of its entries. Consequently,
\[
M_n\le\max_{1\le j\le n}\left(j2^{\lfloor(j-1)/2\rfloor}M_{n-j}\right),\qquad M_0=1.
\]
Equality holds for every chosen \(j\): place a skew-layered, increasing-pairs maximizer of length \(j-1\) on the largest \(j-1\) labels other than \(n\), then the label \(n\), then a maximizing member of \(\mathcal A_{n-j}\) on the smallest labels. A forbidden quadruple entirely in one of the two subwords is impossible. A forbidden quadruple using \(n\) would need a \(123\)- or \(213\)-triple before \(n\), or an entry larger than \(n\), both impossible. A quadruple crossing the two subwords but not using \(n\) is impossible because every left-subword label exceeds every right-subword label and the third and fourth elements of either forbidden pattern exceed its first two elements. Therefore the concatenation avoids both patterns and has exactly the product weight. Writing \(w_j=j2^{\lfloor(j-1)/2\rfloor}\), we have the **exact** recurrence
\[
M_n=\max_{1\le j\le n}w_jM_{n-j}\quad(n\ge1),\qquad M_0=1.
\]
Equivalently, \(M_n\) is the maximum product of the part-weights \(w_j\) over all ordered positive-integer compositions of \(n\).

**4. Extremal compositions.** The first seven part-weights are
\[
(w_1,w_2,w_3,w_4,w_5,w_6,w_7)=(1,2,6,8,20,24,56).
\]
For every \(j\ge8\), replacing a part \(j\) by parts \(5\) and \(j-5\) strictly increases the product: the ratio \(w_5w_{j-5}/w_j\) is \(5(j-5)/j\) for even \(j\) and \(5(j-5)/(2j)\) for odd \(j\), both greater than one in the stated range. Hence no part larger than seven occurs in an optimum.

A part one cannot occur with any other part: merging it with a part \(j\in\{1,\ldots,7\}\) strictly improves the product, since \(w_{j+1}>w_j\). A part six is dominated by \(3+3\), since \(24<36\). Among the remaining parts, the following comparisons are strict (entries represent part lengths; the number in parentheses is the product of the corresponding weights):

- With part four: \(4+2\,(16)\to3+3\,(36)\); \(4+3\,(48)\to7\,(56)\); \(4+4\,(64)\to3+5\,(120)\); \(4+5\,(160)\to3+3+3\,(216)\); \(4+7\,(448)\to3+3+5\,(720)\).
- With part two, after excluding fours: \(2+2\,(4)\to4\,(8)\); \(2+3\,(12)\to5\,(20)\); \(2+5\,(40)\to7\,(56)\); \(2+7\,(112)\to3+3+3\,(216)\).
- With part seven, after excluding twos and fours: \(7+3\,(336)\to5+5\,(400)\); \(7+5\,(1120)\to3+3+3+3\,(1296)\); \(7+7\,(3136)\to3+3+3+5\,(4320)\).

Thus an optimal composition with \(n\ge8\) uses **only parts three and five**: a lone part of size at most seven cannot have total \(n\ge8\), and any other prohibited part admits a strict improvement. Such a composition exists for every \(n\ge8\): the base orders \(8,9,10\) admit representations and adding three preserves representability. Finally, replacing five parts three by three parts five improves the product because \(6^5=7776<8000=20^3\). Therefore an optimum has at most four parts three. The equation \(3b+5a=n\) with \(0\le b\le4\) has exactly one nonnegative solution for each \(n\ge8\), and its weight is \(6^b20^a\). Direct use of the exact recurrence for \(n=1,\ldots,7\) gives the initial values above. This completes the proof.

## Verification

Run `python3 verify.py` alongside this file. The verifier independently tests avoidance by examining all four-position subsequences, computes fiber weights from contiguous suffixes, and enumerates every permutation through order nine. It also directly simulates all preference sequences through order five, verifying the fiber-product identity at every outcome; compares the exact composition recurrence with the closed formula through order 150; and checks the five-step law and strict large-part inequality over finite windows. Its expected terminal line is `VERIFY_OK`. Finite checks are corroboration, not the infinite proof; Steps 1–4 above prove the entire statement.

## Relationship to prior work

Martinez and Zeilberger (arXiv:2609.28650v1, 2026-09-23) define precisely this classical parking-permutation avoidance class and derive a polynomial-time scheme for **summing** its outcome multiplicities; their Lemma 2.1 gives the individual fiber-product weight. The extremal product in the present theorem is a different statistic: total sums do not determine maxima. Colmenarejo and collaborators (arXiv:2009.01124) give the general permutation-fiber product, while Pinsky (arXiv:2404.11529) studies the unconditional parking-permutation probability distribution. Neither general formula alone optimizes the fiber over the nontrivial avoidance class. The proof here uses the known fiber formula and supplies a new max-product reduction specific to \(\operatorname{Av}(1234,2134)\).

Accessible research records were compared for an equivalent maximum-fiber statement, broader coverage, permutation-symmetry equivalents, and the initial integer sequence. No exact equivalent was identified in those checks. This is a bounded novelty assessment, not a claim of global uniqueness.

## Limitations

The theorem maximizes fiber **size**, not the total count of avoiding parking functions, not the number of maximizing permutations, and not probabilities for parking models with different rules. It does not determine all extremizers. External independent validation was not performed. A complete reread of the motivating paper's main-result section could not be obtained on this occasion, so an unnoticed statement in that section or in unindexed literature remains a bibliographic risk; its accessible abstract, introduction and fundamental fiber lemma were inspected, and the new extremal proof is logically self-contained.

## References

1. Lucy Martinez and Doron Zeilberger, *A parking function analog of the Schröder numbers*, arXiv:2609.28650v1 (public 2026-09-23), https://arxiv.org/abs/2609.28650 ; open HTML: https://arxiv.org/html/2609.28650 .
2. Laura Colmenarejo, Pamela E. Harris, Zakiya Jones, Christo Keller, Andrés Ramos Rodríguez, Eunice Sukarto, and Andrés R. Vindas-Meléndez, *Counting k-Naples parking functions through permutations and the k-Naples area statistic*, arXiv:2009.01124 (first public 2020-09-02), https://arxiv.org/abs/2009.01124 .
3. Ross G. Pinsky, *The distribution on permutations induced by a random parking function*, arXiv:2404.11529 (first public 2024-04-17), https://arxiv.org/abs/2404.11529 .
