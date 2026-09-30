# Independent audit — 2026-09-29

Record: `2026/09/15/029`  
Audited source tree: `c3d53e8aaa522a5b1f68b916162ec04b71904427`  
Disposition: **passed**

## Correctness

The monomial-line classification checks directly. With lambda^(d-1)c=1, phi(z)=lambda z conjugates z^d to c z^d, so Prep(g_c)=lambda Prep(z^d); torsion gives the exact common-preperiodic dichotomy. Canonical-height conjugacy gives h_g(z)=h(z/lambda), and h(lambda)<=h(z)+h(z/lambda) with h(c)=(d-1)h(lambda) gives the stated sharp lower gap, attained at roots of unity. Iteration gives slope c^((d^n-1)/(d-1)), so Delta and every fiber power have the claimed density/preperiodicity dichotomy.

## Originality

The proof is an elementary monomial specialization of standard arithmetic dynamics and dynamical Bogomolov/preperiodic-variety ideas. A focused search did not establish that the exact packaged all-k statement is already printed, but absence from search is not evidence of priority.

## Scientific value

The record gives a complete and sharp model calculation—exact intersection cardinality off the torsion locus, a quantitative height gap, and all-k density—which is useful as a sanity check for broader relative Bogomolov formulations.

## Limitations

- Only the one-parameter monomial line is treated, not a general split family.
- The Green-current translation is cited rather than independently reproved analytically.
- The record's reproducibility text/metadata use output/artifacts paths although the archived files live under artifacts/; this packaging mismatch does not affect the deductive proof.
- No priority claim is inferred from literature-search non-detection.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/15/029
- https://arxiv.org/abs/0911.0918
- https://arxiv.org/abs/2212.13215
- https://doi.org/10.1215/00127094-2024-0041
- https://doi.org/10.4007/annals.2014.179.1.2
