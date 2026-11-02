# Exact smallest \(2\)- and \(3\)-attractor spectra for finite Thue–Morse words

## Finding

Let \(t_0=0\) and \(t_{n+1}=\mu(t_n)\), with \(\mu(0)=01\) and \(\mu(1)=10\). Write \(N=2^n\). A \(k\)-attractor of a finite word is a set of positions such that every distinct nonempty contiguous factor of length at most \(k\) has an occurrence containing a selected position. Let \(A_k(n)\) be the number of minimum-cardinality \(k\)-attractors of \(t_n\).

**Theorem (two local-attractor levels).** For every \(n\ge3\), the smallest \(2\)-attractors of \(t_n\) have two positions, and
\[
A_2(n)=\begin{cases}
\dfrac{(N-4)(N+2)}{18},&n\ \text{even},\\
\dfrac{(N-2)^2}{18},&n\ \text{odd}.
\end{cases}
\]
For every \(n\ge4\), the smallest \(3\)-attractors also have two positions, and
\[
A_3(n)=\begin{cases}
\dfrac{(N-4)^2}{72},&n\ \text{even},\\
\dfrac{(N+4)(N-8)}{72},&n\ \text{odd}.
\end{cases}
\]
All optimal position sets have an explicit local classification. Using **zero-based** indices and writing the factor centered at \(i\) of radius \(r\) as \(t_n[i-r\ldots i+r]\):

* A pair \(\{i,j\}\) is a minimum \(2\)-attractor precisely when the two centered length-three factors are \(\{001,110\}\) or \(\{100,011\}\), in either order.
* A pair \(\{i,j\}\) is a minimum \(3\)-attractor precisely when the two centered length-five factors are \(\{01001,10110\}\) or \(\{01101,10010\}\), in either order.

The centered factors are required to exist within the word, so no endpoint convention is implicit. Consequently \(A_3(n)/A_2(n)\to1/4\), while both counts are quadratic in \(N\). This differs from the established constant number \(32\) of smallest *unrestricted* attractors for \(n\ge6\) [1,2].

## Assumptions and scope

The alphabet is labeled \(\{0,1\}\), occurrences are contiguous and may overlap, and \(k\)-attractors must cover **all lengths from one through \(k\)**, not only factors of length exactly \(k\). Attractor sets are unordered sets of distinct positions. The theorem concerns \(2\)-attractors at orders \(n\ge3\) and \(3\)-attractors at orders \(n\ge4\); it makes no claim about earlier orders. The quantity \(A_k(n)\) counts sets, not choices of representative factor occurrences.

## Proof

**Step 1: exact local factor sets.** The word \(t_3=01101001\) contains the four binary factors of length two and all six nonconstant binary factors of length three. The Thue–Morse morphism sends every letter to two distinct letters, so it never produces \(000\) or \(111\) as factors, and its nested prefixes preserve all factors present in \(t_3\). Hence the length-three factor set is exactly
\[
\mathcal F_3=\{001,010,011,100,101,110\}\quad(n\ge3).
\]
Every length-five occurrence in \(\mu(w)\) begins at an even or odd index and is determined by a length-three factor of \(w\). At an even index the length-five output from \(xyz\) is \(\mu(x)\mu(y)\mu(z)[0]\); at an odd index it is \(\mu(x)[1]\mu(y)\mu(z)\). Applying these two rules to the six factors of \(\mathcal F_3\) gives exactly
\[
\mathcal F_5=\{00101,00110,01001,01011,01100,01101,
10010,10011,10100,10110,11001,11010\}.
\]
Each occurs already in \(t_4\); no other length-five factor occurs for \(n\ge4\).

**Step 2: characterize optimal \(2\)-attractors.** One selected position cannot attract both single-letter factors. Any pair covering all four length-two factors must place both positions in the interior, since a boundary position meets at most one length-two occurrence, whereas an interior position meets at most two. The center of a length-three factor \(abc\) covers the letter \(b\) and adjacent pairs \(ab,bc\). Of the six possibilities in \(\mathcal F_3\), the only unordered context pairs whose union covers all four length-two factors are \(\{001,110\}\) and \(\{100,011\}\). Their center letters are \(0\) and \(1\), so both letter factors are covered too. Thus the stated classification is necessary and sufficient.

**Step 3: characterize optimal \(3\)-attractors.** There are six distinct length-three factors. A selected position crosses at most three occurrences of length three, hence a pair covering all six must consist of two interior positions that each cross exactly three distinct length-three factors. Each such position has a complete centered length-five factor. For \(s=s_0s_1s_2s_3s_4\), the factors of lengths one, two and three met by its center are
\[
\{s_2\},\qquad\{s_1s_2,s_2s_3\},\qquad
\{s_0s_1s_2,s_1s_2s_3,s_2s_3s_4\}.
\]
A complete check of the **twelve explicitly listed** elements of \(\mathcal F_5\) finds eight unordered context pairs whose three length-three factors are complementary:
\[
\begin{gathered}
\{00101,01100\},\ \{00110,10100\},\ \{01001,01101\},\ \{01001,10110\},\\
\{01011,11001\},\ \{01101,10010\},\ \{10010,10110\},\ \{10011,11010\}.
\end{gathered}
\]
Of these eight, four fail to cover both single-letter factors (their centers have the same symbol); another two fail to cover all four length-two factors. Exactly \(\{01001,10110\}\) and \(\{01101,10010\}\) survive. In both, all length-one, -two and -three factors are covered. Both context pairs occur in every \(t_n\), \(n\ge4\), by the factor-set result. Thus the optimum is two positions and the classification is complete.

