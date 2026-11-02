# A binomial-tree model for binary palindromic single-deletion codes

## Finding

Let \(\mathcal P_n\) be the set of all binary palindromes of length \(n\). A code \(C\subseteq\mathcal P_n\) corrects one deletion when no distinct codewords have a common length-\(n-1\) deletion descendant. The following holds for every integer \(m\ge1\).

1. For even length \(n=2m\), all \(2^m\) binary palindromes form a single-deletion-correcting code. Thus the maximum is \(2^m\), attained by precisely one codebook.
2. For odd length \(n=2m-1\), the deletion-confusability graph induced on \(\mathcal P_n\) is the binomial tree of order \(m\), with \(2^m\) vertices, under an explicit recursive isomorphism. Its independence number is \(2^{m-1}\). The number of distinct indexed maximum codebooks is exactly
\[
N_m=(m+1)\prod_{j=1}^{m-1}j^{\,2^{m-1-j}},
\]
where the empty product is one. In particular \(N_1,N_2,N_3,N_4,N_5,N_6=2,3,8,60,3456,11612160\).

The binomial-tree independent-set count is already known as a graph enumeration. The identified contribution is the precise induced deletion-graph isomorphism and its coding-theoretic consequences; the product is not claimed independently new as a generic binomial-tree formula.

## Assumptions and scope

The alphabet is \(\{0,1\}\); positions are indexed, with no quotient by reversal, complement, or any other symmetry. A palindrome equals its reversal. For a length-\(n\) word \(w\), its single-deletion shadow is \(D(w)=\{w_1\cdots w_{i-1}w_{i+1}\cdots w_n:1\le i\le n\}\), with repeated descendants counted only once. Correction of exactly one deletion and correction of at most one deletion are equivalent for these fixed-length codebooks, since zero- and one-deletion outputs have different lengths. The odd and even statements both include \(m=1\).

Identify an odd palindrome by its first \(m\) symbols \(u\) through \(P_o(u)=u_1\cdots u_m u_{m-1}\cdots u_1\), and an even palindrome by \(P_e(u)=u_1\cdots u_m u_m\cdots u_1\). For \(r\ge1\), a binary tail is alternating when every consecutive pair in it is unequal. A complementary tail is obtained by flipping each bit.

## Proof

**A deletion-alignment lemma.** Let distinct palindromes \(x,y\) of the same length \(L\) share one deletion descendant. Let \(t\) and \(k=L+1-t\) be their first and last differing positions, in one-based indexing; this symmetry is forced by palindromicity. If the deleted positions in \(x,y\) are respectively \(a\le b\) (swap the two words if necessary), equality of the descendants gives \(x_i=y_i\) for \(i<a\) and \(i>b\), and \(x_{i+1}=y_i\) for \(a\le i<b\). Thus \(a\le t\le k\le b\). Reflection of the shift relation through the palindrome centers gives \(x_i=y_{i+1}\) as well for \(t\le i<k\). It follows that \(x_i=x_{i+2}\) throughout the central differing interval, while \(x_t\ne x_{t+1}\) whenever \(t<k\). Therefore the entire central interval of length \(k-t+1\) alternates, and \(y\) is the bitwise complement of \(x\) on that interval. When \(a=b\), the two palindromes can differ only at their common center, and the same conclusion holds with a one-symbol interval. Conversely, if two palindromes agree outside a centered interval and are opposite-phase alternating words inside, deleting the first symbol of that interval from one and its last symbol from the other yields identical descendants. This proves the criterion in both directions.

**Even case.** In a palindrome of length \(2m\), the two middle symbols are equal. Any nonempty centered differing interval contains these middle symbols, so it cannot be alternating. The lemma excludes every edge between distinct even palindromes. All \(2^m\) are therefore compatible, and the unique maximum code is the entire set.

**Odd graph.** For odd length \(2m-1\), the criterion says that the halves \(u,v\in\{0,1\}^m\) are adjacent precisely when they have some common prefix of length \(m-r\), followed by complementary alternating tails of length \(r\), for one \(1\le r\le m\). This description is exact: the centered interval in the full palindromes is then alternating with opposite phases, and no other pair can have a common descendant.

