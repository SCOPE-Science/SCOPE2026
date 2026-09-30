# Independent audit — Exact square separation for Dunford--Pettis ideals on finite measure L1 spaces

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/dunford-pettis-square-finite-atomless-l1--bef9222a1236`  
**Audited tree:** `980d1bffe9473b2a58fca7baa255f6cb61b9dc03`

## Disposition

**PASSED.** All three required axes pass. Publication may remain in the validated record set.

## Correctness

**PASS.** The cross-space argument is coherent and closes the compression obstruction. For positive Dunford--Pettis A:L1(T)->Z and B:Z->L1(T), splitting off the atomic band makes that contribution representable. On the atomless band, positive kernel representations yield measures beta_omega and alpha_omega. If either kernel has atoms on a positive-measure set, measurable atom selection produces a positive suboperator dominated by A or B; a pulled-back Rademacher sequence is weakly null while its image has fixed positive norm, contradicting order solidity of the Dunford--Pettis ideal. Hence the kernels are atomless a.e., so Nasseri’s polar convolution lemma annihilates the averaged symbol on P. This makes Theta_Z kill every product and therefore the closed square. The right inverse J_P, exact distance identity, Lewis--Stegall factorization for the lower inclusion, singular convolution-square witness for strictness, and purely atomic Schur-property converse then follow as stated.

## Originality

**PASS.** Nasseri’s public arXiv abstract states the exact square-ideal result on L1(0,1) and separately says that the approximate-identity obstruction extends to arbitrary finite measure spaces; it does not advertise the assigned finite-measure square extension. The earlier SCOPE persistent-idempotent record concerns power ideals on L1[0,1] and is not this cross-space transfer theorem. Targeted repository/literature checking found no prior arbitrary-finite-measure exact square separation or the cross-space polar-product lemma. The originality conclusion is to the best of current search.

## Scientific Value

**PASS.** The result preserves the strongest part of the separable model theorem—an exact quotient distance and contractively complemented copy—while extending it to every finite measure algebra with an atomless part, and it gives the exact atomic/atomless boundary. The cross-space polar-product lemma is also a reusable structural mechanism rather than a formal restatement.

## Independent checks

- Reconstructed the positive-kernel atomlessness contradiction on both sides, including the absolute-continuity pushforward needed for well-defined pulled-back Rademachers.
- Checked that the atomic intermediate band factors through l1 and hence gives an absolutely continuous symbol on the Haar-null polar set.
- Verified the factorization G_Z⊆I_2 using a complemented l1 copy and the purely atomic converse using the Schur property.
- Compared the public Nasseri abstract and earlier SCOPE power-ideal record; neither states the assigned arbitrary-finite-measure exact square theorem.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.18348 — Nasseri (2026), exact square theorem on L1(0,1); abstract separately advertises only the approximate-identity extension to arbitrary finite measure spaces.
- https://www.theta.ro/jot/archive/1998-040-001/1998-040-001-001.pdf — Liu (1998), kernel/decomposition background for operators from compact-metric L1 into atomless L1.
- https://kaltonmemorial.missouri.edu/assets/docs/illjm1985.pdf — Kalton--Saab (1985), regular-operator and Dunford--Pettis order-ideal background.
- https://doi.org/10.1016/0022-1236(73)90022-0 — Lewis--Stegall factorization background for representable L1 operators.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/18/persistent-idempotent-dunford-pettis-power-ideals--3d49db0c2e39 — Earlier SCOPE power-ideal result on L1[0,1], related but not overlapping with the finite-measure square transfer.

## Limitations

- The audit independently verified the public arXiv abstract but did not line-verify the package’s quoted Remark 6.2/open-question wording from the full Nasseri PDF in this run.
- Only finite measure spaces are covered; infinite/localizable cases and higher closed powers remain open here.
- The argument relies on classical kernel representation and order-ideal facts rather than formal proof-assistant verification.

## Repository identity

The assigned source-tree SHA `980d1bffe9473b2a58fca7baa255f6cb61b9dc03` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
