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

With the unnormalized plus-sign Fourier transform, Fourier squaring acts on odd functions by −25, so work with sign-pair support counts r≤s. A single input pair has at most two zero rows. For r+s≤7, the only other possibilities reduce by enlarging the allowed Fourier support to (2,4), (2,5), (3,3), and (3,4). I independently reproduced the decisive finite certificate (`python3 /workspace/review-evidence/odd_projective.py`) over F_101 and F_151 with primitive 25th roots 16 and 148. The reproduction tests normals to rows for two columns, and cross products of independent row pairs for three columns, rather than using the supplied row reduction. A violating rank-one subset in three columns can be extended by an outside nonparallel row to a plane, and a rank-zero subset is contained in any such plane. The program verifies that the full row list admits such a plane for each triple. There are at most seven vanishing rows for three columns and only the two stated exceptions with seven or more vanishing rows for two columns. Each full-column-rank specialization proves a nonzero cyclotomic minor; a modular failure alone proves nothing in characteristic zero. For the two exceptions the displayed subgroup sine modes have time support {±5,±10} and transform 5 times the signed difference of the two coset indicators y≡±t mod 5. The zero-constraint matrices have rank at least one (there is a nonmultiple-of-5 row) and at most one by these explicit nonzero kernels, so give exactly one projective class each. Fourier duality gives the other two classes, distinct by support size and within each size by invertibility or distinct residue support. This proves the finite result at cyclic order 25, not an infinite prime-square theorem.

## originality

PASS

The distinct contribution is the sharp odd support-sum bound across all support sizes on cyclic order 25 and the complete projective equality census. An unrestricted bound already handles the (4,10) lower-bound branch, and compressed sine transforms and their failure of full spark at composite order are known. The available earlier statements do not cover the sharp odd minimum and all equality vectors together.

## value

PASS

Cyclic prime-square order is a natural place to test how subgroup structure changes prime-order sine uncertainty. The unrestricted bound plus parity leaves a genuine competing balanced support configuration at order 25. Excluding it and identifying every sharp line gives an exact benchmark for symmetry-restricted prime-power uncertainty and compressed minor ranks, rather than just evaluating a known formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