Let \(a_m=0101\ldots\) and \(b_m=1010\ldots\) be the two alternating halves of length \(m\). The edges with \(r<m\) form two copies of \(G_{m-1}\), one for each first bit. The only edge with \(r=m\) joins \(a_m\) and \(b_m\). Moreover, these are precisely the two rooted bridge vertices in their respective subtrees: the suffix of \(a_m\) in the zero-prefix copy is \(b_{m-1}\), and the suffix of \(b_m\) in the one-prefix copy is \(a_{m-1}\). Complementation is an automorphism interchanging \(a_{m-1}\) and \(b_{m-1}\). Starting at \(G_1=K_2\), induction identifies \((G_m,a_m)\) with the rooted binomial tree obtained by joining the roots of two rooted order-\(m-1\) copies. In particular \(G_m\) is a tree on \(2^m\) vertices.

**Maximum size.** The edges of tail length one join each pair of halves differing only in their last bit. They are a perfect matching of size \(2^{m-1}\), so any independent set contains at most one endpoint from each matching edge. Every tree is bipartite, and its two color classes have equal size because the perfect matching pairs opposite classes. Hence an independent set of size \(2^{m-1}\) exists. This gives the sharp code size.

**Exact number of maximum codebooks.** Let \(N_m\) be the number of maximum independent sets of \(G_m\), and \(A_m\) the number of those containing \(a_m\). The base values are \(N_1=2\), \(A_1=1\). Every maximum independent set in \(G_m\) must restrict to a maximum independent set in each of the two constituent copies. Since exactly \(A_{m-1}\) maxima in each copy contain its bridge endpoint (by complement symmetry), the bridge exclusion yields
\[
N_m=N_{m-1}^2-A_{m-1}^2,\qquad A_m=A_{m-1}(N_{m-1}-A_{m-1}).
\]
Induction gives \(N_m=(m+1)A_m\) and \(A_m=(m-1)A_{m-1}^2\). Solving the latter with \(A_1=1\) gives
\[
A_m=\prod_{j=1}^{m-1}j^{\,2^{m-1-j}},\qquad N_m=(m+1)A_m.
\]
Every independent set corresponds to exactly one labeled codebook through the injective palindrome-half map. This finishes the proof.

## Verification

Run `python3 checks/verify.py` using Python 3 and only the standard library. The script constructs all binary palindromes and their deletion shadows independently of the graph formula. At half-lengths \(1\le m\le8\), it checks all odd/even shadow intersections against the alternating-tail criterion, verifies tree connectivity and edge count, and compares rooted-tree dynamic-programming independent-set counts with the displayed product. It also enumerates all candidate codebooks directly for \(1\le m\le4\). The observed terminal marker was `VERIFY_OK`. These finite checks corroborate, but do not replace, the proof for arbitrary \(m\).

## Relationship to prior work

Levenshtein's 1965 work introduced the insertion/deletion-correction framework. Sloane's 2002 survey explicitly models ordinary binary one-deletion codes as independent sets in a confusability graph, but its unrestricted graph and standard Varshamov–Tenengolts code results do not imply the palindrome-induced tree characterization. The 2012 constant-weight coloring work studies another induced-graph family, not palindromes. The numerical sequence \(N_m\) and its product coincide with the known enumeration of maximum independent sets in binomial trees (OEIS A347289, with an index shift); that source supplies the graph-theoretic formula **after** the new explicit deletion-graph identification, but not the identification itself. Palindromic-duplication codes concern an operation on substrings rather than restricting transmitted codewords to palindromes.

## Limitations

The result is for ordinary reversal palindromes over a binary alphabet, not Watson–Crick reverse complements or arbitrary \(q\)-ary palindromes. It concerns correction of one deletion only. It does not supply asymptotically rate-efficient codes without the palindrome restriction, physical DNA performance claims, or classification modulo symmetries. The graph enumeration identity is previously known for abstract binomial trees; independent historical-priority assessment of the coding-theoretic isomorphism remains outstanding. An older thesis discussing palindromes in extended ternary codes was located but its full text was not retrievable; it remains a limited priority risk.

## References

1. V. I. Levenshtein, “Binary codes capable of correcting deletions, insertions, and reversals,” *Dokl. Akad. Nauk SSSR* 163(4) (1965), 845–848. Bibliographic record: https://www.mathnet.ru/eng/dan31411.
2. N. J. A. Sloane, “On Single-Deletion-Correcting Codes,” first arXiv posting 2002-07-22, https://arxiv.org/abs/math/0207197; relevant discussion in Sections 1, 2, 5, and 6.
3. “Number of independent sets in the binomial tree of order n,” OEIS A347289, https://oeis.org/A347289 (includes the maximum-independent-set interpretation and product enumeration).
4. D. Cullina, A. Kulkarni, N. Kiyavash, “A coloring approach to constructing deletion correcting codes from constant weight subgraphs,” ISIT 2012, https://doi.org/10.1109/ISIT.2012.6284242.
