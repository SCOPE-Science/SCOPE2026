# A binomial law for shortest common supersequences of opposite permutation powers

## Finding
Fix a finite alphabet of \(q\ge2\) pairwise distinct letters and a permutation word \(P=c_0c_1\cdots c_{q-1}\). Let \(\overleftarrow P=c_{q-1}\cdots c_0\), and for arbitrary integers \(k,\ell\ge1\), put
\[
X=P^k,\qquad Y=(\overleftarrow P)^\ell.
\]
A *common supersequence* of \(X,Y\) is a finite **linear** word containing both as scattered subsequences. Its length is minimized in a *shortest common supersequence* (SCS). All output counts below refer to **distinct output words**, not embeddings, alignments, or choices of occurrence positions.

Define the integer parameters
\[
A=(q-1)k-\ell+1,\qquad B=(q-1)\ell-k+1.
\]
Then the shortest length and the number \(C_q(k,\ell)\) of distinct shortest common supersequences are, for all \(q\ge2\) and \(k,\ell\ge1\),
\[
\boxed{L_q(k,\ell)=\max\{qk,q\ell,(q-1)(k+\ell)+1\}},
\]
\[
\boxed{C_q(k,\ell)=
\begin{cases}
\binom{A+B}{A},& A\ge0\text{ and }B\ge0,\\
1,&\text{otherwise}.
\end{cases}}
\]
In the binomial regime there is a **bijection** between all SCS output words and the binary words containing exactly \(A\) occurrences of an \(X\)-only symbol and \(B\) of a \(Y\)-only symbol. The corresponding SCS is obtained by inserting forced common symbols into a fixed schedule of solo slots (described and proved below). When \(A<0\) or \(B<0\), the shorter input is a subsequence of the longer one, which is the unique SCS.

For equal repetition exponents \(k=\ell=r\), the number is \(\binom{2((q-2)r+1)}{(q-2)r+1}\). Thus this number grows exponentially in \(r\) for every \(q\ge3\), whereas \(q=2\) yields exactly two SCS words, for every \(r\).

## Assumptions and scope
The two base orders are exact reversals, the two exponents are arbitrary positive integers (they need not agree), and every base letter occurs exactly once in \(P\). There is no symbol outside the shared alphabet. A subsequence is allowed to omit positions but preserves their order. Relabeling the letters does not change the conclusions. The cases \(q=2\), \(k=1\), \(\ell=1\), \(A=0\), and \(B=0\) are included. There is no claim about three or more input words, general pairs of periodic words, or minimal-but-not-shortest common supersequences.

## Proof
**1. Greedy simultaneous matching.** Relabel \(c_i\) by \(i\). From a candidate SCS word \(Z\), greedily embed \(X\) and \(Y\) from left to right, each by matching the earliest available next requested symbol. If some position of \(Z\) is used by neither greedy embedding, deleting that position preserves both subsequence embeddings; therefore it cannot occur in a shortest \(Z\). At any state in a shortest word, with \(i\) letters of \(X\) and \(j\) of \(Y\) already matched, the next output letter is either \(X_i\), \(Y_j\), or (if both next letters agree) a letter that advances both greedy embeddings. The greedy state transitions are determined uniquely by the output word.

While both strings are unfinished, the next requested symbols agree exactly when
\[
X_i=Y_j\quad\Longleftrightarrow\quad i+j\equiv q-1\pmod q.
\]
Write \(s=i+j\). A letter advancing only one embedding increases \(s\) by one (*solo step*); a letter advancing both increases \(s\) by two (*common step*). Whenever both inputs are unfinished and their next letters agree, a shortest output must use that common letter immediately: another letter would advance neither greedy embedding and would be deletable.

**2. A universal lower bound.** A common step can start only at \(s\equiv q-1\pmod q\), while both inputs are unfinished. Such a state has \(0\le s\le q(k+\ell)-2\). There are exactly \(k+\ell-1\) integers in this interval congruent to \(q-1\); because \(s\) strictly increases, every greedy merge contains at most \(k+\ell-1\) common steps. Since the two inputs jointly request \(q(k+\ell)\) letters, an output with \(h\) common steps has length \(q(k+\ell)-h\). Consequently every SCS has length at least \((q-1)(k+\ell)+1\) and of course at least \(qk\) and \(q\ell\).

**3. Constructing and classifying all optima when \(A,B\ge0\).** Prescribe the following action skeleton:

- \(q-1\) solo steps;
- \(k+\ell-1\) common steps, separated by exactly \(q-2\) solo steps between successive common steps;
- \(q-1\) final solo steps.

Its total number of solo slots is \(2(q-1)+(k+\ell-2)(q-2)=A+B\); it has \(k+\ell-1\) common slots. Fill these solo slots, from left to right, by **any** binary schedule consisting of precisely \(A\) \(X\)-solo and \(B\) \(Y\)-solo actions. At a common slot output the common next letter of the two inputs. At a solo slot output the next letter of the designated input.

