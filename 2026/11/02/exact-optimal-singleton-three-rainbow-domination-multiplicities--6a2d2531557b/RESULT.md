# Exact optimal singleton three-rainbow domination multiplicities of cycle prisms

## Finding
For every integer \(m\ge 3\), let \(P_m=C_m\square K_2\) be the labelled cycle prism with vertices \(u_i,v_i\) for \(i\in\mathbb Z/m\mathbb Z\). A singleton three-rainbow dominating assignment is a map \(f:V(P_m)\to\{0,1,2,3\}\) such that every vertex assigned \(0\) has neighbours labelled \(1,2,3\), once each. Its weight is the number of vertices with nonzero labels.

The minimum weight and the **exact number of minimum-weight assignments with three named colours** are, respectively,
\[
(\widetilde\gamma_3(P_m),N_m)=
\begin{cases}
(m,12),&m\equiv0\pmod6,\\
(m+1,12m),&m\text{ odd},\\
(m+2,18m(3m-5)),&m\equiv2\pmod6,\\
(m+2,18m(3m-1)),&m\equiv4\pmod6.
\end{cases}
\]
The minimum weights agree with earlier work; the exact multiplicities are the result here. The solution space changes from constant to linear to quadratic size according to the cycle length.

## Assumptions and scope
All graphs are finite, simple, undirected and labelled. The indices on the two cycles are fixed, and the three colours are named. No quotient is taken by colour permutations, graph automorphisms, rotations or reflections. The parameter \(m\) is an integer at least \(3\). This is the *singleton* model, not set-valued rainbow domination, in which a vertex may receive multiple colours.

Write \(c_h(m)\) for the number of assignments with precisely \(m+h\) coloured vertices. Because both vertices of any rung cannot be uncoloured, every valid assignment has weight at least \(m\). The proof establishes \(c_0\), \(c_1\), and the needed even-order cases of \(c_2\) exactly; no assertion about higher weights is necessary.

## Proof
A rung with both vertices uncoloured is impossible: either uncoloured vertex would have its vertical neighbour uncoloured and therefore fewer than three available coloured neighbours. Hence each rung carries one of the \(15\) states
\[
S=\bigl(\{0,1,2,3\}^2\bigr)\setminus\{(0,0)\}.
\]
There are \(6\) states with exactly one nonzero label and \(9\) states with two. Let \(\mathcal Q=S\times S\), of size \(225\). A pair \((p,c)\in\mathcal Q\) records consecutive rung states. For \(p,c,q\in S\), say that \(\operatorname{ok}(p,c,q)\) holds precisely when, for each row \(r\in\{0,1\}\) with \(c_r=0\),
\[
\{p_r,c_{1-r},q_r\}=\{1,2,3\}
\]
as multisets (hence the three values are distinct and nonzero). Define the exact integer matrices \(A,B\), indexed by \(\mathcal Q\), with nonzero entries only on transitions from \((p,c)\) to \((c,q)\): put entry \(1\) in \(A\) if \(\operatorname{ok}(p,c,q)\) and \(q\) has one nonzero label, and put entry \(1\) in \(B\) if \(\operatorname{ok}(p,c,q)\) and \(q\) has two nonzero labels. Every other entry is \(0\).

A cyclic assignment of length \(m\ge3\) corresponds bijectively to a closed walk of length \(m\) in this pair-state automaton. Each time \(B\) is used, a completely coloured rung has been entered. Thus, with \(z\) marking the number of completely coloured rungs,
\[
\sum_{h\ge0}c_h(m)z^h=\operatorname{tr}\bigl((A+zB)^m\bigr).
\]
The constraint on each rung is checked exactly once, including the cyclic wraparound.

The crucial finite matrix identity is
\[
A^8=A^2.\tag{1}
\]
It follows directly by checking the defined \(225\) states. There is also a structural explanation: after two transitions restricted to single-coloured rungs, any surviving sequence has alternating uncoloured rows and a uniquely forced third colour; continuation has period six. The bundled exact-integer verifier independently constructs both matrices and checks equality of *all* their entries, not merely their traces.

Put \(R(t)=(I-tA)^{-1}\). Identity (1) gives
\[
R(t)=\frac{P(t)}{1-t^6},\qquad
P(t)=I+tA+t^2A^2+t^3A^3+t^4A^4+t^5A^5
+t^6(A^6-I)+t^7(A^7-A).
\]
Taking the trace of the geometric series and expanding to order two in \(z\) gives the exact formal series identities
\[
\sum_{m\ge0}c_h(m)t^m=\frac{Q_h(t)}{(1-t^6)^{h+1}},\quad h=0,1,2,
\]
where
\[
Q_0=\operatorname{tr}P,\qquad
Q_1=t\operatorname{tr}(P^2B),\qquad
Q_2=t^2\operatorname{tr}(P^2BPB).
\]
For \(m<3\), coefficients of these formal traces are auxiliary matrix traces, not graph counts; only \(m\ge3\) is used.

