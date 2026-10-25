# Global distance-distribution reconstruction of metric roses with pendant edges

## Finding
Let \(G\) be the compact length-metric graph formed by attaching \(m\ge1\) circles of arbitrary positive circumferences \(c_1,\ldots,c_m\) and \(k\ge0\) compact pendant intervals of arbitrary positive lengths \(a_1,\ldots,a_k\) to a single common vertex. Let \(D\) be the shortest-path distance between independent points sampled from normalized arclength. Then the complete probability law of \(D\) determines \(m\), \(k\), every circle circumference, and every pendant-interval length up to permutation. Hence, within this entire class, equality of global pairwise-distance distributions implies isometry, including with repeated lengths and coincident singularity thresholds. The reconstruction is explicit and exact.

## Assumptions and scope
Every circle is a genuine metric loop attached at one vertex, every pendant interval attaches at one endpoint, lengths are strictly positive, there are finitely many edges, and \(m\ge1\). There are no other graph vertices of valence greater than two and no additional interconnections. Distances are intrinsic shortest-path lengths. Sampling is normalized one-dimensional Hausdorff measure. Write \(b_j=c_j/2\), \(T=\sum_i a_i+2\sum_j b_j\), and \(f\) for the density of \(D\) on positive distances. Values of \(f\) at isolated discontinuities are immaterial; its one-sided limits and derivatives in the distributional sense are determined by the probability law.

