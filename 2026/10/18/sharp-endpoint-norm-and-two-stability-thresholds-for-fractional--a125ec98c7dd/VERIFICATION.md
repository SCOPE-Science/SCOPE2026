---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The binomial coefficients w_k decay as k^(-1-alpha), justifying periodic grouping and the zero row sum. For 0<alpha<1 every nonzero residue coefficient is negative; for 1<alpha<2 the single negative coefficient shifts to residue 1, because every coefficient from k=2 onward is positive and their total alpha-1 cannot compensate w_1=-alpha. Circulant column and row absolute sums thus give respectively twice c_0 and minus twice c_1. The beta integral for |w_k| summed over k=jn or jn+1 gives both formulas; the strictly decreasing coefficient tail implies strict size increase, with the separate alpha=1 and n=2 values as stated. Uniform gamma-ratio expansion on compact order strips gives second-term coefficients alpha(alpha+1)/2 at k=jn and (alpha+1)(alpha-2)/2 after replacing k by jn+1, and the weighted remainder is summable uniformly. For n>=3, c_2>0 above alpha=1 yields a negative entry for small positive t; the row sum of the generator is always zero. The largest absolute nonzero eigenphase is alpha(pi/2-pi/n), so the signs of the real parts give exactly the stated convergence, oscillation and exponential growth by unitary Fourier diagonalization. The threshold is interior only at n>=5; at n=3 it is 3, at n=4 it is the excluded endpoint 2, and the n=2 generator and positive spectrum are covered by A=2^(alpha-1)(I-S_2).

## originality

PASS

Pass for the substantive above-one finite-size endpoint norm profile and the full comparison across order one, not for the periodization, Fourier method, or the lower-order norm in isolation. Riascos–Michelitsch–Pizarro-Medina (2020) is a previously uncredited exact-model comparison: in 0<gamma<1 their finite directed ring alias series plus entry signs and zero sums directly give the lower-order norm, including its equivalent beta series by termwise integration. Standard coefficient asymptotics then imply the lower-order correction. Their proof is for 0<gamma<=1; it does not give the change of the unique negative cyclic residue from off-diagonal entries as a group to just residue 1 above order one, the associated switched alias correction and high-order norm profile, or state the all-size positivity-versus-convergence diagram in the higher strip. The latter's phases are straightforward consequences of the known eigenvalue form, not themselves a new spectral method. Pass is for the genuine combined exact norm classification with the above-one cancellation and sharp size dependence, not a historical-priority judgment.

## value

PASS

The exact induced norm detects finite-cycle cancellation that Fourier spectral magnitudes do not describe. The above-one wrap-around loss has a different alias offset and a different second zeta term, giving quantitative size corrections for a natural periodic operator. In the stable, nonpositive range a row of the semigroup can sum to one while having a negative entry, so its absolute row sum is then greater than one: asymptotic stability does not give endpoint contractivity. The exact norm comparison and sharp boundaries quantify that distinction without needing a claim for general directed graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
