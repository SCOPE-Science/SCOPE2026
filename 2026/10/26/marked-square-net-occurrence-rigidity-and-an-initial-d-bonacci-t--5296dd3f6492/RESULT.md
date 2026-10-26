# Marked-square net-occurrence rigidity and an initial d-bonacci transition

## Finding

A *net occurrence* in a finite word is an occurrence of a nonempty factor appearing at least twice, whose one-symbol left and right extensions (when present) each appear exactly once. Missing extensions at a boundary are counted as unique. We index starting positions from zero.

**Marked-square theorem.** Let \(\Sigma\) be any alphabet, \(a\in\Sigma\), and let \(X\in\Sigma^+\) be a nonempty word that begins and ends with \(a\) and has no occurrence of the adjacent pair \(aa\). Choose a new symbol \(z\notin\Sigma\), write \(m=|X|\), and let \(X^-\) denote \(X\) without its final symbol (possibly empty). Then the word
\[
T=XzXXzX^-
\]
has *exactly three* net occurrences. They are the two occurrences of \(B=XzX^-\), starting at \(0\) and \(2m+1\), each of length \(2m\), and the middle occurrence of \(X\), starting at \(m+1\), of length \(m\). No other factor occurrence is net.

**d-bonacci corollary.** For every integer \(d\ge3\), let \(\sigma_d(i)=0(i+1)\) for \(0\le i<d-1\) and \(\sigma_d(d-1)=0\), and \(W_k=\sigma_d^k(0)\). Then the net-occurrence counts are exactly \(0\) for \(k=0,1\), exactly \(2\) for \(2\le k\le d\), and exactly \(3\) for \(k=d+1\). For \(k=d+1\) put \(m=2^{d-1}-1\); the three starts and lengths are \((0,2m)\), \((m+1,m)\), and \((2m+1,2m)\).

## Assumptions and scope

The alphabet can have arbitrary finite or infinite cardinality provided the displayed finite words are well defined. The marker \(z\) must not occur in \(X\). The distinct-adjacency condition means the *same* boundary symbol \(a\) occurs at both ends of \(X\), but nowhere as the pair \(aa\) inside \(X\). Every occurrence here is contiguous. A net occurrence is counted as a position-and-length pair, not merely as a distinct factor. The d-bonacci result covers the displayed *initial* iterates only; it makes no claim about \(k\ge d+2\).

## Proof

**(1) Exact factor multiplicities in the marked-square word.** There are exactly two occurrences of \(z\) in \(T\), at positions \(m\) and \(3m+1\). Thus the factor \(B=XzX^-\), which has \(z\) at its fixed offset \(m\), can occur only at positions \(0\) and \(2m+1\); direct inspection of the displayed concatenation gives both. The first occurrence is a prefix, the second a suffix. Any defined one-character extension of either is unique, because the other occurrence is at a boundary. Hence both occurrences of \(B\) are net.

The \(z\)-free runs of \(T\) are \(X\), \(XX\), and \(X^-\). The pair \(aa\) appears exactly once in the entire word, at the join between the two consecutive copies of \(X\): it appears there because \(X\) ends and starts in \(a\), and nowhere else because \(X\) avoids \(aa\), \(z\ne a\), and \(X^-\) is a factor of \(X\). Consequently, an occurrence of \(X\) cannot cross the central join, nor can it cross a marker \(z\). Since each remaining complete copy of \(X\) has length exactly \(m\), the complete occurrences of \(X\) are precisely at positions \(0\), \(m+1\), and \(2m+1\). The occurrence at \(m+1\) has unique left extension \(zX\) (the other complete occurrences have no left neighbor or have neighbor \(a\)), and unique right extension \(Xa\) (the other complete occurrences are followed by \(z\)). It is therefore net.

**(2) Exhaustion.** A proper sub-occurrence of a net occurrence cannot itself be net: every one-symbol extension toward the larger occurrence appears in at least two copies of its longer repeated factor. Now consider any repeated nonempty factor occurrence \(H\). If \(H\) contains a marker \(z\), it cannot contain both occurrences of \(z\), since such a factor would occur only once. Its two or more occurrences must align their sole \(z\) with the two markers of \(T\). The maximum common left context has length \(m\), and the maximum common right context has length \(m-1\); hence \(H\) lies inside one of the two displayed net occurrences of \(B\). If \(H\) does not contain \(z\), it lies in one of the three \(z\)-free runs. Any occurrence crossing the central \(X|X\) join contains the unique pair \(aa\), and therefore cannot be repeated. Every remaining occurrence lies wholly in a displayed copy of \(X\), contained either in \(B\) or in the middle net occurrence of \(X\). Thus every repeated occurrence other than the three identified ones is a proper sub-occurrence of one of them and is not net. This proves the marked-square theorem.

