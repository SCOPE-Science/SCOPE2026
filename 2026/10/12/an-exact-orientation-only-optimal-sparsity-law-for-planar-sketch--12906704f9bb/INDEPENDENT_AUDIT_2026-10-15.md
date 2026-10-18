# Independent mathematical audit

## correctness

PASS

One-step error is e+ = (I−P_s)e with P_s=(As)(As)^T/||As||²; hence the largest uniform expected squared-error contraction is λmin(E P_s), sharp by choosing the min-eigenvector at step 1. Two orthogonal sketch-pairs (coordinates and dense signs) yield trace-one 2×2 average projectors. In singular coordinates their traceless vector squared norm equals r²/D[u²v²+(1−r²)(t−u²)²]; for κ>1, 0<r<1, unique maximum λmin occurs at t=u²=sin²2θ, independent of κ. Bernoulli occupancy p=2t/(1+t) follows by conditioning on nonempty support. Independently recomputed 2×2 matrices for θ=π/8,0.31,0.11 and κ=2,4.7,1.3; projector values matched formula and interior values beat both endpoints. At κ=1 all t tie, as explicitly excluded.

## originality

PASS

Gower–Richtárik establishes sharp contraction via expected projector and an SDP over generic discrete sampling, but its inspected Section 5.1 does not produce the exact closed-form minimax parameter for this conditioned Bernoulli-sign coordinate/full-support mixture. Recent sparse-sketch spectral bounds examine different families and typically provide estimates rather than the exact planar orientation-only optimum.

## value

PASS

A fully explicit sharp probability for balancing one-sparse and dense-sign sketches on the smallest nontrivial linear solver is a natural constrained design invariant; the unexpected dependence only on singular-vector angle and strict interior gain provide concrete benchmark information not mechanically available from a generic SDP statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
