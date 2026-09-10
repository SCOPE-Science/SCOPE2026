# Certified momentum-preserving exact-resonance census for the S+={1,2} KdV Birkhoff program

## Context

Kappeler–Montalto (Comm. Math. Phys. 2021) prove O(eps^-2) orbital stability of
periodic multi-solitons (finite-gap tori) of KdV under general semilinear
Hamiltonian perturbations f(x,u), via Birkhoff coordinates plus a normal form
to order 3. Their third Melnikov set Pi_gamma(3) carries a derivative loss
`<j1>^2<j2>^2<j3>^2`. Remark (v) notes x-independent densities f=f(u) preserve
momentum and improved stability time is future work; remark (iv) warns
fourth-order almost-resonances bound the method in generality. The admitted
target (eps^-4 via momentum-restricted loss-free divisor) and preset fallback
(one-step tame eps^3 remainder) both require the loss-free momentum-restricted
divisor. Routes A–C were attempted and BLOCKED (see target_exit.json); the
census below is the certified obstruction / divisor table that emerged from the
bounded recovery enumeration, and is exactly the machine-checkable input the
fallback's future_retrieval_use clause requests.

## Definitions

Work in zero-amplitude (linear) frequencies with (2pi)^3 factored out:

- tangential weights 1^3, 2^3; divisor D_0(l,j) = l_1 + 8 l_2 + sum_k j_k^3,
- momentum M(l,j) = l_1 + 2 l_2 + sum_k j_k = 0,
- S_+ = {1,2}, normal modes j in S^perp = Z \ {-2,-1,0,1,2},
- Kappeler–Montalto pair exclusion j_k + j_m != 0 for the cubic class
  (including diagonal k=m, i.e. j_k != 0, automatic for normal modes).

Canonical means j-sorted; nontrivial (cubic) means the pair exclusion holds;
non-integrable (quartic) means l != 0 or the quadruple is unpaired.

## Result

Theorem (certified census).

1. (Nontrivial cubic exact resonances.) (l;j) = (-3,0;-5,4,4) and
   (3,0;-4,-4,5) satisfy D_0 = M = 0 with all j in S^perp and no vanishing
   pair sums. They are minimal in (|l|_2, max|j|) lexicographic order among
   nontrivial solutions in the |l_1|,|l_2| <= 8 window (next competitors
   (0,+-3;...) have max|j| = 10). Hand check: -3+(-125+64+64) = -3+3 = 0,
   -3+(-5+4+4) = 0; 3+(-64-64+125) = 3-3 = 0, 3+(-4-4+5) = 0.
2. (Cubic census.) In |l_1| <= 60, |l_2| <= 30, j in [-12,12]^3 cap S^perp:
   exactly 166 canonical (j-sorted) exact classes, of which 106 are
   nontrivial (satisfy the pair exclusion).
3. (Non-integrable quartic exact resonance.) (l;j) = (-1,0;-9,-5,7,8)
   satisfies D_0 = M = 0 with l != 0 (|l|_2 = 1, the smallest possible nonzero
   value). Hand check: cubes -729-125+343+512 = 1, l-part -1, D_0 = 0;
   M = -1+(-9-5+7+8) = 0. No pair of j's sums to zero.
4. (Quartic census.) In |l_1| <= 12, |l_2| <= 8, j in [-10,10]^4 cap S^perp:
   exactly 130 canonical exact classes, of which 94 are non-integrable
   (l != 0 or unpaired).
5. (Infinite-family lemma.) P(l) := D_0 on the pair-cancel line equals
   P(l_1,l_2) = 6 l_2 - L^3 + L with L = l_1 + 2 l_2. Since
   L^3 - L = L(L-1)(L+1) is always divisible by 6, every integer L yields an
   integer (l_1,l_2) = (L - 2 l_2, (L^3-L)/6) with P(l) = 0; infinitely many.
   These pair-cancel triples are excluded from the divisor class by
   j_k + j_m != 0; the point of (1)-(2) is that the exclusion is insufficient.

Interpretation: the uniform loss-free bound |D_0| >= gamma<l>^{-tau} is FALSE
at linear level on the momentum-restricted class, and the quartic homological
divisor needed for a second Birkhoff step vanishes on non-integrable
momentum-preserving quadruples. Audit note: the cubic witnesses are in fact
globally |l|_2-minimal over unrestricted j (proved by finite divisor
enumeration — for fixed l, P(l) = 3abc with a+b+c = 2J forces each factor to
divide P/3), so the stated window-restricted minimality is conservative.

## Proof / evidence

All statements are exact integer arithmetic, stdlib only:

```
python3 output/artifacts/certify_obstructions.py   # -> VERIFY_OK
```

producing output/artifacts/obstruction_certificate.json (C1–C4). The key
identity is sum j^3 = -L^3 - 3(j_1+j_2)(j_2+j_3)(j_3+j_1) with
L = -sum j = l_1 + 2 l_2 under M = 0, which makes the enumeration a finite
exact check. The independent audit replayed the script (VERIFY_OK),
hand-checked all witnesses, and reproduced the 166/106 and 130/94 counts with
a differently-structured brute-force loop.

## Limitations

- Linear (zero-amplitude) analysis only; finite-amplitude nonlinear frequency
  corrections are not computed. No eps^-4 stability, no loss-free analytic
  divisor bound, no tame remainder inequality, and no measure estimate are
  claimed.
- Minimality as stated is certified within the stated windows (audit
  strengthens the cubic case to global |l|_2-minimality); window counts are
  cutoff-dependent by construction.
- Finite-amplitude detuning could remove the exact zeros, so "obstruction"
  means the uniform loss-free bound and the stated hypothesis set fail at
  linear level, not that eps^-4 is unachievable by a nonlinear transversality
  plus 4th-Melnikov program.

## Reproducibility

- Script: output/artifacts/certify_obstructions.py (stdlib only).
- Certificate: output/artifacts/obstruction_certificate.json (C1–C4).
- Replay: python3 output/artifacts/certify_obstructions.py -> VERIFY_OK.

## References

- T. Kappeler, R. Montalto, On the Stability of Periodic Multi-Solitons of the
  KdV Equation, Comm. Math. Phys. 385 (2021), 1871–1956. PMC8550510.
  (Thm 1.1 O(eps^-2); Pi_gamma(0)–(3) with lossy Pi_gamma(3); remarks (iv)–(v);
  Lemma 8.3 Euler FLT n=3.)
