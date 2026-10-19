# Exact triangle count for four-letter one-deletion graphs

## Finding
Let \(\Sigma\) be an alphabet of exactly four symbols. For each integer \(n\ge1\), define the simple graph \(\Gamma_{n,1,4}\) on \(\Sigma^n\) by joining distinct words when they have a common subsequence of length \(n-1\). The number \(T_4(n)\) of unordered triangles of this graph is exactly
\[
T_4(n)=\frac{4^n(405n^3+81n^2+482n-2344)+1920n^2+2176n+2560}{288}.
\]
In particular, \(T_4(n)=(45/32)4^n n^3+O(4^n n^2)\). The result applies to every positive block length, not merely an asymptotic range.

## Assumptions and scope
The alphabet is labeled and has cardinality four; symbol names play no role. An edge represents **one-deletion confusability**, not Hamming distance or equality of whole deletion decks. Two distinct vertices are adjacent if deleting one symbol from each can produce the same length-\(n-1\) word. A triangle comprises three **distinct** vertices with every pair adjacent. The enumeration is of unordered triangles; no claim is made about code optimality, alphabet sizes other than four, or deletion radii larger than one.

## Proof
**1. An exact recognizer for pairwise confusability.** Scan two words \(x,y\) synchronously, one coordinate pair \((a,b)\) at a time. A nondeterministic finite-state alignment recognizer maintains one of the following situations: \(A\), aligned with no deletion yet; \(B\), aligned having deleted one symbol from each word; \(Y_t\), the single pending symbol \(t\) from the second word after deleting a symbol from the first; or \(X_t\), symmetrically. There are four possible values of \(t\). The transitions on reading \((a,b)\) are:

- From \(A\): remain in \(A\) when \(a=b\); enter \(B\) by deleting both letters; enter \(Y_b\) by deleting \(a\); or enter \(X_a\) by deleting \(b\).
- From \(B\): remain in \(B\) when \(a=b\).
- From \(Y_t\), only when \(a=t\): enter \(B\) by deleting current \(b\), or enter \(Y_b\) by matching the pending symbol and carrying forward \(b\).
- From \(X_t\), only when \(b=t\): enter \(B\) by deleting current \(a\), or enter \(X_a\) by matching the pending symbol and carrying forward \(a\).

The initial state is \(A\); only \(A\) and \(B\) are terminally accepting. A successful alignment with one deletion in each word either deletes aligned symbols or has a single-symbol offset between the first and second deleted positions. Thus these transitions describe **all and only** pairwise confusable or equal word pairs, with no restriction on the separation between deletions. This claim is also independently checked by direct deletion-ball intersection for all pairs of length at most four in the verification program.

Determinize by tracking subsets of the \(A,B,X_t,Y_t\) states. Starting from the singleton \(\{A\}\), exactly \(27\) reachable subset states occur for the four-letter alphabet. Let \(M_2\) be their integer transition-count matrix, obtained by summing the \(16\) possible input pairs, \(u_2\) the initial state indicator and \(f_2\) the accepting-state indicator. The number \(P_n\) of **ordered** pairs at deletion distance at most one, with equal pairs included, is \(P_n=u_2M_2^n f_2\).

**2. Three mutually confusable words.** Take the synchronous product of three copies of this determinized pair recognizer, receiving the ordered coordinate triples \((x_i,y_i,z_i)\) and tracking the pairs \((x,y),(y,z),(z,x)\). Exactly \(1549\) product states are reachable from the common start state. Its transition-count matrix \(M_3\) sums over all \(64\) possible input triples. With start vector \(u_3\) and final indicator \(f_3\), the number of ordered triples, allowing coincident vertices, for which all pairs are confusable is \(A_n=u_3M_3^n f_3\).

**3. A finite exact certificate proving infinite formulas.** The standalone `verify.py` rebuilds both deterministic machines from the transitions above using only integer arithmetic. It constructs \(P_n\) through \(n=31\) and \(A_n\) through \(n=1556\) by exact sparse-matrix iteration. With \(E\) denoting forward shift on a sequence, it verifies all \(27\) identities
\[
(E-4)^3(E-1)P_n=0\qquad(1\le n\le27)
\]
and all \(1549\) identities
\[
(E-4)^4(E-1)^3A_n=0\qquad(1\le n\le1549).
\]
These are not finite-data extrapolations. For any \(d\)-state transition matrix \(M\) and polynomial \(Q\), the sequence \(uM^nQ(M)f\) obeys the characteristic-polynomial recurrence of \(M\), by Cayley–Hamilton. If its first \(d\) consecutive values starting at \(n=1\) vanish, every later value vanishes as well. The two verified finite identity families therefore establish the displayed annihilators for **every** \(n\ge1\).

