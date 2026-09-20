# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The proposed set is checked in both directions.

First, its initial segment follows directly from the greedy rule: all integers from \(2f+\delta\) through \(3f+\delta-1\) are admitted, while the next interval is excluded by adding \(f\).

For the periodic tail, the proof computes all three relevant modular sumsets:
\(E\widehat{+}E\), \(E+R\), and \(R+R\). The last calculation deliberately includes equal residue classes, because two distinct tail integers can occupy the same residue class in different periods. Each sumset is disjoint from \(R\), which proves that no proposed tail entry is a forbidden distinct-pair sum.

Conversely, the displayed witness tables cover every nonselected position in one full tail period. Each witness uses distinct earlier selected integers and contains a summand that can be shifted by any positive multiple of the modulus while remaining selected. Hence the witnesses propagate to every later period.

The period word follows from the ordered residue blocks. Its minimality is certified by a value occurring exactly once in the cyclic word: \(2f-2\) for \(\delta=1\), and \(f+2\) for \(\delta=2\). The transition difference \(f+1\) is absent from the periodic word, proving that the stated preperiod cannot be shortened.

Exact finite verification reproduces the greedy sequence for \(5\le f\le300\) in both families through eight full periods and checks the modular sumset identities. The finite check supports but is not needed for the general proof.

## Originality — PASS, to the best of our knowledge

The most relevant current source is van Berkel–Bosma, arXiv:2609.18522. Its Theorem 12 records the proven region \(g\le2f-1\); Theorem 14 is explicitly presented as the new diagonal case \(g=2f\); and its later theorems provide finite computational verification of broader conjectures. Thus the two lines \(g=2f+1\) and \(g=2f+2\) lie immediately beyond the stated infinite proven frontier in that paper.

Targeted searches were made for the exact forms \(S_{f,2f+1}\) and \(S_{f,2f+2}\), for "2-sumfree" together with these parameter relations, and for equivalent 0-additive/greedy strict terminology. No prior infinite theorem for either family was located.

The principal residual risk is Raymond Queneau's 1972 paper *Sur les suites s-additives*. Its full text was not inspected. Modern sources identify Queneau as foundational for 0-additive sequences and report many explicit special cases. The 2026 papers discuss this historical work and do not identify the two families proved here as previously settled, which is evidence but not a substitute for direct inspection. Steven Finch's 1992 0-additive article and related OEIS entries were also checked at the bibliographic/statement level; they exhibit fixed-base periodic examples, not a theorem matching these variable-\(f\) families. Because the motivating preprints are only days old, unindexed concurrent work is another residual risk.

The originality claim is therefore limited to "to the best of our knowledge."

## Value — PASS

This result advances the exact infinite frontier by two parameter lines rather than adding isolated examples. It gives a closed residue-class description, minimal period and preperiod, an explicit periodic difference word, and the density for each family. The proof is elementary and reusable: it separates a modular sum-free certificate for admitted residues from a finite witness system for rejected residues, with the latter propagating by translation through the period modulus.

The result also converts two portions of a broad computationally supported conjectural pattern into exact theorems for every \(f\ge5\).

## Limitations

The theorem does not settle all greedy strict 2-sumfree sequences. It covers only \(\delta=1,2\) and \(f\ge5\), and it does not assert that the same residue pattern extends to larger offsets. Small values outside the stated range are intentionally excluded. Historical-source access is incomplete as described above, and no independent validation or independent audit is claimed.