## Proof
For \(s>0\), define \(u_s(t)=\mathbf 1_{(0,s)}(t)\), extended as zero outside \((0,\infty)\), and \(x_+=\max(x,0)\). The distance from the shared vertex of a point at arclength coordinate \(x\) on a circle of circumference \(2b\) is \(\min(x,2b-x)\), so its pushforward arclength density on \((0,b)\) is \(2\). For an interval of length \(a\), the corresponding density is \(1\) on \((0,a)\). If the sampled points occupy distinct edges, every shortest route passes through the common vertex, and their distance is the sum of these radial distances. If both occupy the same interval, their ordered-pair distance density is \(2(a-t)_+\); if both occupy the same circle of circumference \(2b\), it is \(4b\,u_b(t)\). Thus the complete exact density identity for \(t>0\) is
\[
T^2 f(t)=2\sum_{i=1}^k(a_i-t)_+ +4\sum_{j=1}^m b_j u_{b_j}(t)+\sum_{e\ne e'}q_eq_{e'}(u_{s_e}*u_{s_{e'}})(t),
\]
where the final sum is over ordered pairs of distinct edges, \((s_e,q_e)=(a_i,1)\) for pendant intervals and \((s_e,q_e)=(b_j,2)\) for circles. The convolution is an elementary continuous piecewise-linear tent/trapezoid. In particular \(\int_0^\infty (u_s*u_v)(t)dt=sv\), and the above density integrates to one exactly.

The only jump discontinuities of \(f\) at positive distance come from the within-circle contributions \(4b_j u_{b_j}\). For every positive \(b\),
\[
\Delta f(b):=f(b+)-f(b-)=-\frac{4b}{T^2}\#\{j:b_j=b\}.
\]
Also \(f(0+)=2/T\). Consequently \(T\) and the full multiset \(\{b_1,\ldots,b_m\}\), including multiplicities, are recovered from the density jumps. This recovers \(m\), all loop circumferences, and total pendant length.

The right derivative at zero is determined by the linear expansions of the same-edge terms and by \((u_s*u_v)(t)=t\) for \(0<t<\min(s,v)\). It satisfies
\[
T^2 f'(0+)= k^2+4km+4m^2-3k-4m.
\]
For fixed integer \(m\ge1\), the right-hand side is strictly increasing as an integer function of \(k\ge0\): the consecutive difference is \(2k+4m-2>0\). Therefore \(k\) is recovered uniquely. If \(k=0\), the already recovered circles finish the reconstruction.

Suppose \(k\ge1\). The completely known circle-only contribution is
\[
B(t)=4\sum_j b_ju_{b_j}(t)+4\sum_{j\ne h}(u_{b_j}*u_{b_h})(t).
\]
On the positive half-line define the finite signed atomic distribution
\[
H=(T^2f-B)''+4k\sum_j\delta_{b_j}.
\]
Using \((u_s*u_v)''=-\delta_s-\delta_v+\delta_{s+v}\) on \((0,\infty)\), and \(2(a-t)_+''=2\delta_a\), the exact signed-atom identity is
\[
\boxed{H=C\sum_i\delta_{a_i}+2\sum_{i<\ell}\delta_{a_i+a_\ell}+4\sum_{i,j}\delta_{a_i+b_j},\qquad C=4-2k-4m<0.}
\]
This is an equality of distributions, including when several terms cancel at the same location. Let the currently reconstructed pendant lengths be a multiset \(S\), initially empty. Subtract from \(H\) all terms of the displayed right side that involve only pendant lengths already in \(S\): specifically subtract \(C\sum_{a\in S}\delta_a\), the pairwise known-known pendant sums with coefficient \(2\), and the known pendant-circle sums with coefficient \(4\). If unknown pendant lengths remain, let \(a_*\) be their least length. Every positive atomic term still involving an unknown pendant length occurs strictly above \(a_*\) because its other length is positive. Therefore the least remaining atom lies at \(a_*\), has strictly negative mass \(C\) times the multiplicity of \(a_*\), and uniquely recovers both. Repeat until all \(k\) pendant lengths are recovered. This constructive induction does not assume any distinctness of lengths or disjointness of thresholds, and proves the assertion.

For instance, take one circle of circumference \(2\) and two pendant lengths \(1\) and \(2\). At distance \(2\), the negative pendant-length atom and a positive interval-circle-sum atom cancel in the unprocessed distribution. The inductive subtraction recovers both lengths despite this cancellation; this illustrates why a naive catalog of visible second-derivative atoms is insufficient.

## Verification
The standalone `rose_verifier.py` reproduces the signed-atom identity and reconstructs the pendant-length multiset by exact rational arithmetic for 4,361 configurations with up to three circles and five pendants, explicitly including repeated lengths and coincident thresholds. It also independently checks exact total probability normalization across five heterogeneous topologies. Direct piecewise-polynomial numerical integration of five representative densities gave integral \(1\) to numerical precision. These computations are checks only; the all-real-length and arbitrary-number-of-edges assertion follows from the analytic density identity and induction.

## Relationship to prior work
Chazal and Sun (arXiv:1305.1172, first public version 2013-05-06) motivated metric-graph reconstruction from sampled metric data but require geometrically richer samples than the one-dimensional global distance law here. Mémoli and Needham (arXiv:1810.09646, 2018, Section 4 and Figure 11) establish the global/local distance-distribution framework, show that global distributions need not distinguish general metric graphs, and explicitly observe jumps at geodesic loops. Their Section 4.1 identifies a topology-recognition mechanism when geodesic loops form a homology basis, and Section 4.4 establishes local injectivity for metric trees; none of the inspected statements reconstruct all edge lengths of arbitrary one-vertex circle bouquets with pendant leaves by one global distribution. Earlier exact global reconstruction of loop-free metric stars provides the tree-only boundary of this claim; extending from stars is not merely formal because circle self-distances create discontinuities and mixed stem-circle sums cause exact cancellations.

## Limitations
The theorem is only for the specified one-common-vertex class with at least one actual circle, not general metric graphs, multivertex cycles, graph embeddings, or sampling with nonuniform density. The resulting reconstruction is mathematically exact, not necessarily numerically stable from finite noisy samples; detecting small jumps and distributional atoms from empirical data can be ill-conditioned. The source search and full-text inspection of the closest metric-graph distribution paper did not identify covering results, but no bibliographic search proves absolute priority. No independent audit has been performed.

## References
1. F. Chazal and J. Sun, *Gromov-Hausdorff Approximation of Metric Spaces with Linear Structure*, arXiv:1305.1172 (first posted 2013-05-06); https://arxiv.org/abs/1305.1172.
2. F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646, Section 4 (first posted 2018-10-23); https://arxiv.org/abs/1810.09646.
