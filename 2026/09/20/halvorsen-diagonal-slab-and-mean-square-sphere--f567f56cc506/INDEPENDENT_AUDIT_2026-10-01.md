# Fresh mathematical audit — Exact diagonal balance and compact-recurrence bounds for the Halvorsen flow

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** Summing the three equations gives \(\dot S=-\sigma S-dQ\), and completing the square gives the exact mean-square balance. For \(\sigma=0\), boundedness makes \(S\) monotone and \(\int_0^\infty Q<\infty\); bounded polynomial dynamics makes \(Q\) uniformly continuous, so \(Q\to0\). A bounded complete orbit has the same limit at both time ends and monotonicity forces the zero orbit. For \(\sigma\ne0\), variation of constants gives \(v=dS/\sigma\le0\). Combining \(Q\ge S^2/3\) with the scalar equation yields a Riccati comparison excluding \(v<-3\) in the relevant time direction. Equality at the two slab boundaries forces the two diagonal equilibria. Averaging then gives the sharp second-moment interval.

Sources checked: RESULT.md at the assigned source tree; artifacts/verify_halvorsen_balance.py; Othman–Jalal 2025 primary article page/PDF preview.

Correctness risks: The theorem is conditional on bounded forward or bounded complete trajectories where stated; it does not establish global boundedness for every initial condition..

## Originality

**PASS.** The located Halvorsen literature emphasizes numerical chaos, control/synchronization, equilibrium stability, and local transcritical/Hopf bifurcation. No inspected source states the sharp global diagonal slab, universal mean-square sphere law, collapse of compact recurrence on \(\sigma=0\), or invariant-measure second-moment bounds.

### Equivalent formulations

Searches/sources: Published-record semantic search: Halvorsen exact diagonal balance slab invariant measures mean-square sphere; Othman–Jalal 2025 DOI 10.21271/ZJPAS.37.6.4; Sprott Halvorsen symmetric chaotic flow.

Evidence: The 2025 primary article describes local transcritical/Hopf bifurcations and periodic-orbit stability. The semantic archive search found the current record but no earlier equivalent global balance theorem.

The audited result concerns global bounded recurrence and invariant measures, not local bifurcation normal forms.

### Broader coverage

Searches/sources: Halvorsen dissipativity/control/synchronization literature cited in the record; Vaidyanathan–Azar 2016 qualitative study.

Evidence: Accessible descriptions of the broader qualitative studies do not state the exact slab/sphere identities or critical compact-recurrence collapse.

No inspected broad Halvorsen dynamics source was shown to imply all four exact consequences.

### Exact database or table

Searches/sources: Resultary exact/semantic search for Halvorsen diagonal balance and invariant measures.

Evidence: No prior exact theorem-record hit was found.

There is no relevant known-value table; the exact comparison is theorem-level.

### Claim versus prior implication

Searches/sources: Compare local transcritical surface \(a+b+c=0\) with global recurrence collapse; Compare generic dissipativity with sharp slab \(-3\le dS/\sigma\le0\).

Evidence: Local equilibrium bifurcation does not imply that every bounded complete trajectory collapses at the critical surface. Generic dissipativity does not imply the sharp slab or exact invariant-measure second moment.

The global consequences require the exact scalar balance plus monotonicity/Riccati arguments and are not routine corollaries of the located local literature.

### Source inspections

- **Hopf Bifurcation Analysis of the Halvorsen System** — RELATED_NOT_COVERING.
  Identifier: https://doi.org/10.21271/ZJPAS.37.6.4
  Trigger: Same four-parameter Halvorsen family and critical parameter surface.
  Material read: Article page, abstract, and accessible first-page/PDF preview; the PDF endpoint itself later returned an access error.
  Method: lawful open-access material
  Evidence: The accessible paper material is explicitly local: equilibrium stability, transcritical/Hopf bifurcation, direction and stability of bifurcating periodic orbits.
- **A Symmetric Chaotic Flow** — BACKGROUND.
  Identifier: https://sprott.physics.wisc.edu/chaos/symmetry.htm
  Trigger: Foundational standard Halvorsen flow.
  Material read: Public scientific web note and bibliographic descriptions.
  Method: lawful public source
  Evidence: It documents the chaotic flow and numerical behavior, not the exact invariant-measure/slab theorem.

Originality risks:
- The complete Vaidyanathan–Azar 2016 chapter was not available for inspection and remains the strongest plausible prior-coverage risk.
- Sprott's later books were not inspected in full.

## Scientific value

**PASS.** The theorem turns a simple but previously unexploited scalar balance into sharp global restrictions on every compact recurrent regime, including a complete critical-surface collapse and quantitative RMS collapse near that surface. These are natural dynamical invariants and boundaries, not merely numerical observations.

Value risks: The theorem does not prove existence of a compact attractor away from the stated boundedness hypotheses..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to the scientific result or slogan is proposed.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
