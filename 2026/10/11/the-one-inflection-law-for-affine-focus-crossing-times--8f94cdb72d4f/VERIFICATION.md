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
# Verification and scope

The exact coordinate solution was checked against the initial-value problem \(\ddot x-T\dot x+Dx=a\), \(x(0)=0\), \(\dot x(0)=-u\). Every first return is obtained by inverting \(u=F_\delta(\omega\tau)\) on \((0,\pi)\), and the strict increase of \(F_\delta\) proves both existence and its first-return character.

The standalone `check_flight_time.py` (SymPy dependency specified in `requirements.txt`) symbolically checks \(N_\delta'\), the identity \(M_\delta'=\sin\theta\,K_\delta\), the differentiated expression for \(K_\delta'\), and the endpoint \(M_\delta(\pi)\) and leading small-angle coefficient. It also performs finite numerical sign checks at a fixed selection of traces; observed output on execution was `CHECK_OK`. Direct integration of four independently selected admissible initial-value problems showed crossing residuals smaller than \(6\cdot10^{-11}\); these finite tests are not used to establish infinitely many parameter cases.

The proof's genuinely global step is analytic: positivity of \(N_\delta\) and the one-turn sign structure of \(K_\delta'\) yield exact counting of zeros of \(M_\delta\). No interval arithmetic or computer-assisted infinite theorem is asserted. A different sign of the forcing, a nondamped-node matrix, or a composite two-zone Poincaré map is outside scope. Publication priority beyond the inspected literature has not been independently certified.
