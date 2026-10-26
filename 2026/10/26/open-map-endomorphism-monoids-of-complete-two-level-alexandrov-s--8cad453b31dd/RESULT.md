# Open-map endomorphism monoids of complete two-level Alexandrov spaces

## Finding
Let \(P_{p,q}\), for positive integers \(p,q\), be the finite \(T_0\) Alexandrov space whose specialization order has \(p\) pairwise incomparable lower points, \(q\) pairwise incomparable upper points, and every lower point below every upper point. Let \(\operatorname{OC}(P_{p,q})\) be its monoid of selfmaps that are both continuous and open. These maps are equivalently order-preserving maps \(f\) satisfying \(f(\uparrow x)=\uparrow f(x)\) for every point \(x\). The entire monoid has the following explicit structure.

For \(q\ge2\), there is a submonoid \(T_p\times S_q\): arbitrary transformations on the lower level and permutations on the upper level. Besides it, there are exactly \(q\) constant maps \(c_u\) to upper points \(u\). These constants form a two-sided ideal with \(c_u\circ g=c_u\) and \(g\circ c_u=c_{\sigma_g(u)}\) for \(g\in T_p\times S_q\). Thus
\[
|\operatorname{OC}(P_{p,q})|=p^p q!+q\qquad(q\ge2).
\]
For \(q=1\), the monoid is precisely the full transformation monoid on \(p+1\) points fixing the unique top point, of cardinality \((p+1)^p\). These statements include \(p=1\) and distinguish the genuine one-upper-point boundary.

In particular, for \(q\ge2\) the number of idempotents is \(\sum_{j=1}^p\binom pj j^{p-j}+q\), while for \(q=1\) it is \(\sum_{j=0}^p \binom pj(j+1)^{p-j}\).

## Assumptions and scope
The topology consists of all upsets of the stated finite order. Here \(T_p\) denotes all maps of the \(p\)-element lower set, and \(S_q\) the permutations of the \(q\)-element upper set. All counts are for labelled points. The result concerns open **and** continuous selfmaps, not all continuous maps; non-surjective maps are permitted. No valuations or proposition-preservation assumptions are imposed. Some authors reserve “p-morphism” for surjective bounded morphisms, so that label is avoided here.

## Proof
In any finite Alexandrov space of upsets, order preservation is equivalent to continuity. The image of an arbitrary upset \(U\) under an order-preserving \(f\) is an upset precisely when each principal upset satisfies \(f(\uparrow x)=\uparrow f(x)\); the forward inclusion is automatic, while openness gives the reverse one because the image is an upset containing \(f(x)\).

Every upper point \(u\) has \(\uparrow u=\{u\}\). Hence the equality forces \(\uparrow f(u)=\{f(u)\}\), so \(f(u)\) is also upper. If some lower point \(a\) maps to an upper point \(v\), order preservation forces \(f(u)=v\) for all upper \(u\), since these images are upper and must lie above \(v\). If \(q\ge2\), no other lower point \(b\) can map lower: openness at \(b\) would require the image of its principal upset to contain all \(q\) upper points, whereas the upper image is the singleton \(\{v\}\). All lower points therefore map to \(v\), making \(f\) constant. This gives exactly \(q\) maps.

Otherwise every lower point maps lower. At each lower point \(b\), openness requires the images of the \(q\) uppers to contain all \(q\) upper points. Because there are only \(q\) upper source points, their images form a permutation. Conversely, every arbitrary transformation of the lower points and permutation of the upper points is monotone and satisfies the principal-upset equality. This proves the \(q\ge2\) classification, including the composition laws. For \(q=1\), the single upper point must be fixed; each lower point independently has any of the \(p+1\) images, which gives the asserted pointed transformation monoid. Idempotents in \(T_p\) are obtained by choosing a nonempty fixed-point set of size \(j\), then mapping the remaining \(p-j\) points into it. For transformations fixing a distinguished top, choose \(j\) additional fixed points among the \(p\) lower points and map other points into the \(j+1\) fixed points; these give the formulas above.

## Verification
The accompanying standalone checker enumerates all selfmaps of \(P_{p,q}\) and checks separately order preservation and the principal-upset equality for every \(1\le p,q\le3\). It compares the exact counts to the theorem. All nine test pairs passed. The infinite two-parameter conclusion follows from the symbolic case split, not the finite experiments.

## Relationship to prior work
Vooijs and Fernández-Duque (2026) study Alexandrov dynamic topological logic and explicitly identify continuous maps with monotone maps on finite preorders, and define a surjective notion of p-morphism (sections 1, 2 and 8). This result makes a different exact enumeration and semigroup determination for maps satisfying the additional topological openness condition, without surjectivity. Separate investigations of full continuous mapping spaces of complete height-two finite posets concern larger map families and homotopy classes; their reported total counts do not specify the open-continuous submonoid. The distinction is substantive: arbitrary lower transformations are allowed only when the upper action is bijective (apart from upper constants).

## Limitations
The classification concerns complete two-level finite \(T_0\) spaces only, with every lower point below every upper point; it does not classify arbitrary finite Alexandrov spaces or arbitrary continuous maps. The generic topological characterization of openness is classical; the claim concerns its exact two-parameter specialization and monoid structure. Earlier semigroup literature may contain an equivalent enumeration under the name of bounded endomorphisms.

## References
1. N. C. Vooijs and D. Fernández-Duque, “Axiomatizability of Alexandrov Dynamic Topological Logic,” LICS 2026, article 81, DOI: 10.4230/LIPIcs.LICS.2026.81. First verified public release: 2026-07-09.
2. P. S. Alexandrov, “Diskrete Räume,” Recueil Mathématique, 1937.
3. Related continuous mapping-space work: “Mapping-space decomposition for complete height-two finite models” (2026), accessible summary record; further priority comparison with its complete proof remains desirable.
