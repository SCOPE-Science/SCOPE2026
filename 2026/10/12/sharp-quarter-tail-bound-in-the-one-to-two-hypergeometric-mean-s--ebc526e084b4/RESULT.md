# Sharp quarter-tail bound in the one-to-two hypergeometric mean strip

## Finding

**Theorem.** Let integers \(n\ge4k\), \(k\ge2\), and \(1\le i\le n\) be given. If \(H\sim\operatorname{Hyp}(n,i,k)\) counts marked objects in a uniform sample of size \(k\) without replacement and
\[
1<\mu:=\frac{ik}{n}\le2,
\]
then
\[
\boxed{\Pr\{H\ge\mu\}=\Pr\{H\ge2\}>\frac14\ge\frac{k}{n}.}
\]
The constant \(1/4\) is sharp as an infimum across this entire parameter range: take \(k=2\), \(n=2i-1\), and let \(i\to\infty\). The conclusion treats the whole infinite low-mean strip, not an unrestricted hypergeometric tail bound.

## Assumptions and scope

The population contains precisely \(i\) marked and \(n-i\) unmarked objects, and the sample is a uniformly random \(k\)-subset. Its probability mass function is \(\Pr(H=j)=\binom{i}{j}\binom{n-i}{k-j}/\binom nk\) on the usual valid support. The bound requires \(n\ge4k\) and \(1<ik/n\le2\). No independence of sampled indicators is assumed. The primary classification is MSC 60E15.

## Proof

**1. Reduction to the crossing boundary.** Write \(r=\lfloor n/k\rfloor+1\). Because \(n\ge4k\), we have \(r\ge5\). Since \(ik>n\), also \(i\ge r\). For fixed \(n,k\), the hypergeometric variable is stochastically increasing in the number of marked objects (couple marked sets by inclusion). Hence
\[
\Pr\{\operatorname{Hyp}(n,i,k)\ge2\}\ge\Pr\{\operatorname{Hyp}(n,r,k)\ge2\}.
\]
As \(n\le rk-1\), enlarge the population by adding only unmarked objects until it has exactly \(rk-1\) objects. Coupling uniform samples by a common random ordering gives stochastic decrease of the number of marked objects, so
\[
\Pr\{\operatorname{Hyp}(n,r,k)\ge2\}\ge\Pr\{\operatorname{Hyp}(rk-1,r,k)\ge2\}.
\]
It remains to show \(\Pr\{\operatorname{Hyp}(rk-1,r,k)\ge2\}>1/4\) for all integers \(r\ge5\), \(k\ge2\).

**2. Fifth-order Bonferroni minorant.** For any integer \(h\ge0\) define
\[
L_5(h)=\sum_{j=2}^{5}(-1)^j(j-1)\binom hj.
\]
For \(h=0,1\), this equals zero; for \(2\le h\le5\), it equals one. For every \(h\ge6\), the elementary alternating-binomial identity gives
\[
L_5(h)=1-\frac{4h+1}{5}\binom{h-2}{4}\le1.
\]
Thus \(L_5(h)\le\mathbf1_{\{h\ge2\}}\) for every integer \(h\ge0\). If \(Z\sim\operatorname{Hyp}(rk-1,r,k)\), its factorial moments imply
\[
\Pr\{Z\ge2\}\ge B_5(r,k):=\sum_{j=2}^{5}(-1)^j(j-1)
\frac{(r)_{\underline j}(k)_{\underline j}}{j!\,(rk-1)_{\underline j}},
\]
where \((a)_{\underline j}=a(a-1)\cdots(a-j+1)\), and terms vanish when \(j>\min\{r,k\}\).

**3. Small sample sizes.** Set \(z=r-5\ge0\). When \(k=2,3,4\), the support has size at most five, so the minorant equals the indicator exactly. Direct rational simplification yields, respectively,
\[
\begin{aligned}
4\Pr\{Z\ge2\}-1&=\frac1{2z+9} &&(k=2),\
&=\frac{z^2+17z+54}{3(3z+13)(3z+14)} &&(k=3),\
&=\frac{3(z+4)(z^2+14z+43)}{2(2z+9)(4z+17)(4z+19)} &&(k=4).
\end{aligned}
\]
Every displayed expression is strictly positive for \(z\ge0\).

