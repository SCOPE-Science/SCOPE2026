# Exact covariance and cubic variance of the modular remainder energy

## Finding

Let \(m\ge 1\), put \(L_m=\operatorname{lcm}(1,\ldots,m)\), and define the modular energy \(E_m(n)=\sum_{k=1}^{m}(n\bmod k)\). If \(N_m\) is uniform on the complete residue period \(\{0,\ldots,L_m-1\}\), then
\[
\mathbb E[E_m(N_m)]=\frac{m(m-1)}4
\]
and, for every \(m\ge1\),
\[
\boxed{\operatorname{Var}(E_m(N_m))=\frac1{12}\left(\sum_{1\le a,b\le m}\gcd(a,b)^2-m^2\right)
=\frac1{12}\left(\sum_{d=1}^{m}J_2(d)\left\lfloor\frac m d\right\rfloor^2-m^2\right),}
\]
where \(J_2(d)=d^2\prod_{p\mid d}(1-p^{-2})\) is the second Jordan totient. Its leading behavior is
\[
\boxed{\operatorname{Var}(E_m(N_m))=
\frac{2\zeta(2)-\zeta(3)}{36\zeta(3)}m^3+O(m^2\log(2m)).}
\]
Consequently \(E_m(N_m)/m^2\to1/4\) in probability. More strongly, for a Haar-uniform compatible residue \(X\in\widehat{\mathbb Z}\), the sequence \(E_m(X)/m^2\to1/4\) almost surely.

## Assumptions and scope

All residues are least nonnegative residues. Here \(N_m\) is sampled uniformly from an **entire period**; the random variables for different \(m\) need not initially be coupled. For the almost-sure assertion, \(X\) lies in the profinite completion \(\widehat{\mathbb Z}=\varprojlim_q\mathbb Z/q\mathbb Z\), endowed with normalized Haar probability; \(X\bmod k\) denotes its canonical representative in \(\{0,\ldots,k-1\}\). This defines a compatible coupling whose marginal at level \(m\) is uniform modulo \(L_m\). The constants implicit in the asymptotic and in probability statements are absolute. The conclusions do not apply to the limit along a fixed ordinary integer \(n\), for which \(E_m(n)=O_n(m)\).

## Proof

**Pair covariance.** Fix positive integers \(a,b\), let \(g=\gcd(a,b)\), and write \(a=gu\), \(b=gv\), with \(\gcd(u,v)=1\). For \(N\) uniform modulo \(\operatorname{lcm}(a,b)=guv\), write \(N=R+gT\), uniquely with \(0\le R<g\) and \(0\le T<uv\). The variables \(R\) and \(T\) are independent and uniform. By the Chinese remainder theorem, \(T\bmod u\) and \(T\bmod v\) are independent uniform residues; thus conditioned on \(R=r\), the two variables
\[
N\bmod a=r+g(T\bmod u),\qquad N\bmod b=r+g(T\bmod v)
\]
are independent and have conditional means \(r+(a-g)/2\) and \(r+(b-g)/2\). The law of total covariance therefore gives
\[
\operatorname{Cov}(N\bmod a,N\bmod b)
=\operatorname{Var}(R)=\frac{g^2-1}{12}.
\]
The identity remains valid for \(a=1\), \(b=1\), and \(a=b\), including the degenerate case \(g=1\).

**Exact mean and variance.** Each \(N_m\bmod k\) is uniform on \(\{0,\ldots,k-1\}\) because \(k\mid L_m\), and hence has mean \((k-1)/2\). Sum these expectations for the stated mean. Expanding the variance and using the pair covariance gives the first exact expression. The divisor identity \(\sum_{d\mid g}J_2(d)=g^2\), obtained from Möbius inversion of \(n\mapsto n^2\), implies
\[
\sum_{a,b\le m}\gcd(a,b)^2
=\sum_{d\le m}J_2(d)\#\{a\le m:d\mid a\}\#\{b\le m:d\mid b\}
=\sum_{d\le m}J_2(d)\left\lfloor\frac md\right\rfloor^2.
\]

