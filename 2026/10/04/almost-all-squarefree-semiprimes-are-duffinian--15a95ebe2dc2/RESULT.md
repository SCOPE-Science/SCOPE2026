# Almost all squarefree semiprimes are Duffinian
## Finding
Let \(S_2(x)\) be the number of squarefree semiprimes
\[
n=pq\le x,\qquad p<q,
\]
and let \(D_2(x)\) count those for which
\[
\gcd(n,\sigma(n))=1.
\]
Then
\[
S_2(x)-D_2(x)=O\!\left(\frac{x}{\log x}\right)
\]
and consequently
\[
D_2(x)\sim S_2(x)\sim\frac{x\log\log x}{\log x}.
\]
Thus Duffinian numbers have relative density \(1\) inside the squarefree
semiprimes, even though the set of all integers coprime to their divisor sum has
ordinary density \(0\).

There is also an exact local criterion. If \(p<q\) are primes, then
\[
pq\ \text{is Duffinian}
\quad\Longleftrightarrow\quad
p\ne2\ \text{and}\ q\not\equiv-1\pmod p.
\]

## Assumptions and scope
The ordinary divisor-sum function is
\[
\sigma(n)=\sum_{d\mid n}d.
\]
A Duffinian number is a composite integer \(n\) with
\[
\gcd(n,\sigma(n))=1.
\]
Only squarefree semiprimes are counted here: products of two distinct primes.
Prime squares are excluded from \(S_2(x)\), but their number is
\(O(\sqrt{x}/\log x)\), so this exclusion does not change Landau's leading
semiprime asymptotic.

The analytic inputs are the prime number theorem in the standard semiprime
count, the Brun--Titchmarsh inequality for primes in arithmetic progressions,
and the boundedness of the sum of reciprocal primes over a fixed logarithmic
interval such as \((x^{1/3},x^{1/2})\).

## Proof
For distinct primes \(p<q\),
\[
\sigma(pq)=(p+1)(q+1).
\]
Since \(p\nmid p+1\) and \(q\nmid q+1\), a common prime divisor of \(pq\) and
\(\sigma(pq)\) must come from a cross-divisibility relation. The relation
\(q\mid p+1\) is impossible unless \(p=2\) and \(q=3\), because \(q>p\).
Moreover, if \(p=2\), then \(2\mid q+1\) for every odd prime \(q\). Hence
\[
\gcd(pq,\sigma(pq))=1
\]
holds exactly when \(p\) is odd and
\[
p\nmid q+1,
\]
which is the stated local criterion.

Let \(B(x)=S_2(x)-D_2(x)\). The pairs counted by \(B(x)\) consist of the pairs
with \(p=2\), together with odd primes \(p<q\) satisfying
\[
pq\le x,\qquad q\equiv-1\pmod p.
\]
The contribution from \(p=2\) is
\[
O\!\left(\frac{x}{\log x}\right).
\]

For odd \(p\le x^{1/3}\), put \(y=x/p\). Then \(y/p=x/p^2\ge x^{1/3}\), so
Brun--Titchmarsh gives
\[
\pi(y;p,-1)
\ll
\frac{y}{(p-1)\log(y/p)}
\ll
\frac{x}{p(p-1)\log x}.
\]
Summing over these primes yields
\[
\sum_{\substack{p\le x^{1/3}\\p\ {\rm odd}}}\pi(x/p;p,-1)
\ll
\frac{x}{\log x}\sum_{p\ge3}\frac1{p(p-1)}
\ll
\frac{x}{\log x}.
\]

For \(x^{1/3}<p<\sqrt{x}\), discard the congruence condition. The elementary
prime-counting bound
\[
\pi(t)\ll\frac{t}{\log t}
\]
and \(\log(x/p)\ge\frac12\log x\) give
\[
\pi(x/p)\ll\frac{x}{p\log x}.
\]
Therefore
\[
\sum_{x^{1/3}<p<\sqrt{x}}\pi(x/p)
\ll
\frac{x}{\log x}
\sum_{x^{1/3}<p<\sqrt{x}}\frac1p
\ll
\frac{x}{\log x},
\]
because the prime reciprocal sum over this interval is bounded. Combining the
three ranges proves
\[
B(x)=O\!\left(\frac{x}{\log x}\right).
\]

Landau's theorem for integers with two prime factors gives
\[
S_2(x)\sim\frac{x\log\log x}{\log x}.
\]
The prime-square contribution is lower order, so this is also the asymptotic
for distinct-prime products. Since
\[
\frac{x/\log x}{x\log\log x/\log x}=\frac1{\log\log x}\longrightarrow0,
\]
subtracting \(B(x)\) gives
\[
D_2(x)\sim S_2(x).
\]

## Verification
The proof is unrestricted and symbolic. The accompanying checker exhaustively
enumerates squarefree semiprimes through \(10^6\), computes \(\sigma(pq)\)
directly, and confirms the exact local criterion on every pair. It also reports
the total, Duffinian, and exceptional counts at several cutoffs. These finite
counts are corroborative only and are not used to establish the asymptotic
statement.

## Relationship to prior work
Dressler proved that, for every fixed positive bound, the set of integers whose
greatest common divisor with a divisor-power sum is at most that bound has
ordinary density \(0\). In the case of the ordinary divisor sum and bound \(1\),
this says that integers satisfying \(\gcd(n,\sigma(n))=1\) have ordinary density
\(0\).

Pollack later studied the distribution of \(\gcd(n,\sigma(n))\) in detail. His
paper has primary classification 11N37 and includes Brun--Titchmarsh estimates
for congruences of the form \(q\equiv-1\pmod m\), which are the relevant
analytic mechanism here. The inspected paper does not state a semiprime
relative-density theorem and contains no occurrence of "semiprime" or
"Duffinian".

OEIS A003624 records the Duffinian numbers and attributes the name to Duffy's
1979 paper. It gives values and elementary comments, not the squarefree
semiprime density result proved here.

## Limitations
The theorem concerns relative density inside one thin multiplicative stratum;
it does not contradict the ordinary-density-zero theorem for all integers.
The error term proved here is only
\[
O\!\left(\frac{x}{\log x}\right);
\]
no leading constant for the exceptional semiprimes is claimed.

Duffy's original 1979 article and Luca's 2007 density paper were identified as
highly relevant historical sources. The former was not available in full text
during this verification, and the latter's full-text endpoint was temporarily
unavailable. Their bibliographic records and the exact OEIS database entry were
checked, but no whole-document noncoverage claim is based on inaccessible text.

## References
1. R. E. Dressler, "On a theorem of Niven", Canadian Mathematical Bulletin 17
   (1974), 109--110, DOI 10.4153/CMB-1974-019-5.
2. P. Pollack, "On the greatest common divisor of a number and its sum of
   divisors", Michigan Mathematical Journal 60 (2011), 199--214,
   DOI 10.1307/mmj/1301586311.
3. L. R. Duffy, "The Duffinian numbers", Journal of Recreational Mathematics 12
   (1979), 112--115.
4. F. Luca, "On the densities of some subsets of integers", Missouri Journal of
   Mathematical Sciences 19 (2007), 167--170,
   DOI 10.35834/mjms/1316032973.
5. OEIS Foundation, A003624, "Duffinian numbers".
