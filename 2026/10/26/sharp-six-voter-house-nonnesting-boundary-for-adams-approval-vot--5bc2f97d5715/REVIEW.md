# Review of the three-candidate Adams-AV house-nonnesting theorem

## Correctness

**PASS.** The rule is reconstructed from Baychkov et al., Definition 6: priority is maximum voter coverage, then marginal weights \((1,1,1/2,\ldots)\), giving a two-seat secondary score of covered voters plus double-approvers. Strong nonnesting on three candidates requires unique optimum singleton and pair. Strict singleton support and the tied-coverage secondary comparisons force \(v,w\ge u+1\), \(p,q\ge r+2\), and hence \(n\ge6+3u+3r+t+e\). Equality determines the unique labeled profile after choosing its winning singleton, and the witness's exact scores establish sufficiency. `verify.py` checks 3002 complete anonymous profiles through six voters, including empty ballots. Enumeration is supporting evidence, not the proof for arbitrary \(n\).

## Originality

**PASS within accessible comparison, with historical-priority uncertainty.** The 2026 Adams-AV primary paper introduces the rule and its quota properties but its inspected definitions, discussion, and appendices do not give a house-nonnesting minimum or classify all minimum profiles. General Thiele optimization and CC provide related nonnesting counterexamples, but qualitative failure or an example with more voters does not imply this lexicographic rule's precise minimality and equality class. A semantic mathematical research index search for Adams-AV/CC/house monotonicity and searches of available source text yielded no equivalent or stronger exact result. This does not exclude an earlier differently worded statement, particularly about CC or tie-break-independent minimality.

## Mathematical value

**PASS.** Adams-AV was proposed specifically to transfer an upper-quota apportionment principle into approval-based committees. It is therefore natural to test which committee-size consistency guarantees survive this generalization. The theorem determines the first robust nonnesting boundary and fully classifies the extremal ballots; it also proves that the secondary tie-break cannot cause an earlier robust failure. This is a precise behavioral boundary useful for rule comparison and regression instances, rather than a mere arbitrarily sized negative example. It is limited to three candidates and does not refute upper quota.

## Limitations and literature

Principal source: Baychkov et al., arXiv:2606.19968v1 (2026), Definition 6, Sections 2–3, Appendix B and C. Context: CC and Thiele optimization, and a distinct larger committee-nonnesting test example in STAR Voting Education & Test-Case Library. Remaining risk: unknown historical claim phrased in terms of CC refinement could encompass the exact minimum. No independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
