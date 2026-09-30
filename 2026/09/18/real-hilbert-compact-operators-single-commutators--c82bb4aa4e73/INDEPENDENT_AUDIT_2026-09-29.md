# Independent Audit — 2026/09/18/real-hilbert-compact-operators-single-commutators--c82bb4aa4e73

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `16920b9f5de3bd80cc8311053e91ffa6c5115574`
- Disposition: **PASSED**

## Correctness

**PASS** — The real-field adaptation is coherent and repairs the places where Liu's complex proof is genuinely field-sensitive. Tran supplies the required dimension-free same-field matrix commutator bound for real traceless blocks, so the zero-diagonal block construction transfers. For the non-trace-class reduction, when the symmetric part is non-trace-class the needed phase steering can be performed with real signs; when only the skew-adjoint part is non-trace-class, the fixed similarity D=diag(2,1/2) sends a rotation block s[[0,-1],[1,0]] to a matrix whose symmetric part is (15s/8)[[0,1],[1,0]], with trace norm 15s/4, thereby reducing to the previous real case with uniformly bounded condition number. The real self-adjoint zero-diagonal lemma follows by successive two-vector rotations balancing positive and negative quadratic mass. In the trace-class case, the trace-concentration and block-assembly steps are real-linear, while Anderson's rank-one compact-commutator construction has a real matrix model; balancing the factors yields the square-root norm bound. No incompatible use of complex scalar multiplication remains in the submitted proof.

## Originality

**PASS** — Liu's new theorem explicitly assumes a complex Hilbert space, while Tran's simultaneous real/complex finite-matrix theorem removes only the finite-dimensional obstruction. Historical surveys still describe the single compact-commutator problem in the complex setting before Liu and Anderson's work as special constructions. Targeted searches for a theorem that every compact operator on a real Hilbert space is a single commutator of real compact operators, especially with a universal square-root norm bound, found no prior source. The submitted fixed-similarity treatment of the non-trace-class skew-adjoint case is the key distinctly real ingredient.

## Scientific value

**PASS** — The result transfers a newly solved decades-old operator-theory theorem to the real Hilbert category with quantitative norm control, where simple scalar-forgetting or complexification does not produce a single real commutator. The proof isolates a reusable real mechanism for converting non-trace-class skew-adjoint mass into symmetric mass under bounded similarity and clarifies exactly which parts of the complex argument are field-independent.

## Sources

- Every compact operator is a commutator of compact operators (Zhichao Liu): https://arxiv.org/abs/2609.20672 — Primary theorem for separable infinite-dimensional complex Hilbert spaces with universal square-root norm control.
- Quantum expanders and dimension-free commutator bounds (Tuan Tran): https://arxiv.org/abs/2609.20161 — Proves same-field dimension-free commutator bounds for traceless real or complex matrices.
- Commutators of compact operators (Joel Anderson): https://doi.org/10.1515/crll.1977.291.128 — Classical compact-commutator construction, including the rank-one projection model used in the trace-class reduction.
- B(H)-Commutators: A Historical Survey II and recent advances on commutators of compact operators (Daniel Beltiţă; Sasmita Patnaik; Gary Weiss): https://arxiv.org/abs/1303.4844 — Historical survey explaining Anderson's rank-one construction and the pre-Liu status of the single compact-commutator problem.

## Limitations

- The universal constant is not optimized.
- The theorem is only for separable infinite-dimensional real Hilbert spaces and does not address real Banach spaces or smaller operator ideals.
- The originality search did not uncover a prior global real theorem, but old operator-theory literature is extensive; an independently stated real-field corollary remains a residual risk.

## Independent check

```json
{
  "implementation": "direct 2x2 real-block calculation",
  "similarity_block": "D=diag(2,1/2)",
  "symmetric_coefficient": "15/8",
  "trace_norm_per_rotation_s": "15s/4",
  "all_ok": true
}
```

The assignment snapshot and source-tree-check commit were compared read-only and no file under this record changed. The dated independent-audit files were verified absent and the current `VERIFICATION.md` blob guard was checked. Open-access/preprint sources were checked first; no decisive comparison required Oxford Download. GitHub was not modified.
