# Exact onset of the Lucas entry-point bias for square discriminants
## Finding
Let \(U=U(P,Q)\) be a regular Lucas sequence of the first kind with \(P,Q\in\mathbb Z\setminus\{0\}\), \(\gcd(P,Q)=1\), and positive square discriminant \(D=P^2-4Q=s^2>0\). Use the notation of Ross--Shen--Cai: \(R_U=\{p:(D/p)=1\}\), \(N_U=\{p:(D/p)=-1\}\), \(Z_U^R(x)=Z_U(x)\cap R_U\), \(Z_U^N(x)=Z_U(x)\cap N_U\), and \(B_U(x)=\#\{1\le n\le x:\#Z_U^N(n)<\#Z_U^R(n)\}\).

Then \(N_U=\varnothing\). Moreover, if
\[
n_0=\min\{z_U(p):p\text{ prime and }p\nmid s\},
\]
then
\[
B_U(x)=\max\{0,\lfloor x\rfloor-n_0+1\}.
\]
The onset \(n_0\) is completely explicit:
\[
n_0=\begin{cases}
2,& P\text{ has an odd prime divisor},\\
4,& (P,Q)=(1,-2)\text{ or }(-1,-2),\\
3,& \text{otherwise}.
\end{cases}
\]
Thus Conjecture 3.1 of Ross--Shen--Cai is automatic on the entire square-discriminant subfamily, and its genuinely two-sided Chebyshev-race content begins only after restricting to nonsquare positive discriminant.

## Assumptions and scope
The sequence is \(U_0=0\), \(U_1=1\), \(U_n=PU_{n-1}-QU_{n-2}\). Regular means \(\gcd(P,Q)=1\). The source paper assumes nondegeneracy; under the present hypotheses this also holds: writing the two integral roots as \(a,b\), the only rational roots of unity for \(a/b\) are \(\pm1\); \(a=b\) would give \(D=0\), while \(a=-b\) would give \(P=0\), both excluded.

The Kronecker symbol is the one used in the source paper. Primes dividing \(D\) have symbol \(0\), so they lie in neither \(R_U\) nor \(N_U\).

## Proof
Because \(D=s^2\), for every prime \(p\nmid s\) one has \((D/p)=1\), while for \(p\mid s\) the Kronecker symbol is \(0\). Hence \(N_U=\varnothing\) and \(R_U=\{p:p\nmid s\}\).

It remains to locate the first prime in \(R_U\) that appears in the sequence. The first terms are
\[
U_1=1,\qquad U_2=P,\qquad U_3=P^2-Q,\qquad U_4=P^3-2PQ.
\]
If an odd prime \(r\mid P\), regularity gives \(r\nmid Q\). If also \(r\mid s\), then \(0\equiv D=P^2-4Q\equiv-4Q\pmod r\), a contradiction. Therefore \(r\in R_U\), and since \(U_1=1\), \(z_U(r)=2\). This gives \(n_0=2\) whenever \(P\) has an odd prime divisor.

Now suppose \(P\) has no odd prime divisor, so \(|P|=2^t\) for some \(t\ge0\). There is no prime in \(R_U\) at index \(2\): if \(t=0\), \(U_2=\pm1\); if \(t\ge1\), regularity forces \(Q\) odd, so \(4\mid D\) and hence \(2\mid s\), making the only prime divisor of \(U_2\) a symbol-zero prime.

Set \(A=U_3=P^2-Q\). Since \(\gcd(P,Q)=1\), also \(\gcd(A,Q)=1\). If a prime \(r\mid A\) also divides \(s\), then
\[
P^2\equiv Q\pmod r,\qquad P^2\equiv4Q\pmod r,
\]
so \(3Q\equiv0\pmod r\). As \(r\nmid Q\), necessarily \(r=3\). Thus every prime divisor of \(A\) other than \(3\) belongs to \(R_U\), and because \(\gcd(A,P)=1\), such a prime has entry point exactly \(3\).

We only need decide when \(|A|\) can be a power of \(3\). Since \(D=s^2\),
\[
Q=\frac{P^2-s^2}{4},\qquad A=\frac{3P^2+s^2}{4}>0.
\]
If \(|P|=1\), then \(s\) is odd and \(s\ge3\), and \(A=(s^2+3)/4\). If \(A=3^k\) with \(k\ge2\), then \(s^2\equiv6\pmod9\), impossible. Hence \(A\) is a power of \(3\) only when \(A=3\), which gives \(s=3\) and \(Q=-2\).

If \(|P|=2^t\) with \(t\ge1\), write \(s=2r\). Then
\[
A=3\cdot2^{2t-2}+r^2.
\]
If \(3\nmid r\), then \(3\nmid A\), so \(A\) is not a positive power of \(3\). If \(3\mid r\), then \(A\equiv3\pmod9\); since \(A>3\), it again cannot be a power of \(3\). Therefore a prime in \(R_U\) occurs at index \(3\) in every remaining case except \((P,Q)=(\pm1,-2)\).

For the exceptional pair, \(U_2=\pm1\), \(U_3=3\), and \(D=9\), so the only prime seen through index \(3\) has symbol \(0\). But \(U_4=\pm5\), and \(5\nmid3\), so \(z_U(5)=4\). This proves the stated classification of \(n_0\).

Finally, because \(N_U=\varnothing\), the inequality \(\#Z_U^N(n)<\#Z_U^R(n)\) is false exactly for \(n<n_0\) and true exactly for \(n\ge n_0\). Counting integers \(1\le n\le x\) gives the formula for \(B_U(x)\).

## Verification
The accompanying `verify_square_bias.py` exhausts all regular pairs \((P,Q)\) with \(0<|P|\le80\), \(0<|Q|\le500\), positive square discriminant, computes the first terms exactly, factors them by trial division, and checks the theorem's predicted onset against the actual first prime divisor with Kronecker class \(+1\). It prints `VERIFY_OK` on success. This finite replay is not used as a proof of the infinite statement; the proof above is complete.

## Relationship to prior work
Ross, Shen, and Cai define the two Kronecker classes and formulate a weak and strong entry-point bias conjecture for every regular Lucas sequence with \(D>0\). Their formulation does not exclude square discriminants. In the inspected full text, the square-discriminant branch is not separated out. The present result identifies that branch as degenerate: the negative Kronecker class is empty, and the exact onset of strict dominance is always \(2\), \(3\), or \(4\).

The Binet formula and the interpretation of \(z_U(p)\) are standard Lucas-sequence facts and are also stated in the source paper; no originality is claimed for them. The contribution is the exact square-discriminant boundary theorem for the bias statistic and its sharp onset classification.

## Limitations
This result says nothing about the genuinely two-sided case where \(D>0\) is nonsquare. It does not prove any new density theorem for ranks of apparition in that case. The originality check used semantic database searches and web/literature searches, but such searches cannot rule out an unindexed or differently phrased prior observation.

## References
1. T. Ross, Z. Shen, T. Cai, *Cyclotomic Congruences and Lucas Sequences*, arXiv:2512.03468, first posted 2025-12-03; inspected version v2 (2026-01-08), especially Section 3 and Conjecture 3.1.
