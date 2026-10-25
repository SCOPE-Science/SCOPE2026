# Scientific review: finite linear two-list insertion census

## Correctness: PASS

Canonical reduced-row-echelon enumeration yields each binary linear \(k\)-subspace once: the pivots are fixed and the only freely chosen entries lie in nonpivot columns after the row pivot. The search checks each received word's *distinct* one-deletion parents against the subspace and exhausts all \({n\brack K(n)+1}_2\) candidates in each next dimension. The Gaussian-binomial totals independently match the enumeration. The largest exclusion comprises all \(43435\) length-nine seven-dimensional subspaces. A second, forward insertion implementation confirms every displayed optimal witness, including the length-nine histogram \((432,480,112)\). The optimal-dimensional census examines all \(788035\) length-nine six-subspaces and finds precisely \(1786\) valid examples. The proof is finite and does not infer any untested infinite extension.

## Originality: PASS with residual risk

The September 2026 Kiah--Wei--Zeng work studies general constant-list insertion/deletion code rates and reduction bounds, rather than exact *binary linear* one-insertion dimension and census profiles for fixed short lengths. The July 2026 Con--Doron--Ribeiro work gives asymptotic list-decoding capacity for unrestricted codes and polynomial-size lists; it does not imply the displayed exact counts. Xie--Chen--Qu--Liu study pairwise insdel distance bounds for linear codes, not exact three-parent incidence counts. Published mathematical-record searches, related deletion-only research, and literature searches for aliases and the exact parameters revealed no result implying the new profile. A relevant 2024 journal article's full text was inaccessible, leaving a genuine residual comparison risk. Failed searches do not prove uniqueness.

## Value: PASS

The difference between deletion and insertion list decoding is an active coding-theory issue. Fixing the stringent list size exactly two and enforcing linear encoding makes finite parameter thresholds and counts operationally meaningful: the result establishes the first length supporting six information bits, identifies an explicit six-row binary generator, and counts every optimal-dimensional code for nine consecutive lengths. Its nine-bit census is a natural complete invariant, not an arbitrarily selected single code or a routine restatement of a pairwise distance bound. No unproved downstream theorem is claimed.

## Closest literature and limits

Kiah--Wei--Zeng (arXiv:2609.21395), Con--Doron--Ribeiro (arXiv:2607.03989), and Xie--Chen--Qu--Liu (DOI:10.3934/amc.2023008). The exact insertion list-two linear subspace census is separate from asymptotic bounds, unique-decoding distances, and two-list deletion problems. An inaccessible plausible primary source remains a residual originality risk. The results have undergone self-review; independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
