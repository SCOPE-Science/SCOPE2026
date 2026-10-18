# Sharp six-state square-root bound for two-state singleton-endpoint NFAs

## Finding
Let \(A\) be any epsilon-free nondeterministic finite automaton over a finite alphabet, with exactly two states, exactly one initial state, and exactly one accepting state; the two distinguished states may coincide. The square-root language is \(\sqrt{L(A)}=\{w:ww\in L(A)\}\). Under the standard NFA convention permitting a set of initial states, \(\sqrt{L(A)}\) always has an epsilon-free NFA with at most six states. This bound is attained by a binary two-state NFA. Consequently the exact worst-case nondeterministic state complexity in this two-state, singleton-endpoint source class is \(6\), not the generic cubic upper bound \(8\). If the source initial and accepting states coincide, five output states suffice.

## Assumptions and scope
The source automaton has state set \(\{0,1\}\), no epsilon transitions, one initial state \(s\), and one final state \(t\). Its letter transitions may be nondeterministic or empty. The output NFA is epsilon-free but may have multiple initial states, as in the standard definition used in the referenced square-root state-complexity work. State complexity counts states, not transitions; the source alphabet is any finite alphabet, including a unary alphabet. Only the case of *two-state source automata with singleton initial and final sets* is classified; arbitrary multiple-endpoint sources and larger state counts are not claimed.

For a word \(w\), let \(M(w)=(m_{ij})_{i,j\in\{0,1\}}\) be its Boolean reachability matrix, with \(m_{ij}=1\) iff \(A\) has a path from \(i\) to \(j\) labeled \(w\). Thus \(w\in\sqrt{L(A)}\) iff \((M(w)^2)_{st}=1\), where multiplication is Boolean.

## Proof
**Three-state unordered-pair construction.** Consider the three multisets \([0,0],[0,1],[1,1]\). For each input symbol, evolve two independent runs of \(A\), and retain the unordered multiset of their successor states. This is an epsilon-free, three-state NFA. Starting at \([u,v]\) and finishing at \([r,s]\), it accepts \(w\) exactly when there are two \(w\)-labeled runs carrying the starting multiset to the finishing multiset, with either matching of the two endpoints. In particular, if \(s\ne t\), the pair component from \([s,s]\) to \([s,t]\) accepts exactly those words for which \(m_{ss}m_{st}=1\). The component from \([s,t]\) to \([t,t]\) accepts exactly those words for which \(m_{st}m_{tt}=1\).

**Different endpoints.** For \(s\ne t\), Boolean squaring gives
\[
(M(w)^2)_{st}=m_{ss}m_{st}\lor m_{st}m_{tt}.
\]
Take the disjoint union of the two three-state pair automata described above. Make both component starting states initial and both component finishing states accepting. This epsilon-free NFA has six states and recognizes precisely \(\sqrt{L(A)}\).

**Coincident endpoints.** For \(s=t\) and \(u\) the other state,
\[
(M(w)^2)_{ss}=m_{ss}\lor (m_{su}m_{us}),
\]
using idempotence of Boolean multiplication of a single entry. An ordinary two-state copy of \(A\), with initial and final state \(s\), recognizes \(m_{ss}\). A three-state unordered-pair component from \([0,1]\) back to \([0,1]\) recognizes \(m_{00}m_{11}\lor m_{01}m_{10}\). Taking their disjoint union recognizes the required expression: the surplus term \(m_{00}m_{11}\) already implies \(m_{ss}\). Thus five states suffice. These constructions cover all endpoint choices and all input words, including the empty word.

**Sharp binary witness.** Let the two source states be \(0,1\), with initial state \(0\) and final state \(1\). Over \(\{a,b\}\), take transition matrices
\[
M(a)=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad M(b)=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]
Define six pairs \((x_i,y_i)\), with the empty word denoted by \(\varepsilon\):

| \(i\) | \(x_i\) | \(y_i\) |
|---:|:---:|:---:|
| 1 | \(\varepsilon\) | `b` |
| 2 | `a` | `bb` |
| 3 | `ab` | `babb` |
| 4 | `abb` | \(\varepsilon\) |
| 5 | `b` | `bab` |
| 6 | `bb` | `ab` |

The Boolean membership matrix \(H_{ij}=\mathbf1_{\{x_i y_j\in\sqrt{L(A)}\}}\), computed exactly from \(M(x_i y_j)^2\), is
```
110000
010000
111000
111100
111110
111111
```
All diagonal entries equal one. For each \(i\ne j\), at least one of \(H_{ij},H_{ji}\) is zero. Therefore the six pairs form a fooling set. In any accepting NFA, choose one accepting run for each diagonal concatenation and mark its state immediately after \(x_i\). If two marked states were equal, the corresponding two runs could be spliced to accept both cross-concatenations, contradicting the matrix. Thus every NFA recognizing the witness square-root language requires at least six states. The construction above attains six, proving sharpness.

## Verification
`CHECK.py` is a dependency-free Python 3 verifier. It reconstructs the six-by-six fooling-set matrix from the literal binary transition matrices and checks all diagonal and cross conditions. Independently, for each of the \(256\) ordered pairs of Boolean two-by-two letter matrices, all four singleton endpoint choices, and all binary input words of lengths \(0\) through \(8\), it compares Boolean squaring with an explicitly simulated two-component unordered-pair automaton (six states when endpoints differ, five when they agree). This supplies \(523264\) finite equivalence tests. The run's exact stdout appears in `CHECK_OUTPUT.txt`. The proof above covers arbitrary words and alphabets; these tests are reproducibility checks, not a substitute for that proof.

## Relationship to prior work
Onishchenko's *Nondeterministic state complexity of square root* (first publicly posted May 2, 2026, arXiv:2605.02957) establishes a general cubic upper bound and a matching worst-case lower bound using a construction with \(n\ge6\) states and multiple initial and accepting states. Its full accessible HTML text was examined, including the constructions and proof in Sections 3–4. The two-state singleton-endpoint sharp constant and the unordered-pair reduction do not follow from that result: the cubic upper bound here is \(8\), and the high-state lower bound does not cover \(n=2\). Earlier deterministic-root state complexity results concern a different source/output model. Searches of relevant research records, mathematical-literature queries, and accessible same-topic research ledgers did not locate a directly covering statement; this is not a proof of priority.

## Limitations
The target automaton may have two initial states. No bound is asserted for target automata required to have a single initial state, for source NFAs with arbitrary initial or final subsets, or for sources with three or more states. The lower witness is binary but only the source side has singleton endpoints. A semantically equivalent earlier characterization under another notation remains possible. No independent scientific audit has been performed.

## References
1. Sergey Onishchenko, *Nondeterministic state complexity of square root*, arXiv:2605.02957, version 1, posted May 2, 2026. https://arxiv.org/html/2605.02957 .
2. Pascal Caron, Edwin Hamel-de-le-court, Jean-Gabriel Luque, *The state complexity of a class of operations involving roots and boolean operations*, arXiv:2004.12958 (2020), concerning the deterministic language-operation model. https://arxiv.org/abs/2004.12958 .
3. Jean-Camille Birget, *Intersection and union of regular languages and state complexity*, Information Processing Letters 43 (1992), 185–190; fooling-set lower-bound method, as cited in Reference 1.
