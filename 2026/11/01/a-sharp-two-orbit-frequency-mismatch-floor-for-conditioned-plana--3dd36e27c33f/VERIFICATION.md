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
# Reproducibility and scope of verification

The universal theorem is verified analytically by integrating the signed angular-speed error on each transformed periodic Jordan curve. Crucial hypotheses are the common orientation sign, \(F(0)=0\), lower metric bound \(m>0\), differential upper bound \(M\), and primitive periods. Combining the two resulting frequency inequalities eliminates the unknown constant reference speed.

The standalone `verify.py` is runnable with an ordinary Python 3 standard library and uses exact rational arithmetic only. It executes 65 assertions: a sharp equality example, the reference-speed optimizer, 61 rational trial angular speeds, a distorted diagonal-map check, and orientation reversal. A successful run prints `PASS: 65 exact rational equality and inequality checks`. No computation is presented as an exhaustive verification of all smooth diffeomorphisms or trajectories.

The strict positive lower bound requires two different signed physical frequencies; equality of those frequencies makes the statement non-informative. The independent audit has not been performed.
