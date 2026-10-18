# Even-palindrome pairing in binary de Bruijn cycles and the complete order-five joint spectrum

## Finding
Let \(n\ge2\), and let \(B\) be a cyclic binary de Bruijn word of order \(n\): its \(2^n\) cyclic factors of length \(n\) are precisely the binary words of that length, each once. Let \(\mathcal P_{n+1}(B)\) be its set of distinct cyclic palindromic factors of length \(n+1\).

**General pairing law.** For each nonconstant palindromic binary word \(v\) of length \(n-1\), the two palindromes \(0v0\) and \(1v1\) either both occur in \(B\) or both fail to occur. No palindrome with a constant middle \(v\) occurs. Consequently
\[
|\mathcal P_{n+1}(B)|=2r(B),\qquad 0\le r(B)\le 2^{\lceil(n-1)/2\rceil}-2.
\]
The bound is universal, but sharpness is **not** asserted at arbitrary order.

**Exact order-five joint spectrum.** For \(n=5\), put
\[
A=\{\texttt{001100},\texttt{101101}\},\qquad
C=\{\texttt{010010},\texttt{110011}\}.
\]
Every binary order-five de Bruijn cycle has \(\mathcal P_6(B)\) equal to one of \(\varnothing,A,C,A\cup C\). Among all \(2048\) labeled-binary cycles modulo rotation (without identifying complementation or reversal), the respective exact multiplicities are
\[
\begin{array}{c|rrrr}
\mathcal P_6(B)&\varnothing&A&C&A\cup C\\\hline
\# B&768&512&512&256
\end{array}.
\]
Thus the number of length-six cyclic palindromes is exactly \(0\), \(2\), or \(4\), with multiplicities \(768\), \(1024\), and \(256\). Both extremes are attained. If a rotation class is chosen uniformly, the indicators of occurrence of the complete pair \(A\) and of the complete pair \(C\) each have probability \(3/8\), but their covariance is \(-1/64\); the two pairs are not independent.

## Assumptions and scope
The alphabet is the fixed, labeled alphabet \(\{0,1\}\). All factors are cyclic, including those crossing the displayed linear cut; two cycles are identified only under cyclic rotation. A factor of length \(n+1\) is counted as a distinct word, not by the number of arbitrary repeated occurrences. Here uniqueness of every length-\(n\) factor ensures that these two counts coincide. The all-order law is proved mathematically; the order-five distribution has a finite exhaustive certificate independent of any heuristic sampling.

## Proof
**1. Local transition pairings.** Form the order-\(n\) binary de Bruijn directed multigraph whose vertices are all \((n-1)\)-bit words and whose edges are all \(n\)-bit words: an edge \(av\) enters the vertex \(v\), and an edge \(vb\) leaves it, where \(a,b\in\{0,1\}\). A de Bruijn cycle is exactly an Euler tour of all \(2^n\) labeled edges. Every vertex has two incoming and two outgoing edges. The tour therefore induces a bijection \(\sigma_v:\{0,1\}\to\{0,1\}\): after entering on \(av\), the tour leaves on \(v\sigma_v(a)\).

A cyclic factor of length \(n+1\) centered on the vertex \(v\) is \(av\sigma_v(a)\). It is a palindrome precisely when \(v\) is a palindrome and \(\sigma_v(a)=a\). A bijection of a binary two-element set has either two fixed points or none. This proves the pairing assertion for a nonconstant palindromic \(v\).

If \(v=0^{n-1}\) and \(\sigma_v(0)=0\), the edge \(0^n\) would be followed immediately by itself; the induced successor permutation on edges would then contain a one-edge cycle, impossible in a single Euler tour of \(2^n>1\) edges. Hence \(\sigma_v\) swaps the two incoming labels. The same argument for \(v=1^{n-1}\) eliminates constant-center palindromes. There are exactly \(2^{\lceil(n-1)/2\rceil}\) palindromic \((n-1)\)-bit words, including these two constants. This gives the stated evenness and bound, for every \(n\ge2\).

**2. Specialization to order five.** The four palindromic four-bit vertices are `0000`, `0110`, `1001`, `1111`. The constant vertices cannot contribute. At `0110`, an identity pairing gives exactly `001100` and `101101`; at `1001`, it gives exactly `010010` and `110011`. Every other pairing gives no length-six palindrome. This proves the four-way support classification without computation.

