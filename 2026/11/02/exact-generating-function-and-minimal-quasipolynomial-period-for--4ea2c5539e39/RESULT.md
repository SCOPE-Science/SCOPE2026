# Exact generating function and minimal quasipolynomial period for seven-one prefix-normal words

## Finding

Let \(P_7(n)\) denote the number of binary prefix-normal words of length \(n\) containing exactly seven occurrences of \(1\). Then the **exact generating function for every \(n\ge0\)** is

\[
\boxed{\displaystyle \sum_{n\ge0}P_7(n)z^n=
 \frac{z^7 A(z)}{(1-z)(1-z^3)(1-z^4)^2(1-z^6)^3},}
\]

where \(A(z)=\sum_{j=0}^{18}a_j z^j\) has ascending coefficient vector

```text
(1, 3, 9, 17, 35, 48, 76, 85, 108, 103, 108, 85, 76, 48, 35, 17, 9, 3, 1).
```

In particular, as \(n\to\infty\),

\[
P_7(n) \sim \frac{289}{3456}\binom{n-1}{6}.
\]

Moreover, \(P_7(n)\) agrees (for sufficiently large \(n\), in fact for all \(n\) with a suitable quasipolynomial expression) with a degree-six quasipolynomial of **minimal period twelve**. The first positive coefficients \(P_7(7),\ldots,P_7(21)\) are

```text
1, 4, 13, 31, 71, 134, 249, 417, 688, 1062, 1628, 2367, 3430, 4781, 6632.
```

## Assumptions and scope

The alphabet is \(\{0,1\}\), a *factor* is a contiguous substring, and \(w\) is *prefix normal* if every factor of length \(\ell\) has at most as many ones as the first \(\ell\) letters, for all \(1\le\ell\le |w|\). Exactly seven ones are required; words shorter than seven contribute zero. Positions are indexed starting at one. Every counted word begins in a one. The seven one positions are \(1=x_1<x_2<\cdots<x_7\), and the six positive successive gaps are \(g_i=x_{i+1}-x_i\). There may be an arbitrary nonnegative number \(t\) of trailing zeros.

## Proof

**1. Gap criterion.** For any \(r\in\{1,\ldots,6\}\), the shortest factor containing a given consecutive block of \(r+1\) ones has length \(1+\sum_{j=i}^{i+r-1}g_j\). The prefix reaches \(r+1\) ones at length \(1+\sum_{j=1}^r g_j\). Therefore prefix normality is *equivalent* to

\[
\sum_{j=i}^{i+r-1}g_j\ge\sum_{j=1}^r g_j
\quad(1\le r\le6,\ 1\le i\le7-r).
\tag{1}
\]

Indeed, if a block were shorter, that block would violate the corresponding prefix length; conversely, if all blocks are at least as long as their initial counterpart, no factor with \(r+1\) ones can appear at a length before the prefix first contains \(r+1\) ones. This equivalence treats *all factor lengths* and includes the boundary cases \(r=1,6\).

**2. Five-variable cone.** Write \(a=g_1\ge1\) and

\[
(g_1,g_2,g_3,g_4,g_5,g_6)
=(a,a+b,a+c,a+d,a+e,a+f),
\]

where \(b,c,d,e,f\ge0\). Expanding (1) for \(r=1,\ldots,6\) and discarding tautological inequalities leaves exactly

\[
c+d\ge b,\quad d+e\ge b,\quad e+f\ge b,\quad d+e+f\ge b+c. \tag{2}
\]

The total length is \(1+6a+b+c+d+e+f+t\). Put

\[
H(z)=\sum_{\substack{b,c,d,e,f\ge0\\c+d,\ d+e,\ e+f\ge b\\d+e+f\ge b+c}}
 z^{b+c+d+e+f}.
\]

Every solution determines precisely one word per \(a\ge1\) and trailing-zero count \(t\ge0\), hence

\[
\sum_{n\ge0}P_7(n)z^n=\frac{z^7H(z)}{(1-z)(1-z^6)}.\tag{3}
\]

**3. Rational summation.** Partition (2) into \(d\ge b\) and \(d<b\). In the first region let \(d=b+u\), \(s=e+f\). The only further constraints are \(s\ge b\), \(0\le c\le u+s\). Because there are \(s+1\) choices for \((e,f)\), elementary geometric summation gives

\[
H_{\ge}(z)=\frac{1}{(1-z)(1-z^2)}\left[
\frac{1}{1-z}\left(\frac{1}{(1-z)^2}-\frac{z^2}{(1-z^3)^2}\right)
-\frac{1}{1-z^2}\left(\frac{z}{(1-z^2)^2}-\frac{z^3}{(1-z^4)^2}\right)\right].\tag{4}
\]

