# Finite shifted-prime obstructions to minimum-product prime partitions

## Finding

Let \(A\) be a fixed nonempty finite set of distinct primes with the **least product among all distinct-prime sets of the same sum**. Put \(d=\sum_{p\in A}p\), \(M=\prod_{p\in A}p\), and define the finite set
\[
\Delta_A=\left\{d-\sum_{p\in U}p:\ U\text{ is a finite set of distinct primes},\ \prod_{p\in U}p<M,\ d-\sum_{p\in U}p\equiv0\pmod2\right\}.
\]
The empty set is allowed, with sum zero and product one. Necessarily \(0\notin\Delta_A\). For **every prime \(q>16M^4\)**,
\[
A\cup\{q\}\text{ is minimum-product at sum }d+q
\quad\Longleftrightarrow\quad
q+\delta\text{ is composite for every }\delta\in\Delta_A.
\]
The criterion is effective: \(\Delta_A\) is a finite, computable collection of nonzero even integers. For example, for \(A=\{3,5\}\) one has \(M=15\) and \(\Delta_A=\{6,8\}\), so beyond \(810000\) a prime \(q\) succeeds exactly when neither \(q+6\) nor \(q+8\) is prime. The prime \(810149\) has prime neighbor \(810151\) but both shifts \(810155\) and \(810157\) are composite; thus full prime isolation is not necessary. In particular,
\[
\#\{q\le X:q\text{ prime},\ q>d,\ A\cup\{q\}\text{ is minimum-product}\}
=\pi(X)+O_A\!\left(\frac{X}{(\log X)^2}\right),
\]
and its increasing sequence \(q_A(n)\) satisfies \(q_A(n)\sim n\log n\). The reciprocal sum of the excluded primes converges.

## Assumptions and scope

A *distinct-prime set* means a finite set, not a multiset. Its sum is \(s(U)\), its product \(v(U)\); \(s(\varnothing)=0\) and \(v(\varnothing)=1\). Minimum-product means that every other distinct-prime set \(B\) with the same sum has \(v(B)\ge v(A)\). The minimum-product set is unique by unique prime factorization. The theorem assumes this property for \(A\). The threshold \(16M^4\) is sufficient rather than optimized. All asymptotics hold as \(X,n\to\infty\) with \(A\) fixed. The quantitative count uses the classical Selberg-sieve upper bound for a fixed, nonzero prime-pair shift; no unproved prime-tuple conjecture is used.

## Proof

First, \(s(U)\le v(U)\) for every finite set of distinct primes, including the empty set, by induction (the two-element starting case uses \(ab\ge a+b\) for \(a,b\ge2\), apart from \(a=b=2\) which also gives equality). Consequently \(d\le M\). Any \(U\) in the definition of \(\Delta_A\) has \(v(U)<M\), so it cannot also have \(s(U)=d\), by minimum-product of \(A\). Thus all its shifts are nonzero. Also, any prime in such a \(U\) is smaller than \(M\), showing finiteness and effectivity.

Fix prime \(q>16M^4\). Then \(q>d\), \(q\) is odd, and \(A\cup\{q\}\) is a distinct-prime set with sum \(q+d\) and product \(qM\). Suppose that a different distinct-prime set \(B\) has \(s(B)=q+d\) and \(v(B)\le qM\). Write \(\ell=|B|\), \(t=\max B\), \(U=B\setminus\{t\}\), \(R=v(U)\), and \(u=s(U)\). Then
\[
t=q+d-u,\qquad tR\le qM,\qquad q+d\le\ell t,
\]
so \(R\le \ell qM/(q+d)<\ell M\). Because \(R\ge 2^{\ell-1}\) and \(\ell^2\le 2^{\ell+1}\) for each integer \(\ell\ge1\), we have \(\ell\le2\sqrt R\). Hence \(R<2M\sqrt R\), giving \(R<4M^2\). Moreover \(u\le R\).

From \((q+d-u)R\le qM\), obtain
\[
q(R-M)\le R(u-d).
\]
If \(R>M\), its left side is at least \(q>16M^4\), but its right side is at most \(R^2<16M^4\), a contradiction. If \(R=M\), then \(U=A\) by unique prime factorization; hence \(u=d\), \(t=q\), and \(B=A\cup\{q\}\), also a contradiction. Thus \(R<M\). As \(t=q+d-u\) is prime, \(t>2\) (indeed \(t\ge q+d-R>q-4M^2\)), and \(q\) is odd, the difference \(d-u\) is even. Accordingly \(\delta=d-u\) belongs to \(\Delta_A\), and \(q+\delta=t\) is prime. This proves the obstruction is necessary for a better competing set.

