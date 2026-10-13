# The first two \(D_2\)-perfect numbers are exhaustive through \(10^8\)
## Finding
Let \(L_2\) be the second Schemmel totient function and let
\[
D_2(1)=0,\qquad
D_2(n)=\sum_{j=1}^{R_2(n)}L_2^{(j)}(n)\quad(n>1),
\]
where \(R_2(n)\) is the first iterate index at which \(L_2^{(j)}(n)\) is \(0\) or \(1\).

Then
\[
D_2(n)=n,\qquad 2\le n\le10^8,
\]
holds exactly for
\[
n=37147\quad\text{and}\quad n=53290831.
\]

Thus these are the only \(D_2\)-perfect numbers through the natural cutoff \(10^8\).

## Assumptions and scope
For \(n>1\), the Schemmel formula is
\[
L_2(n)=
\begin{cases}
0,&2\mid n,\\[4pt]
\displaystyle\prod_{p^\alpha\parallel n}p^{\alpha-1}(p-2),&n\ \text{odd}.
\end{cases}
\]
The search is exhaustive over every integer
\[
2\le n\le10^8.
\]
It does not assume that the two displayed fixed points are the only ones globally.

The primary source reports that, for \(m\in\{2,4,6\}\), the only \(D_m\)-perfect number below \(100000\) found by its computation was \(37147\), and it explicitly asks whether further \(D_m\)-perfect numbers exist for positive even \(m\). OEIS A241667 subsequently records the additional exact fixed point \(53290831\).

## Proof
The proof of the finite classification is an exact exhaustive computation whose recurrence follows directly from the defining formulas.

Let \(p\) be the least prime divisor of \(n\), and put \(u=n/p\). For odd \(n\), multiplicativity of \(L_2\) and the prime-power formula give two cases.

If \(p\mid u\), increasing the exponent of \(p\) by one multiplies the \(L_2\)-value by \(p\), so
\[
L_2(n)=pL_2(u).
\]

If \(p\nmid u\), the factor \(p\) is new and \(L_2(p)=p-2\), so
\[
L_2(n)=(p-2)L_2(u).
\]

For even \(n\),
\[
L_2(n)=0.
\]

These recurrences compute \(L_2(n)\) exactly in increasing order once the least prime divisor of every integer is known. A linear sieve supplies those least prime divisors.

For every \(n>1\),
\[
0\le L_2(n)<n.
\]
Hence all arguments on the right side of the recurrence
\[
D_2(n)=L_2(n)+D_2(L_2(n))
\]
have already been computed when \(n\) is processed, with \(D_2(1)=0\) and \(D_2(n)=0\) for even \(n\). Therefore a single increasing pass gives the exact value of \(D_2(n)\) for every \(n\le10^8\).

The attached verifier performs that pass for every integer from \(2\) through \(10^8\) and records every equality \(D_2(n)=n\). The resulting fixed-point set is exactly
\[
\{37147,53290831\}.
\]

## Verification
The standalone file `verify.cpp` implements the proof above.

It uses a linear least-prime-factor sieve through \(10^8\), checks the known prime count
\[
\pi(10^8)=5761455,
\]
computes \(L_2\) and \(D_2\) by exact integer recurrence, asserts at each odd input that
\[
0\le L_2(n)<n,
\]
and rejects unless the complete fixed-point vector equals
\[
[37147,53290831].
\]

A fresh replay of the finalized verifier produced:
`VERIFY_OK cutoff=100000000 fixed_points=37147,53290831 pi_count=5761455 max_D2=284911615 argmax_D2=97556803`.

The reported maximum is only an implementation diagnostic; it is not part of the mathematical claim.

## Relationship to prior work
Defant introduced the functions \(R_m\), \(H_m\), and \(D_m\) in connection with iterates of Schemmel totients. The paper reports an exhaustive computation below \(100000\) for \(m\in\{2,4,6\}\), with \(37147\) as the only \(D_m\)-perfect number in that range, and then asks whether any further \(D_m\)-perfect numbers exist for positive even \(m\).

OEIS A241667 is the exact sequence \(D_2(n)\). It records
\[
D_2(37147)=37147
\]
and, in a later comment,
\[
D_2(53290831)=53290831.
\]
The database entry does not state an exhaustive fixed-point classification through \(10^8\); its linked table is only through \(40000\).

The present result therefore does not claim discovery of either known fixed point. Its contribution is the exact completeness statement through \(10^8\), a three-order-of-magnitude extension of the finite range explicitly reported in the primary paper and a cutoff that lies beyond the second known example.

## Limitations
This is a finite theorem. It does not prove that \(37147\) and \(53290831\) are the only \(D_2\)-perfect numbers, nor does it classify \(D_m\)-perfect numbers for even \(m>2\).

The originality search found the primary paper, the exact OEIS sequence, and later searchable references, but an unpublished or unindexed computation extending past \(10^8\) remains a residual risk.

The proof depends on the correctness of the attached finite program, whose recurrence is justified above and whose output is independently constrained by the exact prime-count sanity check and by the fixed-point vector assertion.

## References
1. C. Defant, “On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions,” arXiv:1506.05426v1, 17 June 2015; *Journal of Integer Sequences* 18 (2015), Article 15.2.1.
2. OEIS Foundation, A241667, “Sum of the iterates of A058026 up to and including either 0 or 1,” authored 26 April 2014; comment recording \(53290831\) added 18 June 2015.
3. V. Schemmel, “Über relative Primzahlen,” *Journal für die reine und angewandte Mathematik* 70 (1869), 191–192.
