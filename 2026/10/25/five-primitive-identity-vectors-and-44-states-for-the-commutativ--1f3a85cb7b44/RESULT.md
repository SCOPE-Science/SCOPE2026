# Five primitive identity vectors and 44 states for the commutative closure of \(S_4\)

## Finding
Let \(G=S_4\), acting on \(\{0,1,2,3\}\). Fix the permutations \(a=(0\ 1\ 2\ 3)\) and \(b=(0\ 1)\), with product evaluated from left to right using ordinary group multiplication \(p q=p\circ q\). Let \(W\subseteq\{a,b\}^*\) contain precisely the words whose group product is the identity. Let \(K=\operatorname{perm}(W)\) consist of every word whose multiset of letters coincides with that of at least one word in \(W\). Then
\[
\Psi(W)=\langle(0,2),(4,0),(3,3),(6,4),(9,3)\rangle_{\mathbb N_0},\qquad \operatorname{sc}(K)=44.
\]
The five vectors are the irredundant additive generators of the Parikh monoid. In particular, writing \(i\) for the number of \(a\)'s and \(j\) for the number of \(b\)'s, membership is equivalent to exactly one of the following disjoint alternatives:

1. \(j\) is even and \(i\equiv0\pmod4\);
2. \(j\ge4\) is even, \(i\ge6\), and \(i\equiv2\pmod4\);
3. \(j\ge3\) is odd, \(i\ge3\), and \(i\equiv3\pmod4\);
4. \(j\ge3\) is odd, \(i\ge9\), and \(i\equiv1\pmod4\).

## Assumptions and scope
Both generators are **positive letters only**: no inverse symbols appear in the input alphabet. The convention is for complete deterministic finite automata, including all rejecting states and without an end marker. The group language \(W\) uses the regular action on all \(24\) group elements, not the four-point permutation action that recognizes a stabilizer language. The claim is specific to this ordered generating pair of \(S_4\); it makes no claim about all generating pairs or about \(S_n\) for arbitrary \(n\).

## Proof
**Finite-group reduction.** Every identity word of length greater than \(24\) has two equal prefix products among the first \(25\) prefix products (including the empty prefix). The intervening nonempty contiguous subword is an identity word of length at most \(24\). Deleting it preserves the group product and reduces the length. By induction, the Parikh vector of any identity word is a sum of Parikh vectors of identity words of lengths at most \(24\). This reduction makes a finite calculation sufficient for a statement about words of arbitrary length.

**Exact finite calculation.** Define \(P_{i,j}\subseteq G\) to be all products of words with exactly \(i\) letters \(a\) and \(j\) letters \(b\). With \(P_{0,0}=\{e\}\), empty sets for negative indices, and right multiplication of sets by a letter,
\[
P_{i,j}=P_{i-1,j}\,a\ \cup\ P_{i,j-1}\,b.
\]
This recurrence considers both possible final letters, so it is exhaustive, not sampled. The standalone `verify_s4.py` builds these subsets of the actual \(24\) permutations for every \(i+j\le24\), compares the resulting identity memberships with all additive combinations of the five displayed vectors at the same lengths, and asserts equality at every coordinate. Generator witnesses, evaluated with the same explicit group law, are `bb`, `aaaa`, `bababa`, `babaababaa` and `baaabaaabaaa` in the order of the vectors above. Each vector is also checked not to belong to the monoid of the other four. The finite-group reduction now gives the monoid equality for all \(i,j\ge0\).

**Membership normal form.** The vectors \((4,0)\) and \((0,2)\) extend any identity count by four \(a\)'s or two \(b\)'s. Every additive combination has matching parity in its two coordinates. For even \(j\), the \(i\equiv0\pmod4\) case is generated solely by the two axis vectors. To have \(i\equiv2\pmod4\), one needs at least \(6\) occurrences of \(a\) and \(4\) of \(b\), and \((6,4)\) attains both bounds. For odd \(j\), one needs an odd number of \((3,3)\) and \((9,3)\) generators: the smallest \(i\equiv3\pmod4\) is \(3\), and the smallest \(i\equiv1\pmod4\) is \(9\). Conversely, subtracting respectively \((0,0)\), \((6,4)\), \((3,3)\), or \((9,3)\) in the four cases leaves a nonnegative combination of \((4,0)\) and \((0,2)\). These observations establish the four membership alternatives.

