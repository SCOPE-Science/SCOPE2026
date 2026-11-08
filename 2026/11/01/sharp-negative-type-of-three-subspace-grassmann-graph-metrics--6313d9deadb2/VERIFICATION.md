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

For every prime power q>=2 and n>=6, the q-Grassmann distance-regular intersection numbers c_i=[i]_q^2 and b_i=q^(2i+1)[3-i]_q[n-3-i]_q yield the three nonconstant A_1,A_2,A_3 spectral triples. Reconstructed the recurrence and the j=2 powered-distance eigenvalue F_{q,n}(p)=q^3[n-5]_q(1-(q+1)2^p+q3^p)-(q+1)+q2^p. Its derivative is positive for all p>=0, F(0)=-1 and F(1)>0, while j=1 and j=3 remain strictly negative through the root p_{q,n} in (0,1); j=1 remains negative everywhere. Therefore the distance power is conditionally negative semidefinite exactly for 0<=p<=root; its Gaussian entrywise exponential is PSD for all t>0 exactly in that interval by Schoenberg; strict Gaussian positivity follows from distinct Euclidean configuration points. E_2 has endpoint nullity [n choose2]_q-[n choose1]_q, giving exact minimal embedding dimension [n choose3]_q-1-nullity. The first-order Taylor expansion gives p~(q-1)/(q^(n-2)(q log3-(q+1)log2)) for fixed q. An independent Python fractions calculation recomputed the exact eigenbranches on 28 (q,n) choices, including q=4,8,9; numerical root p_{2,6}=0.27053081961035363. Finite checks corroborate, do not prove, the all-parameter statement.

## originality

PASS

Classical Grassmann eigenstructure and Schoenberg negative-type theory give the machinery but do not by themselves state the sharp rank-three q-Grassmann exponent, the decisive middle harmonic, endpoint nullity and asymptotics. Material primary readings and a published-record search identified no dominating theorem giving this exact parameter family; best-knowledge only.

## value

PASS

For the natural finite-field Grassmann graph and its canonical graph metric, the supremal negative-type exponent controls Hilbert embeddings and universally positive Gaussian kernels. The complete all-field and all-ambient-dimension critical exponent, exact endpoint nullity, and small-exponent asymptotics are motivated structural invariants and not just routine parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
