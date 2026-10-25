# Exact palindromic length at binary weight three and its one-sixth extremal density

## Finding

The **palindromic length** \(\operatorname{PL}(w)\) of a nonempty finite word is the least number of nonempty contiguous palindromes whose concatenation equals \(w\). For arbitrary integers \(a,b,c,d\geq0\), write
\[
w=0^a1\,0^b1\,0^c1\,0^d.
\]
Then
\[
\operatorname{PL}(w)=
\begin{cases}
1,&a=d\ \text{and}\ b=c,\\
2,&b=c\ \text{or}\ b=a+d\ \text{or}\ c=a+d,\quad\text{unless the first case holds},\\
4,&b\ne c\ \text{and}\ \min(a,d)>\max(b,c),\\
3,&\text{otherwise}.
\end{cases}
\]
In particular, four is the largest possible palindromic length among binary words containing exactly three ones. Four occurs for the first time at length eight, for exactly the two words \(00110100\) and \(00101100\).

Let \(E_n\) be the number of binary words of length \(n\) containing exactly three ones and having palindromic length four. Then the exact ordinary generating function is
\[
\sum_{n\geq3}E_nz^n=\frac{2z^8}{(1-z)^2(1-z^3)(1-z^4)}.
\]
Consequently
\[
E_n=\frac{n^3}{36}+O(n^2),\qquad
\lim_{n\to\infty}\frac{E_n}{\binom n3}=\frac16.
\]

## Assumptions and scope

Words are finite over the alphabet \(\{0,1\}\). The three displayed occurrences of \(1\) are the only occurrences; all four zero-gap parameters are arbitrary nonnegative integers. Factorizations use consecutive, nonempty palindromes, not scattered subsequences, and the empty word is not counted as a factor. In constructive factorizations, zero-length zero blocks are omitted. The counting series counts distinct literal words, not words modulo reversal or complementation. The variable \(z\) is formal.

## Proof

**Preliminary lemma (up to two markers).** Every binary word with at most two ones has palindromic length at most two. For one marker, \(0^u1\,0^v\), remove a pure-zero prefix or suffix of length \(|u-v|\); what remains is \(0^{\min(u,v)}1\,0^{\min(u,v)}\). For two markers, \(0^u1\,0^v1\,0^t\), remove a pure-zero prefix or suffix of length \(|u-t|\); what remains is \(0^{\min(u,t)}1\,0^v1\,0^{\min(u,t)}\). Each remaining block is a palindrome. Zero-marker words are palindromes.

**Upper bound four.** Split \(w\) immediately before its last \(1\), obtaining a two-marker prefix \(0^a1\,0^b1\,0^c\) and a one-marker suffix \(1\,0^d\). Each has palindromic length at most two by the lemma, so \(\operatorname{PL}(w)\leq4\).

**Lengths one and two.** The full word is a palindrome exactly when its first and last zero gaps agree and its two inner gaps agree, namely \(a=d\) and \(b=c\). If \(b=c\), the three-one core \(1\,0^b1\,0^b1\) is a palindrome; its outer zero padding can be balanced by discarding a single pure-zero prefix or suffix, so the word is a product of at most two palindromes. Assume \(b\ne c\). A palindrome cannot then contain all three ones, so any factorization into two palindromes must allocate the ones as \((1,2)\) or \((2,1)\). In the first allocation the initial palindrome must be \(0^a1\,0^a\), leaving the required palindrome \(0^{b-a}1\,0^c1\,0^d\). This is possible exactly when \(b=a+d\). In the second allocation the initial palindrome must be \(0^a1\,0^b1\,0^a\), leaving \(0^{c-a}1\,0^d\); this is possible exactly when \(c=a+d\). Both equalities automatically ensure the zero counts used are nonnegative. Thus the stated first two cases are exact.

**The four-factor obstruction.** Suppose \(b\ne c\) and \(a,d>\max(b,c)\). No palindromic prefix can contain a \(1\): a prefix with one \(1\) requires \(a\leq b\), a prefix with two requires \(a\leq c\), and a prefix with three requires \(b=c\). Symmetrically, no palindromic suffix can contain a \(1\). A hypothetical factorization into at most three nonempty palindromes would therefore have to start and end with pure-zero factors and place all three ones in a single middle palindrome. That would require \(b=c\), a contradiction. Hence four factors are necessary.

