# Independent Audit — Inseparable quadratic extensions add a missing family of trace-prime algebras

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned/current source tree:** `c60c8f7c50290955da301bd27a25142cb5c18223`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The inventory-snapshot and current-main directory entries match exactly by child Git blob/tree SHA, so the assigned source-tree SHA remains the current tree audited. GitHub was used read-only as evidence.

## Correctness — PASSED

PASS. For a nonzero F-linear trace operation t on a quadratic field E, rank two makes t surjective; choosing y with t(y)=x in t(t(y)·1)=t(y)t(1) forces t(x)=t(1)x. If rank one, choose z=t(u)≠0. Since t(E)=Fz and t(zu)=z^2 lies in Fz, field cancellation gives z∈F^×, hence t(E)=F and t is an arbitrary nonzero F-linear functional E→F. Conversely multiplication maps and F-valued linear functionals both satisfy the trace axiom. The classical trace-pairing criterion identifies the scalar-valued functionals with Tr(cx) exactly in the separable case; for a purely inseparable quadratic extension in characteristic two the field trace is zero. The explicit F_2(s)⊂F_2(s^{1/2}) coefficient functional is therefore a valid tr-prime counterexample to the source's arbitrary-field classification. The isomorphism-orbit description under Aut_F(E) is also correct, and the purely inseparable quadratic automorphism group is trivial.

## Originality — PASSED

PASS, with the classical boundary made explicit. Nondegeneracy of the field-trace pairing for separable extensions is standard and is not new. Centrone–Trindade Barbosa–Yasumura's September 2026 preprint advertises an arbitrary-field classification; targeted searches did not locate a correction addressing the inseparable quadratic case. The original contribution is the source-specific correction: replacing the failed Tr(cx) parametrization by all nonzero functionals in Hom_F(E,F), together with the explicit omitted tr-prime family and corrected isomorphism statement.

## Scientific value — PASSED

PASS. The record identifies a genuine missing family in an advertised arbitrary-field classification, gives an exhaustive repair rather than only a counterexample, and sharply explains why the later finite-field results are not directly affected because finite fields are perfect. This is a useful mathematical correction with clear scope.

## Independent checks

- Re-derived the rank-one/rank-two classification directly from the trace-algebra axiom.
- Checked the explicit purely inseparable quadratic example and its zero field trace by multiplication-matrix trace.
- Checked the standard separability/nondegenerate-trace-pairing criterion and its consequences for the source parametrization.
- Rechecked the isomorphism criterion and trivial automorphism group in the purely inseparable quadratic case.
- Searched for source-specific corrections/errata and found no public correction covering this omitted family.
- Verified inventory-snapshot and current-main record entries are byte-identical by child Git blob/tree SHA.

## Limitations

- The separability criterion and trace-pairing facts are classical and are not credited as original.
- The correction concerns the arbitrary-field quadratic-extension part; it does not directly refute finite-base-field results.
- The source preprint may be revised after this audit date, so the priority finding is current to the audited version.

## Evidence and references

- https://arxiv.org/abs/2609.19797
- https://stacks.math.columbia.edu/tag/0BIE
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/inseparable-quadratic-trace-algebra-classification--042b71181929

This staged audit changes only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
