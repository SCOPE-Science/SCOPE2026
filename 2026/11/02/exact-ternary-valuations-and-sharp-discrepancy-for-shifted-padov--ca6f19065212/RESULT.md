# Exact ternary valuations and sharp discrepancy for shifted Padovan numbers

## Finding

Let \(P_0=P_1=P_2=1\) and \(P_{n+3}=P_{n+1}+P_n\). All these Padovan numbers are positive. For each integer \(n\ge0\),
\[
\nu_3(P_n+1)=
\begin{cases}
1,&n\equiv3\pmod{13},\\
1+\nu_3(n+9),&n\equiv4\pmod{13},\\
1+\nu_3(n+6),&n\equiv7\pmod{13},\\
0,&\text{otherwise}.
\end{cases}
\tag{1}
\]
For \(t,N\ge0\), let
\[
C_t(N)=\#\{0\le n<N:\nu_3(P_n+1)=t\}.
\]
Every valuation \(t\ge0\) has the following positive natural density:
\[
p_t=\lim_{N\to\infty}\frac{C_t(N)}N=
\begin{cases}
10/13,&t=0,\\
7/39,&t=1,\\
4/(13\cdot3^t),&t\ge2.
\end{cases}
\tag{2}
\]
The full **sharp discrepancy spectrum** is
\[
\sup_{N\ge0}|C_t(N)-p_tN|=
\begin{cases}
15/13,&t=0,\\
29/13,&t=1,\\
4/3+20/(13\cdot3^t),&t\ge2.
\end{cases}
\tag{3}
\]
Consequently \(|C_t(N)-p_tN|\le29/13\) holds for *all* nonnegative \(N,t\), with equality at \(N=21,t=1\). The supremum for each fixed \(t\) is achieved, so none of the three classes of constants in (3) can be reduced.

## Assumptions and scope

The sequence uses the standard indexing \(P_0=P_1=P_2=1\), not the alternative convention beginning \(0,1,1\). The latter is the standard sequence shifted one position. The valuation \(\nu_3(m)\) is the exponent of \(3\) in a positive integer \(m\); here every \(P_n+1\) is positive. The cutoff \(N\) and the valuation level \(t\) range independently over *all* nonnegative integers. The nonnegative indices are essential; negative indices are an auxiliary integer extension, not part of the counting law.

## Proof

**1. Period thirteen and initial residue classes.** Put
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},\qquad
v_n=\begin{pmatrix}P_n\\P_{n+1}\\P_{n+2}\end{pmatrix}
=M^n\begin{pmatrix}1\\1\\1\end{pmatrix}.
\]
An exact integer multiplication gives
\[
M^{13}=\begin{pmatrix}7&12&9\\9&16&12\\12&21&16\end{pmatrix}
=I+3A,\qquad
A=\begin{pmatrix}2&4&3\\3&5&4\\4&7&5\end{pmatrix}.
\tag{4}
\]
The first thirteen Padovan values are
\[
(P_n)_{n=0}^{12}=(1,1,1,2,2,3,4,5,7,9,12,16,21).
\]
Thus \(P_n+1\equiv0\pmod3\) occurs exactly when \(n\bmod13\in\{3,4,7\}\). In all other classes the valuation is zero, since \(M^{13}\equiv I\pmod3\).

**2. The constant branch.** For \(n=13m+3\), with \(m\ge0\), (4) gives
\[
P_{13m+3}+1=P_3+1+
\sum_{j=1}^{m}3^j\binom mj e_1^{\mathsf T}A^jv_3.
\]
Here \(P_3+1=3\) and
\[
e_1^{\mathsf T}Av_3=(P_{16}-P_3)/3=(65-2)/3=21.
\]
All remaining terms are divisible by \(9\). Hence \(P_{13m+3}+1\equiv3\pmod9\), proving valuation one for this class.

**3. The two lifting branches.** Since \(\det M=1\), the sequence has a unique integer-valued extension to negative indices using \(P_j=P_{j+3}-P_{j+1}\). This gives \(P_{-9}=P_{-6}=-1\). Fix \(r\in\{4,7\}\), let \(s=r-13\in\{-9,-6\}\), and set \(h=m+1\) for \(n=13m+r\), \(m\ge0\). Thus \(v_{13m+r}=(I+3A)^h v_s\), and, because \(P_s=-1\),
\[
P_{13m+r}+1
=\sum_{j=1}^{h}3^j\binom hj e_1^{\mathsf T}A^jv_s.
\tag{5}
\]
The first coefficient is an integer unit at three:
\[
e_1^{\mathsf T}Av_s=(P_r-P_s)/3
=\begin{cases}1,&r=4,\\2,&r=7.\end{cases}
\]
Let \(a=\nu_3(h)\). For every integer \(j\) with \(2\le j\le h\), the identity
\(\binom hj=(h/j)\binom{h-1}{j-1}\) implies
\[
\nu_3\!\left(3^j\binom hj\right)
\ge a+j-\nu_3(j)\ge a+2.
\]
The final inequality is valid for every \(j\ge2\): if \(\nu_3(j)=k\), then \(j\ge3^k\) and \(j-k\ge2\), including \(k=0\). Consequently, the \(j=1\) term in (5) has valuation exactly \(a+1\) and cannot be cancelled by any higher term. Therefore
\[
\nu_3(P_{13m+r}+1)=1+\nu_3(m+1).
\]
Since \(n+13-r=13(m+1)\) and \(13\) is a three-adic unit, these are exactly the \(n+9\) and \(n+6\) clauses of (1).

