# The first non-universal reflection-complexity spectrum of binary de Bruijn cycles

## Finding
Let \(b\) range over all binary cyclic de Bruijn words of order \(5\), counted up to cyclic rotation, and let \(\mathbf b=b^\omega\). For each \(\ell\), define \(r_{\mathbf b}(\ell)\) to be the number of occurring length-\(\ell\) factors modulo reversal. The length-five value is always \(r_{\mathbf b}(5)=20\). At the **first length capable of distinguishing the cycles**, the exact distribution is

| \(r_{\mathbf b}(6)\) | Number of cyclic words |
| ---: | ---: |
| 22 | 576 |
| 25 | 960 |
| 26 | 192 |
| 28 | 256 |
| 29 | 64 |

The counts sum to the entire set of \(2048\) binary order-five de Bruijn cycles. In particular, the values \(23,24,27\), and every value outside the five-row table, are unattainable.

A structural refinement uses the unique feedback function \(f:\{0,1\}^4\to\{0,1\}\) of the cycle, defined by the recurrence \(x_{i+5}=x_i\oplus f(x_{i+1}x_{i+2}x_{i+3}x_{i+4})\). Let \(A(f)\) be the number of unordered **nonpalindromic** reversal pairs \(\{s,s^R\}\) of four-bit words for which \(f(s)=f(s^R)\); let \(Z(f)\) be the number of **palindromic** four-bit words \(s\) for which \(f(s)=0\). Then

\[
r_{\mathbf b}(6)=28-2A(f)+Z(f).
\]

The complete joint census is

| \(A(f)\) | \(Z(f)\) | \(r_{\mathbf b}(6)\) | Number |
| ---: | ---: | ---: | ---: |
| 0 | 1 | 29 | 64 |
| 1 | 0 | 26 | 192 |
| 1 | 2 | 28 | 256 |
| 2 | 1 | 25 | 960 |
| 3 | 0 | 22 | 576 |

Equivalently, the bivariate enumerator is
\[
\sum_b u^{A(f_b)}v^{Z(f_b)}=64(3u+v)(3u^2+4uv+1).
\]
The sum is over cyclic words, not individual rooted cuts.

## Assumptions and scope
A binary de Bruijn word of order \(n\) is a cyclic word of length \(2^n\) in which every length-\(n\) binary string appears once as a cyclic factor. Rotation is identified; complementation and reversal are **not** identified. In the infinite periodic sequence \(b^\omega\), every circular factor is an ordinary factor. The work concerns the reversal-equivalence factor statistic, not string attractors, discrepancy, the number of globally reversal-symmetric de Bruijn words, or factor conjugacy under cyclic permutation.

All binary order-five cycles have every binary word of length at most five as a factor. The number of all binary words of length five, up to reversal, is \((2^5+2^3)/2=20\), since eight length-five words are palindromes. Thus length six is the first where this statistic can depend on the particular cycle.

## Proof
**Feedback representation (all orders).** For any binary de Bruijn cycle of order \(n\ge2\), consider both order-\(n\) states \(0s\) and \(1s\), where \(s\in\{0,1\}^{n-1}\). Their successors have the form \(s0\) and \(s1\) in some order: their successor states must differ, or the cyclic traversal would repeat a state. Therefore there exists one unique bit \(f(s)\) with transition
\[
   as\longmapsto s\bigl(a\oplus f(s)\bigr),\qquad a\in\{0,1\}.
\]
Conversely, any such feedback map whose transition permutation is a single cycle of length \(2^n\) produces one de Bruijn cycle, and the cycle determines the feedback map. Rotating does not change \(f\). This bijection is exact, not a statement about a sample of feedback maps.

**Reversal accounting (all orders).** A length-\(n+1\) factor is uniquely of the form \(a s b\), with \(b=a\oplus f(s)\). Its reversal \(b s^R a\) also occurs exactly when \(f(s)=f(s^R)\). Let \(P=2^{\lceil(n-1)/2\rceil}\) be the number of palindromic length-\(n-1\) words; let \(A\) count the nonpalindromic reversal pairs with equal feedback values; and let \(Z\) count palindromic \(s\) having \(f(s)=0\). Each of the \(A\) nonpalindromic pairs contributes **two** distinct two-member reversal classes of length-\(n+1\) factors. Each palindromic \(s\) with \(f(s)=1\) contributes **one** such two-member class; when \(f(s)=0\), the two associated factors are separate palindromes. No other distinct factors merge under reversal. As all \(2^n\) order-\(n\) states have distinct length-\(n+1\) extensions, it follows that
\[
 r_{\mathbf b}(n+1)=2^n-2A-(P-Z).
\]
For \(n=5\), \(P=4\), giving \(28-2A+Z\).

