# Even-even period equality for Lucas pairs with \(q=-1\)

## Finding
Let \(p\) be a nonzero even integer and \(m>2\) an even integer. Define the Lucas pair
\[
U_0=0,\qquad U_1=1,\qquad U_n=pU_{n-1}+U_{n-2},
\]
and
\[
V_0=2,\qquad V_1=p,\qquad V_n=pV_{n-1}+V_{n-2}.
\]
Let \(\pi_U(m)\) and \(\pi_V(m)\) be their least periods modulo \(m\), and let \(e_V(m)\) be the least positive index at which \(m\mid V_n\), when such an index exists.

If \(e_V(m)\) exists, then
\[
\pi_U(m)=\pi_V(m).
\]

Therefore the period-equality criterion of Fiebig, Mbirika, and Spilker extends to the previously excluded case in which both \(p\) and \(m\) are even for \(q=-1\). This gives an affirmative answer to their Question 5.3.

A useful local strengthening is
\[
\nu_2(V_n)=
\begin{cases}
1,&n\ \text{even},\\
\nu_2(|p|),&n\ \text{odd}.
\end{cases}
\]
Consequently, writing \(m=2^t r\) with \(r\) odd, if \(t\ge2\) and \(e_V(m)\) exists then
\[
2^t\mid p.
\]

## Assumptions and scope
The notation follows the standard Lucas sequences \(U_n(p,q)\) and \(V_n(p,q)\) with \(q=-1\). Since \(q=-1\), every modulus is coprime to \(q\), so both sequences are purely periodic modulo every positive integer.

The period \(\pi_S(m)\) is the least \(d>0\) for which
\[
S_d\equiv S_0\pmod m,\qquad S_{d+1}\equiv S_1\pmod m.
\]
The entry point \(e_V(m)\) is the least \(e>0\), if one exists, for which
\[
m\mid V_e.
\]

The theorem addresses exactly the \(q=-1\), even-\(p\), even-\(m\), \(m>2\) case left open in Question 5.3. No assertion is made here for the different \(q=1\) problem.

## Proof
We first establish the exact \(2\)-adic behavior of \(V_n\).

For even indices, the Lucas identity
\[
V_{2j}=V_j^2-2(-1)^j
\]
holds because \(q=-1\). Since \(p\) is even, every \(V_j\) is even. Thus \(V_j^2\) is divisible by \(4\), and
\[
V_{2j}\equiv 2\pmod4
\quad\text{or}\quad
V_{2j}\equiv -2\pmod4.
\]
Hence
\[
\nu_2(V_{2j})=1.
\]

For odd indices, define
\[
C_j=\frac{V_{2j+1}}p.
\]
The same-parity subsequence satisfies
\[
V_{n+2}=(p^2+2)V_n-V_{n-2},
\]
so
\[
C_{j+1}=(p^2+2)C_j-C_{j-1}.
\]
The initial values are
\[
C_0=1,\qquad C_1=p^2+3.
\]
Both are odd. Since \(p^2+2\) is even, induction shows that every \(C_j\) is odd. Therefore
\[
\nu_2(V_{2j+1})=\nu_2(|p|).
\]

Now write
\[
m=2^t r,
\qquad
t\ge1,
\qquad
r\ \text{odd}.
\]
Suppose \(e=e_V(m)\) exists.

If \(t\ge2\), then \(2^t\mid V_e\). The valuation formula rules out even \(e\), because an even-indexed \(V_e\) has exactly one factor of \(2\). Hence \(e\) is odd and
\[
t\le \nu_2(|p|),
\]
so
\[
2^t\mid p.
\]

We next compare the periods modulo the odd factor \(r\). Since \(r\mid V_e\), the entry point \(e_V(r)\) exists; let
\[
f=e_V(r).
\]
For even \(p\),
\[
\gcd(V_n,V_{n+1})
=
\gcd(V_0,V_1)
=
\gcd(2,p)
=
2
\]
for every \(n\), because the recurrence allows the Euclidean algorithm to move one step backward. Since \(r\) is odd and \(r\mid V_f\), this gives
\[
\gcd(V_{f+1},r)=1.
\]

The recurrences give, for every \(n\ge0\),
\[
V_{f+n}\equiv V_{f+1}U_n\pmod r.
\]
Indeed, the identity is immediate for \(n=0,1\), and both sides satisfy the same second-order recurrence thereafter. Multiplication by the unit \(V_{f+1}\pmod r\) preserves periods, while shifting a purely periodic sequence preserves its least period. Hence
\[
\pi_U(r)=\pi_V(r)=d.
\]

If \(r>1\), then \(d\) is even. The companion matrix identity, equivalently Cassini's identity, gives
\[
U_{n+1}U_{n-1}-U_n^2=(-1)^n.
\]
At \(n=d\), periodicity gives
\[
U_d\equiv0,\qquad U_{d+1}\equiv1,\qquad U_{d-1}\equiv1\pmod r.
\]
Therefore
\[
1\equiv(-1)^d\pmod r.
\]
Because \(r>1\) is odd, \(d\) cannot be odd. Thus \(d\) is even.

