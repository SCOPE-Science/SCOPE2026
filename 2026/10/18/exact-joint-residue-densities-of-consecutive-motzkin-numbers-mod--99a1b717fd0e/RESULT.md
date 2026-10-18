# Exact joint residue densities of consecutive Motzkin numbers modulo eight

## Finding

Let \(M_0=M_1=1\), and for every integer \(n\ge2\) let
\[
(n+2)M_n=(2n+1)M_{n-1}+3(n-1)M_{n-2}.
\]
These are the Motzkin numbers. For all \(a,b\in\{0,1,\ldots,7\}\), the natural density
\[
\mu(a,b)=\lim_{N\to\infty}\frac1N\#\{0\le n<N:(M_n,M_{n+1})\equiv(a,b)\pmod8\}
\]
exists. The complete matrix \(192\mu(a,b)\), with rows indexed by \(a=0,\ldots,7\) and columns by \(b=0,\ldots,7\), is

| \(a\backslash b\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 10 | 3 | 2 | 4 | 10 | 1 | 2 |
| 2 | 0 | 3 | 0 | 1 | 8 | 3 | 0 | 1 |
| 3 | 0 | 2 | 1 | 10 | 4 | 2 | 3 | 10 |
| 4 | 0 | 4 | 8 | 4 | 0 | 4 | 8 | 4 |
| 5 | 0 | 10 | 3 | 2 | 4 | 10 | 1 | 2 |
| 6 | 0 | 1 | 0 | 3 | 8 | 1 | 0 | 3 |
| 7 | 0 | 2 | 1 | 10 | 4 | 2 | 3 | 10 |

Exactly 44 ordered residue pairs have positive natural density and occur infinitely often. Moreover, no pair containing residue \(0\), and none of the five pairs \((2,2),(2,6),(4,4),(6,2),(6,6)\), occurs at any index. The single-coordinate marginal densities are \(0\) for residue \(0\), \(1/12\) for residues \(2,6\), and \(1/6\) for residues \(1,3,4,5,7\). In particular, adjacent residues are not independent: \(\mu(4,4)=0\) although both marginals at \(4\) equal \(1/6\).

## Assumptions and scope

All index quantifiers concern nonnegative integers; residue arithmetic is modulo \(8\). The density concerns the ordinary initial intervals \([0,N)\), not solely lengths \(2^j\). The pointwise congruence characterization used below is Theorem 11 of Krattenthaler and Müller [2]; it is earlier published mathematical input and not claimed here as a new theorem. The evaluated two-coordinate density matrix and its positive-density support are the present finding.

For binary digits \(\epsilon_i(n)\in\{0,1\}\), define
\[
s(n)=\sum_{i\ge0}\epsilon_i(n),\qquad e(n)=\sum_{i\ge0}\epsilon_i(n)\epsilon_{i+1}(n),\qquad c(n)=\epsilon_4(n).
\]
For \(n\equiv14,15\pmod{16}\), set \(K(n)=\min\{j\ge4:\epsilon_j(n)=0\}\) and \(q(n)=\epsilon_{K(n)+1}(n)\). This is defined for every finite integer \(n\).

## Proof

**1. Pointwise modular input.** Put \(t=n\bmod16\), \(s=s(n)\), \(e=e(n)\), \(c=c(n)\). Theorem 11 of [2], written as a residue evaluator \(R(n;s,e)\), gives the following expressions modulo \(8\):
\[
\begin{array}{c|l}
t& R(n;s,e)\\\hline
0,8&2s^2+4e+1\\
1,9&6s^2+4e+3\\
2&4s+6\\
3,10&4\\
4,12&6s^2+4e+3\\
5,13&2s^2+4e+5\\
6&6s^2+4cs+4e+2c+7\\
7&2s^2+4cs+4e+2c+5\\
11&4s+2
\end{array}
\]
For \(t=14\), with \(K=K(n)\) and \(q=q(n)\), the expression is \((q+1)(4s+6)\) if \(K\) is even and \(2q+4qs+2s^2+4s+4e+7\) if \(K\) is odd. For \(t=15\), it is \(6q+4qs+4\) if \(K\) is even and \(2q+4qs+2s^2+4e+5\) if \(K\) is odd. All these expressions depend on \(s\bmod4\) and \(e\bmod2\) only. The packaged verifier implements precisely this evaluator, including the exceptional branches, and checks it independently against 4096 exact recurrence terms.

**2. Uniform high-digit statistics.** Fix any finite string of low binary digits, ending in a specified bit \(b\). Append independent fair higher bits, one at a time. If \(u\) records the number of appended ones modulo \(4\), \(v\) records new adjacent-\(11\) pairs modulo \(2\) (including the pair crossing the fixed boundary), and \(b\) is the last seen bit, the state transition for an appended bit \(x\) is
\[
(u,v,b)\longmapsto (u+x\bmod4,\ v+bx\bmod2,\ x).
\]
There are exactly 16 states. Every state has two incoming labeled edges, so the uniform distribution is stationary. The chain is irreducible: starting with last bit \(0\), the words \(10\) and \(110\) return to last bit \(0\) while adding respectively \((1,0)\) and \((2,1)\) to \((u,v)\), and these additions generate \(\mathbb Z/4\mathbb Z\times\mathbb Z/2\mathbb Z\). A zero appended after a last zero is a self-loop. Thus the chain is aperiodic and its distribution converges, for any fixed starting bit, to uniform on all 16 states. In particular, \((u,v)\) becomes uniform on the eight pairs, independently of the final bit.

**3. Exhaustive low-prefix partition.** For \(r\in\{0,\ldots,12\}\), fix the low-five-bit word \(w=r+16c\), \(c\in\{0,1\}\). Each word has asymptotic frequency \(2^{-5}\). Neither \(w\) nor \(w+1\) needs an exceptional \(K\) branch, and their bit at position 4 is identical. Their more significant binary digits are therefore identical, and the common added \((u,v)\) in Step 2 can be used in both evaluator arguments.

For \(r\in\{13,14,15\}\), let \(k\ge4\) be the first zero-bit position at or above position 4, and fix the next bit \(q\in\{0,1\}\). The distinguishing prefix is
\[
w_{r,k,q}=r+\sum_{j=4}^{k-1}2^j+q2^{k+1},\qquad L=k+2.
\]
Its frequency is \(2^{-L}\). The addition of one is already resolved within these \(L\) digits, so \(w_{r,k,q}\) and \(w_{r,k,q}+1\) share all digits from position \(L-1\) upwards; their high digit statistics consequently have the same additive increment \((u,v)\). All needed exceptional bits \(K\) and \(q\) are known from this prefix. This partitions the integer indices exhaustively. From the formulas in Step 1, increasing \(k\) by four changes the prefix values of \(s\) and \(e\) by multiples of four while preserving the relevant low bits, \(K\)-parity and \(q\). Therefore both residue outputs, for every \((u,v)\), depend on \(k\) only through \(k\bmod4\). Direct modular verification of this finite identity is also supplied in `verification.py`.

**4. Exact rational evaluation.** Write \(\widehat R(w;u,v)\) for Step 1 evaluated on the finite prefix \(w\), replacing \(s(w)\) with \(s(w)+u\) and \(e(w)\) with \(e(w)+v\). Let \(\mathbf1[P]\) equal 1 when proposition \(P\) holds, and 0 otherwise. The exact density is
\[
\begin{aligned}
\mu(a,b)={}&\frac1{256}\sum_{r=0}^{12}\sum_{c=0}^1\sum_{u=0}^3\sum_{v=0}^1
\mathbf1[\widehat R(r+16c;u,v)=a,\ \widehat R(r+16c+1;u,v)=b]\\
&+\sum_{r=13}^{15}\sum_{k=4}^{7}\sum_{q=0}^1\frac{2}{15\cdot2^{k+2}}
\sum_{u=0}^3\sum_{v=0}^1
\mathbf1[\widehat R(w_{r,k,q};u,v)=a,\ \widehat R(w_{r,k,q}+1;u,v)=b].
\end{aligned}
\]
The coefficient in the second line is \(\frac18\sum_{j\ge0}2^{-(k+4j+2)}=2/(15\cdot2^{k+2})\); thus it accounts for the complete infinite geometric tail, not a truncation. Evaluating the 26 ordinary prefixes and 24 exceptional representative prefixes with eight values of \((u,v)\) gives the displayed matrix. The exact-arithmetic verifier checks every matrix entry, the total mass, the marginals and the 44 positive entries. Every zero entry is absent for all finite prefixes in the exhaustive classification and hence is impossible, not merely density zero.

**5. Full natural density.** Steps 2–4 give the asserted limits first on dyadic intervals with sufficiently many free higher bits. The convergence is uniform in the fixed more-significant digits: the 16-state chain mixes from either boundary bit, and the share of indices with unresolved exceptional \(K\ge m\) is at most \(3\cdot2^{-m}\) times an absolute constant. Hence the same density law holds uniformly in every aligned interval of length \(2^m\), as \(m\to\infty\). Every initial interval \([0,N)\) is a disjoint union of aligned dyadic intervals, at most one of each length. For a fixed cutoff \(m_0\), all blocks of length at least \(2^{m_0}\) obey the same arbitrarily small relative error once \(m_0\) is large, while the total length of smaller blocks is less than \(2^{m_0}\). First take \(N\to\infty\), then \(m_0\to\infty\). This proves the ordinary natural-density assertion.

## Verification

Run `python3 verification.py` with Python 3 (standard library only). The program executes exact rational arithmetic on the 50 representative prefixes, checks periodic reduction \(k\mapsto k+4\) for all branch parameters and all eight tail statistics, establishes strong connectivity, aperiodicity and uniform stationarity of the 16-state chain, and compares the pointwise formulas with 4096 Motzkin numbers computed from the exact recurrence. Its successful completion prints `VERIFY_OK`. These finite checks corroborate, but do not replace, the general arguments in Steps 2, 3 and 5.

## Relationship to prior work

Rowland and Yassawi [1, Section 3.2] give a 28-state automaton for Motzkin residues modulo 8 and in Section 3.3 calculate one-coordinate densities modulo 2 and 4. Krattenthaler and Müller [2, Theorem 11] establish the explicit pointwise modulo-8 formulas used above. Wang and Xin [3, Theorem 3] independently classify pointwise residues. These supply important antecedents; the specific two-coordinate probability matrix, its 44 positive transitions, and its five additional forbidden ordered pairs were not stated in the inspected primary sources. In particular, the general ability to compute an automaton does not itself evaluate these joint limiting frequencies without a further invariant-measure calculation.

## Limitations

The proof is for neighboring terms and modulus 8 only. It gives no effective discrepancy exponent, rates of convergence or longer-block densities. It uses published pointwise congruences as input rather than reproving their entire derivation. A covering theorem or computed transition table in unindexed literature could affect originality; independent checking remains appropriate.

## References

[1] E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635 (first posted October 31, 2013), especially Sections 3.2–3.3. https://arxiv.org/abs/1310.8635

[2] C. Krattenthaler and T. W. Müller, *Motzkin numbers and related sequences modulo powers of 2*, arXiv:1608.05657 (first posted August 19, 2016), especially Theorem 11 and Corollaries 12–13. https://arxiv.org/abs/1608.05657

[3] Y. Wang and G. Xin, *A classification of Motzkin numbers modulo 8*, Electronic Journal of Combinatorics 25(1) (2018), P1.54, especially Theorem 3. https://doi.org/10.37236/7092
