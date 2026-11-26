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

The orbit conditions b=a(1+s) and 1=a+sb uniquely force a=1/D and b=(1+s)/D, with four distinct positions and two expanding slopes. The three ordered cells have lengths (1,s,s²)/D and images respectively cell 1, cell 2, and the whole interval. The transition matrix is primitive, with generating Markov cylinders of shrinking diameter and characteristic polynomial z³−z²−z−1, giving topological entropy log λ. Starting with a uniform conditional distribution in each cell, every allowed affine transition leaves a uniform conditional distribution on its target. The resulting Markov chain has deterministic advances from cells 0 and 1 and probabilities q=(1,s,s²)/D from cell 2. Its unique stationary masses (1,s+1,D)/N give exactly the stated positive step density. The primitive chain mixes; the coding generates modulo endpoint preimages, which form a null set, and the positive density is equivalent to Lebesgue, giving a full physical basin and excluding any distinct acip. Integrating the cell midpoints against the stationary masses gives 1/2+(s+1)/(DN). Writing DN=s⁴+3s³+6s²+5s+3 gives the stated strictly negative derivative; limits at 1 and infinity give the open mean range. The entropy rate is (D/N)H(q), which expands to the displayed formula. The Gibbs reference p_j=λ^(j−3) is normalized; its cross entropy against q is (N/D)log λ, so multiplying the relative entropy by D/N gives exactly the deficit. The zero condition q=p is equivalent to s=λ, when D/s²=s. Finally (s+2)/N=1/s+O(s⁻³) and log(D/s²)=1/s+O(s⁻²), yielding the claimed decay. The supplied script was inspected, not executed; its derivative comparison uses a finite difference, while the derivative and entropy conclusions here follow analytically.

## originality

PASS

The supported distinct contribution is the exact mean calibration and the joint explicit entropy law on the specified period-four endpoint curve. General skew-tent densities, fixed-topological-entropy flexibility, and the abstract renewal relative-entropy identity are not claimed as new. Earlier originating publications are an unresolved risk where their full primary text was unavailable to this audit.

## value

PASS

The shortest itinerary here with four distinct postcritical positions supplies a natural exact Markov family inside the mean-tuning model. It calibrates a measurable statistic over a full interval of target means while holding topological complexity fixed, and locates the sole equality of physical and topological entropy as well as the zero-physical-entropy limit. The value is the concrete calibration and comparison within this same expanding family, not routine stationarity algebra in isolation or a claim about arbitrary parameter slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
