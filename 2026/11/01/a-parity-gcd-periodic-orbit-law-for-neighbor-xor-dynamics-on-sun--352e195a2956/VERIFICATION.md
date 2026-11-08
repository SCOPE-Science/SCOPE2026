---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS. Eliminating leaf variables gives the reversible second-order Rule-90 state matrix A=[[x+x^-1,1],[1,0]] over F2[x,x^-1]/(x^n-1). det A=1. Decompose x^n-1=(x^m-1)^(2^a) with odd m, so CRT applies. Away from x+1, eigenvectors (x,1) and (x^-1,1) diagonalize with eigenvalues x and x^-1, giving twice the degree of gcd(x^n-1,x^t-1). At x+1 the local parameter y=x+1 yields s=y^2/x; for B=A+I, ker B has dimension min(2^a,2), and B^2=sA gives 2min(2^a,2^v2(t)) at even t. For odd t the factor 1+A+...+A^(t-1) is a local unit, so the exceptional contribution is 1 at odd n and 2 at even n. Summation gives exactly the parity/gcd exponent, including the n=3 edge boundary. A^L=I and no earlier full fixed space establish exact order, and the largest invariant factor realizes that primitive period; Möbius inversion is correct. Independent GF(2) adjacency-power/rank checks used 280 (n,t) cases for n=3..16 and 1<=t<=2n+1; code inspected from verify.py, but its saved reported 1,200 cases were not substituted for this audit. Nothing about asynchronous updates or spatial symmetry quotients is proved.

## originality

PASS

PASS, best of knowledge with materially improved primary-source inspection. The reversible second-order Rule-90 recurrence is **not** new: Macfarlane (2004) RCA3, eq.(3), matches it. The materially read 2004 OA primary PDF, particularly eqs.(1)-(5), sections 5 and 6 and appendix, instead computes single-seed weights on one-dimensional arrays using matrix cellular automata, and §6 explicitly considers more complicated initial conditions future work. In the examined material no finite cyclic n-by-n all-initial-state fixed-kernel gcd census or Möbius primitive counts is supplied. The present natural finite-period quotient and one-bit odd/odd defect are not implied by those single-seed weights. Other CA orbit-census equivalences may remain in unindexed literature.

## value

PASS

PASS. A complete periodic orbit census for a natural reversible binary dynamics on the sunlet graph answers a genuinely dynamical question not reducible to the standard statement of reversibility. The exact gcd/parity formula, sharp matrix order and Möbius primitive counts distinguish odd and even graph length for all return times; a researcher studying finite reversible CA, network parity updates, or their zeta functions could use this exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
