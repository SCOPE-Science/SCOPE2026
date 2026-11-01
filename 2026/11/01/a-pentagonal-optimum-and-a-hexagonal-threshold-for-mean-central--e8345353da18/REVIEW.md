# Scientific review: mean central sections of regular prisms

## Correctness — PASS

The claimed quantifiers are every integer \(n\ge5\) and every real \(h>0\), with base circumradius one and half-height \(h\). The exact expected section vertex count follows from the edge-crossing identity: a Haar-uniform normal separates two nonzero endpoint vectors of angle \(\theta\) with probability \(\theta/\pi\). A right regular prism has exactly \(n\) vertical and \(2n\) rim edges, and their endpoint angles are derived explicitly in the proof. Linearity of expectation requires no independence of edge crossings. Differentiation yields a strictly increasing scalar function governing the sign, proving the unique pentagonal maximum and monotonicity for all \(n\ge6\). Direct Taylor expansion proves the distinct cubic and linear high-aspect deficits. The critical half-height reduces algebraically to \((3+\sqrt5)/4\). All nongeneric plane intersections have zero Haar measure.

The standalone Python program (executed from its actual package path) compared 42 exact edge-angle sums, 294 derivative/asymptotic cases and 260,000 independent Gaussian-normal section observations. It printed `VERIFY_OK`, with maximum observed sample mean error 0.016526. These tests are corroborative, not an infinite proof.

## Originality — PASS, best-knowledge, with acknowledged priority risks

Closest primary text [1] was materially read, including the introduction, Proposition 3.6 on prism sections as slabs, and surrounding construction and reconstruction results. It classifies the geometry of possible sections but does not compute Haar expected vertex counts, optimize height, or identify a critical six-gon. The publicly available complete research result [2] gives the full central section law for three-dimensional rectangular boxes, which excludes the asserted \(n\ge5\) regular prism family. Complete published result [3] gives mean-square **width** for regular uniform prisms, a different random observable. Targeted published scientific-record searches for regular prism random central sections, aspect ratio, mean vertex/edge count, and a five/six threshold did not return an implication of the theorem. A previously developed **triangular** prism distribution was compared for scientific implication; it does not imply the result for \(n\ge5\).

Voss [4] and Ohser–Mücklich [5] are plausible earlier stereological literature. Only accessible abstracts and bibliographic information were available; their full papers were not inspected. Their stated sampling models involve sections from spatial or randomly placed planes rather than Haar center-passing normals, but an unrecognized equivalent result remains possible. The edge-angle probability identity is explicitly not claimed as an original lemma. The asserted novelty is the complete extremum and asymptotic phase classification for the natural infinite prism family.

## Mathematical value — PASS

The work addresses a natural scalar invariant: the expected combinatorial complexity of a random central section. It evaluates that invariant **exactly for every aspect ratio and for the entire regular polygon-base sequence**, then locates a sharp nontrivial geometric transition. A finite golden-ratio optimizer exists uniquely for the pentagonal prism, while no prism with at least six base sides has a finite-height optimizer; at six sides the approach to its supremum is cubic rather than linear. This exact structural classification is not an arbitrary small numerical instance and is motivated by current work on combinatorial sections. The calculation is elementary once the correct edge-angle reduction is recognized, but the coherent phase transition is a meaningful complete answer rather than a bare substitution or routine parameter increment.

## Limits and closest literature

The theorem is about expectations for central Haar planes, not full type laws or affine stereological sections. The closest accessible texts are [1] Birkemeyer et al., arXiv:2609.16195v1 (2026-09-14), Proposition 3.6, and published complete results [2] *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes* and [3] *Exact mean-square width of every uniform regular prism*. Possible priority sources [4] Voss (1982), DOI 10.1111/j.1365-2818.1982.tb00443.x and [5] Ohser–Mücklich (1995), DOI 10.2307/1427832, were not fully accessible. Independent mathematical validation remains unperformed.

Self-review: passed. Independent audit: not yet performed.
