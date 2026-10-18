---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

Oddification \(f(\varepsilon)\mapsto (f(\varepsilon)-f(-\varepsilon))/2\) is an \(L^4\) contraction preserving the first-chaos component. Every odd input has the unique 8-coordinate form \(f=S+\chi T\) with \(S=\sum a_ir_i\) and \(T=\sum b_ir_i\). The exact Walsh fourth-moment difference \(\mathbb E(f^4)-(123/200)\mathbb E(S^4)\) was freshly rebuilt from the stated rational Gram matrices \(M_0,M_1,M_2\) and verified coefficient by coefficient in eight independent variables. Fresh symbolic computation independently evaluated every leading principal minor: all 8 of \(M_0\), 4 of \(M_1\), and 4 of \(M_2\) are strictly positive, so the identity is a genuine sum of squares for all real inputs. The explicit three-coordinate witness \(f=r_1+r_2+r_3+tr_1r_2r_3\) has projected fourth moment 21 and input moment \(21+18t^2+t^4+24t\), proving the lower bound. Numerical approximations are used only for illustration, not certification.

## originality

PASS

Best-of-knowledge original exact four-sign upper enclosure: the older named Rademacher-projection source describes an exact three-coordinate result and complementary-projection estimates, not this eight-variable four-coordinate SOS certificate. No stronger source implying the explicit rational constant was identified by accessible search. The 2009 full article could not be retrieved from lawful open routes or the unavailable institutional connection; this is a material residual comparison risk, not grounds for invented novelty proof.

## value

PASS

The norm of a canonical finite-dimensional Walsh projection is a natural precise invariant. A universal rational SOS certificate for the first nontrivial four-coordinate extension supplies an explicit \(1.12923\) upper bound, much sharper than the elementary Khintchine fourth-moment estimate \(3^{1/4}\), and closely brackets a concrete extremal witness. It is neither an arbitrary coefficient slice nor a purported exact determination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
