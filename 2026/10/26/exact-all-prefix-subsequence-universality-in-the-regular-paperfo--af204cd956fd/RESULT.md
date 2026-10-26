# Exact all-prefix subsequence universality in the regular paperfolding word

## Finding

Let \(p=p_0p_1p_2\cdots\) be the binary regular paperfolding word in the convention \(p_i=1\) when the odd part of \(i+1\) is congruent to \(1\pmod 4\), and \(p_i=0\) otherwise. For every integer \(N\ge 1\), write \(W_N=p_0p_1\cdots p_{N-1}\). Let \(U(N)\) be the greatest \(k\ge0\) for which **every** binary word of length \(k\) occurs as a scattered subsequence of \(W_N\), with the alphabet fixed as \(\{0,1\}\) even when the short prefix contains only one symbol. Put \(\operatorname{odd}(n)=n/2^{\nu_2(n)}\) for positive integers \(n\), and let \(\mathbf 1_E\) be the indicator of condition \(E\). Then

\[
U(N)=\left\lfloor\frac{3N+1}{8}\right\rfloor
-\mathbf1_{N\equiv5\ (\mathrm{mod}\ 16)}
-\mathbf1_{8\mid N\,\land\,\operatorname{odd}(N/8)\equiv3\ (\mathrm{mod}\ 4)}.
\]

In particular, for every \(N\ge1\),
\[
-1\le U(N)-\frac{3N}{8}\le\frac18.
\]
Both endpoints occur infinitely often, so these are sharp uniform discrepancy constants, and \(\lim_{N\to\infty}U(N)/N=3/8\). For each integer \(j\ge3\), \(U(2^j)=3\cdot2^{j-3}\). The shortest binary word absent as a subsequence from \(W_N\) has length \(U(N)+1\).

## Assumptions and scope

A subsequence of \(W_N\) is a word whose letters appear in the same order at strictly increasing positions; the positions need not be consecutive. The theorem is about prefixes beginning at the first symbol, not arbitrary shifted factors or circular words. The binary alphabet is fixed as \(\{0,1\}\) for all prefix lengths, so \(U(1)=U(2)=0\). This paperfolding convention starts `1101100111001001`; it is the bit complement of the zero-one convention in Madill--Rampersad (2012). Complementing a word preserves its subsequence-universality index.

## Proof

**1. Greedy arches compute \(U\).** Scan any binary word from left to right, retaining the first symbol of a new segment. Close that segment immediately upon meeting the opposite symbol, and repeat. Suppose the procedure completes \(c\) segments (arches) and leaves an empty or monochromatic remainder. Every binary word of length \(c\) embeds by selecting its successive requested symbols from the \(c\) arches. For the reverse inequality, form a word from the last symbol of each complete arch and then append any symbol absent from the remainder. Greedy embedding of those last symbols is forced to use the end of each corresponding arch, because every earlier letter in that arch is the opposite symbol. The final symbol cannot be matched in the remainder. Hence a length-\(c+1\) word is absent, proving \(U=c\).

**2. Exact eight-symbol blocks.** From the defining odd-part condition, every aligned block starting at \(8j\) has the form
\[
B_j=p_{8j}\cdots p_{8j+7}=110a_j100b_j,
\quad a_j=\mathbf1_{2\mid j},\quad b_j=p_j.
\]
Indeed, at offsets \(0,1,2,4,5,6\) the symbols are respectively `110100` in the appropriate slots, the offset-three symbol is \(1\) exactly for even \(j\), and the offset-seven symbol equals \(p_j\). In particular \(b_0=1\).

**3. The complete finite scanner transition.** At the start of an aligned block the unfinished greedy arch has one of two states: empty, or containing only zeroes. Encode these states by \(t=1\) and \(t=0\), respectively. A direct scan of each of the four strings \(110a100b\), for \(a,b\in\{0,1\}\), gives
\[
\begin{array}{c|c|c}
\text{incoming }t&\text{number of complete arches in }B_j&\text{outgoing state}\\\hline
1&2+b&\text{empty if }b=1,\text{ zero-only if }b=0\\
0&3+b&\text{empty if }b=1,\text{ zero-only if }b=0
\end{array}
\]
This table can also be checked one symbol at a time: an incoming zero-only segment closes at the first `1`, the rest of the scan behaves identically in both cases, and the last symbol determines the outgoing state. The initial state before \(B_0\) is empty. Therefore the incoming state at block \(B_j\), for \(j\ge1\), is \(t=b_{j-1}\). Set \(b_{-1}=1\) for the initial state. Summing the completed arches telescopes:
\[
U(8k)=\sum_{j=0}^{k-1}\bigl(2+b_j+1-b_{j-1}\bigr)=3k+b_{k-1}-1
\quad(k\ge1),
\]
and \(U(0)=0\).

