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

XOR of adjacent letters gives y_(3m)=0, y_(3m+1)=1-y_(2m), y_(3m+2)=1-y_(2m+1). Summing exactly N-1 terms gives E(n)=-E(h(n))+c(n), with h(3m)=2m, h(3m+1)=h(3m+2)=2m+1, and c by residue (-1,0,-2), including E(1)=0 through its self-map. Composing gives the offsets c(n)-c(h(n))=(0,0,-2,1,1,-1,-1,2,0) for residues modulo nine. The bound h(n)-1<=2(n-1)/3 yields h^2 contraction by 4/9, so after at most 1+floor(log_{9/4}(n-1)) two-step reductions the distance is an integer less than one. Residue seven gives E((9u+1)/4)-E(u)=2 if u=3 mod 4. Since 5a_j+1=4^(j+epsilon_j) with even exponent and 5g(u)+1=(9/4)(5u+1), the first j inputs are successively legal modulo four, and the last is b_j. The endpoints are positive integers with a_j<b_j<9^j; their difference of 2j entails at least one absolute discrepancy of j. Taking j=floor(log_9 N) and dividing by five proves the two-sided bound as written. The displayed logarithmic quantity is a PREFIX COUNT discrepancy, not the absolute error of the normalized empirical frequency. Independent direct word generation and prefix counting through N=106288 confirmed all steps and gaps 2,4,6,8,10,12 for j=1 through 6. This is finite corroboration, not the basis for the universal proof; no frozen script was run.

## originality

PASS

Credit the explicit all-j repunit contrast for this normalized word. The nine-to-four Toeplitz structure and density are known, and a distinct indexed logarithmic-discrepancy result covers the sharp order even after translating to the same auxiliary word. The exact repunit endpoints and their +2j gap are not the CRT endpoints or gap of that result. The order alone would not distinguish the frozen claim from that indexed work.

## value

PASS

Adjacent changes in this one-sided rational-base word are a natural observable with established limiting density but nontrivial arithmetic fluctuations. The exact amplification on specified repunit endpoints gives reproducible deterministic witnesses at every scale and explicit uniform bounds, beyond relying on an empirical slope or on the known frequency limit. In light of the order-level overlap, the precise progression and its additive law are the independently useful content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
