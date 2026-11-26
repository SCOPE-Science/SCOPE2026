# Independent mathematical audit

## correctness

PASS

Strict convexity gives u/x=-I1/(I2+r I0), with Ij the discounted moments on [0,h]. The sample multiplier is always less than 1, and exceeds -1 exactly when r/h² exceeds the normalized moment (I1 h/2−I2)/(I0 h²). Setting z=ρh gives ψ. At zero discount the multiplier lies in (−1/2,1). For positive z the derivative has sign K: its factorial-scaled coefficients vanish through degree 4, are positive in degrees 5–15, and are strictly negative for degrees ≥16 by the closed coefficient formula. Hence K/z^15 strictly decreases, starting positive and becoming negative by z=8. The limits −1/12 and 0 from above give a single positive maximum and exactly two neutral rates above the sampling threshold. For fixed positive ρ, F=2(1−e^(−z))z²ψ has F''=z(z−1)e^(−z), hence one positive zero; beyond it the numerator of (F/(1−e^(−z)))' is positive and increasing. This gives the unique crossing of φ=rρ². Independently derived moment and series checks and recomputed the constants (z†=7.66360518354401985…, H*=5.63013461640019324…) and both rate roots for h=6, r=1 via /workspace/branches/replay_1.py. Decimals are approximations and not interval-arithmetic certificates. The result is for repeated exact one-hold optimizers without terminal terms; it makes no general MPC stability claim.

## originality

PASS

The established exact stage-cost construction is not new. The distinct contribution supported by the inspected evidence is the globally unimodal scalar stability discriminant, sharp normalized barrier, and resulting exact discount and sampling slices. No comparison identified a matching or stronger theorem for that phase diagram. This is a bounded best-of-knowledge assessment, not a priority certificate.

## value

PASS

A minimal exact sampled optimal-control model isolates a real qualitative effect of within-hold discounting: stronger discounting can both destroy and restore stability even with no cost-integration error. The peak gives an exact all-discount design guarantee and explains why fixing the discount instead yields a single sampling frontier. This is a substantive sharp stability classification within the stated one-step scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
