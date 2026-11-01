---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

With dA=dxdy/pi and source norm log(e/(1-|z|^2))^alpha, angular integration makes the squared monomial norm v_k(alpha)=int_0^1 t^k log(e/(1-t))^alpha dt. The normalized Hilbert coefficient matrix has entries B_mk=1/((m+k+1)sqrt((m+1)v_k)); Tonelli gives its exact positive HS norm squared sum_{k>=0} S_k/v_k, S_k=sum_{m>=0}1/((m+1)(m+k+1)^2). For k>=1, partial fractions yield S_k=H_k/k^2-(zeta(2)-H_k^(2))/k, S_0=zeta(3). Independent high-precision summation confirmed this for k=1,2,5,20. The Laplace scaling s=k(1-t), with uniform logarithmic moments for alpha∈[2,3], gives v_k=(log k)^alpha/k(1+O(1/log k)); S_k=(log k+gamma-1+O(1/k))/k^2. Hence summands are 1/(k(log k)^(alpha-1))+O(1/(k(log k)^alpha)) uniformly near 2, with uniformly summable remainder; the integral test yields squared HS norm=1/(alpha-2)+O(1). For every fixed alpha≤2 the positive series diverges, while for alpha>2 it converges. Endpoint boundedness does not imply HS. The precise O(1) error and coefficient 1 are normalization-sensitive; no other Schatten exponent or singular-value distribution is proved.

## originality

PASS

Karapetrović (2018) same-source logarithmic Bergman/Hilbert operator article was retrieved and inspected in its complete 19-page primary PDF: §3.2 Theorem 3.2 proves bounded mapping for alpha>2 into A^2_{log^(alpha-2-epsilon)}, not Hilbert–Schmidt membership, trace series or coefficient-one blow-up. Norrbo 2026 accessible full HTML §3.5 proves boundedness at alpha=2, not HS. The published 2026 Resultary/SCOPE Copson model at alpha=2 was read in full: it shows the discrete endpoint normalization differs by an HS operator from a triangular Copson model and determines the essential spectrum/norm; its triangular entries can be damped to heuristically anticipate the supercritical S2 frontier, a genuine substantial implication/priority risk. However it does not provide the precise original Bergman monomial-moment normalization, the exact positive harmonic-number trace identity, or the uniform coefficient-one O(1) blow-up, which require additional summation and uniform moment control. The surviving claim is this exact quantitative supercritical norm law, not new compactness, boundedness, or an endpoint HS perturbation. Best-of-knowledge originality PASS with explicit strong related precursor and possible direct-corollary risk.

## value

PASS

The alpha=2 logarithmic endpoint is a sharp natural boundedness/compactness frontier. The trace of H*H is the natural Hilbert–Schmidt compactness invariant; its exact full parameter series and coefficient-one pole quantitatively sharpen an already interesting phase transition in the actual Bergman normalization. This is not a recomputation of a known essential norm or a claim about general Schatten p.

The dated certificate retains the supplied scientific assessment, sources and limitations.
