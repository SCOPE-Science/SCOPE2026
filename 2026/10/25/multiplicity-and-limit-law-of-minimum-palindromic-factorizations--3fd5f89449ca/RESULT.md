# Multiplicity and limit law of minimum palindromic factorizations in five-run binary words

## Finding

For positive integers \(a,b,c,d,e\), put
\[
w=0^a1^b0^c1^d0^e.
\]
A palindromic factorization is a decomposition into **nonempty contiguous palindromes**. Write \(\operatorname{PL}(w)\) for the least possible number of parts and \(K(w)\) for the number of factorizations attaining that minimum, where two factorizations are distinct precisely when their sets of cut positions differ. The following formulas determine **both** quantities, without exceptional or asymptotic hypotheses.

If \(b=d\), then
\[
(\operatorname{PL}(w),K(w))=
\begin{cases}
(1,1),&a=e,\\
(2,1+\mathbf 1_{c=a+e}),&a\ne e.
\end{cases}
\]
For \(b\ne d\), put
\[
q=\mathbf 1_{c=a}+\mathbf 1_{c=e}
+\mathbf 1_{e<c<a+e}
+\mathbf 1_{a<c<a+e}
+\mathbf 1_{c>a+e}.
\]
Then
\[
(\operatorname{PL}(w),K(w))=
\begin{cases}
(2,1),&c=a+e,\\
(4,c+2),&c<\min(a,e),\\
(3,q),&\text{otherwise}.
\end{cases}
\]
In the last case \(q\) is necessarily either \(1\) or \(2\).

In particular, \(K(w)>2\) holds **exactly** when \(b\ne d\) and \(c<\min(a,e)\). By contrast, every binary word with at most four nonempty constant runs has at most two minimum palindromic factorizations. Thus **five is the first run count allowing unbounded optimal-factorization multiplicity**.

For length \(n\), the largest value of \(K(w)\) over the five-run family is \(1\) at \(n=5\), is \(2\) at \(n=6,7\), and is \(2+\lfloor(n-5)/3\rfloor\) for every \(n\ge8\).

Let \(J_{n,k}\) count the five-run words of length \(n\) beginning in zero with exactly \(k\ge3\) minimum factorizations. Their complete bivariate generating function is
\[
\boxed{\sum_{n\ge5}\sum_{k\ge3} J_{n,k}z^nv^k
=\frac{2z^8v^3}{(1-z)^3(1-z^2)(1-z^3v)}.}
\]
Equivalently, for \(m\ge1\), \(n\ge3m+5\),
\[
J_{n,m+2}=2\sum_{j=0}^{\lfloor(n-3m-5)/2\rfloor}
\binom{n-3m-3-2j}{2},
\]
with zero count below that threshold.

Choose the positive five-part composition of \(n\) uniformly, and let \(K_n\) be the resulting \(K(w)\). Then \(K_n/n\) converges in distribution to a nonnegative variable \(X\) with mass \(2/3\) at zero and density
\[
\boxed{f_X(t)=4(1-3t)^3\quad(0<t<1/3).}
\]
In particular, \(\Pr(K_n\ge3)\to1/3\), and \(\mathbb E[K_n]=n/45+O(1)\). Conditionally on \(K_n\ge3\), the limit has law \(\tfrac13\operatorname{Beta}(1,4)\).

## Assumptions and scope

The alphabet is ordered only for notation; interchanging zero and one does not change the statements. A **run** is a maximal nonempty contiguous constant block, and all five displayed parameters are strictly positive. A cut is between two consecutive positions. Palindrome factors are allowed to have length one. Multiplicity is of positional optimal partitions, not of distinct strings occurring as factors, nor of all nonoptimal partitions. For the distribution, all \(\binom{n-1}{4}\) positive compositions are equally likely. Every exact statement holds over the entire specified positive-integer domain.

## Proof

**Transition accounting.** The word has exactly four alternating symbol transitions. Each palindrome has an even number of transitions, since reversing a palindrome must reverse the transitions in symmetric pairs. A palindrome containing all four transitions must contain both complete one-runs, so necessarily \(b=d\). A two-transition palindrome spans two *consecutive* transitions; its possible center is the first one-run, the central zero-run, or the second one-run. In the first and third cases the palindrome has pattern \(0^s1^b0^s\) or \(0^s1^d0^s\); in the middle case it has pattern \(1^s0^c1^s\).

