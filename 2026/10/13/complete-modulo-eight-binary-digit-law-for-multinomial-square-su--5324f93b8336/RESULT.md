# Complete modulo-eight binary-digit law for multinomial-square sums
## Finding
For positive integers \(\ell\), nonnegative integers \(n\), and even integers \(h\ge2\), define Sun's multinomial-power sum
\[
S_{\ell}^{(h)}(n)=\sum_{\substack{k_1,\ldots,k_\ell\ge0\\k_1+\cdots+k_\ell=n}}
\binom{n}{k_1,\ldots,k_\ell}^{h}.
\]
Write \(n=\sum_{i\ge0}b_i2^i\) with \(b_i\in\{0,1\}\), and put \(s=s_2(n)=\sum_i b_i\). The complete coefficientwise congruence for height two is
\[
\boxed{S_{\ell}^{(2)}(n)\equiv\ell^s+4\sum_{\substack{i\ge0\\ b_{i+1}=1}}\binom{\ell}{b_i+2}\ell^{s-b_i-1}\pmod8.} \tag{1}
\]
The sum is finite, and every exponent appearing in it is a nonnegative integer. At every even height \(h\ge4\), the one-carry contribution disappears:
\[
\boxed{S_{\ell}^{(h)}(n)\equiv\ell^s\pmod8\qquad(h\ge4\text{ even}).} \tag{2}
\]
The correction in (1) has the following sharp simplification. If \(\ell\) is odd,
\[
\boxed{S_{\ell}^{(2)}(n)\equiv\ell^s+4\left(\frac{\ell-1}{2}\bmod2\right)(s-b_0)\pmod8.} \tag{3}
\]
If \(\ell\) is even,
\[
\boxed{S_{\ell}^{(2)}(n)\equiv\ell^s+4\left(\binom\ell2\bmod2\right)\mathbf1_{\{n=2^j:j\ge1\}}\pmod8.} \tag{4}
\]
The two levels of the result differ already at \(\ell=3\), \(n=2\): \(S_3^{(2)}(2)=15\equiv7\pmod8\), while \(3^{s_2(2)}=3\).

