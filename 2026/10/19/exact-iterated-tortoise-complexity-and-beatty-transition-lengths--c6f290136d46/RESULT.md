# Exact iterated tortoise complexity and Beatty transition lengths of Sturmian words

## Finding

For an infinite binary Sturmian word \(x\) of irrational frequency \(\alpha\in(0,1)\) of the symbol \(1\), let \(T\) denote the binary tortoise operation: remove the first \(1\) and append it, or fix the word if it contains no \(1\). For every integer \(k\ge2\) and every integer \(n\ge1\), let \(\rho_x^{T^k}(n)\) count distinct images \(T^k(w)\) as \(w\) ranges over all length-\(n\) factors of \(x\). Then

\[\boxed{\rho_x^{T^k}(n)=\max\left\{2,\ n+1-\left\lfloor\frac{k}{\alpha}\right\rfloor\right\}}.\]

The ordinary abelian complexity of a binary Sturmian word is \(2\) at every positive length. Consequently, the exact last length of coincidence is

\[\boxed{\operatorname{abel}_x(k)=\left\lfloor\frac{k}{\alpha}\right\rfloor+1}\qquad(k\ge2).\]

Thus the complete hierarchy of iterated-tortoise image counts and coincidence thresholds depends only on the slope, not on the intercept.

## Assumptions and scope

The alphabet is ordered as \(0<1\). All word lengths \(n\) are positive integers, and the number \(k\) of tortoise passes is any integer at least \(2\), including \(k\ge n\). Sturmian words are characterized here by irrational mechanical codings: their length-\(n\) factor sets coincide with those of

\[w_i(\theta)=\lfloor (i+1)\alpha+\theta\rfloor-\lfloor i\alpha+\theta\rfloor,\quad 0\le i<n,\quad 0\le\theta<1.\]

The phase \(\theta\) may vary; irrationality ensures that exactly \(n+1\) factors occur. The boundary phase values are represented by adjacent half-open intervals; the set of factors is unchanged by the convention at boundaries. The statement concerns **image complexity**, not the number of preimages or the iterate at which an individual word becomes sorted.

## Proof

**1. Finite-word prefix identity.** For an arbitrary binary word \(w\) of length \(n\), define \(P_j\) as the number of \(1\)'s in the first \(j\) letters, \(0\le j\le n\). Let \(Q_m\) be the number of \(1\)'s in the first \(m\) letters of \(T^k(w)\). Successive tortoise passes remove the first available original \(1\)'s and append them; after the last original \(1\) is removed, subsequent passes fix the sorted word. Thus \(T^k(w)\) is obtained by deleting the first \(\min(k,P_n)\) original \(1\)'s and appending that many \(1\)'s. For \(k\le n\), this gives, for all integers \(0\le m\le n\),

\[Q_m=\begin{cases}\max\{P_{m+k}-k,0\},&0\le m\le n-k,\\[2pt]\max\{P_n+m-n,0\},&n-k<m\le n.\end{cases}\tag{1}\]

Indeed, when \(P_n\ge k\), the unsorted prefix of the result has length \(n-k\), and deleting its first \(k\) ones yields the first formula; the suffix consists of \(k\) ones, giving the second. When \(P_n<k\), all the original ones move to a final block, so both formulas hold by inspection. For \(k>n\), the output is sorted and depends only on \(P_n\). We set \(Q_n=P_n\) in every case.

**2. Phase cuts of Sturmian factors.** Take the mechanical factor \(w(\theta)\) from the preceding section, with \(0\le\theta<1\). Its prefix counts satisfy the exact identity

\[P_j(\theta)=\lfloor j\alpha+\theta\rfloor\qquad(0\le j\le n).\tag{2}\]

For \(1\le j\le n\), the coordinate \(P_j\) has its single upward jump as \(\theta\) crosses \(c_j=1-\{j\alpha\}\). All these cut points are distinct because \(\alpha\) is irrational. When \(k\le n\), (1) shows that every output-prefix coordinate is nondecreasing in \(\theta\). For an output coordinate with \(m\le n-k\), the only possible jump occurs at \(c_{m+k}\); it is a strict jump exactly if the higher value of \(P_{m+k}-k\) is positive, equivalently if \(\lfloor(m+k)\alpha\rfloor\ge k\). Since \(\alpha\) is irrational, this is the same as \((m+k)\alpha>k\). For \(m>n-k\), all possible jumps occur at the single cut \(c_n\). The final prefix \(Q_n=P_n\) always jumps at \(c_n\), regardless of \(k\).

