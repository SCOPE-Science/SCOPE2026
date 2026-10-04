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

The accepted statement was checked directly from the definition of \(\delta\)-average roughness and the weighted equivalent formulation in arXiv:1702.03140v1.

For the finite lower bound, the proof uses the explicit positive \(\ell_q^m\)-norming vector \(c_{ij}=\|x_{ij}\|^{p-1}\), so \(\|c_i\|_q=1\) and \(\sum_j c_{ij}\|x_{ij}\|=1\). The weighted factor inequalities are then combined with Minkowski's inequality, and \(\sum_j c_j\ge1\) yields the factor \(m^{-1/p}\).

For the upper bound, the coordinate-axis test family gives
\[
\|e_j u_j\pm h\|_p^p\le(1+\|h_j\|)^p+\|h\|_p^p-\|h_j\|^p.
\]
A uniform Taylor estimate followed by concavity gives \(1+\|h_j\|+O(\|h\|_p^r)\), where \(r=\min\{p,2\}>1\). Hölder's inequality then gives the limiting coefficient \(2m^{-1/p}\).

The infinite case is not inferred from a finite experiment: for each integer \(m\), one chooses \(m\) distinct coordinate axes inside the infinite sum, obtaining the necessary inequality \(\delta\le2m^{-1/p}\). Since this holds for all \(m\), every positive \(\delta\) is impossible.

No external computation or certificate is required for the proof. The theorem has not received an independent audit.
