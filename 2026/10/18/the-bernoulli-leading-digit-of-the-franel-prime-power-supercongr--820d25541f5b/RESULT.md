# The Bernoulli leading digit of the Franel prime-power supercongruence

## Finding
For every prime \(p\ge5\) and integer \(r\ge1\), define the Franel numbers by
\[
F_n=\sum_{k=0}^{n}\binom nk^3
\]
and the alternating reciprocal-cube residue by
\[
H_p=\sum_{k=1}^{p-1}\frac{(-1)^{k-1}}{k^3}\pmod p.
\]
Then the exact first digit beyond the classical cubic supercongruence is independent of the exponent:
\[
\boxed{\frac{F_{p^r}-F_{p^{r-1}}}{p^{3r}}\equiv H_p\equiv\frac12 B_{p-3}\pmod p.}
\]
Here \(B_m\) is the ordinary Bernoulli number with generating function \(t/(e^t-1)\). In particular, \(\nu_p(F_{p^r}-F_{p^{r-1}})=3r\) for every \(r\ge1\) exactly when \(p\nmid\operatorname{num}(B_{p-3})\); if the prime divides that numerator, all the differences are divisible by \(p^{3r+1}\). The latter primes are the classical Wolstenholme primes. No valuation beyond the displayed lower bound is asserted in the exceptional case.

## Assumptions and scope
The prime is at least five, and the exponent is a positive integer. All rational congruences are interpreted in the localization of the integers at \(p\); in particular the denominators of \(H_p\) are units modulo \(p\). The denominator of \(B_{p-3}\) is also a unit modulo \(p\) by the von Staudt--Clausen theorem (and this is directly clear for \(p=5\)). The usual convention \(\nu_p(0)=\infty\) is used. This theorem is not asserted for the primes two or three, nor for arbitrary indices outside the prime-power tower.

## Proof
**Step 1: the terms whose indices are divisible by the prime.** For \(r=1\), the divisible indices in the sum are only its two endpoints, which contribute \(2=F_1\). Suppose \(r\ge2\). For an interior multiple \(k=pj\), with \(1\le j<p^{r-1}\), set \(s=\nu_p(j)\). Necessarily \(0\le s\le r-2\), and \(\nu_p(p^{r-1}-j)=s\). The binomial identity \(\binom{p^{r-1}}j=(p^{r-1}/j)\binom{p^{r-1}-1}{j-1}\), together with Lucas's congruence, gives
\[
\nu_p\binom{p^{r-1}}j=r-1-s.
\]
Jacobsthal's binomial congruence (in the form of Straub [2, Lemma 5.1]), applied with \(a=p^{r-1}\) and \(b=j\), implies for \(p\ge5\) that
\[
\frac{\binom{p^r}{pj}}{\binom{p^{r-1}}j}
\equiv1\pmod{p^{r+2+2s}}.
\]
The quotient is a \(p\)-adic unit. Taking cubes therefore yields
\[
\nu_p\!\left(\binom{p^r}{pj}^{3}-\binom{p^{r-1}}j^{3}\right)
\ge3(r-1-s)+(r+2+2s)=4r-1-s\ge3r+1.
\]
Summing over \(j\), and observing that both endpoints contribute one, proves
\[
\sum_{p\mid k}\binom{p^r}{k}^3\equiv F_{p^{r-1}}\pmod{p^{3r+1}},
\]
where the sum is taken over \(0\le k\le p^r\).

**Step 2: the remaining terms.** Whenever \(p\nmid k\), the identity
\[
\binom{p^r}k=\frac{p^r}{k}\binom{p^r-1}{k-1}
\]
and Lucas's theorem give \(\binom{p^r-1}{k-1}\equiv(-1)^{k-1}\pmod p\). Consequently
\[
\frac{1}{p^{3r}}\binom{p^r}k^3\equiv \frac{(-1)^{k-1}}{k^3}\pmod p.
\]
Every nonmultiple has a unique representation \(k=ap+b\), with \(0\le a<p^{r-1}\), \(1\le b<p\). The number \(p^{r-1}\) is odd, so \(\sum_{a=0}^{p^{r-1}-1}(-1)^a=1\). Reducing denominators modulo \(p\) gives
\[
\frac1{p^{3r}}\sum_{p\nmid k}\binom{p^r}k^3\equiv
\sum_{b=1}^{p-1}\frac{(-1)^{b-1}}{b^3}=H_p\pmod p.
\]
Steps 1 and 2 prove the first congruence, including the case \(r=1\).

