# Scientific review: four-outcome intrinsic noise for two-band observables

## Correctness (C): PASS

The hypotheses fix the full spectrum \([-1,-a]\cup[a,1]\), \(0\le a<1\), at most four real outcomes in the spectral hull, and exact zeroth and first operator moments. For arbitrary *noncommuting* positive effects the key polynomial certificate is \(N+(T-\lambda_iI)(T-\lambda_{i+1}I)=\sum_j(\lambda_j-\lambda_i)(\lambda_j-\lambda_{i+1})P_j\succeq0\). Thus every adjacent support gap enforces the corresponding scalar interpolation-variance lower bound on the full spectral set. Continuous spectral hats attain the bound for each fixed support, proving noncommuting effects never improve it. The global four-node argument uses the strict inequality \(E(a)<(1-a)^2/4\), forcing one inner node inside each band; their outer midpoint variances force distances at least \(s_a\), and the inner spectral endpoint forces the sharp lower bound. Equality gives the unique outcome set. Endpoint \(a=0\) is included; degenerate \(a=1\) is deliberately excluded. The exact proof handles continuous spectrum without finite approximation.

Computational verification: 3,957 grouped deterministic cases passed in `check_quantization.py`, including 450 random noncommuting POVMs. Finite tests are corroborative only, not a proof or an independent audit.

## Originality (O): PASS, best-knowledge published-record assessment

The nearest operator moment paper is Curto et al. (publisher DOI 10.1007/s11785-024-01649-4), whose Section 5 treats atomic existence and exact moment obstructions but not a fixed-cardinality optimal norm discrepancy. Mädler–Schmüdgen (arXiv:2310.00957) prove a finite-dimensional matricial atomic representation theorem, not an exact four-outcome noise envelope on infinite-dimensional two-band spectra. Massar (arXiv:quant-ph/0703036) introduced the intrinsic-noise operator and its general positivity; Pietrzycki–Stochel (DOI 10.4153/S0008414X22000426) give its zero-noise spectrality characterization. Neither inspected argument contains an optimized two-band four-level bound. Ramezani-Kebrya et al. (arXiv:1908.06077) develop adjacent-level stochastic quantization and a distinct gradient-vector worst-case variance problem. The elementary rounding mechanism and positivity identity are acknowledged as established ingredients.

Published claim searches for *unbiased four-level stochastic rounding on two disconnected intervals*, *finite atomic operator first moment and minimal second-moment error*, and the exact algebraic \(\sqrt{1+3a^2}\) coefficient found no equivalent statement. The nearest accessible claim records concern Fisher-symmetric POVM outcome counts and fixed-probability variance ranges, neither of which bounds this operator moment error. A hidden general theorem in optimal unbiased level design remains a realistic originality risk; search silence is not proof of priority.

## Mathematical value (V): PASS

Finite-atomic exact matching of \((I,T,T^2)\) can fail on infinite spectra. The present theorem quantifies the smallest unavoidable operator-norm defect under an exact first-moment requirement with a natural gap-sensitive four-outcome configuration. It simultaneously gives the unique optimal spectrum of reported outcomes, the exact closed-form gap law, and a general no-noncommuting-advantage certificate. The optimum improves strictly on placing two outcomes at each spectral-band boundary. These are natural operator-moment and measurement-noise invariants, independent of spectral multiplicity, not a change of notation or an arbitrary parameter slice.

## Scope and residual risks

The literature comparison cannot establish absolute novelty. The operator model uses one real observable and restricts outcome values to its convex spectral hull. No broader multidimensional or unrestricted-outcome theorem is claimed. The effect operators need not be unique. Mathematical review has not been performed by an independent expert.

Self-review: passed. Independent audit: not yet performed.
