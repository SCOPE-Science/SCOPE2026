# Exact first-absolute-moment spectrum of pairwise-independent fair signs

## Finding

Let \(n\ge2\), let
\[
\varepsilon_1,\ldots,\varepsilon_n
\]
be pairwise-independent Rademacher variables, and put
\[
S=\sum_{i=1}^n\varepsilon_i.
\]
Then the set of attainable values of
\[
\mathbb E|S|
\]
is exactly the interval
\[
\boxed{[L_n,U_n]}.
\]

The lower endpoint is
\[
L_n=
\begin{cases}
1,& n\ \text{even},\\[1mm]
\dfrac{2n}{n+1},& n\ \text{odd}.
\end{cases}
\]

For the upper endpoint, let \(a\) be the largest nonnegative integer satisfying
\[
a\equiv n\pmod2,
\qquad
a^2\le n,
\]
and put
\[
b=a+2.
\]
Then
\[
\boxed{U_n=\frac{n+ab}{a+b}.}
\]
If \(n=a^2\), this is simply \(U_n=\sqrt n\).

At the lower endpoint,
\[
|S|\in\{0,n\}
\]
for even \(n\), and
\[
|S|\in\{1,n\}
\]
for odd \(n\). At the upper endpoint,
\[
|S|\in\{a,b\}.
\]
All endpoint laws can be realized by exchangeable pairwise-independent fair signs, and convex mixing fills every intermediate first absolute moment.

Consequently,
\[
\frac{L_n}{\sqrt n}\longrightarrow0,
\qquad
\frac{U_n}{\sqrt n}\longrightarrow1.
\]

## Assumptions and scope

Each coordinate has the symmetric two-point law
\[
\Pr(\varepsilon_i=1)=\Pr(\varepsilon_i=-1)=\frac12,
\]
and every pair of distinct coordinates is independent. Mutual independence is not assumed.

The theorem concerns equal coefficients and the first absolute moment. It does not optimize weighted sums with arbitrary coefficients.

## Proof

Pairwise independence and fairness imply
\[
\mathbb E S=0
\]
and
\[
\mathbb E S^2
=
\sum_{i=1}^n\mathbb E\varepsilon_i^2
+
2\sum_{i<j}\mathbb E(\varepsilon_i\varepsilon_j)
=
n.
\tag{1}
\]

Put \(R=|S|\). Since \(S\) is a sum of \(n\) signs,
\[
R\in\mathcal R_n
=
\{r\in\mathbb Z_{\ge0}:r\le n,\ r\equiv n\pmod2\},
\]
and
\[
\mathbb E R^2=n.
\tag{2}
\]

If \(n\) is even, every \(r\in\mathcal R_n\) satisfies
\[
r\ge\frac{r^2}{n}.
\]
Taking expectations gives
\[
\mathbb E R\ge1.
\]
Equality holds only for \(R\in\{0,n\}\), and (2) then forces
\[
\Pr(R=n)=\frac1n.
\]

If \(n\) is odd, every allowed \(r\) lies in \([1,n]\), so
\[
(r-1)(n-r)\ge0.
\]
Equivalently,
\[
r\ge\frac{r^2+n}{n+1}.
\]
Taking expectations gives
\[
\mathbb E R\ge\frac{2n}{n+1}.
\]
Equality holds only for \(R\in\{1,n\}\), with
\[
\Pr(R=n)=\frac1{n+1},
\qquad
\Pr(R=1)=\frac n{n+1}.
\]

For the upper bound, let \(a\) and \(b=a+2\) be as in the statement. No point of \(\mathcal R_n\) lies strictly between \(a\) and \(b\), and
\[
a^2\le n\le b^2.
\]
Hence for every \(r\in\mathcal R_n\),
\[
(r-a)(r-b)\ge0.
\]
Rearranging,
\[
r\le\frac{r^2+ab}{a+b}.
\]
Taking expectations and using (2),
\[
\mathbb E R\le\frac{n+ab}{a+b}=U_n.
\]
Equality requires \(R\in\{a,b\}\). The unique such law with second moment \(n\) is
\[
\Pr(R=b)=\frac{n-a^2}{b^2-a^2},
\qquad
\Pr(R=a)=\frac{b^2-n}{b^2-a^2}.
\tag{3}
\]