**3. Exhaustive exact multiplicities.** At each of the \(16\) four-bit vertices there are exactly two bijections between its incoming and outgoing labeled edges. Enumerate all \(2^{16}=65536\) independent choices. Encode the choice at vertex \(v\) by a bit \(t_v\): the incoming edge labeled \(av\) is followed by the outgoing edge \(vb\) with \(b=a\oplus t_v\). This produces a permutation \(T\) of all \(32\) five-bit edges. A choice corresponds to a cyclic order-five de Bruijn word if and only if \(T\) is a single \(32\)-cycle. Conversely, every de Bruijn word induces exactly one such set of pairings, so this is a bijection with rotation classes; the edge `00000` is the unique fixed rotation anchor.

The standalone checker `check_palindromes.py` enumerates the **entire** range `setting in range(1<<16)`, constructs each permutation \(T\), tests whether its orbit starting at `00000` has length \(32\), and classifies its palindromic-vertex pairings. It finds exactly \(2048\) one-cycle settings, partitioned as \(768,512,512,256\). Independently, a second routine enumerates Euler tours by backtracking through all unused five-bit edges, with edge `00000` first; it reconstructs the cyclic word and classifies its *actual* length-six factors. It obtains the identical distribution. Each search traverses a finite, fully specified space; this is an exhaustive certificate, not an extrapolation from small cases.

## Verification
Run `python3 check_palindromes.py` with standard Python 3; no packages or external data are required. Successful execution prints `ORDER5_PALINDROME_PROFILE_PASS`, `local_assignments=65536`, `cycles=2048`, `independent_euler_cycles=2048`, and the four exact profile counts. The two routines use distinct enumeration representations and compare their outcomes. The all-order lemma needs no computation; the code certifies the finite order-five counts only.

## Relationship to prior work
The standard Euler-tour representation and the count \(2^{2^{n-1}-n}\) of binary order-\(n\) cycles are classical. Chang–Ezerman–Ke–Wang [1] develop successor rules for generating de Bruijn cycles, not this palindrome pairing law or order-five joint profile. Burris–Motta–Shipman [2] analyze reflection classes in *unoriented* de Bruijn sequences, a different universality constraint. Anisiu–Anisiu–Kása [3] describe constructing palindromes from de Bruijn words and general palindrome complexity, but not the distribution inside ordinary full binary de Bruijn cycles. Chang–Wang [4] study reverse-complement symmetry of selected odd-order cycles rather than the four-way palindrome profile of all order-five cycles.

Related established results for order-three palindromes, an order-four expected palindrome count, and an order-five **longest**-palindrome census concern different quantifiers or invariants. In particular a longest-palindrome histogram does not determine which individual length-six palindromes occur. The present order-five data refine the per-length palindrome spectrum. No claim is made that these cited prior methods, counts, or representations are themselves new.

## Limitations
The complete order-five distribution is finite. No distribution, exact maximum, or attainability of every even value is asserted for arbitrary higher order. Novelty is assessed against the sources inspected and searched; an equivalent unindexed result is still possible. Mathematical correctness and originality have not been independently audited.

## References
[1] Z. Chang, M. F. Ezerman, P. Ke, Q. Wang, *New Successor Rules to Efficiently Produce Exponentially Many Binary de Bruijn Sequences*, first public arXiv version 2019-11-15, https://arxiv.org/abs/1911.06670 .

[2] C. S. Burris, F. C. Motta, P. D. Shipman, *An Unoriented Variation on de Bruijn Sequences*, arXiv:1608.08480, 2016, https://arxiv.org/abs/1608.08480 .

[3] M.-C. Anisiu, V. Anisiu, Z. Kása, *Properties of palindromes in finite words*, Pure Mathematics and Applications 17 (2006), 183–195, https://ictp.acad.ro/properties-of-palindromes-in-finite-words/ .

[4] Z. Chang, Q. Wang, *Efficient generation of odd order de Bruijn sequence with the same complement and reverse sequences*, arXiv:2408.01794, first public version 2024-08-03, https://arxiv.org/abs/2408.01794 .
