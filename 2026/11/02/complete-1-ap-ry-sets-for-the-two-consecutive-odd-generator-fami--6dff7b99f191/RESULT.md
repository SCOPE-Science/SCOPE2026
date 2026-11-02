# Complete \(1\)-Apéry sets for the two consecutive-odd generator families

## Finding
Let \(a\ge2\), \(b=2a+1\), and consider the two coin sets
\[
A^-_a=\{b,b+2,\ldots,2b-1\},\qquad
A^+_a=\{b,b+2,\ldots,2b+1\}.
\]
For a coin set \(A\), let \(r_A(n)\) be the number of distinct nonnegative integer multiplicity vectors with total value \(n\). In particular \(r_A(0)=1\). For every \(0\le s<b\), let \(w_s^\pm\) be the *least* nonnegative integer congruent to \(2s\pmod b\) with \(r_{A_a^\pm}(w_s^\pm)\ge2\). The complete \(1\)-Apéry sets are
\[
\boxed{
 w_s^+=\begin{cases}
 4b+2s,&s=0,1,\\
 2b+2s,&2\le s\le b-1,
 \end{cases}
 \qquad
 w_s^-=\begin{cases}
 5b+2s,&s=0,1,\\
 2b+2s,&2\le s\le b-3,\\
 3b+2s,&s=b-2,b-1.
 \end{cases}}
\]
Consequently their complete generating functions for integers with at least two representations are
\[
\boxed{
 \sum_{\substack{n\ge0\\r_{A_a^+}(n)\ge2}}z^n
 =\frac{z^{4b}+z^{4b+2}+\sum_{s=2}^{b-1}z^{2b+2s}}{1-z^b}}
\]
and
\[
\boxed{
 \sum_{\substack{n\ge0\\r_{A_a^-}(n)\ge2}}z^n
 =\frac{z^{5b}+z^{5b+2}+\sum_{s=2}^{b-3}z^{2b+2s}+z^{5b-4}+z^{5b-2}}{1-z^b}}.
\]
The \(1\)-genera, defined as the counts of nonnegative integers with at most one representation, are exactly
\[
\boxed{g_1(A_a^+)=5a+6,\qquad g_1(A_a^-)=5a+10.}
\]
More strongly, the *positive integers having exactly one representation* are precisely
\[
\boxed{
U^+_a=A^+_a\cup\{2b,2b+2,3b,3b+2\}}
\]
and
\[
\boxed{
U^-_a=A^-_a\cup\{2b,2b+2,3b,3b+2,4b-4,4b-2,4b,4b+2\}}.
\]
In these unions the displayed elements are distinct for \(a\ge2\). The plus-family assertions also hold for \(a=1\).

## Assumptions and scope
A representation is an unordered coin sum with repetitions allowed, equivalently one multiplicity vector. The sets \(A_a^-\) and \(A_a^+\) contain respectively \(a+1\) and \(a+2\) positive odd generators; each contains \(b\), and each has gcd one. The \(1\)-Apéry set here is the set of first integers with at least **two** representations, one in each residue class modulo \(b\); it is not the ordinary Apéry set of integers admitting at least one representation. Its complementary count includes \(0\), which has exactly one empty representation.

## Proof
**1. Reduction to a bounded index sum.** Write the generators of either family as \(b+2i\), with \(0\le i\le L\), where \(L=a\) for the minus family and \(L=a+1\) for the plus family. A representation of \(qb+2s\) using \(\ell\) coins has indices \(i_1,\ldots,i_\ell\) satisfying
\[
\ell b+2(i_1+\cdots+i_\ell)=qb+2s,
\quad\text{hence}\quad
 i_1+\cdots+i_\ell=s+\frac{(q-\ell)b}{2}.
\]
Since \(b\) is odd, \(q\equiv\ell\pmod2\). Also \(\ell b\le qb+2s\le\ell(b+2L)\). These parity and size restrictions let us enumerate all possible representations below each proposed first-double threshold.

