# A sharp ternary signed-swap obstruction for two-state probabilistic automata

## Finding

Let \(A_P(w)\) be the least number of states of a probabilistic finite automaton (PFA) whose acceptance probability is uniquely maximized by \(w\) among the words of length \(|w|\) over a specified finite alphabet. For a word \(w=w_1\cdots w_n\) and a signing \(\varepsilon:\Sigma\to\{-1,+1\}\), form a directed graph \(G_\varepsilon(w)\) on its occurring letters as follows. For each adjacent unequal pair \(w_i=a,w_{i+1}=b\), put an edge \(a\to b\) if \(\prod_{j=i+2}^n\varepsilon(w_j)=+1\), and \(b\to a\) otherwise; the empty product is \(+1\).

**Signed-order obstruction.** If \(A_P(w)=2\) and \(w\) contains at least two distinct letters, then \(G_\varepsilon(w)\) is acyclic for some signing \(\varepsilon\). This is a necessary condition, not a proposed characterization of two-state complexity.

**Sharp ternary certificate.** Among ternary words using all three letters, none of lengths \(3,4,5,6\) fails this necessary condition. At length \(7\), exactly \(48\) labeled words fail it, forming the eight classes under permuting the alphabet with canonical representatives

`0100121`, `0101102`, `0102202`, `0110102`, `0120102`, `0121021`, `0121221`, `0122121`.

In particular, every word over any alphabet of at least three letters ending in a relabeling of `0120102` has \(A_P(w)=3\). More generally, each of those \(48\) ternary seven-letter suffixes forces \(A_P(w)=3\), so for every \(q\ge3\) and \(n\ge7\),

\[
\#\{w\in\Sigma_q^n:A_P(w)=3\}\ \ge\ 48\binom q3 q^{n-7}.
\]

The upper bound of three states for every finite word is the theorem of Kjos-Hanssen (2026); the lower bound here is new for these ternary certificates.

## Assumptions and scope

Automata are one-way, with two or more states, row-stochastic transition matrices, a probability distribution of initial states, and a zero-one accepting-state indicator. The word length is fixed when comparing acceptance probabilities. Unique maximization means a strictly positive acceptance gap against **every** other same-length word over the full alphabet. The graph test examines all signings of occurring letters; each edge is strict. The 48-word classification is for seven-letter words with exactly three distinct letters, up to their six alphabet relabelings. The source first publicly appeared on July 28, 2026 (arXiv:2607.26275v1), and supplies the three-state upper bound. The mathematical classification here is in formal languages and automata (68Q45).

## Proof

**Step 1: scalar form of a two-state PFA.** If the acceptance indicator contains zero or two accepting states, no word can be a unique maximizer. Otherwise, label the single accepting state first, and let \(x\in[0,1]\) denote its probability. Each input letter \(a\) acts as an affine map

\[
 f_a(x)=s_a x+t_a,\qquad -1\le s_a\le1,\qquad f_a([0,1])\subseteq[0,1].
\]

An identity letter \(f_a(x)=x\) cannot occur in a uniquely maximizing nonconstant word: every letter in such a word has a boundary next to a distinct letter, and exchanging adjacent identity and nonidentity letters leaves the output unchanged. Thus \(s_a<1\) for every occurring letter and its fixed point \(h_a=t_a/(1-s_a)\) exists in \([0,1]\). Also, if an occurring letter with slope zero appears at any position \(j\ge2\), changing the first input letter leaves the output unchanged, contradicting uniqueness. Hence every letter appearing at a position \(j\ge2\) has nonzero slope. A letter occurring only in the first position may have zero slope, but its slope never appears in any suffix product below; give it either sign.

**Step 2: commutator and directed order.** For two letters \(a,b\), direct expansion yields the identity, independent of \(x\),

\[
 f_b(f_a(x))-f_a(f_b(x))
 =(1-s_a)(1-s_b)(h_b-h_a).
\]

Replace an occurrence of the adjacent block \(ab\) in a uniquely maximizing word by \(ba\). The difference between the original and changed final acceptance probabilities is

\[
 \left(\prod_{j=i+2}^n s_{w_j}\right)
 (1-s_a)(1-s_b)(h_b-h_a)>0.
\]

The factors \(1-s_a\) and \(1-s_b\) are positive, and the suffix slopes are nonzero. Their signs give the graph orientation in the Finding. Each directed edge \(a\to b\) therefore enforces \(h_a<h_b\). Directed cycles are impossible. This proves the signed-order obstruction for all finite alphabets.

**Step 3: one explicit seven-letter obstruction.** For `0120102`, set \(\varepsilon_j=\operatorname{sgn}(s_j)\) and write \(h_0,h_1,h_2\) for the three fixed points. Applying the six consecutive-pair inequalities from Step 2 gives, in order,

