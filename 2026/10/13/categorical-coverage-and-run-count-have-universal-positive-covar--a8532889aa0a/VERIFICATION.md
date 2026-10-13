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
# Verification

The exact domain is an iid sample of length \(n\ge2\) from a finite alphabet of at least two symbols with positive probabilities.

The critical proof checks are:

1. For each symbol \(a\), the event that \(a\) is absent and one distinguished adjacent pair differs has probability
   \[
   (1-p_a)^{n-2}
   \left[
   (1-p_a)^2-(s_2-p_a^2)
   \right].
   \]
2. Subtracting marginals gives
   \[
   \operatorname{Cov}(A_a,I)
   =
   p_a(1-p_a)^{n-2}
   \left[
   2s_2-(1+s_2)p_a
   \right].
   \]
3. Stationarity of adjacent pairs gives the factor \(n-1\).
4. With
   \[
   U_t=\sum_i p_i(1-p_i)^t,\quad
   V_t=\sum_i p_i^2(1-p_i)^t,\quad
   W_t=\sum_i p_i^3(1-p_i)^t,
   \]
   Cauchy--Schwarz yields \(V_t^2\le U_tW_t\), so \(V_t/U_t\) is nonincreasing and at most \(s_2\). This proves strict positivity of the total covariance.

`checker.py` enumerates iid words exactly under several rational nonuniform probability vectors and recomputes the weighted moments of coverage and transition count. It also checks the uniform conditional switch-versus-repeat gap and replays the tilted-ratio inequality over a larger finite family.

Finite computation is used only as an independent check; the theorem for arbitrary \(n\), \(m\), and positive probability vectors rests on the symbolic proof.

No claim is made for dependent sequences, fixed-composition words, or full positive association.
