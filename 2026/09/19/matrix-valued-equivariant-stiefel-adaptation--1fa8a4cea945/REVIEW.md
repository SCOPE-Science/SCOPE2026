# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The main claim is a commutant calculation. Writing a linear map on \(\mathbb R^{d\times r}\) column-by-column reduces ambient \(O(d)\)-equivariance to \(r^2\) endomorphisms of the standard \(O(d)\) representation. Each endomorphism commuting with every orthogonal matrix is scalar, so the full equivariant map is exactly right multiplication \(X\mapsto XB\). This immediately exposes the missing column multiplicity in the motivating paper's converse: among entrywise diagonal maps, \(B\) may be any diagonal \(r\times r\) matrix, not only a scalar multiple of the identity.

The adaptive covariance construction is checked algebraically. Under left rotations, \(\xi^\top\xi\) is invariant; under right frame rotations it transforms by conjugation. Spectral matrix functions therefore transform by the same conjugation, while the embedded Stiefel projector satisfies both \(\Pi_{QW}(QZ)=Q\Pi_W(Z)\) and \(\Pi_{WO}(ZO)=\Pi_W(Z)O\). Frobenius trust capping is invariant, and polar retraction is bi-equivariant under orthogonal left and right factors. These identities prove exact \(O(d)\times O(r)\) equivariance of the stateful covariance-preconditioned update, assuming its internal covariance/momentum states are transformed covariantly.

The scale-homogeneity statement is restricted to \(\varepsilon=0\) and positive-definite covariance, where \(M\mapsto cM\) and \(C\mapsto c^2C\) cancel exactly. The record explicitly does not claim that anisotropic preconditioning remains steepest descent in the fixed embedded metric. The narrower scalar uniqueness statement is separated accordingly.

A deterministic NumPy artifact verifies a non-collinear two-column covariance-normalized direction that still has exact left equivariance, and a random full-covariance trust-capped polar step with both left and right rotations. Residuals are at floating-point roundoff.

## Originality — PASS, to the best of our knowledge

The motivating preprint arXiv:2609.19363v1 was inspected beyond its abstract, especially its open-gap statement and Sections 5.2–5.3. It explicitly calls a single scalar second moment per frame the unique form compatible with ambient \(O(d)\)-equivariance, and its equivariance proposition argues that diagonal scaling commuting with all ambient rotations must be scalar. The commutant calculation above shows that this is not true for the stated action on a \(d\times r\) frame when \(r>1\): the representation contains \(r\) copies of the standard \(O(d)\) representation.

No novelty is claimed for the abstract commutant theorem, covariance preconditioning in general, or Riemannian adaptive optimization in general. Kasai–Jawanpuria–Mishra (ICML 2019) was inspected in its primary PMLR text, including the full left/right covariance construction and its tangent projection. It already provides matrix-valued adaptive weights on matrix manifolds, including Stiefel, and even notes that row-only or column-only adaptation is allowed. This substantially narrows any algorithmic novelty claim.

Kong–Wang–Tao (ICLR 2023; arXiv:2205.14173) was inspected in its full accessible text, including Section 2.3 and the Vision Transformer experiment. It derives an Adam-Stiefel optimizer with second moments and applies Stiefel constraints specifically to \(W_i^Q\) and \(W_i^K\), comparing Stiefel Adam and Stiefel SGD. This contradicts the motivating preprint's statement that the closest prior application of Riemannian methods to query/key projections used fixed-step Riemannian SGD.

Repository searches by arXiv identifier, scalar-second-moment terminology, Stiefel equivariance, and matrix covariance found no overlapping SCOPE record, and the latest repository changes were inspected directly. External searches by the exact source title, uniqueness wording, RASA/Kasai terminology, Stiefel Adam, covariance preconditioning, and equivariant optimizer terminology found no published correction of the 2026 uniqueness claim.

The novelty claim is therefore deliberately source-specific: the exact correction of arXiv:2609.19363v1's \(O(d)\)-equivariance uniqueness argument, the corrected commutant classification under that paper's stated group action, and the observation that a covariance state can retain even joint left/right orthogonal equivariance through the same tangent projection and polar retraction. The underlying representation-theoretic and adaptive-preconditioning ingredients are prior knowledge.

### Residual literature risk

Because the commutant calculation is standard representation theory, older equivariant-optimization or matrix-preconditioning literature may contain essentially the same classification in a different language. That would narrow the novelty of the abstract theorem but not the factual correction to a preprint first posted in September 2026. The motivating paper is extremely recent, so an author revision or contemporaneous commentary not yet indexed may already address the issue. No such correction was located in the sources inspected.

The ICML 2019 RASA paper's primary full text was inspected. The ICLR 2023 Stiefel-optimizer paper's accessible full text was also inspected. No inaccessible paper was found that gives concrete evidence against the correction; the main residual risk is unindexed contemporaneous discussion rather than a specific unavailable source.

## Value — PASS

The uniqueness claim appears in the motivating paper's stated open gap and is used to motivate its scalar second-moment design. Correcting it changes the design space materially: exact ambient coordinate-freeness leaves an entire positive-definite \(r\times r\) family of anisotropic preconditioners, and even diagonal adaptation can retain one scalar per column. The scalar method remains valid, but its justification should be tied to preserving the embedded-metric steepest direction rather than to equivariance alone.

The bi-equivariant formulation is particularly relevant to the same paper because it separately identifies a right \(O(r)\) attention gauge. A covariance tensor that transforms by conjugation can respect that gauge while retaining anisotropy, so imposing the additional right symmetry still does not force an adaptive state to be numerically scalar.

The prior-work correction is also substantive. RASA predates the proposed matrix-manifold adaptive-preconditioning idea, and the 2023 Momentum Stiefel Optimizer paper predates the claimed attention application by applying Stiefel Adam directly to Vision Transformer query/key matrices. These facts do not refute the new paper's experiments or its particular scalar/trust-capped optimizer, but they materially narrow its novelty narrative.

## Limitations checked

No convergence theorem or empirical advantage is established for the matrix-valued rule. Full covariance adaptation changes the fixed embedded metric's steepest direction, may require regularization when the covariance is singular, and costs more than a scalar second moment. Exact gradient-scale homogeneity requires \(\varepsilon=0\) (or a covariantly scaled regularizer) and positive-definite covariance. The right \(O(r)\) statement assumes optimizer states transform with the frame; it is a symmetry theorem, not a claim that arbitrary stored states can be reused after a gauge change without transformation. The correction applies to the v1 wording and proof of arXiv:2609.19363; later revisions may alter those claims.
