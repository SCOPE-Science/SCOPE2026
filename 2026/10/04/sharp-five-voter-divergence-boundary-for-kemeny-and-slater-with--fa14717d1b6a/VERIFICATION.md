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
The embedded `verify_kemeny_slater_five_voters.py` is an exact finite replay using only the Python standard library.

For each odd electorate size \(1,3,5\), it enumerates every labeled profile of strict rankings over three candidates.

Kemeny rankings are computed independently in two ways:
1. maximizing total pairwise support consistent with a ranking;
2. minimizing the total majority-margin weight of reversed majority edges.

Slater rankings are computed independently in two ways:
1. minimizing the number of reversed majority-tournament edges;
2. using a separate three-candidate implementation that distinguishes transitive tournaments from three-cycles.

The verifier confirms:
- \(6\) of \(6\) one-voter profiles have equal winner sets;
- all \(216\) three-voter profiles have equal winner sets;
- among \(7776\) five-voter profiles, exactly \(180\) diverge;
- the exact five-voter divergence probability is \(5/216\);
- every divergent profile has cyclic margin multiset \((1,1,3)\);
- an independent enumeration of all \(252\) anonymous five-voter profiles finds exactly six divergent labeled-candidate anonymous profiles;
- those six form one orbit under candidate relabeling;
- each has labeled-voter multiplicity \(30\), giving \(6\cdot30=180\);
- the canonical \(2(A\succ B\succ C),2(B\succ C\succ A),1(C\succ A\succ B)\) witness has two Kemeny rankings and three Slater rankings exactly as stated.

Run:

`python3 verify_kemeny_slater_five_voters.py`

The first output line must be:

`VERIFY_OK`

The finite replay establishes the sharp first odd-electorate boundary and the complete five-voter census only.
