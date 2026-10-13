# Sharp reversal-isolation thresholds in generalized Chacon words

## Finding
For every integer \(a\ge3\), define a binary morphism \(\sigma_a(0)=0^a10\) and \(\sigma_a(1)=1\). Let \(c_a=\sigma_a^\omega(0)\), and let \(\mathcal F_a(n)\) denote its set of contiguous factors of length \(n\). The **reversal-isolation threshold** is the least positive integer \(T(a)\) such that, for every \(n\ge T(a)\) and every \(u\in\mathcal F_a(n)\), the reversal \(u^R\) is not in \(\mathcal F_a(n)\). In particular, a palindrome fails the isolation condition.

The exact sharp threshold is
\[
T(a)=\begin{cases}19,&a=3,\\a^2+3a,&a\ge4.\end{cases}
\]
The threshold is attained sharply: a palindrome of length \(T(a)-1\) occurs, while not one length-\(T(a)\) factor occurs together with its reversal. In the notation \(\rho_{c_a}(n)=|\mathcal F_a(n)|\) and \(r_{c_a}(n)\) for the number of reversal classes of factors, this implies \(r_{c_a}(n)=\rho_{c_a}(n)\) for every \(n\ge T(a)\). For comparison, the established classical Chacon case \(a=2\) has threshold \(13\); this earlier case is not asserted as new.

## Assumptions and scope
All words are one-sided, infinite, and over the alphabet \(\{0,1\}\), with reversal read in the usual order. No genericity or probabilistic assumption is made. Write \(W_0=0\) and \(W_{j+1}=W_j^a1W_j\), so \(c_a=\lim_{j\to\infty}W_j\). Each \(W_j\), for \(j\ge1\), starts with exactly \(a\) zeros and ends with one zero. The three distinct lengths of zero gaps between consecutive ones are denoted
\[
A=a+1,\qquad B=a,\qquad C=1.
\]
The initial zero run before the first one has length \(B\); later gap lengths are in \(\{A,B,C\}\).

## Proof
### Gap grammar
Let \(G_j\) list the numbers of zeros between consecutive ones in \(W_j\), and put \(G\) for the infinite limit. For \(j\ge2\), concatenation of the blocks \(W_j\) gives the exact word recurrence
\[
G_2=A^{a-1}CB,\qquad G_{j+1}=(G_jA)^{a-1}G_jCBG_j.\tag{1}
\]
Here powers denote repetition of a *letter representing a gap length*, not multiplication of gap lengths. Indeed, two adjacent copies of \(W_j\) contribute the gap \(A\); the distinguished inserted one contributes consecutive gaps \(C,B\). Every \(G_j\) for \(j\ge2\) starts with \(A^{a-1}CB\) and ends with \(CB\).

Induction using (1) establishes the following complete local restrictions in \(G\):

1. Every gap digram belongs to \(\{AA,AC,BA,BC,CB\}\). The two-letter patterns whose reversals also occur are only \(AA,BC,CB\).
2. Every maximal \(A\)-run has length at most \(a\). An \(A\)-run of length exactly \(a\) has left/right neighboring gaps \((B,C)\). An occurrence of \(A^{a-1}\), when supplied with its neighboring gaps, has one of the contexts \((B,C),(B,A),(A,C)\). For the leftmost occurrence, the initial zero-run of length \(B\) is used as its left context.
3. Every alternating run consisting solely of \(B,C\) has length at most four.

For completeness, these assertions can be checked directly from the concatenation boundaries in (1). Inside any copied \(G_j\), the induction hypothesis applies. At an ordinary boundary the suffix \(CB\) is followed by \(A^{a}C\), giving the new maximal \(A\)-run in context \(BA^aC\). At the distinguished boundary the last two gaps \(CB\) are followed by \(CB\) and then a prefix \(A\), giving at most \(CBCB\). All other new adjacencies are \(BA,AA,AC,BC\). An \(A^{a-1}\) occurrence is either an entire \(A\)-run of length \(a-1\), flanked \((B,C)\), or the first/last \(a-1\) letters in \(BA^aC\), with contexts \((B,A)\) and \((A,C)\) respectively. This proves all three assertions at each finite level and hence in the limit.

### Reversible factors for \(a\ge4\)
Suppose a factor \(u\) and its reversal both occur. If \(u\) contains \(h\ge2\) ones, then its \(r=h-1\) *complete* zero gaps between consecutive ones form a word \(D\) whose reverse must also be a factor of \(G\). By restriction 1, \(D\) is either an all-\(A\) word or an alternating word on \(B,C\). Let \(x,y\) be the numbers of zeros of \(u\) before its first and after its last one; each lies between zero and \(A\).

