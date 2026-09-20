# Review: odd-squarefree hardness for Dense Pinwheel Packing

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof preserves the recent strong-hardness reduction and changes only the source part size before that reduction is applied.

The padding step is reversible: each added component is an isolated tripartite triangle, so every triangle partition of the padded graph must use that unique triangle, and removing all dummy triangles recovers a partition of the original graph. The source promises are preserved because dummy vertices have degree two and triangle-incidence one.

After padding to an odd prime part size \(p>3\), the marker primes are all chosen larger than \(p\). A vertex participates in at most three graph triangles, so its marker product \(m_v\) is squarefree with at most three prime factors. Hence the two target period types \(pm_v\) and \(3pm_v\) are odd and squarefree with at most four and five distinct prime factors respectively. Every marker occurs in a witness period, \(p\) occurs in every period, and \(3\) occurs in cell periods, proving the exact least-common-multiple formula. The only prime common to all periods is \(p\): \(3\) is missing from witnesses and each marker is local to one graph triangle. The density identity is unchanged. Bertrand's postulate gives \(p=O(n)\), so the unary size remains polynomial.

The supplied finite verification checks the arithmetic identities independently on representative prime choices and all possible local incidence counts. It is corroborating evidence, not a substitute for the general proof.

## Originality

**PASS, to the best of our knowledge, with elevated near-simultaneous risk.**

The primary source, Kobayashi--Lin--Swernofsky (arXiv:2609.20075v1), was inspected at theorem, source-problem, reduction, soundness/completeness, and explicit-size sections. It proves unary NP-completeness and explicitly uses marker products of at most three primes, but it states no odd-period, squarefree-period, bounded-prime-support, or squarefree-common-LCM restriction.

The earlier Kleinberg--Mishra paper (arXiv:2604.13974) was also checked for `odd`, `squarefree`, `square-free`, and related prime-factor restrictions. No such restricted-hardness theorem was located; moreover, its hardness construction uses squared prime factors in key period expressions, so it does not imply the squarefree statement here.

Exact and synonymous searches were made for combinations of `Dense Pinwheel Packing`, `pinwheel scheduling`, `odd periods`, `squarefree periods`, `prime factors`, `exact covering system`, `disjoint covering system`, and computational hardness. No prior statement equivalent to the theorem was found. The current SCOPE archive was also searched for `pinwheel`, `Dense Pinwheel Packing`, and `pinwheel squarefree`, with no overlapping record found.

Classical squarefree/odd covering-system literature was checked as a possible source of a hidden obstruction. Balister--Bollobás--Morris--Sahasrabudhe--Tiba prove an impossibility for **distinct** squarefree moduli, not for explicit multisets with repeated moduli. Historical literature on odd disjoint covering systems establishes existence/structure results and does not supply the restricted computational-hardness theorem found here.

No inaccessible recent paper was located that is specifically likely to contain the same hardness refinement. Some older covering-system sources were available only through metadata or summaries; their residual originality risk is low because they predate the 2026 NP-hardness results and address structural existence rather than this computational restriction.

The main residual priority risk is instead the freshness of arXiv:2609.20075v1: the refinement is short once its marker-prime construction is known, so a near-simultaneous note or later revision could cover it.

## Value

**PASS.** The result shows that the strong NP-hardness is not caused by even moduli, repeated prime powers, or arithmetically complicated individual periods. Hardness survives when every period is a sparse divisor of a single odd squarefree integer, uses at most five prime coordinates, and all periods share exactly one common prime factor. This places the reduction in a particularly rigid Chinese-remainder setting and cleanly separates it from the distinct-modulus squarefree covering-system obstruction.

The strengthening is modest in proof length but meaningful in structural content. It is more restrictive than polynomial boundedness alone and identifies a robust arithmetic subclass of dense pinwheel instances that remains computationally intractable.

## Limitations

The result crucially keeps the explicit-list convention in which equal periods may correspond to different tasks. It does not settle complexity for distinct moduli. The bound of five prime factors is not proved optimal, and no hardness result with at most four prime factors follows from this argument.
