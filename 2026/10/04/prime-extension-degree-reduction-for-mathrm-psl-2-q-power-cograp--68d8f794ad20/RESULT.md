# Prime extension-degree reduction for \(\mathrm{PSL}_2(q)\) power-cographs

## Finding

Let
\[
q=p^f,\qquad f>1,
\]
with \(p\) prime. Then the power graph of \(\mathrm{PSL}_2(q)\) can be a cograph only when the extension degree \(f\) is prime, with the single exception
\[
q=2^4=16.
\]

More precisely, write “admissible” for an integer that is either a prime power or the product of two distinct primes.

If \(p=2\), then:

- for even \(f\), the power graph is a cograph exactly for \(f=2\) and \(f=4\);
- for odd \(f\), it is a cograph exactly when \(f\) is prime,
\[
\frac{2^f+1}{3}
\]
is prime, and \(2^f-1\) is either prime or a product of two distinct primes.

If \(p\) is odd, then:

- for even \(f\), the power graph is a cograph exactly for \((p,f)=(3,2)\), namely \(q=9\);
- for odd \(f\), necessarily \(f\) is prime and \(p\in\{3,5\}\);
- for \(p=3\) and odd prime \(f\), the exact conditions are
\[
\frac{3^f-1}{2}\ \text{is admissible}
\qquad\text{and}\qquad
\frac{3^f+1}{4}\ \text{is prime};
\]
- for \(p=5\) and odd prime \(f\), the exact conditions are
\[
\frac{5^f-1}{4}\ \text{is prime}
\qquad\text{and}\qquad
\frac{5^f+1}{6}\ \text{is prime}.
\]

Thus the unresolved number-theoretic search for non-prime fields in the \(\mathrm{PSL}_2(q)\) power-cograph problem reduces to prime extension degrees, and in odd characteristic to base primes \(3\) and \(5\).

## Assumptions and scope

The power graph of a finite group has the group elements as vertices, with two distinct elements adjacent when one is a positive power of the other. A cograph is a graph with no induced \(4\)-vertex path.

The starting classification theorem of Cameron, Manna, and Mehatari states that for odd \(q\ge5\), \(\mathrm{PSL}_2(q)\) is a power-cograph group exactly when each of
\[
\frac{q-1}{2},\qquad \frac{q+1}{2}
\]
is admissible; for \(q\) a power of \(2\), the corresponding condition is that each of
\[
q-1,\qquad q+1
\]
is admissible.

The proof below only sharpens those arithmetic conditions for non-prime fields \(q=p^f\). It does not settle whether infinitely many prime extension degrees satisfy the remaining primality conditions.

We use the Bang--Zsigmondy theorem in the following standard form: if \(a>b>0\) are coprime, then \(a^n-b^n\) has a prime divisor not dividing any \(a^k-b^k\) with \(1\le k<n\), apart from the classical exceptional cases. None of the applications below lies in an exceptional case.

## Proof

First suppose \(p=2\).

If \(f=2m\) is even, then
\[
2^f-1=(2^m-1)(2^m+1),
\]
and the two factors are coprime and greater than \(1\). If \(m\) is odd and \(m>1\), then \(2^m+1\) is divisible by \(3\) and is greater than \(3\), hence composite. If \(m\) is even and \(m>2\), then \(2^m-1\) is divisible by \(3\) and is greater than \(3\), hence composite. Therefore \(2^f-1\) cannot be admissible unless \(m=1\) or \(m=2\). Both cases work:
\[
f=2:\quad 2^f-1=3,\quad 2^f+1=5,
\]
and
\[
f=4:\quad 2^f-1=15,\quad 2^f+1=17.
\]

Now let \(f\) be odd. Since \(3\mid 2^f+1\), admissibility of \(2^f+1\) forces
\[
\frac{2^f+1}{3}
\]
to be prime, except potentially when \(2^f+1\) is a power of \(3\). But if
\[
2^f+1=3^k
\]
with \(f\ge3\) odd, reduction modulo \(8\) forces \(k\) even. Writing \(k=2r\) gives
\[
(3^r-1)(3^r+1)=2^f.
\]
Both factors must be powers of \(2\), and two powers of \(2\) differing by \(2\) are \(2\) and \(4\). Hence \(r=1\), \(k=2\), and \(f=3\), which is already included because \((2^3+1)/3=3\) is prime.

