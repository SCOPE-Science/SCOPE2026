# Independent scientific audit — SCOPE-20260921-0ceea66ee9ab

Audited at: 2026-10-01T23:13:29.436856Z

Disposition: **passed**

## Correctness — PASS

The point--2-subset incidence matrix diagonalizes \(KG(k,2)\) into eigenvalues \(\binom{k-2}{2}\), \(3-k\), and \(1\) on subspaces of dimensions one, \(k-1\), and \(\binom{k}{2}-k\). Interlacing from \(W_k\) after deleting \(t\) point vertices forces at least \(\binom{k}{2}+1-t\) positive eigenvalues, while the unchanged induced Kneser graph forces at least \(k-1\) negative eigenvalues. These counts exhaust the vertices and leave no zero eigenvalues. The connectivity and twin-free arguments are elementary and valid for \(k\ge5\).

### Correctness sources

- assigned RESULT.md
- Chen--Li arXiv:2605.07196
- assigned artifacts/verify_inertia_ladder.py

### Correctness risks

- The numpy census for \(5\le k\le10\) is only corroboration and is not used to prove the infinite family.

## Originality — PASS

Chen and Li construct \(W_k\) and state its inertia, and they analyze the special deletion \(W_5-a_1\). Akbari et al. explicitly ask for an infinite family of reduced equality graphs. Resultary's direct search returned the assigned ladder but no earlier all-\(k\), all-\(t\) theorem. The general deletion ladder and resulting infinite equality family are therefore not covered by the inspected primary statements.

### Equivalent formulations

The special deletion is one instance; it does not imply the all-\(k\), all-\(t\) inertia ladder without the interlacing argument.

### Broader coverage

Neither primary source gives a broader theorem that dominates all point deletions.

### Exact database or table

This is an infinite structural theorem, not a known-table recomputation.

### Claim versus prior implication

The full ladder and interval-realization consequence require a new uniform implication; they are not mechanical from the isolated case.

### Sources inspected

- Counterexamples to a conjecture on graph inertia — https://arxiv.org/abs/2605.07196. PARTIAL_COVERAGE: It owns the base family and one deletion but not the all-\(t\) ladder.
- A new conjecture on the inertia of graphs — https://doi.org/10.1016/j.disc.2025.114953. OPEN_PROBLEM_SOURCE: The assigned \(t=1\) family answers the stated problem.

### Checked sources

- arXiv:2605.07196
- arXiv:2508.01163 / DOI 10.1016/j.disc.2025.114953
- arXiv:2609.06319
- Resultary semantic search

### Residual risks

- Very recent differently indexed work on the same counterexample family could overlap, but no concrete source was found.

## Value — PASS

The theorem turns a counterexample construction into an exact deletion ladder, realizes an interval of inertia pairs, and supplies an infinite family answering a named problem. Those are motivated structural consequences rather than isolated numerics.

### Value sources

- Akbari et al. Problem 3.3
- Chen--Li arXiv:2605.07196

### Value risks

- It does not classify all equality graphs or solve the post-counterexample extremal problem.

## Limitations

- The theorem does not determine maximal positive inertia for fixed negative inertia.
- It does not classify all reduced equality graphs.
- Originality is best-of-knowledge against very recent or differently indexed graph-inertia work.