**2. Every displayed threshold has at least two representations.** For the plus family at \(s=0\), \(4b\) equals both four copies of \(b\) and \((2b-1)+(2b+1)\). At \(s=1\), \(4b+2\) equals both three copies of \(b\) plus \(b+2\), and two copies of \(2b+1\). For \(2\le s\le a+1\), the indices of two distinct two-coin representations of \(2b+2s\) are \((0,s)\) and \((1,s-1)\). For \(a+2\le s\le 2a\), use \((s-a-1,a+1)\) and \((s-a,a)\). Every index lies in \([0,a+1]\).

For the minus family at \(s=0,1\), \(5b+2s\) has one five-coin factorization with indices consisting of \(s\) ones and \(5-s\) zeros, and another three-coin factorization with indices \((a,a,1+s)\). These are legitimate because \(a\ge2\). For \(2\le s\le a\), the two index pairs \((0,s)\) and \((1,s-1)\) represent \(2b+2s\); for \(a+1\le s\le2a-2\), use \((s-a,a)\) and \((s-a+1,a-1)\). Finally \(3b+2(2a-1)\) has distinct triples \((a,a-1,0)\) and \((a-1,a-1,1)\), while \(3b+4a\) has triples \((a,a,0)\) and \((a,a-1,1)\). Thus every proposed \(w_s^\pm\) has at least two representations.

**3. Every smaller integer in the same residue class has at most one representation.** Representatives of the class \(2s\pmod b\) below the claimed \(w_s\) are exactly \(qb+2s\) for integers \(0\le q<q_s\), where \(w_s=q_sb+2s\). At most one nonnegative integer of the same residue class lies below \(2s\), namely \(2s-b\) when \(2s\ge b\); it is odd and smaller than the least generator \(b\), so it has no representation and cannot alter the threshold.

For the plus family, when \(s=0,1\), the only represented candidates below \(4b+2s\) are the unique sums at \(b+2s\), \(2b+2s\), and \(3b+2s\), together with the empty sum for \(s=0,q=0\). By the equation in step 1, they require respectively one, two, or three coins with total index \(s\) and so have unique multiplicity vectors. For \(2\le s<b\), all candidates below \(2b+2s\) have at most one representation: a candidate \(b+2s\) has one generator representation if \(s\le a+1\), and none otherwise; a candidate \(2s\) is even and below \(2b\). This proves minimality in every plus residue.

For the minus family, when \(s=0,1\), candidates below \(5b+2s\) with \(q=1,2,3,4\) have exactly one representation using respectively \(1,2,3,4\) coins whose indices sum to \(s\); a representation using two fewer coins would require index sum \(s+b\), which exceeds the available \(\ell a\) for the relevant \(\ell\le2\), and extra coins exceed the target. At \(q=0\), only \(s=0\) permits the empty sum. For \(2\le s\le b-3\), every candidate below \(2b+2s\) has at most a single generator representation (when \(s\le a\)). For \(s=b-2,b-1\), the only represented candidate below \(3b+2s\) is \(2b+2s\), with its unique two-coin index pair of sum \(s=2a-1\) or \(2a\). This proves all minus thresholds are minimal.

**4. All higher elements in a residue class have at least two representations.** Appending the generator \(b\) to each of two distinct multiplicity vectors gives two distinct vectors. Iterating shows \(r_A(w_s+tb)\ge2\) for every integer \(t\ge0\). This establishes both complete \(1\)-Apéry sets and the two rational generating functions, with no unexamined larger integers.

**5. Genuinely exact genus and unique-representation sets.** The residues \(2s\pmod b\), \(0\le s<b\), are pairwise distinct. The number of integers of residue \(2s\pmod b\) strictly below \(w_s\) is \((w_s-(2s\bmod b))/b\). Summing and using \(\sum_{s=0}^{b-1}(2s\bmod b)=b(b-1)/2\) yields
\[
 g_1(A)=\frac{\sum_{s=0}^{b-1}w_s}{b}-\frac{b-1}{2}.
\]
For the plus family the threshold sum is \(3b^2+3b\); for the minus family it is \(3b^2+7b\). The displayed genus values follow on substituting \(b=2a+1\). The low-candidate classification in step 3 also shows that the only positive singly represented integers are the generators themselves and the four (plus) or eight (minus) additional values listed above. This completes the claims.

