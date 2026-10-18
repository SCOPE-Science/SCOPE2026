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

With a C++17 compiler, run:

```sh
c++ -O3 -std=c++17 verify/census.cpp -o census
./census 20
c++ -O3 -std=c++17 verify/independent.cpp -o independent
./independent
```

The first executable asserts the complete maximum and tie-count table and that every one of the \(2^n\) words of each length was visited. It prints `CENSUS_OK n=1..20` on success. The second implements Lyndon enumeration followed by greedy positional subsequence matching; it re-enumerates all words of lengths one through fifteen and independently checks the five longer extremizers, concluding with `INDEPENDENT_OK`. The packaged programs were compiled and run successfully from their source bytes before serialization.

The exact table of all extremizers is `data/maxima.tsv`. For example, at length twenty, the exhaustive maximum is \(4701\) with exactly one maximizing binary word. The second checker confirms that the exhibited word indeed has \(4701\) distinct Lyndon scattered subsequences, but its witness check alone is not an exhaustive upper bound for length twenty. No values at lengths above twenty have been proved.