Conversely, suppose \(q+\delta=t\) is prime for some \(\delta=d-u\in\Delta_A\) represented by a set \(U\) with \(R=v(U)<M\). We have \(u\le R<M\), \(d\le M\), and \(q>16M^4\), so \(t=q+\delta>u\) and \(t>\max U\): the set \(B=U\cup\{t\}\) has distinct prime members and sum \(d+q\). Finally,
\[
qM-tR=q(M-R)-R(d-u)>q-2M^2>0,
\]
since \(M-R\ge1\) and \(R|d-u|<2M^2\). Thus \(v(B)<qM\), so \(A\cup\{q\}\) is not minimum-product. The equivalence follows.

Every excluded prime \(q>16M^4\) therefore belongs to at least one prime-pair configuration \((q,q+\delta)\) with fixed nonzero even \(\delta\in\Delta_A\). For each such \(\delta\), the standard two-dimensional upper-bound Selberg sieve gives \(O_\delta(X/(\log X)^2)\) pairs with \(q\le X\). (The textbook twin-prime calculation applies unchanged to any fixed nonzero even shift, with finitely many local factors changed.) Summing over the finite \(\Delta_A\) and absorbing the bounded initial primes yields \(O_A(X/(\log X)^2)\) exceptions. The prime number theorem gives the stated count and \(q_A(n)\sim n\log n\). Partial summation of the exception bound shows that the sum of reciprocal excluded primes converges.

## Verification

The standalone \(\texttt{verify.py}\) performs an independent exact-arithmetic finite check: it enumerates all distinct-prime partitions up to a fixed sum by a descending subset-product recurrence, separately enumerates \(\Delta_A\) from its definition, and compares the computed minimum product to the predicted shifted-prime condition. It checks fixed sets \(\{2\}\), \(\{3\}\), \(\{3,5\}\), and \(\{3,5,19\}\). Execution reports \(\texttt{VERIFY_OK fixed_sets=4 exact_sum_cases=867 even_offsets_for_3_5_19=82}\). In particular \(\Delta_{\{2\}}=\{2\}\), \(\Delta_{\{3\}}=\varnothing\), and \(\Delta_{\{3,5\}}=\{6,8\}\). This finite check is **not** the proof of the theorem and often tests smaller primes than the conservative proven threshold.

## Relationship to prior work

John M. Campbell's 14 October 2026 preprint introduced the minimum-product terminology and, in its Lemma 2, proved that arbitrarily large isolated primes extend any fixed minimum-product set. Its concluding question explicitly asks for the growth of \(q_A(n)\). The present principal contribution is the **necessary-and-sufficient finite shifted-prime test for all sufficiently large extensions**, not merely an isolated-prime sufficient condition. The density-one consequence could also be inferred qualitatively from the original sufficient isolated-prime construction combined with classical prime-pair bounds, so it is **not presented as a standalone novel mechanism**. The exact obstruction structure is finer: it identifies *which specific fixed shifts* can cause an extension to fail.

The Selberg-sieve bound is a standard external input, not claimed to be new. Deléglise and Nicolas studied the related but different problem of maximum prime product with an upper bound on the sum, not this exact-sum minimum-product extension criterion. Searches of available mathematical records and source literature did not find this exact statement; they do not establish absolute priority.

## Limitations

The fixed-set hypothesis is essential: the implicit constant, the shift set, and the threshold depend on \(A\). The threshold has not been optimized and does not classify all smaller primes. The result counts excluded primes from above, not asymptotically sharply; predicting simultaneous-primality counts requires additional conjectural inputs. A full independent priority review and independent mathematical audit have not been performed.

## References

1. John M. Campbell, *On a problem on partitions into distinct primes*, arXiv:2610.19534v1, 14 October 2026, Sections 1–3; especially Lemma 2 and the question defining \(q_A(n)\). https://arxiv.org/html/2610.19534v1
2. J.-M. Evertse, *Selberg's Sieve*, Chapter 12 lecture notes, in particular Section 12.3 on the two-prime upper bound. https://pub.math.leidenuniv.nl/~evertsejh/ANT-Chapter12.pdf
3. M. Deléglise and J.-L. Nicolas, *On the Largest Product of Primes with Bounded Sum*, Journal of Integer Sequences 18 (2015), Article 15.2.8. https://cs.uwaterloo.ca/journals/JIS/VOL18/Deleglise/deleglise3.pdf
