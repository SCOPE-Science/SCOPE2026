# Scientific review of the seven-point pair-intersection theorem

## Correctness (PASS)
All \(S(7,4)=350\) partitions of seven points into four unlabelled nonempty blocks are generated canonically by restricted-growth words. Their 21-bit within-block-pair masks implement exactly the stipulated pair-intersection relation. A self-contained complete colour-bounded clique search proves no clique of size \(66\) (396 nodes); exhaustive size-65 enumeration (1827 nodes) yields exactly 21 cliques. Independently constructed prescribed-pair stars are exactly those 21 cliques. The search's greedy independent colour classes bound a clique's remaining size, so the pruning is deductively complete. The exact reproduced verifier output is included. The conclusion holds only for the stated finite case.

## Originality (PASS, subject to historical-priority risk)
The motivating 2026 paper of Cao, Liao and Zhang proves its higher-rank EKR statement for substantially larger ground sets (in rank three, at least 24 points), leaving the sharp near-boundary regime open; the seven-point case is not a corollary. The older conjecture in Erdős and Székely supplies the unresolved endpoint but not its bound or complete equality classification. Meagher and Moura use common entire blocks, not a common within-block pair. Searches of published research records and relevant primary sources did not identify the seven-point exact equality classification. Residual risk: an older specialized finite classification or unpublished enumeration may exist, so this assessment does not establish independent historical priority.

## Value (PASS)
The parameter is not an arbitrarily selected small computation: seven is the boundary \(n=2k-1\) for four-block partitions explicitly singled out by a long-standing conjecture, while the general 2026 rank-three theorem applies only much farther away. The exact sharp value and *all* equality cases fill this motivated first endpoint, with a reproducible complete certificate. No asymptotic or general conjecture solution is claimed.

## Literature and limitations
Primary references: Erdős--Székely (2000), *Erdős-Ko-Rado Theorems of Higher Order*, Section 3; Cao--Liao--Zhang (2026), arXiv:2608.05951, Sections 1 and 6; Meagher--Moura (2005), *Erdős–Ko–Rado theorems for uniform set-partition systems*, Section 5.2. A full-text comparison and published-record search cannot rule out all unindexed or unpublished earlier casework. The finite proof depends on source-code inspection and faithful replay; external independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
