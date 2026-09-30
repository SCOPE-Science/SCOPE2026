# Independent Audit — 2026-09-30

**Record:** `2026/09/19/subfield-rank-law-identical-linear-leakage--231ee5b4c708`  
**Title:** Subfield-rank law for identical leakage under linear computations  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `a2bdd9cf27787dc5876494bd535df6517b6714a3`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** PASS. Every nonzero B-linear functional F→B is Tr_{F/B}(beta·) with beta≠0, and the trace pairing identifies the N leakage coordinates with the coefficient vectors beta g_i. Multiplication by beta is a B-linear automorphism, so the leakage-map B-rank is exactly the B-span dimension of the computation columns. Basis-column compression follows immediately. The descent criterion rho_B(G)=K is also correct: a B-basis of the column span must be F-linearly independent because the columns have F-rank K, and its inverse puts all columns in B^K. The rho=K global LERS equivalence follows after selecting K invertible basis-column streams; the rho=Km case is injective locally. The random systematic formula is the standard full-rank probability in the K(m-1)-dimensional quotient. The supplied verifier independently checks 76,200 trace-rank instances and the stated endpoint examples.
- **Originality — PASS:** PASS, with standard rank-metric ingredients explicitly excluded from the novelty claim. Aoutouf–Augot's public abstract introduces arbitrary linear computations and highlights identical leakage as a realistic submodel, while older rank-weight literature treats information leakage in network coding in different models. Targeted searches did not locate the exact statement that reused one-symbol trace leakage has rank equal to the B-column rank of the computation generator, nor the resulting descent/full-disclosure/random-systematic corollaries. The theorem is elementary once the invariant is identified, so near-simultaneous priority risk remains.
- **Scientific value — PASS:** PASS. The exact rank identity cleanly quantifies how much repeated leakage a computation layer creates, separates no-amplification and full-disclosure regimes, and turns several motivating examples into consequences of one invariant. The random systematic threshold gives a useful probabilistic interpretation beyond a single counterexample.

## Independent findings
- Left multiplication by GL_K(F) preserves B-column rank because every F-linear map is also B-linear.
- For a three-wire relation, the third column increases the B-span by exactly one unless both coefficients lie in B.
- Full B-column rank Km makes every nonzero repeated trace functional injective on the K-symbol local state.
- The checked verifier reports PASS for 76,200 rank-identity checks, 65,216 base-field transcript checks, 308 saturation checks, and 11 exact random-threshold cases.

## Independent checks
- Re-derived the rank identity from finite-field trace duality.
- Checked the descent-to-B iff rho=K criterion and the global LERS reduction.
- Recomputed the systematic quotient dimension D=K(m-1) and full-rank probability.
- Inspected the repository verification script and recorded output.

## Literature evidence
- https://arxiv.org/abs/2609.19929 — Aoutouf–Augot motivating framework for leakage under linear computations and identical leakage functions.
- https://wcc2026.inria.fr/assets/final_versions/WCC2026_paper_33.pdf — Earlier subfield-subcode LERS construction; different from the computation-column rank law.
- https://eprint.iacr.org/2019/653 — Local leakage resilience of linear secret sharing background.
- https://arxiv.org/abs/1603.06477 — Generalized rank-weight/information-leakage prior art in network coding; different leakage model.

## Limitations
- The theorem is restricted to identical one-symbol B-linear leakage and linear computation layers.
- The intermediate K<rho_B(G)<Km regime quantifies local information dimension but does not itself decide global attack existence.
- Rank weight, rank support, trace duality, and field-of-definition criteria are prior art; originality is only the application/identity and its stated corollaries.

The assigned source-tree SHA still matches the current record tree inspected on `main`. GitHub was used only as read-only evidence; no repository writes were made.
