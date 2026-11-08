---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For every integer k>=3, n>=2k, x∈[0,1/(k-1)], the exact Newton identity K_x=Σ_{j=0}^k c_j(x)T_jT_j^T follows from binomial inversion on h=|S∩T|. For all j<k, the negative odd terms in c_j/x^{(k-j)^2} sum below e^{1/4}-1<1, so c_j>0; the displayed derivative and right-endpoint inequalities show the top coefficient B_k decreases from 1 to below zero and has a unique simple root ρ_k. The Boolean up/down commutator D_{r+1}U_r-U_{r-1}D_r=(n-2r)I makes T_{k-1} injective for n>=2k and its image contains all lower incidence spaces, hence endpoint rank binom(n,k-1). On its orthogonal complement the eigenvalue is B_k(x), negative just beyond ρ_k. Independent exact rational recomputation checked all 5,300 entries of two inclusion-Gram decompositions (k=3,n=6; k=4,n=8), positive lower coefficients and roots for k=3,4,5,6,8,12. Finite checks corroborate, but the proof establishes the full infinite n,k domain. The theorem deliberately does not classify x>1/(k-1) or all potential later PSD windows.

## originality

PASS

Best-of-knowledge PASS: neither the inspected 2008 Johnson adjacency-spectrum theorem nor the 2014 geodesic-Gaussian all-bandwidth criterion establishes the all-k, ambient-n-independent first-loss boundary and exact nullity. The present Newton inclusion-Gram inequalities and endpoint sector rank supply a comparison not given by prior numerical eigenvalue machinery. A general unlocated association-scheme cone theorem remains a credible priority risk.

## value

PASS

Johnson subset graphs and radial Gaussian kernels are canonical finite metric and kernel objects; a uniform-in-ambient-n exact first-loss cutoff and exact endpoint nullity give a meaningful all-k classification and identify the Boolean top-incidence obstruction. It is not merely a numerical spectrum evaluation or rephrasing of the Eberlein polynomial; the lower-sector positivity bound is substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