**Cubic asymptotic with error.** Möbius inversion gives \(J_2(n)=\sum_{d\mid n}\mu(d)(n/d)^2\). Therefore, uniformly for real \(x\ge1\),
\[
\sum_{n\le x}J_2(n)
=\sum_{d\le x}\mu(d)\sum_{j\le x/d}j^2
=\frac{x^3}{3}\sum_{d\le x}\frac{\mu(d)}{d^3}
+O\left(x^2\sum_{d\le x}\frac1{d^2}\right)
=\frac{x^3}{3\zeta(3)}+O(x^2).
\]
Here extending the absolutely convergent series past \(x\) changes the main term by \(O(x)\). Since \(\lfloor y\rfloor^2=\sum_{r\le y}(2r-1)\), one can interchange finite sums to obtain
\[
\sum_{d\le m}J_2(d)\left\lfloor\frac md\right\rfloor^2
=\sum_{r\le m}(2r-1)\sum_{d\le m/r}J_2(d)
=\frac{m^3}{3\zeta(3)}\sum_{r\le m}\frac{2r-1}{r^3}
+O\left(m^2\sum_{r\le m}\frac{2r-1}{r^2}\right).
\]
The infinite coefficient sum is \(2\zeta(2)-\zeta(3)\). The main-series tail contributes \(O(m^2)\), while the error sum is \(O(m^2\log(2m))\). The term \(-m^2\) in the exact variance is absorbed into the error, yielding the claimed constant.

**Concentration and almost-sure law.** The displayed variance is \(O(m^3)\) and \(\mathbb E[E_m]/m^2=1/4-1/(4m)\); Chebyshev's inequality implies, for each fixed \(\varepsilon>0\),
\[
\mathbb P\left(\left|\frac{E_m(N_m)}{m^2}-\frac14\right|>\varepsilon\right)=O_\varepsilon(m^{-1}).
\]
In the Haar coupling, choose the square subsequence \(m_j=j^2\). The probabilities above are summable in \(j\), so the first Borel--Cantelli lemma gives \(E_{j^2}(X)/j^4\to1/4\) almost surely. Because each added remainder is nonnegative, \(E_m(X)\) is nondecreasing in \(m\). For \(j^2\le m\le(j+1)^2\),
\[
\frac{E_{j^2}(X)}{(j+1)^4}\le\frac{E_m(X)}{m^2}\le
\frac{E_{(j+1)^2}(X)}{j^4}.
\]
Both bounding sequences tend to \(1/4\), proving the full almost-sure assertion.

## Verification

Run \(\texttt{python3 verify.py}\) with Python's standard library. The included verifier enumerates 12 complete periods independently of the covariance formula, checks 900 exact two-residue covariances by direct averaging, verifies Jordan divisor convolutions through 1200, and compares the two finite variance expressions for 126 values of \(m\). All comparisons use rational or integer arithmetic. Finite checks corroborate the identities; the all-\(m\) and asymptotic statements follow from the proof above, not extrapolation.

## Relationship to prior work

En-naoui [1] introduced the modular remainder energy and established its exact period, extremal behavior, and algebraic identities. Its concluding distributional questions explicitly motivate studying complete-period fluctuations; its presented results do not specify the pair-covariance law, exact second moment, cubic variance constant, or profinite almost-sure limit. The calculation also uses the classical Jordan totient divisor convolution. Kaltenböck, Kiuchi, Saad Eddin, and Ueda [2] analyze differently weighted averages of arithmetic greatest-common-divisor sums; their primary asymptotic formulas do not directly state the unweighted rectangular covariance sum or its modular-energy implications. Formula-level overlap with other classical gcd-sum identities remains a bibliographic possibility.

## Limitations

The result treats the full-residue-period model, not sampling from intervals shorter than the least common multiple, and not a fixed integer input. It proves concentration and almost-sure convergence but neither a central limit theorem nor a limiting fluctuation law after cubic-scale normalization. The variance constant could be derivable from broader classical Jordan/gcd-sum theorems, so independent priority assessment should compare equivalent formulations rather than titles alone.

## References

[1] Es-said En-naoui, *The Modular Energy Function: Exact Identities and a Primality Equivalence*, first public 2025-09-12, arXiv:2509.10592, https://arxiv.org/abs/2509.10592.

[2] Lisa Kaltenböck, Isao Kiuchi, Sumaia Saad Eddin, and Masaaki Ueda, *Sums of averages of gcd-sum functions II*, arXiv:2002.11984, https://arxiv.org/abs/2002.11984.

[3] Jordan totient sequence \(J_2\), OEIS A007434, https://oeis.org/A007434.
