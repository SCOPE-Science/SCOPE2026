# Exact orbit comparisons and positive-coefficient certificate

Let \(p\ge3\), \(q\ge2\), \(N=p+q\), \(H=p^2+pq-2p-q\), and let \(A,B,C,D,E,F,G\) denote the seven failure orbits defined in `RESULT.md`. An orbit involving disjoint clique edges requires \(p\ge4\). Define \(\Delta_T\) as the increase in the Kirchhoff index for orbit \(T\).

## All seven exact rational damage values
\[
\begin{aligned}
\Delta_A&=\frac{2(2p^2+2pq-3p+q^2-q)}{p(p-2)(N-1)},\\
\Delta_B&=\frac{2(2p^2+2pq-3p+q^2-2q)}{p(p-1)(N-2)},\\
\Delta_C&=\frac{2M}{pH(H+2)},\\
\Delta_D&=\frac{D_0}{pD_1},\\
\Delta_E&=\frac{E_0}{p(p-1)(N-2)(N-1)},\\
\Delta_F&=\frac{2(2N-3)}{(N-3)(N-1)},\\
\Delta_G&=\frac4{N-2}.
\end{aligned}
\]
The auxiliary polynomials are
\[
\begin{aligned}
M={}&2p^4+4p^3q-6p^3+3p^2q^2-9p^2q+6p^2\\
&+pq^3-5pq^2+6pq-q^3+2q^2,\\
D_0={}&4p^3+6p^2q-8p^2+3pq^2-9pq+6p+q^3-3q^2+2q,\\
D_1={}&p^3+2p^2q-4p^2+pq^2-5pq+4p-q^2+3q-2,\\
E_0={}&4p^3+6p^2q-10p^2+3pq^2-9pq+6p+q^3-3q^2+2q.
\end{aligned}
\]
All fractions are obtained by substituting the corresponding pair of incidence vectors into the rank-two formula in `RESULT.md` and simplifying. In particular, each denominator is positive for \(p\ge3,q\ge2\), since the deleted graphs are connected. The reduced difference denominators below are likewise strictly positive, as can also be checked by shifting parameters and expanding (performed in `verify.py`).

## Strict comparisons against the maximum and runner-up candidates
It is sufficient to prove
\[
\Delta_A>\Delta_B,\quad \Delta_A>\Delta_C,\quad
\Delta_B>\Delta_D,\Delta_E,\Delta_F,\Delta_G,
\]
with \(G\) omitted when \(p=3\). For the first inequality,
\[
\Delta_A-\Delta_B=
\frac{2q(3p^2+3pq-6p+q^2-3q+2)}
{p(p-2)(p-1)(N-2)(N-1)}>0.
\]

For the remaining differences, let \(u=p-3\ge0\) and \(v=q-2\ge0\). The following are the **exact expanded numerators** of the reduced fractions \(\Delta_A-\Delta_C\), \(\Delta_B-\Delta_D\), \(\Delta_B-\Delta_E\), \(\Delta_B-\Delta_F\), \(\Delta_B-\Delta_G\), respectively. Every coefficient is nonnegative and each has a positive constant term. Each denominator is strictly positive. This is a finite coefficientwise certificate of the desired strict inequalities, for **all** integer values in scope, rather than a finite parameter enumeration.

\[
\begin{aligned}
N_{AC}={}&2(u+2)v^4+2(u+2)(4u+17)v^3\\
&+2(u+2)(6u^2+51u+107)v^2\\
&+2(4u^4+59u^3+315u^2+719u+587)v\\
&+2(u+3)^2(u+5)(u^2+8u+13),\\[2mm]
N_{BD}={}&(u+2)v^4+(u+2)(4u+15)v^3\\
&+(5u^3+50u^2+155u+148)v^2\\
&+(u+3)(2u^3+25u^2+87u+82)v\\
&+2(u+3)^2(u^2+4u+1),\\[2mm]
N_{BE}={}&v^2+(2u+9)v+4u+14,\\[2mm]
N_{BF}={}&2v^4+4(2u+7)v^3+2(5u^2+37u+65)v^2\\
&+2(2u+7)(u^2+9u+16)v\\
&+2(u+2)(u+3)(2u+7),\\[2mm]
N_{BG}={}&2v^2+4(u+4)v+6(u+3).
\end{aligned}
\]
The corresponding positive denominators, in order, are
\[
\begin{aligned}
& p(p-2)(N-1)H(H+2),\\
& p(p-1)(N-2)D_1,\\
& p(p-1)(N-1),\\
& p(p-1)(N-3)(N-2)(N-1),\\
& p(p-1)(N-2).
\end{aligned}
\]
The exact coefficient identities and denominator positivity are checked algebraically in `verify.py`; no numerical approximation is used in these inequalities.

## Exact second-place difference
\[
\Delta_B-\Delta_C
=\frac{2F(p,q)}{(p-1)(N-2)H(H+2)},
\quad F(p,q)=-q^2+[p^2(p-3)+2]q+p^2(p-2)^2.
\]
At \(R_p=p^3-3p^2+p+1\), direct substitution yields \(F(p,R_p)=1\) and \(F(p,R_p+1)=-p(p-1)(p-2)\). The numerator has one positive real root, so no integer tie can occur. These identities are symbolically verified by `verify.py`.
