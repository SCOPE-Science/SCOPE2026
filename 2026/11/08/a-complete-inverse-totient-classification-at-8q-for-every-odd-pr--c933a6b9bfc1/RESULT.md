# A complete inverse-totient classification at \(8q\) for every odd prime

## Finding

Let \(\varphi\) be Euler's totient function and set \(X_{8q}=\{n\in\mathbb N:\varphi(n)=8q\}\) for an odd prime \(q\). Define \(A=2q+1\), \(B=4q+1\), and \(C=8q+1\). Conditional on primality, define three sets

\[
S_A=\{5A,8A,10A,12A\},\qquad S_B=\{3B,4B,6B\},\qquad S_C=\{C,2C\}.
\]

A set is omitted if its subscripted base is not prime. Then **the following disjoint union is exact for every odd prime**:

\[
X_{8q}=S_A\,\sqcup\,S_B\,\sqcup\,S_C\,\sqcup\,
\begin{cases}
\{45,72,90\},&q=3,\\
\{75,100,150\},&q=5,\\
\varnothing,&q\ge7.
\end{cases}
\]

Therefore, with \(\mathbf1_{\mathcal P}(t)\) denoting the indicator that \(t\) is prime,

\[
|X_{8q}|=4\mathbf1_{\mathcal P}(2q+1)+3\mathbf1_{\mathcal P}(4q+1)
 +2\mathbf1_{\mathcal P}(8q+1)+3\mathbf1_{\{3,5\}}(q).
\]

For \(q\ge7\), if \(q\equiv1\pmod3\), then \(A,C\) are composite, and \(|X_{8q}|=3\mathbf1_{\mathcal P}(B)\). If \(q\equiv2\pmod3\), then \(B\) is composite and \(|X_{8q}|=4\mathbf1_{\mathcal P}(A)+2\mathbf1_{\mathcal P}(C)\). Thus the possible generic sizes are exactly \(\{0,2,3,4,6\}\), witnessed by \(q=19,17,7,23,11\), respectively. The exceptional sizes are \(|X_{24}|=10\) and \(|X_{40}|=9\). In particular, \(|X_{8q}|\ne1\) for all odd primes \(q\).

## Assumptions and scope

All primes and arguments are positive ordinary integers; \(q\) ranges over *all* odd primes, including \(3,5\). A conditional set in the theorem is empty unless its displayed base is actually prime. No primality conjecture is assumed. A complete classification means an equality of sets, not just an upper bound or the existence of examples. Nothing is claimed for general exponents \(s\ge4\) in the family \(\varphi(n)=2^s q\), nor for arbitrary composite \(q\).

## Proof

**1. Exhaustion of prime divisors.** Suppose \(\varphi(n)=8q=2^3q\), and \(\ell\) is a prime factor of \(n\). From \(\ell-1\mid\varphi(n)\), one has \(\ell-1=2^a q^b\) with \(0\le a\le3\) and \(b\in\{0,1\}\). If \(b=0\), the prime candidates are \(2,3,5,9\), hence only \(2,3,5\). If \(b=1\) and \(a=0\), then \(q+1>2\) is even and not prime. For \(a=1,2,3\), the candidates are \(A=2q+1\), \(B=4q+1\), and \(C=8q+1\). Thus every prime factor belongs to \(\{2,3,5,A,B,C\}\), with the proviso that \(A,B,C\) may only occur when prime.

If an actual prime \(P\in\{A,B,C\}\) divides \(n\), it occurs only to exponent one: otherwise \(P\mid\varphi(P^2)\mid8q\), impossible because \(P>q\) and the only primes dividing \(8q\) are \(2,q\). Also \(3^2\mid n\) is possible only if \(q=3\), since \(\varphi(9)=6\mid8q\); similarly \(5^2\mid n\) is possible only if \(q=5\), since \(\varphi(25)=20\mid8q\). For \(2^u\mid n\), exact \(2\)-part divisibility gives \(u\le4\).

**2. Normal branch.** First suppose neither \(3^2\) nor \(5^2\) divides \(n\). The prime-power totients from \(2^u\), \(3\), and \(5\) are powers of \(2\) only, so exactly one actual prime \(P\in\{A,B,C\}\) must divide \(n\) to supply the single factor \(q\) in \(\varphi(n)\). Write

\[
n=2^u3^e5^fP,\quad e,f\in\{0,1\},\quad \varphi(2^u)=2^{\alpha(u)},\qquad
\alpha(0)=\alpha(1)=0,\quad\alpha(u)=u-1\ (u\ge2).
\]

For \(P=2^a q+1\) with \(a\in\{1,2,3\}\), multiplicativity gives the necessary and sufficient equation

\[
\alpha(u)+e+2f=3-a.
\]

For \(a=1\), the complete solutions are \((u,e,f)=(0,0,1),(1,0,1),(2,1,0),(3,0,0)\), producing \(5A,10A,12A,8A\). For \(a=2\), the solutions are \((0,1,0),(1,1,0),(2,0,0)\), giving \(3B,6B,4B\). For \(a=3\), they are \((0,0,0),(1,0,0)\), giving \(C,2C\). Each listed integer indeed has totient \(8q\). This exhausts the normal branch.

