# Exact small-list two-deletion capacities at binary length seven

## Finding

For binary length-seven block codes with two adversarial deletions, define \(M_L\) as the largest cardinality of a code for which each five-bit received word belongs to the deletion shadows of at most \(L\) different codewords. Then the complete low-list profile for \(1\le L\le6\) is

\[
\boxed{(M_1,M_2,M_3,M_4,M_5,M_6)=(5,11,16,21,26,32).}
\]

In particular \(M_L=5L+1\) for \(2\le L\le5\), while the endpoints are \(M_1=5\) and \(M_6=32\). These are unrestricted, not necessarily linear, codes.

## Assumptions and scope

Let \(U=\{0,1\}^{7}\) and \(V=\{0,1\}^{5}\). A word \(v\in V\) is a descendant of \(w\in U\) when it is obtained by retaining a five-element increasing set of positions, or equivalently deleting exactly two positions. Write \(D(w)\subseteq V\) for the **set of distinct** descendants, so repeated deletion patterns yielding the same word are counted once. For \(C\subseteq U\), define \(m_C(v)=|\{w\in C:v\in D(w)\}|\). List size at most \(L\) means \(m_C(v)\le L\) for every \(v\in V\). The optimum \(M_L\) maximizes \(|C|\) under that condition. All six values in the theorem refer to exactly two deletions; this is equivalent to up to two deletions for a fixed-length source code.

## Proof

There are exactly \(128\) source words and \(32\) possible received words. The attached `certificates.json` gives, for each of the six values of \(L\), (i) an explicitly listed set \(C_L\) of \(M_L\) distinct source words, (ii) a nonnegative rational number \(a_v\) for every \(v\in V\), and (iii) a nonnegative rational number \(b_w\) for every \(w\in U\). They satisfy

\[
\sum_{v\in D(w)}a_v+b_w\ge1\qquad(w\in U),
\]

and the precise certificate objectives are

| \(L\) | Witness size | \(L\sum_v a_v+\sum_w b_w\) |
|---:|---:|---:|
| 1 | 5 | \(256/45\) |
| 2 | 11 | \(666/59\) |
| 3 | 16 | \(452/27\) |
| 4 | 21 | \(1160/53\) |
| 5 | 26 | \(1430/53\) |
| 6 | 32 | \(2340/73\) |

For any admissible \(C\), sum the displayed inequality over \(w\in C\), interchange the finite sums, use \(m_C(v)\le L\) and nonnegativity, and obtain

\[
|C|\le\sum_v a_v m_C(v)+\sum_{w\in C}b_w
\le L\sum_v a_v+\sum_{w\in U}b_w.
\]

Each of the six rational objectives is **strictly below** the next integer after the asserted witness size. Hence the objective bounds \(|C|\) by the asserted integer \(M_L\). Each listed \(C_L\) has cardinality \(M_L\) and no received word with multiplicity exceeding \(L\). Combining upper and lower bounds proves every entry of the profile. The verification below checks all of these finite assertions exactly; neither an asymptotic estimate nor the output of a numerical integer-programming solver is used as a proof.

## Verification

Run `python3 verify.py` beside `certificates.json`, using only the Python standard library. It independently constructs each word's deletion shadow both by retaining five positions and by deleting two positions, and compares the two sets for all \(128\) source words. For all six profiles it verifies codebook cardinality and maximum received multiplicity, all \(128\) dual inequalities with exact fractions, nonnegativity, the exact objective, and the strict objective-to-integer inequality. `check_output.txt` is the recorded output of an actual run. The certificates themselves contain the full finite objects and are sufficient for independent rechecking; the printed log alone is not the proof.

## Relationship to prior work

Kiah, Wei and Zeng (2026) develop fixed-list insertion/deletion coding bounds and formulate the numerical-list-size tradeoff as a motivating question. Their Section 7 supplies general finite-length run-counting converses, but does not provide the six-value exact length-seven profile. Substitution of \(n=7\), two deletions, and binary alphabet into their stated converse yields upper bounds weaker than the exact entries here. Lin (2026) provides asymptotic existence lower bounds for list-decodable deletion codes and combinatorial estimates on common subsequences; its full eight-page text does not give this finite exact profile. Guruswami and Håstad (2020/2021) construct explicit two-deletion codes and size-two list codes in asymptotic regimes; their manuscript does not determine these six finite optima. A published length-six size-two-list result gives \(7\) codewords at length six, but does not settle any of the present length-seven capacity values. The novelty claimed here is the **joint exact length-seven profile and its rational finite certificates**, not the general hypergraph formulation or the fractional-cover method.

## Limitations

The statement applies only to binary source length seven, exactly two deletions, and list sizes \(1\) through \(6\). It does not determine capacities at longer lengths, additional list sizes, or larger alphabets. The proof is finite and fully reproducible, but it does not give an asymptotic coding theorem. Exact priority against inaccessible or unindexed literature remains a residual risk; an independent mathematical audit has not been performed.

## References

- Han Mao Kiah, Hengjia Wei and Ruixiao Zeng, *Constant-List Insertion--Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, first posted 2026-09-18, arXiv:2609.21395, https://arxiv.org/abs/2609.21395.
- Andrew D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, first posted 2026-09-22, arXiv:2609.26650, https://arxiv.org/abs/2609.26650.
- Venkatesan Guruswami and Johan Håstad, *Explicit two-deletion codes with redundancy matching the existential bound*, arXiv:2007.10592, https://arxiv.org/abs/2007.10592.
- *Exact length-six binary two-list two-deletion code size*, publicly indexed mathematical result (2026-10-04), https://github.com/Resultary/2026.
