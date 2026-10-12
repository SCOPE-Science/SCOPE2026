# Exact defect spectrum through three for the Niven–totient bound

## Finding
For every integer \(n>1\), write
\[
n=\prod_{i=1}^r p_i^{a_i},
\qquad
H(n)=\max_{1\le i\le r} a_i,
\]
and define
\[
\Delta_H(n)=n-\varphi(n)-H(n).
\]
Then
\[
\Delta_H(n)=0\Longleftrightarrow n\text{ is prime or }n=4,
\]
\[
\Delta_H(n)=1\Longleftrightarrow n\in\{8,9\},
\qquad
\Delta_H(n)=2\Longleftrightarrow\text{no such }n\text{ exists},
\]
and
\[
\Delta_H(n)=3\Longleftrightarrow n\in\{6,25\}.
\]
In particular \(\Delta_H(n)\ge0\) for every \(n>1\).

## Assumptions and scope
Here \(H(n)\) is Niven's maximum exponent in the standard prime factorization and \(\varphi\) is Euler's totient. The theorem classifies only the defect levels \(0,1,2,3\).

## Proof
Let \(p\) be the least prime divisor of \(n\), and put \(h=H(n)\). Euler's product formula gives
\[
\varphi(n)\le n\left(1-\frac1p\right),
\]
hence
\[
\Delta_H(n)\ge \frac np-h.
\]
For composite \(n\), choose a prime \(q\) whose exponent is \(h\). If \(q=p\), then \(n/p\) is divisible by \(p^{h-1}\); if \(q\ne p\), then \(n/p\) is divisible by \(q^h\). Thus
\[
\frac np\ge2^{h-1},
\qquad
\Delta_H(n)\ge2^{h-1}-h\ge0.
\]
For prime \(n\), \(H(n)=1\) and \(\varphi(n)=n-1\), so the defect is \(0\).

Now suppose \(n\) is composite and \(\Delta_H(n)\le3\). Then
\[
2^{h-1}-h\le3,
\]
which forces \(h\le3\). Writing \(m=n/p\), the inequality \(\Delta_H(n)\ge m-h\) yields
\[
m\le h+3\le6.
\]
Because \(p\) is the least prime divisor of \(n=pm\), it is no larger than the least prime divisor of \(m\). Therefore the only composite candidates are
\[
4,6,8,9,10,12,15,25.
\]
Direct evaluation gives
\[
\Delta_H(4)=0,\quad
\Delta_H(8)=\Delta_H(9)=1,\quad
\Delta_H(6)=\Delta_H(25)=3,
\]
while
\[
\Delta_H(10)=5,\qquad
\Delta_H(12)=\Delta_H(15)=6.
\]
This proves the classification.

## Verification
The accompanying `verify.py` independently computes \(\varphi(n)\), the least prime divisor, and \(H(n)\) for every \(2\le n\le10^6\). It verifies nonnegativity, the least-prime lower bound, and all four claimed low fibers. The finite computation is regression evidence only; the proof above is cutoff-free.

## Relationship to prior work
Sándor and Atanassov prove the baseline inequality
\[
\varphi(n)\le n-\frac{n}{\gamma(n)}\le n-H(n),
\]
where \(\gamma(n)\) is the squarefree kernel. The present theorem determines the equality and first three positive defect levels of its final inequality.

Schinzel and Šalát study \(H\) through asymptotic density, statistical convergence, and normal order rather than the totient defect. Exact-formula, alias, database, and low-fiber searches did not locate an implication-equivalent classification.

## Limitations
The result does not classify \(\Delta_H^{-1}(k)\) for arbitrary \(k\ge4\) and gives no asymptotic distribution for the defect. Because the theorem is elementary, an unindexed note containing the same observation remains a residual originality risk.

## References
1. J. Sándor and K. T. Atanassov, “On certain arithmetical functions of exponents in the factorization of integers,” *Notes on Number Theory and Discrete Mathematics* 29 (2023), 378–388. DOI: 10.7546/nntdm.2023.29.2.378-388.
2. A. Schinzel and T. Šalát, “Remarks on maximum and minimum exponents in factoring,” *Mathematica Slovaca* 44 (1994), 505–514.
3. OEIS A051903, maximum exponent in the prime factorization.
