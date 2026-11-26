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

For nonnegative degree bound D, (n+k+1)^D≤(n+1)^D(k+1)^D and sup(k+1)^D/b^k is finite. Dividing the geometric decomposition by b^k a_n gives ratio 1+O((n+1)^D/b^n) uniformly in k≥1. A legal append also gives ratio a_(n+k)/(b^t a_n) in [1,1+1/a_n); their quotient is the discrete power b^(k−t) and must be 1 uniformly on the tail. For a late index m on an infinite walk, concatenated blocks to any later index n keep a_n/b^(n−m) in [a_m,a_m+1). Its limit is Ab^m, so the residual lies in the CLOSED interval [−1,0]. On each unbounded residue progression every nonconstant polynomial eventually leaves that interval, and a constant outside it never enters. This pruning applies even to unbounded jumps and uniformly over walks once m is large. Between good residues the difference is precisely c_s−b^k c_r, integral on the positive integer tail. Finite directed cycles are equivalent to infinite capped paths, and every directed cycle lifts by positive jumps, including self-loops. Any good residue has the legal loop k=P, d=(1−b^P)c_r, explaining the cap P and bottleneck formula (empty minimum infinite); jumps through increasing multiples of P would also give an actually unbounded-length walk if desired. In the period-four example the legal unit edges 0→1→2 cannot close, whereas 2→0 with length 2 has d=1. The frozen finite checker was inspected only; the proof covers unrestricted parameters and does not depend on it.

## originality

PASS

There is exact earlier Resultary coverage of the A=1, constant-integer periodic subcase, including the cycle idea and an explicit gap formula. Credit that work, not the frozen record, for that case. The supported advance is the rational-amplitude, polynomial-by-residue classification and proof of uniform tail synchronization and pruning under those broader assumptions. The prior finite-residue proof starts with a bounded periodic integer correction and does not itself prune nonconstant polynomials or classify fractional good corrections.

## value

PASS

The class captures a simple dominant base root accompanied by arbitrary root-of-unity polynomial modes, a natural dependent case not decided by multiplicative independence. The infinite-prefix argument shows why even unrestricted jumps cannot save an infinite path through nonconstant residue corrections. The criterion then gives an exact smallest finite cap for the whole stated class, rather than just sufficient examples or a nonsharp existence bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
