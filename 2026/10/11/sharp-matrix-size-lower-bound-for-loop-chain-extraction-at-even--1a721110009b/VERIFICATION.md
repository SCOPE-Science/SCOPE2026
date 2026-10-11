---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The focal arXiv full text was inspected at the finite-level theorem and its proof. The source sets \(r=2m-1\), \(N_m=\lceil2m/3\rceil\), \(v_k=1+\lfloor k/3\rfloor\), and \(F_k=E_{v_{k-1},v_k}\). Its torus Fourier coefficient leaves precisely the permutations \(\pi\) satisfying \(\pi(j)\equiv j\pmod2\), and the selected \((1,N_m)\)-entry is nonzero only for the identity ordering.

For the new converse within the loop-chain architecture, suppose a vertex carries at least three loop labels. Two labels have the same parity. Swapping those two labels is therefore an allowed parity-preserving permutation, and because both corresponding matrix units are the same loop \(E_{s,s}\), the matrix product is unchanged. Hence parity isolation forces at most two loops at each vertex.

There are exactly \(n-1\) forward labels and \(r-(n-1)\) loop labels. Therefore
\[
r-(n-1)\le2n.
\]
With \(r=2m-1\), this is \(2m\le3n\), hence \(n\ge\lceil2m/3\rceil\).

The source construction attains this bound. No finite computation, numerical search, or external certificate is used. The verification does not establish global optimality of the contractivity level outside the stated loop-chain extraction architecture.
