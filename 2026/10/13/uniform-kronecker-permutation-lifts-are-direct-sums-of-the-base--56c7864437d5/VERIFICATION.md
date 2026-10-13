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
`artifacts/verify.py` uses only the Python standard library.

The script reconstructs the source example
\[
A=A\!\left(\operatorname{Cay}(\mathbb Z_{12},\{1,2,6\})\right)
\]
and exhaustively checks all \(2^{12}\) binary vectors. It obtains rank \(10\), dimension \(2\), minimum distance \(8\), and
\[
W_C(z)=1+3z^8.
\]

For the three-cycle permutation matrix \(P\), it constructs
\[
H=A\otimes P
\]
and checks both stages of the exact equivalence:
\[
H(I_{12}\otimes P^T)=A\otimes I_3
\]
and, after the perfect shuffle,
\[
A\otimes I_3\sim I_3\otimes A.
\]

The script computes \(\operatorname{rank}_{\mathbb F_2}H=30\), so the lifted code has exactly \(2^6=64\) words. It enumerates the \(4^3=64\) direct-sum words, transports each one through the verified coordinate permutations to a word of \(\ker H\), and checks every syndrome. The resulting enumerator is
\[
(1+3z^8)^3.
\]

Finally, it builds the Tanner graphs directly. The base Tanner graph is connected; the lifted graph has exactly three connected components, each isomorphic in size to the base component.

The replay is finite and exhaustive for the stated example. The general theorem is proved algebraically rather than inferred from the finite check. Successful replay prints `VERIFY_OK`.
