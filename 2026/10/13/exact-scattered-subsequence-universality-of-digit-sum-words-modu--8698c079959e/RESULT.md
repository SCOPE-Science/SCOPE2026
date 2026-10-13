# Exact scattered-subsequence universality of digit-sum words modulo base plus one

## Finding

For every integer base \(b\geq 2\), write \(s_b(n)\) for the sum of digits in the ordinary base-\(b\) expansion of \(n\geq 0\), with \(s_b(0)=0\). Set \(m=b+1\), let \(t_b(n)=s_b(n)\bmod m\), and take the ambient alphabet to be the **full** set \(\Sigma_b=\{0,1,\ldots,b\}\). For each \(N\geq0\), let \(U_b(N)\) be the largest \(k\) for which every length-\(k\) word over \(\Sigma_b\) occurs as a scattered subsequence of \(t_b(0)t_b(1)\cdots t_b(N-1)\). The empty prefix has universality index zero.

Write \(N=bq+r\), with \(q\geq0\) and \(0\leq r<b\). If \(b\) is even, then, for **every** \(N\geq0\),

\[
U_b(N)=\left\lfloor\frac{q}{2}\right\rfloor=\left\lfloor\frac{N}{2b}\right\rfloor.
\]

If \(b\) is odd, then for every \(N\geq0\),

\[
U_b(N)=\left\lfloor\frac{q}{2}\right\rfloor+
\begin{cases}
1,&q\text{ odd and }r>d_b(q),\\
0,&\text{otherwise},
\end{cases}
\]

where, for every positive odd integer \(q\),

\[
\nu_b(q)=\max\{h\geq0:b^h\mid q\},\qquad
 d_b(q)=\bigl(-2(\nu_b(q)+1)\bmod(b+1)\bigr)\in\{0,2,\ldots,b-1\}.
\]

The reduction modulo \(b+1\) in the definition of \(d_b(q)\) is the least nonnegative residue. The symbol \(\nu_b\) counts trailing zero digits in base \(b\); \(b\) need not be prime.

**Exact arch positions.** Index letters starting from zero. For each \(i\geq1\), the \(i\)-th greedy arch ends at position \(b(2i-1)+b-1\) if \(b\) is even, and at position \(b(2i-1)+d_b(2i-1)\) if \(b\) is odd. Thus the theorem determines not just the count but every arch boundary.

For every \(h\geq1\), \(U_b(b^h)=\lfloor b^{h-1}/2\rfloor\), and

\[
\lim_{N\to\infty}\frac{U_b(N)}{N}=\frac{1}{2b}.
\]

The discrepancy \(\Delta_b(N)=U_b(N)-N/(2b)\) has sharp bounds: if \(b\) is even, \(-1+1/(2b)\leq\Delta_b(N)\leq0\); if \(b\) is odd, \(-1+1/(2b)\leq\Delta_b(N)\leq(b-1)/(2b)\). In both cases both bounds occur infinitely often.

## Assumptions and scope

There are no coprimality or primality assumptions on \(b\). Subsequence means deletion of symbols without reordering, not contiguous-factor occurrence. The full ambient alphabet contains \(b+1\) symbols regardless of the letters currently present in a short prefix. For \(N=0\) this convention yields \(U_b(0)=0\). The valuation \(\nu_b(q)\) is used only for positive \(q\).

## Proof

**1. Aligned blocks and the inherited arch criterion.** Let \(B_j\) be the length-\(b\) block of letters with indices \(bj,\ldots,bj+b-1\). Since \(s_b(bj+u)=s_b(j)+u\) for \(0\leq u<b\), put \(a_j=s_b(j)\bmod m\) to obtain

\[
B_j=(a_j,a_j+1,\ldots,a_j+b-1)\pmod m.
\]

Every \(B_j\) contains precisely \(b\) distinct letters, and its one missing letter is \(c_j=a_j-1\pmod m\). We use the standard greedy arch characterization of scattered-subsequence universality [1]: scanning from left to right, record distinct letters until all \(m\) symbols have appeared, count one completed arch and clear the recorded set. The number of completed arches is exactly the universality index. This known equivalence is recalled rather than claimed as new. For completeness, each arch supplies any chosen one-symbol subsequence and hence \(k\) arches realize every prescribed word of length \(k\). Conversely, in each completed greedy arch choose the final symbol that first makes that arch rich. That symbol does not appear earlier in the same arch. Appending any symbol absent from the incomplete final rest gives a prescribed word of length \(k+1\) whose greedy earliest matching positions are exactly the successive arch endpoints, followed by a nonexistent match in the rest. Therefore no \((k+1)\)-universality is possible.

**2. Digit carries.** For every \(q\geq1\), the usual increment of a base-\(b\) integer replacing \(\nu_b(q)\) trailing \(b-1\) digits by zeros gives

\[
s_b(q)-s_b(q-1)=1-(b-1)\nu_b(q).
\]

Modulo \(m=b+1\), this is \(a_q-a_{q-1}\equiv1+2\nu_b(q)\pmod m\).

**3. Even bases.** If \(b\) is even and \(q\) is odd, then \(b\nmid q\), and the carry identity says \(a_q=a_{q-1}+1\pmod m\). We prove by induction on \(i\geq0\) that the greedy arch scan is empty just before \(B_{2i}\). The block \(B_{2i}\) contains every symbol except \(c_{2i}=a_{2i}-1\), so no arch finishes inside it. The next block \(B_{2i+1}\) starts at \(a_{2i}+1\), and its letters are \(a_{2i}+1,\ldots,a_{2i}+b\pmod m\). Its last symbol alone equals \(a_{2i}-1\pmod m\), the missing one. Hence the next arch finishes at the last letter of \(B_{2i+1}\), leaving an empty remainder. This proves the induction, the exact arch endpoints, and the even-base formula for any prefix, including incomplete final blocks.

