---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For P(n,2), n>=5, open-neighbour F2 parity dynamics has Laurent transition M(x)=[[u,1],[1,u^2]], u=x+x^-1; det=u^3+1 and x^3 det=(x^2+x+1)(x^4+x^3+x^2+x+1). With n=k r and k=2^v2(n), odd r, each selected root of order 3 or5 supports a local length-k truncated ring. At a primitive 3rd root, z=u+1 is a uniformizer and exactly M^2=zU for a commuting invertible U, with Smith exponents (0,1), giving rank max(2k-t,0) and one zero Jordan block of size 2k per root. At a primitive 5th root, trace(M)=1 at the root and its determinant vanishes simply, giving one zero block size k and an invertible k-block per root. Therefore with alpha=1_{3|r}, beta=1_{5|r}, zero Jordan sizes are 2alpha blocks of 2k and 4beta blocks of k, stable dimension d=2n-4k(alpha+beta). Recurrent configurations number 2^d, maximum depth T=max(2k alpha,k beta), and cumulative depth<=t count H_n(t)=2^{d+2alpha min(t,2k)+4beta min(t,k)}. These imply invertibility iff gcd(n,15)=1 and last-depth fractions 3/4 or15/16, respectively. Independently rebuilt adjacency over F2 for all n=5..80 and matched 331 ranks, including n5 recurrent64 T1, n6 recurrent16 T4. Infinite conclusions follow local-algebra decomposition, not numerical extrapolation.

## originality

PASS

Qualified PASS: existing real spectra of generalized Petersen graphs do not determine mod-two higher-power ranks or Jordan chains. Torrence-Torrence binary Lights Out on Petersen graphs studies the CLOSED-neighbour A+I response map rather than repeated open-neighbour A dynamics and does not supply the present transient depth census. The assessed 3/5 root resonance and all-n Jordan-depth formula are the specific increment.

## value

PASS

The generalized Petersen graph family is a standard natural cubic-graph family, and open-neighbour parity is a canonical finite linear dynamical rule. Its exact 3/5 resonance, periodic dimension and complete transient-depth distribution for every n provide structural and enumerative information beyond a one-step rank. These formulas are not arbitrary small-parameter slices and distinguish characteristic-two Jordan phenomena from real spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