If odd \(f\) is composite, write \(f=ab\) with \(a,b>1\) odd. Then
\[
2^a+1
\]
is a proper composite divisor of \(2^f+1\), because it is divisible by \(3\) and exceeds \(3\). Hence \(2^f+1\) cannot be a product of two distinct primes. It also cannot be a prime power by the preceding \(3\)-power argument. Thus odd \(f\) must be prime.

Finally, for odd \(f\ge3\), \(2^f-1\) cannot be a proper prime power. Indeed, if
\[
2^f-1=r^k
\]
with \(k>1\), then even \(k\) contradicts \(2^f-1\equiv7\pmod 8\). If \(k\) is odd, then
\[
2^f=r^k+1=(r+1)(r^{k-1}-r^{k-2}+\cdots-r+1),
\]
whose second factor is an odd integer greater than \(1\), impossible for a power of \(2\). Thus the condition on \(2^f-1\) reduces exactly to being prime or the product of two distinct primes.

Now suppose \(p\) is odd.

If \(f\) is even and \(p\ne3\), then \(p^f\equiv1\pmod8\) and \(p^f\equiv1\pmod3\). Hence
\[
\frac{p^f-1}{2}
\]
is divisible by \(4\) and by \(3\), so it is neither a prime power nor a product of two distinct primes.

If \(p=3\) and \(f=2m\), admissibility of
\[
\frac{3^f-1}{2}
\]
forces it to be a power of \(2\), because it is divisible by \(4\). Therefore
\[
(3^m-1)(3^m+1)
\]
is a power of \(2\). The two factors differ by \(2\), so they must be \(2\) and \(4\). Thus \(m=1\), \(f=2\), and \(q=9\). Conversely,
\[
\frac{9-1}{2}=4,\qquad \frac{9+1}{2}=5,
\]
so \(q=9\) works.

Assume next that \(f\) is odd and composite. Write \(f=ab\) with \(a,b>1\) odd. Then
\[
\frac{p^f+1}{2}
=
\frac{p^a+1}{2}
\left(p^{a(b-1)}-p^{a(b-2)}+\cdots-p^a+1\right).
\]
The first factor is itself composite:
\[
\frac{p^a+1}{2}
=
\frac{p+1}{2}
\left(p^{a-1}-p^{a-2}+\cdots-p+1\right),
\]
with both factors greater than \(1\). Thus \((p^f+1)/2\) cannot be the product of two distinct primes.

To rule out a prime power, apply Bang--Zsigmondy to \(p^{2f}-1\). There is a primitive prime divisor \(r\) of \(p^{2f}-1\). It divides \(p^f+1\), but it does not divide \(p^{2a}-1\), hence does not divide \(p^a+1\). Therefore \((p^f+1)/2\) has a prime divisor outside the proper composite factor \((p^a+1)/2\), so it is not a prime power. Hence odd \(f\) must be prime.

Let \(f\ge3\) now be an odd prime. Factor
\[
\frac{p^f-1}{2}
=
\frac{p-1}{2}\Phi_f(p),
\qquad
\frac{p^f+1}{2}
=
\frac{p+1}{2}\Phi_{2f}(p).
\]
Bang--Zsigmondy supplies a prime divisor of \(\Phi_f(p)\) that does not divide \(p-1\), and a prime divisor of \(\Phi_{2f}(p)\) that does not divide \(p+1\).

If \(p>3\), both \((p-1)/2\) and \((p+1)/2\) exceed \(1\). Since each displayed quantity must be admissible while already having a prime divisor outside its first factor, each first factor must itself be prime. These two first factors are consecutive integers, so the only possibility is
\[
\frac{p-1}{2}=2,\qquad \frac{p+1}{2}=3,
\]
and therefore \(p=5\).

For \(p=3\),
\[
\frac{3^f-1}{2}=\Phi_f(3),
\qquad
\frac{3^f+1}{2}=2\Phi_{2f}(3)
=2\frac{3^f+1}{4}.
\]
The second factor after \(2\) is odd and greater than \(1\), so admissibility is equivalent to its being prime. This yields exactly the stated \(p=3\) criterion.

