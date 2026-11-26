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

Ordering the adjacent sides a>b gives a>c>b by the cosine law, and t=(a+c)/b>2 uniquely recovers the reduced m/n. The integer numerators are (m^2-n^2,n(2m-n),m^2-mn+n^2); parity excludes a common 2, and any odd common prime must divide both 2m-n and 3n^2, so can only be 3. When 3 divides m+n, C=(m+n)^2-3mn has 3-adic valuation 1. The perimeter is (m+n)(2m-n)/d, with the two factors sharing at most 3 and summing to 3m. For d=1 a square would make both factors coprime squares summing to 0 mod 3, impossible. For d=3 divide both factors by 3 to get coprime r,s, r<s<2r. Valuations of 3rs force the 3-times-square/square split with the other coordinate prime to 3; conversely this gives 3 not dividing r+s and gcd(r+s,2r-s)=1. The primitive side formulas and injectivity follow, and the equilateral primitive triangle has perimeter 3. Each uv<=Y wedge has area Y log(2)/4 by the ratio substitution; slicing on the unrestricted coordinate replaces length by (2/3)length+O(1) for the restricted coordinate and gives O(sqrt(Y)+1) total discrepancy. In the coprimality Möbius sum, 3-divisible divisors vanish, the remaining main terms have density (2/3) product_{p!=3}(1-p^-2)=3/(4 zeta(2)), and the errors for d up to O(sqrt(Y)) sum to O(sqrt(Y) log(2Y)), with tail O(sqrt(Y)). Both wedges and Y=sqrt(X)/3 then give 3 log(2)/(4 pi^2) and the stated error. My independent reduced-conic scan, r,s scan and direct perimeter-divisor reconstruction agree through 10^7 (branches/independent_small_replays.py triangle): counts 1,1,6,16,54,165 at the six recorded bounds, with distinct triples sharing perimeter 736164. These are finite checks, not the asymptotic proof.

## originality

PASS

The underlying unrestricted parameterization is known. In particular, the two square-factor families follow by elementary filtering of Zimhoni's exact classification, and should not be credited as a stand-alone new unrestricted classification or a hard consequence. The distinct supported contribution of the composite finding is the square-perimeter triangle count with its arithmetic leading constant and error term. The closest power-perimeter counting result treats a different angle and a different local density. Earlier potentially relevant printed texts remain incompletely checked.

## value

PASS

Perfect squares are a natural sparse restriction on a classical norm-form family. The explicit count with a local coprimality factor and a power-saving discrepancy estimates actual triangles rather than possible perimeter values. This remains mathematically useful after crediting the unrestricted parameterization and the elementary derivation of the square families from it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
