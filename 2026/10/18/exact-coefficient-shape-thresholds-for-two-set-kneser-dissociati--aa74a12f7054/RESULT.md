# Exact coefficient-shape thresholds for two-set Kneser dissociation polynomials

## Finding

For the Kneser graph \(K(n,2)\), \(n\ge4\), let \(D_n(z)=\sum_{k\ge0}a_{n,k}z^k\) count vertex sets inducing maximum degree at most one, including the empty set. The coefficient sequence from its constant term through its leading coefficient is strictly log-concave exactly for \(4\le n\le12\). Ordinary log-concavity also fails for all \(n\ge13\). The sequence is unimodal exactly when \(n\ne14\). At order fourteen the three consecutive coefficients in degrees four through six are \(25025,24024,25025\).

## Assumptions and scope

The vertices are the two-element subsets of the labeled set \([n]\), and adjacency means disjointness. Strict log-concavity means \(a_{n,k}^2>a_{n,k-1}a_{n,k+1}\) at every internal index; ordinary log-concavity allows equality. A unimodal sequence weakly increases up to a mode and then weakly decreases. The result is about the coefficient shape of the all-set polynomial, not the enumeration of inclusion-maximal sets or higher-rank Kneser graphs.

## Counting input

Use the formula
\[
D_n(z)=1+\binom n2 z+n\big((1+z)^{n-1}-1-(n-1)z\big)+\binom n3 z^3+\binom n4\big((1+z)^6-(1+2z)^3\big).
\]
The formula is not claimed as a distinct contribution. A pairwise intersecting selected family with at least two pairs is contained in a unique star or is the three pairs of a triangle: after two pairs \(ab,ac\), a pair not through \(a\) must be \(bc\), and no fourth pair can meet all three. A selected family containing disjoint pairs \(ab,cd\) has each further pair meeting both, so is supported on those four labels. On the six pairs of that support the Kneser graph is a matching of three edges. All its subsets are dissociation sets, and the intersecting ones contribute \((1+2z)^3\); subtract these so that every counted nonintersecting family has a unique support. These cases give the input formula.

## Proof of the thresholds

Let \(W=\binom n4\). Expanding the formula, with \(\binom{n-1}{k}=0\) if \(k>n-1\), gives
\[
\begin{array}{c|cccccc}
k & 2 & 3 & 4 & 5 & 6 & 7\\ \hline
a_{n,k}/W & 3+12/(n-3) & 16+4/(n-3)& n+11 & (n^2-9n+50)/5 & (n^3-15n^2+74n-90)/30 & (n-4)(n-5)(n-6)(n-7)/210 .
\end{array}
\]
Here \(a_{n,0}=1\), \(a_{n,1}=\binom n2\), and \(a_{n,k}=n\binom{n-1}{k}\) for \(k\ge7\). The support is the full range \(0,\ldots,\max(6,n-1)\), with positive coefficients throughout.

For each \(n=4,\ldots,12\), subtracting consecutive coefficient products from the squared internal coefficients gives the following minimum determinants, in order:
\[
21,\ 55,\ 120,\ 231,\ 406,\ 666,\ 1035,\ 1540,\ 2211.
\]
These finite integer evaluations use the displayed coefficients through degree six and the binomial formula thereafter. For \(13\le n\le21\), the determinant at degree five equals \(W^2H_5(n)/150\), where
\[
H_5(n)=n^4-88n^3+1541n^2-9020n+19950.
\]
Indeed it is obtained by subtracting \((n+11)(n^3-15n^2+74n-90)/30\) from \(((n^2-9n+50)/5)^2\) and multiplying by \(W^2\). The successive values of \(H_5\) for \(13,\ldots,21\) are \(-1656,-7350,-15000,-24786,-36864,-51366,-68400,-88050,-110376\). For \(n\ge22\), the determinant at degree four equals \(-W^2H_4(n)/(5(n-3))\), where
\[
H_4(n)=11n^3-283n^2+921n-385.
\]
This follows by subtracting \((16+4/(n-3))(n^2-9n+50)/5\) from \((n+11)^2\). At \(n=22+s\) with \(s\ge0\), \(H_4(n)=11s^3+443s^2+4441s+33>0\). The determinants used are internal; their strict negativity rules out even ordinary log-concavity for all \(n\ge13\).

For \(4\le n\le13\), the same coefficients give unimodality with unique mode three at \(n=4,5,6\) and mode four at \(n=7,\ldots,13\). At \(n=14\), \(W=1001\), and the coefficients in degrees four, five and six are \(25W,24W,25W\), ruling out unimodality. For \(n\ge15\), the constant-to-linear difference is positive and
\[
a_{n,2}-a_{n,1}=n(n-3)(n-1)(n+2)/8>0.
\]
The next five consecutive differences, divided by \(W\), are respectively
\[
13-8/(n-3),\quad n-5-4/(n-3),\quad (n^2-14n-5)/5,
\]
\[
(n^3-21n^2+128n-390)/30,\quad (n^4-29n^3+284n^2-1156n+1470)/210.
\]
The first two are positive. Substituting \(n=15+s\) in the remaining numerators gives \(s^2+16s+10\), \(s^3+24s^2+173s+180\), and \(s^4+31s^3+329s^2+1289s+780\), respectively; all are positive for \(s\ge0\). Thus the coefficients strictly increase through degree seven. From degree seven onward they are a binomial tail, which is unimodal by the successive binomial ratios. This proves the classification.

## Verification and limitations

The finite determinant and mode tables can be reproduced by evaluating the displayed coefficients for the specified orders, taking all internal determinants, and comparing adjacent coefficients. The accompanying original enumeration script tests all subsets directly only for \(n=4,5,6,7\), and tests ordinary (not strict) log-concavity and unimodality of formula coefficients through \(500\). That bounded verification does not prove either all-order statement; the algebraic sign argument above does. There is no claim here for \(K(n,r)\) with \(r>2\).

## Relationship to known results

Brešar and Dravec, *On the dissociation number of Kneser graphs*, [arXiv:2108.10801](https://arxiv.org/abs/2108.10801), Proposition 2.1, prove the scalar extremum and use the four-label localization in the counting input. The Resultary entry [Dissociation polynomials and maximal-set purity of KG(n,2)](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-dissociation-polynomials-and-maximal-set-purity-of-kg-n-2--2b36dd2818f0) states an equivalent all-set polynomial and the complete inclusion-maximal-set polynomial. Equivalence of the quadratic terms follows from \(\binom{\binom n2}{2}=n\binom{n-1}{2}+3\binom n4\). The equivalent enumeration is credited regardless of precedence; no claim about relative discovery dates is made. The distinct question treated here is exactly when the coefficients satisfy either shape property. Neither the matching counting statement nor the scalar result classifies these transitions; the classifications require the coefficient inequalities above. This bounded comparison does not establish universal publication priority.
