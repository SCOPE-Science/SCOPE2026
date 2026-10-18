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

# Mathematical verification

The proof in `RESULT.md` derives the exact Fourier transfer rule and its singular-value consequences without computer assistance. The critical independence mechanism is the exact equality of integer frequency lattices under commuting unimodular twists. The explicit family is checked algebraically using \(R^2=2I\), \(\det U=-1\), and \(U=I+R\).

Execute `python check.py` using a standard Python 3 interpreter. The program checks the integral matrix formulas and membership in the predicted even/odd image lattices for eleven values of the twist exponent, thirteen iterate lengths, and a symmetric integer-frequency grid. It also checks that 48 nonconstant output Fourier labels at each tested parameter pair map to distinct input labels. The exact-integer program reports 51,623 lattice checks.

The infinite Hilbert-space compactness argument, exact Schatten threshold and asymptotic constants follow analytically from the orthogonal Fourier decomposition and lattice-sum convergence. The finite tests are consistency checks, not a proof of the unrestricted quantifiers. The originality analysis has a documented inaccessible-full-text risk, and no independent scientific audit has been performed.
