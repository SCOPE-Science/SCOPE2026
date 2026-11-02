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

For H(z)=z^n+sA overline(z)+B with n>=2 and independent standard circular complex Gaussian A,B, the critical circle of f_n(z)=z^n+overline(z) has radius r_n=n^(-1/(n-1)). The inequality |z^n-w^n|<|z-w| for distinct interior disk points gives at most one reversing preimage, and winding/degree n yields exactly n+2 roots when the effective Gaussian target is in the hypocycloid and n otherwise. Polar-angle monotonicity W_n=n(n-1)(1-cos u)/(n²+2n cos u+1) proves a one-valued radial boundary, hence one random crossing T_n=(|B|/rho_n(Theta))^(1/q_n)/|A|. Independent Rayleigh/exponential integration gives the exact p_n(s) and Mellin strip -2q_n<p<2; Green-residue area and inertia supply small-s coefficients, and moment Taylor supplies large-s coefficients. Expanding q_n=1+1/n+O(n^-2), log rho²=(-2 log n+2 cos u)/n+O(log n/n²), weighted polar Jacobian W_n=(1-cos u)+O(n^-1) and the gamma logarithmic integral gives p_n(s)=s²/(1+s²)-s²[2 log n+EulerGamma+log(1+s^-2)]/[n(1+s²)²]+O_delta,Delta(log²(n)/n²), uniformly on each compact positive coupling interval. Boundary n=2 and s->0/infinity and exclusion of singular threshold respected.

## originality

PASS

Known harmonic-map argument-principle and hypo/epicycloid trinomials supply the deterministic zero-count mechanism, not the Gaussian one-threshold distribution and exact Mellin/moment law. The independent finite-degree coupled random phase/size integration and log(n)/n coefficient were not found in the inspected old references or the targeted Resultary search. This is best-of-knowledge, not a priority guarantee.

## value

PASS

The number of roots is a canonical random-harmonic-map statistic. Its single-threshold distribution and sharp moment strip quantify a real stochastic transition, while the logarithmic large-degree correction discriminates it from the naive rational limit; this is a genuinely motivated exact invariant beyond the known deterministic root-count classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
