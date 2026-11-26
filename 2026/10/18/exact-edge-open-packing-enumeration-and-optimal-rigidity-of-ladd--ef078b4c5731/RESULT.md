# The edge-open-packing size enumerator of the two-row ladder

## Finding

For the ladder \(L_n=P_2\square P_n\) with \(n\ge1\) rungs, let \(E_n(z)=\sum_B z^{|B|}\), where \(B\) ranges over all edge-open packings, including the empty packing. Then
\[
\sum_{n\ge1}E_n(z)t^n=\frac{tN(t,z)}{D(t,z)},
\]
where
\[
\begin{aligned}
N(t,z)&=1+z+t(3z+4z^2)+t^2(z+5z^2+2z^3)+t^3z^4+t^4(z^4-z^3),\\
D(t,z)&=1-t-2t^2z-t^3(z+5z^2+z^3)-t^4z^3-t^5(z^4-z^3).
\end{aligned}
\]
In particular, \(a_n=E_n(1)\), the number of all packings, satisfies \(a_n=a_{n-1}+2a_{n-2}+7a_{n-3}+a_{n-4}\) for \(n\ge5\), with \((a_1,a_2,a_3,a_4)=(2,9,21,54)\). The formula counts packings at every size, and gives a fixed-order recurrence in the number of rungs for the activity-weighted count \(E_n(z)\). The maximum size, number of maxima and classification of the optimal packings were already determined in [1]; none is claimed as a new finding here.

## Assumptions and scope

Graphs are finite, simple and undirected. An edge-open packing is a subset of edges with no pair of distinct members for which a third, different graph edge joins an endpoint of one to an endpoint of the other. Two selected edges are not excluded merely for sharing a vertex. The ladder is open at both ends; the edges and their positions are distinguished, with no quotient by automorphisms. The case \(n=1\) is a single edge. The variables \(t,z\) track rungs and chosen edges, respectively, with the identity taken in \(\mathbb Z[z][[t]]\).

## Proof

Write \(r_i=u_iv_i\), \(p_i=u_iu_{i+1}\), \(q_i=v_iv_{i+1}\) for the rung, upper rail and lower rail edge anchored at column \(i\), omitting the rail edges at \(i=n\). Encode selections by masks with respective bits \(1,2,4\) and let \(w(c)\) count the bits of \(c\). The only same-column exclusion is the pair of rail edges, so the masks are \(S=\{0,1,2,3,4,5\}\) in an interior column and \(\{0,1\}\) in the last. At positive offsets the forbidden edge-type pairs, earlier anchor first, are
\[
\begin{array}{c|l}
1&(r,r),(r,p),(r,q),(p,q),(q,p)\\
2&(p,r),(p,p),(q,r),(q,q).
\end{array}
\]
Indeed a witness edge either joins different rows in the same column or joins consecutive columns in the same row. Checking the endpoints in these two cases and discarding either selected edge as witness gives exactly the listed pairs and the same-column exclusion. Anchors at distance at least three leave all endpoints at least two columns apart, so they cannot conflict. Define \(C_d(a,b)\) to mean that masks \(a,b\) contain no forbidden pair at offset \(d\).

The transfer states are the 17 ordered pairs \((a,b)\) in \(S^2\) with \(C_1(a,b)\). Let \(F_{a,b}\) be the series for nonempty continuations after these masks, starting with two zero masks before the first column. A continuation either uses just the last column or first appends an interior column and continues:
\[
F_{a,b}=t\sum_{c\in\{0,1\}}[C_1(b,c)C_2(a,c)]z^{w(c)}
+t\sum_{c\in S}[C_1(b,c)C_2(a,c)]z^{w(c)}F_{b,c}.
\tag{1}
\]
This is a bijective encoding of each packing by its masks. The factor \(t\) on each term gives a unique formal-series solution by coefficient recursion. The desired series is \(F_{0,0}\).

For an explicit calculation of the resolvent, group the states into the following five classes, in each of which the right sides of (1) coincide after the grouping:
\[
\begin{array}{c|l}
U&(0,0),(1,0)\\
V&(0,1),(2,1),(4,1)\\
W&(0,2),(0,4)\\
X&(0,3),(0,5),(2,2),(2,3),(4,4),(4,5)\\
Y&(2,0),(3,0),(4,0),(5,0).
\end{array}
\]
Substituting the allowed masks gives
\[
\begin{aligned}
U&=t(1+z)+t(U+zV+2zW+2z^2X),& V&=t(1+U),\\
W&=t(1+z)+t(Y+zV+(z+z^2)X),&X&=t(1+Y),\\
Y&=t(1+U+zW+z^2X).
\end{aligned}
\]
To check the rational solution, the numerators for \(U,V,W,X,Y\), over the stated denominator \(D\), are respectively
\[
\begin{aligned}
U_D&=tN,\\
V_D&=t+t^2z+t^3(z+4z^2)+t^4z^3+t^5(z^4-z^3),\\
W_D&=t(1+z)+t^2(z+z^2),\\
X_D&=t+t^3z^2,\\
Y_D&=t+2t^2z+t^2z^2+t^3(z+5z^2+z^3)+t^4z^3+t^5(z^4-z^3).
\end{aligned}
\]
Direct substitution into the five equations after multiplying by \(D\) verifies these polynomial identities. Since \(D(0,z)=1\), uniqueness of (1) proves the stated series. Setting \(z=1\) gives denominator \(1-t-2t^2-7t^3-t^4\) and numerator \(2t+7t^2+8t^3+t^4\); comparing coefficients proves the recurrence and its initial values.

## Verification

The retained `rational_certificate.json` provides the common denominator and numerators of all 17 states, and `verify.py` checks all cleared polynomial identities using exact integer arithmetic. From the directory with the certificate and script, the replay command is `python3 verify.py`. The additional degree and leading-coefficient identities in the script regress against the already known extremal results [1]; they are not a claim of novelty. Direct edge-subset enumeration through \(n=6\) is a further small-order check, not the basis of the generating-function identity. The retained output reports totals \((2,9,21,54,161,425)\) at the first six orders.

## Relationship to prior work and limitations

The exact rational series gives the full size distribution, including the nonoptimal packings not covered by the extremal theorem [1]. The recursion [2] for the same polynomial on forests does not apply to ladders with \(n\ge2\), which contain 4-cycles. The all-cardinality result for rook graphs [3] uses a different product family, intersecting the open ladder family at \(P_2\square P_2=K_2\square K_2\). Maximum-packing algorithms and bounds, such as [4], do not themselves enumerate all cardinalities. No priority is claimed for local transfer matrices as a method. The formula does not cover wider grids, cyclic ladders or a different convention for edge packings. The literature comparison is limited to the accessible sources; it does not establish exhaustive historical priority.

## References

1. *Three-periodic rigidity of maximum edge open packings in ladder graphs*, [Resultary d9bdf15b2f02](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-three-periodic-rigidity-of-maximum-edge-open-packings-in-ladder--d9bdf15b2f02/RESULT.md).
2. *An exact five-state edge-open-packing polynomial recursion for forests*, [Resultary 8c3bbc4f388f](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-an-exact-five-state-edge-open-packing-polynomial-recursion-for-f--8c3bbc4f388f/RESULT.md).
3. *Complete edge-open-packing polynomial and odd-square rigidity of rook graphs*, [Resultary 43a6aee37b6e](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-complete-edge-open-packing-polynomial-and-odd-square-rigidity-of--43a6aee37b6e/RESULT.md).
4. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, [arXiv:2403.00750](https://arxiv.org/abs/2403.00750).
