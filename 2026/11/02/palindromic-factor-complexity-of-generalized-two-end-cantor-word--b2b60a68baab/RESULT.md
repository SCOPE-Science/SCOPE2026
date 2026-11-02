# Palindromic-factor complexity of generalized two-end Cantor words

## Finding
For each integer \(b\ge4\), define the infinite binary word \(C_b=c_0c_1c_2\cdots\) by \(c_n=1\) exactly when every base-\(b\) digit of \(n\) lies in \(\{0,b-1\}\). Equivalently, \(C_b\) is the fixed point beginning in \(1\) of
\[
\mu_b(1)=1\,0^{b-2}\,1,\qquad \mu_b(0)=0^b.
\]
Let \(P_b(n)\) denote the number of **distinct contiguous palindromic factors** of length \(n\) in \(C_b\), counting a factor once regardless of occurrences. Put \(a=b-2\) and \(g_j=a b^j\). For **every** \(n\ge1\),
\[
\boxed{\displaystyle P_b(n)=1+
\mathbf1_{\{n\text{ odd},\ n\le 2a+1\}}
+\sum_{j\ge0}\mathbf1_{\{g_j+2\le n\le(2a+1)b^{j+1},\ n\equiv g_j\pmod2\}}.}
\]
The sum is finite for each \(n\). In fact, **every** palindrome containing at least two occurrences of \(1\) is the unique central length-\(n\) factor (for its length \(n\)) of one of the words
\[
Q_j=0^{g_{j+1}}\,\mu_b^{j+1}(1)\,0^{g_{j+1}},\qquad j\ge0.
\]
A nonzero central factor of \(Q_j\) exists at length \(n\) exactly for the interval/parity in the sum. All remaining distinct palindromes are \(0^n\) and, when \(n\) is odd and \(n\le2a+1\), the central factor of \(0^a1 0^a\). Consequently \(P_b(n)\in\{1,2,3\}\) and each of these values occurs for every \(b\ge4\). As a concrete example, \(P_4(10)=3\), \(P_4(22)=2\), and \(P_4(34)=3\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); bases \(b\) and factor lengths \(n\) are integers with \(b\ge4\), \(n\ge1\). A factor is consecutive, not a scattered subsequence. The ambient word is one-sided infinite, and its factors may occur arbitrarily far to the right. The result counts distinct palindrome **words**, not occurrences, maximal palindrome intervals, or symmetry-axis spacings. No genericity, probabilistic assumptions or unproved computational hypotheses are required.

The same proof and displayed formula also work at the classical base \(b=3\); that boundary instance is included only as a consistency observation, not as a novelty assertion. Base \(b=2\) is excluded because the fixed point then equals \(111\cdots\).

## Proof
**1. Exact gaps.** List the increasing positions carrying \(1\) as \(p_0,p_1,\ldots\). Since \(p_i\) is obtained from the binary expansion of \(i\) by replacing each binary digit \(1\) with the base-\(b\) digit \(b-1\), for \(i\ge1\), letting \(v_2(i)\) be the exponent of \(2\) dividing \(i\), elementary binary carrying gives
\[
p_i-p_{i-1}-1=a b^{v_2(i)}=g_{v_2(i)}.\tag{1}
\]
Indeed, if \(i\) has \(j\) trailing zero bits, then \(i-1\) has \(j\) trailing one bits, so
\[
p_i-p_{i-1}=(b-1)\left(b^j-\sum_{h=0}^{j-1}b^h\right)=(b-2)b^j+1.
\]
In particular the gaps of zeros are unbounded, so \(0^n\) is a factor for all \(n\ge1\).

**2. Palindromes with one \(1\).** Such a palindrome has the form \(0^r1 0^r\). At every interior \(1\) the gaps immediately to its left and right have lengths \(g_{v_2(i)}\) and \(g_{v_2(i+1)}\). Exactly one of \(i,i+1\) is odd, so the shorter is \(g_0=a\). Conversely an interior \(1\) exists with at least \(a\) zeros on both sides. Therefore \(0^r1 0^r\) occurs exactly for \(0\le r\le a\), yielding one distinct such palindrome of each odd length \(n\le2a+1\).

**3. Symmetric central blocks.** Take any palindrome with at least two \(1\)'s. Its two central \(1\)'s are consecutive in \(C_b\), say \(p_{i-1},p_i\): if a further \(1\) lay between them, it would be closer to the center. Thus the palindrome is centered at the midpoint of the zero gap indexed by \(i\). Write \(j=v_2(i)\). The gap lengths on the two sides of that midpoint at separation \(h\) are indexed by \(i-h\) and \(i+h\). For \(1\le h<2^j\),
\[
v_2(i-h)=v_2(h)=v_2(i+h),\tag{2}
\]
so the adjacent gap/one pattern is mirrored through \(2^j\) ones on each side. At the next step, \(h=2^j\), the indices \(i-2^j\) and \(i+2^j\), when both positive, have unequal valuations: one is \(j+1\), the other at least \(j+2\). If the left index is zero, the actual palindrome can only be shorter, and the same upper bound follows.

