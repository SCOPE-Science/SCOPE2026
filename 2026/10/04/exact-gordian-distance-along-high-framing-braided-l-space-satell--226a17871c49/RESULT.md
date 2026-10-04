# Exact Gordian distance along high-framing braided L-space satellite rays
## Finding
Let \(P\subset S^1\times D^2\) be a braided L-space satellite operator represented by the closure of a \(p\)-strand braid, with \(p\ge2\). Let \(K\subset S^3\) be a knot with Hom invariant \(\epsilon(K)=1\). For every pair of integers
\[
m,n\ge 2\tau(K),
\]
the ordinary Gordian distance between the corresponding framed satellites is
\[
 d_G(P(K,m),P(K,n))=\binom{p}{2}|m-n|.
\]
Here \(d_G\) is the minimum number of crossing changes needed to pass from one knot to the other, and \(P(K,r)\) uses the \(r\)-framed longitude in the satellite construction.

Thus, after multiplying the integer metric by \(\binom{p}{2}\), the high-framing sequence \(r\mapsto P(K,r)\) is an isometric ray in the Gordian graph. In particular, the evident full-twist route between consecutive framings is geodesic.

## Assumptions and scope
The satellite convention is the one in Chen--Zemke--Zhou: for a pattern \(P\) of winding number \(\ell\), the notation \(P(K,n)\) means that the solid torus containing \(P\) is identified with a neighborhood of \(K\) using the \(n\)-framed longitude. A closed \(p\)-strand braid oriented along the solid-torus core has winding number \(\ell=p\).

The theorem applies only in the affine range
\[
n\ge2\tau(K)
\]
from their L-space satellite formula and only when \(\epsilon(K)=1\). It makes no assertion about smaller framings, non-braided patterns, or patterns outside the L-space-satellite hypotheses.

The case \(m=n\) is included and gives distance zero.

## Proof
Chen--Zemke--Zhou prove that if \(\epsilon(K)=1\), the pattern is oriented with nonnegative winding number \(\ell\), and \(n\ge2\tau(K)\), then
\[
\tau(P(K,n))
=
 g_3(P)+\frac{\ell(\ell-1)}2n+\ell\tau(K).
\]
For a closed \(p\)-strand braid, \(\ell=p\). Therefore, whenever \(m,n\ge2\tau(K)\),
\[
\left|\tau(P(K,m))-\tau(P(K,n))\right|
=
\binom{p}{2}|m-n|.
\]

A single crossing change induces a genus-one cobordism between the two knots. The Ozsváth--Szabó invariant \(\tau\) is a concordance homomorphism bounded in absolute value by smooth four-ball genus, so one crossing change changes \(\tau\) by at most one. Hence any crossing-change sequence from \(P(K,m)\) to \(P(K,n)\) has length at least
\[
\binom{p}{2}|m-n|.
\]
This proves the lower bound.

For the upper bound, changing the satellite framing by one corresponds to inserting one full twist \(\Delta_p^2\) in the \(p\)-strand braid. This framing/full-twist equivalence is the standard braided-pattern convention and is stated explicitly, for example, in Hedden--Raoux's framing lemma for braided satellite patterns.

Use the pure-braid factorization
\[
\Delta_p^2
=
A_{12}(A_{13}A_{23})\cdots(A_{1p}A_{2p}\cdots A_{p-1,p}),
\]
where
\[
A_{ij}
=
\sigma_{j-1}\cdots\sigma_{i+1}\sigma_i^2
\sigma_{i+1}^{-1}\cdots\sigma_{j-1}^{-1}.
\]
There are exactly \(\binom{p}{2}\) factors \(A_{ij}\). Each is conjugate to \(\sigma_i^2\). Changing one of the two crossings in that central square turns it into \(\sigma_i\sigma_i^{-1}\), so after isotopy that factor disappears. Consequently one full twist can be removed using at most \(\binom{p}{2}\) crossing changes.

Repeating this operation \(|m-n|\) times gives
\[
d_G(P(K,m),P(K,n))
\le
\binom{p}{2}|m-n|.
\]
Together with the \(\tau\)-lower bound, this proves equality.

## Verification
The argument has two independent inequalities. The lower bound uses the exact affine \(\tau\)-formula in the high-framing range and the standard one-crossing Lipschitz property of \(\tau\). The upper bound is diagrammatic: the pure full twist contains one conjugate square for each unordered pair of braid strands, and one crossing change kills each conjugate square.

The count of pure-braid factors is
\[
1+2+\cdots+(p-1)=\binom{p}{2},
\]
so the lower and upper bounds coincide for every \(p\ge2\) and every allowed pair \(m,n\).

No finite experiment is used as a substitute for the proof. The proof does not require a classification of the satellites or an unknotting-number computation.

## Relationship to prior work
Chen--Zemke--Zhou obtain the affine formula for \(\tau(P(K,n))\) in the high-framing range. Their paper does not state a pairwise Gordian-distance theorem; targeted full-text searches for “Gordian”, “distance”, “crossing change”, and “unknotting” do not produce such a result there.

Their later work on unknotting number and L-space satellite operations gives lower bounds for unknotting numbers, including stronger bounds for braided operators. That problem compares a satellite with the unknot, whereas the present statement computes the exact pairwise crossing-change metric between two different framing values of the same satellite operator.

For cables, older formulas for \(\tau\) provide related special-case input. The statement here applies uniformly to every braided L-space satellite operator covered by the recent affine formula, and sharpness comes from the full-twist braid factorization.

## Limitations
The equality is proved only for \(m,n\ge2\tau(K)\) and \(\epsilon(K)=1\). No behavior is asserted across the threshold or in the \(\epsilon(K)\ne1\) regimes.

The result uses ordinary crossing changes and ordinary Gordian distance. It does not claim minimality for other move systems, concordance distance, band distance, or rational tangle replacements.

The theorem gives a metric statement about the knots \(P(K,n)\); it does not assert that distinct framing parameters always give distinct satellite operators before choosing the companion.

## References
1. D. Chen, I. Zemke, and H. Zhou, *Applications of the L-space satellite formula*, arXiv:2509.20288v1, first posted 2025-09-24.
2. P. Ozsváth and Z. Szabó, *Knot Floer homology and the four-ball genus*, Geometry & Topology 7 (2003), 615--639.
3. M. Hedden and K. Raoux, *A 4-dimensional rational genus bound*, Mathematische Annalen (2026), framing lemma for braided patterns.
4. D. Chen, I. Zemke, and H. Zhou, *Unknotting number and L-space satellite operations*, arXiv:2609.14520v1.
