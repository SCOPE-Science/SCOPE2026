# Independent mathematical audit

## correctness

PASS

For normalized nonorthogonal columns a1,a2 with r=a1·a2≠0 and fixed iid sampling p∈(0,1), each exact coordinate step projects the error residual orthogonally to one column. Repetition retains squared error; switching multiplies by r². The post-step indexed expectation vector u_{k,i}=E[f_k 1(J_{k-1}=i)] therefore obeys exact positive matrix T=[[p,p r²],[(1-p)r²,1-p]]. Its Perron root is λ+=(1+sqrt((2p-1)²+4p(1-p)r⁴))/2; strict positivity and nonzero initial expected error imply F_{k+1}/F_k→λ+ for every nonoptimal deterministic start. Exact restricted curvature after previous coordinate i is ξ1=(1-p)(1-r²), ξ2=p(1-r²); mean ξbar=2p(1-p)(1-r²), giving F_{k+1}=ρav F_k-Cov(ξprev,f_k). Let t=4p(1-p),v=r²: 2(λ+-ρav)=sqrt(1-t+tv²)-(1-t+tv). Its squared positive-quantity difference is t(1-t)(1-v)²; gap is strictly positive iff p≠1/2, otherwise zero at all k. For fixed t derivative in v is nonpositive; v→0 gives (sqrt(1-t)-(1-t))/2<=1/8, equality limiting at p=1/4 or3/4. For admissible r≠0 the supremum is unattained. Independent exact rational two-column projections and spectral identities passed; finite runs only corroborate universal Perron/algebraic proof.

## originality

PASS

Xie–Yang (2026) define the restricted-subspace curvature and establish a refined convergence bound conditioned on nonnegative covariance; their numeric sample covariances for selected higher-dimensional cases do not establish biased two-column asymptotic negative population covariance, nor its sharp 1/8 rate gap. Earlier classical coordinate-descent bounds and the published uniform two-coordinate delayed Gauss–Seidel recurrence concern different assumptions or quantities. Perron theory and elementary projections are prior ingredients. The nonnegative-covariance assumption is not contradicted; this result quantifies an exact regime where it fails.

## value

PASS

Provides a complete sharp 2-coordinate applicability boundary for a recent conditional refined rate estimate: bias in either direction makes the population covariance eventually negative even when the two columns are arbitrarily close to orthogonal; the optimistic average-curvature factor can be wrong by nearly an exact 1/8. The precise continuous extremum and every-p result are useful for interpreting when sampling-based curvature averaging is unjustified. This is not a routine numerical counterexample or claim of general optimizer slowdown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
