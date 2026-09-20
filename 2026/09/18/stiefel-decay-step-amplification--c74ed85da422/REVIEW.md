# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The main algebra starts only from the Stiefel tangent condition
\(W^T\Delta+\Delta^TW=0\), which cancels the cross term in
\((aW+\Delta)^T(aW+\Delta)\). This yields the exact Gram matrix, singular values, and full-rank statement. Positive homogeneity of the polar factor for \(a>0\) then gives the exact effective-step identity. The chordal-displacement formula follows from the trace of the polar factor; the only potentially delicate term is \(\operatorname{tr}(W^T\Delta H^{-1})\), which vanishes because the first factor is skew-symmetric and the second symmetric. The principal-angle result follows from an exact graph representation with \(aI+W^T\Delta\) invertible.

Potential failure modes were checked explicitly. The result does not apply to an unprojected ambient optimizer direction. The sign restriction \(a>0\) is necessary for the stated positive-homogeneity identity without a frame sign change. The small-step comparison is only an asymptotic statement with fixed tangent direction. The numerical artifact independently evaluates the exact identities on random instances and a deterministic monotonicity example; residuals are at floating-point roundoff scale.

## Originality

**PASS, to the best of our knowledge.** Classical Stiefel references already contain the underlying manifold geometry and polar/projection retractions, and those facts are not claimed as new. Guerrero (arXiv:2609.19363) explicitly states that Euclidean weight decay has zero Riemannian gradient on the Stiefel manifold and uses a trust-bounded polar update. Loshchilov--Hutter define decoupled Euclidean weight decay. GeometricOptimizers.jl likewise documents the intrinsic no-op and consequently leaves Stiefel/Grassmann parameters undecayed. Kohlberger's Spectral Compact Training applies ordinary optimizer updates followed by QR retraction, but its update is not a tangent-step theorem and no matching effective-step identity was found there.

The originality claim is restricted to the exact interaction between an AdamW-style radial term and a **tangent** task step when both are fused before one polar retraction: the identity \(\mathcal P(aW+\Delta)=\mathcal P(W+\Delta/a)\), its ordering distinction from separately retracted decay, the monotone exact displacement/conditioning consequences, and the use of the same tangent cancellation to remove any small-step requirement for pre-polar full rank. Searches using “Stiefel”, “AdamW”, “decoupled weight decay”, “polar retraction”, “effective step size”, and equivalent update forms did not locate a prior statement of this package.

The main residual originality risk is simultaneous or poorly indexed work prompted by the very recent Stiefel-attention literature. Software implementations may also contain the algebra implicitly without documenting it as a theorem. Accordingly, originality is not asserted beyond “to the best of our knowledge.”

## Value

**PASS.** The distinction is operationally meaningful. A developer can correctly conclude that intrinsic \(L^2\) decay is zero on Stiefel and still obtain a nonzero finite-step effect by mechanically inserting a standard AdamW shrinkage into the same ambient vector that is then retracted. The theorem identifies that effect exactly: it is learning-rate amplification, not intrinsic norm regularization. It also supplies exact diagnostics for singular values, condition number, frame movement, and principal-angle movement, clarifying what a trust cap controls and what it is not needed for.

## Limitations

The contribution is a local one-step structural theorem, not a convergence theorem for AdamW or Riemannian Adam. It assumes exact tangency at the current iterate, exact polar retraction, and \(1-\eta\lambda>0\). Floating-point projection errors can break exact cancellation. It does not claim that fused decay was used in the experiments of arXiv:2609.19363, nor does it infer empirical performance consequences. The unconditional full-rank property of tangent polar steps is a consequence of standard Stiefel algebra; novelty is not claimed for that identity in isolation.

## Sources inspected

- Guerrero, arXiv:2609.19363 (abstract and accessible HTML sections describing the Stiefel metric, tangent projection, polar retraction, trust-bounded update, and zero tangent gradient of weight decay).
- Loshchilov and Hutter, arXiv:1711.05101 / ICLR 2019.
- Absil and Malick, SIAM J. Optim. 22(1), 2012, DOI 10.1137/100802529.
- Edelman, Arias, and Smith, SIAM J. Matrix Anal. Appl. 20(2), 1998, DOI 10.1137/S0895479895290954.
- GeometricOptimizers.jl documentation, “Weight Decay on Manifolds.”
- Kohlberger, arXiv:2604.00733, and its public implementation description.

No highly relevant inaccessible source was identified whose title or available abstract specifically signals the fused tangent-decay identity. The residual risk is instead incompleteness of indexing and simultaneous work.
