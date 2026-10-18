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

The proof reduces all possible squarefree indices to binary expansions with one or two nonzero digits and then applies a safe base-three residue filter. This is exhaustive because the identity \(\nu_2(Q_n)=s_2(n+1)-1\) is necessary. The parity-sensitive ternary criterion is independently established from \(\nu_3\); discarded residues have too many low ternary digits, so they cannot reenter at larger integer values.

Run `python3 verify.py` with standard Python 3. It compares the exact prime-product quotient against Legendre valuations for \(80\) small inputs and independently brute-forces all indices below \(2^{12}\). The full range check then enumerates all potential binary patterns through the stated cutoff, finds \(42\) ternary-eligible candidates, and evaluates valuations for all primes dividing any remaining quotient. It prints all \(35\) squarefree indices and seven explicit square-divisor witnesses. This passed when run from the supplied package.

The claim concerns exactly \(n<2^{16384}\). Computation is exhaustive within that bound and not evidence for the absence of additional squarefree values outside it. No independent mathematical audit has been performed.
