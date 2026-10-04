# Two-prime infinitary harmonic numbers are exactly 6 and 45
## Finding
Let \(N=p^a q^b\) with distinct primes \(p<q\) and \(a,b\ge 1\). If \(H_\infty(N)\) is integral, then \(J(N)\le 3\), where \(J(N)\) is the number of I-components, equivalently the sum of the binary digit counts of \(a\) and \(b\). Hence the only infinitary harmonic integers with exactly two distinct prime factors are \(6\) and \(45\).

## Assumptions and scope
Write \(a=\sum_{i\in A}2^i\) and \(b=\sum_{j\in B}2^j\), with finite nonempty sets \(A,B\). Then \(J(N)=|A|+|B|\), and
\[
\sigma_\infty(N)=\prod_{i\in A}(p^{2^i}+1)\prod_{j\in B}(q^{2^j}+1),
\qquad
H_\infty(N)=\frac{2^{J(N)}N}{\sigma_\infty(N)}.
\]
The result concerns exactly two distinct prime factors; it makes no assertion about infinitary harmonic integers with three or more prime factors.

## Proof
Assume first that \(p\) is odd. For distinct indices \(i<k\),
\[
\gcd(p^{2^i}+1,p^{2^k}+1)=2,
\]
because modulo \(p^{2^i}+1\) one has \(p^{2^i}\equiv-1\), while the exponent quotient \(2^{k-i}\) is even. Since \(H_\infty(N)\) is integral, every odd prime divisor of each \(p^{2^i}+1\) must divide the numerator \(2^{J(N)}p^a q^b\). It cannot equal \(p\), so it must equal \(q\). For every \(i\ge1\), the number \(p^{2^i}+1\) is congruent to \(2\pmod 8\) and is greater than \(2\); therefore it has an odd prime divisor. The pairwise gcd identity then allows at most one index \(i\ge1\) in \(A\). The index \(0\) may occur in addition, so \(|A|\le2\).

If \(p=2\), the numbers \(2^{2^i}+1\) for distinct \(i\) are odd, greater than \(1\), and pairwise coprime. Every prime divisor must therefore be \(q\), so at most one such factor can occur and \(|A|\le1\). Applying the odd-prime argument to \(q\) gives \(|B|\le2\). Hence any even two-prime infinitary harmonic number already has \(J(N)\le3\).

It remains to exclude \(J(N)=4\) when both \(p\) and \(q\) are odd. Equality would force \(|A|=|B|=2\). Thus \(A=\{0,i\}\) and \(B=\{0,j\}\) for some \(i,j\ge1\). On the \(p\)-side, the factor \(p^{2^i}+1\) has an odd divisor and hence a factor \(q\); because it has gcd only \(2\) with \(p+1\), the factor \(p+1\) has no odd prime divisor and is a power of \(2\). Similarly, \(q+1\) is a power of \(2\). But \(q\mid p^{2^i}+1\) gives \(p^{2^i}\equiv-1\pmod q\), so the multiplicative order of \(p\) modulo \(q\) is exactly \(2^{i+1}\). Therefore \(4\mid q-1\), hence \(q\equiv1\pmod4\). On the other hand, an odd prime with \(q+1\) a power of \(2\) satisfies \(q\equiv3\pmod4\), a contradiction. Thus \(J(N)\le3\).

The 2026 small-component classification proves that an infinitary harmonic integer with \(J(N)\le3\) lies in \(\{1,6,45,60,90,15925\}\), and in the same proof it records \(T_{2,2}=\{6,45\}\) and \(T_{3,2}=\varnothing\). Among those integers, exactly \(6\) and \(45\) have two distinct prime factors. This completes the classification.

## Verification
The symbolic proof above is unrestricted. The accompanying checker independently evaluates \(H_\infty\) by exact rational arithmetic for distinct primes below \(100\) and exponents from \(1\) through \(15\); it finds only \(6\) and \(45\). This finite computation is corroborative and is not used to infer the infinite theorem.

## Relationship to prior work
Hagis and Cohen introduced infinitary harmonic numbers and proved finiteness for a fixed number of I-components. A 2026 refinement gives the complete \(J(N)\le3\) list and, within its proof, \(T_{2,2}=\{6,45\}\) and \(T_{3,2}=\varnothing\). A published database finding classifies the \(J(N)=4\) layer globally. None of these statements supplies the structural implication that two-prime support forces \(J(N)\le3\); the gcd-and-order argument above eliminates all higher I-component layers at once.

## Limitations
The originality comparison found no statement equivalent to the all-layer support bound, but older or poorly indexed literature could still contain an equivalent observation. The exact-day archive date attached to the record comes from the public OEIS entry for the infinitary harmonic sequence; the original journal article is older but the available bibliographic record resolves its print date only to February 1990. The proof relies on the published 2026 low-I-component classification only for the final identification of \(6\) and \(45\); the bound \(J(N)\le3\) is proved independently here.

## References
1. P. Hagis, Jr. and G. L. Cohen, “Infinitary harmonic numbers,” *Bulletin of the Australian Mathematical Society* 41 (1990), 151–158, DOI 10.1017/S0004972700017949.
2. E. Hasanalizade, “Upper bounds for infinitary harmonic numbers and infinitary harmonious tuples,” *Bulletin of the Australian Mathematical Society* (2026), DOI 10.1017/S0004972726101324.
3. OEIS A063947, “Infinitary harmonic numbers,” public sequence record initiated 2001-09-03.