**(3) Initial d-bonacci iterates.** Define the Zimin-type words \(Z_1=0\) and \(Z_{j+1}=Z_j\,j\,Z_j\) for \(j\ge1\). They begin and end with \(0\), contain no \(00\), and satisfy \(|Z_j|=2^j-1\). Write \(Z_j^-\) for deletion of the last symbol. For \(1\le j\le d-1\), direct induction on the Zimin recursion gives
\[
\sigma_d(Z_j)=Z_{j+1}^-.
\]
The base case is \(\sigma_d(0)=01=Z_2^-\). In the induction step, \(\sigma_d(j)=0(j+1)\) for \(j<d-1\), whence \(\sigma_d(Z_{j+1})=Z_{j+1}^-0(j+1)Z_{j+1}^-=Z_{j+2}^-\). It follows that \(W_0=0\), \(W_k=Z_k\,k\) for \(1\le k<d\), and \(W_d=Z_d\). Applying \(\sigma_d\) once more yields
\[
W_{d+1}=Z_d Z_d^- = X(d-1)XX(d-1)X^-,\qquad X=Z_{d-1}.
\]
Since \(X\) begins and ends in \(0\) and avoids \(00\), the marked-square theorem gives exactly three net occurrences, at the advertised positions and lengths.

For \(k=0,1\), all factors appearing in \(W_k\) are unique. For \(2\le k<d\), write \(W_k=Y(k-1)Yk\) with \(Y=Z_{k-1}\); for \(k=d\), write \(W_d=Y(d-1)Y\) with \(Y=Z_{d-1}\). In each case the separators occur only once and are absent from \(Y\). Any repeated factor must therefore be contained in one of the two complete copies of \(Y\). The two copies of \(Y\) are themselves net, because their defined one-character extensions are distinguished by a unique separator or a word boundary. Their proper sub-occurrences cannot be net. This gives exactly two and completes the corollary.

## Verification

Run `python3 verify_net_occurrences.py` without external dependencies. The checker counts the multiplicities of *all* nonempty proper factors and independently tests their two one-character extensions. It checks the entire predicted occurrence set for 173 binary or ternary marked-square instances with arbitrary admissible interiors. It also checks all initial iterates \(0\le k\le d+1\) for every \(2\le d\le8\). Expected stdout is supplied in `verification_output.txt`. Finite tests corroborate the symbolic argument but are not used in place of proof for arbitrary \(X\) or \(d\).

## Relationship to prior work

Guo and Kishi (2025) introduced overlapping net-occurrence covers and proved the three-occurrence theorem for finite Fibonacci words and nine for finite Thue–Morse words. Kishi, Guo, Urbina and Bannai (2026) investigated occurrence-preserving morphisms and their relation to net occurrences and minimal unique substrings. Faro and Pavone (2026) proved two-or-three net-occurrence counts for period-aligned regular epistandard morphic approximants. They explicitly do not cover intermediate standard d-bonacci iterates, among which the first post-Zimin iterate \(W_{d+1}\) lies for \(d\ge3\). The present result handles that boundary using a general unique-adjacency mechanism not stated in those inspected papers. The Fibonacci instance \(d=2\) is already known and is not claimed as original.

## Limitations

The general result needs a fresh marker and avoidance of a repeated endpoint digram inside \(X\); removing these hypotheses can produce additional net occurrences. The d-bonacci application is an initial-iterate classification, not a count for every higher iterate. The priority assessment does not establish global uniqueness of the statement; an implicit derivation from general string net-frequency theory or inaccessible literature is possible. The mathematical proof is not an independently audited certification.

## References

- P. Guo and K. Kishi, *Net Occurrences in Fibonacci and Thue-Morse Words*, arXiv:2505.02307, first public 2025-05-05. https://arxiv.org/html/2505.02307v1
- K. Kishi, P. Guo, C. Urbina and H. Bannai, *On Occurrence-Preserving Morphisms*, arXiv:2605.18034, first public 2026-05-18. https://arxiv.org/html/2605.18034v1
- S. Faro and A. Pavone, *Exact Net-Occurrence Counts in Purely Morphic Regular Epistandard Words*, arXiv:2610.04298, first public 2026-10-03. https://arxiv.org/abs/2610.04298
