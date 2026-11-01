# Scientific review: Lucas-number seam response

## Correctness — PASS

For every integer \(n\ge3\), the fixed-point classification follows from the forced propagation of an oppositely colored rung, with the Möbius seam providing the only obstruction. The remaining common-rung states correspond exactly to singleton-free cyclic words counted by a four-state integer transfer matrix. The temporal double-cover lemma is a genuine bijection between two-step-returning states and fixed colorings on the cover; the specific cover isomorphisms are explicitly supplied for both parity classes. A bounded integer energy gives the period-at-most-two restriction without assuming any finite experiment proves an infinite statement. Lucas identities yield the signed seam discrepancy. A standard-library verifier independently checks the update dynamics, graph-cover isomorphisms, and number-theoretic identities; all checks passed. Residual risk: a subtle convention mismatch could invalidate a comparison, so the graph edges, spin update, labels, and orbit equivalence relation are fixed explicitly in the proof.

## Originality — PASS (qualified)

The relevant primary papers on synchronous majority dynamics establish period-two convergence and related stability or information-retention results rather than this census. The 1991 one-dimensional fixed-point paper treats different neighborhoods, and the closest available Möbius-ladder enumeration abstract does not identify these temporal-majority counts. Prior exact counts for open ladders and leaf-decorated cycles do not imply either the two seam-specific cover identifications or the signed residue-class response, even though the singleton-free transfer count is a shared combinatorial ingredient. Targeted searches for Möbius/untwisted majority cycles, Lucas-number differences, equivalent fixed-point formulations, and published research records found no decisive covering statement. The Möbius enumeration article was not obtainable in full, so possible coverage in an uninspected section remains a specific risk; novelty is not claimed as certified or exhaustive.

## Mathematical value — PASS

The problem compares two canonical cubic, locally identical graph families differing by a single global seam identification. It determines their entire finite recurrent-orbit censuses and exposes a nontrivial sign reversal in the oscillatory-orbit advantage at exactly two residue classes modulo six. The absolute seam effect grows like a Lucas number while the bulk orbit population grows like its square, a natural boundary-versus-bulk distinction. This is a structural, graph-topology-sensitive exact invariant rather than an arbitrary small-parameter recomputation. No claim of a broader graph classification is made.

## Sources and limitations

Tamuz--Tessler (arXiv:1307.4035, Sections 1.1, 3.1, 3.4) and Benjamini et al. (arXiv:1405.2486, Introduction and Sections 2--3) were inspected in available full-text HTML. Agur's 1991 abstract concerns one-dimensional periodic majority rules. McSorley's 1998 Möbius-ladder counting paper could only be inspected through repository metadata and abstract; a complete substantive comparison remains open. The output neither enumerates nonperiodic basin sizes nor claims an independent audit.

Self-review: passed. Independent audit: not yet performed.
