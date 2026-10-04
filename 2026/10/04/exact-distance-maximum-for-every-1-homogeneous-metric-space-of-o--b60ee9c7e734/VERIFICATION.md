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

The general theorem is verified at the proof level rather than inferred from computation.

1. If \(G\) is transitive on \(2m\) points and has \(c\) orbits on unordered pairs, the corresponding orbital graphs have positive valencies \(d_1,\ldots,d_c\) summing to \(2m-1\).
2. If \(s\) of those valencies equal \(1\), then \(2m-1\ge2c-s\).
3. Every valency-one orbital graph is a \(G\)-invariant perfect matching. Its mate map is an involution commuting with \(G\), and distinct matchings give distinct involutions.
4. The centralizer of a transitive permutation group is semiregular: fixing one point forces a centralizing permutation to fix the whole transitive orbit. Hence its order divides \(2m\).
5. For odd \(m\), a group whose order divides \(2m\) has 2-part at most \(2\). Its involutions are in bijection with its Sylow \(2\)-subgroups, whose number divides the odd part of the group order, so there are at most \(m\) involutions. Thus \(s\le m\).
6. Therefore \(c\le(3m-1)/2\), and the number of distances is at most \(1+c=(3m+1)/2\).
7. The published construction \(D_m\) has \(2m\) points and \(\lfloor m/2\rfloor+1+m=(3m+1)/2\) distances when \(m\) is odd, so the upper bound is attained.

A separate finite sanity check used the standard degree-18 transitive-group catalog. Orbit enumeration on all \(153\) unordered pairs for all \(983\) transitive groups found maximum pair-orbit count \(13\), attained by 18T4 and 18T5. This independently agrees with the theorem's \(\Delta_1(18)=14\), but it is not used to prove the infinite family.

No independent audit has yet been performed.
