# Exact prime-modulus periods for the four-part pair-product partition statistic

## Finding

For each integer \(n\geq 0\), let \(a(n)\) be the sum of the pairwise-product statistic over the partitions of \(n\) into exactly four positive parts:

\[
a(n)=\sum_{\lambda_1\geq\lambda_2\geq\lambda_3\geq\lambda_4\geq1\atop \lambda_1+\lambda_2+\lambda_3+\lambda_4=n}
\ \sum_{1\leq i<j\leq4}\lambda_i\lambda_j.
\]

For any prime \(p\geq5\), the sequence \((a(n)\bmod p)_{n\geq0}\) is periodic starting at \(n=0\). Its **least period**, which also equals its least eventual period, is exactly

\[
\boxed{\operatorname{per}_p(a)=
\begin{cases}300,&p=5,\\12p,&p\geq7.\end{cases}}
\]

This proves the published conjectural periods \(300,84,132,156,204,\ldots\) at primes \(5,7,11,13,17,\ldots\), and extends them uniformly to every prime greater than three.

## Assumptions and scope

All partitions have four positive parts, are unordered, and may repeat parts. The integer \(a(n)\) is zero when \(n<4\). The period is the smallest positive integer \(T\) satisfying \(a(n+T)\equiv a(n)\pmod p\) for all \(n\geq0\). The eventual period instead requires this equality only for all sufficiently large \(n\). The theorem concerns primes \(p\geq5\), not prime powers or the primes \(2,3\).

Write \(q\) for a formal variable and set

\[
P(q)=6+15q+34q^2+57q^3+95q^4+121q^5+146q^6+126q^7
+106q^8+72q^9+50q^{10}+25q^{11}+11q^{12}.
\]

Define the integer polynomial

\[
H(q)=(q-1)^6(q+1)^4(q^2+q+1)^3(q^2+1)^3.
\]

The main structural identity, established below, is

\[
\boxed{\sum_{n\geq0}a(n)q^n=\frac{q^4P(q)}{H(q)}.}
\]

## Proof

**Generating function.** Every four-part partition can be written uniquely as

\[
\lambda_i=1+\sum_{j=i}^4x_j\quad(1\leq i\leq4),
\qquad x_j\in\mathbb Z_{\geq0}.
\]

Its size is \(4+x_1+2x_2+3x_3+4x_4\). Set \(A_i=1+\sum_{j=i}^4x_j\) and \(E(x_1,x_2,x_3,x_4)=\sum_{i<j}A_iA_j\). Direct expansion gives

\[
\begin{aligned}
E={}&6+3x_1+6x_2+9x_3+12x_4+x_1x_2+2x_1x_3+3x_1x_4\\
&+x_2^2+4x_2x_3+6x_2x_4+3x_3^2+9x_3x_4+6x_4^2.
\end{aligned}
\]

For \(t\) a formal variable, use the exact identities

\[
\sum_{r\geq0}t^r=(1-t)^{-1},\quad
\sum_{r\geq0}rt^r=t(1-t)^{-2},\quad
\sum_{r\geq0}r^2t^r=t(1+t)(1-t)^{-3}.
\]

Apply them to the displayed polynomial \(E\) with \(t=q^j\) for \(j=1,2,3,4\). Collecting terms over

\[
D(q)=\prod_{j=1}^4(1-q^j)^3
\]

yields the exact polynomial identity

\[
D(q)\sum_{n\geq0}a(n)q^n
=q^4(q-1)^6(q+1)^2P(q).
\]

Since \(D(q)=(q-1)^6(q+1)^2H(q)\), cancellation in \(\mathbb Z[[q]]\) proves the stated generating function. The provided standalone checker independently constructs the numerator from \(E\) over the integers and checks both factorizations. In particular, \(\deg H=22\), \(\deg(q^4P)=16\), and \(H(0)=1\).

**No modular cancellation.** Write \(\Phi_j\) for the cyclotomic polynomial of index \(j\). Then

\[
H=\Phi_1^6\Phi_2^4\Phi_3^3\Phi_4^3,
\]

where \(\Phi_1=q-1\), \(\Phi_2=q+1\), \(\Phi_3=q^2+q+1\), and \(\Phi_4=q^2+1\). Exact polynomial division gives

\[
P\equiv864\pmod{\Phi_1},\quad
P\equiv32\pmod{\Phi_2},\quad
P\equiv6\pmod{\Phi_3},\quad
P\equiv-12\pmod{\Phi_4}.
\]

The four nonzero residues have prime factors only \(2\) or \(3\). Thus, for every \(p\geq5\), the reduction of \(P\) modulo \(p\) is coprime to each factor of \(H\). Also \(q^4\) is coprime to \(H\) because \(H(0)=1\). Consequently the displayed rational generating function is in lowest terms over \(\mathbb F_p(q)\).