**4. Infinite family via a positive-coefficient certificate.** Now suppose \(k\ge5\). Put \(x=r-5\ge0\), \(y=k-5\ge0\), and \(N=(5+x)(5+y)-1\). Define the integer polynomial
\[
Q(x,y)=120(N)_{\underline5}\left(B_5(5+x,5+y)-\frac14\right).
\]
Multiplication by \((N)_{\underline5}\) cancels every denominator. The expression can be computed without division as
\[
Q=-30(N)_{\underline5}+\sum_{j=2}^{5}\frac{120(-1)^j(j-1)}{j!}
(5+x)_{\underline j}(5+y)_{\underline j}(N-j)_{\underline{5-j}}.
\]
The polynomial has degree at most five in each of \(x\) and \(y\). Its exact coefficient matrix \(Q(x,y)=\sum_{a,b=0}^{5}c_{ab}x^a y^b\), with rows indexing \(a\) and columns indexing \(b\), is:

| \(a\backslash b\) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 12528000 | 13424880 | 5677500 | 1180950 | 120300 | 4770 |
| 1 | 13424880 | 14203976 | 5945750 | 1228840 | 125110 | 5004 |
| 2 | 5677500 | 5945750 | 2466200 | 505755 | 51160 | 2035 |
| 3 | 1180950 | 1228840 | 505755 | 102645 | 10215 | 395 |
| 4 | 120300 | 125110 | 51160 | 10215 | 980 | 35 |
| 5 | 4770 | 5004 | 2035 | 395 | 35 | 1 |

All 36 entries are strictly positive; consequently \(Q(x,y)>0\) for all real \(x,y\ge0\). The displayed identity is checkable by exact arithmetic in the accompanying standalone script. In particular, the script verifies equality of the factored expression with the coefficient polynomial on the \(6\times6\) grid \(\{0,\ldots,5\}^2\). **This is an identity proof**, not a finite-sample test: both sides are polynomials of bidegree at most five, so interpolation forces global equality. Because \((N)_{\underline5}>0\), it follows that \(B_5(r,k)>1/4\), hence \(\Pr\{Z\ge2\}>1/4\).

Combining the boundary reduction and all cases establishes the theorem. For sharpness, at \(k=2\), \(n=2i-1\), the exact probability equals \(i/[2(2i-1)]\), which decreases to \(1/4\) as \(i\to\infty\). \(\square\)

## Verification

Run `python3 check.py` using only the Python standard library. It checks the exact integer coefficient matrix by polynomial interpolation, positivity of every coefficient, the small-\(k\) rational identities, the Bonferroni pointwise identity, and additional exhaustive finite parameter tests. The certificate's infinitely quantified consequence depends on the proved polynomial degree bound, not on enumeration of parameter values. The sample program is a reproducibility supplement, not an independent mathematical audit.

## Relationship to prior work

Ai and Pelekis prove \(\Pr\{H\ge\mathbb EH\}\ge k/n\) for \(n\ge8k\), conjecture that \(n\ge4k\) may be possible, and identify a broader numerical quarter-tail hypothesis. The present result establishes the quarter bound, with its sharp constant, specifically in the nontrivial strip \(1<\mathbb EH\le2\) down to \(n=4k\). Greenberg and Mohri prove the quarter-tail bound for *binomial* sampling with replacement, not for this negatively dependent hypergeometric model. Neither result implies the precise claim here. This theorem does not prove the full \(n\ge4k\) conjecture, since all larger means remain outside its scope.

## Limitations

The bound requires a sampling fraction of at most one quarter and an expected marked count strictly above one but at most two. It makes no assertion about the full mean range, general zero-sum population extremizers, or the conjectural MMS inequality. The polynomial certificate is finite and exact; it proves the displayed symbolic identity because of the degree bound. There is residual bibliographic risk of an equivalent older formulation in finite-population tail theory; no independent scientific audit has been conducted.

## References

1. J. Ai and C. Pelekis, *On lower bounds for hypergeometric tails*, arXiv:2601.09485 (first publicly submitted 2026-01-14), Sections 1–3, especially Theorem 1.1 and the discussion preceding it. https://arxiv.org/html/2601.09485v2
2. S. Greenberg and M. Mohri, *Tight Lower Bound on the Probability of a Binomial Exceeding its Expectation*, arXiv:1306.1433 (2013), Theorem 2.1. https://arxiv.org/html/1306.1433v3
