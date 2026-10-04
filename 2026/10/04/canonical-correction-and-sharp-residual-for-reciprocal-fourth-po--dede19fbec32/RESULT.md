# Canonical correction and sharp residual for reciprocal fourth-power balancing tails
## Finding
Let \(B_0=0\), \(B_1=1\), and \(B_n=6B_{n-1}-B_{n-2}\) for \(n\ge2\). Put
\[
S_n=\sum_{k=n}^\infty \frac1{B_k^4},
\qquad
G_n(c)=B_n^4-B_{n-1}^4-cB_{2n-1}.
\]
Among all real constants \(c\), the residual \(S_n^{-1}-G_n(c)\) is bounded as \(n\to\infty\) if and only if
\[
c=\frac1{280}.
\]
For this unique value,
\[
S_n^{-1}-
\left(B_n^4-B_{n-1}^4-\frac{B_{2n-1}}{280}\right)
=
\frac{11001\sqrt2}{2665600}
-
\frac{114672321(4+3\sqrt2)}{6933059000}\,(17-12\sqrt2)^n
+O\!\left((17-12\sqrt2)^{2n}\right).
\]
In particular,
\[
\lim_{n\to\infty}
\left[
S_n^{-1}-
\left(B_n^4-B_{n-1}^4-\frac{B_{2n-1}}{280}\right)
\right]
=
\frac{11001\sqrt2}{2665600}
=0.005836495873224196\ldots .
\]
Thus the denominator \(280\) in the recent exact floor formula is asymptotically forced rather than an arbitrary convenient correction.

## Assumptions and scope
The claim concerns the standard balancing sequence above and the reciprocal fourth-power tail \(S_n\). The asymptotic is for integers \(n\to\infty\). No assertion is made here about replacing the exact floor theorem of Panda, Dash and Dutta; their theorem remains stronger in giving the floor for every \(n\ge2\). The new statement identifies the unique linear correction by \(B_{2n-1}\) that keeps the inverse-tail residual bounded and gives its first two finite limiting terms.

## Proof
Set
\[
\lambda=3+2\sqrt2,
\qquad
\rho=\lambda^{-2}=17-12\sqrt2,
\qquad
t=\rho^n.
\]
The Binet formula is
\[
B_m=\frac{\lambda^m-\lambda^{-m}}{4\sqrt2}.
\]
Hence, for \(j\ge0\),
\[
B_{n+j}
=
\frac{\lambda^{n+j}}{4\sqrt2}
\left(1-t\rho^j\right),
\]
so
\[
S_n
=
1024t^2F(t),
\qquad
F(t)=\sum_{j\ge0}\frac{\rho^{2j}}{(1-t\rho^j)^4}.
\]
For \(|t|\) sufficiently small, the binomial expansion gives the convergent local series
\[
F(t)
=
\sum_{m\ge0}
\frac{\binom{m+3}3}{1-\rho^{m+2}}t^m.
\]
Since \(F(0)>0\), its reciprocal is analytic near \(0\). Exact inversion of the first four coefficients yields
\[
\frac1{1024F(t)}
=
\left(-\frac9{16}+\frac{51\sqrt2}{128}\right)
+
\left(\frac9{140}-\frac{27\sqrt2}{560}\right)t
+
\frac{11001\sqrt2}{2665600}t^2
+q_3t^3+O(t^4),
\]
where
\[
q_3=
-\frac{6496317}{3466529500}
-\frac{19488951\sqrt2}{13866118000}.
\]
Therefore
\[
S_n^{-1}
=
\left(-\frac9{16}+\frac{51\sqrt2}{128}\right)t^{-2}
+
\left(\frac9{140}-\frac{27\sqrt2}{560}\right)t^{-1}
+
\frac{11001\sqrt2}{2665600}
+
q_3t
+O(t^2).
\]

On the other hand, direct substitution of the Binet formula gives
\[
B_n^4-B_{n-1}^4
=
\left(-\frac9{16}+\frac{51\sqrt2}{128}\right)t^{-2}
+
\left(\frac1{16}-\frac{3\sqrt2}{64}\right)t^{-1}
+
\left(\frac1{16}+\frac{3\sqrt2}{64}\right)t
-
\left(\frac9{16}+\frac{51\sqrt2}{128}\right)t^2,
\]
while
\[
B_{2n-1}
=
\left(-\frac12+\frac{3\sqrt2}8\right)t^{-1}
-
\left(\frac12+\frac{3\sqrt2}8\right)t.
\]
The coefficient identity
\[
\left(\frac1{16}-\frac{3\sqrt2}{64}\right)
-
\left(\frac9{140}-\frac{27\sqrt2}{560}\right)
=
\frac1{280}
\left(-\frac12+\frac{3\sqrt2}8\right)
\]
shows that
\[
S_n^{-1}-G_n(c)
=
\left(c-\frac1{280}\right)
\left(-\frac12+\frac{3\sqrt2}8\right)t^{-1}
+O(1).
\]
Because \(-\frac12+\frac{3\sqrt2}8>0\) and \(t^{-1}\to\infty\), boundedness holds if and only if \(c=1/280\).

For that value the singular terms cancel. Subtracting the \(t\)-coefficient of \(G_n(1/280)\) from \(q_3\) gives
\[
-\frac{114672321(4+3\sqrt2)}{6933059000},
\]
which proves the stated expansion.

## Verification
The standalone script `verify.py` performs exact arithmetic in \(\mathbb Q(\sqrt2)\). It reconstructs the first four coefficients of \(F(t)\), inverts the series, checks the unique cancellation coefficient \(1/280\), checks the exact limiting constant and first correction, and independently evaluates direct reciprocal tails for \(2\le n\le12\). Its expected terminal line is:

`VERIFY_OK exact_series_coefficients=4 unique_c=1/280 residual_cases=11 n=2..12`

The finite numerical replay is corroboration only; the infinite asymptotic and uniqueness claim follow from the analytic series proof above.

## Relationship to prior work
Panda, Dash and Dutta define the smooth approximant
\[
B_n^4-B_{n-1}^4-\frac{B_{2n-1}}{280}
\]
and prove an exact formula for the floor of \(S_n^{-1}\) for every \(n\ge2\). Their proof uses Pell identities, a period modulo \(280\), and sandwich inequalities. The inspected paper does not state an asymptotic expansion of the residual, a limiting residual constant, or a uniqueness statement for the coefficient multiplying \(B_{2n-1}\).

The present result is complementary: it proves that \(1/280\) is the only coefficient for which the residual can stay bounded, and it computes the exact limiting offset and first exponentially small correction. A semantically close published record concerns cubic reciprocal Fibonacci tails, but it has different recurrence, power, normalization and constants, and therefore does not imply the balancing-number statement.

## Limitations
The result is an asymptotic refinement, not a replacement for the source paper's all-\(n\) floor theorem. It does not prove global monotonicity of the residual, although the verifier confirms increasing behavior for \(2\le n\le12\). The literature searches performed cannot logically exclude every differently phrased prior occurrence; the strongest residual originality risk is an unindexed treatment of balancing reciprocal tails using an equivalent Binet-series normalization.

## References
1. Subhasis Panda, Aditya Kumar Dash, Utkal Keshari Dutta, *On the infinite sum of reciprocals of the fourth powers of balancing numbers*, arXiv:2609.31548v1, 2026.
