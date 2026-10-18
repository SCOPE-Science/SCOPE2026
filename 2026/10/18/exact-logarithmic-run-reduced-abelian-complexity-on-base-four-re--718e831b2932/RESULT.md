# Exact logarithmic run-reduced Abelian complexity on base-four repunit lengths

## Finding
Let \(p=p_0p_1\cdots\) be the period-doubling word, the fixed point beginning with \(0\) of the substitution \(0\mapsto01\), \(1\mapsto00\). For every nonempty factor \(u\), let \(\operatorname{red}(u)\) replace every maximal constant-letter run by one letter. Let \(R_p(n)\) be the number of distinct Parikh vectors of \(\operatorname{red}(u)\), as \(u\) ranges over all contiguous factors of \(p\) of length \(n\).

For each integer \(t\ge1\), put
\[
m_t=\frac{4^t-1}{3},\qquad a_t=\frac{2m_t-2t}{3},\qquad b_t=\frac{2m_t+t}{3}=a_t+t.
\]
These quantities are integers. The **complete reduced-Abelian spectrum** at length \(2m_t\) is
\[
\big\{(z+1,z):a_t\le z<b_t\big\}\ \cup\
\big\{(z,z):a_t<z\le b_t\big\},
\]
where the first coordinate counts zeros and the second counts ones. In particular,
\[
\boxed{R_p\bigl(2(4^t-1)/3\bigr)=2t\quad(t\ge1).}
\]
Moreover \(R_p(n)=O(\log(n+1))\), and therefore
\[
\boxed{\max_{1\le n\le N}R_p(n)=\Theta(\log(N+1))}\qquad(N\longrightarrow\infty).
\]
This exhibits exact logarithmic growth along an explicit sequence despite bounded complexity at many other lengths.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); factors are contiguous, indexed from zero, and their run reduction is computed *separately for each factor*, rather than reducing the whole infinite word. Two factors are equivalent when their reduced words have the same number of zeros and of ones, independent of their original lengths (here all original factor lengths equal \(n\)). The empty factor is excluded. The exact spectrum statement covers every positive integer \(t\), not merely sampled lengths. No claim of a closed formula for \(R_p(n)\) at arbitrary \(n\) is made.

## Proof
**1. A digit-sum expression for factor counts.** Write \(Z(j)\) for the number of zeros in \(p_0\cdots p_{j-1}\), with \(Z(0)=0\). The substitution implies
\[
p_{2i}=0,\qquad p_{2i+1}=1-p_i.
\]
Counting zeros in paired letters gives
\[
Z(2j)=2j-Z(j),\qquad Z(2j+1)=2j+1-Z(j),
\]
or \(Z(j)=j-Z(\lfloor j/2\rfloor)\). Write \(j=\sum_{r\ge0}\epsilon_r2^r\) and define the alternating binary digit sum
\[
\tau(j)=\sum_{r\ge0}(-1)^r\epsilon_r.
\]
Both \(3Z(j)-2j\) and \(\tau(j)\) satisfy the recurrence \(f(j)=(j\bmod2)-f(\lfloor j/2\rfloor)\), with value zero at \(j=0\). Consequently
\[
Z(j)=\frac{2j+\tau(j)}3,\qquad
z_i(m):=\#\{0\text{s in }p_i\cdots p_{i+m-1}\}
=\frac{2m+\tau(i+m)-\tau(i)}3.
\]

**2. A sharp carry bound.** Express integers in base four. For a base-four digit \(d\in\{0,1,2,3\}\), its contribution to \(\tau\) is
\[
w(0)=0,\quad w(1)=1,\quad w(2)=-1,\quad w(3)=0.
\]
Adding \(m_t=1+4+\cdots+4^{t-1}\) adds one to each of the first \(t\) base-four digits, with carries. If the incoming carry is zero, a digit \(d=0,1,2,3\) changes its contribution by \(+1,-2,+1,0\), respectively; only \(d=3\) generates a carry. If the incoming carry is one, those changes are \(-1,-1,+1,+1\), respectively; a carry persists exactly for \(d=2,3\). After digit \(t-1\), a remaining carry increments the higher base-four integer by one. Its contribution to \(\tau\) is either \(-2\) or \(+1\): trailing threes contribute zero change, and the first non-three digit changes by one of these amounts.

