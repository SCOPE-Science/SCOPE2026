# Sharp longest-unbordered-factor law for binary two-marker words

## Finding

A *border* of a nonempty word is a nonempty proper prefix that is also a suffix. A word with no border is *unbordered*. Write \(U(w)\) for the maximum length of an unbordered contiguous factor of \(w\).

**Theorem.** For every triple of integers \(a,b,c\geq0\), put
\[
w=0^a1\,0^b1\,0^c,\qquad M=\max(a,c),\qquad n=a+b+c+2.
\]
Then
\[
\boxed{U(w)=\begin{cases}b+M+2,&M>b,\\b+1,&M\leq b.\end{cases}}
\tag{1}
\]
Thus the longest-unbordered-factor length is determined by a sharp comparison between the middle zero gap and the larger outer zero gap.

The complete finite-length distribution is encoded in the following bivariate rational generating function:
\[
F(z,t)=\sum_{a,b,c\geq0}z^{a+b+c+2}t^{U(0^a1\,0^b1\,0^c)}=F_0(z,t)+F_1(z,t),
\]
where, with \(q=zt\),
\[
F_0(z,t)=\frac{z^2t}{(1-z)^2}\left(\frac1{1-q}-\frac{2z}{1-zq}+\frac{z^2}{1-z^2q}\right),
\tag{2}
\]
\[
F_1(z,t)=\frac{q^2}{1-z}\left(\frac{2q}{(1-q)(1-q^2)}-\frac{(1+z)zq}{(1-zq)(1-zq^2)}\right).
\tag{3}
\]
In particular, writing \(H_n=\sum_{|w|=n,\,|w|_1=2}U(w)\), one has
\[
\sum_{n\geq2}H_nz^n=\frac{z^2(1+8z+16z^2+22z^3+19z^4+11z^5+3z^6)}{(1-z^2)^2(1-z^3)^2}.
\tag{4}
\]

Choose uniformly from the \(\binom n2\) binary words of length \(n\) with exactly two ones and put \(X_n=U(w)/n\). Then \(X_n\) converges in distribution to a random variable \(X\) with the **exact limiting cumulative distribution**
\[
\Pr(X\leq x)=
\begin{cases}
0,&x\leq\tfrac13,\\
(3x-1)^2/3,&\tfrac13\leq x\leq\tfrac12,\\
3(x-\tfrac13)^2,&\tfrac12\leq x\leq\tfrac23,\\
2x-1,&\tfrac23\leq x\leq1,\\
1,&x\geq1.
\end{cases}
\tag{5}
\]
Consequently,
\[
\lim_{n\to\infty}\frac{1}{n\binom n2}\sum_{|w|=n,\,|w|_1=2}U(w)
=\mathbb E[X]=\frac{20}{27}.
\tag{6}
\]
In the limit, two-thirds of the words have normalized longest-unbordered-factor length at least \(2/3\), and their normalized lengths have constant density \(2\) on \([2/3,1]\).

## Assumptions and scope

Words are finite, linear, binary, and contain **exactly two** ones. The zero gaps \(a,b,c\) are nonnegative, so adjacent ones and ones at the endpoints are included. The word length is at least \(2\). Factors are contiguous, including one-letter factors. The empty word is not counted as a factor. All generating functions are identities of formal power series about the origin; the limiting distribution concerns uniform fixed-weight-two words, not uniform unrestricted binary words.

## Proof

**1. Structure of possible unbordered factors.** Any factor with no ones and length exceeding one has the border \(0\). A factor with exactly one one has the form \(0^i1\,0^j\). If both \(i\) and \(j\) are positive, its first and last letters agree, giving a one-letter border. Otherwise it is unbordered, since each nonempty proper prefix and suffix of equal length differ either at an endpoint or in their number of ones. Hence the longest unbordered factor containing exactly one one has length
\[
1+\max(a,b,c).
\tag{7}
\]

An unbordered factor containing both ones cannot have equal first and last letters. Consequently, it must have one of the forms
\[
0^i1\,0^b1\quad(1\leq i\leq a),
\qquad
1\,0^b1\,0^j\quad(1\leq j\leq c).
\tag{8}
\]
The first form is bordered when \(i\leq b\), because \(0^i1\) occurs as both prefix and suffix. When \(i>b\), it is unbordered: every nonempty proper suffix with only its final one has the form \(0^k1\), with \(k\leq b<i\), so its same-length prefix is all zeros; any proper suffix containing both ones cannot match its prefix, which omits the final one. The reversed argument shows that the second form is unbordered exactly when \(j>b\). Thus a two-one unbordered factor exists exactly when \(M>b\), and its greatest possible length is \(M+b+2\). In this case it is longer than (7). When \(M\leq b\), no two-one factor is unbordered and (7) becomes \(b+1\). This establishes (1), including equality at the threshold and all zero-gap boundaries.

