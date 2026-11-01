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

# Reproducible verification and limits

Run `python verify_random_w.py` with a Python installation of SymPy. The program works in exact rational algebra on the two independent symbols `a` and `p`; it checks the Markov row sums, stationary vector, projector identity, unique critical parameter, and nilpotent two-step relation. It also checks images of each affine branch at six distinct rational choices of `a`, and stationary/projector identities at four rational choices of `p` for each, for 24 rational parameter cases. The exact symbolic checks, not the finite table, support the real-parameter algebra; the main proof supplies the Markov coding and infinite-tail independence arguments. The checker does not establish novelty, uniqueness of all full-state stationary measures, or a rigorous computer-assisted global dynamical certificate.

The exact identity `P**2 - Pi - r*(P-Pi) = 0` is checked entrywise as a symbolic rational-function equality. At `p=(a-1)/a`, the program confirms `P**2=Pi` but `P!=Pi`. No independent audit has been undertaken.
