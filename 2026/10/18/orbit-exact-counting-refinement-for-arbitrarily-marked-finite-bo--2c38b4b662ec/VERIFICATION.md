---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The finite Boolean lattice has automorphism group S_n acting on its atoms; stabilizing every individually named subset forces the product of symmetric groups within identical membership columns I_sigma, hence orbit coordinates c_sigma and the binomial class size/product count. Incoming and outgoing cover degrees distinguish ranks after one round. Each atom has (a-1)! upward paths to a uniquely named rank-a marker iff it belongs, allowing the marker bit vector to be separated in at most n-1 rounds. At rank k+1, the sum of the k+1 predecessor count-vectors is k times c(Y), recovering the next rank after one further round, proving the 2n-2 bound. n=1 and empty or zero/full markers are consistent special cases; fixed lattice internal orbit exactness is not global graph identification. An independently written synchronous directed-WL enumeration tested 223 distinct-marker configurations across n=2..5, with maximal observed three rounds. Bounded tests are not the all-n proof.

## originality

PASS

Best-of-knowledge after direct statement/implication comparison with the cited primary mathematical works and targeted Resultary published-record semantic searches; general methods and known special cases are credited. Failure of a search is not proof of priority, and inaccessible plausible sources remain explicit residual risks.

## value

PASS

For finite Boolean covering digraphs with arbitrarily many individually named vertices, a sharp-type explicit automorphism-orbit invariant, finite WL convergence guarantee in n rather than 2^n, and complete orbit-size/colour-count product formulas offer a reusable structural comparison and symmetry-reduction fact. The exact bound and arbitrary-marker regime have mathematical motivation beyond merely computing small examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
