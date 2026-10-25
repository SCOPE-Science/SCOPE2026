---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Over algebraically closed characteristic 3 consider standard functions y³-y=sum_{p=∞,0,1}(A_p q_p(x)²+B_p q_p(x)), all A_p!=0 and q∞=x-1/2, q0=1/2-1/x, q1=-1/2-1/(x-1). Three poles of order 2 give via Riemann–Hurwitz 2g-2=-6+3*2*3=12 => g=7 and Deuring–Shafarevich p-rank 4. If two inequivalent separable degree-3 rational subfields existed in the genus-seven function field their compositum (degree prime) would give a birational (3,3) curve in P1×P1 of arithmetic genus 4, contradiction. Hence the Artin–Schreier quotient is intrinsic to unmarked curves. Normalizing three branch poles leaves Möbius S3 plus scalar F3*={±1}; any additive correction h(x) with a pole would yield a pole of order >=3 in h³-h, contradicting the normalized order-two right-hand sides, so h constant and absorbed. The centered q_p transform under odd permutations by a common negative sign. Thus A triple is permuted, B triple is signed-permuted, scalar -1 negates both. For V with rows (1,A_i,A_i²), interpolation determinants T_j=det(V with column j replaced by B), S3-fixed field is k(e1,e2,e3,T0,T1,T2), since unordered A roots and Cramer interpolation reconstruct B. The remaining involution negates e1,e3,T1 but fixes e2,T0,T2, so the fixed field is purely transcendental k(e2,T0,T2,e1²,e1e3,e1T1) on open A∞A0A1 det(V) e1!=0. Generic orbit reconstruction proves these invariants separate unmarked curve isomorphism classes and establish rationality of the six-dimensional moduli locus. Independent SymPy computation of the six-by-six Jacobian gives 2*prod_{i<j}(A_i-A_j)^3*(A0+A1+A2)^3, nonzero also mod3. The computation supports separable independence, not the genus/pencil or field-identification proof.

## originality

PASS

The primary Artin–Schreier invariants paper specifically leaves the modular equal-three-double-pole invariant RING calculation unfinished; this claim instead gives full rational invariant FIELD and unmarked moduli reconstruction by six explicit quantities, not the stronger ring.

## value

PASS

The three-double-pole characteristic-three locus is natural, dimension six, and already identified in primary literature as difficult for modular invariant-ring computation. A full birational field presentation with six algebraically independent polynomial invariants that generically reconstruct UNMARKED curves is a substantive natural moduli classification; it supplies rationality and usable explicit coordinates without falsely claiming to solve the harder ring problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
