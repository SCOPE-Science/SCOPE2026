---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For d=w+z and H={0,d}, rederived f_c(s)=s+c+d 1{bar(s+c)=bar w}; functional Yang-Baxter identity holds because its correction depends only on V/H. Each local sweep adds e_i=c+d A_i to both site and carrier; modulo H, A_i(t)=1{bar(x_i(0)+b0(0)+i c+t(m+1)c)=bar w}. For odd m or c in H, T²=I; otherwise invariant two-sweep B_i moves each site by d B_i, giving T^4=I and Fix(T²)=q(q-4)^m. One-sweep zero-increment count gives Fix(T)=q(q-2)^m when c=0, q 2^m when c=d, otherwise zero. Hence cycles C1=F1,C2=(F2-F1)/2,C4=(q^(m+1)-F2)/4. The two-point nonzero correction is nonaffine since a nonconstant affine H-valued map has q/2>=4 nonzero inputs. Independent exhaustive full-state sweeps tested 72 parameter/length cases in F2^3 and verified all period and fixed counts.

## originality

PASS

Qualified PASS: Araoka–Tokihiro 2026 invent/transcribe admissible finite-field Yang–Baxter maps, shifted transpositions, helical model, and limited period observations, all acknowledged as prior. Their Table 1 counts rules by maximum period and their §3.2 q=8 case analysis does not give the present full-state primitive census for all n,m. Published Resultary affine helical census covers only affine maps; the present shifted transpositions are provably nonaffine at q>=8. Later journal version and unindexed orbit combinatorics remain risks.

## value

PASS

PASS: The family is a canonical nonlinear subfamily of finite-field Yang–Baxter automata and exact primitive site-plus-carrier orbit populations are a natural complete dynamical invariant. A mixed period-2/period-4 phase fraction 1-(1-4/q)^m is materially stronger than a period upper bound, not an arbitrary small parameter check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
