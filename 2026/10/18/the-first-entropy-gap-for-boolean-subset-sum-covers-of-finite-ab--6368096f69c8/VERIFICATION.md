---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For a finite abelian H, lambda(H) is minimum length of a sequence, repetitions allowed, with all 0/1 subsums equal H; 2^k>=|H| gives the entropy bound. Binary powers in each invariant cyclic factor give sum ceil(log2 d_j) entries. An exact partition-based enumeration of the 38 abelian isomorphism types of orders 2..25 shows this matches ceil(log2|H|) except C5xC5 at 25. For C5^2 every spanning five-term sequence can choose a basis among its terms and normalize it to e1,e2: all 25^3 remaining triples (with repetitions) are exhausted by the recurrence S <- S union (S+v); maximum size 24, attained by 480 ordered normalized triples. Independent full 53130 five-subset census found exactly 1920 extremizers, partitioned by all 480 GL2 matrices into 6 orbits of sizes 120,120,240,480,480,480. Six explicit vectors with duplicate coordinate entries cover all 25 points; thus lambda(C5^2)=6. An independent checker rebuilt the normalized exhaustive search, subset census and linear orbits, agreeing exactly.

## originality

PASS

Erdős–Rényi and Hughes study Boolean subset-sum/product coverage asymptotically, whereas the present theorem is a first exact finite obstruction with complete GL2 classes. Li–Yip analyze pairwise sums/differences from a set, not sums of arbitrary subcollections of a sequence. No compared stated theorem entails a maximum of 24 from five vectors in F5^2 or the exact six-orbit classification.

## value

PASS

The first failure of the entropy-optimal Boolean subset-sum cover is a canonical finite threshold in an established coverage invariant; determining minimal length six plus maximal deficiency, exact extremizers and GL2 classes is a complete mathematically motivated classification, not an arbitrary slice of cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
