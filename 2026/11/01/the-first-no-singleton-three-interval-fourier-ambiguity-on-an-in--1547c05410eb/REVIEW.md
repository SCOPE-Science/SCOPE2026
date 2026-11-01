# Self-review

## Correctness — PASS

The definition of admissible masks is exhaustive: every three-run normalized binary indicator is a unique five-part positive composition with occupied lengths at least two and gaps at least one. Reversal is the only nontranslation geometric equivalence left after endpoint normalization. The Fourier modulus equals the sinc factor times a finite polynomial modulus; therefore continuous Fourier equality is exactly equality of all integer aperiodic autocorrelations. The maximum nonzero correlation lag determines the support length even when comparing different lengths. `CHECK.py` runs two independently structured enumerations over all valid five-part compositions for every length through nineteen, checks complete equality of their correlation fibers and two independent integer-correlation formulas, and proves the stated first collision and unique pair. The witness also has an exact polynomial-factor reversal certificate, independent of the census. No probabilistic sampling, floating-point arithmetic, or unbounded-computation assumption enters the proof. Independent auditing has not been performed.

## Originality — PASS relative to inspected literature

Xia–Xu, arXiv:2606.19855v1, is the closest published construction and general criterion. The article's explicit three-interval counterexample includes a single-unit occupied component, hence is outside the stated constrained class. Its factorization theorem is acknowledged as stronger *structural* knowledge about how ambiguities arise, but it does not state or calculate the sharp first threshold for at-least-two-unit three-run signals, nor the sole first ambiguity fiber. The wide-separation uniqueness theorem treats another regime. Willms (2013) develops run-structure autocorrelation theory, not the verified numerical threshold here. Searches of published mathematical records, mathematical-paper indexes, and accessible prior research claims did not uncover this exact threshold; absence of a database hit is not presented as novelty proof. A hidden earlier census or overlooked general theorem remains a genuine residual risk.

## Value — PASS

The first collision length is a natural resolution invariant for the simplest disconnected binary shapes after excluding isolated one-cell features. This is the smallest nontrivial minimum-feature-size constraint in a three-component 0–1 line model, motivated by phase retrieval of quantized multi-interval apertures. The complete first ambiguity fiber gives both a sharp impossibility boundary for single-magnitude reconstruction and a concrete witness against an overstrong uniqueness assumption. The exact finite census is the contribution; no sweeping stability or unbounded result is claimed.

## Closest sources and limits

Xia–Xu (2026), arXiv:2606.19855v1, §§4–6; Willms (2013), DOI:10.1109/TIT.2013.2259293. Classification applies only inside the prescribed unit-grid, exactly-three-run, no-singleton domain. Unindexed equivalences and independent replication remain outstanding.

Self-review: passed. Independent audit: not yet performed.