The following finite integer coefficient identities suffice for the theorem. All unlisted coefficients of \(Q_0,Q_1\) vanish:
\[
Q_0(t)=225-213t^6,
\]
\[
Q_1(t)=9t+36t^3+60t^5+216t^6+66t^7+36t^9+12t^{11}-3t^{13}.
\]
In \(Q_2\), the *complete* coefficient lists in residues \(2\) and \(4\) modulo \(6\) are
\[
\begin{array}{c|rrrr}
\text{exponent}&2&8&14&20\\\hline
[t^{\text{exponent}}]Q_2&81&2493&1359&-45
\end{array}
\quad
\begin{array}{c|rrr}
\text{exponent}&4&10&16\\\hline
[t^{\text{exponent}}]Q_2&792&2844&252.
\end{array}
\]
No other coefficients of \(Q_2\) have these residues, as \(\deg Q_2\le23\). The actual finite computations behind these identities are fully specified by the matrix definitions; the included \(\texttt{verify.py}\) derives and verifies the entire numerator polynomials using exact integers. In particular, it verifies (1) and all coefficients in the three identities independently of sampled graph sizes.

Expanding \((1-t^6)^{-j}=\sum_{k\ge0}\binom{k+j-1}{j-1}t^{6k}\), we obtain for every \(m\ge3\):
\[
c_0(m)=\begin{cases}12,&6\mid m,\\0,&\text{otherwise},\end{cases}
\]
\[
c_1(m)=\begin{cases}12m,&m\text{ odd},\\36m,&6\mid m,\\0,&m\equiv2,4\pmod6.\end{cases}
\]
For \(m\equiv2\pmod6\), \(m\ge8\), the displayed four coefficients of \(Q_2\) imply
\[
c_2(m)=18m(3m-5).
\]
For \(m\equiv4\pmod6\), \(m\ge4\), its other three coefficients give
\[
c_2(m)=18m(3m-1).
\]
These identities follow by collecting the stated binomial coefficients and simplifying quadratic polynomials in \((m-2)/6\) and \((m-4)/6\), respectively. Each positive coefficient gives an actual assignment because the transfer matrix counts feasible assignments with no signs. The smallest \(h\) having \(c_h(m)>0\) therefore yields the stated minimum weight, and its value gives exactly the number of minima. This completes the proof.

## Verification
Running \(\texttt{python3 verify.py}\) with a standard Python 3 interpreter reconstructs the complete \(225\)-state matrices from the definition, checks \(A^8=A^2\) entrywise, derives all three numerator polynomials with exact integer arithmetic, and compares all coefficients to the stated certificate. It also exhaustively checks all four-label assignments for prism lengths \(3\), \(4\), and \(5\). It then independently generates every possible uncoloured support with at most two fully coloured rungs, computes all admissible named three-colourings by backtracking, and compares all \(30\) cases for \(3\le m\le12\). It also checks the residue formulas for lengths through \(99\); those sampled checks are not the infinite proof. The successful run reports \(\texttt{VERIFY_OK}\).

The exact finite matrix identities, together with formal-series algebra and the bijection from assignments to cyclic walks, establish the theorem for every \(m\ge3\). The independently enumerated small cases and numerical regression tests are supplementary.

## Relationship to prior work
Žerovnik, *On Singleton 3-Rainbow Domination of Cylindrical Graphs* (2026), studies the same singleton model on \(P_s\square C_m\), including the two-row cylinder. Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow \(k\)-Domination in Regular Graphs* (2026), Theorem 19 and Appendix B, establishes exact minimum weights for prisms. Kuzman's *On \(k\)-rainbow domination in regular graphs* (2019 preprint, 2020 journal), Theorem 4.2, concerns the broader set-valued invariant and provides a related lower-bound framework. None of the inspected material supplies the all-order, labelled-colour optimal-assignment multiplicities proved here; the numerical minimum alone does not determine their counts. The originality assessment is historical-priority qualified, not a claim of exhaustive literature coverage.

## Limitations
Only singleton three-colour assignments and the multiplicities at *minimum weight* are enumerated. The complete higher-weight polynomial, quotients by automorphisms or colour relabeling, general \(P_s\square C_m\) with more than two rows, and the set-valued rainbow model remain outside the claim. A publisher page for the two-row cylindrical-graph predecessor returned an access limit, so an uninspected part of that source remains a priority risk. Historical-priority verification by an independent expert has not been carried out.

## References
1. J. Žerovnik, *On Singleton 3-Rainbow Domination of Cylindrical Graphs*, Mathematics **14** (2026), 2917; DOI: 10.3390/math14162917; publicly available 2026-08-12.
2. P. Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow \(k\)-Domination in Regular Graphs*, arXiv:2610.06906 (first version 2026-10-01), especially Theorem 19 and Appendix B; https://arxiv.org/abs/2610.06906.
3. B. Kuzman, *On \(k\)-rainbow domination in regular graphs*, arXiv:1907.08430 (2019), Discrete Applied Mathematics **284** (2020), 454–464, especially Theorem 4.2; https://arxiv.org/abs/1907.08430.
