# Frobenius–genus strictness for three consecutive fifth powers

## Finding
For every integer \(n\ge3\), consider the numerical semigroup
\[
S_n=\langle (n-1)^5,n^5,(n+1)^5\rangle
=\{a(n-1)^5+bn^5+c(n+1)^5:a,b,c\in\mathbb Z_{\ge0}\}.
\]
Write \(F_n\) for its Frobenius number (greatest nonmember) and \(g_n\) for its genus (number of nonnegative nonmembers). Then
\[
2g_n=F_n+1\quad\Longleftrightarrow\quad n=3.
\]
More precisely, \(S_3=\langle32,243\rangle\) has \(F_3=7501\) and \(g_3=3751\); for **every** \(n\ge4\), \(2g_n>F_n+1\). In semigroup language, the only symmetric member of this fifth-power family is \(S_3\).

## Assumptions and scope
All generators are positive integers, \(n\ge3\), and the semigroup includes zero. Consecutive generators are coprime, so \(S_n\) is cofinite, and \(F_n\) and \(g_n\) exist. Coefficients in a generating-semigroup membership equation are nonnegative integers. No prime or congruence condition is imposed on \(n\).

For any numerical semigroup \(S\), the map \(x\mapsto F(S)-x\), for \(0\le x\le F(S)\), sends each member to a nonmember (otherwise their sum would equal \(F(S)\)). Therefore \(2g(S)\ge F(S)+1\); equality is equivalent to the standard symmetry condition that, for every \(0\le x\le F(S)\), exactly one of \(x\) and \(F(S)-x\) lies in \(S\). We classify that equality.

## Proof
We use the classical classification of symmetric semigroups with at most three generators (Herzog's three-generated criterion, in the form recalled by Fel [1, §1]): a minimally three-generated symmetric numerical semigroup has a pair of generators with a nontrivial common divisor. Moreover, if two generators are \(a u,a v\), with \(a>1\), \(\gcd(u,v)=\gcd(a,w)=1\), then \(\langle au,av,w\rangle\) is symmetric if and only if \(w\in\langle u,v\rangle\) (Watanabe's criterion [1, Lemma 1]). Semigroups with two coprime generators are symmetric.

**Odd indices.** Write \(n=2m+1\), \(m\ge1\). The two outer generators are \(32m^5\) and \(32(m+1)^5\), while the middle generator is \((2m+1)^5\), which is coprime to \(32\). Watanabe's criterion makes symmetry equivalent to
\[
(2m+1)^5=A m^5+B(m+1)^5,
\qquad A,B\in\mathbb Z_{\ge0}.
\tag{1}
\]
For \(m=1\), this is solvable, because \(3^5=243\in\langle1,2^5\rangle\), and the original largest generator is already a multiple of the smallest.

Let \(m\ge2\) and suppose (1). Since \((2m+1)/(m+1)<2\), one has \(0\le B\le31\). Reduction modulo \(m\) gives \(B\equiv1\pmod m\), so \(B=1+jm\) with \(j\ge0\), \(jm\le30\). Reduction modulo \(m^2\), using \((2m+1)^5\equiv1+10m\) and \((m+1)^5\equiv1+5m\), yields
\[
j\equiv5\pmod m.\tag{2}
\]
For \(m\ge7\), \(0\le j\le\lfloor30/m\rfloor\le4\), contrary to (2). For \(m=6\), (2) forces \(j=5\), hence \(B=31\), but \(31\cdot7^5>13^5\). For \(m=5\), the bound \(B\le\lfloor11^5/6^5\rfloor=20\) leaves only \(B=1\) under (2). Then \(11^5-6^5=153275\not\equiv0\pmod{5^5}\). For \(m=4\), the bound \(B\le\lfloor9^5/5^5\rfloor=18\) and (2) leave \(B=5\); yet \(9^5-5\cdot5^5\equiv416\pmod{4^5}\). For \(m=3\), \(B\le16\) leaves \(B\in\{7,16\}\); the remainders of \(7^5-B4^5\) modulo \(3^5=243\) are \(162,180\), respectively. For \(m=2\), the bound \(B\le12\) and (2) give \(B\in\{3,7,11\}\). But divisibility of \(5^5-B3^5\) by \(2^5\) would imply \(B\equiv23\pmod{32}\), excluding each. Therefore **no odd** \(n\ge5\) is symmetric.

