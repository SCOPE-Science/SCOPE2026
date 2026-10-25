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

Set c_n=n!a_n, log-concave with interval support. For any k>=1 and residues 0<=j,l<m, indices mk+j,mk+l lie between m(k-1)+j and m(k+1)+l and sums agree, so c_{mk+j}c_{mk+l}>=c_{m(k-1)+j}c_{m(k+1)+l}. The positive factorial weights A_{k,j}=k!/(mk+j)! obey A_{k,j}A_{k,l}>=A_{k-1,j}A_{k+1,l}, since the first k-step quotient is smallest at j=m-1 and second largest at l=0, where they are exactly equal. Multiply and sum m^2 cross-pair inequalities to obtain (k!b_k)^2>=((k-1)!b_{k-1})((k+1)!b_{k+1}), all m including m=1. For m>=2 and b_{k-1}b_{k+1}>0, interval support forces a_{mk}>0 and strict j=l=0 cross-pair gap, so strict ULC. For Poisson input, grouped arrivals are exactly Erlang(m,lambda) renewal counts and strictly decreasing R(k)=(k+1)b_{k+1}/b_k yields Cov(Y,R(Y))=Var(Y)-E[Y]<0. Independently checked 637 exact rational factorial-factor comparisons for m<=6,k<=7; finite checks only corroborate the quantified argument.

## originality

PASS

Puig-Valero-Fernandez-Fontelo 2023/2024 establishes underdispersion of IFR/Erlang renewal counts, which is weaker than distribution-wide strict ULC or closure for all interval-supported ULC inputs. Badiella-del Castillo-Puig 2023 proves ULC for independent-replicate order statistics, a different transformation from deterministic floor(X/m). Classical convolution and thinning closures likewise do not immediately imply equal-width aggregated-block closure. Search did not locate a more general theorem with exact operator, leaving priority uncertainty.

## value

PASS

ULC is a strong regularity property giving more information than the known variance bound; exact closure for every equal integer block size extends from Poisson to arbitrary interval-supported ULC laws, with a strictness theorem. It supplies a reusable structural fact about deterministic count coarsening and Erlang renewal distributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
