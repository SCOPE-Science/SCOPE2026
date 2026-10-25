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

Define alpha=1+sqrt2, a=alpha^{-2}=3-2sqrt2,z=a^n,t=(-1)^n. The exact Binet/binomial expansion S_n=64 z^2[c0+c1 t z+c2 z^2+H] with c0=(1-a^2)^-1,c1=4/(1+a^3),c2=10/(1-a^4) yields inverse coefficients A=-1/4+3sqrt2/16, B=-1/5+sqrt2/10, C=67sqrt2/1200. The proof bounds |H|/c0<21z^3 for n>=3, and remainder |S_n^-1 -(A z^-2+B t z^-1+C)|<180 A z, giving |S_n^-1 -T_n-C|<0.017. As 0.078<C<0.080, 0<S_n^-1-T_n<0.1 for n>=3. Direct rational Pell-growth enclosures handle n=1 and n=2; (-1)^n(2P_2n-Q_2n) modulo 5 and P_4n,Q_4n modulo 4 yield T_n fractional parts 0.9,0.5,0.1 in the three classes, so floors agree without a boundary crossing. Independently formed exact rational tail enclosures for n=1..16 confirming 0<R_n-T_n<0.1 and residues; these are finite checks only.

## originality

PASS

Li–Yang–Yuan (2025) gives the SAME leading fourth-power Pell inverse-tail asymptotic T_n+C+o(1); by the proved finite residue obstruction it ALREADY implies floor equality for sufficiently large n. The surviving contribution is explicit strict (0,0.1) uniform residual for every n and complete all-index floor equality, neither a consequence of an unspecified o(1) threshold for the initial indices.

## value

PASS

The all-index bound settles the natural exceptional-small-index portion of a published Pell reciprocal fourth-power floor problem. The period-three fractional obstruction makes the global 0.1 threshold mathematically relevant and enables an exact algorithm-free floor at every index, not just a routine term of an expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