The construction is always legal. Until just before the final common step, at most \(k+\ell-2\) common steps have occurred, so the number of letters consumed from \(X\) is at most \(A+k+\ell-2=qk-1\), and similarly for \(Y\). Both inputs are therefore unfinished at each common step. The starting \(s\)-coordinate of the first common step is \(q-1\), and successive common-step coordinates differ by \(q\); thus their next letters agree. The solo slots before and between common steps have \(s\not\equiv q-1\pmod q\) and hence advance only their designated input. After the final common step, any input exhausted by its allotted solo actions will never be designated again; all remaining actions are valid, and the final solo action consumes the sole remaining letter. The final state has consumed exactly \(A+(k+\ell-1)=qk\) letters from \(X\) and \(B+(k+\ell-1)=q\ell\) from \(Y\). For \(q=2\), the between-common-step solo intervals are simply empty, so the same construction applies.

Each constructed output has length \((q-1)(k+\ell)+1\), attaining the lower bound. Conversely, every shortest output must have exactly \(k+\ell-1\) common steps. The congruence condition and the forced-common-step rule make their locations in \(s\) exactly the common slots of the displayed skeleton; all other steps are solo, with exactly \(A\) of type \(X\) and \(B\) of type \(Y\). Greedy simultaneous matching recovers their types uniquely from the output. Thus the construction is a bijection and gives \(\binom{A+B}{A}\) **distinct** SCS words, with neither duplicate embeddings nor missing outputs.

**4. The unique-output regime.** If \(A<0\), then \(\ell>(q-1)k+1\). To greedily embed \(P^k\) in \((\overleftarrow P)^\ell\), the ordered successive letters of \(P^k\) require exactly \((q-1)k+1\) reverse-order periods: every increasing step within \(P\) needs a new period and the wrap between successive copies needs none. Therefore \(X\) is a subsequence of \(Y\), so \(Y\) itself is the unique shortest common supersequence. If \(B<0\), symmetry makes \(Y\) a subsequence of \(X\), so \(X\) is the unique shortest word. These cases cannot occur simultaneously because \(A+B=(q-2)(k+\ell)+2>0\). On the boundaries \(A=0\) or \(B=0\), the binomial formula also gives one. Combining the regimes proves both displayed formulas.

## Verification
The accompanying standard-library-only program `verify.py` independently computes the exact shortest length and number of distinct shortest supersequences by a dynamic program on the two suffix positions. It checks the theorem in 448 parameter configurations with \(2\le q\le8\) and \(1\le k,\ell\le8\). A separate constructive routine generates 2,592 optimal words from binary schedules, and direct language-set enumeration agrees with the constructed languages for 38 configurations. The recorded verifier output is `VERIFY_OK dynamic_configurations=448 constructed_words=2592 full_language_configurations=38`. This finite checking is corroboration only; the uniform infinite-parameter result rests on the proof above. To reproduce: `python3 verify.py`.

## Relationship to prior work
Bulteau and Zhang (arXiv:2307.04335, first posted 2023-07-10) study SCS for sets of permutation strings and prove NP-hardness when the number of inputs varies. Their input permutations contain each symbol once, and their length notation \(|\mathrm{SCS}(S)|\) refers to optimum *length*, not the number of shortest output strings. Their paper does not supply the present exact two-input reverse-power classification. Hirota and Sakai (arXiv:2307.10552, 2023) give general algorithms for *maximal common subsequences*, a different object. Sopp, Liyanage, Gong, and Zhu (arXiv:2603.22591, 2026) investigate all inclusion-*minimal* common supersequences and offer general algorithms; their inspected theorems do not state this binomial shortest-output formula.

For the same equal-exponent reverse-power inputs, a separate known special-family result identifies **maximal common subsequences** and proves their common length \(2k-1\). That gives the equal-exponent optimum SCS *length* by the standard SCS/LCS duality, but does not determine the distinct shortest supersequences, their binomial multiplicities, or the unequal-exponent uniqueness transition. The present result directly classifies output strings by the forced-match/solo-step bijection, rather than counting longest-subsequence alignments.

## Limitations
The formula relies essentially on two *opposite* base orders, not merely arbitrary related permutations. It does not calculate the number of nonshortest minimal common supersequences. Computational tests cover only finite ranges. General papers on supersequence enumeration could contain equivalent results under another terminology; the literature comparison is evidence rather than a proof of global novelty. Independent validation has not been performed.

## References
- Laurent Bulteau and Louxin Zhang, *The tree-child network problem for line trees and the shortest common supersequences for permutations*, arXiv:2307.04335 (initial public submission 2023-07-10), https://arxiv.org/abs/2307.04335.
- Miyuji Hirota and Yoshifumi Sakai, *Efficient algorithms for enumerating maximal common subsequences of two strings*, arXiv:2307.10552 (initial public submission 2023-07-20), https://arxiv.org/abs/2307.10552.
- Braeden Sopp, Adiesha Liyanage, Mingyang Gong, and Binhai Zhu, *Computing and Enumerating Minimal Common Supersequences Between Two Strings*, arXiv:2603.22591 (initial public submission 2026-03-23), https://arxiv.org/abs/2603.22591.
