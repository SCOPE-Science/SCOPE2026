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

For the row generator use pi_j=s_j/S and Pi=1 pi. The forward travel times satisfy Qm_j=pi_j^(−1)e_j−1; centering against pi produces G=(Q+Pi)^(−1)−Pi. Expanding the resolvent on the complement gives T=I+12G/h+O(h^(−2)); the stationary sector is identity. Pairing m_ij+m_ji=S and subtracting all unordered pairs from the adjacent pairs gives the claimed weighted sum for n≥4. For n=3, putting a=s_(j−1), b=s_(j+1), the centered term gives G_(j−1,j)=s_j(a s_j−b²)/S²; sum zero and simultaneous equality force homogeneous rates. For n=2 the nonstationary scalar lies strictly between zero and one for h>0 and Pi is positive. Independently checked homogeneous n=3 by using z²+3xz+3x²=0 on the two nonstationary modes z=x(omega−1): the identity (2−x−z)(2(x+1)+z)=x²+2x+4 reproduces the stated positive row. For n=4 evaluate R at 0, −2x, (−1±i)x and invert that four-point Fourier transform. Put A=x²+3x+3, B=x⁴+6x³+18x²+36x+36; R(−2x)=1−6x/A and Im R((−1+i)x)=6x(6−x²)/B. The forward entry becomes 3x[B+2A(6−x²)]/(2AB)=−3x(x⁴−24x²−72x−72)/(2AB); the other three are the stated positive rational entries. Descartes and endpoint signs give one positive root, and h=0 is identity. Replay: frozen RESULT.md proof and the identities here. The frozen verify.py was inspected, not executed; its finite checks and absent attestation/Lean status are not used as universal evidence.

## originality

PASS

The rate-labeled theorem and weighted obstruction are distinct from the closest located manuscripts and catalogue results. The later uniform-cycle record substantially overlaps the homogeneous claims, including the exact four-cycle quartic; this overlap is disclosed and is not used to establish priority or broad uniqueness. The finding does not claim novelty for Padé positivity failure or group inverses.

## value

PASS

Single-step positivity is a meaningful Markov integrator property distinct from conservation. The result classifies a natural family for all positive rates, quantifies an unavoidable sign through missing undirected edges, and gives an actionable exact timestep cutoff in the first homogeneous failing size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
