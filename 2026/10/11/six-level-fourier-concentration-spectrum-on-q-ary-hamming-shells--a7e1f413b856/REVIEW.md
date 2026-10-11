# Scientific review: low-degree Fourier sampling on Hamming shells

## Correctness — PASS

The claim is for all integers \(q\ge3\), \(n\ge4\), and \(2\le k\le n-2\), with ambient and shell probability normalizations distinguished. An orthonormal one-coordinate basis separates radial activity from \(q-2\) independent nonzero-label contrasts. Conditioning on the uniformly sampled shell makes every block explicit: the radial Johnson degrees contribute three levels, the one-contrast blocks two, and double contrasts one. Direct correlation computations give each level and its multiplicity; positivity follows from the interior-support assumption. The calculated rank agrees with an independently constructed and injectively parameterized nullspace \(R\mathcal H_{\le1}\). Exact integer matrix-polynomial and trace checks on four finite cases, plus nine numerical Gram checks, independently stress-test normalization and multiplicities. They are corroborative, not proofs of the all-parameter theorem.

## Originality — PASS, with residual risk

Filmus (arXiv:1406.0142v1) analyzes Boolean slices and thus has no nonzero-label contrast branches for \(q\ge3\). Vasil'eva (arXiv:1412.3622v1) gives radius/eigenvalue-dependent reconstruction of individual q-ary hypercube eigenspaces; it does not state the present six rational squared-singular-value branches for the simultaneous Fourier degrees zero, one and two, or the full multiplier kernel. The general q-ary Terwilliger-algebra decomposition of Levstein, Maldonado and Penazzi (DOI:10.1016/j.ejc.2004.08.005) supplies plausible stronger representation-theoretic machinery, but the available abstract does not contain the explicit result; its full text was not accessible in this examination. Statement- and parameter-oriented searches did not locate an equivalent exact formula. This is not a guarantee of priority: older association-scheme sources could implicitly or explicitly contain the same spectrum, and inaccessible material remains a real risk.

## Value — PASS

Exact recovery and stability of low-frequency information from a Hamming sphere are natural finite harmonic-analysis questions. The complete six-branch classification handles every nonbinary alphabet and every interior radius, distinguishes three geometric spectral mechanisms, identifies the entire unavoidable nullspace rather than merely proving singularity, and provides the exact best quotient conditioning. The rank formula is a uniform structural invariant even as the shell size changes, not an arbitrary finite table or a single-parameter computation. Higher-degree extensions and simplified arithmetic tightness classifications are not claimed.

## Closest sources and limitations

- Yuval Filmus, arXiv:1406.0142v1, full-text basis and Johnson-harmonic analysis of the Boolean slice.
- A. Yu. Vasil'eva, arXiv:1412.3622v1, full-text q-ary sphere reconstruction under additional conditions.
- F. Levstein, C. Maldonado and D. Penazzi, DOI:10.1016/j.ejc.2004.08.005, general q-ary Terwilliger algebra; only its abstract was accessible, so exact historical implication is unresolved.

Proof and normalization details appear in RESULT.md. The included finite checker does not establish an infinite-family theorem. Independent verification has not been performed.

Same-model review: passed. Independent audit: not yet performed.
