# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The argument uses only the uniform theorem of Wang coordinatewise and elementary properties of norm quotients. If the reduced center-valued trace of a class vanishes, subtracting the coordinate center-valued traces changes the representative by a norm-null sequence and produces exact trace-zero representatives. Wang's theorem gives coordinate commutator factorizations with a dimension- and algebra-independent product bound; reciprocal rescaling balances the factors and makes both factor sequences uniformly bounded. The converse follows from traciality of the center-valued trace. The quotient-norm identity follows from contractivity of the trace projection and the explicit central representative. The trace-space description follows because every element differs from its center-valued trace by a single commutator.

The same proof works for norm ultraproduct ideals after replacing ordinary convergence by ultrafilter convergence. When the coordinates are factors, the scalar norm ultraproduct is canonically the scalar field, so the tracial state is unique.

## Originality

**PASS, to the best of our knowledge.** Wang's arXiv:2609.16932 proves the required uniform theorem for finite von Neumann algebras but does not state a reduced-product, ultraproduct, quotient, or corona consequence. Targeted searches for norm ultraproduct/reduced-product single-commutator criteria and trace-kernel characterizations did not locate the theorem above.

There is important prior overlap that limits the novelty claim. Hardy's pseudomatricial work already gives unique trace for matrix ultraproduct-type models and a self-commutator characterization for self-adjoint trace-zero elements. Thus neither unique trace in the matrix special case nor the self-adjoint statement is new. Bice--Farah studied traces on C*-ultrapowers and exhibited settings with extra traces, but does not supply this single-commutator kernel theorem. The new claim is restricted to the consequence enabled by the 2026 uniform finite-von-Neumann theorem: exact single additive commutators with a universal norm bound in operator-norm reduced products, together with the closed-linear quotient and trace-space descriptions.

A residual literature risk remains because older work on pseudocompact/pseudomatricial algebras and C*-ultraproduct traces is broad, and not every full text using alternative terminology was exhaustively checked. No source located in the targeted search stated the arbitrary finite-von-Neumann reduced-product theorem.

## Value

**PASS.** Single commutators are generally a nonlinear subset of a C*-algebra. Here they become exactly a closed linear kernel, and the quotient by the set of single commutators is identified isometrically with the reduced product of centers. The same statement classifies all tracial states. For norm ultraproducts of finite factors it gives the particularly sharp codimension-one formula
\[
\ker\tau_\omega=\{[b,c]:b,c\in\mathcal A_\omega\},
\]
with the same universal norm-product constant as the coordinate theorem. This transfers a very recent finite-von-Neumann result to C*-norm quotients that are not themselves covered by the von Neumann theorem.

## Limitations

The result is a structural corollary of a new uniform commutator theorem, not an independent replacement for that theorem. It does not address arbitrary C*-algebra ultraproducts, and it should not be conflated with tracial/2-norm ultraproducts. The optimal universal constant is not determined here.
