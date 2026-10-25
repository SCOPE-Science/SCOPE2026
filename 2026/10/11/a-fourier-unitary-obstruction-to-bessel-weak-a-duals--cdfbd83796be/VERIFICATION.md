---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

The submitted bounded example satisfies all stated quantified hypotheses of Bellomonte Theorem 3.20: H=ell2(Z), X=[0,1] Lebesgue; Fourier M:H->L2(X) unitary; A=diag(lambda_n), lambda_n=2^{-|n|}, is bounded, compact, selfadjoint, injective, everywhere-defined and hence closable/densely-defined. sum_Z lambda_n^2 = 1+2 sum_{n>=1}4^{-n}=5/3, so phi_x=(lambda_n exp(-2pi i n x)) is an H-valued weakly measurable vector of norm sqrt(5/3), with analysis C_phi=MA. Plancherel establishes integral |<f,phi_x>|^2 dx=||Af||^2=||A* f||^2, exactly the weak A-frame bound with lower constant one. If Bessel weak A-dual psi exists its analysis C_psi:H->L2 is bounded and weak dual identity for all f,u (since bounded A) yields A=C_phi* C_psi. But C_phi*=A M* is injective and A=C_phi* M, implying C_psi=M. For each n in Z, C_psi u_n=exp(2pi i n x) a.e.; intersection over countable Z yields one common full-measure set where every coefficient <u_n,psi_x> has modulus 1. Parseval there requires ||psi_x||^2=sum_Z 1=infinity, contradiction. This is an unrestricted infinite-dimensional analytic proof, not finite sampling or experimental inference. For optional sufficient repair, HS M implies sum_n||M u_n||_L2^2<infinity, hence almost-everywhere square-summable pointwise coefficient representatives and a Bessel H-valued field; this is sufficient, not necessary. No claim is made about the other implications of Theorem 3.20 or general unbounded-A domains.

## originality

PASS

Qualified best-of-knowledge originality of the explicit Bellomonte Theorem 3.20 counterexample, not of its basic Fourier/diagonal upper-semi-frame construction. The exact 2021 source theorem and pointwise-Riesz proof were inspected, and the submitted bounded compact injective A with a dense-range Bessel analysis map demonstrably violates its claimed Bessel weak A-dual implication. Speckbacher--Balazs (arXiv:1704.02818v2, 2019) already gives the Fourier-diagonal construction in Proposition 20 and Example 4, and earlier general point-evaluation/RKHS restrictions. That source predates the targeted 2019-preprint/2021 theorem and does not state the failure of its weak A-dual existence claim or the forced-dual identity. Hence the accepted claim is only the later theorem-specific falsification and precise repair boundary, with a serious residual risk that it is considered an immediate consequence of prior constructions.

## value

PASS

A concrete, elementary but structurally motivated counterexample directly refutes the advertised (weak A-frame => Bessel weak A-dual) leg of a published operator-frame characterization, under the standard nonatomic coefficient space and a bounded compact positive injective A. Its failure mode is precisely the illegitimate application of pointwise Riesz to a generic bounded H->L2 operator, not an isolated numerical pathology. The later same-topic paper (Antoine--Bellomonte--Trapani 2021, Remark 3.9(ii)) explicitly uses the invalid implication, amplifying the mathematical importance of identifying this boundary. An HS coefficient factor is a motivated sufficient way to obtain pointwise vectors; a discrete counting-measure coefficient space avoids the obstruction. These qualify as a substantive counterexample and a useful hypothesis boundary, while no new generic HS theorem, characterization of all L2-representable operators, or independent review of unrelated results is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
