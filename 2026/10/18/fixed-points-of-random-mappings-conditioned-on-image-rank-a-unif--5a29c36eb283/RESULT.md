# Fixed points of random mappings conditioned on image rank: a uniform Poisson law

## Finding

For every integer \(n\ge2\), let \(f:[n]\to[n]\) be a uniformly sampled function, and put \(R=|f([n])|\) and \(F=|\{i:f(i)=i\}|\). For every \(1\le r\le n\), the conditional mean is \(\mathbb E(F\mid R=r)=1\). Nevertheless the conditional distribution depends on \(r\), and its complete factorial moments admit the collision-free surjection formula below.

Let \(a_k(n,r)=\mathbb E[(F)_{\underline k}\mid R=r]\). For \(0\le k\le r\),
\[
a_k(n,r)=\frac{(r)_{\underline k}}{r!\,S(n,r)}\sum_{j=0}^{r-k}(-1)^j\binom{r-k}{j}(r-j)^{n-k},
\]
where \(S(n,r)\) is a Stirling number of the second kind; for \(k>r\), \(a_k(n,r)=0\). Thus the displayed formula specifies the full conditional law by factorial-moment inversion. It also yields, for every integer \(0\le k\le r\),
\[
\frac{(r)_{\underline k}}{r^k}\le a_k(n,r)\le1.
\]
In particular,
\[
1-\frac1r\le\operatorname{Var}(F\mid R=r)\le1,
\qquad
\left(1+\frac{z-1}{r}\right)^r\le\mathbb E[z^F\mid R=r]\le e^{z-1}\quad(z\ge1).
\]
Writing \(d_{\rm TV}\) for total variation distance between integer-valued laws, one has the **uniform-in-\(n\)** bound
\[
\boxed{\displaystyle d_{\rm TV}\!\left(\mathcal L(F\mid R=r),\operatorname{Poisson}(1)\right)\le\frac{e^2}{r}.}
\]
Consequently, for *every* sequence of admissible pairs with \(r\to\infty\), the conditional fixed-point law tends to \(\operatorname{Poisson}(1)\), no matter how \(n\) grows relative to \(r\). In the other regime, for each fixed \(r\ge1\), as \(n\to\infty\), \(\mathcal L(F\mid R=r)\) tends to \(\operatorname{Binomial}(r,1/r)\). The conditional mean remains exactly one in both regimes.

## Assumptions and scope

The map is uniform among all \(n^n\) functions \([n]\to[n]\). Rank \(R\) is the number of distinct images, **not** the number of cycles or cyclic vertices. The falling factorial is \((x)_{\underline k}=x(x-1)\cdots(x-k+1)\), with \((x)_{\underline0}=1\). The formula applies only when \(n\ge2\) and \(1\le r\le n\); all conditioning events have positive probability. Total variation is \(\frac12\sum_{j\ge0}|\Pr(X=j)-\Pr(Y=j)|\). The numerical bound can exceed one for small \(r\), but is valid without further assumptions and is not claimed optimal.

## Proof

**Step 1: independent image subset and uniform surjection.** Given \(R=r\), the image set \(S=f([n])\) is a uniform \(r\)-subset of \([n]\). Conditional on \(S\), the function is uniformly sampled among all surjections \([n]\to S\). Identify \(S\) with \([r]\) by any bijection and write \(g:[n]\to[r]\) for that random surjection. For \(k\) distinct fixed domain indices, membership in \(S\) has probability \((r)_{\underline k}/(n)_{\underline k}\). Conditional on membership, exchangeability of the \(r\) target labels gives probability \(q_k/(r)_{\underline k}\) of their specified fixed-point images, where \(q_k=\Pr(g(1),\ldots,g(k)\text{ all distinct})\). Hence the joint probability of \(k\) prescribed fixed points is \(q_k/(n)_{\underline k}\), and summing over the ordered distinct domain indices yields \(a_k(n,r)=q_k\). If \(k>r\), both sides vanish. In particular \(a_1=1\).

**Step 2: exact surjection count.** The number of onto maps \([n]\to[r]\) is \(r!S(n,r)\). If the first \(k\) outputs have distinct prescribed values, their remaining \(n-k\) outputs must cover the other \(r-k\) values. Inclusion-exclusion gives \(\sum_{j=0}^{r-k}(-1)^j\binom{r-k}{j}(r-j)^{n-k}\) completions. There are \((r)_{\underline k}\) ordered distinct initial outputs. This proves the displayed exact factorial moment formula and, via \(\operatorname{Var}(F)=\mathbb E(F)_{\underline2}+\mathbb EF-(\mathbb EF)^2\), the variance identity \(\operatorname{Var}(F\mid R=r)=q_2\).

