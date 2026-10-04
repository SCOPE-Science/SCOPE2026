# Same-model review

## Correctness — PASS
The proof reduces the main estimate to a linear operator on the Banach space of bounded bilinear maps: \(D(h)=h^{\square}-h^{\diamond}\). Each Arens extension preserves the bilinear norm, so \(\lVert D(h)\rVert\le2\lVert h\rVert\). The reverse triangle inequality yields the claimed \(2\)-Lipschitz law. The distance estimate follows immediately by comparing with any product having \(D=0\).

The sharpness example was checked symbolically. Its multiplication has norm \(1\), all triple products vanish, and the triangular sign matrix has opposite iterated free-ultrafilter limits \(1\) and \(-1\). Thus its Arens gap is exactly \(2\), while the zero multiplication is regular at distance \(1\).

## Originality — PASS
The closest source, arXiv:2609.11379v1, proves separate perturbation bounds for the two Arens products and qualitative persistence of irregularity. It does not state the intrinsic norm gap, the global metric inequality, the distance-to-regularity lower bound, or the sharp nilpotent example. published-finding corpus searches using source IDs, gap/defect aliases, distance language, and the exact constant found no covering result. The 2021 extreme-irregularity literature uses WAP and topological-center size rather than this norm invariant. The 1991 stability paper's inspected theorem summary concerns preservation under constructions, not a norm-gap modulus.

Residual originality risk remains that an older bilinear-map paper may contain the same short inequality under different notation.

## Value — PASS
A qualitative openness statement becomes a sharp quantitative geometry statement on the space of multiplications. The number \(\Delta_A(m)/2\) is an explicit certified radius that excludes every Arens-regular associative product, and the constant is attained by a simple nilpotent algebra. This directly clarifies how robust non-Arens regularity can be measured in multiplication norm.

## Closest literature and limitations
The result is a quantitative refinement of Rajoriya's 2026 perturbation argument, not a replacement for finer notions such as extreme or strong Arens irregularity. It gives a universal lower bound on distance to the regular locus; only the exhibited nilpotent example is shown to attain equality.

Same-model review: passed. Independent audit: not yet performed.
