# Independent Audit — 2026/09/18/output-sensitive-qary-fix-free-construction--e8ec1ec6a0dd

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `aa183b98b67de7a93a7883b541f702b40fbed20f`
- Disposition: **PASSED**

## Correctness

**PASS** — The two implementation reductions were checked independently. From δ_S(x)=b_x-r_{j(x)}(S)-c_{i(x)}(S), selecting x=(i,j) decrements exactly the candidates with i(·)=j and those with j(·)=i. Under either Gao-Shan one-sided uniqueness condition, one of these is a whole group update and the other contains at most one live candidate, so grouped lazy offsets plus local/global heaps reproduce the exact greedy minimum in O(log|D|) per selected word. A fresh randomized finite reconstruction matched naive score recomputation for both uniqueness orientations. For the longest layer, when λ3≥2λ2 the admissible words are exactly P×X^{λ3-2λ2}×S; when λ2<λ3<2λ2 they are bijective with the disjoint union of P_a×S_a over the β=2λ2-λ3 overlap. Fresh binary/ternary tests matched exhaustive enumeration. Building the overlap buckets costs O(N2) and enumeration can stop after μ3 outputs, giving the stated output-sensitive term.

## Originality

**PASS** — Gao-Shan's September 2026 paper supplies the q-ary three-length deterministic construction and the one-sided-uniqueness interpolation structure, but the audited optimization exploits that structure to remove repeated packet rescans and the exhaustive longest-word scan. Searches did not locate this grouped-priority implementation or the bound O(N2 log N2+μ3 λ3). Standard heaps and Cartesian-product enumeration are of course not new; the novelty is their source-specific structural application. The older binary Congero-Zeger construction is a residual comparison risk, but it predates the later q-ary matrix interpolation theorem being optimized and no matching bound was located.

## Scientific value

**PASS** — The improvement changes the source construction from a quadratic middle-layer scan plus exhaustive N3 final scan to near-linear-logarithmic middle-layer work and output-sensitive final-layer generation. This is a meaningful algorithmic strengthening for the same constructive coding theorem even though the 3/4 Kraft threshold itself is unchanged.

## Sources

- The 3/4 Conjecture for q-Ary Fix-Free Codes With at Most Three Distinct Codeword Lengths (Weiguo Gao; Zhi Shan): https://arxiv.org/abs/2609.18237 — Primary q-ary construction source; introduces the matrix interpolation and one-sided uniqueness structure optimized here.
- The 3/4 Conjecture for Fix-Free Codes With at Most Three Distinct Codeword Lengths (S. Congero; K. Zeger): https://doi.org/10.1109/TIT.2022.3218212 — Earlier binary three-length theorem and residual source for potentially related implementation ideas.

## Limitations

- The result improves only the implementation of the Gao-Shan construction; it does not strengthen the Kraft threshold or handle four or more lengths.
- No lower bound proves that O(N2 log N2) is optimal for producing one prescribed middle-layer cardinality.
- The full text of the older closed-access Congero-Zeger paper was not needed for correctness and was not claimed to have been read; it remains a limited originality risk.

## Independent exact check

```json
{
  "implementation": "fresh Python reconstruction of dynamic scores and longest-layer admissibility",
  "greedy_tests": "both one-sided uniqueness orientations; packet sizes 1,2,5,10,25,50 with 20 deterministic seeds each",
  "greedy_matches_naive": true,
  "longest_layer_tests": "four binary/ternary overlap and nonoverlap cases",
  "direct_generation_matches_exhaustive": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked first. No decisive comparison required Oxford Download in this record.
