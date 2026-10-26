# Maximal determinization complexity and exact spatial-image entropy of elementary cellular automaton Rule 73

## Finding

Let \(F:\{0,1\}^{\mathbb Z}\to\{0,1\}^{\mathbb Z}\) be elementary cellular automaton Rule 73: its local output is \(1\) precisely for input neighborhoods `000`, `011`, and `110`. Let \(Y=F(\{0,1\}^{\mathbb Z})\) be its **one-step spatial image**, with the ordinary spatial shift, and let \(a_n=|\mathcal L_n(Y)|\) for all integers \(n\ge0\), where \(a_0=1\).

1. The minimal complete deterministic finite automaton recognizing \(\mathcal L(Y)\) has exactly **16 states**, including a rejecting sink. This attains the full \(2^4\) subset bound for the canonical four-state labeled de Bruijn image presentation.
2. The image is **strictly sofic**. For every integer \(k\ge1\), the word `11001` followed by \(k\) zeros and then `11` is minimally forbidden: \(11001\,0^k\,11\).
3. The exact word-complexity generating function is \(A(z)=N(z)/D(z)\), with

\[
\begin{aligned}
N(z)={}&1-2z+z^2+z^4-2z^5+3z^6-4z^7+z^8+3z^9\\
 &-4z^{10}+4z^{11}-2z^{12}+z^{13},\\[2mm]
D(z)={}&1-4z+5z^2-2z^3+z^4-4z^5+9z^6-13z^7\\
 &+12z^8-7z^9+z^{10}+4z^{11}-6z^{12}+4z^{13}-2z^{14}.
\end{aligned}
\]

The initial block counts are \(1,2,4,8,16,32,62,119,225,427,808,1526\).

4. The spatial topological entropy is \(h_{\mathrm{top}}(Y)=\log\lambda\), where \(\lambda=1.8864996390854936195\ldots\) is the positive Perron root of the transition matrix in the proof. In particular \(h_{\mathrm{top}}(Y)=0.6347230691078676926\ldots\). This root satisfies
\[
\begin{aligned}
0={}&\lambda^{14}-4\lambda^{13}+5\lambda^{12}-2\lambda^{11}+\lambda^{10}-4\lambda^9\\
&+9\lambda^8-13\lambda^7+12\lambda^6-7\lambda^5+\lambda^4\\
&+4\lambda^3-6\lambda^2+4\lambda-2.
\end{aligned}
\]

## Assumptions and scope

All configurations are bilateral binary configurations indexed by \(\mathbb Z\). The image \(Y\) is the set obtained after exactly one Rule 73 application, not the eventual limit set, not an invariant subsystem selected by special initial conditions, and not the entropy of the time-evolution map \(F\). The word language consists of precisely the finite blocks appearing in some element of \(Y\).

A finite binary word occurs in \(Y\) if and only if some finite input block of length two greater maps to it. Indeed, the forward implication is immediate; for the converse, extend the finite input block arbitrarily to a bilateral input. Thus finite-path recognition below has no extra extension assumption.

## Proof

**1. Exact labeled image graph.** Index the input two-letter states `00`, `01`, `10`, `11` by \(j=0,1,2,3\). For an input triple \((a,b,c)\), draw an arrow from \(2a+b\) to \(2b+c\), labeled by its Rule 73 output. For a subset \(S\) of the four states let \(T_e(S)\) be the union of all arrow destinations with label \(e\in\{0,1\}\). Encode \(S\) by its bit mask \(m=\sum_{j\in S}2^j\). All finite output words are accepted by the deterministic automaton starting at mask \(15\), updating via \(T_e\), and accepting precisely when the final mask is nonzero.

The complete transition table, directly obtained from the eight rule triples, is:

| Mask \(m\) | \(T_0(m)\) | \(T_1(m)\) | Shortest reaching word from mask 15 |
|---:|---:|---:|:---|
| 0 | 0 | 0 | `100111` |
| 1 | 2 | 1 | `111` |
| 2 | 4 | 8 | `1110` |
| 3 | 6 | 9 | `110` |
| 4 | 3 | 0 | `10011` |
| 5 | 3 | 1 | `11` |
| 6 | 7 | 8 | `1100` |
| 7 | 7 | 9 | `11000` |
| 8 | 8 | 4 | `11001` |
| 9 | 10 | 5 | `1101` |
| 10 | 12 | 12 | `11010` |
| 11 | 14 | 13 | `10` |
| 12 | 11 | 4 | `1001` |
| 13 | 11 | 5 | `1` |
| 14 | 15 | 12 | `100` |
| 15 | 15 | 13 | empty word |

Every listed reaching word can be checked by transition-table multiplication. Hence all \(16\) possible subsets are reachable. Moreover, each of the suffixes `111`, `11001`, `0111`, `10011` is readable from **exactly one** of the four original two-letter states, respectively states \(0,1,2,3\). A subset accepts one of these four suffixes if and only if it contains the corresponding original state. Thus distinct masks have distinct right languages: no deterministic-state merger is possible. The complete minimal DFA has exactly \(16\) states.

