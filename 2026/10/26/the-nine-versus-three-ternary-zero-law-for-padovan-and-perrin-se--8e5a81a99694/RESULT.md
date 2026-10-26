# The nine-versus-three ternary zero law for Padovan and Perrin sequences

## Finding

Let the Padovan and Perrin integer sequences be defined by
\[
P_0=P_1=P_2=1,\qquad R_0=3,\quad R_1=0,\quad R_2=2,
\]
and the shared recurrence \(X_{n+3}=X_{n+1}+X_n\) for all \(n\ge0\). Let \(Z_X(k)\) be the number of indices \(0\le n<L_k\) for which \(X_n\equiv0\pmod{3^k}\), where \(L_k=13\cdot3^{k-1}\).

**Theorem.** For every integer \(k\ge1\), \(L_k\) is the exact least period of both sequences modulo \(3^k\), and
\[
Z_P(k)=\begin{cases}4,&k=1,\\6,&k=2,\\9,&k\ge3,\end{cases}
\qquad
Z_R(k)=\begin{cases}4,&k=1,\\3,&k\ge2.\end{cases}
\]
For \(k\ge3\), the nine Padovan zero indices comprise six classes \(n\equiv9\pmod{13}\) and one class each in \(n\equiv5,10,12\pmod{13}\). For \(k\ge2\), the three Perrin zero indices occupy exactly one class in each of \(n\equiv1,3,9\pmod{13}\).

Consequently, the exact natural densities of indices divisible by \(3^k\) for \(k\ge3\) are \(9/(13\cdot3^{k-1})\) and \(3/(13\cdot3^{k-1})\), respectively. The period formula itself is also reflected in existing Perrin-period tables; the zero-count dichotomy and its exceptional-branch explanation are the contribution emphasized here.

## Assumptions and scope

All indices are nonnegative integers, \(k\) is a positive integer, and congruences are over the ordinary integers. Index periods mean periods of the whole scalar sequence (equivalently its three-coordinate recurrence state), not merely periods of a single value. Counting is performed over one complete least period. The standard Padovan initial normalization \((1,1,1)\) is essential; a differently shifted Padovan convention shifts zero classes without changing their counts.

## Proof

Set
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},\quad
U=M^{13}=\begin{pmatrix}7&12&9\\9&16&12\\12&21&16\end{pmatrix}=I+3B,
\quad B=\begin{pmatrix}2&4&3\\3&5&4\\4&7&5\end{pmatrix}.
\]
Write \(v_P=(1,1,1)^T\), \(v_R=(3,0,2)^T\), and \(e=(1,0,0)^T\). Then \(X_n=e^TM^nv_X\). Direct arithmetic gives \(M^{13}\equiv I\pmod3\), but \(Mv_X\not\equiv v_X\pmod3\) for both initial vectors. Since \(13\) is prime, each state has exact period \(13\) modulo \(3\). Moreover \(Bv_P=(9,12,16)^T\) and \(Bv_R=(12,17,22)^T\) are nonzero modulo \(3\).

For every \(m\ge0\), the binomial theorem gives
\[
U^{3^m}=I+3^{m+1}C_m,\qquad C_m\equiv B\pmod3.
\]
This follows at \(m=0\) directly and then inductively from cubing: \(C_{m+1}=C_m+3^{m+1}C_m^2+3^{2m+1}C_m^3\). If \(t=3^mw\) with \(3\nmid w\), then
\[
U^tv_X-v_X\equiv 3^{m+1}wBv_X\pmod{3^{m+2}}\ne0.
\]
Together with the exact order \(13\) modulo \(3\), this proves that the least period of either sequence modulo \(3^k\) is exactly \(13\cdot3^{k-1}\).

Write every index uniquely as \(n=r+13t\) with \(0\le r<13\) and \(0\le t<3^{k-1}\). Put \(F_{X,r}(t)=e^TM^rU^tv_X\) and \(a_{X,r,i}=e^TM^rB^iv_X\). The only values of \(r\) with \(a_{X,r,0}\equiv0\pmod3\), together with the exact first four coefficients, are:

| Sequence and residue \(r\) | \(a_0\) | \(a_1\) | \(a_2\) | \(a_3\) |
|---|---:|---:|---:|---:|
| Padovan 5 | 3 | 37 | 465 | 5842 |
| Padovan 9 | 9 | 114 | 1432 | 17991 |
| Padovan 10 | 12 | 151 | 1897 | 23833 |
| Padovan 12 | 21 | 265 | 3329 | 41824 |
| Perrin 0 | 3 | 12 | 158 | 1983 |
| Perrin 1 | 0 | 17 | 209 | 2627 |
| Perrin 3 | 3 | 29 | 367 | 4610 |
| Perrin 9 | 12 | 158 | 1983 | 24914 |

These numbers are obtained by multiplying the three displayed integral matrices; the verifier reproduces them. Every residue \(r\) not listed gives no zero even modulo \(3\), establishing \(Z_P(1)=Z_R(1)=4\).

