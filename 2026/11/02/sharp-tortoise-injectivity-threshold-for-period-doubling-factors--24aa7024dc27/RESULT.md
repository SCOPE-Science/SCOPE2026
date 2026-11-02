# Sharp tortoise-injectivity threshold for period-doubling factors

## Finding
Let \(\mathbf d=\phi^{\omega}(0)\) be the infinite binary period-doubling word, where \(\phi(0)=01\) and \(\phi(1)=00\). For a finite binary word \(w\), define \(T(w)\) by moving the first occurrence of \(1\) to the end, leaving a word without \(1\)'s unchanged. Let \(\mathcal F_n(\mathbf d)\) be the set of distinct length-\(n\) factors, and define \(p(n)=|\mathcal F_n(\mathbf d)|\) and \(\rho_T(n)=|\{T(w):w\in\mathcal F_n(\mathbf d)\}|\).

**Theorem.** The complete one-step tortoise-complexity function is
\[
(\rho_T(1),\ldots,\rho_T(9))=(2,2,3,3,5,7,9,10,13),\qquad
\rho_T(n)=p(n)\quad\text{for every }n\ge10.
\]
The threshold \(10\) is sharp: the distinct length-nine factors `000101010` and `010001010` have identical tortoise image `000010101`. In particular, \(T\) is injective on \(\mathcal F_n(\mathbf d)\) exactly for \(n=1\) and \(n\ge10\).

This is an explicit all-length enumeration because the **previously known** factor complexity satisfies \(p(1)=2\), \(p(2)=3\), and, for each integer \(j\ge2\),
\[
p(2j)=2p(j),\qquad p(2j-1)=p(j-1)+p(j).
\]
These recurrences are prior work (OEIS A275202), not part of the novelty claim.

## Assumptions and scope
The factor language is that of the one-sided infinite fixed point starting in \(0\); factors may start at any nonnegative position. The operator is **one** application of the binary Defant–Kravitz tortoise map, not the hare map or a higher iterate. All exact counts concern distinct factor words, rather than occurrences. The only infinite-word assumptions used in the proof are the explicitly defined substitution and the resulting valuation identity.

## Proof
**1. Valuation description and bounded zero runs.** Number symbols from zero. Induction on the substitution shows
\[
 d_i\equiv \nu_2(i+1)\pmod2 \qquad (i\ge0),
\]
where \(\nu_2\) is the exponent of \(2\) dividing a positive integer: \(d_{2i}=0\) and \(d_{2i+1}=1-d_i\). Because every even-positioned symbol is zero, `11` never occurs. If four consecutive symbols were zero, their two odd-positioned symbols would both be zero, forcing two consecutive symbols of \(\mathbf d\) to be one, a contradiction. Hence **every factor of length four contains a one**.

**2. Prefix inheritance lemma.** Let \(x\) be any infinite binary word, and \(L\ge1\) be such that every length-\(L\) factor contains a one. If \(T\) is injective on the length-\(L\) factors of \(x\), it is injective on length-\(n\) factors for all \(n\ge L\). Indeed, suppose \(u,v\) are length-\(n\) factors with \(T(u)=T(v)\). Each has its first one within its first \(L\) symbols. Writing \(u_L,v_L\) for those prefixes, both \(T(u_L)\) and \(T(v_L)\) equal the first \(L-1\) symbols of the common output followed by a one. Length-\(L\) injectivity gives \(u_L=v_L\). The first-one position is therefore the same in \(u,v\), and reinsertion at that position in the common image gives \(u=v\).

**3. Complete length-ten factor certificate.** Every factor of length ten of \(\mathbf d\) occurs in the 42-symbol prefix \(d_0d_1\cdots d_{41}\). To see this, consider the ten consecutive positive integers indexing any length-ten factor through \(d_i=\nu_2(i+1)\bmod2\). Since \(10<16\), at most one is divisible by \(16\). At all other coordinates the symbol depends only on the integer modulo \(16\). If no multiple of \(16\) occurs, the factor is represented by a window starting at an index between \(0\) and \(15\). Otherwise, place the exceptional coordinate at \(16\) or \(32\), according as its required valuation parity is zero or one; these two numbers have valuation parity zero and one, respectively. The resulting ten-symbol representative starts between \(6\) and \(31\) and ends no later than index \(40\). Thus the first 42 symbols suffice (with a spare endpoint).

