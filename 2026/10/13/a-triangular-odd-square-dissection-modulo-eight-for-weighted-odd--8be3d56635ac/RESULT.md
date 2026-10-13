# A triangular–odd-square dissection modulo eight for weighted odd excludants

## Finding

For each nonnegative integer \(n\), let \(S(n)\) be the sum, over all partitions of \(n\) in which each even part occurs at most once, of the smallest positive odd integer absent from the partition. The empty partition contributes \(S(0)=1\). Put \(T_j=j(j+1)/2\), and write \(\delta_T(n)=1\) if \(n=T_j\) for some \(j\geq0\), and \(0\) otherwise. Define the finite representation number
\[
C(n)=\#\{(j,s)\in\mathbb Z_{\geq0}\times\mathbb Z_{>0}:s\text{ odd and }T_j+s^2=n\}.
\]
Then, for every \(n\geq0\),
\[
\boxed{S(n)\equiv(-1)^n\delta_T(n)+4C(n)\pmod 8.}
\]
Equivalently, as a coefficientwise identity in \(\mathbb Z[[q]]/8\mathbb Z[[q]]\),
\[
\boxed{\sum_{n\geq0}S(n)q^n\equiv
\left(\sum_{j\geq0}(-q)^{T_j}\right)
\left(1+4\sum_{\substack{s\geq1\\s\text{ odd}}}q^{s^2}\right)\pmod8.}
\]
In particular, \(S(n)\) is odd exactly when \(n\) is triangular; \(4\mid S(n)\) exactly when \(n\) is nontriangular; and, for nontriangular \(n\), \(\nu_2(S(n))=2\) exactly when \(C(n)\) is odd, while \(8\mid S(n)\) exactly when \(C(n)\) is even. Furthermore,
\[
\lim_{X\to\infty}\frac1X\#\{1\leq n\leq X:8\mid S(n)\}=1.
\]
The valuation convention is \(\nu_2(0)=\infty\).

## Assumptions and scope

All partitions are ordinary integer partitions, with repetitions allowed for odd parts and forbidden for even parts. All series manipulations take place in the formal power-series ring \(\mathbb Z[[q]]\); infinite products have constant term one, so all needed quotients exist. The congruence holds coefficientwise without asymptotic or numerical restrictions. The density assertion uses the classical divergence of the sum of reciprocals of primes in each reduced arithmetic progression.

## Proof

Let \(E(q)=\prod_{m\geq1}(1-q^m)\), \(\Theta(q)=\sum_{r\in\mathbb Z}q^{r^2}\), and \(\Psi(q)=\sum_{j\geq0}q^{T_j}\). The generating function for partitions with no repeated even part is
\[
G(q)=\frac{(-q^2;q^2)_\infty}{(q;q^2)_\infty}=\frac{E(q^4)}{E(q)}.
\]
To have smallest missing odd part \(2m+1\), the odd parts \(1,3,\ldots,2m-1\) must all occur and \(2m+1\) must not occur. The resulting contribution to the weighted generating function is \((2m+1)q^{m^2}(1-q^{2m+1})G(q)\). Telescoping the sum over \(m\geq0\) gives
\[
F(q):=\sum_{n\geq0}S(n)q^n
=G(q)\sum_{m\geq0}(2m+1)q^{m^2}(1-q^{2m+1})
=G(q)\Theta(q).
\]
This also independently recovers the initial generating-function identity for the statistic established by Mukherjee.