If there is no carry after digit \(t-1\), the total change lies in \([-2t,t]\). If a carry remains, let \(h<t\) be the first digit that generates one. Its change is zero instead of the possible \(-2\) or \(+1\); the other \(t-1\) digit changes lie in \([-2,1]\), and the higher tail contributes between \(-2\) and \(+1\). The same bound follows. Thus for every \(i\ge0\),
\[
-2t\le\tau(i+m_t)-\tau(i)\le t.\tag{1}
\]
The upper bound is attained by \(i=0\), since \(\tau(m_t)=t\). The lower bound is attained by \(i=m_t\), since \(\tau(2m_t)=-t\). Formula (1) and the prefix identity show that the smallest and largest zero counts of length-\(m_t\) factors are exactly \(a_t\) and \(b_t\).

The equality cases additionally force **the first symbol** of any minimal-zero factor to be \(1\), and of any maximal-zero factor to be \(0\). Here are the carry details. For equality at the lower bound with no carry, all first \(t\) digits of \(i\) are \(1\), so \(i\equiv1\pmod4\). If there is a carry, equality requires it to be created at digit \(t-1\), with preceding digits all \(1\), and the higher tail change equal to \(-2\). Indeed, if a carry were created earlier, the next digit with incoming carry could not contribute \(-2\). For \(t>1\) this again gives \(i\equiv1\pmod4\). For \(t=1\), the equality-with-carry case says that the base-four expansion of \(i\) starts with one or more digits \(3\), followed by a digit \(1\); hence \(\nu_2(i+1)\) is odd. In every lower-equality case \(\nu_2(i+1)\) is odd. For equality at the upper bound without carry, the first base-four digit is \(0\) or \(2\), making \(i\) even. With a carry first created at digit \(h>0\), the same is true for its first digit. With a carry created at digit \(0\), equality requires every following affected digit to retain the carry and contribute \(+1\), and the final higher tail to contribute \(+1\). Thus the base-four expansion of \(i\) begins with one or more digits \(3\), followed by a \(0\) or \(2\), so \(\nu_2(i+1)\) is even. Finally, the fixed point satisfies \(p_i=\nu_2(i+1)\bmod2\). This proves the claimed restrictions on first symbols.

**3. Every intermediate zero count occurs with both first symbols.** Sliding a length-\(m_t\) factor one position changes its zero count by \(p_i-p_{i+m_t}\in\{-1,0,1\}\). The substitution is primitive: both images under its square contain both alphabet symbols. Therefore every factor appears with bounded gaps in \(p\); in particular, factors attaining the minimum and maximum counts occur infinitely often. Passing from an occurrence of the minimum to an occurrence of the maximum forces, for every \(a_t<z<b_t\), an upward step from zero count \(z\) to \(z+1\). Such a step has outgoing bit \(p_i=1\), giving a factor of zero count \(z\) starting in \(1\). Passing back down similarly forces a downward step from \(z\) to \(z-1\); its outgoing bit is \(p_i=0\). Hence both first symbols occur for every strictly intermediate zero count. The two equality restrictions proved above give only initial \(1\) at \(a_t\), and only initial \(0\) at \(b_t\).

**4. Transfer to run-reduced Parikh vectors.** For any \(m\ge1\), a length-\(2m\) factor beginning at odd index \(2i+1\) is
\[
(1-p_i)\,0\,(1-p_{i+1})\,0\cdots(1-p_{i+m-1})\,0.
\]
Write \(z=z_i(m)\). Because its ones are isolated, its run-reduced Parikh vector is \((z,z)\) if \(p_i=0\), and \((z+1,z)\) if \(p_i=1\).

A factor starting at even index \(2i\) has the form
\[
0\,(1-p_i)\,0\,(1-p_{i+1})\cdots0\,(1-p_{i+m-1}),
\]
and yields the same two possibilities, now determined by the *last* letter of the length-\(m\) factor of \(p\). No extra types arise: the language of \(p\) is closed under reversal. For completeness, put \(u_k=\mu^k(0)\) and \(v_k=\mu^k(1)\), where \(\mu(0)=01\) and \(\mu(1)=00\). An induction gives \(u_k=h_kb_k\), \(v_k=h_k(1-b_k)\) with \(h_k\) a palindrome: if true at \(k\), then \(h_{k+1}=h_kb_kh_k\) is a palindrome. The palindromic prefixes \(h_k\) tend to infinite length and contain every factor of \(p\), so the reversal of every factor also occurs. Thus a factor ending in a prescribed bit has a reversed factor starting in that bit, without changing its zero count.