**Step 4: count local contexts.** Let \(p_n(ab)\) be the number of occurrences of the pair \(ab\) in \(t_n\). For \(n\ge1\), \(t_n\) contains \(2^{n-1}\) of each letter. Every adjacent pair of \(t_{n+1}=\mu(t_n)\) is either internal to a two-letter image or crosses between images, so
\[
\begin{aligned}
p_{n+1}(00)&=p_n(10),&p_{n+1}(11)&=p_n(01),\\
p_{n+1}(01)&=2^{n-1}+p_n(11),&
p_{n+1}(10)&=2^{n-1}+p_n(00).
\end{aligned}
\]
Starting at \(t_2=0110\), induction gives
\[
\begin{array}{c|cccc}
& p_n(00)&p_n(01)&p_n(10)&p_n(11)\\\hline
n\text{ even}&(N-4)/6&(N-1)/3&(N-1)/3&(N+2)/6\\
n\text{ odd}&(N-2)/6&(N+1)/3&(N-2)/3&(N-2)/6.
\end{array}
\]
Here the odd line is used for \(n\ge3\). An occurrence of \(001\) (respectively \(100\)) in \(t_n\) arises exactly once from a pair \(10\) of \(t_{n-1}\); similarly \(011\) and \(110\) each arise from a pair \(01\). Denote their counts by \(a_n\) for each of \(001,100\) and \(b_n\) for each of \(011,110\). The preceding table implies
\[
(a_n,b_n)=\begin{cases}
((N-4)/6,(N+2)/6),&n\text{ even},\\
((N-2)/6,(N-2)/6),&n\text{ odd}.
\end{cases}
\]
The two context-pair types from Step 2 are disjoint, so their total count is \(A_2(n)=2a_nb_n\), yielding the first formula.

For length five, direct even/odd image inspection gives
\[
\begin{split}
\#_{t_n}(01001)=\#_{t_{n-1}}(110),&\quad \#_{t_n}(01101)=\#_{t_{n-1}}(011),\\
\#_{t_n}(10110)=\#_{t_{n-1}}(001),&\quad \#_{t_n}(10010)=\#_{t_{n-1}}(100).
\end{split}
\]
Thus the first two five-letter factors each occur \(u_n\) times, and the last two each \(v_n\) times, where
\[
(u_n,v_n)=\begin{cases}
((N-4)/12,(N-4)/12),&n\text{ even},\\
((N+4)/12,(N-8)/12),&n\text{ odd}.
\end{cases}
\]
Step 3 yields the disjoint product count \(A_3(n)=2u_nv_n\). Substituting proves the second formula. Every transformation used is exact; no limiting or finite-enumeration hypothesis enters the proof. \(\square\)

## Verification

The standalone `verify.py` builds a global coverage mask for every factor of length at most \(k\), enumerates all two-position sets, and independently enumerates position pairs from the local context description. The two sets agree for \(k=2\), \(3\le n\le10\), and for \(k=3\), \(4\le n\le10\). It checks both closed counts and absence of singleton attractors, verifies the twelve-factor table, and compares relevant five-factor occurrence counts through \(n=14\). The exact output is in `verification_output.txt`. The finite experiments corroborate the all-order morphic induction; they do not themselves establish an infinite theorem.

## Relationship to prior work

Banbara et al. [1] and Faro, Marino and Pavone [2] classify unrestricted minimum-size attractors of finite Thue–Morse words, which have four positions and, from order six, exactly 32 possibilities. Their exact four-position results and MUS coverage characterization do not imply a classification of smaller **length-limited** attractors, which are not required to cover long factors. The older literature establishes general \(k\)-attractor definitions and hardness of optimization [3] but does not, in the material checked, supply this two-level all-order local classification. Factor frequencies of the Thue–Morse word are standard; the claimed contribution is their combination with the exact minimal \(k\)-attractor context-pair classification and both cardinality laws.

## Limitations

The theorem is restricted to the canonical finite Thue–Morse iterates, \(k=2\) and \(k=3\), with the specified order ranges. It does not classify minimum \(k\)-attractors for \(k\ge4\), arbitrary factors of the infinite Thue–Morse word, or arbitrary morphic families. The potential existence of earlier equivalent unindexed or inaccessible results has not been completely eliminated. Independent specialist verification has not been performed.

## References

[1] M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno and Y. Okamoto, *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words*, arXiv:2602.16152, first public February 18, 2026, https://arxiv.org/abs/2602.16152 .

[2] S. Faro, F. P. Marino and A. Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words*, arXiv:2610.10950, first public October 7, 2026, https://arxiv.org/abs/2610.10950 .

[3] J. Fuchs and P. Whittington, *The 2-Attractor Problem Is NP-Complete*, arXiv:2304.06523, first public April 13, 2023, https://arxiv.org/abs/2304.06523 .
