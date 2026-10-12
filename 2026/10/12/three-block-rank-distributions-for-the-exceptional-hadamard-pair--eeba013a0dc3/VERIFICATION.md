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

For \(H^{1,1,1}\), it encodes the four local function spaces printed in the primary source over the monomial basis
\[
\epsilon,a_1,b_1,c_1,d_1,e_1,a_1d_1,b_1d_1
\]
and performs exact binary row reduction on every union of local spaces.

For \(\bar H^{2,0,0}\), it reconstructs the code from
\[
(x_1,x_2)\in\mathbb Z_8^2
\]
and the additive coordinates \((1,j)^{\mathsf T}\), \(j\in\mathbb Z_8\), using Carlet's Gray map. It checks the Hadamard weight distribution, binary span rank, source block labeling, all six pair ranks, and all four triple ranks.

The script then starts from these exact base histograms and iterates
\[
P_{C^+}(j)=b\,\mathbf 1_{\{j=5\}}+4P_C(j)
\]
and
\[
T_{C^+}(j)=8T_C(j)+4P_C(j-1)
\]
through ten Plotkin extensions. At every level it compares the recurrence output with the closed forms and verifies that the total pair and triple counts are
\[
\binom{4\cdot2^m}{2}
\quad\text{and}\quad
\binom{4\cdot2^m}{3}.
\]

The finite base calculations check the nonstandard inputs; the infinite-family step is the proved recurrence in `RESULT.md`.

Successful replay prints `VERIFY_OK`.
