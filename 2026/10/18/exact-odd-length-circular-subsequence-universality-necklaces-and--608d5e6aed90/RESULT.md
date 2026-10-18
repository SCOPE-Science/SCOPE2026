# Exact odd-length circular subsequence-universality necklaces and primitive extremizers

## Finding

For every integer \(k\geq1\), exactly \((2k+1)2^k\) labeled binary words of length \(2k+1\) attain the largest possible **circular subsequence-universality index** \(k\). **Every one is primitive** (has no proper period), hence there are exactly \(2^k\) corresponding necklaces, where rotations are identified. Exactly \((k-1)2^k\) labeled words become \(k\)-universal only after a suitable rotation.

There is a complete structural criterion. Mark each cyclic edge between unlike neighboring bits by \(1\), and each edge between equal neighbors by \(0\). The number of zero edges is necessarily odd. The word attains circular index \(k\) **if and only if exactly one run of one-edges between successive zero-edges has even length**, with zero permitted as an even run length.

For \(k=1,2,3,4,5,6,7\), the numbers of labeled maximizers are \(6,20,56,144,352,832,1920\), while the numbers of maximizing necklaces are \(2,4,8,16,32,64,128\).

## Assumptions and scope

Fix the binary alphabet \(\Sigma=\{0,1\}\). A *subsequence* is obtained by deleting zero or more symbols without changing their order. For any word \(w\), its linear universality index \(\iota(w)\) is the largest integer \(j\) for which every word in \(\Sigma^j\) occurs as a subsequence of \(w\). Its *circular universality index* is \(\zeta(w)=\max_{0\leq r<|w|}\iota(\operatorname{rot}_r(w))\). Both indexes are measured relative to the fixed alphabet \(\Sigma\), including for constant words.

Only odd lengths \(n=2k+1\) with \(k\geq1\) are included. Since every binary-rich block has length at least two, \(\zeta(w)\leq\lfloor n/2\rfloor=k\). A *labeled word* distinguishes the starting position on the circle; a *necklace* is its orbit under cyclic rotation. The reversal operation is **not** identified. A length-\(n\) word is *primitive* if it is not a proper integer power of a shorter word.

Indices are cyclic modulo \(n\). Set \(e_i=w_i\oplus w_{i+1}\), so \(e_i=1\) precisely for an unlike adjacent pair. Enumerate the cyclic zero-edges in cyclic order and let \(t_1,\ldots,t_s\) be the lengths of the interposed maximal runs of one-edges, allowing \(t_j=0\).

## Proof

**1. Universality and near-perfect matchings.** A binary word is subsequence-\(j\)-universal if and only if it can be partitioned into \(j\) consecutive factors each containing both symbols, followed by an arbitrary remainder. Indeed, greedily finish each factor upon seeing its second distinct symbol; the number of factors equals the universality index (the arch-factorization criterion, recalled in the references). In a length-\(2k+1\) rotation admitting \(k\) such factors, each has length at least two. Thus at most one extra symbol exists beyond the \(2k\) required letters. Inside every mixed factor of length two or three one can select two *adjacent unlike symbols*. These \(k\) pairs are disjoint. Conversely, if the cyclic sequence admits \(k\) disjoint unlike neighboring pairs, exactly one vertex of its odd-length circle is uncovered. Start reading immediately after that uncovered vertex to obtain a rotation split into \(k\) successive unlike pairs and the uncovered vertex as its leftover symbol. Therefore

\[
\zeta(w)=k \quad\Longleftrightarrow\quad \nu(H(w))=k,
\]

where \(H(w)\) is the spanning subgraph of the undirected cycle \(C_n\) retaining precisely the edges with \(e_i=1\), and \(\nu\) denotes maximum matching size. There are no parallel edges for \(n\geq3\); the endpoint \(n=3\) is covered.

**2. The unique parity-defect criterion.** The XOR sum of all the cyclic differences is zero. Thus the number of edges with \(e_i=1\) is even. Since \(n\) is odd, the number \(s\) of edges with \(e_i=0\) is odd and positive. Removing these edges leaves \(s\) path components, with \(t_j\) edges (including possible isolated vertices when \(t_j=0\)). A path with \(t\) edges has maximum matching size \(\lfloor(t+1)/2\rfloor\). Writing \(o\) for the number of odd \(t_j\), we obtain

\[
\nu(H(w))=\sum_{j=1}^s\left\lfloor\frac{t_j+1}{2}\right\rfloor
=\frac{\sum_jt_j+o}{2}=\frac{n-s+o}{2}.
\]

Since \(\sum_jt_j=n-s\) is even, the number \(o\) is even. Because \(s\) is odd, \(o\leq s-1\), with equality if and only if **precisely one \(t_j\) is even**. Consequently \(\nu(H)=k\) precisely in that case. This proves the structural criterion.

**3. Enumeration of transition vectors.** Every admissible maximizing cyclic difference sequence has a unique zero-edge immediately *following* its even-length run of one-edges. Distinguish that unique edge, choose its labeled position (\(n\) choices), then read the cyclic edge sequence just after it. Exactly \(2h\geq0\) runs of odd one-edge length, each followed by a zero-edge, are followed by one run of even one-edge length, whose terminal zero is the distinguished edge. The generating functions for a run together with its following zero are