## Verification
Run `python3 verify.py` with Python 3 and its standard library. It independently enumerates coin-change multiplicity vectors by dynamic programming for every plus-family parameter \(1\le a\le150\) and minus-family parameter \(2\le a\le150\). For the first nineteen cases it compares that recurrence with a separately implemented top-down enumeration of multiplicities. It checks all threshold values, every claimed singleton representation, genus, Frobenius boundary, and the upward-closure property with exact integers. The latest package test prints `VERIFY_OK cases=299 residue_classes=45597 checked_integers=251679 independent_recursive_cases=19 exact_integer=yes`. These finite checks confirm sample consequences but are not the proof for unbounded \(a\).

For instance, \(a=2\) gives \(b=5\); the plus thresholds in order \(s=0,1,2,3,4\) are \((20,22,14,16,18)\), with \(g_1=16\), and the minus thresholds are \((25,27,14,21,23)\), with \(g_1=20\).

## Relationship to prior work
Komatsu, Hyun and Song (arXiv:2608.14053, first posted 2026-08-14) settle \(p\)-Frobenius-number conjectures for these *same* two consecutive-odd families. Their Sections 3 and 4 establish bounded partition-count identities and construct an element with two or more representations in every residue class; the published proofs establish maximal \(p\)-Apéry elements to recover Frobenius numbers. In the \(p=1\) plus case the stated Lemma 4.2 supplies exactly the **upper-bound witnesses** used here. The present theorem does not claim those witnesses, the original \(p\)-Frobenius formula, or the general Apéry-sum identities as new. It supplies the missing *minimality in every residue*, the fully evaluated \(1\)-Apéry sets, the closed two-representation generating functions, both \(1\)-genera, and complete singleton loci. These data cannot be recovered from the maximum \(1\)-Apéry element alone.

Komatsu's earlier general \(p\)-Apéry framework (arXiv:2111.11021, first posted 2021-11-22) supplies the abstract formulas for \(p\)-Frobenius and related invariants, including \(p\)-genus, but not the evaluated consecutive-odd Apéry minima. The generalized Fibonacci-triple work (arXiv:2304.00443, first posted 2023-04-02) applies similar methods to different generators. Earlier work on consecutive integer generators, not consecutive odd ones, does not subsume the evaluated formulas here.

## Limitations
The result concerns only the first double-representation threshold (the \(p=1\) layer) for the two specified families. No formula for higher \(p\), for arbitrary arithmetic progressions, or for the full denumerant of every integer is claimed. General \(p\)-Apéry-to-genus and generating-series reductions are previously known; novelty rests on the explicit evaluations, complete singleton classification, and all-residue minimality. A mathematically equivalent earlier evaluation under another formulation is still possible, and historical-priority assessment remains open.

## References
1. T. Komatsu, S. Hyun and K. Song, *\(p\)-numerical semigroup of the sequence of consecutive odd integers*, arXiv:2608.14053 (2026-08-14), https://arxiv.org/abs/2608.14053 .
2. T. Komatsu, *On the determination of \(p\)-Frobenius and related numbers using the \(p\)-Apéry set*, arXiv:2111.11021 (2021-11-22); subsequent journal version 2024, https://arxiv.org/abs/2111.11021 .
3. T. Komatsu, S. Laishram and P. Punyani, *\(p\)-numerical semigroup of generalized Fibonacci triples*, arXiv:2304.00443 (2023-04-02), https://arxiv.org/abs/2304.00443 .
4. T. Komatsu and K. R. Pandey, *\(p\)-numerical semigroup of the sequence of consecutive integers*, Bull. Korean Math. Soc. 62 (2025), 1397–1409; the original conjectures about consecutive odd generators are discussed in [1].
