# Scientific review: sharp zero-only cyclic equalization at weight two

## Correctness — PASS

For two-one binary words, all circular orbit information is the unordered pair of arc lengths. Writing the arc lengths after common zero insertions yields two exact linear integer equations, one for equal internal distances and one for complementary distances. Every inserted zero contributes a coefficient in \(\{-1,0,1\}\), so a required imbalance of absolute value \(h\) costs at least \(h\) insertions; the proof locates a single gap attaining that lower bound whenever the branch is feasible. The resulting three-case formula implies the bound \(n-3\), sharp witness, and disjoint extremal families of sizes \(4(n-2),4,4\). Literal zero-padding plus cyclic-rotation enumeration confirms every pair through \(n=8\); the universal result is mathematical, not computational extrapolation.

## Originality — PASS within examined evidence

Thongjarast, Pasiphol, and Ruangwises, arXiv:2604.19504v1, prove general existence and expressly ask for minimum insertion length. Thongjarast, arXiv:2607.18452v1, proves existence under zero-only insertions, gives a polynomial construction, and explicitly asks for sharp nonasymptotic length (Section 10.1). Neither inspected complete manuscript states the exact weight-two formula, all-length sharp bound, or 4n extremal enumeration. Related indexed mathematical results and accessible previous claims were searched using aliases. Historical priority remains qualified by unindexed literature and the incomplete inspection of the original 2025 foundational manuscript.

## Mathematical value — PASS

The case of two ones is the first nontrivial fixed-weight layer for restricted zero insertion: at weight one all binary words are cyclically equivalent without insertions. Exact minimal helping-card cost is a stated problem in the source literature. An explicit formula for every pair, a sharp linear worst-case threshold, and a classification of all extremizers give a complete resource benchmark within this natural layer. This is not a claim about the general-weight optimum.

## Scope and risks

The result is restricted to two binary words of the same length, each with exactly two ones, and identical zero-only gap insertions. Allowing arbitrary inserted symbols changes the cost; no stronger claim is made. Equivalent unindexed work is possible. The embedded checker supplies finite cross-checks but no independent scientific certification.

Self-review: passed. Independent audit: not yet performed.