Using the substitution (or the valuation formula), this exact prefix is

`010001010100010001000101010001010100010101`

Its 33 starting windows of length ten yield exactly the following 16 distinct factors and their 16 distinct images:

```
0001000100 -> 0000001001
0001000101 -> 0000001011
0001010100 -> 0000101001
0010001000 -> 0000010001
0010001010 -> 0000010101
0010101000 -> 0001010001
0100010001 -> 0000100011
0100010101 -> 0000101011
0101000100 -> 0010001001
0101000101 -> 0010001011
0101010001 -> 0010100011
1000100010 -> 0001000101
1000101010 -> 0001010101
1010001000 -> 0100010001
1010001010 -> 0100010101
1010100010 -> 0101000101
```
Consequently \(T\) is injective at length ten. It follows for **all** longer lengths by the prefix inheritance lemma, since every length-ten factor contains a one.

**4. Complete short-length enumeration.** Every length-\(n\) factor with \(1\le n\le9\) extends to a length-ten factor, so the same 42-symbol prefix contains the entire shorter factor language. Direct sets of the windows and images yield, respectively,
\[
\begin{array}{c|rrrrrrrrr}
n&1&2&3&4&5&6&7&8&9\\\hline
p(n)&2&3&5&6&8&10&11&12&14\\
\rho_T(n)&2&2&3&3&5&7&9&10&13
\end{array}
\]
The displayed pair of length-nine factors verifies sharpness. This finishes all quantifiers of the theorem.

## Verification
Run `python3 pd_tortoise_verify.py` without third-party dependencies. The program computes the 42-symbol prefix independently from the \(2\)-adic valuation and the substitution, enumerates every window for lengths one through ten, prints the complete length-ten input/output table, verifies all counts and the unique collision at length nine, and checks extra larger finite examples. `pd_tortoise_verification_output.txt` contains its actual output. The finite check is exhaustive for length ten **because of Step 3**, not merely because the input prefix is long. The all-length conclusion follows from the separately proved Step 2, not from extrapolating experiments.

## Relationship to prior work
Campbell and Rampersad (first publicly posted April 28, 2026) introduce the factor-tortoise complexity and show that this one-step operation is eventually injective on **paperfolding** factors; for **Thue–Morse**, they derive a different persistent noninjectivity pattern. Their paper's general bounded-deficit theorem does not supply an injectivity threshold or counts for the **period-doubling** fixed point. This theorem establishes the sharp eventual-injectivity threshold and the entire small-length profile for that distinct canonical automatic word. Defant and Kravitz introduced the sorting map itself; the ordinary period-doubling factor complexity recurrence is separately established in the literature and recorded as OEIS A275202. Closely related work on period-doubling attractors and periodic complexity studies different invariants.

## Limitations
Only the period-doubling substitution, binary alphabet, and a single tortoise application are addressed. This does not assert injectivity for arbitrary bounded-gap automatic words or for repeated tortoise operations. It is not a classification of every automatic word. Priority relative to unindexed independently derived calculations remains a residual risk; no independent mathematical audit has been conducted.

## References
1. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811, initial public version April 28, 2026. https://arxiv.org/html/2604.25811v2
2. C. Defant and N. Kravitz, *Stack-sorting for words*, Australasian Journal of Combinatorics **77** (2020), 51–68. https://ajc.maths.uq.edu.au/pdf/77/ajc_v77_p051.pdf
3. OEIS A275202, *Subword complexity of the period doubling sequence*, including the pre-existing recurrence and its 2020 proof. https://oeis.org/A275202
