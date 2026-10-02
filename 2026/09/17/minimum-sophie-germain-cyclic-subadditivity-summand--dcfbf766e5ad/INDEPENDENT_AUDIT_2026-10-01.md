# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260917-dcfbf766e5ad`

## Correctness — PASS

The lower bound and witness are independently reproducible. Every cyclic integer greater than two is odd and squarefree. If \(a\) and \(2a+1\) are cyclic, squarefreeness excludes \(a\equiv0,4\pmod 9\); together with oddness this leaves exactly residues \(1,3,5,7,11,15,17\pmod{18}\). Exhausting the 18 starting residues gives window maxima \(1,1,2,2,3,3,4,4,5,5,6,6,6,6,7,7,7,7,8,8\) for lengths one through twenty, each no larger than the exact initial count \(C_\sigma(m)\). Therefore no counterexample has smaller summand at most twenty. An independent integer computation also reproduces all nine Sophie Germain cyclic integers in \((87088,87109]\), giving nine new terms against \(C_\sigma(21)=8\), so the sharp witness is valid.

### Correctness sources

- assigned RESULT.md
- artifacts/verify.py and verify-output.txt
- Ibarra, arXiv:2607.09793
- OEIS A397387
- independent exact integer/factorization recomputation

### Correctness risks

- The theorem minimizes only the smaller summand under \(1\le m\le n\), not total size or the larger summand.

## Originality — PASS

Cohen states the subadditivity conjecture, and Ibarra's published counterexample uses smaller summand 31. Fresh exact and semantic searches found no prior determination of the minimum smaller summand, no prior \(m=21\) witness, and no prior mod-18 packing proof. OEIS A397387 supplies sequence data but not the global minimum theorem.

### equivalent_formulations

Searches:
- semantic search for minimum shorter summand in a Sophie Germain cyclic subadditivity counterexample
- search for the pair \((21,87088)\) and the mod-18 obstruction

Evidence:
- The audited record was the only exact theorem-level match found.

Reasoning:
Equivalent formulations in terms of window increments \(C_\sigma(n+m)-C_\sigma(n)\) were also considered.

### broader_coverage

Searches:
- Cohen, arXiv:2508.08335
- Ibarra, arXiv:2607.09793

Evidence:
- Cohen poses the conjecture; Ibarra disproves it at \(m=31,n=3928\).

Reasoning:
Ibarra gives only an upper bound of 31 on the unknown minimum, not the sharp value 21 or the universal exclusion of lengths at most 20.

### exact_database_or_table

Searches:
- OEIS A397387 and linked table

Evidence:
- The database lists Sophie Germain cyclic numbers and links Cohen/Ibarra.

Reasoning:
Sequence data can check candidates but does not imply the all-\(n\) lower bound; the mod-18 argument supplies that infinite proof.

### claim_vs_prior_implication

Searches:
- comparison of the Ibarra counterexample with the audited lower bound

Evidence:
- The prior counterexample is compatible with \(m\ge21\) and does not determine the minimum.

Reasoning:
The exact boundary and sharp length-21 witness are not corollaries of the prior result.

### source_inspections
- **A counterexample to a subadditivity conjecture of Cohen for Sophie Germain cyclic numbers** — https://arxiv.org/abs/2607.09793. Trigger: Closest prior disproof of the same conjecture. Material read: Abstract and accessible full preprint text, including the explicit \(m=31,n=3928\) counterexample. Method: Primary full-text statement comparison. Assessment: Does not determine the minimum smaller summand. Evidence: Its theorem supplies one counterexample at smaller summand 31.
- **Conjectures about Primes and Cyclic Numbers** — https://arxiv.org/abs/2508.08335. Trigger: Original conjecture. Material read: Abstract and scope. Method: Primary-source comparison. Assessment: Poses the subadditivity question; does not contain the audited sharpening. Evidence: The work introduces/tests the cyclic-number conjectures.
- **OEIS A397387** — https://oeis.org/A397387. Trigger: Exact sequence database for Sophie Germain cyclic numbers. Material read: Current entry, links and examples. Method: Database inspection. Assessment: Useful for sequence verification but not covering the theorem. Evidence: The entry links Cohen and Ibarra and provides sequence-generation data.
- **Assigned finite verifier** — artifacts/verify.py. Trigger: Residue-window table and sharp witness. Material read: Complete source and captured output. Method: Line-by-line inspection plus independent exact recomputation. Assessment: All finite ingredients reproduce exactly; the universal lower bound comes from the stated residue lemma. Evidence: The nine witness values and all length-at-most-21 window maxima match.

### checked_sources

- https://arxiv.org/abs/2508.08335
- https://arxiv.org/abs/2607.09793
- https://oeis.org/A397387
- assigned RESULT.md and artifacts/verify.py

### residual_risks

- A very recent unindexed follow-up to Ibarra could overlap the sharpening, but none was located in the fresh searches.

## Scientific value — PASS

The result identifies the exact structural threshold in a newly disproved counting-function conjecture: a congruence packing obstruction rules out every shorter window, and an explicit window attains the first permitted length. This is a natural sharp boundary, not merely another counterexample.

### Value sources

- Cohen's conjecture
- Ibarra's \(m=31\) counterexample
- the mod-18 obstruction and \(m=21\) witness

### Value risks

- The minimization criterion is specifically the smaller summand.

## Limitations

- The theorem does not minimize total counterexample size or the larger summand.
- Originality is best-of-knowledge.
- The explicit witness is finite computation, while the exclusion of all shorter summands is mathematical and periodic modulo 18.

## Disposition

**PASSED**
