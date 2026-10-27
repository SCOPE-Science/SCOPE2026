# Exact minimal automata for shifted binary digit sums modulo \(m\)

## Finding
Let \(s_2(n)\) denote the number of \(1\)-digits in the binary expansion of a nonnegative integer \(n\). Fix integers \(m\ge 2\) and \(c\ge 0\). Let \(N_m(c)\) be the minimum number of states of a complete deterministic finite automaton with output (DFAO) computing \(s_2(n+c)\bmod m\) on **every** finite binary input word read least-significant digit first, including the empty word and arbitrarily many terminal zeroes.

Put \(\ell=\lceil\log_2(c+1)\rceil\), taking \(\ell=0\) when \(c=0\), and define the finite set
\[
\mathcal P_{m,c}=\left\{\left(\left\lfloor\frac{c+p}{2^h}\right\rfloor,\;s_2((c+p)\bmod 2^h)\bmod m\right):0\le h\le\ell,\ 0\le p<2^h,\ \left\lfloor\frac{c+p}{2^h}\right\rfloor>0\right\}.
\]
Then the **exact** minimal state count is
\[
\boxed{N_m(c)=m+|\mathcal P_{m,c}|.}
\]
In particular, \(N_m(0)=m\). For every integer \(r\ge0\), the entire power-of-two shift family admits the closed form
\[
\boxed{N_m(2^r)=m+\sum_{h=0}^{r}\min\{h+1,m\}=\begin{cases}m+(r+1)(r+2)/2,&0\le r\le m-2,\\mr+m(5-m)/2,&r\ge m-1.\end{cases}}
\]
The two formulas agree at their common boundary if either branch is extended there. In particular, the growth changes from triangular to linear when \(r\) reaches the residue modulus.

## Assumptions and scope
A finite input \(w=b_0b_1\ldots b_{h-1}\in\{0,1\}^*\) represents \(n=\sum_{j=0}^{h-1}b_j2^j\). No canonical-encoding restriction is imposed: every word, including the empty word (representing \(0\)) and words with terminal zeros, must produce the indicated output. The minimum is over complete deterministic Moore automata with output alphabet \(\{0,1,\ldots,m-1\}\). Arithmetic residues are represented by their standard nonnegative representatives.

## Proof
**Residual representation.** After reading an input prefix of length \(h\) with numeric value \(p\), put
\[
d=\left\lfloor\frac{c+p}{2^h}\right\rfloor,\qquad a=s_2((c+p)\bmod 2^h)\bmod m.
\]
For any subsequent least-significant-first suffix representing \(v\), the output is
\[
F_{d,a}(v)=a+s_2(v+d)\pmod m.
\]
Indeed \(c+p+2^hv\) decomposes into the disjoint lower \(h\) digits and the upper integer \(v+d\). Initially \((d,a)=(c,0)\). On reading the next digit \(b\in\{0,1\}\), the transition is
\[
(d,a)\longmapsto\left(\lfloor(d+b)/2\rfloor,\ a+((d+b)\bmod2)\bmod m\right).
\]
The output attached to the state \((d,a)\) is \(a+s_2(d)\bmod m\). Because \(d\) never exceeds \(c+1\), and \(a\) has only \(m\) possibilities, the reachable-state automaton is finite.