**Exact dyadic residue law.** For every fixed positive \(\ell\equiv3\pmod4\), every \(k\ge2\), and every \(r\in\{1,3,5,7\}\),
\[
\boxed{\#\{0\le n<2^k:S_{\ell}^{(2)}(n)\equiv r\pmod8\}=2^{k-2}.} \tag{5}
\]
For even \(\ell\), formula (4) implies \(S_{\ell}^{(2)}(n)\equiv0\pmod8\) whenever \(s_2(n)\ge3\). Thus, among \(0\le n<X\), at most \(O((\log X)^2)\) indices have a nonzero residue modulo eight (for each fixed even level).

## Assumptions and scope
The parameters are integers \(\ell\ge1\), \(n\ge0\), and even \(h\ge2\); no primality, nonvanishing, or asymptotic hypothesis is imposed. The binomial coefficient \(\binom\ell r\) is zero when \(r>\ell\). We set \(b_0=0\) when \(n=0\), and \(s_2(0)=0\). For \(\ell=1\), all sums are identically one. Equations (1)–(4) include these boundary cases. Equation (5) is a finite **exact** census on every dyadic interval, not merely a natural-density assertion.

## Proof
**Step 1: Multinomial valuations count total binary carries.** In any composition \(k_1+\cdots+k_\ell=n\), let \(d_i\) be the number of summand digits equal to one in binary column \(i\), and let \(c_i\) be the carry entering this column, with \(c_0=0\). Digit addition gives
\[
 d_i+c_i=b_i+2c_{i+1}.
\]
The carries are nonnegative integers with finite support. Summing over \(i\) and using Legendre's factorial valuation identity gives
\[
\nu_2\!\left(\binom n{k_1,\ldots,k_\ell}\right)
=\sum_{j=1}^{\ell}s_2(k_j)-s_2(n)=\sum_{i\ge1}c_i.\tag{6}
\]
Thus an odd multinomial coefficient is equivalent to **no carries**, and exact valuation one is equivalent to **one carry of size one at exactly one column boundary**.

**Step 2: Enumerate zero carries.** At each position \(i\) with \(b_i=1\), select exactly one of the \(\ell\) summands to receive that bit; at each zero bit, select none. These choices are independent, so there are exactly \(\ell^s\) carry-free compositions. Every corresponding multinomial coefficient is odd; the square of every odd integer is \(1\pmod8\). The same holds at every even exponent \(h\ge2\).

**Step 3: Enumerate exactly one carry.** Suppose the unique positive outgoing carry is \(c_{i+1}=1\). The addition identity at position \(i\) forces \(d_i=b_i+2\), with \(\binom\ell{b_i+2}\) choices of summands. At position \(i+1\), the entering carry must stop immediately, so \(d_{i+1}+1=b_{i+1}\), forcing \(b_{i+1}=1\) and \(d_{i+1}=0\). All other nonzero binary positions carry exactly one chosen summand bit. Their number is \(s-b_i-1\), giving \(\ell^{s-b_i-1}\) choices. Distinct \(i\) give disjoint compositions. Every corresponding multinomial coefficient has valuation one and its square is \(4\pmod8\). Any coefficient with valuation at least two has square divisible by sixteen, so contributes zero modulo eight. This proves (1). At even height at least four, **every even coefficient's power is divisible by sixteen**, so only zero-carry terms remain, proving (2).

**Step 4: Simplify the correction.** If \(\ell\) is odd, the parities of \(\binom\ell2\) and \(\binom\ell3\) both equal the second least significant bit of \(\ell\), namely \(((\ell-1)/2)\bmod2\). As \(\ell\) is odd, each extra power of \(\ell\) is odd, and the correction modulo eight is four times this bit times the number of one digits in positions at least one, \(s-b_0\). This proves (3). If \(\ell\) is even, \(\binom\ell3\) is even. A term involving \(\binom\ell2\) survives modulo eight only when the power of \(\ell\) has exponent zero, namely \(s=1\) and \(b_i=0\), with \(b_{i+1}=1\). This says precisely that \(n\) is a positive power of two greater than one; the surviving term yields (4).

**Step 5: Count residues exactly.** Fix \(\ell\equiv3\pmod4\). Formula (3) becomes \(\ell^{b_0+t}+4t\pmod8\), where \(t=\sum_{i=1}^{k-1}b_i\). Its residue is determined by the pair \((b_0,t\bmod2)\). For \(\ell\equiv3\pmod8\), the four pairs give \(1,7,3,5\), respectively, in the order \((0,0),(0,1),(1,0),(1,1)\). For \(\ell\equiv7\pmod8\), they give \(1,3,7,5\). In either case, all four odd classes occur once among the four choices of pair. The top \(k-1\ge1\) digits have each parity at precisely \(2^{k-2}\) configurations, and the low bit is independent. This proves (5). Finally, when \(\ell\) is even and \(s_2(n)\ge3\), both terms of (4) vanish modulo eight. There are \(O((\log X)^2)\) integers below \(X\) with at most two one digits, giving the sparsity statement.

## Verification
Run `python3 verify.py` using the adjacent standalone file (Python standard library only). Its direct multinomial-power convolution modulo eight checks heights \(2,4,6,8\), levels \(1\) through \(32\), and all indices \(0\) through \(512\); independent exact factorial enumeration covers levels \(1\) through \(6\), indices \(0\) through \(10\). A separate exact valuation-one enumeration checks levels \(1\) through \(6\), indices \(0\) through \(12\). The dyadic four-residue census is checked for \(\ell\in\{3,7,11,15,19,23,27,31\}\) through block size \(2^{10}\). Recorded output appears in `verification_output.txt`. The infinite results rest on Steps 1–5, not on these finite tests.

## Relationship to prior work
Sun [1] introduced the multinomial-power family, identified its Franel and Domb specializations, and proved weighted index sums modulo primes plus a Domb-related supercongruence. The present statement instead classifies **individual terms uniformly modulo eight** for every even height and level, including a one-carry correction and exact dyadic residue distribution. Beluhov [2] studies two-adic valuations of lattice-walk counts \(\binom{2n}{n}S_\ell^{(2)}(n)\) and gives substantial existing valuation bounds; the known binomial and Domb special cases of our congruence are not separately asserted as novel. The related published result [3] concerns a weighted prime-indexed sum and its exceptional \(p\mid\ell+1\) branch, not the individual-term mod-eight sequence or its dyadic residue statistics. Calderon [4] analyzes Domb supercongruences at odd primes, likewise with a different object and modulus.

## Limitations
The theorem concerns only modulus eight and even heights. It does not give higher powers of two, odd heights, or new results for the already-classical central-binomial special case alone. The finite verifier is not a proof for all parameters. The literature comparison cannot exclude unpublished or unindexed equivalent formulas, and no independent audit has been performed.

## References
1. Zhi-Wei Sun, *A new kind of numbers and related congruences*, arXiv:2607.07638v1 (first public July 8, 2026), especially equation (1.5), Theorems 1.1–1.3 and Section 4. https://arxiv.org/abs/2607.07638
2. Nikolai Beluhov, *Powers of 2 in High-Dimensional Lattice Walks*, arXiv:2506.12789, Sections 1–6 and the valuation theorem. https://arxiv.org/abs/2506.12789
3. *The exceptional branch in Sun's multinomial prime congruence*, public finding identifier `2026/10/4/SCOPE-the-exceptional-branch-in-sun-s-multinomial-prime-congruence--54bbd0a326b7`; compare its weighted-sum statement modulo \(p\).
4. Kevin Calderon, *Supercongruences for Domb Numbers*, arXiv:2610.04772v1 (October 3, 2026). https://arxiv.org/abs/2610.04772
