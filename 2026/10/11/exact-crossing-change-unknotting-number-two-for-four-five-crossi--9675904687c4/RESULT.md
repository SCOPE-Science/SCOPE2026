# Exact crossing-change unknotting number two for four five-crossing virtual knots
## Finding
For each of the Green-table virtual knots \(5.40\), \(5.107\), \(5.880\), and \(5.1238\), the crossing-change unknotting number is
\[
u=2.
\]
The recent table of Acu, Pongtanapaisan, and Singhal records only \(u\le 2\) for these four knot types. The exact value follows by combining a sharp odd-writhe lower bound with explicit two-change reductions.

## Assumptions and scope
The knot names and signed Gauss codes are the Green-table labels and codes printed in Appendix 6.2 of Acu--Pongtanapaisan--Singhal. A crossing change interchanges the over/under status at one classical crossing and reverses its crossing sign. The unknotting number \(u\) counts crossing changes; virtual Reidemeister moves and detours are free equivalences.

For a signed Gauss code, a classical crossing is called odd when an odd number of endpoints lie strictly between its two occurrences. Kauffman's odd writhe \(J\) is the sum of the signs of all odd crossings.

## Proof
For each of the four printed Gauss codes, the endpoint positions have the same parity pattern: crossings \(1,2,4,5\) are odd and crossing \(3\) is even. In all four cases crossings \(1,2,4,5\) are negative. Hence
\[
J=-1-1-1-1=-4.
\]
Kauffman proved that \(J\) is invariant under virtual-knot equivalence. A crossing change does not change the underlying chord diagram, hence does not change which crossing is odd; it only reverses the sign of the changed crossing. Therefore a single crossing change changes \(J\) by \(0\) if the crossing is even and by \(\pm2\) if it is odd. Since the unknot has \(J=0\), every crossing-change unknotting sequence from any of these four knots has length at least \(2\).

For the upper bound, change crossings \(1\) and \(4\). For \(5.40\) and \(5.107\), the changed code admits the cancellations
\[
RII(4,5),\qquad RI(3),\qquad RII(1,2),
\]
ending at the empty Gauss code. For \(5.880\) and \(5.1238\), it admits
\[
RII(1,2),\qquad RI(3),\qquad RII(4,5),
\]
again ending at the empty Gauss code. Thus two crossing changes suffice for every knot in the four-element set. Together with the odd-writhe lower bound, this proves \(u=2\) in all four cases.

## Verification
The standalone verifier `artifacts/verify_unknotting.py` hardcodes the four source Gauss codes, recomputes chord parity and \(J\), checks the lower bound \(|J|/2=2\), performs the two crossing changes, checks the local signed Gauss-code conditions for each stated type-I or type-II Reidemeister cancellation, and verifies that the final code is empty. Its expected terminal line is:

`VERIFY_OK knots=5.40,5.107,5.880,5.1238 odd_writhe=-4 lower_bound=2 upper_bound=2`

The finite checker is not being used as a substitute for an infinite theorem: the claim concerns exactly four explicitly specified finite Gauss codes, while the only general input is Kauffman's proved invariance of odd writhe.

## Relationship to prior work
Acu--Pongtanapaisan--Singhal give the four signed Gauss codes and list the unknotting entry only as \(u\le2\), explicitly distinguishing such upper bounds from exact table values. Kauffman introduced the odd writhe and proved its invariance, but does not compute these Green-table entries or their unknotting numbers. The present claim is the exact-value consequence obtained by computing \(J=-4\) on these four source codes and independently exhibiting two-change reductions.

Semantic searches for the four labels together with “unknotting number”, “crossing change”, and “odd writhe” did not locate a prior statement of these four exact values. A 2019 work on polynomial invariants mentions the Green-table labels \(5.40\)--\(5.42\) in a different classification, but the located material concerns polynomial/genus data rather than crossing-change unknotting numbers.

## Limitations
No claim is made about the remaining five-crossing rows whose table entries are only upper bounds, nor about six-crossing rows. The result does not classify all virtual knots of crossing number five. The literature comparison cannot exclude unindexed or unpublished computations; it establishes only that no covering statement was found in the inspected primary sources and targeted searches.

## References
1. B. Acu, P. Pongtanapaisan, R. Singhal, *Ascending, Bridge, and Unknotting Numbers of Knotted Graphs*, arXiv:2610.00788v1 (2026), especially Appendix 6.2.
2. L. H. Kauffman, *A Self-Linking Invariant of Virtual Knots*, arXiv:math/0405049v1 (2004); Fundamenta Mathematicae 184 (2004), 135--158, DOI 10.4064/fm184-0-10.
