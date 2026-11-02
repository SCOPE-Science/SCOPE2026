# Complete circular-discrepancy distribution of binary order-five de Bruijn cycles

## Finding

Let \(\mathcal B_5\) be the set of binary de Bruijn cycles of order \(5\), identified up to cyclic rotation but **not** up to reversal or bit complementation. Every \(w\in\mathcal B_5\) is a cyclic word of length \(32\) containing each binary five-word exactly once. Define its *circular discrepancy* by

\[
\operatorname{disc}(w)=\max_{0\le s<32}\max_{1\le\ell\le32}\left|\sum_{j=0}^{\ell-1}\bigl(2w_{(s+j)\bmod32}-1\bigr)\right|.
\]

**Exact classification.** There are \(2048\) cycles in \(\mathcal B_5\). Their complete discrepancy distribution is:

| Circular discrepancy | Number of cycles |
| ---: | ---: |
| \(5\) | \(224\) |
| \(6\) | \(688\) |
| \(7\) | \(912\) |
| \(8\) | \(224\) |

No other discrepancy occurs. In particular, the minimum and maximum at order five are exactly \(5\) and \(8\), each attained by exactly \(224\) cycles. A uniform random cycle in \(\mathcal B_5\) has mean discrepancy \(839/128\), and each extremal class has probability \(7/64\). The exact multiplicities and full distribution, not the general minimum-discrepancy value, are the content of this finding.

## Assumptions and scope

The alphabet is \(\{0,1\}\). Cycles are directed, labeled binary strings modulo cyclic rotation only. The discrepancy maximizes over *cyclic* contiguous substrings (including those crossing the chosen starting point). A length-\(32\) binary order-five de Bruijn cycle has all \(32\) length-five blocks once and contains exactly sixteen zeros and sixteen ones. No conclusions are made about a different order, a different alphabet, or a different discrepancy convention.

## Proof

**1. Exhaustive feedback encoding.** Interpret a five-bit block as a state \((a,u)\), where \(a\in\{0,1\}\) and \(u\in\{0,1\}^4\). Every cyclic de Bruijn sequence defines a permutation of the \(32\) states in one cycle, with shift-register update of the form

\[
T(a,u)=(u,f(a,u)).
\]

For fixed \(u\), the successors of \((0,u)\) and \((1,u)\) have identical leading four bits. Since the update is a permutation, their last bits must be different. Thus there is a unique Boolean map \(g:\{0,1\}^4\to\{0,1\}\) with \(f(a,u)=a\oplus g(u)\). Conversely every such \(g\) defines a bijective shift-register update; it gives an order-five de Bruijn cycle exactly when its orbit from the all-zero state has period \(32\). There are exactly \(2^{16}=65536\) candidate truth tables. Every de Bruijn cycle contains the all-zero five-block exactly once, so rooting the orbit there identifies exactly one truth table per directed cycle modulo rotation. Exhaustive traversal of those \(65536\) tables produces \(2048\) full cycles.

**2. Reduction of discrepancy to prefix-range.** Write a canonically rooted output as \(w_0\ldots w_{31}\) and define \(P_0=0\) and \(P_j=\sum_{i=0}^{j-1}(2w_i-1)\) for \(1\le j\le32\). The de Bruijn property makes the word balanced, hence \(P_{32}=0\). The signed sum of any nonwrapping circular substring is a difference of two prefix values; for a wrapping substring the equality \(P_{32}=0\) gives the same assertion with opposite sign. Conversely any pair of prefix values is realized (up to sign) by a contiguous circular substring. Consequently

\[
\operatorname{disc}(w)=\max_{0\le j\le32}P_j-\min_{0\le j\le32}P_j.
\]

The first enumeration computes this quantity for every distinct full-period feedback cycle.

**3. A separate exhaustive encoding.** The binary order-four de Bruijn directed multigraph has sixteen four-bit vertices and thirty-two distinctly labeled five-bit edges. Its Euler circuits correspond bijectively to order-five de Bruijn cycles. Each Euler circuit uses the edge labeled `00000` exactly once. Force that edge first and enumerate every remaining unused-edge extension until all \(32\) edges have been traversed and the walk closes at its initial vertex. A depth-first enumeration with exact used-edge bit masks produces a second set of \(2048\) distinct length-\(32\) words. The second set equals the first set exactly. Independently calculating discrepancy by examining all \(32\times32\) start/length choices yields the same four classes with multiplicities \(224,688,912,224\). Thus the table is a finite exhaustive result with two independent enumerations, not an inference from initial terms.

**4. Derived quantities.** The class sizes sum to \(2048\). Their weighted sum is \(5\cdot224+6\cdot688+7\cdot912+8\cdot224=13424\), giving mean \(13424/2048=839/128\). The extremal probabilities are \(224/2048=7/64\).

## Verification

Run `python3 verify.py` with Python's standard library. It enumerates all \(65536\) truth tables and all rooted Euler circuits, checks that both \(2048\)-element sets coincide, and independently evaluates the prefix-range and direct cyclic-substring discrepancy algorithms. Expected final output is `VERIFY_OK` with histogram `{5: 224, 6: 688, 7: 912, 8: 224}` and sequence-set digest `e8b5746482780303fec542789b123a2d51a892f460137bb9f8a96c85fec30421`. The code is self-contained and uses no external data.

## Relationship to prior work

Cooper and Heitsch (2009 preprint) study discrepancy of the single lexicographically least de Bruijn sequence, with emphasis on initial segments; that does not enumerate the full order-five cyclic population. Gabric and Sawada (2020 preprint, revised 2021) define circular-substring discrepancy and analyze construction families. Their Section 7 expressly proposes studying the discrepancy distribution across *all* de Bruijn sequences and separately conjectures a maximum formula. At order five, the maximum found here equals their conjectured value \(\binom{4}{2}+\lfloor5/2\rfloor=8\), but this finite case does not prove their general conjecture. Álvarez, Becher, Mereb, Pajor and Soto (2024 preprint) prove that the minimum possible binary order-\(n\) discrepancy equals \(n\); therefore the **existence** of discrepancy-five cycles is known and is not claimed as original here. The numerical multiplicities and the entire order-five distribution are not implied by those statements.

## Limitations

This finite exact classification concerns only order five; it does not provide a formula for other orders or prove a distributional limit theorem. The minimum value \(5\) is a special case of an existing general theorem. The maximum \(8\) proves only one case of a previously proposed all-order conjecture. A literature search can miss unindexed enumerations; independent confirmation of historical priority remains appropriate. Computational finiteness is justified by the two complete encodings and their explicit bijections, not solely by agreement of outputs.

## References

1. Joshua Cooper and Christine Heitsch, *The Discrepancy of the Lex-Least De Bruijn Sequence*, first public preprint 2009-03-22, https://arxiv.org/abs/0903.3753.
2. Daniel Gabric and Joe Sawada, *Investigating the discrepancy property of de Bruijn sequences*, first public preprint 2020-05-04, https://arxiv.org/abs/2005.01638; relevant open problems in Section 7 of revised version.
3. Nicolás Álvarez, Verónica Becher, Martín Mereb, Ivo Pajor and Carlos Miguel Soto, *De Bruijn Sequences with Minimum Discrepancy*, first public preprint 2024-07-24, https://arxiv.org/abs/2407.17367.
