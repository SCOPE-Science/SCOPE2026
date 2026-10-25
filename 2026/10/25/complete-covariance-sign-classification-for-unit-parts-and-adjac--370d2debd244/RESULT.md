# Complete covariance-sign classification for unit parts and adjacent equalities in uniform compositions

## Finding

For integers \(n\ge1\) and \(1\le k\le n\), choose uniformly among all ordered compositions \((X_1,\ldots,X_k)\) of \(n\) into \(k\) positive parts. Define
\[
U=\sum_{i=1}^{k}\mathbf 1\{X_i=1\},\qquad
A=\sum_{i=1}^{k-1}\mathbf 1\{X_i=X_{i+1}\}.
\]
The following list exhausts **all** possible signs of \(\operatorname{Cov}(U,A)\):

- It is **negative** precisely when \(n\) is even and either \(k=2\) with \(n\ge4\), or \(k=3\) with \(n\ge6\).
- It is **positive** precisely when either \(k=4\) and \(n\) is even with \(n\ge6\), or \(k\ge5\) and \(n\ge k+2\).
- It is **zero** in every other case.

In particular, for every even \(n\ge6\), changing the number of parts from three to four switches covariance from strictly negative to strictly positive. For odd \(n\), negative covariance never occurs, and \(k=4\) is a zero-covariance boundary.

There is an exact finite expression. For \(k\ge3\), put \(m=n-k\), \(D=\binom{n-1}{k-1}\), and for integer \(j\) let
\[
h_j^{(k)}=\begin{cases}
[z^j](1-z)^{-(k-3)}(1-z^2)^{-2},&j\ge0,\\
0,&j<0.
\end{cases}
\]
Then
\[
\boxed{\operatorname{Cov}(U,A)
=\frac{2(k-1)}{(n-1)D}
\left((k-3)h_{m-2}^{(k)}-h_{m-3}^{(k)}\right).}
\]
For \(k=2\) the covariance is \(-2/(n-1)^2\) at even \(n\ge4\), and zero otherwise; for \(k=1\) it is zero. Useful closed boundary cases are
\[
\operatorname{Cov}(U,A)=
\begin{cases}
-\dfrac{4(n-4)}{(n-1)^2(n-2)},&k=3,\ n\ge6\text{ even},\\[4pt]
\dfrac{18(n-4)}{(n-1)^2(n-2)(n-3)},&k=4,\ n\ge6\text{ even}.
\end{cases}
\]

## Assumptions and scope

The uniform law is over the \(\binom{n-1}{k-1}\) **ordered** positive-integer compositions, with fixed \(n\) and fixed \(k\). Equality in \(A\) is for **consecutive** parts only; the terminal and initial parts are not treated as neighbors. Unit parts are those of size exactly one. Covariance is ordinary unconditioned covariance under this fixed-\((n,k)\) uniform law. No approximation or limiting regime is assumed.

## Proof

Write \(Y_i=X_i-1\), so the vector \((Y_i)\) is uniformly chosen among the \(k\)-tuples of nonnegative integers of total \(m=n-k\). For \(k\ge3\), define the formal power series
\[
g(z)=(1-z)^{-(k-2)},\quad
f(z)=\frac{g(z)}{1-z^2},\quad
b(z)=\frac{g(z)}{1+z}.
\]
Each of the \(D=\binom{m+k-1}{k-1}\) configurations has the same weight. Counting zeros and equal adjacent entries, with \([z^m]\) denoting formal coefficient extraction, gives
\[
\begin{aligned}
D\,\mathbb E[U]&=k\binom{m+k-2}{k-2},\\
D\,\mathbb E[A]&=(k-1)[z^m]f(z),\\
D\,\mathbb E[UA]&=(k-1)[z^m]\bigl(2g(z)+(k-2)b(z)\bigr).
\end{aligned}
\]
For the last identity, the marked zero can occupy one of the two positions of the equal pair, forcing that pair to be \((0,0)\); alternatively it can occupy any of the other \(k-2\) positions, leaving an unconstrained equal pair. The resulting generating functions are respectively \(g(z)\) and \(b(z)\). This argument remains valid when \(k=3\), using \((1-z)^0=1\).

Let \(L=z\,d/dz+(k-1)\). Because \((m+k-1)[z^m]F=[z^m]LF\), substitution into the covariance and multiplication by \((m+k-1)D/(k-1)\) yield the coefficient of
\[
T(z)=L\bigl(2g(z)+(k-2)b(z)\bigr)-k(k-1)f(z).
\]
Direct differentiation with a common denominator, using \(b=g/(1+z)\) and \(f=g/(1-z^2)\), gives the exact formal-series identity
\[
T(z)=2z^2(k-3-z)(1-z)^{-(k-1)}(1+z)^{-2}
=2z^2(k-3-z)(1-z)^{-(k-3)}(1-z^2)^{-2}.
\]
Coefficient extraction proves the boxed covariance formula.

