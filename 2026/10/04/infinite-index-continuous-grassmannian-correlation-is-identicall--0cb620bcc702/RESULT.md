# Infinite-index continuous Grassmannian correlation is identically one
## Finding
Let \(\mathcal H\) be a nonzero finite-dimensional Hilbert space over \(\mathbb R\) or \(\mathbb C\), and let \(\Omega\) be an infinite set. For every family of unit vectors \(\{\tau_\alpha\}_{\alpha\in\Omega}\subset\mathcal H\),
\[
\sup_{\alpha\ne\beta}|\langle\tau_\alpha,\tau_\beta\rangle|=1.
\]
If \(\mathcal H\) is real, the signed version also satisfies
\[
\sup_{\alpha\ne\beta}\langle\tau_\alpha,\tau_\beta\rangle=1.
\]

Therefore the pointwise supremum correlation introduced in Definition 3.7 of arXiv:2109.09296v1 is constant on the entire class of normalized continuous frames whenever the index set is infinite: its value is always \(1\). Hence, whenever at least one normalized continuous frame exists, every normalized continuous frame is a continuous Grassmannian frame according to Definition 3.8, and the infimum in that definition is \(1\).

A concrete existence consequence is available on finite positive nonatomic measure spaces. If \(0<\mu(\Omega)<\infty\) and \(\mu\) is nonatomic, then for each integer \(d\ge1\) there is a measurable partition \(\Omega=E_1\sqcup\cdots\sqcup E_d\) with \(\mu(E_j)=\mu(\Omega)/d\). For an orthonormal basis \(e_1,\ldots,e_d\), setting \(\tau_\alpha=e_j\) on \(E_j\) produces a normalized tight continuous frame. Thus continuous Grassmannian frames exist on every such measure space, but the stated Grassmannian optimization is degenerate there.

For real finite-dimensional Hilbert spaces, the same compactness argument also forces the signed supremum used in arXiv:2311.07606v1 to equal \(1\) on every infinite index set.

## Assumptions and scope
The compactness statement needs only three assumptions: \(\mathcal H\) has finite positive dimension, every \(\tau_\alpha\) has norm \(1\), and \(\Omega\) is infinite. No topology, measure, measurability, Bessel bound, or frame inequality on \(\Omega\) is needed for that statement.

The continuous-frame consequences use the definitions in arXiv:2109.09296v1, where normalized means \(\|\tau_\alpha\|=1\) for every index. The nonatomic existence statement additionally assumes a finite positive nonatomic measure. The signed conclusion is asserted only over \(\mathbb R\).

## Proof
Fix \(r>0\). The unit sphere of finite-dimensional \(\mathcal H\) is compact, hence totally bounded, so finitely many open balls of radius \(r\) cover it. Because \(\Omega\) is infinite, two distinct indices \(\alpha\ne\beta\) have \(\tau_\alpha\) and \(\tau_\beta\) in the same covering ball. Consequently
\[
\|\tau_\alpha-\tau_\beta\|<2r.
\]
For unit vectors,
\[
\operatorname{Re}\langle\tau_\alpha,\tau_\beta\rangle
=1-\frac12\|\tau_\alpha-\tau_\beta\|^2
>1-2r^2.
\]
In the complex case,
\[
|\langle\tau_\alpha,\tau_\beta\rangle|
\ge \operatorname{Re}\langle\tau_\alpha,\tau_\beta\rangle,
\]
and in the real case the same estimate directly bounds the signed inner product. Since \(r>0\) is arbitrary, the relevant supremum is at least \(1\). Cauchy--Schwarz gives the reverse bound \(1\), proving both equalities.

For the nonatomic existence statement, split \(\Omega\) into measurable sets \(E_1,\ldots,E_d\) of equal measure and set \(\tau_\alpha=e_j\) on \(E_j\). Then for every \(h=\sum_{j=1}^d h_j e_j\),
\[
\int_\Omega |\langle h,\tau_\alpha\rangle|^2\,d\mu(\alpha)
=\sum_{j=1}^d \mu(E_j)|h_j|^2
=\frac{\mu(\Omega)}d\|h\|^2.
\]
Thus the family is a normalized tight continuous frame. Because the index set of a positive nonatomic measure space is infinite, the compactness result applies and its continuous frame correlation is \(1\). The same applies to every other normalized continuous frame on that index set.

## Verification
The proof is purely analytic and has no computational or asymptotic certificate. Its quantifiers were checked in the following boundary cases.

If the family repeats a unit vector at two distinct indices, the supremum is attained at \(1\). If the family has infinitely many distinct vectors, compactness produces distinct-index pairs with distance arbitrarily close to \(0\), so the supremum is still \(1\) even if it is not attained. Finite cardinality is essential: finite Grassmannian packings can have correlation strictly below \(1\). Finite dimension is also essential: an infinite orthonormal family in an infinite-dimensional Hilbert space has correlation \(0\).

The nonatomic construction is measurable because it is constant on each measurable partition cell, and its displayed identity supplies equal positive lower and upper frame bounds \(\mu(\Omega)/d\).

## Relationship to prior work
Krishna's arXiv:2109.09296v1 defines continuous frame correlation by the off-diagonal pointwise supremum and defines continuous Grassmannian frames by minimizing that quantity. It then asks in Question 3.9 for a classification of measure spaces and finite-dimensional Hilbert spaces admitting such frames. The same paper explicitly computes correlation \(1\) for its circle example, but does not state the general infinite-index compactness collapse. The present statement shows that the pointwise supremum carries no packing information at all once the index set is infinite and the Hilbert space is finite-dimensional.

Krishna's later arXiv:2311.07606v1 studies a signed continuous Rankin supremum for normalized continuous Bessel families in real Hilbert spaces. On infinite index sets in finite dimension, that signed supremum is likewise forced to \(1\), independently of the measure-theoretic lower bound.

Datta, Howard, and Cochran's work on the geometry of Welch bounds supplies integral continuous Welch estimates, while the finite Grassmannian-frame literature studies finite collections. Neither implication covers the pointwise infinite-index statement above: integral averages can remain nontrivial even though the off-diagonal pointwise supremum equals \(1\).

## Limitations
The result does not classify existence of normalized continuous frames on arbitrary measure spaces. It gives an explicit positive answer for finite positive nonatomic spaces and reduces continuous Grassmannian existence to normalized-frame existence whenever the index set is infinite.

The statement does not make integral quantities such as continuous frame potential or continuous RMS correlation trivial. It concerns only the pointwise off-diagonal supremum. It also does not apply to finite index sets or to infinite-dimensional Hilbert spaces, where genuine packing behavior can persist.

The literature comparison did not locate a published source making this compactness observation for the definitions above. Because the underlying compactness lemma is elementary, an unindexed or informal prior observation remains a residual originality risk.

## References
1. K. Mahesh Krishna, *Continuous Welch bounds with Applications*, arXiv:2109.09296v1, first public 2021-09-20; later published in *Communications of the Korean Mathematical Society* 38 (2023), 787--805, DOI 10.4134/CKMS.c220200.
2. K. Mahesh Krishna, *Continuous Rankin Bound for Hilbert and Banach Spaces*, arXiv:2311.07606v1.
3. S. Datta, S. Howard, and D. Cochran, *Geometry of the Welch bounds*, *Linear Algebra and its Applications* 437 (2012), 2455--2470; arXiv:0909.0206.
4. J. I. Haas IV and P. G. Casazza, *On the structures of Grassmannian frames*, arXiv:1703.01787.
