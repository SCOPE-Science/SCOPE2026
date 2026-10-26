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

# Verification and reproducibility

The standalone Python 3 program `check_involutions.py` uses only the standard library. Running `python check_involutions.py` enumerates all involutions on labelled sets of orders 1 through 7, all ordered pairs, and verifies component decomposition and eleven exact mixed factorial-moment identities by integer arithmetic. The combined enumeration has exactly 60,397 ordered pairs, and the terminal success line is `INVOLUTION_COMPONENT_MOMENTS_OK 60397 11`.

The exact identity checked is
\[
\mathbb E\left[\prod_H(C_H(n))_{r_H}\right]=(n)_M\left(\frac{I_{n-M}}{I_n}\right)^2\prod_H |\operatorname{Aut}(H)|^{-r_H}.
\]
The checker does not test arbitrary first-order sentences and does not certify any limit from finite samples. The infinite proof additionally uses the known asymptotic for involution counts, bounded-degree Hanf locality, saturation of nonclosed rooted neighbourhood types and independence of the Poisson limits for arbitrarily many fixed odd path sizes. These arguments are explained in `RESULT.md`.

The Poisson component description substantially overlaps Lugo's 2009 results. Unavailable complete historical coverage, especially the full Compton 1987 paper, limits novelty certainty. Self-review was performed; independent audit has not been performed.
