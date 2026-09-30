# Independent audit — 2026-09-30

## Disposition: PASSED

Record: `2026/09/19/purely-inseparable-quadratic-trace-classification--910430002ee1`

### Correctness
PASS. The rank dichotomy is exact. For nonzero t on a two-dimensional field E, rank two makes t surjective; with α=t(1), t(t(y)·1)=t(y)t(1) gives t(x)=αx for x=t(y). In rank one, im t=Fy for y=t(u)≠0 and y²=t(t(u)u)∈Fy, so field cancellation gives y∈F and im t=F. Every F-valued F-linear functional satisfies t(t(a)b)=t(a)t(b). In a purely inseparable quadratic extension the field trace is zero, so these nonzero rank-one maps cannot be Tr(c·). The explicit F2(s) example and the centroid calculation also check.

### Originality
PASS, qualified to the inspected evidence. The source preprint still publicly claims a classification of two-dimensional trace-prime algebras over an arbitrary field and no later correction or revision covering the inseparable quadratic branch was located. The separability/trace-pairing theorem is standard prior art and is not credited as new. The contribution is the application that exposes and completely replaces the missing rank-one branch, plus the dependent centroid correction.

### Scientific value
PASS. This is a targeted correction to an explicit arbitrary-field classification. The omitted objects form an entire family of tr-simple/tr-prime algebras over imperfect characteristic-two fields, while the audit correctly localizes the impact and leaves the finite-field identity theorems untouched.

### Independent findings
- The field-theoretic trace collapse in the inseparable quadratic case invalidates representation of all rank-one traces as Tr_{E/F}(c·).
- The corrected dichotomy multiplication maps versus arbitrary nonzero F-linear functionals E→F is complete.
- The centroid of a nonzero F-valued rank-one trace is F, whereas the zero trace has centroid E.
- No current author revision was located that already incorporates this correction.

### Independent checks
- Reproved the rank-two and rank-one cases directly from the trace-operator identity.
- Checked the characteristic-two example ell(a+bu)=b and the absence of nontrivial F-automorphisms for a purely inseparable quadratic extension.
- Recomputed the centroid condition c ell(x)=ell(cx).
- Compared the current source claim with the standard separability criterion for the field-trace pairing.

### Literature evidence
- https://arxiv.org/abs/2609.19797 — Centrone–Trindade Barbosa–Yasumura current preprint; public abstract still claims arbitrary-field classification.
- https://stacks.math.columbia.edu/tag/0BIE — Standard trace/separability criterion; used only as prior field theory, not as the novelty claim.

### Limitations
- The audit does not re-audit the source paper's other two-dimensional algebra branches or its finite-field T-ideal bases.
- Because the source is very recent, a not-yet-indexed author correction remains a normal contemporaneous priority risk.
