# Dyadic 2-binomial complexity of the ordinary paperfolding word

## Finding
Let \(\mathbf f=f_0f_1\cdots\) be the binary ordinary paperfolding word, indexed from zero. For every integer \(k\ge 2\), its 2-binomial complexity at length \(2^k\) is
\[
 b_{\mathbf f}^{(2)}(2^k)=2^{k+1}+k+1.
\]
More precisely, at length \(L=2^k\) there are exactly three possible numbers of ones, \(L/2-1\), \(L/2\) and \(L/2+1\). These three weight groups contain respectively \(L\), \(k+1\), and \(L\) distinct 2-binomial equivalence classes. In the central group the sums of zero-based positions occupied by ones form one arithmetic progression of length \(k+1\) and common difference \(L/2\).

## Assumptions and scope
For \(n\ge0\), write \(n+1=2^v u\), where \(u\) is odd. Set \(f_n=0\) when \(u\equiv1\pmod4\) and \(f_n=1\) when \(u\equiv3\pmod4\). Equivalently, for \(i\ge0\),
\[
 f_{2i}=i\bmod 2,\qquad f_{2i+1}=f_i.
\]
For finite binary words \(x,y\) of the same length, write \(x\sim_2 y\) if every binary scattered subsequence of lengths one and two appears equally often in both. A scattered subsequence preserves order but need not use adjacent positions. The function \(b_{\mathbf f}^{(2)}(n)\) counts \(\sim_2\)-classes among **all** contiguous length-\(n\) factors of \(\mathbf f\), at arbitrary starting indices. The assertion applies to the specific ordinary binary paperfolding word and to all integers \(k\ge2\), not to arbitrary paperfolding instructions or nondyadic lengths.

For a factor \(x=x_0\cdots x_{L-1}\), set
\[
 W(x)=\sum_{j=0}^{L-1}x_j,\qquad S(x)=\sum_{j=0}^{L-1}j x_j.
\]
Write \(P_L^e\) for the set of all pairs \((W(x),S(x))\) as the starting index of \(x\) ranges through nonnegative integers congruent to \(e\pmod2\), for \(e\in\{0,1\}\).

## Proof
**Step 1: 2-binomial statistics.** For any binary word of length \(L\) with \(W\) ones and positional sum \(S\), the scattered ordered-pair counts are
\[
 \binom{x}{00}=\binom{L-W}{2},\quad
 \binom{x}{11}=\binom W2,\quad
 \binom{x}{01}=S-\binom W2,\quad
 \binom{x}{10}=W(L-W)-S+\binom W2.
\]
Indeed, if the one positions are \(j_1<\cdots<j_W\), the zeros preceding the \(t\)-th one number \(j_t-(t-1)\). Thus, at a fixed length, two words are 2-binomially equivalent if and only if their \((W,S)\) pairs agree.

**Step 2: exact parity refinement at length four.** Put \(i\equiv e\pmod2\), \(a=f_i\), and \(c=f_{i+1}\). The factors starting at \(2i\) and \(2i+1\) have respectively the four symbols
\[
 (e,a,1-e,c)\quad\text{and}\quad(a,1-e,c,e).
\]
Every choice of \((a,c)\in\{0,1\}^2\) occurs for each value of \(e\). Explicit witnesses are \(i=0,2,4,10\) for even \(i\), giving the pairs \((0,0),(1,0),(0,1),(1,1)\), and \(i=1,3,5,11\) for odd \(i\), giving \((0,1),(0,0),(1,1),(1,0)\). As no other binary adjacent pairs exist, the complete profile sets are
\[
\begin{aligned}
P_4^0={}&\{(1,0),(1,2),(2,1),(2,3),(2,5),(3,4),(3,6)\},\\
P_4^1={}&\{(1,1),(1,3),(2,1),(2,3),(2,5),(3,3),(3,5)\}.
\end{aligned}
\]
For each extreme weight, each parity set has two positional sums and the parity sets are disjoint, having opposite positional-sum parities. Both central-weight sets equal \(\{(2,1),(2,3),(2,5)\}\).

**Step 3: exact lifting to twice the factor length.** Let \(L\) be divisible by four, and let \(x=f_i\cdots f_{i+L-1}\), with \((W,S)=(W(x),S(x))\) and \(e=i\bmod2\). The recurrence for \(f\) interleaves the known alternating bits with the symbols of \(x\). For the factors of length \(2L\) starting at \(2i\) and \(2i+1\), respectively, the resulting pairs are
\[
\begin{aligned}
T_{L,e}^{0}(W,S)&=\left(W+\frac L2,\ 2S+W+\frac{L^2}2-eL\right),\\
T_{L,e}^{1}(W,S)&=\left(W+\frac L2,\ 2S+\frac{L^2}2+(2e-1)\frac L2\right).
\end{aligned}
\]
For example, the even offsets of the first lifted factor are the alternating bits \((i+j)\bmod2\), whose contribution to the positional sum is \(L^2/2-eL\); its odd offsets carry the symbols of \(x\). The second lifted factor reverses those two roles. Every starting index is uniquely \(2i\) or \(2i+1\), so there are **equalities of complete infinite factor-profile sets**, not sampling inclusions:
\[
P_{2L}^{d}=\bigcup_{e=0}^1 T_{L,e}^{d}(P_L^e),\qquad d\in\{0,1\}.
\]

