# Independent Audit — 2026/09/20/subnormal-intertwining-linear-schatten-exponent--682fbd020d3f

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `6077738b3f0a6e0d5ea2e1266bab795368f060f2`
- Disposition: **PASSED**

## Correctness

**PASS** — The linear Schatten estimate is correct. From D_n,D_{n+1} in S_p one has A^n C=D_{n+1}-D_nB and C B^n=D_{n+1}-A D_n. For subnormal A, the normal-extension interpolation argument gives AC in S_{np} with the stated norm bound; hyponormality plus Douglas factorization then gives A* C in the same class. Applying the same argument to B* and C* gives C B and C B* in S_{np}. The exact cubic identity CC*C=C X* A* C-C B* X* C is therefore in S_{np}; since CC*C=V|C|^3, this is equivalent to C in S_{3np}. The spectral-cutoff interpolation step is legitimate for p>=1 and the limit follows by lower semicontinuity. The root-of-unity diagonal example also checks: D_n=0, D_{n+1} is in S_p whenever q<(n+1)p, but C is not in S_q, so every universal exponent has linear lower order at least (n+1)p. Finally, Kittaneh's 2006 proof was inspected in full: it already reaches A*C and CB* in I^(1/2^(n-1)); stopping at the same cubic expression and taking a cube root indeed yields the submitted I^(1/(3*2^(n-1))) refinement rather than continuing Kittaneh's two successive square-root steps.

## Originality

**PASS** — Kittaneh's 1986 subnormal theorem gives C in S_{8p} for the n=2 powers, while his 2006 arbitrary-ideal consecutive-power theorem gives C in I^(1/2^(n+1)), hence S_{2^(n+1)p}. The full 2006 proof does not state the cube-root stopping refinement and does not use the normal-extension interpolation that produces the linear S_{3np} bound. The lower-barrier construction also establishes that the order in n cannot be removed. Targeted searches for the exact linear-in-n Schatten conclusion did not locate an earlier statement. The residual priority risk is older subnormal/symmetric-ideal literature under different notation, so novelty is claimed only for the explicit linear estimate, matching-order barrier, and cube-root refinement rather than for the underlying Douglas or interpolation tools.

## Scientific value

**PASS** — The theorem changes the known consecutive-power Schatten exponent from exponential to linear under the original subnormal hypotheses and proves that linear dependence on n is unavoidable. It also improves the general ideal proof without strengthening its hypotheses. The optimal constant between n+1 and 3n remains open, but the correct growth order is resolved.

## Sources

- **Some intertwining relations modulo operator ideals** — Fuad Kittaneh. https://doi.org/10.1017/S0017089505002910 — Authorized full text checked after open-access attempts. Theorem 1 gives the I^(1/2^(n+1)) conclusion and its proof was compared line-by-line with the submitted cube-root refinement.
- **On the commutants modulo C_p of A^2 and A^3** — Fuad Kittaneh. https://doi.org/10.1017/S1446788700028056 — Earlier n=2 subnormal result with the S_{8p} conclusion.
- **Some inequalities for norms of commutators** — Rajendra Bhatia; Fuad Kittaneh. https://doi.org/10.1137/S0895479895293235 — Prior sharper results in more structured self-adjoint/positive settings, appropriately excluded from the novelty claim.

## Limitations

- The optimal universal exponent is only bracketed between (n+1)p and 3np.
- The linear upper bound uses subnormality through normal extensions; under the weaker range-inclusion hypotheses only the general ideal refinement is established.
- The interpolation proof is stated for 1<=p<infinity; compact-ideal endpoint behavior is a separate qualitative statement.
- Equivalent interpolation sharpenings in older subnormal or symmetric-ideal literature remain a residual originality risk.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "normal_extension_interpolation_checked": true,
  "douglas_factorization_steps_checked": true,
  "cubic_identity_and_schatten_root_checked": true,
  "root_of_unity_lower_barrier_checked": true,
  "kittaneh_2006_full_text_checked": true,
  "open_access_first": true,
  "oxford_used": true,
  "oxford_job_id": "eac4486a9cfbf36d2822ae225fd50674",
  "oxford_status": "complete",
  "oxford_pages_checked": "1-7 of 7"
}
```

The assigned record tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access/preprint sources were checked before institutional retrieval. Any inaccessible comparison is explicitly identified and is not claimed read.