\[
G(z)=\sum_{a\geq0}z^{2a+2}=\frac{z^2}{1-z^2},\qquad
H(z)=\sum_{b\geq0}z^{2b+1}=\frac{z}{1-z^2}.
\]

The ordinary generating function for the resulting sequences based at the distinguished edge is

\[
\sum_{h\geq0}G(z)^{2h}H(z)
=\frac{z(1-z^2)}{1-2z^2}.
\]

For \(k\geq1\), the coefficient of \(z^{2k+1}\) is \(2^{k-1}\). The unique distinguished edge makes this encoding bijective: after choosing a *labeled* edge position, there is no residual cyclic overcount. Hence the number of labeled cyclic difference vectors satisfying the criterion is \(n2^{k-1}\). Each such even-parity difference vector lifts to exactly two binary words, upon choosing \(w_0\in\{0,1\}\) and reconstructing successively. Therefore the number of maximizers is

\[
2\cdot n\cdot2^{k-1}=n2^k=(2k+1)2^k.
\]

**4. Primitive orbits.** Suppose a maximizing word is an integer power of a shorter binary word, with repetition multiplicity \(r>1\). Since \(n\) is odd, \(r\) is odd and \(r\geq3\). Its cyclic difference sequence also repeats \(r\) times; the shorter cyclic segment necessarily contains a zero-edge, since a binary odd cycle cannot have every neighboring pair unlike. Thus the cyclic list of run lengths between zero-edges is itself repeated \(r\) times. But its full list has **exactly one** even entry by Step 2, impossible for a repeated list with \(r\geq3\). Therefore every maximizing word is primitive, each necklace consists of precisely \(n\) labeled rotations, and the necklace count is \(n2^k/n=2^k\).

**5. How many rotations rescue universality?** For a *fixed* starting position, a length-\(2k+1\) binary word has \(\iota(w)=k\) if and only if its greedy arch factorization has \(k\) arches of length at least two. There are only two mutually exclusive possibilities: (i) all \(k\) arches have length two and there is one remaining letter, giving \(2^k\cdot2=2^{k+1}\) words; or (ii) exactly one of the \(k\) arches has length three, the others length two, and there is no remainder, giving \(k\cdot2^k\) words. (A length-two arch is \(01\) or \(10\); a greedy length-three arch is \(001\) or \(110\).) Their union has \((k+2)2^k\) words. Subtracting from the circular count yields exactly

\[
(2k+1)2^k-(k+2)2^k=(k-1)2^k
\]

words that acquire maximal universality only under rotation. All assertions follow.

## Verification

Run \(`python3 verification/circular_universality_check.py`\) using Python 3.9 or later; the program uses only the standard library. An exhaustive independent calculation covers **all binary words of lengths \(1\) through \(16\)**, comparing the direct all-rotations greedy-universality algorithm to the cyclic transition/run criterion and counting labeled words, necklaces, and fixed-origin words. A further 6,400 seed-fixed tests at lengths \(17\) through \(80\) compare these procedures and check odd-length primitivity of successes. These finite tests supplement, rather than replace, the all-length matching and counting proof. The script reports `ALL CHECKS PASSED` when successful.

## Relationship to prior work

Barker et al. (2020) introduce circular scattered-factor universality and establish its relationship with arch factorization and word powers. Fleischmann, Germann, and Nowotka (2021) study characterization of circular universality through remainders; only the publicly accessible abstract was examined here. Schnoebelen and Veron (2023), whose first version became public on 24 April 2023, supply explicit circular-universality algorithms and generalized arch tools. Their accessible complete 2023 text was examined, as was Barker et al.'s accessible 2020 complete text. These provide the **definitions and general-purpose index characterization**, but the inspected statements do not give the odd-length all-maximizer transition-parity classification, exact labeled/necklace counts, or universal primitivity. The previously established exact **linear** universality counts, including the general generating function, do not imply the new circular classification without resolving overlaps among optimal rotations.

## Limitations

The theorem concerns binary alphabets and odd lengths at the sharp upper bound. It does not enumerate even-length maximizers, non-maximal universality classes, larger alphabets, or reversal-identified bracelets. Exhaustive tests are finite and not proof of all lengths. The originality comparison is based on the named accessible full texts, a targeted published-research-record search, and available abstracts; the 2021 paper's full text was inaccessible, so an equivalent unlocated result remains possible. This is not an independent novelty certification or an independent audit.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words* (2020), arXiv:2003.04629, https://arxiv.org/html/2003.04629v1.
2. P. Fleischmann, S. B. Germann, and D. Nowotka, *Scattered Factor Universality — The Power of the Remainder* (2021), arXiv:2104.09063, https://arxiv.org/abs/2104.09063 (public abstract inspected; full text inaccessible).
3. P. Schnoebelen and J. Veron, *On Arch Factorization and Subword Universality for Words and Compressed Words* (first publicly posted 24 April 2023), arXiv:2304.11932, https://arxiv.org/html/2304.11932v1.
4. D. Adamson, *Ranking and Unranking \(k\)-Subsequence Universal Words* (2023), arXiv:2304.04583, https://arxiv.org/abs/2304.04583 (linear-universality context).
