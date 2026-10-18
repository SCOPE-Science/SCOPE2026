---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For cube-free n and sigma_{-2}(n), prime p permits exactly 1, 1+p^-2, 1+p^-2+p^-4. Euler's product gives W=zeta(2)/zeta(6)=315/(2*pi^4). For prime p>=29, Nagura's strict next-prime <6p/5 bound implies sum_{q>p} log(1+q^-2+q^-4) > (25/11)/p^2 > log(1+p^-2); seven exact rational finite prime-tail products handle 5<=p<=23. This three-choice tail dominance recursively fills the entire log interval, so the p>=5 factor closure is [1,T], T=9720/(91*pi^4). The nine local p=2,3 translated intervals merge, by rational Archimedean pi bounds, into exactly [1,T], [10/9,120/pi^4], and [5/4,315/(2*pi^4)], separated by two strict gaps. Cube-free local exponent probabilities (4,2,1)/7 and (9,3,1)/13 yield component conditional densities 36/91,16/91,39/91 and absolute densities divided by zeta(3). Independent exact-fraction verification checked seven small-prime witnesses, all nine interval order/overlaps/gaps, and density identities. Finite products and illustrations are not the unbounded prime proof, which explicitly invokes Nagura.

## originality

PASS

Defant's foundational restricted-domain paper treats generalized divisor-function ranges with exponent cutoffs and asks for exact component counts. Sanna’s prior unrestricted t=-2 theorem does give three components and densities, but its prime-power domains include arbitrarily high exponents and its numerical endpoints/densities differ. A coverage comparison of the actual interval bounds shows the unrestricted closure theorem cannot force the cube-free restricted range to fill three intervals; this needs the new restricted-prime-tail argument. Related Resultary entries concern unitary or alternating divisor functions with different local factors. No indexed exact cube-free triple and weights were located; priority remains best of knowledge.

## value

PASS

Determining the *complete* topological range invariant and each natural density for an exponent-cutoff-two divisor function directly answers a published range-component problem. The restricted prime-tail interval lemma is substantive and cannot be supplied by a finite sample or by unrestricted image density. Exact three components and rational cylinder probabilities are mathematically motivated by the canonical cube-free domain and reciprocal-square weight, not arbitrary parameter sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