**Step 3: identify the Bernoulli coefficient.** Fermat's theorem implies \(\sum_{k=1}^{p-1}k^{-3}\equiv0\pmod p\). Separating odd and even \(k\) therefore gives
\[
H_p\equiv-\frac14\sum_{k=1}^{(p-1)/2}k^{-3}\pmod p.
\]
Write \(m=p-3\), which is even and at least two. The standard power-sum identity for Bernoulli polynomials, evaluated at \((p+1)/2\), gives
\[
\sum_{k=1}^{(p-1)/2}k^{-3}\equiv\sum_{k=1}^{(p-1)/2}k^{p-4}
\equiv\frac{B_m(1/2)-B_m}{m}\pmod p.
\]
Here the denominators occurring in the polynomial are \(p\)-adic units, and \(B_m(1/2)=(2^{1-m}-1)B_m\). Fermat's theorem gives \(2^{1-m}=2^{4-p}\equiv8\pmod p\); therefore the last displayed expression is \(6B_m/(-3)=-2B_m\pmod p\). It follows that \(H_p\equiv B_{p-3}/2\pmod p\), as asserted. The final valuation dichotomy is immediate from the first nonzero \(p\)-adic digit and the standard Bernoulli characterization of Wolstenholme primes [3]. \(\square\)

## Verification
The standalone standard-library program `VERIFY.py` computes the Franel sums as exact integers, compares the quotient modulo \(p\), computes even-index Bernoulli numbers with rational arithmetic, and separates the divisible and nondivisible residue blocks. Its completed test covers \(32\) prime-power pairs with \(p\le79\) and \(p^r\le1000\), as well as five independent residue-block checks. These finite computations are diagnostic; the proof above establishes the unbounded statement.

## Relationship to prior work
Straub [2, Example 3.6 and equation (30)] proves the known supercongruence \(F_{p^r}\equiv F_{p^{r-1}}\pmod{p^{3r}}\) as part of a broader multivariate family, using Jacobsthal's theorem. That cubic divisibility is *not* claimed here. Sun [1] develops congruences for Franel-number sums, but his inspected statements do not determine the first digit of this prime-power difference. The present refinement computes that digit for every height and identifies exactly when the established modulus improves uniformly. The Wolstenholme-prime criterion is classical [3], and is used to interpret the coefficient, not presented as new. The comparative literature [4] studies different weighted Franel sums.

## Limitations
This finding does not determine how many additional powers divide the difference at a Wolstenholme prime, nor does it extend to arbitrary positive indices in place of a prime power. Jacobsthal's binomial congruence is taken as a cited classical lemma, not reproved here. Although targeted mathematical-record, bibliographic and full-text comparisons found no prior statement of the uniform leading-digit formula, priority cannot be established by search alone; a stronger unlocated p-adic theorem may already imply it. No independent mathematical audit has been performed.

## References
[1] Z.-W. Sun, *Congruences for Franel numbers*, arXiv:1112.1034, first publicly posted December 5, 2011, https://arxiv.org/pdf/1112.1034.

[2] A. Straub, *Multivariate Apéry numbers and supercongruences of rational functions*, Algebra & Number Theory 8 (2014), https://msp.org/ant/2014/8-8/ant-v8-n8-p07-s.pdf; especially Example 3.6 and Lemma 5.1.

[3] R. Meštrović, *Congruences for Wolstenholme primes*, arXiv:1108.4178, https://arxiv.org/html/1108.4178v1.

[4] G.-S. Mao, *Proof of some congruence conjectures of Z.-H. Sun involving Apéry-like numbers*, arXiv:2111.08778, https://arxiv.org/pdf/2111.08778.
