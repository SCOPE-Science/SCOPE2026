# Two-commutator transfer for self-similar factorization ideals

## Statement

For Banach spaces \(X\) and \(Y\), write
\[
\operatorname{Fac}_Y(X)
 =\{ST:T\in\mathcal B(X,Y),\ S\in\mathcal B(Y,X)\}.
\]

Assume that:

1. \(Y\) is isomorphic either to the countable \(\ell_p\)-sum
   \((\bigoplus_{n=0}^\infty Y)_p\) for some \(1\le p<\infty\), or to the
   countable \(c_0\)-sum of copies of \(Y\); and
2. \(X\) contains a complemented subspace isomorphic to \(Y\).

Then every \(R\in\operatorname{Fac}_Y(X)\) is a sum of two commutators
\[
R=[A_1,B_1]+[A_2,B_2],
\]
where all four factors \(A_1,B_1,A_2,B_2\) themselves belong to
\(\operatorname{Fac}_Y(X)\).

Thus the factor-through-\(Y\) ideal has commutator width at most two inside itself.

## Proof

Let
\[
E=\Bigl(\bigoplus_{n=0}^{\infty}Y\Bigr)_p
\quad\text{or}\quad
E=\Bigl(\bigoplus_{n=0}^{\infty}Y\Bigr)_{c_0},
\]
according to the hypothesis. Since \(E\cong Y\) and \(X\) contains a complemented
copy of \(Y\), choose bounded operators
\[
J:E\to X,\qquad Q:X\to E,\qquad QJ=I_E.
\]
Let \(\iota_0:Y\to E\) and \(\pi_0:E\to Y\) be the first-coordinate embedding
and projection, and put
\[
V=J\iota_0,\qquad U=\pi_0Q.
\]
Then \(UV=I_Y\).

Take \(R\in\operatorname{Fac}_Y(X)\), say \(R=ST\) with
\(T:X\to Y\) and \(S:Y\to X\), and set \(C=TS\in\mathcal B(Y)\). Then
\[
[SU,VT]
 =S(UV)T-V(TS)U
 =R-VCU.
\tag{1}
\]

It remains to write \(VCU\) as one commutator with factors through \(Y\).
On \(E\), let \(L\) and \(R_+\) be the left and right shifts,
\[
L(y_0,y_1,y_2,\ldots)=(y_1,y_2,\ldots),\qquad
R_+(y_0,y_1,y_2,\ldots)=(0,y_0,y_1,\ldots),
\]
and let
\[
\widetilde C=\operatorname{diag}(C,C,\ldots).
\]
These are bounded in both the \(\ell_p\)- and \(c_0\)-sum cases. We have
\[
LR_+=I_E,\qquad
R_+L=I_E-\iota_0\pi_0,
\]
and \(\widetilde C\) commutes with both shifts. Hence
\[
[L,R_+\widetilde C]
 =\iota_0C\pi_0.
\tag{2}
\]
Using \(QJ=I_E\), equation (2) gives
\[
[JLQ,\,JR_+\widetilde C\,Q]
 =J[L,R_+\widetilde C]Q
 =J\iota_0C\pi_0Q
 =VCU.
\tag{3}
\]
Combining (1) and (3),
\[
\boxed{
R=[SU,VT]+[JLQ,\,JR_+\widetilde C\,Q].
}
\]
The first two factors factor through \(Y\). The second pair factor through
\(E\cong Y\). Thus every factor belongs to \(\operatorname{Fac}_Y(X)\).

## Application 1: the classical James spaces

