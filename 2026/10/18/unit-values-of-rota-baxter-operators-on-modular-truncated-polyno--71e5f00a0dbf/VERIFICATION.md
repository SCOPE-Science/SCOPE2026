---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

Run `python verify_rb.py` to reproduce the finite-field checks without third-party packages. The checker uses native modular arithmetic for prime fields and explicit irreducible quadratic polynomials for \(\mathbb F_4\) and \(\mathbb F_9\). It builds the operator by triangular expansion in the vectors \(t^ia^j\), projects onto \(k[a]\), and applies truncated integration, then verifies the Rota–Baxter identity on all ordered pairs of basis monomials. By bilinearity this verifies each tested operator on the entire finite algebra.

The program reports `VERIFICATION_OK 1204` after 1,204 constructed operators in 24 field/truncation configurations, with some large-value sets sampled to a stated cap of 300. It independently enumerates every linear map and checks the predicted **set of attainable unit values** in five exhaustive configurations: \((q,N)=(2,2),(2,3),(2,4),(3,2),(3,3)\). The respective counts of all valid operators are 2, 4, 24, 3, and 15; the numbers of distinct unit values are 2, 2, 4, 3, and 9.

The decisive universal verification is the proof: any \(P(1)\) satisfies the divided-power \(p\)-nilpotence relation, and for each nilpotent target \(a\) the projection–integration composition is an explicit witness. Nonzero leading-degree coefficients are inverted only where those coefficients are units; factorial denominators involved are at most \(p-1\) and therefore invertible. This accounts for every field of characteristic \(p\), not only tested finite fields. The coefficient-matrix formula also proves regular dependence on the reduced valuation strata.

No full enumeration of operators, their scheme components, their global moduli space or their total finite-field number is claimed. Finite experiments are not substitutes for the exact proof. Independent audit has not been performed.
