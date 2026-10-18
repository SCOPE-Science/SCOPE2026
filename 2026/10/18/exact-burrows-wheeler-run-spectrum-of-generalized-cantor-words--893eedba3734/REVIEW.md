# Self-review

## Correctness: PASS

The claimed formula \(r(\operatorname{BWT}(C_{b,k}))=4k\) holds for every integer \(b\ge3\), \(k\ge2\). The proof explicitly identifies all circular zero gaps as \((b-2)b^{\nu_2(i)}\) except for the unique zero-length closing gap; unique maximal gap ensures primitive cyclic rotations. It partitions all zero-starting rotation rows by leading zero length and rigorously compares their first differing future gap at offset \(2^j\). This proves a three-class predecessor order, one of whose groups is \(1^{2^t-1}0^{2^t-1}1\). The one-starting group has exactly one predecessor one and starts and ends in zero. All boundary separations are nonempty for \(b\ge3,k\ge2\), yielding exactly \(2k\) one-runs and \(2k\) zero-runs. The ordered one-run spectrum and original-run ratio are consequent identities. Finite tests confirm but do not replace the unrestricted proof.

## Originality: PASS (best knowledge, with residual risk)

Targeted mathematical-record and primary-literature searches did not identify an equivalent result. Gil–Scott (2012) develops a bijective BWT variant rather than Cantor-word cyclic-BWT exact runs. Brlek et al. (2019) study Thue–Morse, Fibonacci generalizations and particular morphism compositions, not this substitution. Crucially, Frosini et al. (2022) already cover the **same family** in their general nonprimitive-growing binary-morphism asymptotic regime: their Theorems 4.1 and 4.2 imply \(\Theta(k)\) here. The new claim is specifically the exact coefficient \(4\), the base independence, full ordered one-run lengths and lexicographic group theorem; the known asymptotic bound does not imply those. An unindexed exact calculation remains possible and merits independent bibliographic audit.

## Value: PASS

This is an all-base, all-level classification of the BWT run measure in a canonical uniform morphic family, including the familiar middle-thirds Cantor word. The invariance of the complete one-run spectrum under changing the geometric base is not a generic consequence of BWT complexity bounds. Exact runs govern run-length storage and compressed indexing. The theorem gives an exact clustering ratio \(4k/(2^{k+1}-1)\), and its sharp constant and spectrum refine an existing general \(\Theta(\log n)\) theorem in a mathematically motivated nonprimitive case.

## Limits and closest literature

The boundary \(k=1\) is excluded because the exact value depends on \(b\). The theorem concerns cyclic BWT without a sentinel. Direct finite experiments covered 44 cases up to length 59,049, including 29 cases with separately sorted full rotations; the proof does not extrapolate from them. Closest covering theorem: Frosini et al. 2022, Theorems 4.1–4.2, covers the same morphism family asymptotically but not the exact enumeration. Source inspected: arXiv:2202.02609 in full-text HTML, relevant Sections 1–4; 2019 Brlek et al. lawful full manuscript, Sections 1–3 and all stated families; Gil–Scott arXiv:1201.3077 introduction and BWT preliminaries. The earliest dated relevant public reference is 2012-01-15.

Self-review: passed. Independent audit: not yet performed.