**All reachable states are inequivalent.** If two residuals have the same \(d\) and distinct \(a\), their outputs already differ at the empty suffix. If \(0\le d<e\), choose any sufficiently large integer \(L\) with \(2^L>e\) and put \(v=2^L-e\). Then
\[
s_2(v+d)-s_2(v+e)=L-s_2(e-d-1)-1.
\]
The right side changes by one as \(L\) increases, so it is not constant modulo any \(m\ge2\). Thus no fixed offset \(a-a'\) can make the two residual functions agree on every suffix. All distinct reachable pairs are therefore distinct Myhill--Nerode output classes, and **every reachable pair contributes one necessary state**.

**Exact reachable-state set.** For \(0\le h\le\ell\), all positive-quotient residuals are exactly the pairs listed in \(\mathcal P_{m,c}\). Since \(c<2^\ell\), any quotient after \(h\ge\ell\) digits is \(0\) or \(1\). If \(h>\ell\) and the quotient equals \(1\), the low \(h\)-digit remainder is an integer \(u\) in \(\{0,\ldots,c-1\}\). The identical pair \((1,s_2(u)\bmod m)\) already appears at depth \(\ell\), by choosing the lower input value \(p=2^\ell+u-c\), which satisfies \(0\le p<2^\ell\). Hence no additional positive-quotient state appears later. Every zero-quotient state \((0,a)\) with \(0\le a<m\) occurs: choose arbitrarily large \(t\equiv a\pmod m\) with \(2^t-1\ge c\), take \(h=t+1\), and input lower value \(p=2^t-1-c\). Then \(c+p=2^t-1<2^h\) and \(s_2(c+p)=t\). Therefore precisely \(m\) zero-quotient states occur, disjoint from \(\mathcal P_{m,c}\), proving the first formula.

**Dyadic shifts.** If \(c=2^r\), at depths \(0\le h\le r\) the positive quotient is exactly \(d=2^{r-h}\), and the lower remainder \(p\) ranges over every \(h\)-bit integer. The possible digit sums run through \(0,1,\ldots,h\), yielding exactly \(\min\{h+1,m\}\) distinct residues. Different depths have different positive quotients. At depths \(h>r\), any remaining positive quotient is \(1\), and its residues are already attained at depth \(r\). Summing gives the displayed expression. Finally, summing the capped arithmetic progression gives its two stated branches. This completes the proof.

## Verification
The accompanying standalone Python program `checker.py` constructs reachable residual automata, minimizes them independently by iterative Moore partition refinement, computes the explicit finite-set formula without traversing the transition graph, and compares direct outputs with \(s_2(n+c)\bmod m\). It checked every \(2\le m\le9\), \(0\le c\le128\), and all \(0\le n<128\). The results were \(1{,}032\) parameter pairs and \(132{,}096\) direct input tests, all passing. The power-of-two special formula was checked whenever the shift was in range. These finite experiments are reproducibility checks; the all-parameter result follows from the preceding proof.

## Relationship to prior work
Moradi, Rampersad, and Shallit study state complexity for linear subsequences of automatic sequences; their 2025 preprint discusses shifts of Thue--Morse in **most-significant-first** representation and gives a general linear bound, not this exact least-significant-first formula for all residue moduli. Charlier, Cisternino, and Massuir compute the minimal automata for the sets \(q\mathcal T+r\), where \(\mathcal T\) is the even-bit-sum set; this is a multiplication-and-translation construction, not a uniform additive shift of the complete multi-valued digit-sum sequence. Related exact classifications for binary-output shifts do not automatically establish the \(m\)-dependent residue saturation in the present theorem. The present proof works directly from the complete residuals, including the often-important terminal-zero convention.

## Limitations
The result concerns binary digit sums, integer nonnegative shifts, least-significant-first reading, and complete DFAOs defined on all binary words. It makes no statement about least-state counts for most-significant-first input, general bases, sparse or restricted encodings, or values of \(m=1\). The explicit finite-set formula is exact but not necessarily the fastest way to evaluate very large arbitrary shifts. No independent external verification is asserted. Unindexed equivalent automata classifications remain a possible historical-priority limitation.

## References
- D. Moradi, N. Rampersad, and J. Shallit, *Complexity of Linear Subsequences of \(k\)-Automatic Sequences*, arXiv:2512.10017v1, first public 10 December 2025, https://arxiv.org/html/2512.10017v1 .
- É. Charlier, C. Cisternino, and A. Massuir, *Minimal Automaton for Multiplying and Translating the Thue-Morse Set*, Electronic Journal of Combinatorics 28(3), P3.12 (2021), https://doi.org/10.37236/9068 .
- D. Moradi, P. Popoli, J. Shallit, and I. Vukusic, *State Complexity of Shifts of the Fibonacci Word*, arXiv:2603.18858 (2026), https://arxiv.org/abs/2603.18858 .
