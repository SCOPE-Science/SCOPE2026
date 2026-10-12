# Sharp logarithmic discrepancy constants for Thue–Morse 01-occurrences
## Finding
Let \((t_n)_{n\ge0}\) be the Thue–Morse word,
\[
t_n=s_2(n)\bmod 2,
\]
and let
\[
D_N=
\#\{0\le n<N:t_n=0,\ t_{n+1}=1\}
-\frac N3.
\]
For every integer \(k\ge1\),
\[
\max_{0\le N<4^k}D_N
=
\frac{1+\lceil k/2\rceil}{3},
\]
and
\[
\min_{0\le N<4^k}D_N
=
-\frac{\lfloor k/2\rfloor}{3}.
\]

Both bounds have explicit equality cases. For odd \(k\), a maximum is attained at
\[
N=\frac{4^k-1}{3},
\]
while for even \(k\) a maximum is attained at
\[
N=\frac{4^{k-1}-1}{3}.
\]
For even \(k\), a minimum is attained at
\[
N=\frac{2(4^k-1)}{3},
\]
while for odd \(k\) a minimum is attained at
\[
N=\frac{2(4^{k-1}-1)}{3}.
\]

Consequently the logarithmic order proved previously has the sharp two-sided constants
\[
\limsup_{N\to\infty}\frac{D_N}{\log_2N}
=
\frac1{12},
\qquad
\liminf_{N\to\infty}\frac{D_N}{\log_2N}
=
-\frac1{12}.
\]

## Assumptions and scope
The count in \(D_N\) records starting positions \(0,\ldots,N-1\) at which the length-two factor \(01\) occurs. The normalization by \(N/3\) is the one used in the source literature.

The claim concerns this particular factor discrepancy in the classical binary Thue–Morse word. It does not assert sharp constants for every factor, every automatic word, or other normalizations.

## Proof
Put
\[
A_n=
\begin{cases}
1,&t_n=0,\ t_{n+1}=1,\\
0,&\text{otherwise},
\end{cases}
\qquad
E_N=3D_N.
\]
Then
\[
E_N=3\sum_{0\le n<N}A_n-N.
\]

The Thue–Morse identities imply
\[
(t_{4n},t_{4n+1},t_{4n+2},t_{4n+3},t_{4n+4})
=
(t_n,1-t_n,1-t_n,t_n,t_{n+1}).
\]
Therefore
\[
A_{4n}=1-t_n,\qquad
A_{4n+1}=0,\qquad
A_{4n+2}=t_n,\qquad
A_{4n+3}=A_n.
\]
Each complete four-position block thus contributes \(1+A_n\) occurrences of \(01\). It follows that
\[
\begin{aligned}
E_{4n}&=E_n,\\
E_{4n+1}&=E_n+2-3t_n,\\
E_{4n+2}&=E_n+1-3t_n,\\
E_{4n+3}&=E_n.
\end{aligned}
\]
At the same time,
\[
t_{4n}=t_n,\quad
t_{4n+1}=1-t_n,\quad
t_{4n+2}=1-t_n,\quad
t_{4n+3}=t_n.
\]

Read the base-\(4\) digits of \(N\) from left to right. The pair
\[
(E_N,t_N)
\]
is updated by the preceding formulas. Digits \(0\) and \(3\) leave both the discrepancy and state unchanged. Digits \(1\) and \(2\) toggle the state. When the current state is \(0\), their respective increments to \(E\) are \(2\) and \(1\); when the state is \(1\), the increments are \(-1\) and \(-2\).

Let \(M_k(q)\) be the largest additional \(E\)-value obtainable from \(k\) remaining base-\(4\) digits when the current state is \(q\in\{0,1\}\). Since digit \(1\) dominates digit \(2\) for maximization,
\[
\begin{aligned}
M_{k+1}(0)&=\max\{M_k(0),\,2+M_k(1)\},\\
M_{k+1}(1)&=\max\{M_k(1),\,-1+M_k(0)\}.
\end{aligned}
\]
Starting from \(M_0(0)=M_0(1)=0\), induction gives
\[
M_k(0)=1+\left\lceil\frac k2\right\rceil,
\qquad
M_k(1)=\left\lfloor\frac k2\right\rfloor.
\]
Since a number \(0\le N<4^k\) is exactly a base-\(4\) word of \(k\) digits, allowing leading zeros, the first formula yields the asserted maximum after division by \(3\).

