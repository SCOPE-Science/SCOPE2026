# Scientific review

## Correctness

**PASS.** For any coprime \(n,b\), the periodic floor-difference mechanical word has exact cumulative one-counts. Telescoping the two opposite length-\(\ell\) intervals yields \(v+\mathbf1_{j+r\ge n}\) and \(v+\mathbf1_{r>j}\), so their equality has precisely two disjoint residue intervals. Each contains \(\min(j,n-1-j)\) residues, and multiplication by the coprime slope permutes residues. The asserted distribution therefore follows for every rotation. Reproducibility checks cover 105,388 rotations through length 80; they supplement rather than replace the proof.

## Originality

**PASS, with bounded residual risk.** The closest relevant published results are Blanchet-Sadri–Chen–Hawes (2017), Theorem 3 on global counts of arbitrary binary words by Abelian-border number; Carey–Clampitt (2018), Theorem 1 and Corollary 1 on fixed-length partitioned circular factors (strictly shorter than the full Christoffel word); and Bugeaud–Reutenauer (first public 2022), Section 8 on ordinary exact-match borders of Christoffel conjugates. Their inspected statements concern distinct statistics and do not give the simultaneous full-length, all-rotation Abelian-border set or the slope-independent distribution. Targeted research-record and literature searches found no equivalent statement. A reformulation in other terminology or unindexed results remains possible.

## Mathematical value

**PASS.** It is natural to ask how many rotations of a highly structured balanced word are Abelian-bordered, and how many different lengths occur. The theorem supplies the complete arithmetic answer for **every** coprime slope and length, including each allowed border length and the entire count spectrum. It sharpens the simple existence of an unbordered Christoffel conjugate into exactly two Abelian-unbordered rotations and identifies the unique all-length bordered conjugate in odd lengths. This is a natural structural classification, not a small numerical table or a generic renaming.

## Limits

The result is specifically about binary primitive Christoffel conjugates. Searches cannot prove absolute novelty, and an independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