\[
\begin{aligned}
&\varepsilon_1(h_1-h_0)>0,\\
&\varepsilon_1\varepsilon_2(h_2-h_1)>0,\\
&\varepsilon_0\varepsilon_1\varepsilon_2(h_0-h_2)>0,\\
&\varepsilon_0\varepsilon_2(h_1-h_0)>0,\\
&\varepsilon_2(h_0-h_1)>0,\\
&h_2-h_0>0.
\end{aligned}
\]

The first and fifth imply \(\varepsilon_1=-\varepsilon_2\); the fourth and fifth imply \(\varepsilon_0=-1\). Consequently the second gives \(h_2<h_1\), and the third gives \(h_0>h_2\), contradicting the sixth. Prefixing any additional word does not change these six suffix comparisons. Permuting letter labels similarly preserves the contradiction. Therefore no two-state PFA witnesses any such word.

**Step 4: exact sharp enumeration.** For each three-symbol-surjective word of length \(3\) through \(7\), enumerate the eight possible signings and the six strict rank orderings of the three fixed points. A word passes precisely if at least one signing and one rank ordering satisfy all adjacent-pair inequalities. Equivalently, a word passes precisely if at least one of its eight graphs is acyclic. The two independent implementations in `verify.py` check all \(2,538\) surjective words, giving the complete table

| Length | Surjective ternary words | Failed signed-order tests | Failure classes under alphabet permutations |
|---|---:|---:|---:|
| 3 | 6 | 0 | 0 |
| 4 | 36 | 0 | 0 |
| 5 | 150 | 0 | 0 |
| 6 | 540 | 0 | 0 |
| 7 | 1,806 | 48 | 8 |

The eight canonical representatives are exactly those listed in the Finding. The finite computation is exhaustive because it loops over every word in \(\{0,1,2\}^n\), checks surjectivity, and visits every possible signing and strict total order; no numerical optimization or search cutoff is used. It establishes sharpness **only for this necessary obstruction**, not the minimum length of a genuinely ternary word with \(A_P=3\).

**Step 5: state complexity and density.** By Step 2, each failed graph test rules out two-state PFAs. One-state PFAs cannot distinguish any same-length words. Kjos-Hanssen's construction gives \(A_P(w)\le3\) over every finite alphabet, so the forbidden suffixes force equality. Over \(q\) symbols there are exactly \(48\binom q3\) suffixes formed by choosing three distinct symbols and one of the \(48\) bad surjective words on them; these suffixes are distinct. Each admits \(q^{n-7}\) arbitrary length-\((n-7)\) prefixes, proving the count.

## Verification

Run `python3 verify.py` with standard-library Python 3.10 or newer. The program independently constructs the signed-order test by (i) checking each of the \(6\) rank permutations and (ii) testing all directed graphs for cycles. Both methods agree on every surjective ternary word of lengths \(3\) through \(7\), and the asserted classification and eight canonical representatives pass. The included `verification_output.txt` is the recorded output of this run. The general obstruction, the seven-letter contradiction, and the positive-density bound are mathematical proofs, not extrapolations of those finite checks.

## Relationship to prior work

Gill (2024) introduced probabilistic automatic complexity, classified **binary** words having two-state complexity, and used fixed points and commutation of two affine maps in Lemma 4.3. This work does not claim the two-map commutation identity as new. Kjos-Hanssen (2026) proved the general three-state upper bound, again without a ternary two-state classification. Here the contribution is a multi-letter signing/partial-order obstruction, the complete first surjective-ternary cutoff of this obstruction, and the resulting explicit, positive-density maximal-complexity suffix family. The length-four arbitrary-alphabet classification from an accessible earlier record addresses a shorter cutoff and does not imply the seven-letter signed-order obstruction. Search and inspection found no equivalent classification; that observation is not a proof of publication priority.

## Limitations

The signed-order test is **only necessary** for \(A_P(w)=2\); passing it does not prove realizability. The length-seven minimality applies to the obstruction among surjective ternary words, **not** to all ternary words of three-state complexity. The positive-density lower bound need not be sharp. The proof assumes the standard fixed-length unique-maximizer PFA definition; variants with tied maxima or varying input length are not covered. Independent review and exhaustive publication-priority verification have not been performed.

## References

1. Kenneth Gill, *Probabilistic automatic complexity of finite strings*, arXiv:2402.13376, first public version February 20, 2024. https://arxiv.org/abs/2402.13376 — definitions, binary two-state classification, and affine fixed-point commutation (Lemma 4.3).
2. Bjørn Kjos-Hanssen, *Every string has probabilistic automatic complexity at most three*, arXiv:2607.26275v1, first public version July 28, 2026. https://arxiv.org/abs/2607.26275 — uniform three-state upper bound over finite alphabets.
