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

# Reproducibility and verification limits

From the directory containing this file and `verify.py`, run:

```bash
python3 verify.py
```

Python 3's standard library is sufficient; no downloaded data, third-party numerical packages or external services are needed. The script forms both \(A(1\pm\delta)\) sampled matrices as exact rational-coefficient polynomials in \(\delta\), builds the three-moment map independently, and verifies the displayed transfer matrix and cubic characteristic-at-one identity as formal polynomial identities. It also checks nonsingularity of the switching commutator as a formal polynomial identity; checks the exact positive-definite Lyapunov certificate for \(\delta=2/5\); enumerates every length-\(0\) through length-\(6\) interval sequence for four rational jitter magnitudes and three rational initial states; and encloses the critical root with 100 steps of rational bisection. A successful run prints `PASS: 106 exact assertions / finite-path checks`.

The finite tests corroborate algebra; they do not prove a universal spectral statement. The global classification instead follows from the positive-definite eigenmatrix argument, order comparison, continuity of spectral radius and the cubic root-uniqueness proof in `RESULT.md`. None of the scripts claims to establish bibliographic novelty or independent validation. The exact scientific scope is sample-instant, noiseless mean-square stability; intersample estimates, non-iid intervals, other gains and almost-sure exponents are outside the verified theorem.
