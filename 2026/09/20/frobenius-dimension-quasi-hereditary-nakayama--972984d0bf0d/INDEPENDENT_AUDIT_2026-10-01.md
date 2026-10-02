# Independent scientific audit — SCOPE-20260920-972984d0bf0d

Audited at: 2026-10-01T19:12:08.377982Z

Disposition: **passed**

## Correctness — PASS

The interval description of uniserial Nakayama modules gives the stated Hom-count formula and writes Frobenius dimension as the sum of \(n^2\) injective-projective Hom dimensions. For a cyclic quasi-hereditary algebra, the primary Nakayama classification confirms both that some simple has projective dimension two and that \(\operatorname{pd}S_i=2\) exactly when \(c_{i+1}+1=c_i+c_{i+c_i}\). After rotation this makes the endpoint sequence constant from indices \(1\) through \(p=c_0\); periodicity forces \(p\le n\). The resulting length bounds make every Hom at most two, and the interval congruence shows that a two-dimensional Hom can occur only for \(I_R=P_1\). The displayed Kupisch family has every one of the \(n^2\) pairs nonzero and exactly that one double pair, hence \(F(A)=n^2+1\).

### Correctness sources

- assigned RESULT.md
- https://arxiv.org/html/1811.05846v2
- https://arxiv.org/abs/2607.15999

### Correctness risks

- The proof is specialized to connected basic Nakayama algebras over an algebraically closed field, exactly as stated.

## Originality — PASS

The complete 2026 Frobenius-dimension preprint was inspected and proves bounds in terms of total vector-space dimension plus formulas for truncated path algebras, but it does not state or imply the fixed-number-of-simples quasi-hereditary Nakayama extremum. The 2020 MathOverflow page explicitly poses and numerically conjectures the \(n^2+1\) maximum. The Nakayama classification provides the homological criterion used in the proof, not the Frobenius-dimension optimization.

### Equivalent formulations

No earlier equivalent theorem was located; the later restatement does not establish prior coverage of the 2026-09-20 claim.

### Broader coverage

These sources are broader in algebra class or homological classification, but neither determines the exact maximum at fixed number of simples.

### Exact database or table

The object is an extremal theorem rather than a table lookup; conjectural tabulation does not cover the proof.

### Claim versus prior implication

The final bound and sharp family require the new endpoint-plateau/unique-double-Hom optimization and are not mechanical corollaries of the inspected results.

### Sources inspected

- Bounds on Frobenius dimension — https://arxiv.org/abs/2607.15999. NOT_COVERING: No theorem treats quasi-hereditary Nakayama algebras at fixed number of simples or gives the \(n^2+1\) extremum.
- A combinatorial classification of 2-regular simple modules for Nakayama algebras — https://arxiv.org/html/1811.05846v2. COVERING_INGREDIENT: It verifies the projective-dimension-two criterion and the quasi-hereditary cyclic criterion used by the proof, but contains no Frobenius-dimension extremum.
- Frobenius dimensions of Nakayama algebras — https://mathoverflow.net/questions/351323/frobenius-dimensions-of-nakayama-algebras. OPEN_PROBLEM_SOURCE: The page motivates exactly the maximum \(n^2+1\) and presents it as a conjectural pattern.

### Checked sources

- https://arxiv.org/abs/2607.15999
- https://arxiv.org/html/1811.05846v2
- https://mathoverflow.net/questions/351323/frobenius-dimensions-of-nakayama-algebras
- https://doi.org/10.1080/00927872.2022.2063301
- Resultary semantic search

### Residual risks

- A very recent or poorly indexed independent solution of the MathOverflow extremal problem could exist, but no such source was located after inspecting the most plausible same-invariant preprint in full.

## Value — PASS

This is an exact all-\(n\) answer to a motivated published extremal problem, with a structural explanation and an explicit sharp family. It is not a routine recomputation of small cases.

### Value sources

- https://mathoverflow.net/questions/351323/frobenius-dimensions-of-nakayama-algebras
- https://arxiv.org/abs/2607.15999

### Value risks

- The theorem does not address the separate lower-bound question for arbitrary finite-global-dimension Nakayama algebras.

## Limitations

- The theorem is for connected basic finite-dimensional Nakayama algebras over an algebraically closed field.
- It resolves the extremal quasi-hereditary question, not the separate finite-global-dimension lower-bound question.
- Originality remains best-of-knowledge against very recent parallel work.
