# The two-almost-prime barrier for equal consecutive aliquot sums
## Finding

Let \(s(n)=\sigma(n)-n\) be the sum of the proper positive divisors of \(n\), and let \(\Omega(n)\) count prime factors with multiplicity, with \(\Omega(1)=0\). For every integer \(n\ge 1\),
\[
s(n)=s(n+1),\qquad \Omega(n)\le 2,\qquad \Omega(n+1)\le 2
\]
holds if and only if \(n=2\). Equivalently, every solution with \(n>2\) satisfies
\[
\max\{\Omega(n),\Omega(n+1)\}\ge 3.
\]

## Assumptions and scope

All primes are positive rational primes. The theorem is unbounded: neither \(n\) nor the prime factors are subject to a numerical cutoff. An integer with \(\Omega\le2\) is \(1\), a prime, a prime square, or a product of two distinct primes.

## Proof

The case \(n=1\) fails because \(s(1)=0\) and \(s(2)=1\). If exactly one of two consecutive integers is prime and the other is composite, equality is impossible: a prime has aliquot sum \(1\), whereas a composite integer has aliquot sum strictly larger than \(1\). If both are prime, the only consecutive prime pair is \(2,3\), and \(s(2)=s(3)=1\). Thus \(n=2\) is a solution.

It remains to exclude the case where both \(n\) and \(n+1\) are composite and have \(\Omega\le2\). Each is then either a prime square or a product of two distinct primes.

Two prime squares cannot be consecutive, since two positive squares cannot differ by \(1\).

Suppose \(n=p^2\) and \(n+1=qr\), where \(q\) and \(r\) are distinct primes. Equality of aliquot sums gives
\[
1+p=1+q+r,
\]
so \(p=q+r\). But \(qr=p^2+1\), whereas
\[
qr\le \frac{(q+r)^2}{4}=\frac{p^2}{4},
\]
a contradiction.

Suppose \(n=pq\) and \(n+1=r^2\), where \(p,q\) are distinct primes. Equality gives \(p+q=r\), while consecutiveness gives \(r^2=pq+1\). Hence
\[
pq+1=(p+q)^2>pq+1,
\]
again a contradiction.

Finally suppose
\[
n=pq,\qquad n+1=uv,
\]
with \(p<q\) and \(u<v\) distinct primes. Equality of aliquot sums gives
\[
p+q=u+v=:S.
\]
Because \(uv=pq+1>pq\), and the function \(x(S-x)\) is strictly increasing for \(0<x<S/2\), we have \(u>p\). Put \(t=u-p\ge1\). Then \(v=q-t\), and
\[
1=uv-pq=t(q-p-t).
\]
Both factors on the right are positive integers, so \(t=1\) and \(q-p-t=1\). Thus \(u=p+1=q-1=v\), contradicting \(u<v\). This exhausts all possibilities and proves the theorem.

## Verification

The accompanying `verify.py` independently evaluates \(\Omega\) and \(s\) from prime factorizations for every \(1\le n\le200000\), retains only pairs for which both multiplicities are at most \(2\), and confirms that the only equality is \(n=2\). This finite computation is regression evidence only; the proof above is the unbounded argument.

## Relationship to prior work

Lebowitz-Lockard and Vandehey study constant runs of the sum-of-proper-divisors function. They prove that six consecutive equal values are impossible and explicitly note that they are unaware of papers resolving \(s(n)=s(n+1)\); they report the question whether \(n=2\) is the only solution and the computation excluding other solutions through \(10^{16}\). The present result does not resolve that open equation globally. It isolates its entire first two prime-factor-multiplicity layers: any further solution must have at least three prime factors, counted with multiplicity, in one of the two consecutive integers.

The equation is equivalently
\[
\sigma(n+1)=\sigma(n)+1.
\]
This differs from the Erdős--Sierpiński equation \(\sigma(n+1)=\sigma(n)\). Results for equal full divisor sums therefore do not imply the theorem here.

## Limitations

The theorem gives no classification once either integer has \(\Omega\ge3\), and it does not prove that \(n=2\) is the only unrestricted solution. The computational check is deliberately bounded and is not used to justify the infinite statement. Literature searches cannot rule out an obscure or poorly indexed prior observation, although the focal paper's discussion, the cited MathOverflow thread, OEIS A001065, and targeted statement-level searches revealed no covering result.

## References

1. N. Lebowitz-Lockard and J. Vandehey, “Arithmetic Functions that Remain Constant on Runs of Consecutive Integers,” *Journal of Integer Sequences* 26 (2023), Article 23.8.4. https://cs.uwaterloo.ca/journals/JIS/VOL26/Lebowitz/lebo10.html
2. A. Frank, “Are there pairs of consecutive integers with the same sum of factors?”, MathOverflow question 14459. https://mathoverflow.net/q/14459
3. OEIS Foundation Inc., A001065, “Sum of proper divisors (or aliquot parts) of \(n\).” https://oeis.org/A001065
