# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS.** For a connected inverse-closed Cayley graph, every eigenvalue from the unique nonlinear representation appears in the regular spectrum with multiplicity divisible by \(d\), whereas each of the \(d\) linear characters contributes once. Thus total spectral multiplicity modulo \(d\) recovers the number of linear-character sums at each eigenvalue. Connectedness excludes the only ambiguous residue \(d\), because if all linear sums equalled the principal sum \(|S|\), the top eigenvalue would not be simple. The zero adjacency trace then recovers the unique nonlinear character sum. Abdollahi--Zallaghi's connected-complement reduction extends this to all Cayley graphs. The affine groups \(\operatorname{AGL}(1,q)\) have exactly \(q-1\) linear characters and one nonlinear character of degree \(q-1\), so the criterion applies. The broader Frobenius-branch statement uses Seitz's classical one-nonlinear-character classification.
- Originality: **PASS.** The complete 2019 primary source proves the order-20 and order-42 affine cases separately and lists BI-groups only through order 30. Its introduction still frames classification of BI-groups as open. No inspected source states the general spectral-residue criterion or the all-\(q\) \(\operatorname{AGL}(1,q)\) theorem.
- Scientific value: **PASS.** The result replaces two isolated affine examples with a simple general spectral mechanism covering every \(\operatorname{AGL}(1,q)\), and standard CI restrictions then yield an infinite nonabelian BI-but-not-CI family. It directly advances the published BI-group classification problem.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and
`INDEPENDENT_AUDIT_2026-10-01.json`. Earlier same-model scientific evidence
remains separately identified in `AUDIT.json` and is not relabeled as this
independent assessment.