**Even indices.** If \(n\ge4\) is even, the three fifth-power generators are pairwise coprime: any two consecutive bases are coprime, and \(\gcd(n-1,n+1)=1\). By the three-generator symmetry criterion, a symmetric semigroup could arise only if a generator is redundant. The smallest is not redundant; the middle one cannot be expressed using the smallest and largest, because it is below the largest and is not a multiple of the coprime smaller generator. Thus only the largest could be redundant, requiring
\[
(n+1)^5=A(n-1)^5+Bn^5,\qquad A,B\in\mathbb Z_{\ge0}.\tag{3}
\]
Reducing modulo \(n\) gives \(1\equiv-A\pmod n\), so \(A\ge n-1\). But (3) also implies \(A\le((n+1)/(n-1))^5\). For every even \(n\ge8\), the right side is at most \((9/7)^5<7\le n-1\), a contradiction. At \(n=6\), the conditions force \(A=5\), while \(7^5-5\cdot5^5=1182\) is not divisible by \(6^5\). At \(n=4\), the conditions leave \(A\in\{3,7,11\}\); the remainders of \(5^5-A3^5\) modulo \(4^5\) are respectively \(348,400,452\), all nonzero. Therefore **no even** \(n\ge4\) is symmetric.

Finally, \(S_3=\langle2^5,3^5,4^5\rangle=\langle32,243\rangle\). By the classical two-generator formula, \(F_3=32\cdot243-32-243=7501\) and \(g_3=(F_3+1)/2=3751\). The two parity cases prove the theorem. \(\square\)

## Verification
A standalone Python 3 program, `verify.py`, independently checks the finite congruence branches in the proof, the candidate nonmembership equations over expanded ranges, and exact Frobenius/genus computations for small \(n\) using shortest-path Apéry sets. Run `python3 verify.py`; the expected output is `VERIFY_OK`. The infinite classification is proved by the modular inequalities above; finite checks alone would not suffice.

## Relationship to prior work
Fel [1] treats exactly the analogous generators for exponents \(2,3,4\), proving that the fourth-power case is symmetric at \(n\in\{3,5,7\}\), and explicitly raises the higher-power \(k\ge5\) case. The present result establishes a genuinely different boundary at exponent five: the two extra quartic symmetry exceptions disappear. Fel [1, §5] additionally reports a bounded numerical search over odd indices and many powers, in which the only higher-power symmetric examples found are at exponent eleven or thirteen and index five. That computation already supplies partial finite evidence against fifth-power exceptions; the new contribution is the all-index fifth-power proof, including even indices. Its argument specializes the three-generator symmetric-semigroup criteria recalled in [1], but the full fifth-power Diophantine exclusions, strict genus/Frobenius inequality, and all-\(n\) classification are not given there. Rosales and Branco [2] give related Frobenius/genus methods; their complete text was unavailable for detailed comparison. The statement may still follow from an unlocated later general classification; no absolute novelty is claimed.

## Limitations
Only the equality or strictness of \(2g_n\ge F_n+1\) is determined for \(n\ge4\): no explicit formula for \(F_n\), \(g_n\), or their positive difference is asserted. The cited three-generator structural theorem is classical external input; the new modular deductions are written out. The literature check does not constitute independent priority certification.

## References
[1] L. G. Fel, *Numerical semigroups generated by squares, cubes and quartics of three consecutive integers*, arXiv:1608.08693v1, first posted 2016-08-31, especially Section 1, Lemma 1, Propositions 1–3 and the higher-power problem statement. https://arxiv.org/pdf/1608.08693

[2] J. C. Rosales and M. B. Branco, *The Frobenius problem for numerical semigroups*, Journal of Number Theory 131 (2011), 2310–2319, DOI:10.1016/j.jnt.2011.05.011, MSC 11D07 and 20M14. This is background on the Frobenius and genus framework, not a claimed source for the fifth-power classification.

[3] K. Watanabe, *Some examples of one-dimensional Gorenstein domains*, Nagoya Mathematical Journal 49 (1973), 101–109, cited as [15] in [1]. The gluing criterion used above is as reproduced and inspected in [1].
