# Independent mathematical audit — SCOPE-20260918-505b9a3beb70

Final disposition: **PASS**.

## Correctness
**PASS.** On a=0, H=cos x+cos y is conserved. Using the stated exact mechanical period T(h)=4K(sqrt(1-h^2/4)) and orbit average <cos y>=h/2 gives Delta z=bT(h)(1-h) with no approximation. Subtracting the zero-mean oscillatory part through the periodic circle cohomological equation yields the smooth annular change zeta=z-b psi and the exact linear flow with frequencies Omega(h) and b(1-h). Differentiating the integral representation gives strict positive-energy monotonicity, and its endpoint limits give the stated range. Dense irrational linear flows force any continuous first integral to be constant on irrational energy tori, and continuity extends this to rational tori, so it factors through H. The negative-energy symmetry and branch monodromy follow consistently. The package's numerical script is only a sanity check and is not needed for the proof.

## Originality
**PASS.** The Szumiński–Llibre primary abstract confirms local regular-domain integrability on a=0 but does not state the global rigid return map, exact rational/irrational torus classification, annular factorization of continuous first integrals, or branch monodromy conclusion. Searches found no separate source for those global statements. Full paper text was not obtainable during this audit, so the originality finding is explicitly best-of-knowledge rather than a whole-document noncoverage assertion.

### Equivalent formulations
These equivalent formulations were compared with the source abstract; none is stated there.

### Broader coverage
Local regular-domain integrability does not by itself state global single-valued integrability on a complete energy torus.

### Exact database or table
This check is secondary and is not used as novelty proof.

### Claim versus prior implication
No inspected stronger theorem mechanically supplies the global factorization statement.

## Value
**PASS.** The result resolves a natural global-versus-local integrability question for the exact invariant axis: it classifies every regular energy torus, gives a complete resonance spectrum on the positive branch, and explains why local branch first integrals do not globalize. These are structural dynamical statements, not merely a numerical special case.

## Source inspections
- **Trigonometric Nosé–Hoover oscillator: chaos, periodic orbits and integrability** (arXiv:2609.19958): primary abstract; direct full-text access and authorized retrieval attempts were unavailable Assessment: ABSTRACT_ONLY; establishes local-domain integrability context but is insufficient to decide hidden full-text overlap. Evidence: The abstract explicitly says two functionally independent first integrals are constructed on regular domains when a=0.

## Residual risks
- Because the full source paper could not be inspected, some exact ingredients or even part of the global interpretation may already appear there.
- The theorem is deliberately restricted to regular annuli and b nonzero; nothing here treats the separatrix or persistence for a nonzero.

The JSON companion records the structured four-part originality comparison and the same limitations.
