# Power-map counterexamples to composition closure of quasi-injective functions
## Finding
For every integer \(k\ge2\), set
\[
G_k(n)=n^k
\]
and
\[
F_k(n)=\begin{cases}1,&n\text{ is a perfect }k\text{-th power},\\ n,&\text{otherwise}.\end{cases}
\]
Both \(F_k\) and \(G_k\) are quasi-injective. The inner map \(G_k\) is, in fact, injective and completely multiplicative. Nevertheless,
\[
(F_k\circ G_k)(n)=1
\]
for every positive integer \(n\), so the composition is not quasi-injective. This gives a negative answer to the first part of Pongsriiam's Question 19 and shows that complete multiplicativity together with injectivity of the inner map does not replace the surjectivity hypothesis in the sufficient condition stated there.

## Assumptions and scope
A function \(f:\mathbb N\to\mathbb C\) is called quasi-injective when
\[
f(an)=f(bn)\text{ for every }n\in\mathbb N
\]
implies \(a=b\). Here \(\mathbb N\) denotes the positive integers. The result concerns arbitrary integers \(k\ge2\) and uses no unproved hypothesis.

## Proof
Fix \(k\ge2\). The map \(G_k\) is injective because \(a^k=b^k\) for positive integers implies \(a=b\). It is completely multiplicative because
\[
G_k(mn)=(mn)^k=m^kn^k=G_k(m)G_k(n).
\]
Hence \(G_k\) is quasi-injective.

To prove that \(F_k\) is quasi-injective, let \(a\ne b\). Choose a prime \(r\) that divides neither \(a\) nor \(b\). In each of \(ar\) and \(br\), the exponent of \(r\) in the prime factorization is exactly \(1\). Since \(k\ge2\), neither number can be a perfect \(k\)-th power. Therefore
\[
F_k(ar)=ar\qquad\text{and}\qquad F_k(br)=br.
\]
Because \(a\ne b\), these two values are unequal. Thus it is impossible to have \(F_k(an)=F_k(bn)\) for every \(n\), proving quasi-injectivity of \(F_k\).

Finally, \(G_k(n)=n^k\) is always a perfect \(k\)-th power, so
\[
F_k(G_k(n))=F_k(n^k)=1
\]
for every \(n\). The constant function is not quasi-injective: for example, its values at \(n\) and \(2n\) agree for every \(n\), although \(1\ne2\). This proves the claim.

## Verification
The proof is symbolic. A standalone exact-integer regression program additionally checked the construction for every \(2\le k\le8\). It performed 100800 complete-multiplicativity checks for \(G_k\), 3500 injectivity value checks, 49980 constructive quasi-injectivity witness checks for \(F_k\), and 14000 checks that \(F_k(G_k(n))=1\). The program returned `VERIFY_OK`.

## Relationship to prior work
Pongsriiam introduced the above notion of quasi-injectivity and asked in Question 19 whether the composition of two quasi-injective functions must be quasi-injective. The same question notes the sufficient hypothesis that the inner function be both surjective and completely multiplicative. The construction here gives an infinite family of counterexamples, even with the inner function injective and completely multiplicative. Thus the first question has a negative answer, while the broader requested categorization remains open. A separate positive result for right composition by iterates of the divisor-counting function does not imply this counterexample family: it concerns a special surjective inner map and establishes preservation rather than failure.

## Limitations
The result does not characterize all pairs \((f,g)\) for which \(f\circ g\) is quasi-injective. It also does not assert that every useful sufficient condition must literally contain surjectivity; it proves only that complete multiplicativity plus injectivity of the inner map is insufficient in general. The computational checks are regression tests and are not used as an infinite proof.

## References
P. Pongsriiam, “Quasi-Injectivity of Some Arithmetic Functions,” Journal of Integer Sequences 24 (2021), Article 21.10.1, 1–13. Published November 8, 2021. Primary MSC 11A25.