Similarly let \(m_k(q)\) be the minimum possible additional \(E\)-value. Digit \(2\) dominates digit \(1\) for minimization, so
\[
\begin{aligned}
m_{k+1}(0)&=\min\{m_k(0),\,1+m_k(1)\},\\
m_{k+1}(1)&=\min\{m_k(1),\,-2+m_k(0)\}.
\end{aligned}
\]
Induction gives
\[
m_k(0)=-\left\lfloor\frac k2\right\rfloor,
\qquad
m_k(1)=-1-\left\lceil\frac k2\right\rceil.
\]
This proves the minimum formula.

The equality cases come directly from alternating toggle choices. A string of \(k\) base-\(4\) digits all equal to \(1\) is optimal when \(k\) is odd; when \(k\) is even, prepend one zero to the optimal odd-length string. For minima, use all \(2\)'s when \(k\) is even and prepend one zero when \(k\) is odd. These digit strings have exactly the integer values displayed in the finding.

Finally, if
\[
4^{k-1}\le N<4^k,
\]
the quartic-prefix bounds give
\[
-\frac{k}{6}+O(1)
\le D_N\le
\frac{k}{6}+O(1),
\qquad
\log_2N=2k+O(1).
\]
Hence every limit point of \(D_N/\log_2N\) lies in
\[
\left[-\frac1{12},\frac1{12}\right].
\]
The explicit maximizing witnesses with odd \(k\) and minimizing witnesses with even \(k\) have logarithms \(2k+O(1)\) and discrepancies respectively \(k/6+O(1)\) and \(-k/6\), proving that both endpoints are attained asymptotically.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier first computes \(E_N=3D_N\) directly from the definition through \(N=4^9\). It checks all four local occurrence identities and the four discrepancy recurrences for every complete four-block in that range.

A second evaluator computes \(E_N\) only from the base-\(4\) recurrence and is compared against the direct prefix count at every tested \(N\).

The exact maxima, minima, and displayed witnesses are then checked for \(1\le k\le9\). Finally, an independent two-state dynamic program verifies the closed forms for both state-conditioned maxima and minima through \(k=100\).

The finite computations are checks of the algebraic proof; the theorem for all \(k\) and the limiting constants follow from the recurrences and their elementary induction.

## Relationship to prior work
Spiegelhofer introduced this discrepancy in the study of gaps between consecutive occurrences of \(01\) in the Thue–Morse word. The paper proves that \(D_N\) is the output sum of a finite transducer, obtains
\[
D_N=O(\log N),
\]
and proves that the range of \(D_N\) is exactly \((1/3)\mathbb Z\).

The same paper supplies explicit positive and negative families showing that \(D_N\) is unbounded in both directions. Its final proof, however, stops at an unspecified logarithmic upper constant and example subsequences; it does not determine the exact extrema on natural digital intervals or the limsup and liminf constants above.

The present result uses the same discrepancy but compresses its behavior to a two-state base-\(4\) recurrence. This yields exact extremal values on every interval \(0\le N<4^k\), identifies simple extremizing digit patterns, and converts the qualitative \(O(\log N)\) estimate into sharp asymptotic constants.

Targeted searches for the exact constants, quartic-prefix extrema, recurrence aliases, and the factor-\(01\) discrepancy did not locate a published covering statement.

## Limitations
The theorem is specific to the occurrence discrepancy for \(01\). Other factors can require different states and can have different extremal behavior.

The result gives sharp global envelopes on quartic prefixes and sharp logarithmic limit constants, but it does not enumerate every \(N\) attaining each intermediate discrepancy value.

An unindexed note or unpublished calculation could contain the same two-state recurrence or sharp constants.

## References
1. L. Spiegelhofer, “Gaps in the Thue--Morse word,” arXiv:2102.01018v1, first public version 2021-02-01; Bulletin of the Australian Mathematical Society 105(2), 2022, DOI 10.1017/S1446788721000380.
