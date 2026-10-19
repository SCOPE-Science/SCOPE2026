# Self-review

## Correctness — PASS
For a real planar SPD Hessian, the exact minimizer along a direction is an \(H\)-orthogonal rank-one complement projection after the \(H^{1/2}\) transform. Independent directions give a composition whose expected matrix is diagonal in the spectral basis. A Euclidean-orthogonal second direction gives a conditional overlap scalar. Exact Cauchy integrals and a displayed partial-fraction decomposition establish that the two expected matrices differ by the universal scalar \(\bigl((\kappa-1)/(\kappa+1)\bigr)^2\). The top eigenvalue yields sharp worst-case factors for all \(\kappa\ge1\). All boundary cases, including \(\kappa=1\), are explicit. Reproduced SymPy integrations and full-angle quadratures passed; finite checks are not substituted for proof.

## Originality — PASS with residual risk
Primary full text of Berglund–Khirirat–Wang (arXiv:2202.04612) presents general randomized subspace Newton updates and convergence, not the exact coupling law. The full text of Gower–Kovalev–Lieder–Richtárik (arXiv:1905.10874) provides the general sketch Newton framework but does not establish this conditional two-step planar identity. Kozak–Molinari–Rosasco–Tenorio–Villa (arXiv:2107.03941) uses Haar-orthogonal columns *within a single finite-difference gradient estimate*, not two sequential exact Hessian-line minimizations. Targeted mathematical-record searches did not identify a stronger statement implying this identity. Closest records on two-step steepest descent, Haar-moment subspace descent, and inverse-positive coordinate sampling have different updates or coupling. Unindexed equivalent classical random-pursuit identities are an acknowledged risk; absence in search is not proof of uniqueness.

## Mathematical value — PASS
Comparing two natural same-cost sketch sampling schemes with identical one-direction marginals is a motivated design question. The exact all-initial-error matrix identity gives a genuinely sharp planar coupling classification: it improves every nonzero error strictly at any nontrivial finite condition number and changes an isotropic two-step residual of \(1/4\) into exact termination. The result diagnoses the benefit of anti-correlated *sequential* directions, which is not implied by one-step sketch convergence rates or simultaneous-block orthogonality. The planar and exact-oracle restrictions limit external scope but do not make this structural comparison a routine sampling restatement.

## Closest literature and limitations
See the three arXiv sources identified above and Gower–Richtárik (arXiv:1506.03296, whose accessible abstract emphasizes iid per-iteration sketches). The latter's full text was not inspected here; generic sketch-and-project theory could contain an equivalent planar specialization. The empirical checks are finite, and no theorem beyond dimension two is claimed.

Self-review: passed. Independent audit: not yet performed.
