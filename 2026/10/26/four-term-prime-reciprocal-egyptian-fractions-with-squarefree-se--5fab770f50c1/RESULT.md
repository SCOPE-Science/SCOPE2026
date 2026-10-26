# Four-term prime-reciprocal Egyptian fractions with squarefree-semiprime denominators

## Finding

For every prime \(p\), consider representations
\[
\frac1p=\frac1{d_1}+\frac1{d_2}+\frac1{d_3}+\frac1{d_4},
\]
where the four positive integers \(d_i\) are **pairwise distinct**, and each is a product of **two distinct primes**. Such representations are completely classified:

1. For \(p=2\), there are none.
2. For \(p=3\), the only unordered denominator set is \(\{6,14,15,35\}\).
3. For every prime \(p\ge5\), the denominator sets are **exactly**
\[
\left\{2q,2r,qr,pr\right\},\qquad
q=\frac{p+t}{2},\quad r=\frac{p+2+p(p+6)/t}{2},
\]
where \(t\) ranges over the **positive odd divisors** of \(p(p+6)\) for which \(p,q,r\) are pairwise distinct odd primes. Equivalently, the prime parameters satisfy
\[
(2q-p)(2r-p-2)=p(p+6).
\]
Every admissible \(t\) gives a representation, and distinct admissible values give distinct unordered denominator sets. In particular, existence and enumeration for any given \(p\) require only the finite divisor set of \(p(p+6)\).

Examples include \(\frac13=\frac16+\frac1{14}+\frac1{15}+\frac1{35}\) and \(\frac15=\frac16+\frac1{62}+\frac1{93}+\frac1{155}\).

## Assumptions and scope

All primes are ordinary positive rational primes. A squarefree semiprime is a product \(uv\) of **distinct** primes \(u\ne v\). Denominators are distinct, all four summands are positive, the target is precisely \(1/p\), and unordered denominator sets identify representations differing only by a permutation. No claims are made for repeated denominators, higher prime powers, arbitrary positive rational targets, or five or more terms.

## Proof

**Prime-incidence reduction.** Encode the denominators as the four distinct edges of a finite simple graph \(G\), whose vertices are the primes appearing in the denominators. Let \(P\) be the product of all vertices. Multiplying the identity by \(P\) gives
\[
P/p=\sum_{uv\in E(G)}P/(uv).
\]
The right side is integral, so \(p\) must be a vertex. Any vertex \(v\ne p\) has degree at least \(2\): if it had degree \(1\), reduction modulo \(v\) would make the left side and every summand but the unique edge incident to \(v\) vanish, while that one summand would be nonzero, a contradiction. With four edges, \(\deg(p)\le2\), since three or more distinct neighbors each need degree at least two, exceeding the total degree \(8\). If \(\deg(p)=1\), there are exactly three other vertices (fewer cannot support four distinct edges, more would require total degree exceeding \(8\)); they form a triangle with the edge from \(p\) attached to one vertex, a *paw*. If \(\deg(p)=2\), there are exactly three other vertices, all of degree two; hence \(G\) is a four-cycle. These are the only possible graphs.

**The target \(p=2\).** The four smallest possible distinct squarefree semiprime denominators are \(6,10,14,15\). Their reciprocal sum is \(17/42<1/2\), so no four positive summands can represent \(1/2\).

**Four-cycle case.** Name the cycle's vertices consecutively \(p,a,b,c\). The unit-fraction identity reduces, after multiplication by \(pabc\), to
\[
abc=(p+b)(a+c).
\]
Reduction modulo the distinct primes \(a\) and \(c\) gives \(ac\mid(p+b)\). Write \(p+b=kac\) with positive integer \(k\). The displayed equality then implies \(b=k(a+c)\). Since \(b\) is prime and \(a+c>1\), necessarily \(k=1\) and \(b=a+c\); also \(p=ac-a-c\). For \(a+c\) to be prime, exactly one of \(a,c\) is \(2\). Writing the other as \(q\) yields three primes \(p=q-2\), \(q\), \(b=q+2\). Among three consecutive odd numbers spaced by two, one is divisible by three, so the unique possibility is \((p,q,b)=(3,5,7)\). The four edges give denominators \(6,14,15,35\), and direct summation verifies their reciprocal sum is \(1/3\).

