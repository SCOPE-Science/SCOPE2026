# Independent mathematical audit — Depth-one local Clifford ensembles are non-plussed distinct

Audited on 2026-10-01 UTC.

**Disposition:** PASSED

## Correctness — PASS

The proof reconstructs the DNP estimate from the exact FLM intersection machinery. FLM Lemma 7.15 gives \(c(\mathrm{Dist},\mathrm{NoPlus})^2\le t(t-1)/(N-t+1)\), and the proof of their Theorem 7.7 supplies the factor-4 union-bound losses. Independently, \(I-\Pi_{\mathrm{NoPlus}}\preceq\sum_j |+\rangle\langle+|_j\) gives the \(t\mu_+\) term. For a local exact 2-design the two-copy equality projector twirls to \((2/(d+1))\Pi_{\mathrm{sym}}\); independence over \(n\) sites gives \((2/(d+1))^n\), and a pair union bound gives the displayed collision estimate. A tensor product of local 1-designs is a global 1-design. These steps establish the stated bound for \(2\le t\le N/2\).

## Originality — PASS

The final contribution is the lifting principle 'ordinary distinctness plus one-copy plus-state flatness implies DNP concentration' and its product-local-design/local-Clifford corollary. The motivating paper explicitly leaves the local-Clifford DNP question open, while FLM proves DNP concentration for global unitary 2-designs. No published SCOPE/resultary hit or primary source inspected states the product-local corollary or general lifting inequality.

### Equivalent formulations

The local-product theorem is not a renaming of FLM's global 2-design result because the product ensemble is not a global 2-design; the proof replaces global two-copy randomness by ordinary-distinctness plus one-copy flatness.

Evidence: Resultary returned this record but no equivalent earlier finding. The Raza--Eisert--Fefferman discussion asks whether independent depth-one single-qubit Cliffords are non-plussed distinct. FLM defines DNP as Distinct intersect NoPlus and proves the global-2-design theorem.

### Broader coverage

Neither prior theorem dominates the final implication: one has the needed geometry but a stronger randomization hypothesis; the other has the target ensemble but only ordinary distinctness.

Evidence: FLM's broader geometric intersection lemma is prior and is explicitly used, but its probabilistic hypothesis is a global unitary 2-design. Raza--Eisert--Fefferman proves ordinary distinctness for the depth-one local Clifford ensemble but leaves the stronger DNP property open.

### Exact database or table

The claim is theorem-level, not a database/table lookup; the relevant exact-index search was nevertheless performed.

Evidence: No earlier database/table entry with the theorem was found; Resultary's only exact thematic hit was this record.

### Claim versus prior implication

The final claim is a nontrivial corollary of combining distinct prior ingredients with a new general sufficient condition; neither cited prior result alone mechanically implies it.

Evidence: FLM supplies the geometric inequality but does not imply the local product ensemble satisfies the needed separate conditions without the new calculation. Raza's ordinary-distinctness bound plus local design facts becomes sufficient only after the lifting inequality is isolated.

### Source inspections

- **Quantum Lazy Sampling and Path Recording for Any Group** — COVERING for the geometric bound, NOT_COVERING for product-local-design DNP.. Material read: Section 7.1 excerpts including Lemma 7.15 and the proof of Theorem 7.7. Evidence: Lemma 7.15 states \(c^2\le t(t-1)/(N-t+1)\); Theorem 7.7 combines this with factor-4 Dist/NoPlus errors for global 2-designs.
- **Distinctness threshold for pseudorandom unitaries** — NOT_COVERING; it leaves the target stronger property open.. Material read: Abstract plus indexed discussion/open-question quotation. Evidence: The indexed discussion asks whether the depth-one independent single-qubit Clifford ensemble is non-plussed distinct.

### Checked sources

- arXiv:2609.03065
- arXiv:2606.30281
- Resultary published findings

### Residual risks

- The question and solution are close in time, so unindexed near-simultaneous work remains possible.
- This audit does not claim that DNP concentration alone removes the binary phase layer in a full PRU security proof.

## Scientific value — PASS

This resolves an explicit open question for a natural depth-one quantum ensemble and extracts a reusable sufficient condition that applies beyond global 2-designs. It is a motivated structural lemma with a concrete cryptographic application, not an arbitrary parameter slice.

## Limitations

- The result is for parallel forward-query states and does not by itself prove PRU security after removing the binary phase layer.
- The exact constants are not claimed optimal.
- The motivating papers are recent, so near-simultaneous priority remains a residual risk.
