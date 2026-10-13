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

The concrete check is exact. For \(X\sim N(0,1)\),
\[
X_{i:n}\overset{d}{=}-X_{n-i+1:n}.
\]
With \(q(x)=1-x\),
\[
q(X_{n-i+1:n})\overset{d}{=}1+X_{i:n}.
\]
Translation leaves differential Shannon entropy unchanged and also leaves \(\int f(x)^2\,dx\) unchanged. Hence the source's Shannon equality and its \(\alpha=2\) Tsallis, Rényi, information-generating, and extropy analogues hold for every \(n\ge i\). Yet \(q(X)\sim N(1,1)\), so the prescribed q-symmetry conclusion fails.

For the structural diagnosis, set
\[
p(x)=F^{-1}(1-F(x)).
\]
Substitution of \(u=1-F(x)\) into the source's quantile-density identity gives
\[
q'(x)=-\frac{f(x)}{f(p(x))}.
\]
Direct differentiation of \(p\) gives the same derivative, and therefore \(q=p+C\) on connected full support. The derivative condition alone cannot determine \(C\).

The verification does not extend the counterexample to weighted extropy, and it does not assert that bounded-support versions retain the same additive freedom. No numerical experiment is part of the proof.