If \(D\) alternates \(B,C\), restriction 3 gives \(r\le4\). Thus its complete gaps contribute at most \(2B+2C=2a+2\) zeros, its \(r+1\) ones contribute at most five symbols, and its two partial end runs contribute at most \(2A\). Therefore
\[
|u|\le4a+9.\tag{2}
\]
If \(D=A^r\), restriction 2 gives \(r\le a\). For \(r\le a-2\),
\[
|u|\le r(A+1)+1+2A\le a^2+2a-1.\tag{3}
\]
For \(r=a\), every occurrence has neighboring gaps \((B,C)\). Since both orientations of \(u\) occur, the left and right partial zero runs of \(u\) each have length at most \(\min(B,C)=1\). Thus
\[
|u|\le aA+(a+1)+2=a^2+2a+3.\tag{4}
\]
For \(r=a-1\), let the context of the occurrence of \(u\) be \((P,Q)\) and that of its reversal be \((P',Q')\); both contexts belong to \(\{(B,C),(B,A),(A,C)\}\). Their opposite orientations impose
\[
x\le\min(P,Q'),\qquad y\le\min(Q,P').
\]
Checking the nine possible ordered context pairs gives
\[
\max_{(P,Q),(P',Q')}\bigl(\min(P,Q')+\min(Q,P')\bigr)=2a.
\]
Consequently
\[
|u|\le(a-1)A+a+2a=a^2+3a-1.\tag{5}
\]
A factor with no ones has length at most \(A\); a factor with one one has length at most \(2A+1\). For every integer \(a\ge4\), the right-hand sides of (2)--(4), and these two remaining bounds, do not exceed \(a^2+3a-1\). Thus no reversible factor has length \(a^2+3a\) or greater.

For sharpness, the context \(BA^aC\) occurs in \(G_3\) by (1). Its prefix \(BA^{a-1}A\) yields the explicit palindromic factor
\[
P_a=0^a1(0^{a+1}1)^{a-1}0^a,
\qquad |P_a|=a^2+3a-1.
\]
This proves \(T(a)=a^2+3a\) for \(a\ge4\).

### The exceptional parameter \(a=3\)
A finite localization lemma makes an exhaustive small certificate sufficient. For any \(a\ge2\), \(j\ge1\), and \(n\le|W_j|\), **every length-\(n\) factor of \(c_a\) already occurs in \(W_{j+1}\)**: at higher levels the word decomposes into copies of \(W_j\), separated by either nothing or one symbol \(1\). A length-\(n\) factor can meet at most one such boundary, and both boundary templates \(W_jW_j\) and \(W_j1W_j\) appear in \(W_{j+1}=W_j^a1W_j\). This proves the lemma, not merely a sampling assertion.

For \(a=3\), the exact iterates have \(|W_2|=21\), \(|W_3|=85\). Hence every length-\(19\) factor occurs in \(W_3\). Exhaustive enumeration of its \(85-19+1=67\) candidate windows yields precisely \(37\) distinct factors, none paired with its reversal, including no palindrome. The complete set and the containing word \(W_3\) are embedded in `a3_certificate.json`; the standalone `verify.py` reconstructs both and checks all reverse comparisons. Any longer factor and its reversal would contain a length-\(19\) reversed pair, so all lengths \(n\ge19\) are excluded. Conversely,
\[
010000100001000010
\]
is an explicit length-\(18\) palindrome in \(W_3\). Hence \(T(3)=19\).

## Verification
Run `python3 verify.py` beside `a3_certificate.json` using only the Python standard library. The program recomputes the finite certificate from the defining recurrence and also checks gap grammar and short cutoff predictions for independent parameter samples. The exact length-\(19\) case is exhaustive for the *infinite* word because the proved localization lemma uses \(|W_2|=21\). Finite checks for \(a\ge4\) are corroboration only; equations (1)--(5) and the displayed palindrome prove that infinite parametric family.

## Relationship to prior work
Allouche, Campbell, Shallit and Stipulanti introduced reflection complexity and explicitly treated the classical Chacon morphism \(0\mapsto0010,1\mapsto1\), observing equality of reflection and factor complexity from length \(13\) onward [1, §9]. Allouche, Baake, Cassaigne and Damanik had earlier established absence of palindromes of length at least \(13\) for that same classical morphism [2, §5]. Neither inspected Chacon statement treats the family of morphisms \(0\mapsto0^a10\) for varying \(a\), nor gives the sharp quadratic cutoff. Rampersad and Shallit established the existence and limitations of binary words avoiding reversed subwords [3]; their theorem does not determine the threshold of these fixed points. The principal novelty here is the exact all-parameter \(a\ge3\) classification and its gap-context mechanism, rather than the previously known \(a=2\) case.

## Limitations
The theorem concerns absence of factors together with their literal reversal; it does not give a complete closed form for \(\rho_{c_a}(n)\) or for \(r_{c_a}(n)\) at smaller lengths. No assertion of uniqueness against all unpublished or unindexed literature is made. The smaller cutoff at \(a=3\) uses an exhaustive, explicitly localized finite certificate instead of the coarser all-parameter gap estimate. No independent external validation has been performed.

## References
[1] J.-P. Allouche, J. M. Campbell, J. Shallit, M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302v1, first posted 2024-06-13. https://arxiv.org/abs/2406.09302

[2] J.-P. Allouche, M. Baake, J. Cassaigne, D. Damanik, *Palindrome complexity*, arXiv:math/0106121v1, first posted 2001-06-14. https://arxiv.org/abs/math/0106121

[3] N. Rampersad, J. Shallit, *Words avoiding reversed subwords*, arXiv:math/0311121, first posted 2003-11-07; Journal of Combinatorial Mathematics and Combinatorial Computing 54 (2005), 157--164. https://arxiv.org/abs/math/0311121