**Paw case.** Let the triangle's vertices be distinct primes \(r,b,c\), with pendant edge \(pr\). Multiplication by \(prbc\) gives
\[
rbc=bc+p(r+b+c).
\]
Reduction modulo \(p\) yields \(r\equiv1\pmod p\); in particular, for odd \(p\), the prime \(r\) cannot be \(2\). If \(b,c\) were both odd, then \(rbc\) would be odd while \(bc+p(r+b+c)\) would be even. Exactly one of \(b,c\) is therefore \(2\); write the other \(q\), an odd prime distinct from \(p,r\). The preceding identity becomes
\[
2rq=2q+p(r+q+2),
\]
which is equivalent to
\[
(2q-p)(2r-p-2)=p(p+6).
\]
The first factor is positive, because \(r(2q-p)=p(q+2)+2q>0\). Put \(t=2q-p\), a positive odd divisor of \(p(p+6)\). Solving uniquely gives
\[
q=(p+t)/2,\qquad r=(p+2+p(p+6)/t)/2.
\]
Conversely, whenever these formulas yield pairwise distinct odd primes \(p,q,r\), each denominator \(2q,2r,qr,pr\) is the product of two distinct primes, the four denominators are distinct, and the factored identity reverses to prove the required sum. For \(p=3\), the only possible \(t\) values are \(1,3,9,27\), giving \(q=2,3,6,15\), none an odd prime distinct from \(p\). Thus the four-cycle set is the only \(p=3\) solution. The prime \(p=2\) was excluded above. Uniqueness of the divisor parameter follows from the unique pendant prime \(p\), its neighbor \(r\), and the uniquely determined odd triangle vertex \(q\). This completes the classification.

## Verification

Running `python3 verify.py` with Python 3 standard library returns `VERIFY_OK`. The verifier enumerates every one of the \(\binom{55}{4}=341055\) four-edge selections on the \(11\) primes up to \(31\), computes their reciprocal sums using `fractions.Fraction`, and checks that precisely the two predicted target-prime representations have all vertices in that prime set. Independently it enumerates admissible parameters for target primes up to \(997\) and confirms each resulting four-term identity by exact rational arithmetic. These finite calculations corroborate the algebraic proof but do not substitute for its universal argument.

## Relationship to prior work

Li's 2026 solution to Erdős Problem 306 proves that every positive rational with squarefree reduced denominator admits a finite representation by distinct reciprocal squarefree semiprimes, and explicitly represents semiprimes as edges of a prime graph. That existence theorem does **not** specify the complete structure at exactly four summands or a prime-reciprocal target. The public indexed result *Three-term semiprime Egyptian representations of prime reciprocals* classifies the three-term case by the different factorization \(p+1=(q-1)(r-1)\). The present four-term classification has two graph topologies, a unique cyclic exception, and a new divisor factorization \(p(p+6)\); its assertion does not follow simply from the three-term criterion. Czenky and collaborators treat Egyptian fractions supported on few allowed prime factors, with different restrictions from the squarefree semiprime four-edge problem. Exact-overlap searches did not find a published equivalent, but this is not a proof of priority.

## Limitations

The theorem gives a finite primality test for each target prime, not a characterization of which primes admit any paw representation by elementary congruence classes or a density theorem. It does not determine a uniform bound on the number of representations. Exhaustive verification is restricted to the stated finite ranges. The most relevant sources have been inspected, but an earlier implicit classification, alternative graph phrasing, or an unindexed theorem remains a bibliographic risk. No independent audit has been performed.

## References

1. Shisheng Li, *Unit fractions with semiprime denominators: an elementary proof of Erdős Problem #306*, arXiv:2609.32140v1, first posted 2026-09-26, https://arxiv.org/abs/2609.32140.
2. M. Czenky and collaborators, *Egyptian fractions for few primes*, arXiv:2507.03727, https://arxiv.org/abs/2507.03727.
3. *Three-term semiprime Egyptian representations of prime reciprocals*, public mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-three-term-semiprime-egyptian-representations-of-prime-reciproca--cf632275242a (indexed statement inspected; full manuscript not independently obtained).
