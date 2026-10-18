---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: Reconstructed the full normal form b a^k b a^j; a leading a power fixes Q. After first b and rotation, the missing h lies either inside the two-element duplicate kernel (then the second image still has n-1 states) or outside (then the second b omits exactly e and b(h)). The bijection b:Q\K -> Q\{e,d} makes the obtainable oriented nonzero hole differences all residues except rho=d-e. An unordered pair is excluded in both orientations iff n even, rho=n/2 and the pair is antipodal. Witness k=h-e mod n and j=x-e mod n gives length <=2n, for ALL n>=3; the exceptional case is only about exactly two b occurrences, not global reachability. Independent exhaustive brute-image enumeration (not source verifier) over all rank-n-1 b for n=3,4,5,6 checked 18,144,1200,10800 transformations, yielding exceptional maps only at even antipodal parameters (48/144 at n4 with two unreachable pairs; 2160/10800 at n6 with three). Infinite proof is structural, not inferred from finite checks.

## originality

PASS

PASS, best-of-knowledge: Don 2016 Proposition 2/Section 4 proves n(n-k) subset reachability for circular rank-defect-one machines when gcd(rho,n)=1 and his introduction observes generic 1-contracting reachability for at least C(n,2)-n codimension-two sets. Here the exact two-b classification holds for arbitrary rho, including noncoprime n=9,rho=3, and isolates the one antipodal obstruction, with explicit <=2n witnesses. Don does not give this precise all-displacements iff statement. Other reachability results require complete reachability, primitivity, or stronger hypotheses. Sharpness via Cerny family is preexisting, not a novel separate claim.

## value

PASS

PASS: Resolves the natural first nontrivial two-defect subset-reachability layer for the broad class of all cyclic-letter plus arbitrary defect-one-letter automata, identifies a sharp parity boundary, and gives explicit uniformly short words beyond coprime/complete-reachability assumptions; not a mere restatement of Don general bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
