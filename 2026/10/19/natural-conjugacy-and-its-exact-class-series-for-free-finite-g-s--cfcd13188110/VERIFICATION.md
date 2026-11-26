---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With the frozen composition convention, ag=gb and hag=b imply hgb=b; bh=ha and gbh=a imply gha=a. The restrictions of g and h to the respective images are mutually inverse and intertwine the restrictions. Conversely, an equivariant image isomorphism extends to g and its inverse to h: on each free exterior orbit choose a representative and a preimage of the required target under a or b. Freeness makes extension equivariant and well-defined, and intertwining plus the inverse restrictions give the last two witness equations. For the image isomorphism from a to b the multiplier equation is u_i t_(f(i))=t_i v_(σ(i)). Eliminating twists around each directed cycle equates ordered products up to conjugation by the first twist, and a matching conjugacy allows all twists on the cycle to be solved. Tree twists are then uniquely solved given their successor's twist, with no commutation of group factors. An image digraph with r vertices and s internal sources requires r+s≤m, since distinct sources need distinct exterior preimages; one new orbit per source suffices and extra exterior orbits may all map to any image vertex. Weighting each internal source by one extra z gives a leaf of weight z², a nonleaf tree root of weight z, and a cycle vertex of weight z even without attached trees. The multiset transform gives T=z(E−1)+z² and A=zE; the recursion uniquely gives an integral tree series. Burnside on rotations yields the connected cycle series c∑(φ(k)/k)log(1/(1−A(z^k))). The component multiset transform then uses ∑_(d|n)φ(d)=n to give the stated product; discard the empty graph and accumulate degrees through m to obtain the factor 1/(1−z). As an independent coefficient check, A=z+z³+z⁴+2z⁵+3z⁶+O(z⁷), so F_1 has coefficients 1,1,2,4,8,15,31 through degree six; cubing F_1 and cumulatively summing its positive-degree coefficients gives 3,12,37,103,268,675, as claimed. For m=2 there are c one-loop, c two-cycle, and binomial(c+1,2) two-loop types, giving 12 for S_3. Inspected VERIFICATION.md and verification/check.py; no frozen script was executed. The file exists despite not being included in the initial bound support list. Its documented direct witness check is finite, not the justification for extension or enumeration for all m.

## originality

PASS

The supported increment is the nonabelian free-orbit classification and its all-m class series. The abelian trim framework and the trivial-group image-digraph classification are prior work, and the counting transforms are standard. The inspected paper asks for the nonabelian extension and does not already give the stated free nonabelian classification and source-weighted series.

## value

PASS

This classifies a natural semigroup relation on a free action of an arbitrary finite group, extending a stated question to the free case. It explains why only cycle holonomies survive and why class counts depend only on c(G), not the group's order or structure beyond it. The minimum ambient orbit cost of an image diagram makes the all-m enumerator usable and is not a count of unrestricted endomorphisms or of unit-conjugacy classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
