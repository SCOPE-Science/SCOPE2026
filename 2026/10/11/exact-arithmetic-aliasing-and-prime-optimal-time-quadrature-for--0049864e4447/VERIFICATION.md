---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Reconstructed from pinned RESULT.md with probability-normalized dx dt. Spatial Fourier Parseval yields integral_x |U|^4 = S^2+2 sum_{h=1}^K |B_h(t)|^2, B_h(t)=sum_{m=0}^{K-h} a_{m+h}conj(a_m) exp(2pi i(2hm+h^2)t). Continuous time selects equal m; N-point roots-of-unity sum selects N|2h(m-n). Pairing m<n and h>0 gives 4 Re(a_{m+h+r}conj(a_{m+h})conj(a_{m+r})a_m), summed over h+r<=K. With d=N/gcd(N,2), N|2hr iff d|hr; v=gcd(d,h) implies h>=v and r>=d/v. Conversely minimizing divisor v yields collision. All-ones vector has positive alias defect, proving necessary threshold K<sigma(d) even though general signed defects may be negative. Without collisions, 2S^2-sum |a|^4 <= (2-1/(K+1))S^2 by Cauchy-Schwarz, equality iff all nonzero vector entries have equal modulus (including K=0). A collision produces strict norm enlargement by all-ones. For K>=2 least odd prime p>=K has sigma(p)=p+1 and works. Bertrand gives p<2K. Any N<p and N<K has sigma(d)<=d+1<=K; even N>=K has d=N/2<K; odd composite N>=K has divisor 3<=v<=sqrt N so sigma(N)<=3+N/3<3+2K/3<=K for K>=9, with K=2..8 checked directly (only composite exception N=9,K=8). Frequency translation is phase factor plus x translation, preserving spatial Haar fourth moments. Independently checked all collision thresholds K=0..19,N=1..79, prime optimality K=2..199, and independently enumerated all momentum/time congruence quartic terms for K=0..7,N=1..18 with complex coefficients; finite tests corroborate, do not prove the general result.

## originality

PASS

Qualified best-of-knowledge originality. Prior continuous parabolic fourth-moment orthogonality (Bourgain/Zygmund) is not new and directly supplies the continuum baseline; rational Talbot quadratic Gauss sums and continuously integrated Strichartz estimates do not imply arbitrary-complex-coefficient uniform temporal quadrature for all moduli, the signed alias polynomial, factor-minimization cutoff, or optimal least odd prime grid. Full published Resultary fourth-moment and chirp-overlap claims are distinct objectives. A simple derivation from classical ingredients does not alone mean a pre-existing theorem states the global arithmetic classification, but a historical or stronger generic finite quadrature result could cover it; see risks.

## value

PASS

A canonical discrete Schrödinger/parabola fourth-power measurement becomes exactly evaluable from a finite uniform time grid. The claim completely classifies all bandwidths and moduli by an intrinsic divisor-pair-sum invariant, identifies signed alias interactions and failed-grid witnesses, settles the sharp baseline constant and equality cases, and proves the surprisingly linear minimum sampling budget, the least odd prime >=K, versus naive quadratic temporal frequency range. This is a natural general exact sampling classification (not an arbitrary small table) with plausible use in finite-time diagnostics. Classical Fourier orthogonality is easy, but the optimal sample-count/divisor threshold across every integer modulus is an independent meaningful arithmetic synthesis; it does not assert novelty of Parseval, Bertrand or the continuous L4 bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
