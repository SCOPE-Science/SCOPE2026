# Independent audit — 2026/09/09/104

## Scope
Independent three-axis review of `2026/09/09/104` at source tree `c8eb35fd38a8618cc8d8001f0f680906b7e6f1b9` on repository `SCOPE-Science/SCOPE2026`. The source tree on `main` matched the assignment tree at audit time.

## Correctness
**PASS_AFTER_REPAIR.**
- Independent exact symbolic replay gives Hilbert function (1,3,6,10,10,6,3,1), the displayed nonzero second-Hessian factorization, middle multiplication determinant -36 and rank 10, the full maximal rank profile, kernel dimensions (0,10,20,26,32,35,38,39,40,40), Jordan type [8,6,6,4,4,4,2,2,2,2], and minimal-generator counts mu4=5, mu5=2.
- The original RESULT.md additionally promoted a higher-Hessian bridge identity that was only sampled at eight points and is not implemented in the committed verifier. That auxiliary statement is not adequately proved by the saved package.
- The original METADATA claim_type says 'Hessian-vanishing witness' although the verified second Hessian is explicitly nonzero. The repair removes the unsupported bridge claim, corrects the Buchsbaum–Eisenbud wording, and fixes the metadata.

## Originality
**PASS_NARROW.**
- Boij–Migliore–Miró-Roig–Nagel–Zanello reduce the codimension-3 problem to compressed odd-socle algebras and solve the predecessor Hilbert function; the 2024 small-Sperner result explicitly leaves the regime d>6 and Sperner>6 open.
- Targeted exact-polynomial searches did not locate this Fermat-plus-tail septic or its Hessian/Jordan/minimal-generator tuple. The claim is only an exact data point, not a universal WLP theorem.

## Scientific value
**PASS_NARROW.**
- A single positive example does not resolve the open cell, but a fully reproducible exact tuple in the first compressed socle-7 region is a usable boundary datum for WLP/Hessian/Jordan experiments. Its value is computational and diagnostic rather than theorem-level.

## Reproducibility
The committed verifier's exact Sympy computations were independently reproduced for every retained numerical claim.

## Literature checked
- On the weak Lefschetz property for artinian Gorenstein algebras of codimension three: https://arxiv.org/abs/1302.5742 — Reduction to compressed odd socle and complete treatment of the first open Hilbert function (1,3,6,6,3,1).
- The weak Lefschetz property for artinian Gorenstein algebras of small Sperner number: https://arxiv.org/abs/2406.17943 — WLP for Sperner number at most d+1; explicitly states the codimension-3 regime with both socle degree and Sperner number above six remains open.
- Lefschetz elements of Artinian Gorenstein algebras and Hessians of homogeneous polynomials: https://arxiv.org/abs/0903.3581 — Higher-Hessian criterion background; does not supply this exact septic computation.

## Publication disposition
`repaired`. This audit file records a proposed publication change-set only; it does not state that any change has been applied to GitHub.

## Limitations
- Universal WLP for the entire (1,3,6,10,10,6,3,1) cell remains open.
- The revised record validates only the committed verify_F0.py outputs; no point-sampled bridge identity is claimed.
- No Macaulay2/Singular cross-check or explicit 7x7 alternating Buchsbaum–Eisenbud matrix is present.
