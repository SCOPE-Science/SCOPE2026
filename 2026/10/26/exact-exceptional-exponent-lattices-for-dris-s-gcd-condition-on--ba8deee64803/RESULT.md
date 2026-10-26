# Exact exceptional-exponent lattices for Dris’s GCD condition on two-prime supports

## Finding
Let \(\sigma\) denote the sum-of-positive-divisors function and define \(\mathcal A=\{m\ge1:\gcd(m,\sigma(m^2))=\gcd(m^2,\sigma(m^2))\}\). Fix an odd prime \(p\). Let \(d=\operatorname{ord}_p(2)\) and \(c=\nu_p(2^d-1)\), where \(\nu_p\) is the exact \(p\)-adic valuation. For integers \(a,b\ge1\):

* If \(d\) is even, every \(2^ap^b\) belongs to \(\mathcal A\).
* If \(d\) is odd, the **exact complementary classification** is
\[
2^ap^b\notin\mathcal A\quad\Longleftrightarrow\quad d\,p^{\max(0,b+1-c)}\mid(2a+1).
\]
Consequently the natural density of excluded exponents \(a\ge1\), for fixed \(p,b\), is zero when \(d\) is even, and otherwise exactly \(1/(d\,p^{\max(0,b+1-c)})\).

Moreover, for \(N\ge1\) let
\[
E_p(N)=\#\{(a,b)\in\{1,\ldots,N\}^2:2^ap^b\notin\mathcal A\}.
\]
If \(d\) is even, \(E_p(N)=0\) identically. If \(d\) is odd, then
\[
E_p(N)=\frac{N}{d}\left(c-1+\frac1{p-1}\right)+O_p(\log(2N)).
\]
Thus the excluded exponent pairs grow **linearly** in an \(N\)-by-\(N\) exponent square, and their relative density tends to zero, even though each fixed-\(b\) excluded column has positive density when \(d\) is odd.

## Assumptions and scope
The prime \(p\) is any odd prime; \(a,b,N\) are positive integers. Multiplicative order is defined since \(p\nmid2\), and \(d\mid p-1\), hence \(p\nmid d\). The \(O_p\)-constant may depend on fixed \(p\), but not on \(N\). Densities refer to exponents, not to the natural density of integers supported on \(\{2,p\}\). The global density-zero conjecture for \(\mathcal A\) is not resolved.

## Proof
Write \(m=2^ap^b\). Multiplicativity and the geometric-series formula give
\[
\sigma(m^2)=(2^{2a+1}-1)(1+p+\cdots+p^{2b}).
\]
The first factor is odd. The second factor consists of \(2b+1\) odd terms, hence is odd, and is congruent to \(1\pmod p\). Therefore \(\nu_2(\sigma(m^2))=0\), and
\[
\nu_p(\sigma(m^2))=\nu_p(2^{2a+1}-1)=v.
\]
Thus the two GCDs are respectively \(p^{\min(b,v)}\) and \(p^{\min(2b,v)}\). Equality holds precisely when \(v\le b\).

Put \(L=2a+1\), which is odd. By the definition of multiplicative order, \(v=0\) unless \(d\mid L\). If \(d\) is even it cannot divide odd \(L\), proving the first case. If \(d\) is odd and divides \(L\), lifting the exponent for odd \(p\) yields
\[
\nu_p(2^L-1)=\nu_p(2^d-1)+\nu_p(L/d)=c+\nu_p(L/d).
\]
Because \(p\nmid d\), the condition \(v>b\) is equivalent to \(d p^{\max(0,b+1-c)}\mid L\). This proves the classification, including the boundary case \(c=b+1\).

When \(d\) is odd, each modulus \(M_b=d p^{\max(0,b+1-c)}\) is odd. The congruence \(2a+1\equiv0\pmod{M_b}\) therefore selects exactly one residue class of \(a\) modulo \(M_b\), establishing its density \(1/M_b\).

For the two-variable count, the integers \(1\le b<c\) contribute \((c-1)N/d+O_p(1)\) once \(N\ge c-1\). For \(b\ge c\), put \(k=b+1-c\ge1\). The corresponding congruence has modulus \(dp^k\), and contributes \(N/(dp^k)+O(1)\) pairs \((a,b)\). But no such pair exists when \(dp^k>2N+1\). Thus only \(O_p(\log(2N))\) values of \(k\) contribute. Summing \(N/(dp^k)\) over them produces
\[
\frac{N}{d}\sum_{k\ge1}p^{-k}+O_p(1)=\frac{N}{d(p-1)}+O_p(1),
\]
since the omitted geometric tail is \(O_p(1)\). Counting one \(O(1)\) discrepancy per active residue class yields the stated \(O_p(\log(2N))\) remainder. This proves all assertions.

## Verification
The accompanying `verify.py` independently computes \(\sigma((2^ap^b)^2)\), both GCDs, and the predicted order/valuation criterion for every odd prime below \(50\), \(1\le a\le 20\), and \(1\le b\le 4\). It separately compares exact exponent-pair counts and the linear asymptotic for several primes. These finite checks test the hypotheses and edge cases; the infinite claims follow from the proof above.

For example, \(p=7\) has \(d=3\), \(c=1\), so exclusion is precisely \(3\cdot7^b\mid2a+1\); the coefficient in \(E_7(N)\) is \(1/18\). For \(p=3\), \(d=2\) is even and no positive pair is excluded.

## Relationship to prior work
Dris introduced this GCD set and conjectured that its **global natural density** equals zero (arXiv:2202.08116, Section 5). That paper gives computational examples, a general positive-density exclusion cylinder involving three prime factors, and a density bound, but not this exact two-prime-support exponent classification or its two-dimensional linear count. The known squarefree prime-support subfamily obtained by restricting all prime divisors to \(2\pmod3\) also addresses a different question and neither provides the present mixed prime-power complement nor its asymptotic. The result uses standard order theory and lifting-the-exponent but combines them with an exact exponent-lattice count. It is not a solution to the global conjecture.

## Limitations
The theorem treats only integers with exactly the distinct prime factors \(2\) and \(p\), with \(p\) fixed and exponents varying. The error constant is not uniform over growing \(p\). The elementary proof does not establish independent publication priority; an unindexed equivalent result or a published general cyclotomic valuation theorem could subsume the statement. No independent mathematical audit has been performed.

## References
1. Jose Arnaldo Bebita Dris, *A new approach to odd perfect numbers via GCDs*, arXiv:2202.08116v1 (first publicly posted 2022-02-10), Section 5, https://arxiv.org/html/2202.08116v1 .
2. *A squarefree \(2\bmod3\) subfamily in Dris’s GCD set*, research result available at https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-squarefree-2-bmod-3-subfamily-in-dris-s-gcd-set--3181e476c480 (comparison based on accessible abstract; full text not retrieved).
