---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the zero-at-target entrance hitting column H_j, first-step analysis gives (I−P)H_j=m off the target. Multiplying by the embedded invariant row nu forces the exceptional component to be m_j−(nu·m)/nu_j. Weighting columns by pi_j=nu_j*m_j/(nu·m) therefore gives a harmonic vector, constant by irreducibility. Conditioning on the initial stationary interval biases the joint duration–mark law by w/m_i; averaging the residual length and the destination gives r_i=u_i/(2m_i) and q_ik=b_ik/m_i. After the next jump the process starts on a fresh entry. In the target-weighted difference the sum over j other than i is K−pi_i*H_ki, so the row-sum-zero difference q_i−P_i yields the stated negative sign on the marked term. For the star witness the conditional Gamma second moments are 8/5 and 72/5, giving mixture second moment 8. The common H rows are (0,6,5),(1,0,6),(2,8,0), with pi=(4,1,2)/7. Swapping the Gamma marks changes q_12 from 1/4 to 3/4, so the state-1 defect is respectively −1/7 and +1/7 while the other defects vanish. Two states without self jumps offer no alternative exit mark; with marginal SCV one the residual term also vanishes. This proves exactly the stated minimality.

## originality

PASS

The entrance constancy and general residual-life first-step machinery are established. The distinct supported result is nonidentifiability at a stationary observation from identical entire unmarked holding laws, transition matrix, stationary occupancy and entrance mean hitting matrix, with an explicit minimal, unit-SCV pair and opposite signed defects. No inspected statement establishes this matched-observables obstruction.

## value

PASS

The pair tests whether quantities available without linking each holding interval to its destination determine a natural network hitting summary. It gives failure even when full unmarked holding laws, not merely their moments, agree, and removes the usual mean-residual-life explanation by matching unit SCV. The sign reversal and two-state boundary identify precisely why that reduction fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
