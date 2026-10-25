---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Inclusion-exclusion of coprime counts gives the exact a.e. sawtooth identity D_qp(t)=h_q(t)-h_q(pt), where h_q(u)={qu}-{u}. Couple uniform T=(K_p+U)/p to independent V=(K_p+W)/p. On all but at most q-1 grid intervals containing a breakpoint of h_q, |h_q(T)-h_q(V)|<= (q-1)/p; bounded density of h_q(V)-h_q(U) proves the stated uniform CDF error <=2(q-1)/p. Integrate the piecewise affine law for second/fourth limiting moments. For q=3, exact integral over j/(3p)<t<(j+1)/(3p) reduces to sum_j[E_j^5-(E_j-Delta)^5]/[5 Delta(3p)^5]. Splitting p=3m+kappa and residues j=kp+s, s=3a+u shows each branch numerator is a rational polynomial in m of degree at most 6; checking 7 exact nodes per branch therefore proves all m. Independently computed all 14 integer nodes m=0..6 and rational H4 at p=5,7,11,13,17,19,23,29, matching the two stated closed rational branches; independent finite values corroborate the degree-bound proof.

## originality

PASS

Delange second-moment theory and Brown 2026 generalized fourth Franel/Mobius reduction are prior, as are McIntosh 1996 and multiple-Franel techniques. Brown explicitly leaves general odd squarefree fourth integrals unsimplified. The precise all-p 3p rational two-branch evaluation and quantified fixed-q limiting distribution have no matched theorem in compared full-text portions, though earlier Franel identities might specialize implicitly; inaccessible 1993 Greaves-Hall-Huxley-Wilson remains a material risk.

## value

PASS

The case 3p is the first natural odd semiprime two-factor family for a newly studied fourth Delange integral. A closed exact formula for every prime p and sharp quantitative weak-limit coupling explain the common asymptotic fourth moment structurally, rather than recomputing Delanges known second moment or an arbitrary small numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