**3. The two exceptional square-divisor branches.** If \(3^2\mid n\), then \(q=3\) by Step 1; moreover \(3^3\nmid n\) because \(\varphi(27)=18\nmid24\). The factor \(9\) contributes \(\varphi(9)=6=2q\). No prime \(A,B,C\) can also occur, since each would supply another factor of \(q\). The remaining part is supported on \(2,5\) and must have totient \(24/6=4\), so it is exactly one of \(5,8,10\). The three extra preimages are \(45,72,90\).

If \(5^2\mid n\), then \(q=5\), with \(5^3\nmid n\) since \(\varphi(125)=100\nmid40\). Now \(\varphi(25)=20=4q\), no mixed prime can occur, and the remaining part is supported on \(2,3\) with totient \(40/20=2\). It is exactly one of \(3,4,6\), producing \(75,100,150\). These two cases are exhaustive, since \(q\) cannot simultaneously equal \(3\) and \(5\).

**4. Disjointness, sizes and congruence cases.** The prime bases \(A,B,C\), whenever prime, are distinct and each is greater than \(5\); every member of its conditional set has that prime factor and none of the other two. The exceptional members are precisely those divisible by \(3^2\) or \(5^2\), while all members of the normal branch are not. Hence the union is disjoint and the cardinality formula follows. For \(q\ge7\), if \(q\equiv1\pmod3\), then \(3\mid A,C\), so both are composite; if \(q\equiv2\pmod3\), then \(3\mid B\), so \(B\) is composite. These observations give the asserted size sets. The witnesses are verified by elementary primality checks; examples are also checked by the standalone integer verifier. Every nonempty conditional set has at least two distinct members, and the exceptional contributions contain three, so a singleton never occurs. \(\square\)

## Verification

The standalone `verify.py` uses Python standard-library integer arithmetic. It constructs a totient sieve over \(1\le n\le23940\) and, independently, enumerates all admissible prime-power factorizations for the target totient, without relying on the closed formula. Both computations agree with the formula for every odd prime \(3\le q\le997\) (167 primes), including both exceptions. The full conditional sets are also checked via direct totient products. Run with `python verify.py` from the extracted package directory. Finite checks are corroboration, **not** the proof of the unrestricted prime-parameter theorem; that proof is Steps 1–4.

## Relationship to prior work

Tian-Xiao He, *The Family \(X_{qp^s}\) for Distinct Primes \(q,p\) in Connection with Carmichael's Totient Conjecture* (arXiv:2610.34808v1, posted October 26, 2026), §5, resolves the mirror family at \(s\le2\), and explicitly poses the complete classification for \(s\ge3\) as Open Problem 16. Its Table 2 gives the *sizes* of \(X_{8q}\) at six primes \(q\equiv1\pmod6\) but not the uniform exact set, the exceptional \(q=3,5\) sets, or the full multiplicity dichotomy. The present result resolves the **first open exponent \(s=3\)** for all odd primes, and proves the no-singleton clause in this subfamily.

Shannon, Shiue, He and Saito, *On the special cases of Carmichael's totient conjecture* (2025), Theorem 2.3.1, treats \(X_{4q}\) under \(q\equiv1\pmod6\); its general prime-divisor/prime-power enumeration method is the standard starting point for this proof, but the publication does not give the uniform \(8q\) classification. Its Table 1 **already lists** the two fixed exceptional fibers \(X_{24}\) and \(X_{40}\); those finite sets are included here for completeness and are not separately claimed as new. The same paper cites Grosswald's earlier necessary condition that a singleton totient fiber at \(k\) requires \(32\mid k\); thus the no-singleton corollary for \(8q\) was independently known. The present priority claim concerns the **full uniform symbolic classification** and its parameter-dependent multiplicities, not the old singleton obstruction or old small table entries. Generic inverse-totient algorithms determine finite individual fibers, but do not by themselves state this uniform symbolic three-primality formula and all its exceptional branches. The usual global Carmichael conjecture remains open.

## Limitations

Only the first open mirror exponent \(s=3\) is resolved; no implication is claimed for \(s\ge4\), for infinitely many simultaneous prime pairs, or for the general Carmichael totient conjecture. The proof uses elementary arithmetic and published prime-power totient properties. The known no-singleton criterion and already-tabulated fibers at \(24\) and \(40\) are not originality claims. The precise historical priority of the uniform \(8q\) formula remains qualified by the finite set of inspected sources; an unindexed earlier inverse-totient classification might exist. Verification tests a finite range and cannot establish historical originality or replace the proof.

## References

1. T.-X. He, *The Family \(X_{qp^s}\) for Distinct Primes \(q,p\) in Connection with Carmichael's Totient Conjecture*, arXiv:2610.34808v1, first posted October 26, 2026, https://arxiv.org/html/2610.34808v1 (especially §§5.2–5.4, Open Problem 16).
2. A. G. Shannon, P. J.-S. Shiue, T.-X. He, and C. Saito, *On the special cases of Carmichael's totient conjecture*, Notes on Number Theory and Discrete Mathematics 31 (2025), 504–534, https://doi.org/10.7546/nntdm.2025.31.3.504-534 (especially §2.3).
3. Classical prime-power formula and multiplicativity of Euler's totient, as recalled in both references above.
