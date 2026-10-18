---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For scalar A=e1 and Gaussian sketch rows, W=chi-square_l/l has density proportional to w^{l/2-1}e^{-lw/2}. Since M(w)=1-eta/w behaves as -eta/w near zero, E|M(W)|^r is finite if and only if r<l/2, including strict boundary divergence. Conditioning on the finite run partition of k iterations gives independent blocks with exponent q*r_i. The all-retention event has positive probability (1-p)^{k-1} for every 0<p<1, yielding cutoff l>2qk, while p=1 gives cutoff l>2q; deterministic B-block refresh gives l>2q min(B,k). Independent symbolic inverse-chi-square moments at eta=(l-4)/l give E M^2=2/(l-2), so i.i.d. second moment is its kth power; l=6,k=2 retained block demands fourth inverse moment and diverges. The state-independent positive-probability reset chain is ergodic with chi-square invariant law; integrable logarithm plus Jensen yields the same strictly negative a.s. exponent for all p>0 and periodic schemes. This is an exact analytical proof, not inference from a finite check.

## originality

PASS

PASS best of knowledge: the i.i.d. fresh-sketch mean-square formula and optimal step belong to Lacotte–Pilanci 2019/2021 and are explicitly excluded from novelty. Their full Section 4 Theorem 4.1 requires i.i.d. sketches; it does not imply the all-retention rare-event heavy-tail cutoff for a Bernoulli-persistent sketch, the p-independent almost-sure exponent, or the bounded reuse threshold. Conditional fixed-sketch high-probability arguments are different from unconditional moments over shared inverse chi-square multipliers.

## value

PASS

Sketch reuse is a natural practical performance choice. The sharp threshold says that even a tiny chance of keeping a bad inverse sketch for a long run eventually destroys finite expected error moments, while typical sample paths contract at unchanged exponential rate. The deterministic refresh-cap B offers a mathematically precise safeguard. This sharp moment-versus-a.s. distinction is a motivated structural boundary even in the deliberately simple rank-one setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
