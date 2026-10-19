# Palindromic minimal-absent-factor rigidity through five binary runs

## Finding

For arbitrary positive integers \(a,b,c\), consider the finite binary palindrome
\[
P_{a,b,c}=0^a1^b0^c1^b0^a.
\]
Put \(M=\max(a,c)\) and \(m=\min(a,c)\). The **entire set** \(\mathcal M(P_{a,b,c})\) of minimal absent contiguous factors is the disjoint union of these five families:

1. \(\{0^{M+1},\;1^{b+1}\}\);
2. \(\{0\,1^j0:1\le j<b\}\);
3. \(\{1\,0^j1:1\le j\le M,\;j\ne c\}\);
4. \(\{0^{m+1}1^b0^{m+1}\}\) when \(a\ne c\), empty otherwise;
5. \(\{1\,0^c1^b0^c1\}\) when \(a\ge c\), empty otherwise.

In particular,
\[
\boxed{|\mathcal M(P_{a,b,c})|=b+\max(a,c)+1+\mathbf1_{a>c}.}
\]
Every member of \(\mathcal M(P_{a,b,c})\) is a palindrome. Indeed **every nonempty binary palindrome having at most five maximal constant-symbol runs has only palindromic minimal absent contiguous factors**. This run threshold is sharp: the seven-run palindrome `0010110100` has nonpalindromic minimal absent factors `0011` and `1100`.

## Assumptions and scope

The ambient alphabet is exactly \(\{0,1\}\), even when a given word uses just one letter. A *contiguous factor* of a finite word is a consecutive substring, including the empty factor. A nonempty word \(u\) is a *minimal absent factor* (also called a minimal absent word) of \(w\) when \(u\) is not a factor of \(w\) but **every proper contiguous factor** of \(u\) is. For \(|u|\ge2\), it suffices to check that the length-\(|u|-1\) prefix and suffix occur, because every other proper factor is contained in one of these. We treat one-letter absent words separately. All displayed run exponents are positive integers. Reversal and global exchange of the two alphabet letters preserve the statements.

## Proof

**1. Occurring factors of the five-run word.** Directly from the five maximal source runs, one-run factors \(0^i\) occur exactly for \(1\le i\le M\), while \(1^j\) occur exactly for \(1\le j\le b\). Both orientations of a two-run factor with zero-run length \(i\) and one-run length \(j\) occur precisely when \(i\le M\) and \(j\le b\).

For three-run factors, with every displayed exponent positive, the occurrence criteria are
\[
\begin{aligned}
0^i1^j0^h\text{ occurs}
&\iff j=b\text{ and }[(i\le a,\ h\le c)\text{ or }(i\le c,\ h\le a)],\\
1^i0^j1^h\text{ occurs}
&\iff j=c,\ i\le b,\ h\le b.
\end{aligned}
\]
The four-run factors have exactly the patterns and restrictions
\[
\begin{aligned}
0^i1^j0^k1^h &:\quad i\le a,\ j=b,\ k=c,\ h\le b,\\
1^i0^j1^k0^h &:\quad i\le b,\ j=c,\ k=b,\ h\le a.
\end{aligned}
\]
Every five-run factor starts and ends with \(0\); it has shape \(0^i1^b0^c1^b0^h\) with \(1\le i,h\le a\). No factor has six or more runs. These criteria follow because a factor traversing three or more runs must include every internal source run in full.

**2. One and two runs in a minimal absence.** The largest occurring zero-only and one-only factors give exactly the two absent unary extensions in family 1. A mixed two-run word outside the rectangular occurrence range already contains an absent one-run proper factor. Hence no additional two-run minimal absence is possible.

**3. Three-run minimal absences.** Consider \(0^i1^j0^h\). If \(j<b\), it is absent; both one-letter boundary deletions can be factors only when \(i=h=1\). This is family 2. The case \(j>b\) is excluded by an absent proper one-run factor. When \(j=b\), the allowable pairs \((i,h)\) form the down-set
\[
([1,a]\times[1,c])\ \cup\ ([1,c]\times[1,a]).
\]
The only missing lattice point within the supported coordinate square \([1,M]^2\) whose two immediate predecessors belong to the down-set is \((m+1,m+1)\), and that point is missing exactly when \(a\ne c\). Larger coordinate values already contain an absent proper factor, so family 4 is complete.

Now consider \(1^i0^j1^h\). If \(j\ne c\), the boundary deletion conditions force \(i=h=1\) and \(j\le M\), yielding family 3. If \(j=c\), the three-run factor occurs whenever both outer exponents are at most \(b\); exceeding this bound produces an absent proper one-run factor. No further three-run minimal absence exists.

**4. Four-run minimal absences.** By reversal it suffices to examine \(0^i1^j0^k1^h\). If \(i,h>1\), the present prefix and suffix of length one less are both four-run factors; their restrictions jointly force \(i\le a,j=b,k=c,h\le b\), so the proposed word itself occurs. If \(i=1,h>1\), its prefix is a three-run factor and its suffix a four-run factor; together they again force the same inequalities. If \(i>1,h=1\), its prefix is four-run and its suffix three-run. The occurrence criterion of the suffix \(0^i1^b0^c\) implies \(i\le a\); the remaining three inequalities come from the prefix. Finally, when \(i=h=1\), the two three-run boundary deletions force \(j=b,k=c\), so the four-run word occurs. Thus there are no four-run minimal absences.

