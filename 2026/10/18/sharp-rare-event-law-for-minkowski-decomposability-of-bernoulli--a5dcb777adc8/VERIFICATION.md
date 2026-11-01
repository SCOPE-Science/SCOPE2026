---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For fixed p in (0,1), N=2^n, b=p²+q², coordinate-prism E_i has independent N/2 matching pairs and exact probability b^(N/2). Pairwise E_i∩E_j has probability c^(N/4), c=p⁴+q⁴<b². Inclusion–exclusion for j directions gives (p^(2^j)+q^(2^j))^(2^(n-j)). By the published deterministic Boolean-polytope Theorem 1.1, every full-dimensional Minkowski decomposition corresponds to a coordinate Cartesian split. For smaller side k≥2, M=2^k, each J-column must be empty or a common size-a≥2 set A and has probability f=q^M+p^a q^(M-a). If p≥q, f≤p^M+q^M≤(p⁴+q⁴)^(M/4); if p<q, f≤q^(M-2)b≤(q² b)^(M/4). In both cases rho_p^4<b². At most 2^n 2^(2^(n/2)) choices multiply rho_p^N, exponentially below b^(N/2). Any deficient cube sample lies in a hyperplane containing at most 2^(n-1) cube vertices, and ≤2^(n²) hyperplanes spanned by n cube vertices suffice, giving exp(-Ω_p(N)) full-dimensional failures. Conditioned on E_i, N/2 independent collapsed Bernoulli indicators have parameter p²/b, giving the same bound. Therefore P(D_n|F_n)=n b^(N/2)(1+O_p(exp(-c_p N))), also P(D_n∩F_n). Two singleton factors and any nonsingleton product are negligible, leaving a unique unit coordinate segment times an indecomposable (n-1)-dimensional factor. Independent exact finite checker found 60879 full n=4 samples, 625 products, 577 prisms, 48 non-prism; rate inequalities checked for five rational p values and M=4..128. Finite enumeration is not the proof.

## originality

PASS

Best-of-knowledge originality PASS for the sharp fixed-p rare-event law n(p²+(1-p)²)^(2^(n-1)) with exponentially small relative error, and dominance by a unique coordinate segment. Published deterministic 0/1-polytope decomposition is an acknowledged prerequisite, as are Bernoulli random-polytope graph-expansion models. The exact stochastic prefactor and conditional prime-factor mechanism are not determined by inspected prior results. Older conjunctive AND decomposition enumeration might dominate, especially under switching-theory terminology; full text unavailable and no global priority certification claimed.

## value

PASS

The Bernoulli cube-vertex model is a canonical random 0/1-polytope. Quantifying decomposability as a rare event with its double-exponential probability, sharp dimension prefactor n and conditional unique segment factor answers a natural distributional/structural question not implied by a high-probability indecomposability slogan or deterministic decomposition alone. A precise exponentially smaller competing mechanism and an exact inclusion-exclusion formula for coordinate prisms make the result reusable for conditional structure or rare-sample analysis. This is a motivated global asymptotic invariant rather than an arbitrary small slice or textbook parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
