---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The case split is exhaustive and direct from the defining prime-power divisibility. For odd positive \(\mu\), \(n=2\) works. For even non-powers of two, writing \(\mu=2^v m\) with odd \(m\ge3\), the choice \(n=2^{v+1}\) satisfies the sole prime-power condition and is at most \(\mu\). For \(\mu=2^v\) with composite successor, any prime divisor of \(\mu+1\) is a witness not exceeding \(\mu\). If \(2^v+1\) is prime, the standard factorization of \(x^t+1\) for odd \(t>1\) forces \(v\) itself to be a power of two. The explicit factorizations \(145=5\cdot29\) and \(627=3\cdot11\cdot19\) satisfy all required divisibilities for \(\mu=256\) and \(65536\), respectively.

## originality

PASS

The primary paper poses the exact small-witness conjecture for all nonexceptional integers and does not give the positive-parameter Fermat-prime reduction. Targeted Resultary searches found the audited result itself and a later distinct classification of large low-prime-factor witnesses, but no prior result implying this positive reduction. The proof genuinely collapses the whole positive parameter range to hypothetical new Fermat-prime shells and separately disposes of the two nonexcluded known shells.

## value

PASS

The theorem meaningfully compresses an explicit infinite existence conjecture on all positive parameters to an exceptionally sparse classical obstruction, while disposing of every currently known nonexcluded Fermat-prime shell. This is a motivated structural reduction of the conjecture, not an arbitrary parameter scan.

The dated certificate retains the supplied scientific assessment, sources and limitations.