**One and two parts.** The whole five-run word is a palindrome exactly when \(a=e,b=d\). Suppose it is not. A two-part palindromic decomposition either has a four-transition palindrome and a zero-only factor, or it has two two-transition palindromes, or its cut lies at a transition so that one part is unary and the other has four transitions. The latter cases cannot add anything beyond trimming a zero-only excess at an extreme when \(b=d\). Such trimming yields exactly one cut unless a second, two-transition-plus-two-transition split occurs. The only such split occurs in the central zero-run, with its left fragment equal to \(a\) and its right fragment equal to \(e\); hence its necessary and sufficient condition is \(c=a+e\). Consequently, when \(b=d\) but \(a\ne e\), there are \(1+\mathbf1_{c=a+e}\) minimum two-part factorizations. When \(b\ne d\), there is no four-transition palindrome, and precisely one two-part decomposition exists when \(c=a+e\).

**Three parts.** Assume \(b\ne d\) and \(c\ne a+e\), so one or two parts are impossible. With three palindromic factors, the four transitions must be distributed among palindrome interiors in one of two ways. If exactly two transitions lie at factor boundaries, the other two occur in one two-transition palindrome and the two other parts are constant. Pairing the first two, middle two, or last two transitions is possible respectively only when \(c=a\), \(b=d\), or \(c=e\). The middle option is excluded here. In the other possibility, no transition lies at a cut: two two-transition palindromes cover the first and last transition pairs, with the remaining factor constant. According to whether this constant part precedes, separates, or follows the two palindromes, the exact conditions are \(e<c<a+e\), \(c>a+e\), or \(a<c<a+e\). Each admissible condition fixes all cuts uniquely.

To see the constructions explicitly, the five respective cuts for \(c=a\), \(c=e\), \(e<c<a+e\), \(a<c<a+e\), and \(c>a+e\) are displayed below, with bars denoting factors:
\[
\begin{aligned}
&0^a1^b0^a\;|\;1^d\;|\;0^e,\\
&0^a\;|\;1^b\;|\;0^e1^d0^e,\\
&0^{a+e-c}\;|\;0^{c-e}1^b0^{c-e}\;|\;0^e1^d0^e,\\
&0^a1^b0^a\;|\;0^{c-a}1^d0^{c-a}\;|\;0^{a+e-c},\\
&0^a1^b0^a\;|\;0^{c-a-e}\;|\;0^e1^d0^e.
\end{aligned}
\]
The strict inequalities guarantee all three factors are nonempty in the last three displays. These five types exhaust the three-part possibilities; their indicators sum to \(q\). When \(c<\min(a,e)\), none is available; otherwise (with the present exceptions excluded) at least one is available. At most two conditions can hold simultaneously, so \(q\in\{1,2\}\) in the stated domain.

**Four parts.** If \(b\ne d\) and \(c<\min(a,e)\), a four-part factorization exists:
\[
0^a\;|\;1^b\;|\;0^c1^d0^c\;|\;0^{e-c}.
\]
Exactly zero or two of the four transitions may lie on its three cuts, because the number remaining inside palindromic factors must be even. With zero transition cuts, the first and last two transitions must be paired within distinct three-run palindromes. This requires a split of the middle zero-run into two positive pieces, with \(c-1\) choices; the other two parts are the nonempty exterior zero runs. With two transition cuts, there is one two-transition palindrome and three unary factors. Its paired transitions may be the first two, the middle two, or the last two, and each case fixes the cuts; all three are feasible. These cases are disjoint and exhaustive. Therefore the minimum is four and its multiplicity is \((c-1)+3=c+2\).

**First run-count threshold and maximum.** A binary word with one, two, or three runs has a unique minimum palindromic partition (or its whole word is a palindrome). For a four-run word \(0^a1^b0^c1^d\), the minimum is two when \(a=c\) or \(b=d\), and its multiplicity is exactly \(\mathbf1_{a=c}+\mathbf1_{b=d}\): a split into two palindromes must be either \(0^a1^b0^a\;|\;1^d\) or \(0^a\;|\;1^b0^c1^b\). If both equalities fail, the minimum is three, with exactly two possible decompositions: one uses a two-transition palindrome centered on the first one-run and zero/one unaries to its left or right depending on the comparison of \(a,c\); the other similarly uses the palindrome centered on the zero-run with exterior unaries depending on the comparison of \(b,d\). The transition pairing excludes all further cases. Thus the multiplicity is at most two in every four-run word. For five runs, the only case with multiplicity above two has \(c<\min(a,e)\), forcing \(a,e\ge c+1\), while distinct positive one-run lengths force \(b+d\ge3\). Hence \(n\ge3c+5\), so \(c\le\lfloor(n-5)/3\rfloor\). Conversely, whenever \(n\ge8\), choose \(c\) at that bound, \(a,e\ge c+1\), and \(b\ne d\) with the remaining positive length allocated to the run lengths; the bound is attained. The small cases follow directly.

