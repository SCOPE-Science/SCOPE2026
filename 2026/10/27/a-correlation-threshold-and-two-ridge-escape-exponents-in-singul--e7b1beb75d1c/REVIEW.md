# Independent mathematical audit

## correctness

PASS

Independently reduce the given 3-by-2 problem on each circle u²+v²=s. The angular minimum of (1+s)u²+2γuv is s λ₋(1+s), where λ₋(d)=(d−sqrt(d²+4γ²))/2. The reduced unregularized value is 1+[β−1−2γ²s/(1+s+sqrt((1+s)²+4γ²))]/(1+s). The term subtracted from β−1 is strictly less than γ² at finite s and tends to γ². Thus for K≥0 the infimum is 1, is not attained and ridge minimizers escape; for K<0 the profile has a compact sublevel below 1, confining all small-ridge minimizers. At infinity the excess over 1 is K/s+(γ²−K)/s²+O(s⁻³). Add εs; the trial radii and matching lower bounds confine ε^(1/2)s (K>0) or ε^(1/3)s (K=0) to compact positive intervals. The unique minimizers of the limiting profiles q+K/q and q+γ²/q² give exactly the asserted norm and value constants. On either escaping branch the optimal eigenvector has u/v=−2γ/(1+s+sqrt((1+s)²+4γ²))∼−γ/s, hence |v|∼sqrt(s) and uv→−γ for every global minimizer. The frozen square-completion proof is consistent with this separate reduction. CHECK.py was inspected, not executed: its symbolic identities and sampled BFGS diagnostics have different evidentiary scope; the conclusion about global minima follows analytically. Parameters γ and β are fixed and γ is strictly positive.

## originality

PASS

Prior work covers singular-penalty nonattainment and global solution methodology, and the familiar fourth-root balance is already implicit in augmenting a simpler uncoupled example. The positive-correlation attainment boundary and the sharp critical sixth-root escape for all global minimizers are not covered by the strongest inspected statements. This is a bounded priority assessment, not a claim that fractional-exponent perturbation theory is new.

## value

PASS

A minimal full-column-rank overdetermined benchmark separates boundedness, ordinary escape and critical escape for a genuinely singular regularizer. The sharp band boundary and differing constants can test global regularized solver behavior near nonattainment; the example also shows where a standard sufficient condition ceases to be informative. The value is this mechanism and benchmark, not a claim of general TLS rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
