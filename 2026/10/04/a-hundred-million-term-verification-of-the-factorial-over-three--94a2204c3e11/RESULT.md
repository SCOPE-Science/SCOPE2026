# A hundred-million-term verification of the factorial-over-three refactorable conjecture
## Finding
For every integer \(n\) with \(3\le n\le 100{,}000{,}000\), let \(X_n=n!/3\). Then
\[
	au(X_n)\mid X_n.
\]
Consequently the factorial-over-three refactorable conjecture recorded in 2002 has no counterexample through \(10^8\).

## Assumptions and scope
A positive integer \(m\) is refactorable (or a tau number) when \(	au(m)\mid m\), with \(	au(m)\) the number of positive divisors. The domain here is exactly the finite interval \(3\le n\le 100{,}000{,}000\). The statement does not prove the conjecture for larger \(n\).

## Proof
Put \(X_n=n!/3\). For every prime \(q\), define \(E_q(n)=v_q(X_n)\) and \(T_q(n)=v_q(	au(X_n))\). Since
\[
X_n=\prod_p p^{E_p(n)},\qquad 	au(X_n)=\prod_p (E_p(n)+1),
\]
we have the exact identity
\[
T_q(n)=\sum_p v_q(E_p(n)+1).
\]
Therefore \(	au(X_n)\mid X_n\) if and only if \(T_q(n)\le E_q(n)\) for every prime \(q\).

The checker starts from \(X_3=2\), hence \(E_2(3)=1\), and maintains the complete prime-exponent vectors \(E\) and \(T\). When advancing from \(n-1\) to \(n\), each prime power \(p^c\parallel n\) changes \(E_p\) from \(e\) to \(e+c\). Accordingly the factor \(e+1\) in \(	au(X_{n-1})\) is removed and the factor \(e+c+1\) is inserted. Exact prime factorizations of those two integers update all affected \(T_q\). A maintained violation count is zero exactly when every inequality \(T_q\le E_q\) holds.

The loop visits every integer \(n\) in the stated range, so this is exhaustive rather than sampled. In addition, the package recomputes \(E\) and \(T\) from Legendre's formula at 1002 selected small inputs and compares the same divisibility criterion independently of the incremental state.

## Verification
Compile `artifacts/verify.cpp` with a conforming C++17 compiler and run the executable with argument `100000000`. The packaged run produced:

`VERIFY_OK limit=100000000 checks=99999998 direct_samples=1002`

The program uses exact integer arithmetic only. Its largest factorial exponent is below \(10^8\), safely within the signed 32-bit storage used for exponent arrays; products used by the sieve are promoted to signed 64-bit integers before multiplication. The certificate is a complete deterministic traversal of the claimed interval, not probabilistic evidence.

## Relationship to prior work
Zelinsky records the conjecture that \(n!/3\) is a tau number for every \(n>2\), and proves that for each fixed prime \(p\), the \(p\)-adic divisibility needed for a more general factorial expression eventually holds. That theorem is explicitly prime-by-prime and does not supply one simultaneous threshold over all primes, so it does not imply any stated global cutoff for the conjecture. The same paper leaves the factorial assertion conjectural. The general OEIS entry A033950 records refactorable numbers but, in the inspected entry, gives no factorial-over-three verification range.

The present result is deliberately a finite verification rather than a proposed proof of the infinite conjecture. Searches for the exact factorial-over-three phrase, its tau-number/refactorable aliases, and a reported computational cutoff did not locate a prior cutoff at or beyond \(10^8\). This search evidence reduces but cannot eliminate the possibility of an unindexed earlier computation.

## Limitations
The computation proves nothing for \(n>10^8\). It also does not turn Zelinsky's fixed-prime asymptotic argument into a uniform proof. Novelty is based on inspected literature, database entries, and exact-phrase/alias searches; an unindexed or unpublished prior computation may exist. Independent audit has not been performed.

## References
1. J. Zelinsky, “Tau Numbers: A Partial Proof of a Conjecture and Other Results,” *Journal of Integer Sequences* 5 (2002), Article 02.2.8. Published 2002-12-16. https://cs.uwaterloo.ca/journals/JIS/VOL5/Zelinsky/zelinsky9.pdf
2. S. Colton, “Refactorable Numbers — A Machine Invention,” *Journal of Integer Sequences* 2 (1999), Article 99.1.2. https://cs.uwaterloo.ca/journals/JIS/colton/joisol.html
3. OEIS Foundation, A033950, “Refactorable numbers: number of divisors of k divides k. Also known as tau numbers.” https://oeis.org/A033950
