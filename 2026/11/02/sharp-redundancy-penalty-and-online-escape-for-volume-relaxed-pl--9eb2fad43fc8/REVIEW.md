# Review of sharp volume-relaxed planar block projections

## Correctness — PASS
For every two-row block, the exact projector is the identity. The specific source relaxation gives scalar error multiplier \( -\sqrt{1-v/v_\star} \); averaging its square is exact. A doubled-angle chord representation and the parallelogram identity give the strict universal bound, and the explicit collapsing configuration proves sharpness for each row count. The exact geometric stopping-time law and online first-step behavior follow from whether the sampled pair has maximal volume. The standalone checker of rational identities is supplementary to the proof.

## Originality — PASS (with priority risk)
Entezari–Banerjee–Kalantari, arXiv:2610.12346v1, Theorem 2, **already gives the general volume-dependent factor** and suggests a running maximum; these are credited. The separate sharp \(M\)-row envelope, asymptotically extremizing geometry, expected first-hit maximum and fixed-versus-online behavior are not stated in its examined sections. Earlier related works arXiv:2111.06931v3 and arXiv:2503.09469v3 concern, respectively, unrelaxed volume sampling and different relaxation laws. Two related accessible prior results were compared at the statement level: a two-row *single-row* relaxation calculation and an unrelaxed volume-sampling spectral bound. Neither has the present two-row-block row-count envelope. Other relevant mathematical publications were also checked. A geometric identity might be known in stronger form, and an unlocated source may already apply it to this algorithm.

## Mathematical value — PASS
The theorem answers a sharp natural convergence-factor question in the fully informative block regime, gives explicit adversarial row families and a quadratic expected exact-hit penalty, and explains why using the empirically updated maximum is materially different from using a precomputed global maximum. No claims are made about larger ambient dimensions with undersized blocks, inconsistent data, or actual runtime performance in large applications. The outcome is not an independent external certification.

## Main sources and boundaries
- arXiv:2610.12346v1, Section 3.3 Theorem 2 and online normalization note: https://arxiv.org/html/2610.12346v1
- arXiv:2111.06931v3 and arXiv:2503.09469v3: predecessor algorithmic frameworks
- arXiv:2001.02745: familiar sphere distance-energy relations (abstract consulted)

Self-review: passed. Independent audit: not yet performed.