The verifier also establishes, from exact initial conditions and these recurrences, the closed formulas
\[
P_n=\frac{4^n(27n^2-3n+28)-16}{12},
\]
\[
A_n=\frac{4^n(405n^3+405n^2+446n-2104)+1920n^2+2176n+2368}{48}.
\]
Indeed, both right-hand sides are linear combinations of polynomial multiples of \(4^n\) (degrees at most two and three respectively) and polynomial multiples of \(1^n\) (degrees at most zero and two). Consequently they satisfy the corresponding annihilators. Agreement at the first four and seven positive indices respectively fixes every subsequent term.

**4. Remove repeated vertices.** There are \(4^n\) all-equal triples \(x=y=z\). For each of the three possible pair equalities (such as \(x=y\)), exactly \(P_n\) admissible ordered triples satisfy it. Inclusion–exclusion gives \(3P_n-2\cdot4^n\) ordered admissible triples with at least one equality. Each triangle of the simple graph has six orderings, so
\[
T_4(n)=\frac{A_n-3P_n+2\cdot4^n}{6}.
\]
Substitute the two closed expressions and simplify to obtain the formula in the Finding. Its leading term is \((45/32)4^n n^3\), proving the claimed asymptotic.

## Verification
Run `python3 verify.py` using Python 3 and only its standard library. It reconstructs the \(27\)-state pair machine and \(1549\)-state triple machine; computes all needed transfer terms by exact integer arithmetic; verifies the Cayley–Hamilton annihilator identities and both formulas; and **independently** builds actual deletion-output sets for each of the \(4^n\) words at lengths \(1\le n\le4\). The direct graph triangle counts are \(4,172,2484,23968\). The last check corroborates the automaton semantics; the finite-dimensional Cayley–Hamilton argument supplies the proof for all lengths.

## Relationship to prior work
Alon, Bourla, Graham, He, and Kravitz (arXiv:2209.11882; first public version 2022-09-23) define the general-alphabet deletion graph and use its triangle sparsity to improve deletion-code lower bounds. Their Section 2, Lemma 7 and main theorem bound the triangle count by \(O_{\alpha,k}(\alpha^n n^{3k}(\log n)^k)\); they do not give this exact four-letter, radius-one expression or its leading constant. A separate published exact binary enumeration gives \([2^n(n^3+n^2-6n-28)+16(n^2+n+2)]/8\). That binary result does not imply this four-letter formula: its finite alphabet is fixed to two, and the weighted transition matrix has different state multiplicities for four symbols. The present result uses the same broad finite-state strategy but determines a distinct, natural four-letter invariant. Full-text comparison with the relevant literature and statement-level research-record searches found no dominating nonbinary formula; unindexed equivalent earlier work remains possible.

## Limitations
The finite-state matrix dimensions and annihilator checks are computer-assisted but completely reproducible using integer arithmetic and the embedded verifier. The proof uses Cayley–Hamilton to extend these exact finite checks to all lengths; finite brute force is not an infinite proof. The result gives neither a sharp code-size theorem nor exact triangle counts for general alphabet size, and says nothing about deletions of radius two or greater. Originality is assessed against inspected sources, not asserted as formally certified against all literature.

## References
1. N. Alon, G. Bourla, B. Graham, X. He, and N. Kravitz, “Logarithmically larger deletion codes of all distances,” arXiv:2209.11882; first submitted 2022-09-23, https://arxiv.org/abs/2209.11882. See Theorem 1, Lemma 7 and Section 2, with 2026 revision also inspected.
2. “Exact triangle count in the binary single-deletion graph,” public research record `2026/10/4/SCOPE-exact-triangle-count-in-the-binary-single-deletion-graph--a53aac659908`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-triangle-count-in-the-binary-single-deletion-graph--a53aac659908. Its claim is binary only.
