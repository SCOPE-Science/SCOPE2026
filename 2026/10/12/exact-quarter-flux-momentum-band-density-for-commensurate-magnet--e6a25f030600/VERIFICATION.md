---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For every coprime p,q>=1, s=p+q, ell_2=2pi p/s and ell_3=2pi q/s, and A=1/4 modulo 1/2, source Eq.(34) becomes the periodic sign condition -cos(st)sin(pt)sin(qt)>0 after t=2pi k/s. At u=t/pi, the period is u∈[0,1), and sign parity for the cosine and sines gives the mutually exclusive regions x={su}<1/2,y={pu}>x or x>=1/2,y<=x. In the s cells u=(j+x)/s, residue pj mod s permutes 0,...,s-1 by gcd(p,s)=1. The inequality y>x is qx<r<s-px except at finitely many zero/boundary points, and N(x)=s-1-floor(px)-floor(qx). The exact measure P=(1/s)(∫_0^(1/2)N+∫_(1/2)^1(s-N))=1/2-(D_p+D_q)/s, where D_n=-n/4 for even n, and D_n=-n/4+1/(4n) for odd n; hence P=3/4-[1_(p odd)/p+1_(q odd)/q]/[4(p+q)]. For odd p,q this reduces to 3/4-1/(4pq), for exactly one odd r to 3/4-1/[4r(p+q)]. Because the leading periodic trigonometric product is not identically zero and has finitely many roots per period, the imported source uniform high-energy O(k^-2) correction changes the limiting sign-density only in arbitrarily small neighborhoods of its roots. This passage uses the original paper as an asymptotic premise; no full secular-condition rederivation is claimed. An independently implemented exact rational root-partition checker verified all 1547 ordered coprime pairs 1<=p,q<=50 and 160 independent parity integrals, agreeing with the analytic proof. Boundary p=q=1 gives 1/2 and p=1,q=2 gives 2/3. The finite checks are corroboration, not infinite proof.

## originality

PASS

Qualified best-of-knowledge originality: the October 4 published exact quarter-flux adjacent-pair theorem settles the entire p/q=m/(m+1) subfamily, so no novelty credit is given to it. Its full RESULT explicitly says no formula for arbitrary coprime rational p/q; the current theorem covers every positive coprime p,q by a general residue-permutation/floor-integral proof, including nonadjacent pairs such as 3/5 with P=11/15. The same mathematical model 2022 primary article supplies Eq.(34) and numerical commensurate Fig.8 but explicitly says that a commensurate closed form was not obtained. A separate October 4 all-p/q parity anomaly is nonmagnetic: its leading factor is sin(pt)sin(qt), whereas the magnetic quarter-flux problem includes -cos((p+q)t) and has different values (at 3/5: 8/15 nonmagnetic versus 11/15 magnetic). Generic-length universality does not cover rational dependence. Searches of Resultary and public scientific literature found no full all-coprime covering result; this is not an exhaustive priority claim.

## value

PASS

The all-coprime magnetic commensurate momentum-band density is a natural spectral invariant singled out as an unresolved regime in the original paper (Eq.34 and numerical Fig.8). The published October 4 adjacent-pair theorem settles an infinite but thin subfamily; the present exact parity-controlled formula covers every coprime pair without adjacentness, providing a complete rational-length classification at the distinguished quarter flux and explaining numerical dips, the exact symmetric value 1/2 and convergence toward the irrational value 3/4. This fills a mathematically motivated gap and is not merely evaluating a randomly chosen pair, a known table or a renaming of a prior result. The derivation uses new general residue/floor counting; it is short but not an unsupported significance claim. Value is confined to that full commensurate classification, not a general all-flux spectral theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
