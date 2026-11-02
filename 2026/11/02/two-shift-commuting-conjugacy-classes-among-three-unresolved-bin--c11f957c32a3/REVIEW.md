# Scientific review: two conjugacy classes among three unresolved binary two-to-one cellular automata

## Correctness (PASS)

The three five-site Boolean polynomials have been copied directly from the three question-mark rows of Appendix B in Haugland--Larsen--Omland--Rustad (2026). The proposed factorization is a Boolean identity on every five-bit input: \(A=PD\), \(B=DP\). The proposed two-sided local inverse of \(P\) is verified on its entire seven-bit support. Locality extends these identities from their exhaustive finite support to every bi-infinite configuration, so \(P\) is a genuine shift-commuting homeomorphism. The complete 32-state ring graphs give time-cycle length profiles \((1,10)\), \((1,10)\), \((1,5)\); their fifth-time fixed-point cardinalities are therefore \(1,1,6\). Shift-commuting conjugacy would preserve both the spatial period-five subspace and these counts. The proof uses this invariant only for the nonconjugacy conclusion and does not improperly extrapolate ring data to global dynamics.

## Originality (PASS; priority uncertainty remains)

The 2026 source (arXiv:2610.33131v1, Appendix B, page 27) tabulates exactly the same three two-to-one binary maps but poses the LEO questions separately and does not assert a conjugacy or the periodic-point separation. The 2024 source (arXiv:2411.00721v1, Example 1.3) already identifies \(P\) as a reversible local rule; no discovery of its reversibility is claimed here. Its known bijectivity alone neither identifies \(A=PD\), \(B=DP\), nor separates \(C\). Comparison of those logical implications, targeted mathematical-record queries and previously accessible claim statements did not produce the three-representative conjugacy classification. An author might have recognized the \(PD/DP\) relationship without publishing it, and unindexed or subsequent results might duplicate it. No independent priority certification is claimed.

## Value (PASS)

These three maps are precisely the outstanding two-to-one, five-site examples in a recent systematic small-diameter LEO study. A complete two-class conjugacy classification is a natural structural invariant of that distinguished family, not an arbitrary numeric slice. The explicitly reversible conjugacy proves that two unresolved LEO decisions are equivalent; the fifth-iterate obstruction certifies that the third representative cannot be folded into the same shift-preserving conjugacy class. This reduces the dynamical classification and the number of independent questions still to examine. It is not a purported resolution of either LEO question.

## Sources and limitations

Primary sources: Haugland--Larsen--Omland--Rustad, *Locally eventually onto cellular automata*, arXiv:2610.33131v1 (Appendix B, p. 27); Haugland--Omland, *New classes of reversible cellular automata*, arXiv:2411.00721v1 (Example 1.3). The symbolic calculations and complete period-five graphs are reproducible through `verify.py`. The theorem applies to these three displayed local-rule representatives and shift-commuting conjugacy; the LEO status of the two classes, conjugacy without shift commutation, and classification beyond this trio remain open or unaddressed. Earlier private or unindexed work could affect novelty.

Self-review: passed. Independent audit: not yet performed.
