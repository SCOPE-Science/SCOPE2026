---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The centered process is a linear filter of telegraph noise plus independent Gaussian thermal noise. Work random part equals −ω∫gσ−√(2D)∫g dB; Gaussian term has vanishing fourth cumulant. For s1<s2<s3<s4 the stationary telegraph fourth joint cumulant is exactly −2 exp{−γ[(s3−s1)+(s4−s2)]}, verified independently from all three pairings. Integrating it gives −48ω⁴ times an ordered positive-kernel integral. Nontrivial monotone finite-variation λ makes g nonzero and one-signed, proving strict negativity. For optimal initial/final jumps and linear interior, g=c(2e^(ks) for s<0,1 for 0≤s≤T); the A,B,C,J cascade has C→1/(2γ³), J=T/(2γ³)+O(1). Combined with Q=2T/γ+O(1), this yields the stated kurtosis coefficient after c cancels. For cyclic ±a jumps at separation δ, k→∞ gives 4(1−e^(−γδ))(3e^(−γδ)−1) by exact two-state parity, so short δ yields positive sign for sufficiently large finite k. Independently checked four-time cumulants, pulse-sign formula and Gaussian cancellation; inspected original standalone checker’s independent Markov moment recursion.

## originality

PASS

The primary active-particle work paper gives this exact model, known optimum and second-order variance (prior work), explicitly notes non-Gaussian fluctuations, but its relevant derivations do not present a universal monotone-protocol fourth-cumulant sign theorem or the order-1/T coefficient and reversal counterexample. The telegraph fourth-correlation identity is standard; its work-protocol consequences constitute the assessed contribution.

## value

PASS

A strict fourth-cumulant sign law for all monotone drive protocols, sharp contrast with cyclic reversal and Gaussian propulsion, and a concrete long-time coefficient resolve a motivated non-Gaussian work-fluctuation question beyond the known optimum/variance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