**5. Five or more runs.** A five-run candidate beginning with \(0\) has shape \(0^i1^j0^k1^\ell0^h\). The prefix and suffix occurrence conditions, using the four- and five-run criteria from step 1, force \(j=\ell=b,k=c,i,h\le a\), regardless of whether either boundary run has length one. The candidate therefore occurs. A five-run candidate beginning with \(1\) must begin and end with a singleton \(1\); otherwise one of its boundary deletions would be an impossible five-run factor beginning with \(1\). It consequently has shape \(1\,0^j1^k0^\ell1\). Its two four-run boundary factors occur together exactly when \(j=\ell=c,k=b\) and \(c\le a\). The candidate itself cannot occur, because all five-run factors begin with \(0\); this is precisely family 5.

For a candidate with at least seven runs, deleting one boundary letter leaves at least six runs, which cannot occur. A six-run candidate cannot have both boundary deletions occur: if it starts with \(0\), deleting its first letter cannot produce an occurring five-run factor (that new factor would begin with \(1\)); if it starts with \(1\), deleting its last letter cannot produce one (that factor would begin with \(1\)). Hence no minimal absence has six or more runs.

Steps 2–5 give exactly the five advertised, pairwise-disjoint families. Their sizes are respectively \(2\), \(b-1\), \(M-1\), \(\mathbf1_{a\ne c}\), and \(\mathbf1_{a\ge c}\). Since
\[
\mathbf1_{a\ne c}+\mathbf1_{a\ge c}=1+\mathbf1_{a>c},
\]
the cardinality formula follows. Each listed word is unchanged by reversal, proving palindromicity.

**6. Sharp threshold for binary palindromes.** A nonempty binary palindrome has an odd number of maximal equal-letter runs. One-run words \(0^a\) have exactly the minimal absent factors \(1\) and \(0^{a+1}\). The three-run words \(0^a1^b0^a\) have exactly
\[
\{0^{a+1},1^{b+1}\}\ \cup\
\{0\,1^j0:1\le j<b\}\ \cup\
\{1\,0^j1:1\le j\le a\},
\]
again all palindromic, by the same three-run factor test. Five-run words are handled above; swapping symbols covers palindromes beginning with \(1\). The seven-run palindrome `0010110100` has both `0011` and `1100` absent, although respectively `001` and `011`, and `110` and `100`, occur. These are nonpalindromic minimal absent factors and establish sharpness.

## Verification

The accompanying self-contained Python program `check_maw_palindromes.py` constructs all distinct contiguous factors of each test word, enumerates candidate minimal absences directly from pairs of occurring boundary factors, and compares **whole sets**, rather than cardinalities alone, with the displayed five-family formula. All \(12^3=1728\) parameter triples \((a,b,c)\) with \(1\le a,b,c\le12\) pass. It additionally checks 342 one- and three-run palindrome cases and confirms the seven-run counterexample. Exact parameter-unrestricted conclusions follow from the proof above; finite checks are only corroboration.

## Relationship to prior work

Akagi–Okabe–Mieno–Nakashima–Inenaga (2022, arXiv:2202.13591) introduced run-length-encoded algorithms and a general five-class analysis of minimal absent **contiguous** words. That broad algorithmic framework can enumerate the cases here, but the inspected statements do not give the closed five-run-palindrome formula, the universal palindromicity consequence, or the sharp seven-run boundary. The present argument extracts a specific structural rigidity law from factor-incidence geometry.

Mieno–Watanabe–Nakashima–Inenaga–Bannai–Takeda (2020, arXiv:2006.02134) study *minimal absent palindromic words* (MAPWs), defined by palindromicity, absence, and occurrence of the inner factor. MAPWs need not satisfy the two-boundary-factor condition defining an ordinary minimal absent factor, so the two notions are not interchangeable. Neither the generic palindrome algorithms nor the general run-length MAW algorithms alone state the classification proved here.

## Limitations

The five-family formula is for the symmetric five-run pattern with positive exponents over the binary alphabet; it is not a formula for arbitrary five-run words. The seven-run example disproves only the extension of the universal palindromicity property to all longer palindromes; it does not classify seven-run MAWs generally. The accompanying program is finite verification, not a substitute for the proof. A previously unindexed equivalent classification may exist; the cited literature and accessible mathematical-record searches do not establish absolute priority.

## References

1. T. Akagi, K. Okabe, T. Mieno, Y. Nakashima, S. Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591 (first posted 2022-02-28), https://arxiv.org/abs/2202.13591 ; open full text https://drops.dagstuhl.de/storage/00lipics/lipics-vol223-cpm2022/LIPIcs.CPM.2022.27/LIPIcs.CPM.2022.27.pdf .
2. T. Mieno, K. Watanabe, Y. Nakashima, S. Inenaga, H. Bannai, M. Takeda, *Palindromic Trees for a Sliding Window and Its Applications*, arXiv:2006.02134 (first posted 2020-06-03), https://arxiv.org/abs/2006.02134 .
