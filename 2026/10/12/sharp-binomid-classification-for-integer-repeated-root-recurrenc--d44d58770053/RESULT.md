# Sharp binomid classification for integer repeated-root recurrences

## Finding

Let \(a\) be a nonzero integer, and let \(x_0,x_1\) be integers. Define an integer sequence by
\[
x_{n+2}=2a x_{n+1}-a^2 x_n\qquad(n\ge0).
\]
Assume \(x_n\ne0\) for every \(n\ge1\). In the terminology of Shapiro [1], this sequence is **binomid** if
\[
{n\brack k}_x:=\frac{x_nx_{n-1}\cdots x_{n-k+1}}{x_1x_2\cdots x_k}\in\mathbb Z
\quad\text{for all integers }n\ge1,\ 0\le k\le n,
\]
with empty products equal to \(1\).

**Theorem.** For every such integer recurrence, the following statements are equivalent:

1. The sequence is binomid.
2. The sequence is a divisibility sequence: \(m\mid n\implies x_m\mid x_n\) for all positive integers \(m,n\).
3. Either \(x_0=0\) or \(x_1=a x_0\).

More strongly, if \(x_0\ne0\) and \(x_1\ne a x_0\), then **infinitely many distinct primes** \(p\) have a corresponding positive integer \(k\) for which
\[
\nu_p\!\left({2k\brack k}_x\right)=-1.
\]
Thus infinitely many central generalized binomial coefficients are nonintegral, and their denominators involve infinitely many primes.

## Assumptions and scope

The parameters \(a,x_0,x_1\) are arbitrary integers with \(a\ne0\) and every \(x_n\), \(n\ge1\), nonzero. Zero entries are excluded because the defining generalized binomial coefficients then have zero denominators. The theorem treats integer repeated characteristic roots \(a\); it does not classify recurrences with distinct characteristic roots, nonintegral repeated roots, or sequences containing zero positive-index terms. Negative parameters and negative sequence terms are allowed. For a nonzero rational number \(q\), \(\nu_p(q)\) is the exponent of \(p\) in its prime factorization, with negative values permitted.

## Proof

**1. Closed form.** Write \(C=x_1-a x_0\) and \(D=a x_0\). The characteristic polynomial is \((T-a)^2\), and direct substitution and the initial conditions give
\[
x_n=(Cn+D)a^{n-1}\qquad(n\ge1).
\]
For \(0\le k\le n\), cancelling the common constant factor in the products and collecting powers of \(a\) yields the exact identity
\[
{n\brack k}_x
=a^{k(n-k)}\frac{\prod_{j=n-k+1}^{n}(Cj+D)}{\prod_{j=1}^{k}(Cj+D)}. \tag{1}
\]
All displayed denominator factors are nonzero by hypothesis.

**2. Sufficient cases.** If \(C=0\), (1) equals \(a^{k(n-k)}\), an integer. Moreover \(x_n/x_m=a^{n-m}\) whenever \(m\mid n\). If \(D=0\), (1) equals \(a^{k(n-k)}\binom nk\), an integer, and for \(m\mid n\) one has \(x_n/x_m=(n/m)a^{n-m}\in\mathbb Z\). Thus either exceptional case is binomid and divisible. As \(a\ne0\), these cases are exactly \(x_1=a x_0\) and \(x_0=0\), respectively.

**3. Infinite prime obstruction when \(CD\ne0\).** Put \(g=\gcd(|C|,|D|)\), and multiply the affine factor by a global sign if necessary. We may write
\[
Cj+D=\varepsilon g(Aj+B),\qquad A\ge1,\quad B\in\mathbb Z\setminus\{0\},\quad\gcd(A,B)=1,
\]
where \(\varepsilon\in\{-1,1\}\). The factor \(\varepsilon g\) cancels from (1).

Suppose \(A=1\). Then \(B<0\) would make the positive-index term at \(j=-B\) vanish, contrary to the hypothesis. Therefore \(B>0\). By Dirichlet's theorem there are infinitely many primes \(p\equiv B\pmod A\), where for \(A=1\) this simply means all primes. Discard the finitely many primes dividing \(a\), and take \(p\) sufficiently large that
\[
k:=\frac{p-B}{A}\ge1,\qquad p>|A+B|,
\]
and, when \(A\ge2\), that \(2p-B<(A+1)p\). All these conditions hold eventually along the chosen prime progression.

