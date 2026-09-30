# Independent audit — 2026-09-29

Record: `2026/09/18/heisenberg-subalgebra-commutativity-degree--e3fb5b5762fa`  
Assigned and audited source tree: `83014e9f3c6d76b94078a7686d0c05253b2ffbe3`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The classification and counting argument is correct. A subalgebra either contains the one-dimensional center and is U⊕Z for an arbitrary U≤V, or misses the center and is the graph of a linear functional over a totally isotropic subspace. For two graph subalgebras Γ_f(U), Γ_g(W), with T=U∩W, direct calculation gives (A+B)∩Z=(f-g)(T)z; hence the pair is nonpermuting exactly when f and g agree on T and ω(U,W) is nonzero. The compatible functional count q^(r+s-t), Möbius-inversion formula for isotropic W disjoint from U/T, and the q^((r-t)(s-t)) lift count for W≤U^⊥ all check. A fresh exact evaluation reproduces the stated m=2 closed form and shows the q→∞ values trending to 0,0,5/9,1 for m=1,2,3,≥4. The archived verifier's exhaustive H_2(F_2) enumeration (158 Lie subalgebras and 6,000 nonpermuting ordered pairs) is also internally consistent with the formula.

## Originality

**qualified_with_inaccessible_group_prior**. Muhie–Otera–Russo introduced the Lie-algebra subalgebra commutativity degree in September 2026 and publicly advertise a Heisenberg study; the record correctly identifies their explicit three-dimensional case as prior. Shen–Voll's higher-Heisenberg work counts finite-index lattices over local rings, a different invariant. Targeted searches did not locate the present all-m finite-field formula or its 0,0,5/9,1 large-field transition. The 2009 Tărnăuceanu subgroup-commutativity paper is the main residual risk for the odd-prime extraspecial-group corollary: direct OA attempts did not yield full text and authorized institutional retrieval stopped at human verification, so this audit does not claim to have read it. Accordingly, originality is supported for the finite-field Lie-algebra formula and rank transition, while priority of the group-theoretic corollary remains deliberately qualified.

## Scientific value

**meaningful_exact_extension**. The result extends a newly introduced probabilistic lattice invariant from the first Heisenberg algebra to every symplectic rank, with an exact finite-sum formula and a nontrivial asymptotic phase transition. The formula also exposes the mechanism—competition between center-containing and isotropic-graph strata—behind the limiting values, so it is substantially more informative than a finite table of examples.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/heisenberg-subalgebra-commutativity-degree--e3fb5b5762fa
- https://arxiv.org/abs/2609.19086
- https://arxiv.org/abs/2605.23003
- https://arxiv.org/abs/2406.10064
- https://doi.org/10.1016/j.jalgebra.2009.02.010
- https://arxiv.org/abs/1312.0296

## Limitations

- The exact formula is expressed as finite Gaussian-binomial/isotropic-subspace sums rather than a single closed rational function for arbitrary m.
- The Lazard extraspecial-group corollary is stated only for odd primes and the class-<p setting.
- The full text of Tărnăuceanu (2009) could not be inspected because authorized retrieval required human verification; no claim is made about any theorem hidden there.
- The originality window is unusually narrow because the motivating Lie-algebra invariant was posted only in September 2026.
