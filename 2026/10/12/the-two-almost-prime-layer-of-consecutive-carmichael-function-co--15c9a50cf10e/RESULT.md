# The two-almost-prime layer of consecutive Carmichael-function coincidences
## Finding
Let \(\lambda(n)\) be Carmichael's function, the exponent of the unit group modulo \(n\), and let \(\Omega(n)\) count prime factors with multiplicity. For every integer \(n\ge2\),
\[
\lambda(n)=\lambda(n+1),\qquad \Omega(n)\le2,\qquad \Omega(n+1)\le2
\]
holds if and only if
\[
n=3.
\]
Hence \((3,4)\) is the unique consecutive equal-\(\lambda\) pair whose two members are each prime or semiprime, with prime squares counted as semiprimes. In particular, every solution with \(n>3\) satisfies
\[
\max\{\Omega(n),\Omega(n+1)\}\ge3.
\]

## Assumptions and scope
For an odd prime \(p\) and integer \(a\ge1\),
\[
\lambda(p^a)=p^{a-1}(p-1).
\]
Also \(\lambda(2)=1\), \(\lambda(4)=2\), and for coprime prime-power factors the Carmichael function is their least common multiple.

The restriction \(n\ge2\) excludes the conventional trivial equality \(\lambda(1)=\lambda(2)=1\). The condition \(\Omega(m)\le2\) means that \(m\) is prime, a prime square, or a product of two distinct primes.

## Proof
Among two consecutive integers, exactly one is even. If an even integer \(e\) satisfies \(\Omega(e)\le2\), then
\[
e\in\{2,4\}\quad\text{or}\quad e=2p
\]
for an odd prime \(p\).

The small even cases are immediate. The pair \((2,3)\) has Carmichael values \(1\) and \(2\). The pair \((3,4)\) has equal value \(2\), while \((4,5)\) has values \(2\) and \(4\). Thus it remains to treat
\[
e=2p
\]
with \(p\) an odd prime. Then
\[
\lambda(e)=p-1.
\]
Let \(o\) be the adjacent odd integer, so \(o=2p-1\) or \(o=2p+1\), and assume \(\Omega(o)\le2\).

If \(o=r\) is prime, then \(\lambda(o)=r-1\). For \(r=2p-1\) this equals \(2(p-1)>p-1\), and for \(r=2p+1\) it equals \(2p>p-1\). So the prime case is impossible.

If \(o=r^2\) is a prime square, then
\[
\lambda(o)=r(r-1).
\]
If \(r^2=2p-1\), then
\[
p-1=\frac{r^2-1}{2}<r(r-1).
\]
If \(r^2=2p+1\), equality \(p-1=r(r-1)\) would give
\[
\frac{r^2-3}{2}=r(r-1),
\]
or
\[
r^2-2r+3=0,
\]
which has negative discriminant. Thus the prime-square case is impossible.

It remains to let
\[
o=qr
\]
with distinct odd primes \(q<r\). Put
\[
d=\gcd(q-1,r-1).
\]
Then \(d\ge2\), \(d\le q-1\), and
\[
\lambda(o)=\operatorname{lcm}(q-1,r-1)=\frac{(q-1)(r-1)}{d}.
\]
Assume this equals \(p-1\).

If \(qr=2p-1\), then
\[
qr=2\frac{(q-1)(r-1)}{d}+1.
\]
After multiplication by \(d\),
\[
(2-d)qr=2q+2r-2-d.
\]
For \(d=2\), the left side is \(0\) while the right side is positive. For \(d>2\), the left side is negative, while
\[
2q+2r-2-d\ge q+2r-1>0,
\]
a contradiction.

If \(qr=2p+1\), then similarly
\[
qr=2\frac{(q-1)(r-1)}{d}+3,
\]
so
\[
(2-d)qr=2q+2r-2-3d.
\]
For \(d=2\), the right side is \(2q+2r-8>0\). For \(d>2\), the left side is negative, while using \(d\le q-1\),
\[
2q+2r-2-3d\ge 2r-q+1>0.
\]
Again there is a contradiction.

Every possible form of the odd member has now been excluded when the even member is \(2p\). Therefore the only solution with \(n\ge2\) is \(n=3\).

## Verification
The accompanying checker evaluates the Carmichael function from its prime-power formula and tests every \(n\le2{,}000{,}000\). It finds the only solution satisfying both multiplicity bounds at \(n=3\). The same scan records many unrestricted consecutive coincidences, confirming that the theorem is a low-complexity structural classification rather than a claim that consecutive coincidences do not occur.

The finite scan is corroborative only. The unrestricted conclusion under \(\Omega(n),\Omega(n+1)\le2\) follows from the complete case split above.

## Relationship to prior work
Ford, Luca and Pomerance study Carmichael's function as an arithmetic function and determine the order of magnitude of its value set. Their archival paper states the prime-power and least-common-multiple formulas used here and has primary classification \(11A25\). Its complete text does not discuss consecutive equal values, semiprimes, or the equation \(\lambda(n)=\lambda(n+1)\).

Lebowitz-Lockard and Vandehey later study arithmetic functions that remain constant on runs of consecutive integers. For Carmichael's function they prove an upper bound for the maximum run length up to \(x\), namely
\[
F_\lambda(x)\ll(\log x\,\log_2 x)^2.
\]
Their Carmichael section uses the same prime-power formula but does not classify the two-almost-prime layer and contains no semiprime statement.

OEIS A002322 records Carmichael's function itself and its prime-power formula. It does not provide the classification proved here.

## Limitations
The theorem only classifies the layer in which both consecutive integers have at most two prime factors counted with multiplicity. It does not classify all solutions of \(\lambda(n)=\lambda(n+1)\), and such unrestricted solutions are plentiful computationally.

The result is structurally close to low-factor classifications for other arithmetic-function coincidences, but the least-common-multiple behavior of \(\lambda\) requires a separate semiprime argument through \(d=\gcd(q-1,r-1)\).

## References
1. K. Ford, F. Luca and C. Pomerance, “The image of Carmichael's \(\lambda\)-function”, arXiv:1408.6506v1, submitted 27 August 2014; *Algebra & Number Theory* 8 (2014), 2009–2025.
2. N. Lebowitz-Lockard and J. Vandehey, “Arithmetic Functions that Remain Constant on Runs of Consecutive Integers”, *Journal of Integer Sequences* 26 (2023), Article 23.8.4.
3. OEIS Foundation, A002322, “Carmichael lambda function”.