**Necessity of the period.** Fix a prime \(p\geq5\). If \(T\) is even an eventual period modulo \(p\), then \((1-q^T)\sum_{n\geq0}a(n)q^n\) is a polynomial in \(\mathbb F_p[q]\). Coprimality of the numerator and denominator forces \(H(q)\mid 1-q^T\) in \(\mathbb F_p[q]\). Since \(\Phi_3\Phi_4\mid H\) and \(p\nmid12\), primitive roots of orders \(3\) and \(4\) imply \(12\mid T\).

Write \(T=p^et\) with \(p\nmid t\). The zero \(q=1\) of \(1-q^T=(1-q^t)^{p^e}\) has multiplicity exactly \(p^e\). Since \((q-1)^6\mid H\), it follows that \(p^e\geq6\). Hence every eventual period is a multiple of \(300=12\cdot5^2\) when \(p=5\), and of \(12p\) when \(p\geq7\).

**Sufficiency and initial periodicity.** Put \(T=300\) for \(p=5\), and \(T=12p\) for \(p\geq7\). In \(\mathbb F_p[q]\), the Frobenius identity gives

\[
1-q^T=(1-q^{12})^{p^e},
\quad p^e=\begin{cases}25,&p=5,\\p,&p\geq7.\end{cases}
\]

All four cyclotomic factors of \(H\) divide \(1-q^{12}\), and their exponents in \(H\) are at most six. Because \(p^e\geq6\), we have \(H\mid1-q^T\). Therefore

\[
(1-q^T)\sum_{n\geq0}a(n)q^n
=q^4P(q)\frac{1-q^T}{H(q)}
\]

is a polynomial of degree \(16+T-22=T-6<T\). Equality of coefficients of degrees at least \(T\) proves \(a(n+T)\equiv a(n)\pmod p\) for **all** \(n\geq0\). The necessary divisibility already proved shows that no smaller eventual or ordinary period exists.

## Verification

Run `python3 verify.py` from the directory containing the standalone checker. It uses only the Python standard library and independently expands \(E\), reconstructs \(D\), \(H\), and \(P\), checks all four cyclotomic residues, compares the first \(41\) coefficients with direct four-part partition enumeration, and checks period and least-period patterns for seven sample primes including \(5\), \(7\), and \(101\). These finite computations verify the exact displayed algebra and illustrate the conclusions; the proof for all primes and all indices is the cyclotomic argument above.

## Relationship to prior work

Ballantine, Beck, and Merca introduced this exact statistic and displayed a conjectural table of its least periods modulo \(2,3,4,5,6,7,\ldots\). They proved periodic congruences for \(2,3,4\) (their Theorem 2), but explicitly described the other displayed periods as conjectural. The values \(300\) for modulus \(5\), \(84\) for \(7\), \(132\) for \(11\), and so on were therefore already *predicted*: the contribution here is an exact generating-function proof and a uniform formula for all primes \(p\geq5\), not the observation of those small numerical values.

Nijenhuis and Wilf established prime-modulus periods for unweighted restricted partition counts, and Kwong studied more general modular periodicities of rational generating functions. The cyclotomic approach is classical; the specific numerator cancellation and all-prime period classification for this weighted statistic are the results established here. Subsequent work on elementary symmetric partition maps studies injectivity and image-part multiplicities rather than these prime-modulus periods.

## Limitations

The theorem does not determine least periods modulo prime powers, arbitrary composites, or moduli \(2\) and \(3\). It addresses only the four-part second elementary-symmetric statistic, not all fixed-length partition statistics. The source's table gives some prime cases numerically without a proof; absolute bibliographic priority of the uniform theorem remains subject to further independent literature review.

## References

1. C. Ballantine, G. Beck, and M. Merca, *Partitions and elementary symmetric polynomials: an experimental approach*, first posted 23 August 2024, arXiv:2408.13346; *Ramanujan Journal* **66**, article 34 (2025), doi:10.1007/s11139-024-01001-6.
2. A. Nijenhuis and H. S. Wilf, *Periodicities of partition functions and Stirling numbers modulo p*, *Journal of Number Theory* **25** (1987), 308–312, doi:10.1016/0022-314X(87)90034-5.
3. Y. H. Kwong, *Minimum periods of partition functions modulo M*, *Utilitas Mathematica* **35** (1989), 3–8.
4. C. Ballantine, S. Nazir, B. E. Tenner, K. Westrem, and C. Zhao, *On partitions associated with elementary symmetric polynomials*, arXiv:2510.01100 (1 October 2025).