The Jacobi triple product and Gauss triangular-number identity give
\[
\Theta(q)=\frac{E(q^2)^5}{E(q)^2E(q^4)^2},\qquad
\Psi(-q)=\frac{E(q^2)^2}{E(-q)},\qquad
E(-q)=\frac{E(q^2)^3}{E(q)E(q^4)}.
\]
Consequently
\[
F(q)=\Psi(-q)R(q)^2,
\qquad R(q)=\frac{E(q^2)^3}{E(q)^2E(q^4)}
=\prod_{m\geq1}\frac{(1+q^m)^2}{1+q^{2m}}
=\prod_{m\geq1}\left(1+\frac{2q^m}{1+q^{2m}}\right).
\]
Write \(R(q)=1+2U(q)\) for the unique integer-coefficient series \(U(q)\). Modulo two, all products involving at least two nonconstant factors of the last product disappear after dividing by two. Thus
\[
U(q)\equiv\sum_{m\geq1}\sum_{k\geq0}q^{(2k+1)m}\pmod2.
\]
At a positive index \(a\), the coefficient is the number of odd divisors of \(a\) modulo two. Writing \(a=2^v u\) with \(u\) odd, this number is odd precisely when \(u\) is a perfect square. Squaring power series in characteristic two therefore shows
\[
U(q)+U(q)^2\equiv U(q)+U(q^2)
\equiv \sum_{\substack{s\geq1\\s\text{ odd}}}q^{s^2}\pmod2:
\]
all powers of two times odd squares cancel except those having \(v=0\). Since
\(R(q)^2=(1+2U(q))^2=1+4(U(q)+U(q)^2)\), substitution into \(F(q)=\Psi(-q)R(q)^2\) proves the formal modulo-eight identity. Its coefficients give the stated valuation alternatives.

For the density statement, if \(C(n)>0\), then for some \(j\geq0\) and odd \(s\geq1\),
\[
8n+1=(2j+1)^2+8s^2.
\]
For a prime \(p\equiv5,7\pmod8\), \(-8\) is a quadratic nonresidue modulo \(p\). If \(p\) divides the right side, then \(p\) divides both \(2j+1\) and \(s\), so \(\nu_p(8n+1)\) is even after iterating this implication. For any finite set \(\mathcal P\) of such primes, the set of integers \(n\) for which every \(\nu_p(8n+1)\) is even has natural density
\[
\prod_{p\in\mathcal P}\frac{p}{p+1}
\]
by prime-adic residue counting and the Chinese remainder theorem. These products tend to zero as \(\mathcal P\) grows, since \(\sum_{p\equiv5,7\ (8)}1/p\) diverges. Hence the set with \(C(n)>0\) has density zero. The triangular indices also have density zero, proving the final assertion.

## Verification

The standalone script `verify.py` computes \(G(q)\) by the independent unrestricted-odd/distinct-even partition product, multiplies it by \(\Theta(q)\), and compares all 601 coefficients of indices \(0\leq n\leq600\) with the triangular–odd-square formula modulo eight. It also enumerates partitions explicitly at each \(0\leq n\leq22\), enforcing the even-part restriction and summing the least missing positive odd part. All tests passed. This finite agreement supports, but does not replace, the formal proof and the independent density argument.

## Relationship to prior work

Gargi Mukherjee, *Parity of parts and excludant statistics in partitions* (arXiv:2603.13915v1, initially public 2026-03-14), defines this exact weighted statistic and derives its generating function in Theorem 1.12 and the associated proof. The present result starts from that known object but supplies the coefficientwise modulo-eight triangular–odd-square dissection, exact valuation alternatives at the first three binary levels, and natural-density-one divisibility by eight. Its central new step is the odd-divisor-square cancellation in the square of the dyadic product \(R(q)\), not a restatement of the generating function. Work on unrestricted minimal-excludant sums, such as Baruah–Bhoria–Eyyunni–Maji (2022), concerns a different class of partitions and does not imply this classification.

## Limitations

The result determines residues modulo eight, not full two-adic valuations beyond the threshold three. The representation count \(C(n)\) is exact but is not reduced to a closed prime-factorization formula. The density argument proves a qualitative density-one theorem, not a rate of convergence. Novelty comparisons cannot exclude unindexed equivalent work.

## References

1. G. Mukherjee, *Parity of parts and excludant statistics in partitions*, arXiv:2603.13915v1 (2026), Theorem 1.12 and Section 6, https://arxiv.org/html/2603.13915v1.
2. N. D. Baruah, S. C. Bhoria, P. Eyyunni, and B. Maji, *A refinement of a result of Andrews and Newman on the sum of minimal excludants*, arXiv:2110.08108 (2021; later version 2022), https://arxiv.org/abs/2110.08108.
3. OEIS A001935, four-regular partition numbers, https://oeis.org/A001935.
4. Classical identities: Jacobi triple product, Gauss triangular-number identity, and divergence of prime reciprocal sums in reduced arithmetic progressions.