Let \(1<p<\infty\). Laustsen proved that the weakly compact operators on the
\(p\)-th James space \(J_p\) are precisely the operators that factor through the
reflexive complemented space
\[
J_p^{(\infty)}
 =\Bigl(\bigoplus_{n=1}^{\infty}J_p^{(n)}\Bigr)_p,
\]
and that
\[
J_p^{(\infty)}
 \cong \ell_p(\mathbb N,J_p^{(\infty)}).
\]
Therefore the theorem above yields
\[
\boxed{
\mathcal W(J_p)
=
\{[A_1,B_1]+[A_2,B_2]:
 A_i,B_i\in\mathcal W(J_p)\}.
}
\]
Laustsen's Theorem 4.6 gave three weakly compact commutators, and Question 4.9
asked whether three was optimal. The displayed formula answers that question
negatively: two always suffice. It does not decide whether one always suffices.

## Application 2: the long James spaces

Kania and Kochanek proved that for the long James space \(J_p(\omega_1)\),
the ideal of weakly compactly generated operators is exactly the ideal of
operators factoring through a complemented Banach space \(G_p\), and that
\(G_p\) is isomorphic to its countable \(\ell_p\)-sum. Their Theorem 3.11 gave
a three-commutator bound. The transfer theorem improves it to
\[
\boxed{
\mathcal{WCG}(J_p(\omega_1))
=
\{[A_1,B_1]+[A_2,B_2]:
 A_i,B_i\in\mathcal{WCG}(J_p(\omega_1))\}.
}
\]

## Application 3: the Loy--Willis ideal

For \(C_0[0,\omega_1)\), the factorization used in the proof of the
three-commutator result for the Loy--Willis ideal passes through a complemented
space \(E_{\omega_1}\) satisfying
\[
E_{\omega_1}\cong c_0(\mathbb N,E_{\omega_1}).
\]
Consequently every operator in the Loy--Willis ideal is a sum of at most two
commutators whose factors remain in that ideal, improving the previously stated
upper bound of three.

## Relation to prior literature

The shift identity in (2) is not claimed as new. Dosev's 2009 work on
commutators on Banach spaces contains a closely related corner-commutator
mechanism for spaces isomorphic to countable direct sums of themselves.
Laustsen's 2002 paper supplies the factorization description of
\(\mathcal W(J_p)\), the complemented self-similar factor space, the
three-commutator theorem, and the explicit optimality question. Later work of
Kania--Kochanek and of Kania--Koszmider--Laustsen used the same
factorization-plus-self-similarity pattern and still stated three-commutator
bounds in their respective ideals.

The contribution here is the two-commutator transfer identity above and its
application to these factorization ideals. To the best of our knowledge, no
explicit statement resolving Laustsen's Question 4.9 or reducing these three
bounds to two was located in the literature checked through 2026-09-21.
Because the proof combines known ingredients in a short way, an equivalent
observation under different terminology in older commutator literature remains
the principal originality risk.

## Limitations

The theorem gives an upper bound of two; it does not show that two is optimal,
nor characterize which elements of the three ideals above are single
commutators. The argument requires both a complemented copy of the factor space
inside \(X\) and countable self-similarity of that factor space.

## References

1. N. J. Laustsen, *Commutators of operators on Banach spaces*, Journal of
   Operator Theory 48 (2002), 503--514.
   https://jot.theta.ro/jot/archive/2002-048-003/2002-048-003-003.html
2. D. T. Dosev, *Commutators on Banach Spaces*, PhD dissertation,
   Texas A&M University, 2009.
   https://oaktrust.library.tamu.edu/server/api/core/bitstreams/73eff080-556b-45b5-b604-806e63f5b707/content
3. D. T. Dosev, *Commutators on \(\ell_1\)*, Journal of Functional Analysis
   256 (2009), 3490--3509.
   https://doi.org/10.1016/j.jfa.2009.03.006
4. T. Kania and T. Kochanek, *The ideal of weakly compactly generated
   operators acting on a Banach space*, Journal of Operator Theory 71 (2014),
   455--477.
   https://doi.org/10.7900/jot.2012jun23.1959
5. T. Kania, P. Koszmider, and N. J. Laustsen, *A weak*-topological dichotomy
   with applications in operator theory*, Transactions of the London
   Mathematical Society 1 (2014), 1--28.
   https://doi.org/10.1112/tlms/tlu001