Apply Step 3 with \(m=m_t\). At \(z=a_t\), only \((z+1,z)\) occurs; at \(z=b_t\), only \((z,z)\) occurs; and both types occur for each of the \(t-1\) intermediate counts. They are pairwise distinct because their second coordinate is \(z\). The total is \(1+2(t-1)+1=2t\), proving the exact spectrum.

**5. A global logarithmic upper bound.** For any positive integer \(m\), let \(L\) be its number of base-four digits. When adding \(m\) to any \(i\), each of the first \(L\) digit contributions to \(\tau\) changes by at most two in absolute value, and a possible carry into the higher digits changes the remainder by at most two. Hence \(|\tau(i+m)-\tau(i)|\le2L+2\), uniformly in \(i\). The prefix identity gives only \(O(\log(m+1))\) possible zero counts for length-\(m\) factors. For even \(n=2m\), Step 4 gives at most two run-reduced Parikh vectors per zero count. For odd \(n=2m+1\), a factor beginning at an even index uses \(m\) inner odd-position letters and has Parikh vector \((z+1,z)\) for a length-\(m\) factor of \(p\); one beginning at an odd index uses \(m+1\) odd-position letters and has vector \((z+1-e,z)\), where \(e\in\{0,1,2\}\) is the number of endpoint zeros of that length-\(m+1\) factor of \(p\). These give \(O(\log(n+1))\) possibilities in total. Since \(2m_t\) is of order \(4^t\) and \(R_p(2m_t)=2t\), the maximal profile up to \(N\) is also bounded below by a constant multiple of \(\log(N+1)\). This proves the second boxed assertion.

## Verification
The accompanying `check.py` constructs the period-doubling fixed point both by substitution and by the independent \(2\)-adic valuation formula. It compares the predicted complete spectra to sliding-transition counts for every starting position in a prefix of length \(2^{17}\) at \(t=1,\ldots,7\), independently recomputes literal run reductions for 2,000 starting positions at each tested length, and compares the predicted zero-count ranges to an independent digit-sum calculation. All seven tests passed with measured class counts \(2,4,6,8,10,12,14\). These finite computations are corroboration only; Steps 1–5 prove the claims for all quantified parameters.

Reproduction: run `python3 check.py` with Python 3 and inspect `check_output.txt`. No third-party packages or external data are required.

## Relationship to prior work
Campbell, Currie and Rampersad introduced run-reduced factor and Abelian complexities and evaluated the paperfolding case; their 2025 preprint / 2026 journal article does not analyze the period-doubling reduced-Abelian profile. Parreau, Rigo, Rowland and Vandomme (2015) prove regularity and recurrences for the different, finer \(2\)-Abelian complexity of the period-doubling word and the Abelian complexity of its overlapping two-block coding; their Theorem 21 does not provide the present run-reduced spectrum. Machacek (2025) relates a group-action factor complexity of the ternary square-free word to ordinary Abelian complexity of period doubling, not run reduction. The present theorem concerns factorwise run collapse, an explicit geometric progression of source lengths, and full class content rather than just regularity. No priority claim is made for the underlying digit-sum identity or for standard substitution properties.

## Limitations
No exact formula for all values of \(R_p(n)\) is established. The upper bound concerns logarithmic order, not a sharp global leading constant. Priority comparisons cannot exclude every unindexed source or a rephrased consequence of known automatic-sequence recurrences; these remain residual risks. The presented proof is a mathematical argument with finite numerical corroboration, not an independent external validation.

## References
1. J. M. Campbell, J. D. Currie and N. Rampersad, *Reduced complexities for sequences over finite alphabets*, arXiv:2509.16034 (first posted 2025-09-19); *INTEGERS* 26 (2026), A34, https://math.colgate.edu/~integers/aa34/aa34.pdf .
2. A. Parreau, M. Rigo, E. Rowland and É. Vandomme, *A new approach to the 2-regularity of the ℓ-Abelian complexity of 2-automatic sequences*, *Electron. J. Combin.* 22 (2015), P1.27, arXiv:1405.3532, https://ericrowland.github.io/papers/A_new_approach_to_the_2-regularity_of_the_l-abelian_complexity_of_2-automatic_sequences.pdf .
3. J. Machacek, *Group Actions and Some Combinatorics on Words with vtm*, arXiv:2509.26613 (first posted 2025-09-30), https://arxiv.org/pdf/2509.26613 .
