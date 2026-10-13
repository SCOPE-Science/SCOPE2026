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
# Verification

The proof was checked symbolically in the following chain.

1. For a prime \(p\mid h\), if \(v_p(x_0)<v_p(h)\), then \(v_0\equiv0\pmod p\) and \(u_0\not\equiv0\pmod p\); after one step the projective ratio is \(\infty\) and no later \(u_n\) is divisible by \(p\).
2. If \(v_p(x_0)>v_p(h)\), then the initial ratio is \(0\), but this only affects \(u_0\); the first counted obstruction uses \(u_n\) with \(n\ge1\). The next ratio is \(\infty\), so again there is no counted failure from \(p\).
3. If \(v_p(x_0)=v_p(h)=\alpha\), then the reduced ratio modulo \(p\) is \((x_0/p^\alpha)(h/p^\alpha)^{-1}\), giving the stated class modulo \(p^{\alpha+1}\).
4. The reduced ratio evolves by \(t\mapsto t+t^{-1}\) until a hit of \(0\); after a hit, it moves to \(\infty\), so first-hit sets are disjoint.
5. The cited square criterion converts a hit at time \(r\) into a failed term at index \(r+1\).
6. The Chinese remainder theorem combines the local states, and grouping by distinct finite hit times gives the number of failed terms.

The included `verify.py` implements both the theorem prediction and the original exact integer recurrence. Replayed from the packaged file, it returns:

`VERIFY_OK exhaustive_h_le_60_states=16182 h65_counts=3507,714,4 modulus=4225 B5={2: [1, 4], 1: [2, 3]} B13={1: [5, 8]}`

The computation checks complete periods, not sampled starts, for \(h\le60\) and for the stated \(h=65\) example. It is corroboration only; no finite computation is treated as proof of the universal theorem. No independent audit has been performed.
