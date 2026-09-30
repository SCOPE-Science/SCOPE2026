# Independent audit — Tensor amplification yields maximal amenable–quasidiagonal trace separation

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/18/tensor-amplified-maximal-amenable-qd-trace-separation--497bed58636c`  
**Audited tree:** `dfdf77c61847f75685bb593c1bfd818d09fe9a31`

## Disposition

**PASSED.** All three required axes pass. Publication may remain in the validated record set.

## Correctness

**PASS.** The abstract amplification theorem is correct. Conditioning a quasidiagonal trace on a positive-mass projection in a commuting tensor factor can be implemented by spectral compression of quasidiagonal u.c.p. approximants; this yields quasidiagonal conditional traces. Applying that lemma one coordinate at a time forces equal masses on adjacent word sectors and hence mass 2^{-r} on every word. The lower norm bound is obtained by the norm-one self-adjoint unitary 2E_ω-1, and the quasidiagonal product trace λ^{⊗r} attains the same value because its complementary component is supported on 1-E_ω. The infinite-product distance 2 follows by restriction to each finite tensor stage. The application to Moradi is also supported by the source: Lemma 3.2 gives τ_∞=(μ_0+μ_1)/2 with sector-supported μ_i, and Theorem 4.1 gives equal sector mass for every quasidiagonal trace.

## Originality

**PASS.** Moradi's 2026 preprint proves the two-sector balance and failure of faciality but does not state tensor-power sector amplification or the exact dual-norm distances 2(1-2^{-r}) and 2. Targeted searches for quasidiagonal/amenable traces combined with tensor powers and norm distance did not locate an earlier equivalent statement. Standard permanence facts for quasidiagonal and amenable traces are prior art and are not counted as novel; the originality claim is limited to the sector-amplification theorem and its exact metric consequences.

## Scientific Value

**PASS.** The result turns a qualitative counterexample to faciality into a quantitative separation theorem: finite RFD tensor powers produce amenable traces at exact distance tending to the full state-space diameter, and the infinite tensor power reaches distance 2. This is a clear and reusable strengthening of the source construction.

## Independent checks

- Reconstructed the projection-conditioning argument from u.c.p. quasidiagonal approximants: spectral projections of φ_n(1⊗q) give normalized compressed matrix models with the required multiplicativity and trace limit.
- Checked the hypercube argument: conditional equality in each coordinate makes masses constant along every edge, and the 2^r orthogonal word projections sum to 1, forcing mass 2^{-r}.
- Recomputed the exact distance: evaluation on 2E_ω-1 gives 2(1-2^{-r}); λ^{⊗r}=2^{-r}μ_ω+(1-2^{-r})θ_ω with orthogonal supports gives equality.
- Checked the infinite-stage argument by restricting any quasidiagonal trace to finite tensor stages and letting r→∞.
- Read Moradi arXiv:2609.18793v1 in open-access HTML: Lemma 3.2 states τ_∞=(μ_0+μ_1)/2 with μ_ε(e^δ)=δ_{εδ}, and Theorem 4.1 states every quasidiagonal trace has equal sector masses.

## Literature and prior-art boundary

- https://arxiv.org/html/2609.18793v1 — Moradi (2026), source construction. Lemma 3.2 gives the equal sector decomposition of τ_∞; Theorem 4.1 gives equal masses for every quasidiagonal trace.
- https://arxiv.org/abs/math/0304009 — Brown (2006), standard background on amenable/quasidiagonal traces and finite-dimensional approximation; auxiliary permanence facts are treated as prior art.

## Limitations

- The infinite tensor power is not asserted to be RFD, exact, nuclear, simple, or UCT.
- The result requires the specific rigid two-sector balance hypothesis; it is not a general amplification theorem for every failure of faciality.
- Originality is to the best of the targeted literature search; general trace-permanence theory may subsume auxiliary lemmas but no earlier exact sector-distance theorem was located.

## Repository identity

The assigned source-tree SHA `dfdf77c61847f75685bb593c1bfd818d09fe9a31` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
