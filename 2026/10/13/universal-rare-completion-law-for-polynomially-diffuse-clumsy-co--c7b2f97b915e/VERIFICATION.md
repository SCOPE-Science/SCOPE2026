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
# Verification of the rare-completion law

## Reproduction
Run `python3 CHECKER.py` with the Python 3 standard library; no network, package installs, or external data are required. The checker reported `PASS: 540 exact rational assertions` on the packaged code. It directly enumerates the finite presence-state Markov chain and, separately, the visited-coordinate-set distribution; agreement verifies the exact conditional identity used in the analytical clump estimate.

## Analytical checks
The invariant distribution is the product of independent presence bits of bias \(q=1-p\). Its new-entrance flux equals \(p q^n\). The core identity \(a_{r+1}=p\mathbb E[q^{K_r}W_r]\) conditions only on the selected coordinates and is valid for arbitrary positive selection weights. For \(r\le1/(64w_+)\), repeat-selection counting gives \(\mathbb P(K_r<r/2)\le4^{-r}\); for later \(r\), the already-visited-set cardinality gives an exponentially small bound in \(1/w_+\). The lower frequency bound produces polynomial mixing, and the separate empty-start estimate excludes early completion. Stationary rare-entry block and burn-in arguments yield the law; a uniform block success bound yields moment convergence.

## Scope of computational evidence
Checks are finite and exact; they do not prove asymptotic convergence or exhaust all probability vectors. The mathematics applies only to fixed \(p\in(0,1)\), polynomially diffuse weights, and the specified one-coordinate refresh process. The obstruction with a coordinate of weight \(e^{-\theta n}\), for \(\theta> -\log(1-p)\), shows that the same normalization need not work outside the class. Independent validation is not claimed.