**4. Every intermediate position.** For \(1\le r\le7\), a scan of the first \(r\) symbols of the current aligned block from either permissible incoming state gives \(1-t+h_r(a_j)\) additional arches, where
\[
\begin{array}{c|rrrrrrr}
r&1&2&3&4&5&6&7\\\hline
h_r(a)&0&0&1&1&2-a&2&2
\end{array}.
\]
Using \(U(8k)=3k+t-1\), with \(t=b_{k-1}\) and the initial convention \(t=1\) when \(k=0\), yields the complete identity
\[
U(8k+r)=3k+h_r(a_k),\qquad k\ge0,\quad1\le r\le7.
\]
In particular \(r=5\) contributes \(3k+1\) for even \(k\) and \(3k+2\) for odd \(k\). The other six positive remainders are independent of \(k\). Comparing this seven-entry table and the \(r=0\) formula with \(\lfloor(3N+1)/8\rfloor\) gives exactly the two indicator corrections in the stated formula: \(r=5\) with even \(k\) means \(N\equiv5\pmod{16}\), while \(r=0\) with \(b_{k-1}=0\) means \(\operatorname{odd}(k)\equiv3\pmod4\).

**5. Sharpness and limits.** Inspecting all eight residues shows \(-1\le U(N)-3N/8\le1/8\). The lower equality holds whenever \(N=8k\) and \(\operatorname{odd}(k)\equiv3\pmod4\), for example all \(k\equiv3\pmod4\). The upper equality holds at every \(N\equiv13\pmod{16}\). Both are infinite arithmetic progressions. Division by \(N\) gives the limit \(3/8\). At \(N=2^j\), \(j\ge3\), the odd part of \(N/8\) is one, so neither correction applies; the dyadic formula follows.

## Verification

`verify.py` uses only Python's standard library. Run `python verify.py` from the directory containing this file. The checker independently generates 262143 paperfolding symbols by iterative folding and by the odd-part arithmetic rule; enumerates both incoming states for all four allowed eight-symbol templates and all partial offsets; checks the formula for all prefix lengths from 1 through 262143; compares exhaustive scattered-subsequence membership for every binary candidate at lengths 0 through 28; and tests dyadic instances. The proof above, not these finite tests, establishes the unrestricted assertion.

## Relationship to prior work

Madill and Rampersad (2012) define the ordinary paperfolding word and establish its abelian *factor*-complexity recurrence, a statistic of contiguous factors and their Parikh vectors. Barker et al. (2020) develop the general scattered-factor universality index and arch method; Kosche et al. (2021) develop shortest absent subsequences via arches. These general frameworks provide the definitions and method but do not in their inspected results state an exact all-prefix value for the regular paperfolding word. Shallit (2024/2025) studies its maximal constant-symbol runs and run positions; those are related but are not the greedy binary arches whose exact prefix counts are computed here. OEIS A014577 tabulates the paperfolding symbols, not these universality-index values. The formula and sharp constant-error law are the assertions under review, not the general arch characterization or the underlying paperfolding recursion.

## Limitations

This classifies fixed-origin prefixes of the regular paperfolding sequence only. It does not treat arbitrary paperfolding folding instructions, shifted factors, circular universality, or the full set/count of shortest absent subsequences. Relevance and exact priority relative to works not accessible through the inspected sources remain to be assessed independently.

## References

- B. Madill and N. Rampersad, *The abelian complexity of the paperfolding word*, arXiv:1208.2856, initially public 2012-08-14. https://arxiv.org/abs/1208.2856
- L. Barker, P. Fleischmann, K. Harwardt, F. Manea and D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629, initially public 2020-03-10. https://arxiv.org/abs/2003.04629
- M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, initially public 2021-08-31. https://arxiv.org/abs/2108.13968
- J. Shallit, *Runs in Paperfolding Sequences*, arXiv:2412.17930, initially public 2024-12-23. https://arxiv.org/html/2412.17930v2
- OEIS A014577, *The regular paper-folding sequence*, https://oeis.org/A014577
