# Independent audit — 2026-10-01

## Final claim

Among eight-vertex graphs with the minimum nine edges for \(\mathcal C_{[4,6]}\)-saturation, there are exactly six isomorphism classes, with the six representatives, automorphism orders, and total of \(100800\) labeled extremal graphs stated in RESULT.md.

## Correctness — PASS

The source saturation theorem fixes the minimum at nine edges. For a nonedge \(uv\), adding it creates a forbidden cycle of length \(4,5,6\) exactly when the original graph has a simple \(u\)-to-\(v\) path of length \(3,4,5\). The actual C++ verifier was inspected and freshly replayed over all \(6906900\) labeled nine-edge graphs; it returned exactly \(100800\) saturated hits and six canonical degree-preserving isomorphism classes, with orbit sizes and representatives matching RESULT.md. Degree-preserving canonicalization is complete because every graph isomorphism preserves degrees.

Checked sources:
- Liu--Wang--Gong, Minimizing the number of edges in \(\mathcal C_{[4,6]}\)-saturated graphs, arXiv:2608.18551 (2026), primary abstract and bibliographic record inspected.
- Published-record semantic search for eight-vertex nine-edge \(\mathcal C_{[4,6]}\)-saturated classifications.
- Fresh exact replay of the package C++ verifier over all \(\binom{28}{9}=6906900\) labeled graphs.
- Fresh auxiliary exact check that the seven-vertex minimum layer has one isomorphism class, so order eight is the first layer where equality structure branches.

Residual risks:
- The infinite saturation-number theorem is used as a published input; the equality classification itself is a finite exhaustive result.

## Originality — PASS

Best-of-knowledge originality passes. The primary 2026 paper establishes the saturation number \(\operatorname{sat}(n,\mathcal C_{[4,6]})\) but the accessible primary material does not state an eight-vertex six-class equality census. Exact semantic searches returned only the assigned classification. The full preprint was not accessible in this run, so no whole-document noncoverage claim is made and that source remains a residual risk.

### Equivalent formulations

Searches:
- Resultary query: C_[4,6] saturated graphs eight vertices nine edges six isomorphism classes
- Primary arXiv:2608.18551 abstract

Evidence:
- The assigned record is the only exact semantic hit.
- The primary abstract announces the saturation-number formula, not an isomorphism classification at \(n=8\).

Reasoning: Equivalent formulations are an equality-case census at \(n=8\) and the six orbits totaling \(100800\) labelings; no earlier equivalent record was found.

### Broader coverage

Searches:
- Liu--Wang--Gong 2026 saturation-number theorem

Evidence:
- The source is stronger in order range for the minimum edge count but does not, in accessible material, provide the complete equality structure at order eight.

Reasoning: Knowing the optimum edge count does not determine all extremal graphs.

### Exact database or table

Searches:
- Exact semantic search for 100800, six classes, and eight-vertex nine-edge saturation

Evidence:
- No independent census/table was located.

Reasoning: The package computation is a fresh exhaustive certificate of correctness, not itself novelty proof.

### Claim versus prior implication

Searches:
- Saturation-number theorem versus equality classification

Evidence:
- The prior theorem yields only that extremals have nine edges; it does not mechanically identify the six isomorphism classes.

Reasoning: A separate exhaustive equality analysis is necessary.

### Source inspections

- **Minimizing the number of edges in C_[4,6]-saturated graphs** — Establishes the nine-edge threshold at order eight but is not used to assert whole-document noncoverage of the six-class census. Material read: Primary abstract and bibliographic record; full preprint text was not retrievable in this run. Method: Primary-source abstract inspection after open-access lookup. Evidence: The abstract states the closed saturation-number formula for \(r=6\).

Checked sources:
- Liu--Wang--Gong, Minimizing the number of edges in \(\mathcal C_{[4,6]}\)-saturated graphs, arXiv:2608.18551 (2026), primary abstract and bibliographic record inspected.
- Published-record semantic search for eight-vertex nine-edge \(\mathcal C_{[4,6]}\)-saturated classifications.
- Fresh exact replay of the package C++ verifier over all \(\binom{28}{9}=6906900\) labeled graphs.
- Fresh auxiliary exact check that the seven-vertex minimum layer has one isomorphism class, so order eight is the first layer where equality structure branches.

Residual risks:
- The inaccessible full preprint could contain small-order equality examples or appendices; no such coverage was established from accessible material.

## Scientific value — PASS

This is a natural equality-case classification attached to a newly determined saturation number. A fresh auxiliary check shows the seven-vertex minimum layer has a single isomorphism class, whereas order eight is the first layer where the equality structure branches into multiple types. The complete six-orbit census, automorphism data, and reproducible exhaustive certificate therefore provide a meaningful finite structural benchmark rather than an arbitrary isolated count.

Checked sources:
- Liu--Wang--Gong, Minimizing the number of edges in \(\mathcal C_{[4,6]}\)-saturated graphs, arXiv:2608.18551 (2026), primary abstract and bibliographic record inspected.
- Published-record semantic search for eight-vertex nine-edge \(\mathcal C_{[4,6]}\)-saturated classifications.
- Fresh exact replay of the package C++ verifier over all \(\binom{28}{9}=6906900\) labeled graphs.
- Fresh auxiliary exact check that the seven-vertex minimum layer has one isomorphism class, so order eight is the first layer where equality structure branches.

Residual risks:
- No classification for larger orders is claimed.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
