# Mathematical assessment

## Correctness — PASS

The claimed inradius, circumradius, uniqueness of both optimal centers, and all contact families are supported by the full matching-polytope facet description and a self-contained Euclidean argument. Averaging under the vertex-permutation group reduces a maximal inball center to a common edge coordinate. The coordinate, degree and odd-set facet distances are then explicit; a monotone odd-set denominator and an exact comparison yield blossom control only for \(n=3,5,7\), a tie for \(n=4\), and degree control for \(n=6\) and all \(n\ge8\). Active facet equalities and coordinate lower bounds prove uniqueness.

A matching of size \(j\) has squared distance \(j(1-2q)+\binom n2q^2\) from \(q\mathbf1\). Its upper envelope over all matching sizes is minimized at \(q=\lfloor n/2\rfloor/\binom n2\) for \(n\ge3\); every maximum matching and no smaller matching lies on the outer sphere. Strong convexity gives circumcenter uniqueness, with the segment case \(n=2\) handled directly.

An independently developed facet-system LP directly optimized all center coordinates for \(n=2,\ldots,9\), checking 626 facet inequalities. Separate vertex enumeration checked 3,734 matching vertices and the complete contact lists for those finite instances. Exact symbolic checks verified the quadratic and balance identities. These are finite corroborations; the theorem for all \(n\) rests on the analytic proof.

## Originality — PASS, best of knowledge

The published matching-polytope facet theorem of Eisley, Matsushita and Vindas-Meléndez (2025, Proposition 3) supplies the combinatorial half-space description but does not compute the Euclidean ball radii or their facet contacts. Abreu, Costa, Nascimento and Patuzzi (2019) determine graph-theoretic skeleton degrees instead of Euclidean radii.

A more general published result, *Weighted Euclidean distance extrema survive fractional matching relaxation*, implies equality of integral and fractional **enclosing** balls. It overlaps one methodological component, but neither evaluates the exact complete-graph circumball nor addresses the genuine integral matching-polytope inradius and odd-set/degree-facet transition. A published spectral John ellipsoid theorem concerns maximum-volume ellipsoids of a different fractional body; a Kneser eigenpolytope result uses an orthogonal-projection/polar realization, not the full canonical matching polytope. Searches under matching-polytope, triangular-graph stable-set, blossom facet, insphere, inradius, circumradius and Chebyshev-center terminology did not identify a result implying the full classification. Search absence is not a priority certificate, and unindexed equivalent accounts remain possible.

## Mathematical value — PASS

Both radius invariants and contact sets are natural sharp metric data for a classical polytope family. The finite odd-blossom phase and its exact threshold expose geometric information not readable from the facet theorem without solving the normalized optimization problem. The outer contacts identify maximum matchings geometrically. The theorem does not claim general graph formulas or affine invariance.

## Primary sources and boundaries

- B. Eisley, K. Matsushita and A. R. Vindas-Meléndez, *Matching Polytopes, Gorensteinness, and the Integer Decomposition Property*, Graphs and Combinatorics 41 (2025), article 58; DOI 10.1007/s00373-025-02923-8, especially Proposition 3.
- N. M. M. Abreu, L. M. G. C. Costa, C. H. P. Nascimento and L. Patuzzi, *A Note on the Matching Polytope of a Graph*, TEMA 20 (2019), 189–196; DOI 10.5540/tema.2019.020.01.0189, Theorems 4 and 9.
- *Weighted Euclidean distance extrema survive fractional matching relaxation*, published mathematical finding, 2026; its main theorem concerns farthest squared distances and enclosing balls, not inner facet distances.
- *Spectral John ellipsoids of vertex-and-edge-transitive fractional matching polytopes*, published mathematical finding, 2026; fractional body and maximal-volume ellipsoid objective.
- *Parity-controlled John and Löwner ellipsoids of Kneser pair-eigenpolytopes*, published mathematical finding, 2026; distinct orthogonal spectral space.

No proof-assistant verification or external expert attestation is claimed. The statement concerns the canonical edge-coordinate metric, and its historical priority remains subject to independent expert and archive checking.
