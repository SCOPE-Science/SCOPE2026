# Exact doubling detector in the LCM prime-increment recurrence

## Finding
Let \(a_1=1\) and
\[
a_n=a_{n-1}+\operatorname{lcm}(n,a_{n-1})\qquad(n\ge2),
\]
and define
\[
b_n=\frac{a_n}{a_{n-1}}-1=\frac{n}{\gcd(n,a_{n-1})}.
\]
For every prime \(p\ge5\),
\[
b_{2p}\in\{1,p\}
\]
and in fact
\[
b_{2p}=1\quad\Longleftrightarrow\quad b_{2p-1}=2p-1.
\]
Therefore \(b_{2p}=p\) precisely when \(b_{2p-1}\ne2p-1\).

If the prime-or-one conjecture \(b_m\in\{1\}\cup\mathbb P\) is assumed only at \(m=2p-1\), then
\[
b_{2p}=1\quad\Longleftrightarrow\quad 2p-1\in\mathbb P.
\]
The implication from \(2p-1\in\mathbb P\) to \(b_{2p}=1\) is unconditional. Hence, under the global conjecture, the original \(K=1\) recurrence itself detects exactly the prime pairs \(p,2p-1\) at the even semiprime indices \(2p\).

## Assumptions and scope
The exact equivalence \(b_{2p}=1\Longleftrightarrow b_{2p-1}=2p-1\) is unconditional for every prime \(p\ge5\). Only the conversion of the maximal increment \(b_{2p-1}=2p-1\) into primality of \(2p-1\) uses the prime-or-one conjecture, and it needs that conjecture only at the single index \(2p-1\).

The result concerns the recurrence with coefficient \(K=1\). It does not prove that infinitely many pairs \(p,2p-1\) are prime and does not prove the global prime-or-one conjecture.

## Proof
The elementary identities \(b_n=n/\gcd(n,a_{n-1})\) and \(b_n\mid n\) hold by definition. Also
\[
a_n=a_{n-1}(1+b_n),
\]
so every \(a_n\) is a multiple of \(a_{n-1}\). Directly,
\[
a_2=3,\quad a_3=6,\quad a_4=18,\quad a_5=108,\quad a_6=216.
\]
Thus \(a_n\) is even for every \(n\ge3\), and \(8\mid a_n\) for every \(n\ge6\).

Fix a prime \(p\ge5\). Since \(a_{2p-1}\) is even, \(2\mid\gcd(2p,a_{2p-1})\). As \(p\) is prime, the gcd is either \(2\) or \(2p\). Hence \(b_{2p}\in\{p,1\}\).

If \(b_{2p-1}=2p-1\), then
\[
a_{2p-1}=a_{2p-2}(1+b_{2p-1})=2p\,a_{2p-2},
\]
so \(2p\mid a_{2p-1}\) and therefore \(b_{2p}=1\).

Conversely, suppose \(b_{2p}=1\). Then \(p\mid a_{2p-1}\). Since
\[
a_{2p-1}=\prod_{k=2}^{2p-1}(1+b_k),
\]
there is some \(k\le2p-1\) for which \(p\mid 1+b_k\). From \(1\le b_k\le k\le2p-1\), one has \(2\le1+b_k\le2p\); hence
\[
b_k\in\{p-1,2p-1\}.
\]

The possibility \(b_k=p-1\) is impossible. Because \(b_k\mid k\) and \(k\le2p-1\), it would force \(k=p-1\) or \(k=2p-2\). In the first case,
\[
\gcd(p-1,a_{p-2})=\frac{p-1}{b_{p-1}}=1,
\]
contradicting the fact that both \(p-1\) and \(a_{p-2}\) are even. In the second case,
\[
\gcd(2p-2,a_{2p-3})=\frac{2p-2}{b_{2p-2}}=2.
\]
But \(4\mid2p-2\) and, since \(2p-3\ge7\), one has \(8\mid a_{2p-3}\). Their gcd is therefore divisible by \(4\), again a contradiction.

Thus \(b_k=2p-1\). Since \(b_k\mid k\) and \(k\le2p-1\), this forces \(k=2p-1\), proving
\[
b_{2p}=1\quad\Longleftrightarrow\quad b_{2p-1}=2p-1.
\]

For the prime-pair corollary, if \(2p-1\) is prime, the prime-step lemma for the recurrence gives \(b_{2p-1}=2p-1\), hence \(b_{2p}=1\). Conversely, if \(b_{2p}=1\), the proved equivalence gives \(b_{2p-1}=2p-1>1\); the prime-or-one conjecture at that single index then forces \(2p-1\) to be prime.

## Verification
The proof is symbolic. The standalone verifier reconstructs the recurrence exactly through \(n=200000\) using prime-adic exponent bookkeeping rather than storing the enormous integers \(a_n\). For every prime \(5\le p\le100000\), it checks the unconditional equivalence
\[
b_{2p}=1\quad\Longleftrightarrow\quad b_{2p-1}=2p-1.
\]
It also records the observed agreement with primality of \(2p-1\) over this finite range. That latter computation is evidence only; the infinite converse remains conditional exactly as stated above.

Replay with a standard Python interpreter:

`python artifacts/verify.py`

The recorded output is in `artifacts/verification_output.txt`.

## Relationship to prior work
Cloitre's recent paper introduces the \(K=1\) recurrence, proves \(b_q=q\) for every prime \(q\ge5\), and develops the deterministic stock of factors \(q+1\). It then changes to a \(K=2\) recurrence to obtain a conditional detector for twin primes at prime indices. The result here stays in the original \(K=1\) recurrence and identifies a different exact mechanism at the composite indices \(2p\): a forced one there is equivalent to the preceding odd index having its maximal possible increment.

Ruiz-Cabello's earlier paper proves basic divisibility properties, the prime-step result, and the connection of the global prime-or-one conjecture with strong prime-distribution input. Its inspected statements do not give this exact \(2p\)-to-\(2p-1\) equivalence. The OEIS entry for the increment sequence records the prime-step behavior but, in the inspected material, not this doubling criterion.

## Limitations
The theorem does not show that \(2p-1\) is prime whenever \(b_{2p}=1\) without an additional hypothesis: that last step is exactly an instance of excluding a composite maximal increment. The unconditional content is the exact equivalence with \(b_{2p-1}=2p-1\), plus the unconditional direction from primality of \(2p-1\).

The finite replay through \(200000\) does not certify any infinite assertion and is not used to prove the theorem.

## References
1. Benoît Cloitre, *Primes in LCM recurrences: a density theorem via companion sieves*, arXiv:2510.18891, first public 2025-10-18; current text inspected at v3.
2. Serafín Ruiz-Cabello, *On the use of the least common multiple to build a prime-generating recurrence*, arXiv:1504.05041; *International Journal of Number Theory* 13 (2017), 819--833, DOI 10.1142/S1793042117500439.
3. OEIS A135506, multiplicative increments of OEIS A135504.