**2. Unbounded minimal obstructions.** In mask notation,
\[
T_{11001}(15)=8,\qquad T_0(8)=8,\qquad T_1(8)=4,\qquad T_1(4)=0.
\]
Consequently every word \(w_k=11001\,0^k\,11\), \(k\ge1\), is forbidden. Removing its last letter yields a legal word ending in mask \(4\). For the suffix obtained by removing its first letter, \(T_{1001}(15)=12\), and for \(k\ge1\),
\[
T_{0^k}(12)\in\{11,14,15\},\qquad
T_{11}(11)=5,\quad T_{11}(14)=4,\quad T_{11}(15)=5.
\]
The latter suffix is also legal. Because image languages are factorial, every proper contiguous factor of \(w_k\) is legal: every such factor belongs to either the length-one-shorter prefix or suffix. The words \(w_k\) are therefore minimally forbidden, with unbounded lengths. A shift of finite type has bounded lengths of minimal forbidden words; hence \(Y\) is not of finite type. The finite labeled presentation shows it is sofic.

**3. Rational count certificate.** Delete the rejecting mask \(0\). Form the integer \(15\times15\) matrix \(M\) indexed by masks \(1,\ldots,15\), with entry \(M_{ij}\) equal to the number of labels \(e\in\{0,1\}\) for which \(T_e(i)=j\). Let \({\bf1}\) be the all-one column and \(e_{15}\) the column basis vector selecting initial mask \(15\). Unique determinism gives for every \(n\ge0\):
\[
a_n=e_{15}^{\mathsf T}M^n{\bf1},\qquad
A(z)=e_{15}^{\mathsf T}(I-zM)^{-1}{\bf1}.
\]
Computing the characteristic polynomial of this explicit integer matrix yields
\(\det(I-zM)=D(z)\), where the coefficient of \(z^{15}\) is zero. The complete numerator identity is
\(e_{15}^{\mathsf T}\operatorname{adj}(I-zM){\bf1}=N(z)\). Both are exact finite integer-polynomial identities, independently reproduced by the standalone `verify.py` using matrix traces and coefficient-wise vector recurrences. This proves the rational function for *all* lengths rather than guessing a recurrence from a finite initial segment.

**4. Entropy.** The same explicit matrix satisfies \(M^9>0\) entrywise (checked from its finite integer entries); therefore it is primitive. Perron--Frobenius gives a simple positive eigenvalue \(\lambda\) strictly larger in absolute value than its other eigenvalues, and \(a_n\) grows at exponential rate \(\lambda\). It follows that the spatial entropy is \(\log\lambda\). The displayed degree-14 polynomial is the characteristic polynomial with the zero eigenvalue removed; the numerical approximations follow by root evaluation. No inference about temporal entropy is made.

## Verification

The independently executable standard-library `verify.py` reconstructs all \(16\) subset transitions from the original eight neighborhoods, checks reachability and four singleton-distinguishing suffixes, verifies the forbidden-word cycle algebra and \(255\) example instances, recomputes the integer characteristic polynomial and generating-function numerator, compares directly generated output blocks against DFA acceptance for lengths \(0\) through \(12\), and checks positivity of \(M^9\).

The mathematical proof of infinitely many minimal forbidden words and all word counts uses finite transition identities and induction, not the finite checks of individual example instances. To reproduce: run `python3 verify.py` in this package directory.

## Relationship to prior work

Jen's one-step preimage recurrence methods and Fukś's subsequent preimage-sequence work concern preimage multiplicities and multistep occurrence statistics, rather than the **number of distinct words** in Rule 73's one-step image. Chen, Chen, Bian, and Chen studied Rule 73's time evolution on explicitly constructed invariant subsystems and computed associated restricted **temporal** entropies, not the spatial entropy or minimal deterministic presentation of \(F(\{0,1\}^{\mathbb Z})\). Kang's Rule 73 study principally investigates long-distance (nonadjacent-neighborhood) variants. Salo develops general sofic-image and regularity theory, without an evaluated Rule 73 image-language formula in the inspected text. Standard de Bruijn/subset constructions are used here and are not claimed as new.

Searches for image languages, minimal forbidden words, subset determinization, canonical rule equivalences, and the specific root and obstruction family did not locate this evaluated combination in accessible indexed literature or compared mathematical research records. This is **not** a proof of historical novelty; a nonindexed table or uninspected specialization may predate it.

## Limitations

The theorem addresses a single classical rule's **one-step spatial image**, not its temporal trajectory entropy, long-time attractor, or all elementary rules. The infinite forbidden family is proved minimal but is not claimed to enumerate *all* minimal forbidden words. The automaton and exact word-count identity are fully determined; other possible structural invariants of the same image remain open here. Historical priority awaits independent verification, especially for older classification tables and one unavailable Rule 73 manuscript. The 2011 conference source precedes the earliest day-level verified motivating arXiv source; the exact date of that earlier public availability was not established.

## References

- H. Fukś, *Sequences of preimages in elementary cellular automata*, first arXiv submission 2013-05-28, arXiv:1305.6533. https://arxiv.org/abs/1305.6533
- J. Chen, F. Chen, Y. Bian, and W. Chen, *Dynamics of Wolfram's Class III Cellular Automaton Rule 73*, WORLDCOMP/CSC 2011, proceedings PDF. https://worldcomp-proceedings.com/proc/p2011/CSC2769.pdf
- L. Kang, *Investigation of Rule 73 as Case Study of Class 4 Long-Distance Cellular Automata*, arXiv:1310.3311, first submission 2013-10-11. https://arxiv.org/abs/1310.3311
- V. Salo, *On von Neumann regularity of cellular automata*, arXiv:2209.13373, 2022. https://arxiv.org/abs/2209.13373
- Wolfram Atlas, *Rule 73 — Rule properties*. https://atlas.wolfram.com/01/01/73/01_01_1_73.html