In the second region set \(b=d+v\), \(e=v+u\), \(c=v+h\) for \(v\ge1\) and \(u,h\ge0\), and let \(s=u+f\). Conditions (2) become \(s\ge\max(d,v)\) and \(0\le h\le s-v\). For fixed \(s\), there are \(s+1\) choices of \((u,f)\). Define the following *explicit rational functions* (the symbol \(q\) is a formal indeterminate, with \(z\) independent):

\[
\Phi(x,q)=\frac{x(2-x-q)}{(1-x)^2},
\]

\[
U_r(q)=\frac{\Phi(z^r q,q)-z^2\Phi(z^{r+2}q,q)}{(1-z^2)(1-q)^2}
+\frac{z^r\Phi(z^2q,q)-\Phi(z^{r+2}q,q)}{(1-z^r)(1-q)^2}.
\]

The identity \(\sum_{s\ge m}(s+1)q^s=q^m((m+1)-mq)/(1-q)^2\), together with a split into \(d\le v\) and \(d>v\), now yields

\[
H_{<}(z)=\frac{U_3(z)-zU_2(z^2)}{1-z}.\tag{5}
\]

Cross-multiplication of the explicit rational expressions (4) and (5) simplifies to the *exact polynomial identity*

\[
H_{\ge}(z)+H_{<}(z)=\frac{A(z)}{(1-z^3)(1-z^4)^2(1-z^6)^2}.\tag{6}
\]

An executable **integer-polynomial cross-product check** of (6) appears in `verify.py`; it verifies the complete rational identity and is not a finite-coefficient heuristic. Equations (3) and (6) prove the boxed formula for all \(n\ge0\).

**4. Leading asymptotic and period.** Since \(A(1)=867\), the pole at \(z=1\) is of order seven and has leading coefficient
\(867/(3\cdot4^2\cdot6^3)=289/3456\). Every other pole has order at most five, proving the stated asymptotic. All poles are twelfth roots of unity, so the coefficient sequence is quasipolynomial with period dividing twelve. Because \(A(z)\equiv z\pmod{z^2+1}\) and \(A(z)\equiv1\pmod{z^2-z+1}\), primitive fourth- and sixth-root poles survive. Their orders force any quasipolynomial period to be divisible by four and six, respectively; hence the minimal period is twelve.

## Verification

Execute `python3 verify.py` from a directory containing the standalone verification script. It checks: (i) the exact all-degree rational-function identity (6), by polynomial cross-products in integer arithmetic with no symbolic algebra dependency; (ii) direct factor checking and the complete gap criterion for all \(75,582\) seven-one words of lengths seven through eighteen; (iii) an independent five-variable cone enumeration for lengths seven through twenty-nine against the generating-function coefficients. The recorded output is in `verification_output.txt`. These finite tests corroborate rather than replace the argument for all lengths.

## Relationship to prior work

Burcsi, Fici, Lipták, Ruskey and Sawada established rationality for each fixed one-count and explicitly derived generating functions through density six (Proposition 16), while reporting that their list did not extend beyond six. The displayed density-seven rational function is the immediately next natural explicit case; it is not claimed that rationality itself is new. Adamson, Dudey, Fleischmann and Huch study prefix-normal word-chain generation in 2025 and describe enumeration as an active question, but their chain framework does not provide this density-seven formula. The comparison concerns exact statements, not just matching titles or keywords.

## Limitations

Only binary words with precisely seven ones are classified. No closed generating function for arbitrary density, no complexity improvement for general prefix-normal enumeration, and no independently verified publication priority are claimed. The numerator and denominator are exact, but they do not immediately settle all-density enumeration. An unindexed or inaccessible equivalent prior calculation remains a priority risk. Independent mathematical audit has not been performed.

## References

1. P. Burcsi, G. Fici, Z. Lipták, F. Ruskey, J. Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017 (first posted 2016-11-28), especially §4.2 and Proposition 16. https://arxiv.org/abs/1611.09017
2. D. Adamson, M. Dudey, P. Fleischmann, A. Huch, *Word Chain Generators for Prefix Normal Words*, arXiv:2508.19619v1 (first posted 2025-08-27), especially §3–4. https://arxiv.org/html/2508.19619v1
3. Y. Eikmeier, P. Fleischmann, M. Kulczynski, D. Nowotka, *Weighted Prefix Normal Words: Mind the Gap*, arXiv:2005.09281 (first posted 2020). https://arxiv.org/abs/2005.09281