**Step 4: induction for both extreme weights.** At \(L=4\), each extreme group in each \(P_L^e\) has \(L/2\) distinct pairs, and the two parity sets have sums of opposite parity. Assume these properties at some \(L=2^k\), \(k\ge2\). Both extreme weights lift to \(L-1\) or \(L+1\), respectively. Within either child parity, the contributions from \(e=0\) and \(e=1\) cannot overlap: an equality in either map would force the two parent sums to differ by \(L/2\), which is even, while they have opposite parity. Each map separately preserves distinctions because its positional-sum coordinate has coefficient two. Consequently each child parity contains \(L\) classes at each extreme weight. The child-even positional sums are odd, as the new weight is odd; the child-odd sums are even because \(L/2\) is even. Hence the two child parity sets are disjoint at each extreme weight. Thus, at length \(2L\), **each extreme weight contributes exactly \(2L\) classes**, and the opposite-parity condition is preserved.

**Step 5: induction for the middle weight.** At length \(L=2^k\), suppose both parity-indexed profile sets of middle weight \(W=L/2\) are
\[
\left\{\left(\frac L2,a+j\frac L2\right):0\le j\le k\right\}
\]
for some integer \(a\). This holds at length four with \(a=1\). Under \(T_{L,e}^{0}\), the two values of \(e\) yield two adjacent translates of an arithmetic progression of step \(L\), so the child-even middle-weight positional sums are
\[
\left\{2a+\frac{L^2}2-\frac L2+jL:0\le j\le k+1\right\}.
\]
Under \(T_{L,e}^{1}\), the child-odd middle-weight positional sums form exactly the same set. Thus at length \(2L\) the middle group has \(k+2\) classes, its two parity-indexed sets agree, and their step is \((2L)/2=L\). This closes the induction.

At length \(L=2^k\), the two extreme groups contribute \(L\) classes each, and the middle group contributes \(k+1\). They have different weights and cannot overlap. Therefore \(b_{\mathbf f}^{(2)}(2^k)=2L+k+1=2^{k+1}+k+1\) for every \(k\ge2\).

## Verification
Run the accompanying self-contained Python program with a standard Python 3 interpreter:

```bash
python verify_paperfolding_binomial.py
```

It reconstructs the exact parity-indexed base profiles from the eight permitted adjacent-pair types; applies the exact profile transforms and tests the three class-count claims for exponents \(2\) through \(12\); independently computes over \(65{,}000\) paperfolding bits by the odd-part formula and the even/odd recurrence; and compares the derived complete profile sets with direct sliding windows through exponent \(10\). It also verifies the scattered-pair count formulas on short explicit words. The observed output concludes with `VERIFY_OK`. The infinite theorem relies on Steps 1–5, not on the finite tests.

## Relationship to prior work
Madill and Rampersad established 2-regularity and explicit recurrences for the **ordinary abelian** complexity of the paperfolding word. In particular, their recurrences give ordinary abelian complexity \(3\) at dyadic lengths at least four. The present result counts **scattered length-two** subword multiplicities and shows that those same three weight classes split into \(2^k\), \(k+1\), and \(2^k\) refined classes.

Rigo and Salimov introduced the binomial-complexity framework and computed it for Sturmian and Thue–Morse words, not for the ordinary paperfolding word in their inspected preprint. Later work on generalized Thue–Morse 2-binomial complexity concerns a distinct morphic word. Work on reduced complexities of paperfolding words first collapses constant-letter runs and thus uses a different equivalence relation. The displayed numerical values also coincide, under an index shift, with the arithmetic sequence recorded as OEIS A006127; that generic integer sequence does not itself establish an interpretation as paperfolding factor classes.

## Limitations
The theorem does not address nondyadic lengths, higher orders of binomial equivalence, or non-regular paperfolding instructions. The explicit central arithmetic progression is proven to exist and to have the indicated length and step, but no standalone formula for its starting value is needed. The literature comparison is limited to the named accessible works and searches; an unindexed or unavailable equivalent theorem may exist. Verification is reproducible and internally checked, but has not undergone an independent scientific audit.

## References
1. B. Madill and N. Rampersad, *The abelian complexity of the paperfolding word*, arXiv:1208.2856v1 (first posted 2012-08-14), https://arxiv.org/abs/1208.2856.
2. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, author preprint publicly available by 2013-05-27, https://orbi.uliege.be/handle/2268/149313.
3. X.-T. Lü, J. Chen, Z.-X. Wen and W. Wu, *On the 2-binomial complexity of the generalized Thue–Morse words*, arXiv:2112.05347, https://arxiv.org/html/2112.05347v1.
4. J. M. Campbell, J. Currie and N. Rampersad, *Reduced complexities for sequences over finite alphabets*, arXiv:2509.16034v1, https://arxiv.org/abs/2509.16034.
5. OEIS Foundation, *A006127: \(a(n)=2^n+n\)*, https://oeis.org/A006127.
