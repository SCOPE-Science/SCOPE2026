# Independent scientific audit — SCOPE-20260917-b89d6d65a1a2

Audited at: 2026-10-01T06:12:13.318800Z

Disposition: **passed**

## Correctness — PASS

The source's printed condition is literally vacuous because for each input \(T\) one may take the existentially quantified \(S=\Phi(T)\). For the two-fold amplification \(\Phi(T)=U(T\oplus T)U^*\), the induced Calkin map is an injective unital *-homomorphism, so it preserves and reflects unitaries and preserves spectra. Its range commutes with the nontrivial Calkin projection induced by the first summand, while the Calkin class of the flip does not; therefore the range is proper. Under the standard target-surjectivity condition, the induced quotient map is surjective, and unitary preservation/reflection yields the stated Jordan *-automorphism argument. The Hamel-complement projection has quotient map equal to the identity and sends the compact ideal to zero, so the separate equality claim is also false.

## Originality — PASS

The primary v1 preprint was inspected at the displayed definition, theorem, and compact-ideal lemma. Older preserver literature explicitly uses the opposite target-surjectivity convention. No prior correction of this specific recent source or equivalent amplification counterexample was located.

### Equivalent formulations

The audited counterexample is the direct operator-algebraic realization of the discrepancy between the two quantified directions.

### Broader coverage

Prior general preserver theory explains the correct hypothesis but does not supply this source-specific correction/counterexample.

### Exact database or table

This is a theorem-correction problem, not a database/table lookup.

### Claim versus prior implication

The record supplies genuinely new counterexamples to a newly stated theorem rather than restating the older convention.

## Value — PASS

The record identifies a hypothesis that renders major conclusions false as written, gives a concrete counterexample, isolates the standard corrected hypothesis, repairs the central Kasparov-cycle implication, and identifies a second independent false equality. This is a mathematically substantive correction.

## Sources inspected

- Linear maps preserving Kasparov cycles and the characterization of induced automorphisms — https://arxiv.org/abs/2609.18619. COVERING_TARGET_STATEMENTS: The paper prints the source-to-target condition \(\varphi(T)-S\in K(E)\), uses it in Theorem 2.5, and Lemma 2.6 claims equality on compact operators.
- Linear maps preserving semi-Fredholm operators — https://users.fmf.uni-lj.si/semrl/preprints/mope.pdf. PRIOR_CONVENTION: The prior convention quantifies over the target operator and requires it to be compactly approximated by an image, the reverse of the 2026 source's displayed condition.

## Residual risks

- A later revision of the 2026 preprint may correct the displayed hypothesis or theorem statements.
- The audit addresses the literal v1 statements and does not claim to replace every spectral-preserver proof in that manuscript.

## Limitations

- The result concerns the literal v1 preprint and may be superseded by a revision.
- The repair is complete for the Kasparov-cycle theorem described in the record, not every spectral statement in the source.
