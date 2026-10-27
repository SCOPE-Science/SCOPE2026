# Fermat-prime criterion for maximal primitive-normal progressions in quadratic fields

## Finding
For each prime \(p\ge5\), write \(K=\mathbb F_{p^2}\). Let \(T(p)\) be the number of ordered start–difference pairs \((a,b)\in K\times K^\times\) for which the \(p-1\) terms \(a+jb\), \(0\le j\le p-2\), are all primitive in \(K\). Then
\[
T(p)=\begin{cases}\varphi(p^2-1),&p-1\text{ is a power of }2,\\0,&\text{otherwise.}\end{cases}
\]
When the count is positive, the complete set of pairs is \(\{(g,g):g\in K^\times\text{ primitive}\}\). Every primitive element of \(K\) is normal over \(\mathbb F_p\), so these are exactly the primitive-normal progressions in the usual sense. No \(p\)-term nonrepeating progression in \(K\) consists entirely of primitive elements. Equivalently, the maximum possible length \(p-1\) is reached precisely when \(p\) is a Fermat prime (with \(p\ge5\)).

## Assumptions and scope
The base characteristic \(p\) is prime and at least five, the extension degree is exactly two, and differences \(b\) are nonzero. A term is primitive if its multiplicative order is \(p^2-1\); it is normal if its conjugate pair is an \(\mathbb F_p\)-basis. Progressions are ordered by their start and nonzero difference, and only terms indexed from zero to \(p-2\) are included in the count. The condition that \(p-1\) is a power of two is equivalent, for a prime \(p\), to \(p\) being a Fermat prime. No assertion is made about the exact longest progression for non-Fermat primes.

## Proof
**1. Primitivity implies normality in degree two.** If \(z\in K^\times\) is not normal then \(z^p=c z\) for some \(c\in\mathbb F_p^\times\). Applying Frobenius again gives \(c^2=1\), so \(z^p=\pm z\). Thus the order of \(z\) divides \(p-1\) or \(2(p-1)\). Since \(p\ge5\), both are smaller than \(p^2-1\); a primitive element cannot satisfy either relation.

**2. An affine prime-field line avoiding zero has too few primitive points.** Consider the line \(a+\mathbb F_p b\), \(b\ne0\). Suppose \(y=a/b\notin\mathbb F_p\). With \(N\) the norm to \(\mathbb F_p\), we have
\[
N(a+jb)=N(b)\bigl(j^2+\operatorname{Tr}(y)j+N(y)\bigr),\qquad j\in\mathbb F_p.
\]
The monic quadratic \(Q(j)\) in parentheses has no zero in \(\mathbb F_p\) and has nonzero discriminant. For the quadratic character \(\chi\) on \(\mathbb F_p\), the exact identity \(\sum_{j\in\mathbb F_p}\chi(Q(j))=-1\) follows by counting factorizations of that discriminant, or by completing the square. Multiplying \(Q\) by \(N(b)\) can reverse the signs, but in either case at most \((p+1)/2\) norm values are nonsquares. The norm of a primitive element of \(K\) generates \(\mathbb F_p^\times\), hence is a nonsquare. Therefore such a line has at most \((p+1)/2<p-1\) primitive points.

**3. A long progression must be a punctured scalar line.** If all \(p-1\) terms \(a+jb\) are primitive, step 2 forces \(y=a/b\in\mathbb F_p\). Among the \(p\) indices \(j\in\mathbb F_p\), exactly one makes \(a+jb=0\), namely \(j=-y\). Since the progression uses every index except \(p-1\), and all displayed terms are nonzero, necessarily \(-y=p-1=-1\) in \(\mathbb F_p\), so \(y=1\), or \(a=b\). Its term set is exactly \(b\mathbb F_p^\times\).

**4. Characterization of primitive scalar cosets.** Fix a generator \(h\) of cyclic \(K^\times\) of order \(M=p^2-1\). For any primitive \(b=h^k\), \(\gcd(k,M)=1\), and
\[
b\mathbb F_p^\times=\{h^{k+(p+1)t}:0\le t\le p-2\}.
\]
If an odd prime \(\ell\mid p-1\), then \(\ell\nmid p+1\). As \(t\) traverses the displayed range, an exponent \(k+(p+1)t\) is divisible by \(\ell\); the corresponding element is not primitive. Conversely, if \(p-1\) is a power of two, then every prime divisor \(\ell\mid M\) divides \(p+1\) (including \(\ell=2\)). Therefore \(k+(p+1)t\equiv k\not\equiv0\pmod\ell\) for every such prime and every \(t\). Every element of \(b\mathbb F_p^\times\) is primitive. There are exactly \(\varphi(M)\) choices of primitive \(b\), and step 3 proves there are no other valid start–difference pairs.

**5. Optimal length.** A progression of length \(p\) visits an entire prime-field affine line. If it passes through zero, it has a nonprimitive term; if not, step 2 limits primitive terms to \((p+1)/2<p\). Thus length \(p\) is impossible. A positive value of \(T(p)\) attains the longest possible nonrepeating length, \(p-1\). If \(p-1=2^r\) and \(p\) is prime, then \(r\) is itself a power of two, so \(p\) is a Fermat prime; the converse is immediate.

## Verification
The included `verify.py` uses arithmetic in \(\mathbb F_p[u]/(u^2-d)\), with explicit quadratic nonresidues \(d\). It independently enumerates every nonzero difference and start for \(p\in\{5,7,11,17\}\), testing primitivity via exact multiplicative-order exponentiation. The full counts are respectively \(8,0,0,96\), matching \(\varphi(24),0,0,\varphi(288)\). All nonzero counts consist exactly of pairs \((b,b)\). These finite tests do not replace the general character-sum and cyclic-group proof.

## Relationship to prior work
Bagger and Fernando (2026, arXiv:2610.07538v1) study primitive-normal progressions, supplying existence bounds for fixed lengths and many finite fields, notably length four. Lemos, Neumann and Ribas (2022, arXiv:2208.02876v1) provide character-sum and sieve estimates and explicit classifications at lengths two and three. The result here instead fixes extension degree two and asks for the longest nonrepeating progression as the characteristic varies. The exact Fermat-prime criterion and enumeration of all extremal ordered pairs are not statements of the inspected theorems. The argument uses familiar elementary finite-field tools in a new maximal-length combination; this is not a claim that the individual norm or cyclicity lemmas are new.

## Limitations
The result does not compute the longest possible progression for non-Fermat primes, nor handle extension degrees greater than two. The statement is conditional on the existence of further Fermat primes and does not assert their infinitude. Earlier unindexed or implicit literature coverage remains possible. Computational verification covers only the four displayed prime fields; the infinite proof is analytic.

## References
- G. K. Bagger and M. Fernando, *Primitive normal progressions in finite fields*, arXiv:2610.07538v1 (first public 2026-10-06), https://arxiv.org/abs/2610.07538 .
- A. Lemos, V. Neumann and S. Ribas, *On arithmetic progressions in finite fields*, arXiv:2208.02876v1 (2022), https://arxiv.org/abs/2208.02876 .
- J. Sharma, R. Sarma and S. Laishram, *Arithmetic Progressions of r-Primitive Elements in a Field*, Bull. Braz. Math. Soc. (2024), https://doi.org/10.1007/s00574-024-00412-9 .
