# A sixth-order Jones recurrence for a Khovanov-large four-braid family
## Finding
For \(t\ge 0\), let
\[
L_t=\widehat{(\sigma_1\sigma_3\sigma_2^4)^t\sigma_1\sigma_3}.
\]
With \(\delta=-A^2-A^{-2}\), let \(F_t(A)=\langle L_t\rangle\) denote the Kauffman bracket and let \(E\) be the forward shift, \((EF)_t=F_{t+1}\). Define
\[
Q_1(\lambda)=A^{12}\lambda-A^{10}\lambda^2-2A^8\lambda+2A^4\lambda+A^2-\lambda,
\]
\[
Q_2(\lambda)=A^{16}\lambda-A^{14}\lambda^2-A^{12}\lambda+2A^8\lambda-A^4\lambda-A^2+\lambda,
\]
and
\[
P_A(\lambda)=(A^2+\lambda)(A^6-\lambda)Q_1(\lambda)Q_2(\lambda).
\]
Then
\[
P_A(E)F_t=0
\]
for every integer \(t\ge0\). The polynomial \(P_A\) has degree six in \(\lambda\) and leading coefficient \(-A^{24}\), which is a unit in \(\mathbb Z[A,A^{-1}]\). Thus the relation is a genuine sixth-order recurrence.

The braid word has writhe \(6t+2\). Therefore, with
\[
J_t(A)=V_{L_t}(A^{-4})=A^{-18t-6}F_t(A),
\]
the Jones polynomials satisfy the equivalent recurrence
\[
P_A(A^{18}E)J_t=0.
\]

## Assumptions and scope
The statement uses the standard Kauffman-bracket normalization \(\langle\bigcirc\rangle=1\), \(\delta=-A^2-A^{-2}\), and the positive-braid Temperley--Lieb representation
\[
\rho(\sigma_i)=A\,1+A^{-1}e_i.
\]
It concerns exactly the four-braid family \(L_t\) above for all \(t\ge0\). No claim is made that the displayed sixth-order recurrence is minimal, and no claim is made about cancellation patterns or asymptotic coefficient growth of \(J_t\).

## Proof
Work in \(TL_4(\delta)\) over \(\mathbb Z[A,A^{-1}]\). Let
\[
B=\rho(\sigma_1\sigma_3\sigma_2^4),\qquad
S=\rho(\sigma_1\sigma_3).
\]
The algebra has the standard fourteen noncrossing-pairing basis. Let \(\operatorname{cl}\) be the closure functional that sends a basis diagram whose closure has \(c\) circles to \(\delta^{c-1}\). By construction,
\[
F_t=\operatorname{cl}(B^tS).
\]

An exact multiplication in the fourteen-element diagram basis gives the stronger state identity
\[
P_A(B)S=0
\]
inside \(TL_4(\delta)\). This is not a finite-pattern guess: it is an identity of Laurent-polynomial coefficients on every basis diagram. Multiplying by \(B^t\) and applying \(\operatorname{cl}\) gives
\[
0=\operatorname{cl}(B^tP_A(B)S)=P_A(E)F_t
\]
for every \(t\ge0\).

For the orientation induced by the positive braid, the writhe is \(6t+2\). The standard Jones normalization yields
\[
V_{L_t}(A^{-4})=(-A^3)^{-(6t+2)}F_t=A^{-18t-6}F_t.
\]
Substituting \(F_t=A^{18t+6}J_t\) into the bracket recurrence replaces each \(E\) by \(A^{18}E\), giving \(P_A(A^{18}E)J_t=0\).

## Verification
The bundled verifier reconstructs all fourteen noncrossing pairings, the diagram product, the three Temperley--Lieb generators, \(B\), \(S\), and the polynomial \(P_A\) using only integer Laurent-polynomial arithmetic. It then checks coefficient-by-coefficient that \(P_A(B)S=0\).

As normalization checks it independently obtains
\[
F_0=-A^8-A^4
\]
and
\[
F_1=-A^{14}-3A^6+A^2-4A^{-2}+2A^{-6}-3A^{-10}+A^{-14}-A^{-18}.
\]
Running `python3 verify_recurrence.py` returns:

`VERIFY_OK basis=14 block_terms=8 tail_terms=4 annihilator_degree=6 state_identity=true F0_terms=2 F1_terms=8`

## Relationship to prior work
Kelomäki and Schütz introduced exactly this family in Proposition 1.6 of arXiv:2601.02119v1 to prove asymptotically large Khovanov ranks. Their Remark 7.4 explicitly notes that their construction gives those Khovanov lower bounds without providing information about the Jones polynomials \(J_{L_t}\). The recurrence above supplies an exact Jones-theoretic description for that same family.

General methods do not make the displayed family-specific law redundant. Morton and Short give a polynomial-time algorithm for Jones polynomials of closed braids on a fixed number of strands. Berceanu and Nizami give a Fibonacci-type recurrence when one exponent in a fixed braid word is varied, together with general expansion methods. Those results provide broad computational frameworks, but the repeated six-crossing block parameter \(t\) here changes the word length and their displayed one-exponent relation does not state the degree-six constant-coefficient transfer annihilator \(P_A\) above.

## Limitations
The result is an exact recurrence, not an analysis of its dominant roots, coefficient signs, span, or cancellation against the large Khovanov groups. It also does not prove that order six is minimal. A general recurrence methodology for Jones polynomials of braids is known, so the original content here is the explicit compressed transfer identity for this particular four-braid family and its direct Jones normalization.

## References
1. T. Kelomäki and D. Schütz, *On computational complexity of Khovanov homology*, arXiv:2601.02119v1, 2026.
2. B. Berceanu and A. R. Nizami, *A recurrence relation for the Jones polynomial*, Journal of the Korean Mathematical Society 51 (2014), 443--462; arXiv:1002.3735v1.
3. H. R. Morton and H. B. Short, *Calculating the 2-variable polynomial for knots presented as closed braids*, Journal of Algorithms 11 (1990), 117--131.
4. L. H. Kauffman, *State models and the Jones polynomial*, Topology 26 (1987), 395--407.
