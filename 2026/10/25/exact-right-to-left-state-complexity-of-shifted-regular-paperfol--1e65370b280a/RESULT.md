# Exact right-to-left state complexity of shifted regular paperfolding words

## Finding

Let \(p(n)\), for \(n\ge 0\), be the regular binary paperfolding sequence. Write uniquely
\[
n+1=2^v(2m+1),\qquad v,m\ge0,
\]
and define \(p(n)=m\bmod2\). For each fixed integer \(c\ge0\), let \(N_{\mathrm{LSD}}(c)\) be the minimum state count of a complete deterministic finite automaton with output that computes \(p(n+c)\) when given the binary digits of \(n\) least-significant first, including the empty representation of zero and arbitrary redundant high-order zeroes. Then
\[
\boxed{N_{\mathrm{LSD}}(c)=\begin{cases}4,&c=0,\\6+\lfloor\log_2 c\rfloor,&c\ge1.\end{cases}}
\]
Thus \(N_{\mathrm{LSD}}(1)=6\), \(N_{\mathrm{LSD}}(2)=7\), and the state count increases by exactly one on crossing every positive power of two beyond one. This is a statement about *minimal* automata, not merely a construction with the displayed number of states.

## Assumptions and scope

The digit alphabet and output alphabet are both \(\{0,1\}\). Every finite digit word \(u\) of length \(k\) is interpreted as the nonnegative integer \(x(u)=\sum_{j=0}^{k-1}u_j2^j\); in particular trailing zeros in the input order do not alter its value. The automaton must give the correct output for every such word, including the empty word. There is no restriction on the shift \(c\) beyond integrality and nonnegativity. The theorem does not address most-significant-first representations or other paperfolding conventions.

## Proof

**1. Exact residual classification.** After reading any \(k\ge0\) low-order digits encoding \(x\), where \(0\le x<2^k\), the remaining-input output function is
\[
F_{k,x}(z)=p(2^kz+c+x),\qquad z\ge0.
\]
Different reachable residual functions require different states, and the residual functions themselves form a complete deterministic automaton under appending input bits. Consequently the minimum state count is exactly the cardinality of the set of distinct \(F_{k,x}\) over all \(k,x\).

At \(k=0\) there is just \(F_{0,0}(z)=p(z+c)\). For \(k\ge1\), divide \(c+x+1=2^kq+r\), \(0\le r<2^k\). The binary-digit definition of \(p\) gives three exhaustive cases:

* If \(r=0\), then \(2^kz+c+x+1=2^k(z+q)\), hence \(F_{k,x}(z)=p(z+q-1)\). The unique \(x\in[0,2^k)\) with \(r=0\) satisfies \(q-1=\lfloor c/2^k\rfloor\). Thus this residual is exactly \(p(z+\lfloor c/2^k\rfloor)\).
* If \(r=2^{k-1}\), then \(2^kz+c+x+1=2^{k-1}(2(z+q)+1)\), hence \(F_{k,x}(z)=(z+q)\bmod2\). For its unique corresponding \(x\), one has \(q=\lfloor(c+2^{k-1})/2^k\rfloor\).
* In every other case \(r\ne0,2^{k-1}\), set \(j=\nu_2(r)\). Then \(j\le k-2\), and the bit of \(2^k(z+q)+r\) immediately above its \(j\) trailing zeros is independent of \(z\). Hence \(F_{k,x}(z)=(r/2^{j+1})\bmod2\), a constant function.

The above cases are also exhaustive at the exceptional small level \(k=1\): its residues are only \(0\) and \(2^{k-1}\), with no constant residuals at that level.

**2. Which residuals occur.** Every level \(k\ge1\) has exactly one residue-zero prefix, so the shifted paperfolding functions appearing among all residuals are
\[
\{z\mapsto p(z+\lfloor c/2^k\rfloor):k\ge0\}.
\]
For \(c=0\) this family has one member. For \(c\ge1\), writing \(m=\lfloor\log_2 c\rfloor\), its members have shifts \(c,\lfloor c/2\rfloor,\ldots,\lfloor c/2^{m}\rfloor=1,0\), hence precisely \(m+2\) distinct members.