**2. Exact rational generating function.** In the regime \(a,c\leq b\), formula (1) contributes
\[
\sum_{b\geq0} z^{b+2}t^{b+1}\left(\sum_{j=0}^b z^j\right)^2
=F_0(z,t),
\]
using three geometric series. In the complementary regime, write \(M=\max(a,c)>b\) and \(m=\min(a,c)\). For each \(0\leq m<M\) there are two ordered outer-gap pairs; for \(m=M\) there is one. Their weighted sum is
\[
\sum_{m=0}^{M}(2-\mathbf1_{m=M})z^m
=\frac{2-(1+z)z^M}{1-z}.
\]
Multiplying by \(z^{M+b+2}t^{M+b+2}\), then summing over \(b\geq0\) and \(M\geq b+1\), gives (3) via geometric series in \(q\) and \(zq\). Thus (2)--(3) account for every admissible triple exactly once. Differentiating \(F(z,t)\) with respect to \(t\) and setting \(t=1\) yields (4) by rational simplification.

**3. Limiting law.** Uniform integer compositions \(a+b+c=n-2\), divided by \(n\), converge in distribution to the uniform probability measure (constant area density \(2\)) on the simplex \(\{(A,B,C):A,B,C\geq0,\ A+B+C=1\}\). Outside the zero-area boundary \(B=\max(A,C)\), (1) gives the limiting statistic
\[
X=\begin{cases}B,&B\geq\max(A,C),\\1-\min(A,C),&B<\max(A,C).\end{cases}
\tag{9}
\]
The boundary does not alter weak convergence.

The event \(X\leq x\) splits into the disjoint regimes in (9). Exchangeability of \(A,B,C\) and inclusion--exclusion give
\[
\Pr(B\geq\max(A,C),\ B\leq x)
=\frac13\left[1-3(1-x)_+^2+3(1-2x)_+^2-(1-3x)_+^2\right]
\quad(0\leq x\leq1),
\tag{10}
\]
where \(y_+=\max(y,0)\). For the second regime put \(s=1-x\). The event \(\min(A,C)\geq s\) has probability \((1-2s)_+^2\). Its intersection with \(B\geq\max(A,C)\) is empty for \(s>1/3\); for \(0\leq s\leq1/3\), translating \(A,C\) by \(s\) leaves the polygon
\[
A',C'\geq0,\qquad 2A'+C'\leq1-3s,\qquad A'+2C'\leq1-3s.
\]
This polygon has area \((1-3s)^2/6\), hence probability \((1-3s)^2/3\) under simplex density \(2\). Subtracting it gives
\[
\Pr(B<\max(A,C),\ 1-\min(A,C)\leq x)
=(2x-1)_+^2-\tfrac13(3x-2)_+^2
\quad(0\leq x\leq1).
\tag{11}
\]
Adding (10) and (11), and simplifying on the intervals with breakpoints \(1/3,1/2,2/3,1\), gives (5). Integrating its piecewise density gives \(\mathbb E[X]=20/27\). Since \(0\leq X_n\leq1\), weak convergence also yields convergence of expectations, proving (6).

## Verification

The standalone standard-library program `verify.py` compares formula (1) against direct border testing of every factor of every two-one word of lengths \(2\) through \(23\) (\(2024\) words). It independently expands the six rational terms in (2)--(3), checking all bivariate coefficients through degree \(48\) against exhaustive gap enumeration. It separately compares length-\(500\) empirical cumulative probabilities at five thresholds and the normalized mean with (5)--(6). To reproduce: `python3 verify.py` from the directory containing this document. All assertions must succeed and the program must print `CHECKS_OK`. Finite computations are corroboration, not the proof of the universal or asymptotic statements.

## Relationship to prior work

Kucherov, Loptev, and Starikovskaya (2015) study the longest unbordered factor for general words, proving unrestricted-alphabet expectation bounds and a general algorithm; their results do not specify this fixed-weight-two distribution. Sekizaki and Mieno (2025, revised 2026) show that longest unbordered factors are bounded by complete runs in a run-length encoding and give general compressed-string algorithms. Their general procedure can compute the statistic on the present family, but it does not state (1)--(6) or the limiting distribution. The structural formula and its exact and asymptotic enumeration are the contribution here; no general algorithmic breakthrough or unrestricted-alphabet improvement is asserted.

## Limitations

Only words containing exactly two ones are classified. The binary alphabet is fixed; the result is not a statement about arbitrary sparse alphabets, periodic infinite sequences or cyclic factors. Equations (5)--(6) are asymptotic statements for the specified fixed-weight model; they do not replace finite-length coefficients of (2)--(3). An equivalent earlier classification under different terminology cannot be excluded by a non-exhaustive literature search. No independent audit has been performed.

## References

1. G. Kucherov, A. Loptev, T. Starikovskaya, *On Maximal Unbordered Factors*, arXiv:1504.07406v1 (first posted 28 April 2015), especially Sections 1, 3--5. https://arxiv.org/abs/1504.07406
2. S. Sekizaki and T. Mieno, *Algorithms for Computing Longest Unbordered Factors on Run-Length Encoded Strings*, arXiv:2507.16285v2 (originally posted 22 July 2025; version inspected dated 20 October 2026), especially Section 3, Lemma 3. https://arxiv.org/abs/2507.16285
