# Scientific review: exact periodic-marker maximal-pattern complexity

## Correctness — PASS

For any finite sampling window, the proof separates \(m\) possible starting phases. Each active phase sees binary symbols in exactly one residue class of the window; all remaining entries are constant markers. Because the alphabets are disjoint, no two distinct active phases can overlap in the observed word, and a silent marker-only phase cannot overlap an active phase. The single-step carry in the binary index is harmless by uniform recurrence. This proves the exact window identity \(p_y(T)=\sum_{r\in S}p_x(U_r)+D_w(S)\). Choosing independently maximizing binary windows proves the exact extremal formula for every \(k\geq1\). The single-defect signature count follows from a bijection with cyclic occupied-to-empty transitions and the existence of an adjacent pair in the complement. Explicit separated-residue selections attain both branches of the claimed sharp maximum. There are no unchecked limiting arguments, and the verifier's finite tests are not treated as an infinite proof.

## Originality — PASS, subject to recorded priority risks

Schlortt, arXiv:2505.05627v1, §5 Theorem 1.3 and §6, establishes only eventual \(2k+C\) for this structure and exhibits certain previously known sharp examples. The new claim is the full all-length cyclic-signature formula and the unbounded correction \(\min\{k+1,\lceil m/2\rceil\}\) at fixed four-letter alphabet. Le, Pavlov and Schlortt, arXiv:2508.13420v1, §4.3, establishes structural interleaving categories rather than exact template counts. The original binary pattern Sturmian \(2k\) law is not new. Indexed semantic and primary-literature comparisons were made against alternative terminology, exact parameter coverage and possible stronger results. The 2006 Toeplitz abstract advertises an almost-exact formula for one-hole Toeplitz words; its full text was not inspected, so any intersecting specialized result remains a genuine priority risk. Neither that abstract nor the inspected stronger structural classifications covers arbitrary irrational Sturmian bases with the explicit constant. This assessment is not an independent priority guarantee.

## Mathematical value — PASS

The explicit symbolic family is central to an existing structure theorem whose eventual additive offset is left undetermined. Counting *all* sampling lengths and *all* marker templates settles a natural combinatorial invariant. A template with one exceptional marker exhibits arbitrarily large eventual \(p_y^*(k)-2k\) on just four symbols, including the exact onset of the plateau. The fixed-alphabet unboundedness is a meaningful mechanism distinct from an isolated computation, a routine finite example or a formal change of notation.

## Verification and limitations

The analytical derivation is self-contained conditional on the standard pattern Sturmian hypothesis. The standalone Python 3 checker recomputes 17861 finite exact assertions from periodic rational mechanical test words, direct sample enumeration and independent marker signature counts. It tests the finite identities, not the universal irrational case. No claim is made for overlapping marker/binary alphabets, several nonconstant residues, or nonuniformly recurrent bases. Priority remains subject to specialized literature and external expert assessment.

Self-review: passed. Independent audit: not yet performed.