For any \(c\), a parity residual occurs at each positive level \(k\), with parity offset \(\lfloor(c+2^{k-1})/2^k\rfloor\). If \(c=0\), these offsets are all zero, so only \(z\bmod2\) occurs. If \(c\ge1\), the offsets are odd at \(k=m+1\) and even at \(k=m+2\), so both \(z\bmod2\) and its complement occur. Finally, already at \(k=2\), the residues \(r=1\) and \(r=3\) occur as \(x\) ranges through its four possibilities. They produce respectively the constant-zero and constant-one residual functions. Thus both constants always occur.

**3. Pairwise distinctness.** The paperfolding sequence is not eventually periodic. Indeed, suppose its tail had a period \(d\ge1\). Choose \(k\) so large that \(2^k>d\), \(k>\nu_2(d)+1\), and both \(2^k-1\) and \(3\cdot2^k-1\) lie past the eventual-periodicity threshold. The defining formula gives
\[
p(2^k-1)=0,\qquad p(3\cdot2^k-1)=1.
\]
But adding \(d\) to either index makes the number one greater than that index equal to either \(2^k+d\) or \(3\cdot2^k+d\). Both have the same trailing-zero exponent \(\nu_2(d)\) and the same bit immediately above it. Their \(p\)-values are therefore equal, contradicting periodicity. Thus \(p\) is not eventually periodic.

If distinct shifts \(p(z+a)\), \(p(z+b)\) were equal for every \(z\ge0\), then \(p\) would have eventual period \(|a-b|\), a contradiction. No shifted \(p\) can equal a constant or a parity function, because those have period at most two. The two constants and two parity functions are mutually distinct. Consequently the families counted in step 2 are disjoint, except for the already-excluded repeated shifts.

**4. Exact count.** For \(c=0\), the counts are one shifted paperfolding function, one parity function, and two constants, totaling \(4\). For \(c\ge1\), they are \(m+2\) shifted functions, two parity functions, and two constants, totaling \(m+6\). Each arises from an actual finite prefix and all residuals have been classified, which proves both minimality and the stated upper bounds. \(\square\)

## Verification

A standalone Python 3 checker in `verify.py` implements the defining binary-digit formula independently of the symbolic case count. It enumerates residual functions explicitly for shifts \(0\) through \(95\) and selected shifts \(127,128,129,191,192,255\), using at least \(\max(100,4c+20)\) continuation values. It checks the structural count for additional power-of-two boundaries through \(16384\) and directly tests each case of the residual classification for every binary input prefix through eight digits for shifts \(0\) through \(39\). Its recorded output is supplied in `verification_output.txt`. Every check passed. These are finite consistency checks, not a replacement for the all-shifts proof.

## Relationship to prior work

Zantema and Bosma (2022), *Complexity of Automatic Sequences*, Example 3 and the discussion after Theorem 16, give respectively the reversed state complexity \(4\) of the unshifted regular paperfolding word and the reversed state complexity \(6\) of its one-step tail. Their general results provide constructions and bounds for operations on automatic sequences; those two evaluations do not give the exact formula for arbitrary positive shifts.

Moradi, Popoli, Shallit, and Vukusic (first posted March 19, 2026), *State Complexity of Shifts of the Fibonacci Word*, develop the shift-complexity question, including exact or logarithmic behavior in least-significant-first Zeckendorf numeration for the different Fibonacci word. Their theorems do not cover the binary regular paperfolding word. The present result supplies the complete dyadic staircase for this distinct and classical automatic word, with a direct classification of its entire right-to-left residual family.

## Limitations

The result is for regular paperfolding with the explicit indexing convention above and for least-significant-first binary input with redundant high-order zeros allowed. It does not assert the same formula for most-significant-first automata, generalized paperfolding sequences, or other arithmetic subsequences. The mathematical proof establishes an infinite classification; finite software tests provide only corroboration. Priority against unindexed or unpublished equivalent formulas cannot be guaranteed by the cited literature comparison.

## References

1. H. Zantema and W. Bosma, *Complexity of Automatic Sequences*, **Information and Computation** 288 (2022), 104710. https://www.math.ru.nl/~bosma/pubs/Zantema_Bosma_Complexity_of_Automatic_Sequences.pdf
2. D. Moradi, P. Popoli, J. Shallit, and I. Vukusic, *State Complexity of Shifts of the Fibonacci Word*, arXiv:2603.18858, first posted 2026-03-19. https://arxiv.org/abs/2603.18858
3. D. Moradi, N. Rampersad, and J. Shallit, *Complexity of Linear Subsequences of k-Automatic Sequences*, arXiv:2512.10017, first posted 2025-12-10. https://arxiv.org/abs/2512.10017