For each *regular* listed branch (Padovan \(r\in\{5,10,12\}\), Perrin \(r\in\{1,3,9\}\)), the coefficient \(a_1\) is nonzero modulo \(3\). The matrix lifting congruence gives, for every \(m\ge0\),
\[
F_{X,r}(t+3^m)-F_{X,r}(t)\equiv 3^{m+1}a_1\pmod{3^{m+2}}.
\]
In particular \(F_{X,r}(t)/3\) is integral, initially has one root modulo \(3\), and the displayed nonzero increment makes every root lift to exactly one root modulo each higher power. Consequently each of the six regular branches contributes exactly one zero index in a period modulo \(3^k\) for every \(k\ge2\). For the exceptional Perrin branch \(r=0\), \(a_0/3=1\) and \(a_1\equiv0\pmod3\), hence \(F_{R,0}(t)/3\equiv1\pmod3\); it contributes none for \(k\ge2\). This already proves \(Z_R(k)=3\) for all \(k\ge2\).

The remaining Padovan branch \(r=9\) has \(a_0=9\) and \(a_1=114\), so the exact binomial expansion
\[
F_{P,9}(t)=\sum_{i\ge0}3^i\binom ti a_{P,9,i}
\]
(the sum terminates for nonnegative integral \(t\)) is divisible by \(9\). Let \(f(t)=F_{P,9}(t)/9\in\mathbb Z\). Modulo \(3\),
\[
f(t)\equiv1+38t+1432\binom t2\equiv1+2t+\binom t2\pmod3.
\]
Its roots are exactly \(t\equiv1,2\pmod3\). To prove that both lift simply despite the normalization by \(9\), define \(C_m=(U^{3^m}-I)/3^{m+1}\) for \(m\ge1\). Cubing the case \(m=1\) gives the exact congruence
\[
C_m\equiv B+3B^2+3B^3\pmod9\qquad (m\ge1).
\]
Because \(U^t\equiv I+3tB\pmod9\),
\[
\frac{e^TM^9U^tC_mv_P}{3}
\equiv\frac{114}{3}+(t+1)1432+17991\equiv t\pmod3.
\]
The quotient is integral since its numerator is divisible by \(3\). Therefore, for all \(m\ge1\),
\[
f(t+3^m)-f(t)\equiv3^m t\pmod{3^{m+1}}.
\]
At each root with \(t\equiv1\) or \(2\pmod3\), its increment coefficient \(t\) is a unit modulo \(3\). Testing \(t,t+3^m,t+2\cdot3^m\) consequently produces exactly one lift from a root modulo \(3^m\) to a root modulo \(3^{m+1}\). It follows that \(f\) has exactly two roots modulo \(3^d\) for every \(d\ge1\). When \(k\ge3\), the original condition \(3^k\mid F_{P,9}(t)\) is \(3^{k-2}\mid f(t)\), while \(t\) ranges over residues modulo \(3^{k-1}\). Each of the two roots modulo \(3^{k-2}\) yields three indices, hence this branch contributes **six** zero classes. For \(k=2\), the entire branch \(F_{P,9}(t)\) vanishes modulo \(9\), contributing three classes. Adding the three regular Padovan classes proves the remaining cases \(Z_P(2)=6\) and \(Z_P(k)=9\) for \(k\ge3\). This concludes the proof.

## Verification

The standalone Python 3 script `padovan_perrin_3adic_verifier.py` uses exact integer matrix arithmetic. Execute it with `python padovan_perrin_3adic_verifier.py`. It verifies \(M^{13}=I+3B\), every coefficient in the displayed table, exceptional lifting congruences, and the complete least periods and zero sets modulo \(3^k\) for \(1\le k\le10\). The largest checked period contains \(255879\) positions. These finite experiments provide reproducibility and error detection; the unrestricted theorem is proved by the symbolic lifting argument above.

## Relationship to prior work

Bravo, Bravo and Luca (2022) study exact *integer* zeros and repeated values of Padovan-type sequences; this is different from counting residue-zero positions modulo powers of three. Bravo (2023) determines common integer values of Padovan and Perrin sequences, supplying the normalizations used here but not the claimed modular frequency classification. The known Perrin period database OEIS A104217 already records periods for individual moduli; period lifting is included as a necessary normalization step, not proposed as independently new. OEIS A000931 and A001608 contain the underlying sequences. A 2024 study by Bravo and Irmak addresses shifted \(2\)-adic valuations, rather than this \(3\)-adic zero-class question.

## Limitations

The result covers only divisibility by powers of \(3\) for the stated initial conditions. It determines zero counts and residue-class locations, not the full distribution of nonzero residues, nor an explicit closed formula for each lifted root. Existing tables establish some recurrence periods, so the distinctive proposed contribution is the nine-versus-three root-count law. The 2022 Padovan-type multiplicity article was accessible only through its abstract and metadata during the literature comparison; a hidden general theorem in inaccessible full text cannot be ruled out. No independent mathematical audit has been performed.

## References

1. E. F. Bravo, J. J. Bravo, F. Luca, *On the Multiplicities of Padovan-Type Sequences*, Bulletin of the Brazilian Mathematical Society, 53 (2022), 1519–1549. DOI: 10.1007/s00574-022-00315-7.
2. E. F. Bravo, *Common Values of Padovan and Perrin Sequences*, Mediterranean Journal of Mathematics, 20 (2023), article 268. DOI: 10.1007/s00009-023-02467-2.
3. E. F. Bravo and N. Irmak, *The 2-adic valuation of shifted Padovan and Perrin numbers and applications*, Turkish Journal of Mathematics, 48 (2024), 1183–1196. DOI: 10.55730/1300-0098.3568.
4. The On-Line Encyclopedia of Integer Sequences, A000931 (Padovan), A001608 (Perrin), A104217 (Perrin periods), https://oeis.org/.