**Enumeration.** In the regime \(K=c+2\), write \(a=c+\alpha\), \(e=c+\beta\), where \(c,\alpha,\beta\ge1\); independently \(b,d\ge1\), \(b\ne d\). The two distinct orderings of \(b,d\) contribute
\[
\sum_{b,d\ge1,\ b\ne d}z^{b+d}
=\frac{2z^3}{(1-z)(1-z^2)}.
\]
The independent positive shifts \(\alpha,\beta\) contribute \(z^2/(1-z)^2\); the central variable contributes \(\sum_{c\ge1}z^{3c}v^{c+2}=z^3v^3/(1-z^3v)\). Multiplication gives the announced bivariate generating function. Expanding \((1-z)^{-3}\), \((1-z^2)^{-1}\) and \((1-z^3v)^{-1}\) gives the coefficient formula.

**Limit law.** The vector \((a,b,c,d,e)/n\) of a uniform positive composition tends to the uniform Dirichlet law on the simplex \(\{(A,B,C,D,E)>0:A+B+C+D+E=1\}\). The condition \(b\ne d\) fails with probability \(O(1/n)\). Away from boundaries, \(K_n/n\) therefore tends to \(C\) when \(C<\min(A,E)\), and to zero otherwise. For \(0<t<1/3\), fixing \(C=t\) and substituting \(A'=A-t\), \(E'=E-t\) leaves four positive coordinates with total \(1-3t\). The Dirichlet density is \(24\); the cross-sectional simplex has volume \((1-3t)^3/6\). Thus the positive part of the limiting law has density \(4(1-3t)^3\). Its integral is \(1/3\), leaving mass \(2/3\) at zero. Its first moment is
\[
\int_0^{1/3}4t(1-3t)^3\,dt=\frac1{45}.
\]
The bivariate rational generating function gives \(\sum K(w)=\frac{1}{45}n\binom{n-1}{4}+O(n^4)\) over the \(K\ge3\) regime; elsewhere \(K\le2\), so \(\mathbb E[K_n]=n/45+O(1)\).

## Verification

The standalone program `verification/check.py` computes \((\operatorname{PL},K)\) independently by dynamic programming over every substring, testing palindromicity character by character and adding counts for all minimum-cost predecessor cuts. It compared all \(6^5=7776\) tuples with parameters from 1 through 6, another 400 larger seeded tuples, and the exact generating-function coefficients and finite-length maxima for \(5\le n\le30\). Successful output is recorded in `VERIFICATION.md`. These finite checks corroborate but do **not** replace the transition-based proof and exact generating-function calculations.

## Relationship to prior work

The classical palindromic-length problem and algorithms compute minimum palindrome decompositions for unrestricted words; here the object is **the number of distinct optimal cut sets** for a specific complete run-structured family, plus its sharp extremum and distribution. Rukavicka (2020) studies palindromic lengths of infinite words with periodic-palindrome structure, not this positional-multiplicity law. Rubinchik and Shur (2020) give efficient algorithms for fixed-\(k\) palindromic factorization and reconstruct a factorization. Borchert and Rampersad (2015) study palindrome-pair factors and minimal non-palindrome pairs; their classifications supply relevant context for the two-part threshold, not the five-run multiplicity distribution. An earlier five-run palindromic-defect classification concerns the number of **distinct palindromic factors**, a different invariant, and does not imply the count of optimal palindromic partitions. The present result does not claim priority for general palindromic-factorization algorithms or for the mere characterization of palindrome pairs.

## Limitations

The classification applies to binary words with exactly five nonempty constant runs; the limiting law is for a uniform composition of those run lengths, not for a uniformly sampled unrestricted binary word. The factors must be contiguous palindromes and the optimization is minimum number of factors. The result does not characterize six-run or more general words. Exhaustive checks cover finite cases and are not infinite proofs. The literature comparison includes several complete directly relevant accessible articles, but logically equivalent specializations in other work cannot be ruled out by bibliographic searches alone. Independent external audit has not been performed.

## References

- J. Rukavicka, *Palindromic Length of Words with Many Periodic Palindromes* (first public 2020-05-04), arXiv:2005.01371, https://arxiv.org/abs/2005.01371 .
- M. Rubinchik and A. M. Shur, *Palindromic k-Factorization in Pure Linear Time* (2020), arXiv:2002.03965, https://arxiv.org/abs/2002.03965 .
- A. Borchert and N. Rampersad, *Words with Many Palindrome Pair Factors* (2015), arXiv:1509.05396, https://arxiv.org/abs/1509.05396 .
- J. Rukavicka, *Palindromic factorization of rich words* (2021), arXiv:2110.13078, https://arxiv.org/abs/2110.13078 .
