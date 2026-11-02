# Two squarefree three-prime survivors of the Sylow divisor condition

## Finding
For a positive integer \(n\), say that \(n\) satisfies the *Sylow divisor condition* if for every prime \(t\mid n\) there is a divisor \(d\mid n\) with \(d>1\) and \(d\equiv1\pmod t\). Among squarefree integers with exactly three prime divisors, the condition holds **if and only if** \(n\in\{30,105\}\). More precisely, if \(n=pqr\) with primes \(p<q<r\), the condition forces \((p,q,r)=(2,3,5)\) or \((3,5,7)\).

Consequently, among squarefree integers \(n>1\) with at most three distinct prime divisors, the condition holds exactly for \(30\) and \(105\). The unit integer satisfies it vacuously.

## Assumptions and scope
Here divisors are positive, prime factors are distinct, and the witness \(d\) may depend on \(t\). The statement concerns the arithmetic necessary condition coming from Sylow's subgroup-count theorem, **not** the existence of a finite simple group with the given order. No restriction on the sizes of the primes is imposed.

## Proof
Let \(p<q<r\) be distinct primes and suppose \(pqr\) meets the condition. The only divisor \(d>1\) of \(pqr\) that is coprime to \(r\) and can be congruent to \(1\pmod r\) is \(pq\): the single primes \(p,q\) lie strictly between \(1\) and \(r\). Thus \(r\mid pq-1\), and there is an integer \(k\) such that
\[
pq-1=kr,\qquad 1\le k\le p-1.
\]
The bound follows from \(pq-1<pr\).

Modulo \(q\), the only possible witnesses are \(r\) or \(pr\), because \(1<p<q\). The first possibility \(r\equiv1\pmod q\) would give \(q\mid k+1\), contrary to \(1\le k+1\le p<q\). Hence \(pr\equiv1\pmod q\), so reducing \(kpr=p(pq-1)\) modulo \(q\) gives \(q\mid k+p\). Since \(p+1\le k+p\le2p-1<2q\), we obtain
\[
q=p+k.
\]

Modulo \(p\), we have \(kr\equiv-1\pmod p\). As \(1\le k<p\), the element \(k\) is invertible modulo \(p\). Since \(q\equiv k\pmod p\), it follows that \(qr\equiv-1\pmod p\). If \(p\) is odd, the divisor \(qr\) therefore cannot be a witness at \(p\). Also \(q\equiv1\pmod p\) would force \(k=1\) and \(q=p+1\), an even integer greater than \(2\), contradicting primality. Thus \(r\equiv1\pmod p\). The relation \(kr\equiv-1\pmod p\) now forces \(k=p-1\). Accordingly,
\[
q=2p-1,\qquad r=\frac{p(2p-1)-1}{p-1}=2p+1.
\]
For every odd prime \(p>3\), one of \(2p-1\) and \(2p+1\) is divisible by \(3\) and exceeds \(3\); hence the pair cannot be prime. Therefore \(p=3\), giving \((p,q,r)=(3,5,7)\).

If \(p=2\), the bound on \(k\) gives \(k=1\), so \(q=p+k=3\) and \(r=pq-1=5\).

Both surviving triples satisfy the condition: for \(30\), witnesses for \(2,3,5\) are respectively \(3,10,6\); for \(105\), witnesses for \(3,5,7\) are respectively \(7,21,15\). This proves the classification.

Finally, squarefree integers with one prime factor have no nontrivial witness coprime to that prime. If \(n=pq\) with primes \(p<q\), any divisor congruent to \(1\pmod q\) and greater than \(1\) must be \(p\), impossible because \(1<p<q\). These observations prove the stated corollary for at most three prime factors.

## Verification
The included standalone Python program `verify.py` directly enumerates all unordered triples of distinct primes below \(1000\) and independently checks the defining divisor congruences for each. The only survivors are \((2,3,5)\) and \((3,5,7)\). It also checks the forced-prime-triplet shape for primes below \(100000\). Run `python3 verify.py` in the package directory; it uses only Python's standard library. These finite tests do not replace the unrestricted proof.

## Relationship to prior work
The Sylow divisor condition was introduced by Erdős and is the subject of the exact asymptotic theorem of E. Li, *A Resolution of Erdős Problem 768: the Sylow Divisor Condition*, arXiv:2606.24872, first submitted 23 June 2026. That work counts all integers satisfying the condition, without determining its complete squarefree three-prime stratum. OEIS A352287 tabulates members and expressly records \(105\) (and lists \(30\)); those observations do not prove that no other squarefree triple exists. The classical group-theoretic theorem excluding simple groups of order \(pqr\) is stronger about actual groups but does not imply this purely arithmetic classification, since the two survivors satisfy the necessary numerical test while no corresponding nonabelian simple group exists.

## Limitations
The classification applies only to squarefree integers with at most three prime factors. Nonsquarefree integers such as \(12\) can satisfy the condition. The proof does not determine higher-support families, does not classify finite groups, and does not establish priority over all unindexed historical observations.

## References
1. E. Li, *A Resolution of Erdős Problem 768: the Sylow Divisor Condition*, arXiv:2606.24872v2 (original public submission: 23 June 2026), https://arxiv.org/html/2606.24872v2 .
2. OEIS Foundation, A352287, *Numbers \(k\) such that, for every prime dividing \(k\), a nontrivial divisor is congruent to \(1\) modulo that prime*, https://oeis.org/A352287 .
3. P. Erdős, *Remarks on some problems in number theory*, Mathematica Balkanica 4 (1974), 197–202 (cited in Li, bibliographic priority risk).