The denominator affine factors of (1) for \(n=2k\) are \(Aj+B\) with \(1\le j\le k\). They increase from the fixed integer \(A+B\) to \(p\); for sufficiently large \(p\), none of the earlier factors is divisible by \(p\), while the final factor equals \(p\). Thus the denominator affine product has valuation exactly \(1\) at \(p\).

The numerator affine factors are
\[
p+A,\ p+2A,\ldots,\ 2p-B. \tag{2}
\]
When \(A=1\), they lie strictly between \(p\) and \(2p\) because \(B>0\), so none is divisible by \(p\). When \(A\ge2\), they lie in the open interval \((p,(A+1)p)\). Any multiple \(hp\) there has \(2\le h\le A\). But each term of (2) is congruent to \(B\pmod A\), whereas \(hp\equiv hB\pmod A\). Since \(\gcd(A,B)=1\), equality requires \(h\equiv1\pmod A\), impossible for \(2\le h\le A\). Therefore no numerator affine factor is divisible by \(p\).

Finally \(p\nmid a\), so the power \(a^{k^2}\) in (1) is a \(p\)-adic unit. Hence
\[
\nu_p\!\left({2k\brack k}_x\right)=0-1=-1. \tag{3}
\]
The prime progression contains infinitely many distinct admissible \(p\); their corresponding \(k\) also tend to infinity. Thus the sequence is not binomid, and the stronger infinite obstruction follows.

**4. Converse involving divisibility.** In the two sufficient cases above, divisibility has already been proved. Conversely, when \(CD\ne0\), take a sufficiently large prime witness from step 3: \(x_k=(Ck+D)a^{k-1}=\varepsilon gp a^{k-1}\), while \(x_{2k}=\varepsilon g(2p-B)a^{2k-1}\). For \(A\ge2\), \(2p-B\) is not divisible by \(p\) for all sufficiently large \(p\) (because \(p>|B|\)); for \(A=1\), the same holds. As \(p\nmid a\), the quotient \(x_{2k}/x_k\) has valuation \(-1\). Hence divisibility fails. This establishes all equivalences. \(\square\)

## Verification

The standalone standard-library program `verify.py` enumerates integer recurrence parameters, checks every generalized binomial coefficient in positive cases through index \(16\), and constructs and tests the central prime obstruction in negative cases. Its accompanying `verify_output.txt` contains the actual output. These are finite consistency checks; they do not replace the proof's use of Dirichlet's theorem or establish the theorem for arbitrary parameters.

## Relationship to prior work

Shapiro [1] defines binomid sequences and explicitly asks in Open Questions 29 which order-two recurrence sequences are binomid and whether binomidness implies divisibility. His discussion proves the zero-initial-value Lucas case and treats polynomial sequences separately, but does not state this classification of the integer repeated-root family. The sufficient \(x_0=0\) direction is therefore **not** new; the converse and infinite prime-denominator obstruction are the contribution here. Granville [2] classifies linear **division** sequences, which is relevant to the divisibility half but does not by itself classify possibly binomid, nondivisible sequences. The theorem resolves the binomid-versus-divisibility question only for the integer repeated-root subfamily, not all second-order recurrences.

## Limitations

The proof uses Dirichlet's theorem about primes in coprime arithmetic progressions, so it is not a purely elementary finite identity argument. It does not provide bounds for the least obstruction index or classify the allowed recurrence parameters if a positive-index term vanishes. The literature comparison includes the primary papers and targeted searches, but cannot rule out an equivalent unindexed formulation elsewhere. 

## References

[1] Daniel B. Shapiro, *Divisibility Properties for Integer Sequences*, **INTEGERS** 23 (2023), A57, especially Definition 1, Lemma 3, Sections 4.3-4.4, and Open Questions 29. First public arXiv version dated 2023-02-04: https://arxiv.org/abs/2302.02243 . Journal open-access text: https://math.colgate.edu/~integers/x57/x57.pdf .

[2] Andrew Granville, *Classifying linear division sequences*, arXiv:2206.11823v1, first submitted 2022-06-23: https://arxiv.org/abs/2206.11823 .
