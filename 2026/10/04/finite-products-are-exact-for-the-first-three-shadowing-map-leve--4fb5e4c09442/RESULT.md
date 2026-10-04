# Finite products are exact for the first three shadowing-map levels

## Finding
Let \(m\ge 1\). For nonempty compact metric spaces \((X_j,d_j)\) and homeomorphisms \(f_j:X_j\to X_j\), put
\[
X=\prod_{j=1}^m X_j,\qquad F=\prod_{j=1}^m f_j,
\]
and endow \(X\) with the max metric
\[
d_X((x_j),(y_j))=\max_{1\le j\le m} d_j(x_j,y_j).
\]
Then each of the following properties is equivalent for \(F\) and for all of its factors \(f_j\):

1. existence of a shadowing map;
2. existence of an L-shadowing map;
3. existence of a self-tuning pseudo-orbit map.

Equivalently, a finite Cartesian product belongs to any one of these first three levels of Artigue's shadowing-map hierarchy exactly when every factor belongs to that level.

## Assumptions and scope
All phase spaces are nonempty compact metric spaces and all dynamics are homeomorphisms. The product uses the max metric. For the sequence-space metric appearing in the self-tuning definition, fix one \(\mu\in(0,1)\) and use
\[
\widetilde d_s(x,y)=\sum_{k\in\mathbb Z}\mu^{|k|}d(x_k,y_k).
\]
Using one common \(\mu\) is harmless: on the compact sequence spaces the choices \(\mu\in(0,1)\) give uniformly equivalent metrics, and the self-tuning criterion used below is stable under replacing the metric by a uniformly equivalent one.

The statement is only for finite products. It does not claim an analogous reflection theorem for the stronger shift-invariant or dynamically-invariant levels of the hierarchy; the factor-extraction construction below does not preserve those exact commutation identities without additional hypotheses.

## Proof
For a homeomorphism \(f\) and \(\delta>0\), write \(\widetilde X(f,\delta)\) for its two-sided \(\delta\)-pseudo-orbits. Under the max product metric,
\[
\widetilde X(F,\delta)=\prod_{j=1}^m \widetilde X_j(f_j,\delta).
\]

Assume first that every factor \(f_j\) admits a pseudo-orbit map \(S_j\) of one of the three indicated types. Shrinking domains if needed, choose a common \(\delta>0\). Define
\[
S((x^1,\ldots,x^m))=(S_1(x^1),\ldots,S_m(x^m)).
\]
This map is continuous, and on every genuine orbit it returns the initial point coordinatewise, so it is a pseudo-orbit map for \(F\).

For ordinary shadowing maps, Artigue's Proposition 3.2 identifies a shadowing map with a pseudo-orbit map that induces the shadowing property. Given \(\varepsilon>0\), choose factor tolerances \(\gamma_j\) so that \(S_j\) \(\varepsilon\)-shadows every \(\gamma_j\)-pseudo-orbit. With \(\gamma=\min_j\gamma_j\), a product \(\gamma\)-pseudo-orbit splits into factor \(\gamma\)-pseudo-orbits, and the max metric gives
\[
d_X(F^iS(x),x_i)=\max_j d_j(f_j^iS_j(x^j),x_i^j)\le\varepsilon
\]
for all \(i\in\mathbb Z\). Hence \(S\) induces shadowing, so it is a shadowing map.

If every \(S_j\) is an L-shadowing map, let \(x\) be a product pseudo-orbit whose jumps tend to zero as \(|i|\to\infty\). Each coordinate pseudo-orbit has the same property. The factor maps both \(\varepsilon\)-shadow and limit-shadow their coordinates, and because there are finitely many factors,
\[
\max_j d_j(f_j^iS_j(x^j),x_i^j)\longrightarrow0.
\]
Thus the product selector is an L-shadowing map.

For self-tuning, use Artigue's Proposition 5.3. It says that a pseudo-orbit map is self-tuning exactly when, for every \(\varepsilon>0\), sufficiently small local sequence discrepancy
\[
\widetilde d_s(\sigma^i x,\operatorname{orb}_f(x_i))
\]
forces \(d(f^iS(x),x_i)\le\varepsilon\). For the max metric, each factor discrepancy is bounded by the product discrepancy. Taking the minimum of the finitely many factor thresholds therefore gives the product criterion, hence \(S\) is self-tuning.