It remains to realize these absolute-sum laws by pairwise-independent signs. Start from any probability law on \(\mathcal R_n\) satisfying \(\mathbb E R^2=n\). Conditional on \(R=r>0\), choose an independent fair sign and put \(S=\pm r\); if \(r=0\), put \(S=0\). Then
\[
\mathbb E S=0,
\qquad
\mathbb E S^2=n.
\]
Set
\[
K=\frac{n+S}{2}.
\]
Conditional on \(K=k\), choose uniformly among all sign vectors having exactly \(k\) plus signs.

The resulting vector is exchangeable and satisfies
\[
\mathbb E K=\frac n2,
\qquad
\mathbb E[K(K-1)]=\frac{n(n-1)}4.
\]
Therefore, for \(i\ne j\),
\[
\Pr(\varepsilon_i=1)=\frac12,
\qquad
\Pr(\varepsilon_i=\varepsilon_j=1)=\frac14.
\]
By sign symmetry, all four ordered pair outcomes have probability \(1/4\), proving pairwise independence.

Thus both endpoint laws are realizable. Convex mixtures preserve all one- and two-coordinate marginals, so every point of \([L_n,U_n]\) is attainable.

Finally, with \(x=\sqrt n\),
\[
x-U_n
=
\frac{(x-a)(b-x)}{a+b}.
\]
Because \(b-a=2\), the numerator is bounded while \(a+b\) is of order \(\sqrt n\). Hence
\[
U_n=\sqrt n+O(n^{-1/2}).
\]

## Verification

A standalone exact-rational checker accompanies the theorem. It verifies the three pointwise affine certificates on every tested parity lattice, constructs all endpoint count laws, checks their first two factorial moments, and confirms the pairwise-independent exchangeable realization.

For an additional stress test, it enumerates all feasible two-point laws on the allowed absolute-sum lattice for moderate lengths and confirms that their extrema equal the stated formulas.

The computation is supplementary. The universal result follows from the pointwise inequalities and the explicit realization proof.

## Relationship to prior work

Pass and Spektor studied Khintchine-type inequalities for pairwise-independent Rademacher variables. Their 2014 preprint focuses on upper absolute moments with exponent \(p\ge2\). For even length and equal coefficients, they construct the law supported on zero sum and the two unanimous sign vectors, and prove that it maximizes the higher absolute moments.

The present first-moment result reverses that role: for even \(n\), the same zero/unanimous law minimizes \(\mathbb E|S|\). The maximizing first-moment law instead places \(|S|\) on the two parity-compatible magnitudes bracketing \(\sqrt n\). The inspected 2014 text does not treat \(p=1\), give this lattice upper envelope, or state the complete attainable interval.

The later revised Pass--Spektor treatment states the classical Khintchine inequality for all positive exponents, but its limited-independence sharp theorem remains in the regime \(p\ge2\). It likewise does not contain the first-absolute-moment spectrum above.

Targeted searches using lower-Khintchine, first-absolute-moment, expected-absolute-Rademacher-sum, pairwise-independence, and exchangeability terminology did not locate the formulas \(L_n\) and \(U_n\) or an equivalent complete interval.

## Limitations

The result is restricted to equal coefficients. Weighted pairwise-independent Rademacher sums have a different magnitude geometry.

The theorem identifies the extremal law of \(|S|\), but does not claim uniqueness of every nonsymmetric full joint-law extremizer. Exchangeable extremizers are supplied explicitly.

The originality assessment is based on targeted searches. An equivalent elementary moment statement could exist in older limited-independence or coding literature under different terminology.

## References

1. B. Pass and S. Spektor, “On Khinchine type inequalities for pairwise independent Rademacher random variables,” arXiv:1412.7859, first submitted 2014-12-25.
2. B. Pass and S. Spektor, “On Khintchine type inequalities for \(k\)-wise independent Rademacher random variables,” arXiv:1708.08775, first submitted 2017-08-27.
3. A. Khintchine, “Über dyadische Brüche,” *Mathematische Zeitschrift* 18 (1923), 109–116.
