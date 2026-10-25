---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Complete proof reconstruction from frozen RESULT.md with correct domain p odd prime >=5 and nonzero arbitrary complex f,g, counting-normalized STFT. Let a,b be signal/window support sizes. Cauchy–Davenport gives at least min(p,a+b−1) nonzero translation rows, prime Fourier uncertainty gives >=p+1−r frequencies for a nonzero row of time support r, and the sum of row supports equals ab, hence s>=(p+1)|K|−ab. For all pairs except (a,b)=(1,1) and (p,p), integer monotonicity (if a+b<=p) or ab<=p(p−1) (if a+b>p) yields s>=2p. A singleton pair has s=p. In the full/full case, if every row has >=2 frequencies then s>=2p. Otherwise select one character row and define the nonvanishing shifted window ratios r_j(n). A second character row at any nonzero d generates all shifts via cocycle and primeness, forcing s=p. With one unique character row, if no remaining row has >=3 frequencies then r_1 has exactly two; r_2=r_1(n)r_1(n−1) has three distinct modes 2u,u+v,2v, all nonzero since p is odd and -1 is no p-th root; thus s>=1+3+2(p−2)=2p. Point-mass constructions attain p and 2p. A p=2 rational counterexample shows parity essential. No magnitude or approximate-support bound is asserted.

## originality

PASS

Best-of-knowledge pass. The exact second attainable cardinality for arbitrary nonzero signal/window pairs on every odd prime cyclic group p>=5 is not mathematically implied by the relevant inspected prior statements. Krahmer–Pfander–Rashkov input-support bounds leave the both-full case at s>=p; exact minimizer classifications specify s=p but do not isolate it by a growing exclusion interval. The new character-ratio cocycle and three-frequency noncancellation closes this previously unhandled class. The p=3 finite support case is expressly credited and is not a new isolated claim. Unindexed exact equivalents and inaccessible portions of separate technical reports remain risks.

## value

PASS

The second-smallest exact support cardinality of a short-time Fourier transform is a natural discrete time-frequency invariant. The result proves a sharp and increasing p−1-length forbidden band immediately above the p-coefficient uncertainty minimum uniformly over arbitrary complex signal/window pairs, resolves the structurally hard both-full-support case not handled by the standard row inequality, and provides explicit sharp endpoint witnesses. This is not merely a restatement of known minimum equality, nor a small unmotivated slice. It does not purport to control approximate/noisy support or determine all higher support levels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
