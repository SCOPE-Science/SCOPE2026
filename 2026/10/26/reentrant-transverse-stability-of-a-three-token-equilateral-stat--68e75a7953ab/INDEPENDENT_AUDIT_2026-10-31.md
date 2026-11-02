# Independent mathematical audit

## correctness

PASS

At the equilateral family the softmax weights are p=e^(3β/2)/(e^(3β/2)+2) on self and q=1/(e^(3β/2)+2) on neighbors. Radial pre-normalized factor 1-hK>0, K=1-3q. Direct differentiating tangential softmax gives δt_i=q(2+3β)/4 Σ_{j != i}(δ_i-δ_j); shape derivative L=1+3q(3β-2)/4 and neutral rotation eigenvalue 1. The double transverse multiplier λ=(1-hL)/(1-hK) satisfies |λ|<1 iff h S(β)<2, S=K+L=2+9(β-2)/[4(e^(3β/2)+2)]. S has one maximum because its derivative sign is 2+(4-3β/2)e^(3β/2), with exactly one zero >2. This proves the unique sharp h_c and two flip-neutral β boundaries for h_c<h<1, without asserting nonlinear bifurcation at λ=-1. Twelve direct finite-difference perturbations of the full 3-token normalized map agree with the double eigenvalue at six β values and two h values.

## originality

PASS

This is a sharp transverse Jacobian and reentrant sharpness classification for full (unmasked) repulsive softmax on a regular triangle. Altafini’s 2026 positive-dominant-value hypotheses exclude V=-I; Gao–Yang–Chen 2026 treats negative values and regular polygons but apparently uses diagonal-masked attention in the relevant model. A first-order reduction of full attention to masked attention with β-dependent effective residual step is possible at equilateral states, and could make part of this a corollary of an exact masked polygon multiplier theorem. Its primary full text could not be inspected, so the priority judgment is qualified rather than claiming a definitive separation. The additional unique-maximum/return-stability threshold is not stated in accessible material.

## value

PASS

An exact stability diagram for the first nontrivial regular triangle in normalized repulsive attention resolves which fixed step lengths admit instability at intermediate attention sharpness but recovery at high sharpness. The two-root transition and critical step distinguish self-attention scaling regimes. It is a mathematically motivated local stability boundary rather than an arbitrary three-point finite experiment; no nonlinear flip claims are used.

The dated certificate retains the supplied scientific assessment, sources and limitations.
