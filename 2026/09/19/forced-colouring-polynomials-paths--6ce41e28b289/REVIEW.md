# Review

## Correctness

**PASS.** A successful partial 3-colouring of a path cannot leave an endpoint uncoloured and cannot contain two adjacent uncoloured vertices. Hence the uncoloured set is an independent subset of the internal vertices. For a fixed proper full 3-colouring, such an uncoloured vertex is forceable exactly when its two neighbours have different colours. Encoding a proper 3-colouring by its initial colour and its \(\pm1\) edge differences in \(\mathbb Z_3\), each omitted vertex imposes one equality on a disjoint adjacent pair of edge-difference variables. For an omitted independent set of size \(j\), this gives exactly \(3\cdot2^{n-1-j}\) compatible full colourings. There are \(\binom{n-1-j}{j}\) such omitted sets, proving the coefficient formula.

The probability formula is the direct domain-size weighting of those coefficients. The Fibonacci-type recurrences, minimum-domain size, and minimum-domain counts follow algebraically. The formulas for \(\lambda=1,2\) and \(\lambda\ge4\) use established results from the source paper and the fact that \(\Delta(P_n)=2\).

Definition-level exhaustive verification agrees with the exact coefficient formula for every \(P_n\) with \(2\le n\le8\). The \(P_3\) check gives six successful domain-two assignments and twelve successful domain-three assignments, independently confirming the correction of the displayed special case.

## Originality

**PASS, to the best of our knowledge.** The accessible full text of arXiv:2609.17108v1 was inspected. It develops the general forced-colouring function, gives the \(\lambda=2\) bipartite theorem, the high-colour maximum-degree simplification, and all connected examples through four vertices, but contains no general path \(P_n\) formula. Its \(P_4\) example is recovered by the theorem here. Its displayed \(K_{1,2}=P_3\), \(\lambda=3\) value conflicts with both direct enumeration and the paper's own identity at \(p=1/3\); the corrected value is a consequence of the general formula.

The accessible full preprint arXiv:2406.15746 introducing the polynomial framework was also inspected; no path-family formula was found. Targeted searches covered British and American spelling variants of forced/forcing colouring/coloring, paths, partial 3-colourings, chromatic forcing, and forced-colouring polynomials. No equivalent coefficient formula or recurrence was located.

The main unresolved coverage risk is G. E. Farr, *On Problems with Short Certificates*, Acta Informatica 31 (1994), 479--502. The 2026 paper cites it for the complexity of deciding whether a fixed partial 3-colouring forces a full colouring. Bibliographic metadata and the later description were inspected, but the full 1994 text was not inspected. It may contain path-specific structural observations, although no located evidence suggests the enumerative formula proved here. Unindexed or differently-termed work remains a residual risk.

## Value

**PASS.** The theorem determines the complete forcing-domain distribution for 3-colouring a path, not just the total probability. Combined with known results at \(\lambda=2\) and for \(\lambda\ge4\), it gives the entire forced-colouring function of every path for every positive number of colours. It also yields a two-term Fibonacci-type recurrence, an exact minimum forcing-domain size and count, exponential enumeration at the uniform point, and a concrete correction to a current low-order example.

## Limitations

- The new coefficient theorem is specific to paths and three colours.
- The \(\lambda=2\) and \(\lambda\ge4\) branches of the all-colour path formula are consequences of results already present in the 2026 source.
- The full 1994 paper on forcing and short certificates was not inspected; it is the strongest identified residual prior-coverage risk.
- Finite exhaustive computation supports but does not replace the proof.
- Unindexed recent work or substantially different terminology may conceal equivalent results.
- Independent audit has not been performed.

Same-model review: passed. Independent audit: not yet performed.