It remains to compare the \(2\)-power periods.

If \(t=1\), then modulo \(2\), because \(p\) is even,
\[
U_n\equiv U_{n-2}\pmod2,
\]
so
\[
\pi_U(2)=2.
\]
Every \(V_n\) is even, so
\[
\pi_V(2)=1.
\]

If \(t\ge2\), the existence of \(e_V(m)\) already forced \(2^t\mid p\). Hence modulo \(2^t\),
\[
S_n\equiv S_{n-2}\pmod{2^t}
\]
for both \(S=U\) and \(S=V\). Since
\[
(U_0,U_1)\equiv(0,1)
\]
and
\[
(V_0,V_1)\equiv(2,0)
\]
with \(2\not\equiv0\pmod{2^t}\), both sequences have least period \(2\):
\[
\pi_U(2^t)=\pi_V(2^t)=2.
\]

Finally, periods factor over coprime moduli by the Chinese remainder theorem:
\[
\pi_S(2^t r)
=
\operatorname{lcm}\bigl(\pi_S(2^t),\pi_S(r)\bigr).
\]

If \(t\ge2\), both \(2\)-power periods equal \(2\), and the odd-part periods both equal \(d\). Hence
\[
\pi_U(m)=\pi_V(m).
\]

If \(t=1\), then \(m>2\) forces \(r>1\), so the common odd-part period \(d\) is even. Therefore
\[
\pi_U(m)
=
\operatorname{lcm}(2,d)
=
d
=
\operatorname{lcm}(1,d)
=
\pi_V(m).
\]
This completes the proof.

## Verification
The accompanying `verify.py` independently computes both sequences modulo \(m\), their least periods, and the entry point of \(V\).

It checks all nonzero even parameters
\[
|p|\le40
\]
and all even moduli
\[
4\le m\le160.
\]
Whenever \(e_V(m)\) exists, it verifies
\[
\pi_U(m)=\pi_V(m).
\]
It also checks the exact \(2\)-adic valuation formula for
\[
|p|\le80,\qquad 0\le n\le100,
\]
and verifies the forced divisibility \(2^t\mid p\) in every tested case with \(t\ge2\).

The computation is finite regression evidence only. The all-parameter statement is proved symbolically above.

## Relationship to prior work
Fiebig, Mbirika, and Spilker prove that if \(m>2\) and \(e_V(m)\) exists, then
\[
\pi_U(m)=\pi_V(m)
\]
when either \(p\) is odd or \(p\) is even and \(m\) is odd. Their Question 5.3 explicitly asks whether the same conclusion holds for \(q=-1\) when both \(p\) and \(m\) are even, noting that computational data supports it.

The theorem above supplies exactly that missing parity case. Its mechanism is not the coprimality criterion used in their Corollary 3.13: when \(p\) and \(m\) are even, consecutive \(V\)-terms have common divisor \(2\), so that criterion is unavailable. Instead, the proof isolates the \(2\)-primary obstruction exactly and then recombines the odd and \(2\)-power periods by the Chinese remainder theorem.

Renault's earlier work develops periods, ranks of apparition, and orders for the first Lucas sequence \(U\), but does not compare the first and second Lucas periods in this even-even setting.

OEIS A106291 tabulates periods of the classical Lucas numbers \(V_n(1,-1)\) modulo \(n\). That is the odd-\(p\) specialization and does not address the two-parameter even-\(p\) problem.

Targeted searches for Question 5.3, the even-even extension of Corollary 3.13, and equality of \(\pi_U(m)\) and \(\pi_V(m)\) in this setting did not locate an implication-equivalent theorem.

## Limitations
The theorem is restricted to \(q=-1\). The analogous \(q=1\) even-even problem is different and is not addressed.

Existence of \(e_V(m)\) remains an explicit hypothesis. The proof does not classify all even moduli for which that entry point exists.

A residual originality risk is that the even-even argument may have appeared under older Lucas-sequence notation or in an unindexed note. This risk was reduced by inspecting the accepted full text that still labels the case open, the principal earlier period literature cited there, the relevant OEIS period entry, and targeted semantic and exact-formulation searches.

## References
1. Morgan Fiebig, aBa Mbirika, and Jürgen Spilker, “Period patterns, entry points, and orders in the Lucas sequences: theory and applications,” arXiv:2408.14632v1, 26 August 2024; DOI 10.1080/00150517.2024.2442591.
2. Marc Renault, “The Period, Rank, and Order of the \((a,b)\)-Fibonacci Sequence Mod \(m\),” Mathematics Magazine 86(5) (2013), 372–380, DOI 10.4169/math.mag.86.5.372.
3. OEIS A106291, “Period of the Lucas sequence A000032 mod \(n\).”
