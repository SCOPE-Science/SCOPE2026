---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For oriented edges of Q_d and D incidence, projector Π=D(D^T D)^+D^T, heat-kernel representation ∫D H_t D^Tdt yields same-coordinate nonnegative row mass 1 and different-coordinate absolute row mass 1/2; thus intact norm (d+1)/2. Removing nonbridge h gives exact rank-one projector update Π'(f,g)=Π(f,g)+Π(f,h)Π(h,g)/(1-Π(h,h)); denominator >0 because cube remains connected. For parallel edge e one transverse Hamming step away, heat-integral identities give q_d=(2^d-1)/(d 2^(d-1)), a_d=(2^d-d-1)/(d(d-1)2^(d-1)), α=a_d/(1-q_d)>0; sign pattern makes damaged row masses 1 own-direction, (1-α)/2 in one transverse direction and (1+α)/2 in d-2 remaining directions. Summation proves R_d=(d+1)/2+(d-3)α/2 for all d>=2, > intact for every d>=4, and d(R_d-(d+1)/2)→1. Independently built exact rational Walsh eigencharacter projection and all deleted row sums in d=2,3,4, obtaining entire histograms d2: norm1 all3 rows, d3: max2 and counts 2×2,9/5×1,15/8×4,39/20×4; d4: max133/51, norming exactly 3 edges at transverse Hamming distance one; other row sums 125/51×3,41/17×1,22/9×6,42/17×12,127/51×6. Each row signed vector reaches row norm. Global sharp norm for d>=5 is expressly unclaimed; analytic row bound rather than finite extrapolation proves all d>=4.

## originality

PASS

Best-of-knowledge PASS for exact one-edge deletion sharp threshold (dimension four), dimension-four global norm 133/51, and all-dimensional specific row formula. Jiang–Lim–Yao–Ye give Hodge least-squares edge-flow projection framework; Burton–Pemantle develop transfer-impedance/Green's function methods, while Schild–Rao–Srivastava and Gurel-Gurevich et al. establish general localization bounds; none inspected states a single-edge-outage hypercube worst-row norm or dimension threshold. Methods are not claimed new. Residual risk earlier effective-resistance cube calculations imply exact formula after an unrecognized reduction.

## value

PASS

Least-squares edge-gradient reconstruction and max-coordinate perturbation amplification are natural numerical conditioning metrics for incomplete pairwise differences. Demonstrating that removing ONE redundant measurement strictly worsens worst-case sensitivity exactly from d=4 is a motivated sharp counterexample to naive robustness; the exact dimension-four optimum and all-d row lower bound are useful without solving global d>=5 norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