**4. Complete valuation residue classes and densities.** For \(t=0\), the valuation class is the ten residue classes
\[
R_0=\{0,1,2,5,6,8,9,10,11,12\}\pmod{13}.
\]
For \(t=1\), it is
\[
R_1=\{3,4,7,16,17,20,29\}\pmod{39}.
\]
For each \(t\ge2\), let \(L=13\cdot3^t\). The valuation-\(t\) class is precisely the **four** residues
\[
R_t=\{L/3-9,\ L/3-6,\ 2L/3-9,\ 2L/3-6\}\pmod L.
\tag{6}
\]
To see (6), in either lifting branch write \(m+1\) modulo \(3^t\); exact valuation \(t-1\) means \(m+1\equiv3^{t-1}\) or \(2\cdot3^{t-1}\pmod{3^t}\). Substitution into \(n=13m+r\) gives (6). Each valuation set is therefore periodic, with exactly \(10\), \(7\), or \(4\) indices per period \(13\), \(39\), or \(13\cdot3^t\) respectively. The densities (2) follow. Their sum is one.

**5. Exact sharp discrepancies.** For each \(t\), the function \(D_t(N)=C_t(N)-p_tN\) is periodic of the same period, because every full period contains exactly \(p_tL\) members. It suffices to inspect a single period.

For \(t=0\), the signed extrema over \(0\le N\le13\) are \(-15/13\) at \(N=8\) and \(9/13\) at \(N=3\). For \(t=1\), the signed extrema over \(0\le N\le39\) are \(-7/13\) at \(N=3\) and \(29/13\) at \(N=21\). Both follow immediately by scanning the explicit small residue sets displayed above; no unbounded search is involved.

For \(t\ge2\), let the four ordered residues (6) be \(a<b<c<d\). The signed discrepancy decreases by \(4/L\) for each unit of \(N\) except that it jumps up by \(1\) when \(N\) passes one of \(a,b,c,d\). Its extrema must occur immediately before or after one of those four jumps (or at a period endpoint). Substituting (6) into the eight candidates gives the minimum \(-4/3+36/L\), attained at \(N=a=L/3-9\), and the maximum \(4/3+20/L\), attained at \(N=d+1=2L/3-5\). The latter is larger in absolute value than the former since \(L\ge117\). This proves (3). Finally \(29/13\) exceeds \(15/13\) and \(4/3+20/(13\cdot3^t)\) for \(t\ge2\); the global best constant is \(29/13\).

## Verification

The accompanying standard-library Python file `verify.py` reproduces the integer matrix identity (4), the two backward roots, an exact recurrence through \(n=4000\), an independent modular recurrence through \(n=199999\), high-order far-index checks, and **complete** period enumeration for valuation levels \(0\le t\le8\). It returns `VERIFY_OK`. The finite checks are diagnostic evidence for the proof and exact small residue extrema; they are **not** used to establish the infinite formula or the general-\(t\) discrepancy inequality. The nonstandard lifting inequality and complete all-\(t\) extrema are proved above.

## Relationship to prior work

Rihane and Togbé (2021) treat repdigit products and use two-adic information about unshifted Padovan terms under a different initial-index convention. Bravo (2023) treats common Padovan/Perrin values and explicitly extends the standard Padovan sequence to negative indices, but does not give shifted ternary valuation classes. Bravo and Irmak (2024) determine two-adic valuations for \(P_n-1\) and \(R_n+1\), but not the three-adic valuations of \(P_n+1\) or their sharp frequency discrepancies. These are genuine distinctions of prime, shift, object and result, not merely different theorem titles. Finite Lucas/Padovan periodicity alone gives neither the exact lifting order nor the optimal count error. The inspected theorems, as stated, do not entail the exact shifted ternary valuation or its sharp frequency-discrepancy spectrum.

## Limitations

The result concerns only the **positive shifted** standard Padovan sequence at prime three, not all primes or all additive shifts. The all-index proof is mathematical, but the verification program's direct recurrence is finite. It does not establish bibliographic uniqueness: an unindexed equivalent or stronger mathematical theorem may exist. No conclusion about inaccessible literature is inferred from finite calculations.

## References

1. S. E. Rihane and A. Togbé, *Repdigits as products of consecutive Padovan or Perrin numbers*, Arabian Journal of Mathematics **10** (2021), 469–480, first public 28 March 2021. https://link.springer.com/article/10.1007/s40065-021-00317-1
2. E. F. Bravo, *Common Values of Padovan and Perrin Sequences*, Mediterranean Journal of Mathematics **20** (2023), article 268, first public 17 July 2023. https://link.springer.com/article/10.1007/s00009-023-02467-2
3. E. Bravo and N. Irmak, *The 2-adic valuation of shifted Padovan and Perrin numbers and applications*, Turkish Journal of Mathematics **48** (2024), 1183–1196, available 14 November 2024. https://www.researchgate.net/publication/385944064_The_2-adic_valuation_of_shifted_Padovan_and_Perrin_numbers_and_applications