It follows that the distinct cut points at which the **whole output** changes are exactly \(c_n\), together with the points \(c_j\) indexed by

\[1\le j\le n-1,\qquad j\alpha>k.\tag{3}\]

The apparent lower restriction \(j\ge k+1\) is automatic from \(j\alpha>k\) because \(\alpha<1\). Every active cut changes at least one coordinate, and no output coordinate can decrease as \(\theta\) rises; consequently, there are no repeated image values on distinct intervening phase intervals.

**3. Counting cuts.** For \(k\le n\), the number of integer indices satisfying (3) is

\[\max\{0,n-1-\lfloor k/\alpha\rfloor\}.\]

Adding the always-active \(c_n\) and the initial phase interval yields

\[\rho_x^{T^k}(n)=2+\max\{0,n-1-\lfloor k/\alpha\rfloor\}=\max\{2,n+1-\lfloor k/\alpha\rfloor\}.\]

For \(k>n\), every length-\(n\) word becomes sorted. Sturmian balance and aperiodicity give exactly two possible letter counts, hence exactly two images. The displayed formula also equals \(2\), because \(k/\alpha>k>n\). This includes all boundary cases \(n=1\) and \(k=n\).

**4. Coincidence length.** A binary Sturmian word has exactly two Abelian factor classes at every positive length. The formula equals \(2\) precisely when \(n\le\lfloor k/\alpha\rfloor+1\), and exceeds \(2\) at the next integer length. Hence the claimed sharp abelian-coincidence statistic follows. \(\square\)

## Verification

The self-contained standard-library program `checker.py` checks identity (1) for every binary word of lengths \(1\) through \(11\), for powers from \(2\) to \(n+2\), checking every prefix length. It separately constructs the full phase-cell factor sets for seven explicitly specified irrational slopes at lengths \(1\) through \(68\), and verifies the theorem across \(5040\) slope–length–power instances. The generated text output is in `checks.txt`. Finite tests corroborate, but do not replace, the unrestricted proof given above. Running `python checker.py` reproduces the finite checks without third-party dependencies.

## Relationship to prior work

Campbell and Rampersad introduced \(k\)-tortoise factor complexity and the statistic \(\operatorname{abel}_x(k)\) in *Subword enumeration up to stack-sorting equivalence* (arXiv:2604.25811, first posted April 28, 2026), particularly Definitions 1–2 and the conclusion's question about Sturmian generalizations. Their investigated infinite words are paperfolding and Thue–Morse; no all-slope, all-iterate Sturmian expression was located in the examined full text. Defant and Kravitz introduced the underlying finite-word operators. An earlier one-pass Sturmian result gives the special case \(k=1\); the newly asserted domain here is strictly \(k\ge2\) and supplies the entire Beatty-parameter hierarchy of sharp coincidence thresholds. General facts about Sturmian mechanical codings and Abelian balance are classical.

## Limitations

This theorem applies to binary Sturmian words with irrational slope, not arbitrary balanced words, periodic mechanical codings, alphabets of larger size, or the hare operation. It counts distinct images and does not determine their multiplicities. It does not establish publication priority: equivalent statements under different terminology could exist beyond the literature searched. The verification program samples finite lengths and slopes only; the proof handles all allowed parameters. Independent validation has not been performed.

## References

- J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811 (first public version April 28, 2026), https://arxiv.org/abs/2604.25811 .
- C. Defant and N. Kravitz, *Stack-sorting for words*, Australasian Journal of Combinatorics 77 (2020), 51–68, preprint https://arxiv.org/abs/1809.09158 .
- G. A. Hedlund and M. Morse, *Symbolic dynamics II: Sturmian trajectories*, American Journal of Mathematics 62 (1940), 1–42.
