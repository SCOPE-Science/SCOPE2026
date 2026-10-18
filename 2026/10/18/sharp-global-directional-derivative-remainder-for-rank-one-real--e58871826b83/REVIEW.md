# Scientific review

## Correctness — PASS
The right derivative is the support function of the norming face of a rank-one trace-class operator. The contraction-completion lemma is proved by a genuine orthogonal Julia dilation, a planar rotation with explicit norm distance, and compression. Optimizing the resulting one-parameter quadratic gives an all-dimension upper bound. Rank-one perturbations attain both sharp branches; the scalar branch is checked separately. The proof handles arbitrary real Hilbert dimensions and the \(t=1,2\) boundary values. Exact rational witnesses and finite-dimensional checks are reproducible in `verify.py`; neither supplies the infinite-dimensional proof.

## Originality — PASS (best-knowledge, not a priority certificate)
The closest inspected full source is Dantas--Jung--Mazzitelli--Rodríguez, arXiv:2209.01767v1 (Theorem C(iii), Proposition 4.3, Section 4.2). It establishes the qualitative uniform strong subdifferentiability of Hilbert elementary projective tensors, but its statements and micro-transitivity proof do not give the exact all-scale remainder or the scalar/non-scalar transition. Search comparisons against nuclear-norm Taylor estimates, sharp fixed-vector contraction perturbations, and published tensor geometry revealed no directly matching theorem. A 2019 related local-property paper was accessible only by abstract, and literature not indexed under this terminology may contain equivalent estimates.

## Mathematical value — PASS
The motivating literature gives a qualitative uniform differentiability statement. This result gives its sharp global quantitative modulus, an explicit change of regime at \(t=2\), a complete scalar boundary case, and concrete extremizing rank-one perturbations. The dimension independence permits a uniform estimate in infinite-dimensional nuclear tensor settings, and the completed contraction lemma provides a reusable operator-geometric mechanism, not just a finite numerical observation.

## Remaining limitations
The theorem concerns real Hilbert trace-class tensor products only. Exact equivalence to any more general perturbation theorem outside inspected sources remains a residual bibliographic risk; independent audit is not available.

Self-review: passed. Independent audit: not yet performed.
