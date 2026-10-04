# Exact \(99.681\%\) density from the full Table-7 totient collision envelope

## Finding
For each positive integer \(c\), define
\[
f_c(n)=(n+c)\varphi(n),
\]
and let
\[
A=\{c\ge1:f_c\text{ is not injective on the positive integers}\}.
\]

Noppakaew and Pongsriiam give \(28\) distinct pairs \((a,b)\) in their Table 7 with
\[
f_1(a)=f_1(b).
\]
Their Lemma 19(iii) implies that, for any one of these pairs,
\[
\gcd(c,ab)=1
\quad\Longrightarrow\quad
f_c(ca)=f_c(cb).
\]
Thus every such \(c\) belongs to \(A\).

Let \(U\) be the union, over all \(28\) Table-7 pairs, of the corresponding coprimality classes
\[
U_{a,b}=\{c\ge1:\gcd(c,ab)=1\}.
\]
Then \(U\) has the exact natural density
\[
d(U)=
\frac{
261806484037693243959002547710701698711688881953592878066348537
}{
262644288415413354670375252365059773178132935923609006683897535
},
\]
which is
\[
d(U)=0.9968101176584697\ldots.
\]

Consequently,
\[
\underline d(A)\ge0.9968101176584697\ldots.
\]

The published lower bound is
\[
\underline d(A)\ge0.981728.
\]
Using the full Table-7 collision envelope therefore improves the certified proportion by about \(1.5082\) percentage points. Equivalently, the proportion not covered by these particular certificates falls from at most \(1.8272\%\) under the published bound to exactly
\[
0.3189882341530271\ldots\%
\]
for the full Table-7 envelope.

## Assumptions and scope
The only external mathematical input is the published collision propagation lemma: if \(f_1(a)=f_1(b)\) and \(\gcd(c,ab)=1\), then \(f_c(ca)=f_c(cb)\). The \(28\) seed pairs are exactly the pairs printed in Table 7 of the same paper.

The exact density is the density of the union of these \(28\) sufficient coprimality conditions. It is not claimed to be the exact density of \(A\). There may be additional values of \(c\) for which \(f_c\) is noninjective by other mechanisms.

## Proof
For a Table-7 pair \((a,b)\), the source gives
\[
(a+1)\varphi(a)=(b+1)\varphi(b).
\]
If
\[
\gcd(c,ab)=1,
\]
multiplicativity of the Euler totient gives
\[
\varphi(ca)=\varphi(c)\varphi(a)
\quad\text{and}\quad
\varphi(cb)=\varphi(c)\varphi(b).
\]
Therefore
\[
\begin{aligned}
f_c(ca)
&=(ca+c)\varphi(ca)\\
&=c(a+1)\varphi(c)\varphi(a),
\end{aligned}
\]
and similarly
\[
f_c(cb)=c(b+1)\varphi(c)\varphi(b).
\]
The Table-7 equality makes these values equal. This reconstructs the relevant instance of the source's Lemma 19(iii).

For each Table-7 pair, let
\[
S_{a,b}=\{p:p\text{ is prime and }p\mid ab\}.
\]
The certificate \(\gcd(c,ab)=1\) depends only on whether each prime in \(S_{a,b}\) divides \(c\). Four of the \(28\) support sets properly contain another support set, so their coprimality events are redundant. The same union \(U\) is therefore represented by \(24\) irredundant support sets.

Across those support sets there are \(36\) relevant primes. Put
\[
M=\prod p
=
17908663449893375001554206957763965693924172368887203729748237321510,
\]
where the product is over those \(36\) primes. Membership in \(U\) is periodic modulo \(M\), so \(d(U)\) is the proportion of residue classes modulo \(M\) that satisfy at least one of the \(24\) irredundant coprimality conditions.

The residue count can be done exactly by a finite prime-by-prime recurrence. Index the \(24\) support sets. After processing some relevant primes, a state records which support sets have already been hit by a prime divisor of \(c\). When the next prime is \(p\), there are \(p-1\) residue classes modulo \(p\) in which \(p\nmid c\), leaving the hit state unchanged, and one class in which \(p\mid c\), which adds every support set containing \(p\) to the hit state.

After all \(36\) primes are processed, the full hit state is precisely the set of residue classes for which every coprimality certificate fails. The exact recurrence gives
\[
57126529299223468965659239562059665568954263999519745916195977628
\]
such classes. Hence the number of certified classes is
\[
17851536920594151532588547718201906028355218104887683983832041343882.
\]
Dividing by \(M\) and reducing gives the density stated above.

Since
\[
U\subseteq A,
\]
the same number is a lower bound for the lower natural density of \(A\).

## Verification
The accompanying `verify.py` independently evaluates \(\varphi\) and confirms all \(28\) printed seed collisions. It factors every product \(ab\), removes only support sets whose coprimality events are logically redundant, rebuilds the \(36\)-prime modulus, and performs the exact integer residue-state recurrence described in the proof.

The checker verifies both the unreduced certified residue count and the reduced density fraction. A successful replay prints `VERIFY_OK`.

The computation is finite and exhaustive for the explicitly defined Table-7 certificate union because membership in that union depends only on divisibility by the \(36\) relevant primes.

## Relationship to prior work
The primary paper proves the propagation lemma and supplies the \(28\) Table-7 seed collisions. Its Theorem 23 uses only three selected coprimality conditions to obtain
\[
|A(N)|\ge0.981728N+O(1).
\]
The paper does not combine all Table-7 seed pairs into one exact periodic union and does not state the density \(0.9968101176584697\ldots\).

Targeted searches for the exact density, the exact reduced fraction, the full Table-7 envelope, and a \(99.681\%\) lower-density statement for \((n+c)\varphi(n)\) did not locate a prior statement. Searches for stronger later results proving noninjectivity for every \(c\) also did not locate such a theorem.

## Limitations
This result does not answer the paper's question whether \(f_c\) is noninjective for every positive integer \(c\). The remaining
\[
0.3189882341530271\ldots\%
\]
is only the portion not covered by these particular Table-7 coprimality certificates; some or all of it may be covered by other arguments.

The exact density calculation is specific to the finite collision table printed in the source. Adding new seed collisions can enlarge the certificate union further.

## References
1. Passawan Noppakaew and Prapanpong Pongsriiam, “Product of Some Polynomials and Arithmetic Functions,” *Journal of Integer Sequences* 26 (2023), Article 23.9.1, published 2 November 2023.
