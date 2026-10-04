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

The verifier works locally at one world because, on the discrete cover base, the modal conditions factor pointwise.

For
\[
1\le n\le4,
\]
it enumerates all antichains of the Boolean lattice
\[
\mathcal P(W)
\]
and obtains
\[
M_1=3,\quad
M_2=6,\quad
M_3=20,\quad
M_4=168.
\]

For
\[
1\le n\le3,
\]
it enumerates every raw family of modal covers and computes the induced semantic upset
\[
\{X:\exists\beta\in\mathcal C_w,\ \beta\subseteq X\}.
\]
The number of distinct CM behaviors agrees exactly with the corresponding Dedekind number, and the minimal members of each nonempty behavior form the unique irredundant modal-cover antichain.

For SL, it directly filters raw cover families by modal inclusion and verifies exactly three induced behaviors per world.

For PLL, it additionally requires the identity cover and checks modal transitivity, obtaining exactly two induced behaviors per world.

For finite CK-box, it enumerates every nonempty raw cover family through
\[
n=3,
\]
checks modal confluence, verifies that the total intersection belongs to the family, and confirms
\[
\mu(X)=1
\quad\Longleftrightarrow\quad
K_w\subseteq X
\]
for the least cover \(K_w\). Exactly
\[
2^n
\]
local behaviors occur.

The global counts are products of the independent local choices:
\[
M_n^n,\qquad
3^n,\qquad
2^n,\qquad
2^{n^2}.
\]

The script prints `VERIFY_OK`.

## Limits

The finite replay corroborates the structural proof. The CK-box theorem for arbitrary finite \(n\) follows from finite downward directedness, not from extrapolation. No statement is made for infinite CK-box cover families or non-discrete local cover systems.
