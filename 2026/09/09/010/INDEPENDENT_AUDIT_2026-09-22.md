# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/09/010`  
**Audited source tree:** `0ff4c8a4b5f3bb6421700d79b2b529822a5bcd03`  
**Date:** 2026-09-26 UTC  
**Disposition:** PASSED

## Correctness

PASS. An independent 128-subset BFS gives ordinary reset distance 36 for C7, no careful singleton reachable in any of its 14 one-hole mutants, and all 98 ordinary fill distances exactly as committed (including nonsynchronizing cells). The trap sets Q, F={0,…,5}, G={1,…,6} explain the negative careful verdict. In the a-hole-at-6 case, a at Q is forbidden rather than a Q loop; this wording error does not affect the trap conclusion.

## Originality

PASS, finite scope. Vorel and Cambie–de Bondt–Don study careful thresholds, complexity and extremal families; their results do not furnish this complete 14-mutant C7 and 98-fill map. The C7 baseline and semantics are prior art; the exact local stability chart is the contribution.

## Scientific value

PASS, modest. Uniform loss of careful synchronizability after one deletion is a concrete local fragility result, and the fill table gives a reproducible 98-cell benchmark. It supplies no careful-versus-ordinary finite gap witness.

## Prior work

- https://arxiv.org/abs/1403.3972
- https://arxiv.org/abs/2108.13927

## Scope

The pass applies to the stated finite record. Limitations and prior overlap above are part of the verdict; no limiting, general-family, or inaccessible-full-text claim is inferred.
