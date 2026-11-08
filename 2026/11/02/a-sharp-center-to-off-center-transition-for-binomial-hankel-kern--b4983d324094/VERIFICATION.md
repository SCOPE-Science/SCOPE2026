---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Poisson variance identity gives exact testing F_c(r)=1+c^2-r^{2m}-c^2 r^{2n}+2c r^{m-n}(1-r^{2n}) after optimal angular phase; boundary r=1 gives zero and center value 1+c^2. For m<3n positive r^{m-n} term dominates for small r, so center never maximizes. For m>=3n set x=r^{2n}, p=(m-3n)/(2n) and inspect discriminant of c^2-2c x^p(1-x)+x^{2p+2}; upper root x^p(1-x+sqrt(1-2x)) yields c_+=2^{-p-1}(1-y)^p(1+y)^{p+2}, y=sqrt(1-2x). Its unique maximum gives c threshold when p>0 and coexistence radius, while p=0 gives threshold 2 with continuous central approach. Small c scaling r=c^{1/(m+n)}s produces limiting maximand 2s^{m-n}-s^{2m}, unique maximizer s=((m-n)/m)^{1/(m+n)} and gain K c^{2m/(m+n)}. Finite-rank Hankel H^*H=I+c(S^d+(S*)^d)+c^2P_n has paths of maximal size ceil(m/d), providing operator slope cos(pi/(L+1)) and strictly larger norm. Independently verified rational m=5,n=1 threshold 27/64, coexisting r^2=3/8 and finite kernel matrix identity. No formal certification, finite checks do not prove all m,n,c.

## originality

PASS

Classical kernel Poisson identity, Garsia norm and strong reproducing kernel thesis equality locus are known. Full mathematically relevant published polynomial-rigidity and finite-rank shifted-Blaschke classifications were read and do not provide explicit maximal kernel location for failure-of-equality symbols or fractional-response constants. Direct new Dyakonov source accessible as abstract only; its full text attempt was blocked, and institutional method returned vpn_disconnected. Best-of-knowledge priority PASS with explicit unresolved full-text comparison risk.

## value

PASS

Quantifies how far normalized reproducing kernels are from norming a two-frequency finite-rank Hankel operator, separating continuous/discontinuous optimal kernel radius and fractional vs linear coefficient response; a natural structural invariant beyond known SRKT yes/no classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