**4. Odd bases.** Now \(b\) is odd, so \(m\) is even. Suppose the scan has reached the beginning of the even-indexed block \(B_{q-1}\), with \(q\geq1\) odd, and the recorded alphabet is empty. Scanning \(B_{q-1}\) records exactly \(\Sigma_b\setminus\{c_{q-1}\}\). By the carry identity, the symbol \(c_{q-1}\) occurs in the succeeding block \(B_q\) at the unique offset

\[
d_b(q)\equiv c_{q-1}-a_q\equiv-2(\nu_b(q)+1)\pmod m.
\]

As \(m\) is even, this offset is even, and hence belongs to \(\{0,2,\ldots,b-1\}\); it is actually among the \(b\) letters of \(B_q\). The arch therefore completes exactly at this offset, not earlier. The remaining part of \(B_q\) has fewer than \(m\) symbols, so no second arch completes inside it.

It remains to check that the scan cannot finish a second arch in \(B_{q+1}\) and has all but one color seen by its end. If \(\nu_b(q)=0\), then \(d_b(q)=m-2=b-1\), so the remaining part of \(B_q\) is empty. The next block is incomplete on its own. If \(\nu_b(q)>0\), then \(b\mid q\), but \(b\nmid(q+1)\). Hence \(a_{q+1}=a_q+1\pmod m\), so \(B_{q+1}\) misses \(c_{q+1}=a_q\). This is also the first letter of \(B_q\), and cannot occur in the suffix strictly after offset \(d_b(q)\). Therefore the union of that suffix and \(B_{q+1}\) still misses \(a_q\), and cannot complete another arch. Nevertheless \(B_{q+1}\) has supplied all colors except its missing color, restoring precisely the same induction hypothesis at the beginning of \(B_{q+2}\). The base case \(B_0\) is immediate, so induction establishes one arch for each pair \(B_{2i},B_{2i+1}\), finishing at offset \(d_b(2i+1)\) in the second block.

A prefix of length \(N=bq+r\) includes \(\lfloor q/2\rfloor\) complete pairs. When \(q\) is even, its partial block is the initial, incomplete half of the next pair, so there is no extra arch. When \(q\) is odd, its partial block is the second half of the current pair and contains the missing color exactly when \(r>d_b(q)\). This proves the full odd-base formula.

**5. Consequences and sharpness.** The formula differs from \(q/2\) by at most \(1/2\), and \(|N/b-q|<1\), yielding the limit and stated sharp discrepancy bounds by direct substitution. For the lower bound, take infinitely many odd \(q\) not divisible by \(b\) and \(r=b-1\). Such \(q\) have \(d_b(q)=b-1\), so the extra indicator vanishes and the discrepancy is \(-1+1/(2b)\). For even \(b\), the upper bound zero occurs at \(N=2bk\) for all integers \(k\geq0\). For odd \(b\), choose infinitely many odd positive \(q\) with \(\nu_b(q)=(b-1)/2\); then \(d_b(q)=0\). Taking \(r=1\) gives discrepancy \((b-1)/(2b)\). Finally, substituting \(N=b^h\) gives the power-prefix formula directly.

## Verification

The accompanying `verify.py` uses only the Python standard library. Run it with `python3 verify.py`; it directly constructs digit sums and scans greedy arches, compares every prefix against the closed formula across bases 2 through 30, independently checks the digit-carry and offset identities, and brute-forces all candidate subsequences for short words. Its reproduced final summary is:

`VERIFY_OK direct_prefixes=91029 carry_relations=58000 brute_subsequence_cases=155 bases=2..30 power_prefixes=checked`

The proof is the symbolic argument above; the finite checks neither certify every integer base nor replace any induction. The exact formula can be evaluated with \(O(\log_b N)\) digit operations for a given base and prefix length.

## Relationship to prior work

Generalized Thue–Morse words are studied through substitution, palindromic structure, and complexity in [2] and [3]. The definition \(s_b(n)\bmod m\) is classical. Barker et al.'s greedy-arch characterization, as presented in [1], makes universality computable for an arbitrary finite word; [1] supplies further arch-jumping and compressed-word algorithms. These general results do not by themselves specify arch endpoints for the infinite digit-sum family with modulus exactly \(b+1\). The contribution proved here is the **uniform all-base, all-prefix exact classification**, including the previously non-obvious distinction between even and odd bases and the trailing-zero controlled early arches. Work on \(k\)-binomial complexity of generalized Thue–Morse words [3,4] studies counts and equivalences of bounded-length subsequences within factors, not this all-word universality index over the full ambient alphabet.

## Limitations

The theorem concerns modulus exactly \(b+1\), not arbitrary moduli, other alphabets, contiguous subwords, or circular universality. Originality has been checked against identified published sources and mathematical databases but remains subject to unindexed or inaccessible equivalent prior derivations. No independent external audit is asserted.

## References

[1] Ph. Schnoebelen and J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932, first public 24 April 2023. https://arxiv.org/abs/2304.11932.

[2] Š. Starosta, *Generalized Thue-Morse words and palindromic richness*, arXiv:1104.2476, 2011. https://arxiv.org/abs/1104.2476.

[3] H. Lü, J. Chen, Z. Wen, and W. Wu, *On the 2-binomial complexity of the generalized Thue-Morse words*, arXiv:2112.05347, 2021. https://arxiv.org/abs/2112.05347.

[4] H. Golafshan, M. Rigo, and M. Whiteland, *Computing the k-binomial complexity of generalized Thue–Morse words*, arXiv:2412.18425, first public 24 December 2024; consulted as subsequent related literature, not as the 2023 motivating source. https://arxiv.org/abs/2412.18425.