**Exhaustive finite step.** There are exactly \(2^{16}=65{,}536\) possible truth tables for \(f:\{0,1\}^4\to\{0,1\}\). `verify.py` iterates them all. For each, it follows the deterministic transition from the all-zero five-bit state until a state repeats, and accepts a map exactly when the orbit returns to the all-zero state after visiting all 32 possible states. This is equivalent to the transition being one 32-cycle, hence equivalent to the de Bruijn property by the preceding bijection. The code evaluates \(A,Z\) and, separately, constructs all length-five and length-six factors and counts reversal classes. Its exact joint counter has the five rows above and totals \(2048\). The enumeration therefore proves the **complete** distribution, not merely existence witnesses.

**Independent graph enumeration.** `crosscheck.cpp` instead traverses the directed binary order-five shift graph by depth-first search, rooting the traversal at vertex `00000`. It visits all 32 distinct vertices and accepts precisely the Hamiltonian directed cycles that return to the root; every cyclic de Bruijn word appears once because `00000` appears only once. For every accepted cycle it reconstructs the word from vertices and directly counts reversal classes of its 32 cyclic length-six windows. This second algorithm produces the same complete five-bin distribution without using feedback-function tests or the formula for \(A,Z\).

## Verification
In a standard Python 3 interpreter run `python3 verify.py`; for independent exhaustive graph traversal compile and run `g++ -std=c++17 -O2 crosscheck.cpp -o crosscheck && ./crosscheck`.

The observed first run printed `VERIFY_OK tables=65536 cycles=2048 r5=20` and the distribution `[(22,576),(25,960),(26,192),(28,256),(29,64)]` with joint counts `[(0,1,29):64, (1,0,26):192, (1,2,28):256, (2,1,25):960, (3,0,22):576]`. The C++ program printed `GRAPH_DFS cycles=2048 nodes=92636 r22=576 r25=960 r26=192 r28=256 r29=64` and `GRAPH_DFS_VERIFY_OK`.

Each verifier is self-contained and uses only standard language facilities. The general identity is proved symbolically; only the order-five frequency distribution is certified by finite exhaustive computation. Assertions in both checkers explicitly reject incomplete or inconsistent censuses.

## Relationship to prior work
Allouche, Campbell, Li, Shallit, and Stipulanti introduced the reflection-complexity invariant and gave general relationships with factor and palindrome complexities, graph interpretations, periodicity results, and evaluations for several infinite words [1]. Their graph-theoretic de Bruijn terminology concerns factor-overlap graphs; the inspected manuscript does not enumerate reflection complexity across **cyclic de Bruijn words of order five**. Our reversal-pair bookkeeping is compatible with their general identity, but the exact cycle distribution and forbidden values are not supplied by it.

Chang and Wang study special de Bruijn cycles with global reverse-complement symmetry and their counting and linear complexity [2]. Those properties do not determine how many length-six cyclic factors have an occurring **plain reversal** in every order-five cycle. Classical de Bruijn enumeration supplies the total 2048 but not its splitting into the five reflection-complexity bins [3].

## Limitations
The enumerated distribution is specific to binary cycles of order five; no order-six or general-order distribution is asserted. The symbolic feedback identity does hold for every binary order \(n\ge2\). There is no assertion about optimality for error-correcting codes, attracting sets, or discrepancy. The exact finite computation is independently replayable but is not a formally machine-checked infinite proof; the infinite-order identity has a human-readable combinatorial argument. Priority risk remains from potentially unindexed equivalent computations or alternate terminology for reverse-pair factor statistics.

## References
[1] J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, and M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302, first public 2024-06-13, https://arxiv.org/abs/2406.09302.

[2] Z. Chang and Q. Wang, *Efficient generation of odd order de Bruijn sequence with the same complement and reverse sequences*, arXiv:2408.01794, first public 2024-08-03, https://arxiv.org/abs/2408.01794.

[3] N. G. de Bruijn, *A combinatorial problem*, Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen, 49 (1946), 758–764. The classical enumeration is background; it is not used as a substitute for the included exact computation.