The central \(2^{j+1}\) ones and their intervening gaps consequently form \(\mu_b^{j+1}(1)\). More explicitly, the index \(i-2^j\) is divisible by \(2^{j+1}\), so every interior gap index \(i-2^j+t\), \(1\le t<2^{j+1}\), has valuation \(v_2(t)\). Therefore its full internal gap list agrees with that of \(\mu_b^{j+1}(1)\). This block is a palindrome of length \(b^{j+1}\), with central zero run of length \(g_j\). The first mismatched outer gaps have lengths \(g_{j+1}\) and at least \(g_{j+2}\). Hence any palindromic extension on that axis lies inside
\[
Q_j=0^{g_{j+1}}\mu_b^{j+1}(1)0^{g_{j+1}},\qquad
|Q_j|=b^{j+1}+2g_{j+1}=(2a+1)b^{j+1}.\tag{3}
\]
Conversely this entire word actually occurs around the gap indexed by \(i=3\cdot2^j\): its two outer neighboring gaps have lengths \(g_{j+1}\) and \(g_{j+2}\), each at least \(g_{j+1}\). Thus (3) is an attained exact bound, not merely an estimate.

**4. Distinct factors and lengths.** Every palindrome centered at a \(g_j\)-gap is the central factor of \(Q_j\); for each fixed length \(n\), there is at most one such word. Its center has the same parity as \(g_j\). For \(n\le g_j\) it contains no \(1\); for the next admissible parity length \(n=g_j+2\) it contains its two nearest \(1\)'s. It therefore contributes one *new* nonzero palindrome precisely when
\[
g_j+2\le n\le (2a+1)b^{j+1},\quad n\equiv g_j\pmod2.\tag{4}
\]
For two different gap levels \(j\ne k\), the resulting nonzero palindromes have different lengths of their **central zero runs** (\(g_j\ne g_k\)), so they cannot coincide. They also differ from the one-\(1\) palindromes of step 2. Adding the one all-zero palindrome proves the formula.

**5. Sharp boundedness.** For \(b\ge4\), \(g_{j+2}+2>(2a+1)b^{j+1}\), since \((b-2)b>2b-3\). Thus at most two consecutive indices \(j\) can contribute for a fixed \(n\). The one-\(1\) contribution cannot overlap two gap contributions: its length is at most \(2a+1\), whereas the second gap level begins at \(g_1+2=a b+2>2a+1\). Hence \(1\le P_b(n)\le3\). The value \(2\) occurs at \(n=1\); the value \(3\) occurs at \(n=g_1+2\) (both levels \(0,1\) contribute); the value \(1\) occurs at \(n=2\) for odd \(b\), and at \(n=2a+3\) for even \(b\). This proves sharpness.

## Verification
A standalone Python-standard-library program, `verify.py`, reconstructs finite prefixes by substitution, independently checks each symbol against the base-digit definition, and enumerates **all distinct palindromic factors** for each length \(1\le n\le149\) for each \(b\in\{3,4,5,6,7\}\). It matches the formula in all \(745\) cases. Independent computations check the first \(511\) one-position gaps and the palindromicity of five successive substituted cores. Run from the supplied directory using `python verify.py`; expected terminal message begins with `VERIFY_OK`.

These finite tests are regressions only. The universal claim for arbitrary \(b,n\) follows from steps 1–5, not extrapolation from tested prefixes.

## Relationship to prior work
Chen, Lü and Wu (2017) analyze \(k\)-Abelian complexity of the **classical** \(b=3\) Cantor sequence and prove its \(3\)-regularity. Their invariant identifies factors through \(k\)-Abelian equivalence rather than counting distinct palindromic factors; their statements do not give the formula (4) for any \(b\ge4\).

Morfonios, Schmelcher, Kalozoumis and Diakonos (2013 preprint) investigate maximal-palindrome *positions, lengths and spacings* for the classical \(b=3\) Cantor lattice (Section III.5). Their conclusion that all maximal-palindrome lengths occur does not count distinct palindrome words at a fixed length, nor extend to the full base family. Allouche, Baake, Cassaigne and Damanik (2001) prove automaticity of palindrome complexity under **primitive** uniform class-P morphisms with extra hypotheses; \(\mu_b(0)=0^b\) is nonprimitive, and their result is not this explicit spectrum. The general automatic-sequence reflection-complexity results of Allouche and collaborators (2024) concern reversal-equivalence classes and do not list the present closed formula.

The contribution is the explicit all-base \(b\ge4\) classification and exact factor-count spectrum, based on the two-adic gap hierarchy. Generic automaticity or reversal-count identities alone do not evaluate these interval thresholds.

## Limitations
The theorem concerns two-end digit Cantor words and ordinary reversal palindromes; it does not classify arbitrary deleted-digit Cantor sets or counts of occurrences of a factor. It makes no claim about the number or distribution of maximal-palindrome axes. Published-source inspection and semantic searches cannot rule out an unindexed equivalent proof or theorem; further independent expert assessment would be valuable. Finite regression tests do not supply an independent proof of infinite claims.

## References
1. Jin Chen, Xiaotao Lü and Wen Wu, *On the \(k\)-Abelian complexity of the Cantor sequence* (first public 2017-03-12), https://arxiv.org/abs/1703.04063.
2. C. Morfonios, P. Schmelcher, P. A. Kalozoumis and F. K. Diakonos, *Local symmetry dynamics in one-dimensional aperiodic lattices* (first public 2013-07-07), https://arxiv.org/abs/1307.1838, Section III.5.
3. J.-P. Allouche, M. Baake, J. Cassaigne and D. Damanik, *Palindrome complexity* (first public 2001-06-14), https://arxiv.org/abs/math/0106121, especially Section 6.
4. J.-P. Allouche and collaborators, *The reflection complexity of sequences over finite alphabets* (first public 2024-06-13), https://arxiv.org/abs/2406.09302, especially Sections 2 and 6.
