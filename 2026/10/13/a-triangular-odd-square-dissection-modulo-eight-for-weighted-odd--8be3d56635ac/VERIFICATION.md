---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Odd parts can repeat, even parts cannot, and S(0)=1. Requiring odd parts through 2m-1 and excluding 2m+1 gives the factor q^(m^2)(1-q^(2m+1)); weighting by 2m+1 and telescoping gives F=(E(q^4)/E(q)) Theta(q). Jacobi and Gauss give F=Psi(-q) R^2, with R=E(q^2)^3/(E(q)^2 E(q^4))=prod_{a>=1}(1+2q^a/(1+q^(2a))). For R=1+2U, each positive-index coefficient of U modulo 2 is the number of odd divisors of that index, which is odd exactly when the odd part is a square. Frobenius gives U^2=U(q^2) modulo 2; in U+U(q^2) the indices with positive 2-adic exponent cancel. Hence R^2=1+4 sum_{s>0 odd} q^(s^2) modulo 8. At each coefficient the sign in the correction times 4 disappears modulo 8, giving the stated formula and valuation alternatives including the constant term. If C(n)>0, 8n+1=(2j+1)^2+8s^2 has even valuation at each prime p=5 or 7 modulo 8, since -8 is a nonresidue there and any divisibility forces both coordinates to be divisible by p. For each such prime the density of even valuation is (1-1/p) sum_{a>=0}p^(-2a)=p/(p+1); truncation errors are bounded by the density of divisibility by a high p-power, and CRT multiplies densities for finitely many primes. Their product tends to zero by divergence of the prime reciprocal sum. Triangular indices also have density zero, so 8 divides S(n) on a set of natural density one. The frozen verification notes, output and code were inspected but the code was not run. A separate direct enumeration checked n=0..24 over 3,721 admissible partitions without mismatch. The finite checks do not prove the congruence or density.

## originality

PASS

The exact weighted statistic and generating function are established prior work. The supported distinct claim is the coefficientwise mod-8 dissection, the nontriangular valuation criterion, and the resulting density-one divisibility for this specific partition class. Nearby odd-mex congruences and overpartition residue laws do not coincide with this statistic. The conclusion is best-of-knowledge after bounded comparisons, not inferred from an empty search.

## value

PASS

The result explains every residue modulo eight of a named partition statistic in terms of two sparse families and separates the exact valuation-two cases from divisible-by-eight cases. Density-one divisibility then follows from a distinct arithmetic obstruction. This is more informative than an isolated congruence progression or an empirical frequency and does not depend on novelty of the original generating function.

The dated certificate retains the supplied scientific assessment, sources and limitations.