For \(k=3\), the series defining \(h_j^{(3)}\) is \((1-z^2)^{-2}=\sum_{t\ge0}(t+1)z^{2t}\), hence the covariance is negative precisely when \(m-3\) is a nonnegative even integer, equivalently when \(n\) is even and \(n\ge6\); otherwise it vanishes. For \(k=4\), write \(H(z)=(1-z)^{-1}(1-z^2)^{-2}\). Its coefficient at index \(j\ge0\) is \((r+1)(r+2)/2\), where \(r=\lfloor j/2\rfloor\). Thus \(h_{m-2}^{(4)}-h_{m-3}^{(4)}\) is strictly positive exactly when \(m\ge2\) is even; it is zero otherwise.

For \(k\ge5\), coefficients of \((1-z)^{-(k-3)}\) are nonnegative and nondecreasing, and coefficients of \((1-z^2)^{-2}\) are nonnegative, with constant term one. Their convolution therefore has \(0\le h_{j-1}^{(k)}\le h_j^{(k)}\) for \(j\ge0\) and \(h_j^{(k)}>0\) for \(j\ge0\). As \(k-3\ge2\), the boxed expression is strictly positive when \(m\ge2\), and zero when \(m=0\) or \(1\).

When \(k=2\), equality of the two parts requires even \(n\). At even \(n\ge4\), the equality indicator and the unit-part count never occur simultaneously: the equality event has probability \(1/(n-1)\), while the expected unit-part count is \(2/(n-1)\). Their covariance is therefore \(-2/(n-1)^2\). At other sizes the covariance is zero. When \(k=1\), the adjacent-equality count is identically zero. These cases complete the exhaustive classification.

## Verification

A standalone exact-arithmetic Python verifier (`verify_composition_covariance.py`) performs three independent checks: direct enumeration of **all** ordered compositions through \(n=18\), separate coefficient-based computation of the three mixed moments, and evaluation of the closed covariance formula. For \(19\le n\le140\), the two independent exact formulas are checked without brute-force enumeration. It verifies all sign regimes and stated boundary examples; it reports 19,745 passed exact assertions.

Run with `python verify_composition_covariance.py` using Python's standard library only. The infinite classification follows from the algebraic proof above, not from the bounded enumeration.

## Relationship to prior work

The count of adjacent equal parts (also called levels) is classical in integer-composition enumeration. Knopfmacher and Prodinger's *On Carlitz compositions* (1998) treats equal adjacencies among other statistics. Louchard and Prodinger (2002) study probabilistic properties of Carlitz compositions, namely compositions excluding equal consecutive parts. Heubach and Mansour (arXiv 2003; published 2005) give generating functions for the number of levels in unrestricted compositions with prescribed length and various allowed-part sets. In particular, their level-count coefficient generating function is the first-moment expression underlying this proof.

The claim here is neither the known first-moment formula nor a Carlitz count: it is the **mixed covariance with the number of unit parts** and a complete parity-sensitive, all-\((n,k)\) **sign classification**. Heubach and Mansour's stated multivariate generating function marks rises, levels, drops and length, but not the count of unit parts. Their theorem therefore does not directly imply this covariance-sign theorem. Gafni (arXiv 2009) studies the longest run of equal parts rather than this mixed moment. These comparisons do not establish historical uniqueness; see limitations.

## Limitations

The result is restricted to uniform compositions of a fixed integer into a fixed number of **ordered** positive parts. It does not address arbitrary nonuniform weights, cyclic equalities, or higher moments. The underlying single-statistic generating functions are established in prior work. An author-hosted account of the 1998 Knopfmacher–Prodinger paper was located, but full text was inaccessible in this review, leaving an explicit historical-priority risk. An earlier unrecognized joint refinement of known generating functions could in principle contain the sign theorem. Independent validation and independent historical review have not been performed.

## References

1. S. Heubach and T. Mansour, *Counting rises, levels, and drops in compositions*, arXiv:math/0310197v1, first posted 2003-10-14; *Integers* 5 (2005), A11. https://arxiv.org/abs/math/0310197
2. G. Louchard and H. Prodinger, *Probabilistic Analysis of Carlitz Compositions*, *Discrete Mathematics & Theoretical Computer Science* 5 (2002), 71–96. DOI: 10.46298/dmtcs.302. https://dmtcs.episciences.org/en/articles/302/download
3. A. Knopfmacher and H. Prodinger, *On Carlitz Compositions*, *European Journal of Combinatorics* 19 (1998), 579–589. DOI: 10.1006/eujc.1998.0216. Author abstract: https://www.finanz.math.tugraz.at/~prodinger/abs_136.htm
4. A. Gafni, *Longest Run of Equal Parts in a Random Integer Composition*, arXiv:0907.5553v1, 2009-07-31. https://arxiv.org/abs/0907.5553