**A finite recognizing automaton.** The membership test is periodic with \(i\mapsto i+4\) once \(i\ge9\), and with \(j\mapsto j+2\) once \(j\ge3\). Thus the states \((i,j)\) with \(0\le i\le12\), \(0\le j\le4\) suffice. Start at \((0,0)\); on input \(a\), increment \(i\), folding \(13\) to \(9\); on input \(b\), increment \(j\), folding \(5\) to \(3\). Accept according to the four alternatives. All \(65\) states are reachable and this automaton recognizes \(K\).

**Exact minimization.** Refining the initial accepting/rejecting partition by both successors leaves exactly \(44\) right-congruence classes: \(33\) singleton classes, \(9\) classes of size two, and \(2\) classes of size seven. The size-two classes pair \((i,j)\) with \((i+4,j)\) for \(i\in\{6,7,8\}\) and \(j\in\{0,1,2\}\). The two seven-element classes comprise all \((i,j)\) with \(6\le i\le12\), \(3\le j\le4\), split by parity of \(i+j\). All other canonical states are singletons. The included independent pair-distinguishability iteration confirms that every two different resulting classes admit distinguishing suffixes of length at most \(7\), while same-class states agree and have same-class successors. This proves both the lower and upper bounds of \(44\).

## Verification
Run `python3 verify_s4.py` with Python 3 and no external packages. The script reconstructs the finite products, tests the complete bounded Parikh table, validates the five generator witnesses and irredundancy, compares the closed membership test with the generator monoid up to total length \(100\) as a separate corroboration, verifies reachability, and minimizes the explicit complete automaton. Its expected final line reports `CERTIFICATE_OK`, `DFA_raw=65`, `DFA_min=44`, and a distinguishing-suffix horizon of `7`. The unlimited-word proof rests on the cycle-deletion lemma plus the exact \(24\)-step finite certificate; merely testing lengths up to \(100\) is not the proof of the infinite result.

## Relationship to prior work
Hoffmann's *State Complexity Bounds for the Commutative Closure of Group Languages* (first public version 24 April 2020) proves regularity and general state bounds for commutative closures of group languages and constructs lattice-labelled automata. Its Example 4 considers a four-point permutation automaton induced by a transposition and a cycle; that automaton's recognized language is based on a subset of points, whereas the present language is the identity word language for the \(24\)-element group. The source supplies no exact five-generator identity-count monoid or \(44\)-state minimum for this regular-action language. Hoffmann's 2021 study of commutative language operations also concerns general bounds and regularity-preserving constructions. The local comparison with earlier work on dihedral and dicyclic identity languages concerns nonisomorphic group families and distinct generator presentations; those results do not imply this formula.

## Limitations
The statement does not assert a sharp bound for arbitrary group languages or any family of all symmetric groups. Computation is used only for an exhaustive finite \(24\)-step group check and exact automaton minimization, each supplied in full. The literature comparison is not a guarantee against unindexed or unavailable publications; independent mathematical auditing has not been conducted.

## References
1. Stefan Hoffmann, *State Complexity Bounds for the Commutative Closure of Group Languages*, first submitted 24 April 2020, arXiv:2004.11772. https://arxiv.org/abs/2004.11772
2. Stefan Hoffmann, *State Complexity Investigations on Commutative Languages — The Upward and Downward Closure, Commutative Aperiodic and Commutative Group Languages*, first submitted 26 November 2021, arXiv:2111.13524. https://arxiv.org/abs/2111.13524