**Step 3: the collision-free inequality.** Generate \(g\) instead by independent uniform outputs in \([r]\), conditional on the event \(U\) that every target is hit. Let \(D\) count distinct values among the first \(k\) outputs. Given \(D=d\), the conditional probability of \(U\) depends only on \(r-d\) as the number of as-yet-unhit targets, and it is nondecreasing in \(d\): covering fewer specified targets with the remaining \(n-k\) draws cannot be harder. Therefore conditioning on \(U\) cannot reduce the probability that \(D=k\), its maximal value. Thus \(q_k=\Pr(D=k\mid U)\ge\Pr(D=k)=(r)_{\underline k}/r^k\), while \(q_k\le1\). Termwise comparison of nonnegative factorial-moment coefficients in \(\mathbb E(1+t)^F=\sum_{k=0}^r a_k t^k/k!\), for \(t\ge0\), proves the generating-function sandwich.

**Step 4: an explicit Poisson error.** Extend \(a_k=0\) to all \(k>r\). The birthday union bound gives \(1-a_k\le\binom{k}{2}/r\) for \(k\le r\), and for \(k>r\) the same inequality holds because \(\binom{k}{2}/r\ge1\). By exact factorial-moment inversion,
\[
\Pr(F=j\mid R=r)=\frac1{j!}\sum_{\ell=0}^{\infty}\frac{(-1)^\ell a_{j+\ell}}{\ell!}.
\]
The corresponding expression for a \(\operatorname{Poisson}(1)\) variable has every factorial moment equal to one. Summing absolute differences, then reindexing by \(k=j+\ell\), gives
\[
 d_{\rm TV}\le\frac12\sum_{k\ge0}\frac{2^k}{k!}(1-a_k)
 \le\frac1{2r}\sum_{k\ge0}\frac{2^k}{k!}\binom{k}{2}=\frac{e^2}{r}.
\]
This step uses no limit theorem or independence approximation.

**Step 5: the second asymptotic regime.** With \(r\) fixed and \(n\to\infty\), the probability that an independent uniform map \([n]\to[r]\) fails to be onto is at most \(r(1-1/r)^n\), tending to zero (for \(r=1\), it is identically zero). Thus the first \(k\) surjection outputs tend to independent uniform outputs, so \(a_k\to(r)_{\underline k}/r^k\) for \(k\le r\). These are exactly the factorial moments of \(\operatorname{Binomial}(r,1/r)\). As both laws have support at most \(r\), moment inversion yields convergence in total variation.

## Verification

The accompanying `verify_rank_fixedpoint.py` enumerates every map \([n]\to[n]\) for \(2\le n\le6\), groups them both by their full in-degree vector and by image size, and checks the factorial-moment identities against exact integer counts. It makes 8,633 rational/integer assertions, including the surjection inclusion-exclusion formula, all finite-size factorial-moment inequalities, and the conditional variance identity. Run with `python3 verify_rank_fixedpoint.py`; it requires only the Python standard library. Enumeration is a finite cross-check; the proof above establishes all sample sizes.

## Relationship to prior work

Classical random-mapping enumeration treats cycle statistics, image/preimage structure, and other component parameters. Hansen and Jaworski's model conditions on exchangeable in-degree vectors and obtains local predecessor/successor laws; their basic uniform-with-given-degree construction is compatible with Step 1 but does not itself assert the rank-conditioned fixed-point factorial moments, the mean-independence phenomenon, or the uniform \(e^2/r\) Poisson bound. Bender, Canfield, Richmond, and Wilf analyze sums of fixed-point labels for permutations and all functions and obtain a different general Poisson-family asymptotic result; their fixed-point-sum distribution does not imply the present rank-conditioned law. The results here distinguish ordinary fixed points (self-loops) from all cyclic vertices. See References and the accompanying review for overlap uncertainties.

## Limitations

Only the ordinary uniform mapping model is covered, not arbitrary biased image probabilities. The probability bound is explicit but need not be numerically informative for small ranks and is not optimized. The assertion of originality is comparative and not an independent exhaustive priority certificate. A sufficiently broad earlier mapping-enumeration identity could contain some consequences implicitly; the accessible full texts listed below did not directly resolve the same conditional-rank statements. A relevant classical Flajolet–Odlyzko source was identified but its author-hosted compressed full text could not be read here; its unverified implications remain a genuine historical risk.

## References

1. E. A. Bender, E. R. Canfield, L. B. Richmond and H. S. Wilf, *A Discontinuity in the Distribution of Fixed Point Sums*, Electronic Journal of Combinatorics 10 (2003), R15, DOI: 10.37236/1708. Publicly posted 2003-04-23. Full article examined, especially pp. 1–8.
2. J. C. Hansen and J. Jaworski, *Local Properties of Random Mappings with Exchangeable In-Degrees*, Advances in Applied Probability 40 (2008), 183–205, DOI: 10.1239/aap/1208358892. Full accessible PDF examined, especially model definition, Section 3 and the applications in Section 4. Primary MSC 60C05.
3. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, Advances in Cryptology—EUROCRYPT '89, Lecture Notes in Computer Science 434 (1990), 329–354, DOI: 10.1007/3-540-46885-4_34. Abstract and author bibliography identified; complete full text not examined.