**All remaining cases need at most three.** Assume \(b\ne c\) and \(\min(a,d)\leq\max(b,c)\). Reversing the word if needed, we can arrange \(a\leq\max(b,c)\). If \(a\leq b\), take the palindromic prefix \(0^a1\,0^a\); the remainder has two ones and needs at most two palindromes. If instead \(a\leq c\), take the palindromic prefix \(0^a1\,0^b1\,0^a\); the remainder has one \(1\) and needs at most two palindromes. The previous paragraph and the length-two classification separate the cases exactly, completing the four-tier formula.

**Enumeration.** Four factors are required precisely for unequal inner gaps and outer gaps greater than both inner gaps. Put \(m=\max(b,c)\geq1\), \(\ell=\min(b,c)\in\{0,\dots,m-1\}\), \(a=m+1+r\), and \(d=m+1+s\), with \(r,s\geq0\). There are two orders of the unequal inner gaps and the word length equals \(3m+\ell+5+r+s\). Therefore
\[
\begin{aligned}
\sum_{n\geq3}E_nz^n
&=\frac{2z^5}{(1-z)^2}\sum_{m\geq1}\sum_{\ell=0}^{m-1}z^{3m+\ell}\\
&=\frac{2z^5}{(1-z)^3}
\left(\frac{z^3}{1-z^3}-\frac{z^4}{1-z^4}\right)\\
&=\frac{2z^8}{(1-z)^2(1-z^3)(1-z^4)}.
\end{aligned}
\]
The first nonzero coefficient is \(E_8=2\). Near \(z=1\), this rational function has leading principal part \(1/[6(1-z)^4]\); other poles on the unit circle have lower order. Hence \(E_n=n^3/36+O(n^2)\). Dividing by the total \(\binom n3=n^3/6+O(n^2)\) three-one words yields the one-sixth limit.

## Verification

The standalone \`check.py\` independently computes palindromic length from its definition using a dynamic program over all palindromic substrings, with no use of the four-gap formula in the dynamic-programming routine. It checks every parameter quadruple with \(0\leq a,b,c,d\leq10\), totaling \(14641\) quadruples. It separately enumerates every three-one word of lengths three through twenty-eight and compares the observed four-factor counts against coefficients of the rational generating function, calculated from its product expansion. It checks the first two extremal words at length eight. All finite checks passed when run with Python 3; these checks corroborate but do not substitute for the unrestricted proof above. Reproduce with \`python3 check.py\` in the directory containing the embedded source.

## Relationship to prior work

Ravsky's analysis of the maximum palindromic length among **all** binary words at fixed total length gives a global worst-case function, without an all-gap classification at fixed weight three. The later work of Frid, Puzynina, and Zamboni develops factorization bounds and unboundedness for factors of infinite words. Bucci and Richomme investigate greedy variants and periodicity of infinite words. These results establish the importance of the invariant but do not state the four-tier sparse-word formula or its extremal rational generating function. A general minimum-palindromic-factorization algorithm can evaluate individual words, but such an algorithm by itself does not give the closed-form four-gap classification or the asymptotic one-sixth proportion. The first length-eight extremal phenomenon is consistent with previously known global worst-case tables and is not itself claimed as an independently new global optimum.

## Limitations

The theorem applies only to words with exactly three ones. No analogous formula is claimed for words with four or more ones or for larger alphabets. The proof establishes an exact classification and enumeration, not a new general-purpose palindrome-factorization algorithm. Historical priority is not certified: an unindexed or earlier equivalent fixed-weight statement may exist despite the targeted comparisons. Independent mathematical audit has not been performed.

## References

1. A. Ravsky, *On the palindromic decomposition of binary words*, arXiv:1004.1278, publicly accessible arXiv version dated 2010-04-08, https://arxiv.org/abs/1004.1278.
2. A. E. Frid, S. Puzynina, and L. Q. Zamboni, *On minimal factorizations of words as products of palindromes*, arXiv:1210.6179, initial arXiv date 2012-10-23, https://arxiv.org/abs/1210.6179.
3. M. Bucci and G. Richomme, *Greedy palindromic lengths*, arXiv:1606.05660, initial arXiv date 2016-06-17, https://arxiv.org/abs/1606.05660.