For \(p=5\),
\[
\frac{5^f-1}{2}=2\Phi_f(5)
=2\frac{5^f-1}{4},
\]
so admissibility is equivalent to \((5^f-1)/4\) being prime. Also
\[
\frac{5^f+1}{2}=3\Phi_{2f}(5)
=3\frac{5^f+1}{6}.
\]
A primitive divisor of \(5^{2f}-1\) does not divide \(5^2-1\), so \(\Phi_{2f}(5)\) has a prime divisor different from \(3\). Consequently the second displayed number cannot be a power of \(3\); admissibility is therefore equivalent to \((5^f+1)/6\) being prime. This proves the exact \(p=5\) criterion and completes the proof.

## Verification

The proof is symbolic and uses only the published \(\mathrm{PSL}_2(q)\) power-cograph criterion plus the Bang--Zsigmondy theorem.

The included replay independently factors the relevant integers and compares the published criterion with the reduced criterion for:

- \(p=2\) and every \(2\le f\le31\);
- odd primes \(p\in\{3,5,7,11\}\) and every \(2\le f\le9\).

Every tested case agrees. In particular, the characteristic-\(2\) passing degrees through \(31\) are
\[
2,3,4,5,7,11,13,17,19,23,31,
\]
matching the published list on that range, while among the tested non-prime odd-characteristic fields the passing examples are
\[
3^2,\quad 3^3,\quad 3^5,\quad 3^7.
\]
The replay returns `VERIFY_OK`.

Finite computation is not used to justify the universal theorem.

## Relationship to prior work

Manna, Cameron, and Mehatari first isolated the \(\mathrm{PSL}_2(q)\) question and explicitly observed that it becomes number-theoretic. For \(q=2^f\), they already showed that even \(f\) gives only \(q=4,16\), and for odd \(f\) they recorded the necessary condition that \((2^f+1)/3\) be prime. They also listed several arithmetic patterns for odd \(q\), without reducing non-prime fields to prime extension degrees or to the base primes \(3\) and \(5\).

Cameron, Manna, and Mehatari subsequently proved the exact finite-simple-group criterion used here: for \(\mathrm{PSL}_2(q)\), the two torus orders must each be a prime power or the product of two distinct primes. They described the remaining determination of the admissible \(q\) as a difficult number-theoretic problem.

Brachter and Kaja later classified non-solvable power-cograph groups relative to precisely these \(\mathrm{PSL}_2(q)\) and Suzuki-group number-theoretic obstacles, again leaving those arithmetic questions as the remaining obstruction.

The present result does not solve the residual primality questions. Its contribution is a structural reduction for non-prime fields: apart from \(q=16\), only prime extension degrees need be considered, and odd characteristic collapses further to \(p=3\) or \(p=5\).

## Limitations

The theorem concerns only the \(\mathrm{PSL}_2(q)\) branch of the finite-simple power-cograph classification. It does not address the corresponding Suzuki-group arithmetic conditions.

The remaining prime-extension conditions contain genuine unresolved primality questions. In particular, no infinitude statement is proved.

The originality search covered the principal power-cograph papers, their exact theorem statements, the later non-solvable classification, published-finding corpus records, and targeted searches under the phrases “extension degree”, “prime power field”, “Zsigmondy”, and the cyclotomic specializations. An equivalent reduction could still exist in unindexed literature or be implicit in unpublished notes.

## References

1. P. Manna, P. J. Cameron, and R. Mehatari, “Forbidden Subgraphs of Power Graphs,” *Electronic Journal of Combinatorics* 28(3) (2021), P3.4, DOI 10.37236/9961, arXiv:2010.05198.
2. P. J. Cameron, P. Manna, and R. Mehatari, “On finite groups whose power graph is a cograph,” *Journal of Algebra* 591 (2022), 59–74, DOI 10.1016/j.jalgebra.2021.09.034, arXiv:2106.14217.
3. J. Brachter and E. Kaja, “Classification of non-solvable groups whose power graph is a cograph,” *Journal of Group Theory* (2023), DOI 10.1515/jgth-2022-0081, arXiv:2203.02362.
4. K. Zsigmondy, “Zur Theorie der Potenzreste,” *Monatshefte für Mathematik und Physik* 3 (1892), 265–284.
