---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Using the source's equivalence, a crystal pair gives an integer \(w\) with \((x+y-1)^2=wxy\), where \(x=(a+1)/2\) and \(y=(b+1)/2\). Any common divisor of \(x,y\) divides 1 after reduction of this equation, so \(\gcd(a+1,b+1)=2\). For \(d=\gcd(a,b)\), oddness gives the inverse \(h=2^{-1}\pmod d\) and \(x\equiv y\equiv h\). The conic forces \(w\equiv0\pmod d\). The published recurrence for consecutive solution terms then propagates the congruence \(h\) backwards because \(u_{j-2}=(w-2)u_{j-1}+2-u_j\equiv2-3h\equiv h\pmod d\). Reaching \(u_1=1\) gives \(h\equiv1\), incompatible with \(2h\equiv1\) unless \(d=1\). Hence every crystal factorization is unitary, and with exactly two prime divisors only one nontrivial unordered unitary split exists.

## originality

PASS

The complete primary paper was inspected. It classifies crystal pairs by the conic/recurrence and explicitly ends by conjecturing uniqueness of crystal components, saying a proof or counterexample does not follow easily. It does not state either coprimality conclusion. Targeted literature and Resultary searches found no equivalent coprime/unitary component theorem. The audited modular recurrence argument therefore supplies a new structural restriction and proves the source conjecture on the full two-prime-support stratum.

## value

PASS

Coprimality of every crystal component pair is a reusable structural invariant, and it settles the published uniqueness conjecture for all crystals supported on exactly two primes. This materially narrows any future counterexample search to at least three distinct prime factors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
