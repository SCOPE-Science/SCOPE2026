# Scientific review

## Correctness — PASS

The homotopy concentration and exact Betti number are Theorem 4.1 of Adams--Shukla--Singh (arXiv:2212.05871v2, pp. 7--9). Their Lemma 3.1 identifies scale-two facets exactly as closed neighborhoods. For a nonidentity translation, the proof classifies every invariant simplex: none if translation weight exceeds \(2\), and precisely \(2^{n-1}\) reversed edges otherwise. The resulting signed Lefschetz traces and finite-group Fourier inversion yield the exact multiplicities. This is an all-size proof, not a finite-table extrapolation. The actual bundled checker reconstructs simplicial chains and characters in the stated ranges. Residual correctness dependence: accuracy of the cited published homotopy concentration theorem and standard Hopf/Lefschetz trace theory.

## Originality — PASS

The closest primary source Adams--Shukla--Singh fixes the homotopy type but leaves group actions untreated; homology rank alone does not fix a nontrivial elementary abelian-group character. Matsushita (arXiv:2511.12608v2, Introduction and Theorems 1.2/1.5) connects closed neighborhoods to independence complexes and graph fundamental groups but does not give these hypercube characters. The neighboring group-representation literature studies Vietoris--Rips complexes of cubes; its source and target complexes have different homological degrees. Searches for the exact Čech object, closed-neighborhood aliases, translation action, Walsh characters, and the explicit multiplicity expression found no stronger covering prior statement. Relevant prior same-object results at a different Čech scale were excluded by direct scale/degree comparison. Residual novelty risk: incomplete indexing or uninspected literature; no global novelty certification is claimed.

## Value — PASS

The natural translation symmetry is an invariant omitted by the foundational nonequivariant classification: the result tells which of the \(2^n\) one-dimensional characters occur, their exact multiplicities, the dimension of invariant cycles, and the onset of full character support at \(n=4\). This is an infinite-family representation refinement of a canonical topological filtration, with direct applicability to symmetry-aware calculations; neither total Betti numbers nor the competing Rips results imply the answer.

## Closest literature and scientific limits

The defining Čech result is arXiv:2212.05871 (first posted 2022-12-12), primary MSC \(55N31\). The later closed-neighborhood generalities are arXiv:2511.12608 (2025). Rational translation modules, not integral modules, the full cube automorphism-group decomposition, or other Čech scales, are claimed. Explicit signed-face computations are finite confirmations, not the general proof. Independent validation is not performed.

Same-model review: passed. Independent audit: not yet performed.
