# Scientific review

## Correctness — PASS
The construction, independent block indicators and generalist indicator are fully specified. The variance identity follows by expanding covariances. The proof supplies strict derivative signs at two rational probes per scale for every integer \(k\ge2\), with explicit inequalities controlling the generalist covariance terms; continuity and polynomial analyticity produce separated strict extrema. Independent exact-integer calculation from `verify.py` confirms these signs for \(k=1,2,3\). The program's finite cases are corroborative rather than substitutes for the proof.

## Originality — PASS, with a literature-access risk
Eklöf–Tang–Allesina (2013) supply a broader probabilistic ecology setting for topological coextinctions. Jones–Zurell–Wiesner (2024) analytically characterize expected network robustness. Chabert-Liddell–Barbillon–Donnet (arXiv:2106.06348, 2021; Environmetrics 2022) derive expectations and variances for stochastic-block-network robustness and are the closest potentially stronger source, but only the abstract was accessible after attempts to retrieve the preprint and lawful open-access text. Their accessible statements do not assert arbitrarily many local variance maxima in **fixed, connected** ecological networks with uniform primary degree two. Neither formula availability nor failure to find matching words establishes originality by itself; the residual stronger-coverage risk is explicit. Searches of the research database for equivalents, aliases and stronger statements returned no direct covering claim.

## Value — PASS
A widespread modeling practice summarizes ecological fragility by expected secondary extinction. This theorem proves that, even when that expectation grows monotonically under a single homogeneous primary-extinction parameter, variance can exhibit an unbounded number of separated vulnerability windows. The network is genuinely connected and has no variation in primary species degree; thus the effect cannot be dismissed as merely adding disconnected ecosystems or varying primary exposure. This is a qualitative, nonroutine structural boundary rather than a small numerical improvement.

## Scope and limits
The model uses one-step, all-partners-lost secondary extinctions and independent primary species losses. The construction has exponentially separated consumer degree scales, grows very rapidly with the requested number of peaks, and places late peaks near near-total primary loss. No claim is made about realism in measured ecological networks, universal behavior, or exactly \(k\) total extrema.

Self-review: passed. Independent audit: not yet performed.
