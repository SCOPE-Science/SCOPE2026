# A seven-prime obstruction for the first unknown alternating-divisor multiplier

## Finding

Let \(\beta:\mathbb{N}\to\mathbb{N}\) be multiplicative with \(\beta(1)=1\) and, for every prime \(p\) and integer \(e\ge1\),
\[
\beta(p^e)=p^e-p^{e-1}+\cdots+(-1)^e=\frac{p^{e+1}+(-1)^e}{p+1}.
\]
Write \(\omega(n)\) for the number of distinct prime divisors of \(n\).

**Theorem.** For every integer \(n\ge1\),
\[
4\beta(n)=n\quad\Longrightarrow\quad\omega(n)\ge7.
\]
This is a necessary condition, **not** an existence theorem for \(4\)-imperfect numbers.

## Assumptions and scope

The definition is the alternating divisor sum used for \(k\)-imperfect numbers (\(k\beta(n)=n\)) in Zhou--Zhu (2009) and in Tóth (2013/2014). No assumption is made about parity, size, or prime exponents of \(n\); these are handled in the proof. The claim holds for every positive integer.

## Proof

Suppose for contradiction that \(4\beta(n)=n\) and \(\omega(n)\le6\). Necessarily \(4\mid n\), so write
\[
n=2^a\prod_{i=1}^{r}p_i^{e_i},\qquad a\ge2,\quad 0\le r\le5,\quad 3\le p_1<\cdots<p_r.
\]
The prime \(p_i\) is odd and every \(e_i\ge1\).

**Local inequalities.** For odd \(p\),
\[
\frac{\beta(p^e)}{p^e}=\frac{p}{p+1}\left(1+\frac{(-1)^e}{p^{e+1}}\right).
\]
For any exponent \(e\ge1\), this ratio is at least \((p-1)/p\). For even \(e\) it is strictly greater than \(p/(p+1)\). For odd \(e\) it is at least \((p-1)/p\). Both functions \((p-1)/p\) and \(p/(p+1)\) increase with \(p\).

The first five odd primes are \(3,5,7,11,13\), and their minimal totient-factor product is
\[
P=\frac23\frac45\frac67\frac{10}{11}\frac{12}{13}=\frac{384}{1001}.
\]
As \(r\le5\), monotonicity and the fact that all factors are at most \(1\) show
\[
\prod_{i=1}^r\frac{\beta(p_i^{e_i})}{p_i^{e_i}}\ge P.
\]
For the power of \(2\),
\[
\frac{\beta(2^a)}{2^a}=\frac23+\frac{(-1)^a}{3\cdot2^a}.
\]
At \(a=2\) this is \(3/4\); at \(a=4\) it is \(11/16\); and for all \(a\ge5\) it is at least \(21/32\) (the minimum occurs at \(a=5\)). Hence
\[
\frac{\beta(n)}n\ge
\begin{cases}
\frac34 P=\frac{288}{1001}>\frac14,&a=2,\\
\frac{11}{16}P=\frac{264}{1001}>\frac14,&a=4,\\
\frac{21}{32}P=\frac{252}{1001}>\frac14,&a\ge5.
\end{cases}
\]
Each case contradicts \(\beta(n)/n=1/4\).

**The remaining exponent \(a=3\).** Here \(\beta(8)=5\) is odd. From \(4\beta(n)=n\) we have \(v_2(\beta(n))=a-2=1\). For an odd prime, \(\beta(p^e)\) is even exactly when \(e\) is odd. Thus there is **exactly one** index \(j\) for which \(e_j\) is odd; all other exponents are even. In particular \(r\ge1\).

For a given set of \(r\) odd primes, the local lower bound with one odd exponent is minimized by assigning that odd exponent to the smallest prime: the ratio between the odd-exponent bound and the even-exponent bound is
\[
\frac{(p-1)/p}{p/(p+1)}=1-\frac1{p^2},
\]
which increases with \(p\). Replacing the \(r\) primes by the first \(r\) odd primes can only decrease the lower bound; inserting the remaining primes up to five multiplies by factors below one. Hence the lower bound for every \(r\le5\) is obtained by assigning the sole odd exponent to \(p=3\) among the five odd primes \(3,5,7,11,13\). Therefore
\[
\frac{\beta(n)}n>
\frac58\frac23\frac56\frac78\frac{11}{12}\frac{13}{14}
=\frac{3575}{13824}>\frac14.
\]
The inequality is strict because at least one even-exponent factor is strictly above its bound; if \(r<5\), the padded lower bound is weaker but still valid. This again contradicts \(\beta(n)/n=1/4\).

All \(a\ge2\) are excluded. The contradiction proves \(\omega(n)\ge7\). \(\square\)

## Verification

The proof uses rational inequalities only; no finite search is substituted for the universal argument. The accompanying standalone Python checker uses exact rational arithmetic for the four decisive bounds, verifies the parity and local estimates over finite sample ranges, and independently checks \(4\beta(n)\ne n\) for all \(1\le n\le100000\). Run with Python 3 as `python verify.py`.

The exact symbolic inequalities, not the finite computation, establish the infinite theorem.

## Relationship to prior work

Zhou and Zhu's *On \(k\)-Imperfect Numbers* (2009), Proposition 11, proves the general lower bound \(\omega(n)\ge k-1\); for \(k=4\) that gives only \(\omega(n)\ge3\). The same paper's Theorem 9 concerns *odd* \(k\)-imperfect numbers, and is inapplicable here because \(4\beta(n)=n\) forces \(4\mid n\). Its searches up to \(2^{32}\) do not prove any all-size support bound.

Tóth's *A survey of the alternating sum-of-divisors function* (initial arXiv version 2011, updated 2014) documents the local definition, the absence of known \(k\)-imperfect numbers for \(k>3\), and relevant comparisons with \(\varphi\). It does not state this seven-prime obstruction. The present result exploits the narrowly decisive rational gap \(252/1001>1/4\) and handles the exceptional \(v_2(n)=3\) stratum by parity of the odd-prime exponents.

## Limitations

This theorem does not construct a \(4\)-imperfect number and does not rule out numbers with seven or more distinct prime divisors. Its lower bound is **not known to be sharp**. Unindexed equivalent literature is a residual priority risk; independent mathematical review has not been conducted. The elementary inequalities are unconditional.

## References

1. W. Zhou and L. Zhu, *On \(k\)-Imperfect Numbers*, INTEGERS 9 (2009), 1--8, first published 2009-01-05 in the open PDF; https://math.colgate.edu/~integers/j1/j1.pdf ; DOI: 10.1515/INTEG.2009.001.
2. L. Tóth, *A survey of the alternating sum-of-divisors function*, Acta Univ. Sapientiae Math. 5 (2013), 93--107; initial arXiv preprint 1111.4842 (2011); https://arxiv.org/pdf/1111.4842 .
