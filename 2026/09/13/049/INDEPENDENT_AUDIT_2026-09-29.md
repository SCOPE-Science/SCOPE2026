# Independent audit — 2026-09-29

Record: `2026/09/13/049`  
Audited source tree: `d128944c0912777f66a884647cffe843cedd10b5`  
Disposition: **passed**

## Correctness

The reference-flow conclusion is correct. For constant real t, both J_t and theta_0 are left-invariant, so left translations act transitively by pseudohermitian automorphisms. Webster scalar curvature is therefore constant on each Rossi sphere. The fixed volume form theta_0 wedge d theta_0 makes the unit-volume rescaling t-independent. In the normalized CR Yamabe flow, constant Webster curvature gives zero velocity, so u=1 is an exact stationary solution; standard uniqueness identifies it with the reference flow. The coframe identity d theta_0=i(1-t^2) theta_t^1 wedge theta_t^bar1 gives strict pseudoconvexity on |t|<=1/4.

## Originality

The homogeneous Rossi geometry and constant Webster-curvature formulas are established in the literature. Once those facts are combined with the normalized-flow equation, stationarity of the fixed reference contact form is immediate. Thus the record is best classified as a useful target-specific corollary/clarification, not as an original CR-flow mechanism. The 2026 bubbling result for other initial data has different quantifiers and does not contradict the reference-flow statement.

## Scientific value

The result cleanly separates the behavior of the homogeneous reference form from known non-convergent flows starting from other data on small Rossi deformations. Its value is conceptual and diagnostic rather than technical novelty.

## Limitations

- The conclusion is only for the fixed homogeneous reference initial data, not arbitrary initial contact forms.
- The argument depends on standard existence/uniqueness for the normalized CR Yamabe flow.
- The repository text names output/artifacts/verify_coframe.py and output/artifacts/uniform_bounds.py, while the audited tree stores both under artifacts/; this is a packaging-path defect only.
- The originality axis is intentionally downgraded because homogeneous Rossi curvature is prior literature.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/13/049
- https://doi.org/10.4171/RMI/1491
- https://arxiv.org/abs/2309.02278
- https://arxiv.org/abs/2606.27164