Conversely, suppose that \(F\) has a pseudo-orbit map \(S\) of one of the three indicated types. Fix a factor index \(r\) and choose base points \(q_j\in X_j\) for \(j\ne r\). Embed a pseudo-orbit \(x=(x_i)_{i\in\mathbb Z}\) of \(f_r\) into a product pseudo-orbit \(I_r(x)\) by
\[
(I_r(x))_i=(f_1^i(q_1),\ldots,f_{r-1}^i(q_{r-1}),x_i,f_{r+1}^i(q_{r+1}),\ldots,f_m^i(q_m)).
\]
All coordinates except the \(r\)-th are genuine orbits. Define
\[
S_r(x)=\pi_r(S(I_r(x))).
\]
The map \(S_r\) is continuous. If \(x\) is a genuine orbit through \(p\in X_r\), then \(I_r(x)\) is the genuine \(F\)-orbit through the point with coordinates \(q_j\) and \(p\), so \(S_r(x)=p\). Hence \(S_r\) is a pseudo-orbit map.

If \(S\) is a shadowing map, Proposition 3.2 says it induces shadowing. A sufficiently accurate pseudo-orbit of \(f_r\) becomes, under \(I_r\), an equally accurate product pseudo-orbit; projecting an \(S\)-shadow gives an \(S_r\)-shadow. Therefore \(S_r\) induces shadowing and is a shadowing map.

If \(S\) is an L-shadowing map, then a two-sided limit pseudo-orbit of \(f_r\) becomes a two-sided limit pseudo-orbit of \(F\), because every other coordinate has zero jump error. Projecting the product shadow preserves both the uniform shadowing bound and convergence of the error to zero. Thus \(S_r\) is an L-shadowing map.

Finally suppose \(S\) is self-tuning. For the embedded pseudo-orbit, all non-\(r\) coordinates agree exactly with the corresponding orbit through \((I_r(x))_i\). Consequently
\[
\widetilde d_{s,X}(\sigma^iI_r(x),\operatorname{orb}_F((I_r(x))_i))
=
\widetilde d_{s,r}(\sigma^ix,\operatorname{orb}_{f_r}(x_i)).
\]
Apply Proposition 5.3 to \(S\) and project the resulting estimate
\[
d_X(F^iS(I_r(x)),(I_r(x))_i)\le\varepsilon
\]
to the \(r\)-th coordinate. This gives
\[
d_r(f_r^iS_r(x),x_i)\le\varepsilon,
\]
so Proposition 5.3 implies that \(S_r\) is self-tuning. Since \(r\) was arbitrary, every factor has the property.

## Verification
The proof was reconstructed directly from the defining quantifiers. The only nontrivial source reductions are Artigue's Proposition 3.2, which converts existence of a continuous pseudo-orbit selector inducing shadowing into the paper's shadowing-map definition, and Proposition 5.3, which replaces the self-tuning commutation estimate by a pointwise local-discrepancy estimate. Both are stated and proved in arXiv:2504.00171v1.

The factor-reflection step was checked separately for all three levels. The key construction inserts exact orbits in every passive coordinate, so product pseudo-orbit error, limit error, and the local sequence discrepancy reduce exactly to the active factor. No finite experiment or asymptotic computation is used.

## Relationship to prior work
Artigue introduces pseudo-orbit maps, shadowing maps, L-shadowing maps and self-tuning maps, and proves the hierarchy relations among them. The source explicitly shows that ordinary shadowing need not imply existence of a shadowing map: its pseudo-Anosov two-sphere example has shadowing but no shadowing map. Thus classical product theorems for the shadowing property do not imply the selector theorem proved here.

Full-text searches of arXiv:2504.00171v1 for Cartesian products and direct products found no product theorem for the new map hierarchy. Broader literature contains product-preservation statements for ordinary shadowing and other shadowing properties, and recent work proves an L-shadowing equivalence between a map and its induced hyperspace homeomorphism, but those statements concern existence of shadowing points or induced dynamics rather than continuous pseudo-orbit selectors with Artigue's axioms.

## Limitations
The theorem concerns only finite Cartesian products and the first three map levels: shadowing, L-shadowing, and self-tuning. It does not establish product reflection for shift-invariant or dynamically-invariant shadowing maps. The proof uses the max product metric and a common standard weighted sequence metric; no claim is made here about infinite products or noncompact phase spaces.

## References
1. A. Artigue, *Shadowing maps*, arXiv:2504.00171v1, 31 March 2025.
2. M. Antunes, B. Carvalho, W. Cordeiro, *L-shadowing for the induced hyperspace homeomorphism*, arXiv:2512.08677, 2025.
3. D. Thakkar, *On Nonautonomous Discrete Dynamical Systems*, International Journal of Analysis (2014), Article 538691.
