---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For n>=3 and 0<a,b, a!=b, Fourier eigenvalues of the biased ring generator have imaginary parts (a-b)sin(2pi k/n). The real circulant exponential P(t) is symmetric iff every sampling phase lies in pi Z. For n>=5 both sin(2pi/n),sin(4pi/n) are nonzero; their rational ratio forces 2cos(2pi/n) a rational algebraic integer, hence integer; 0<2cos<2 forces n=6. Direct sine sets for n=3,4,6 give precisely t=2m pi/(sqrt3|a-b|) for 3,6 and m pi/|a-b| for 4. At even m phases all +1 so P=e^{tQsym}; at odd m the first nontrivial Fourier eigenvalue is strictly negative, excluding an exponential of a reversible continuous-time generator. Sampled KL entropy zero iff P symmetric since P(t)>0. Independently computed numerical matrix exponentials and Fourier eigenvalues for the three resonant sizes (m=1,2), tested negative modes and even-m symmetric exponentials; exact algebraic-integer proof covers all n.

## originality

PASS

Best-of-knowledge originality after direct claim/implication comparison with published same-object and general methods. Known ingredients, exact overlaps, and inaccessible/plausible priority alternatives are explicitly retained; unsuccessful search alone is not novelty proof.

## value

PASS

A sharp arithmetic 3/4/6 restriction identifies precisely when observing an irreversible continuous-time Markov ring at an exact regular interval destroys all measurable one-step time asymmetry, plus a meaningful distinction between odd discrete-time reversible aliasing and even genuine reversible embedding. This exact finite-system classification is relevant to stroboscopic inference and not a routine stationary-distribution computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
