---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The full proof covers every integer m,n>=2 and every continuous injective equivariant map by the Curtis--Hedlund--Lyndon finite-window theorem. Two fixed points must be mapped bijectively. A swap is impossible: a single length-m zero island in 1^Z maps, by locality, to a finite nonempty 1-island S in 0^Z; two far-separated source islands at translate d=m+ell produce disjoint translates S and S+d. Every large consecutive ell would force n to divide the inter-island zero gap m+ell+a-b-1, impossible as n>=2. With fixed points preserved, a single isolated source 1 in 0^Z maps to a finite nonempty 1-island S, and two source 1s separated by km zeros produce two output islands and an inter-island zero gap km+a-b. For every sufficiently large k, n|(km+a-b); subtraction at consecutive k forces n|m. Sufficiency is the canonical inclusion when n|m. For entropy the irreducible right-resolving m-state graph has finite-to-one labeling (all-zero point is its only multiply labeled point), polynomial x^m-x^(m-1)-1 and a unique Perron root >1; the implicit scalar relation 1=x^(-1)+x^(-m) gives strict entropy decrease in m. Direct independent reconstruction of six Git blobs verifies original source tree SHA. Independent exact symbolic characteristic-polynomial checks for m=2..11 and 77 exact cyclic-word vs graph-trace comparisons for m=2..8, p=1..11 corroborate the structural algebra, while the unrestricted conclusion rests on the proof, not enumeration.

## originality

PASS

The natural full two-parameter embedding classification Y_m -> Y_n iff n divides m was not located as an independent theorem. Marcus--Meyerovitch--Wu (arXiv:2606.25475, Theorem 7 and Proposition 2) gives broad near-Markov existence and algorithmic criteria; specializing these involves nontrivial verification of blowup and compatibility and it does not state the arithmetic family result. Marcus--Meyerovitch--Thomsen--Wu (arXiv:2508.02554, Section 4) concerns the stricter factorizable-embedding question. Dastjerdi--Jangjoo classify S-gap conjugacy and compute entropy, not arbitrary source-to-target embedding for the modular-gap pairs. Resultary semantic searches returned the exact mirror of THIS record but no distinguishable prior result. The entropy formula is previously covered by the classical S-gap entropy function; the asserted novel contribution is the exact arbitrary-embedding obstruction. This is a best-of-knowledge conclusion, not a claim that every literature source has been examined.

## value

PASS

An explicit pairwise embedding classification for the canonical infinite family of periodic S-gap shifts is a natural exact invariant of the dynamical category, not a tailored finite example. It gives a simple complete arithmetic embeddability poset, accounts for arbitrary sliding block codes rather than inclusions, and isolates a robust finite-island obstruction even when the entropy inequality is favorable. The entropy formula is older, but the unrestricted embedding characterization is a substantive structural conclusion not mechanically replaced by it. The exact invariant and asymptotic island method are plausibly useful for coding theory and symbolic-dynamics embeddings without requiring an overarching general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
