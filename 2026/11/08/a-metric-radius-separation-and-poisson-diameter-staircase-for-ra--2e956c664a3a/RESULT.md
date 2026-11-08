# A metric-radius separation and Poisson diameter staircase for randomly thinned cubes

## Finding
Let \(Q_d=[0,1]^d\), \(d\ge2\). Retain each of its \(2^d\) vertices independently with probability \(p_d\in[0,1]\), form their convex hull \(K_d\), and denote its minimum enclosing Euclidean-ball radius and Euclidean diameter by \(R_d\) and \(\Delta_d\). Both are defined to be zero for the empty selection. Then the following asymptotic laws hold as the integer \(d\) tends to infinity.

**Sparse polynomial sample.** For every fixed real \(s>2\), take \(p_d=d^s2^{-d}\) for all sufficiently large \(d\). With probability tending to one the unique minimum enclosing ball of \(K_d\) is \(B_2((1/2,\ldots,1/2),\sqrt d/2)\), and
\[
\frac{\Delta_d^2}{d}\xrightarrow{\mathbb P}\frac12,\qquad
\frac{\Delta_d}{2R_d}\xrightarrow{\mathbb P}\frac1{\sqrt2}.
\]
In particular, the minimal containing sphere already matches the whole cube although the sampled convex hull typically has substantially smaller diameter.

**Near-antipodal staircase.** For every fixed integer \(j\ge0\) and every fixed constant \(c>0\), take \(p_d=c2^{-d/2}d^{-j/2}\) for all sufficiently large \(d\). The same unique cube circumball is optimal with probability tending to one. For the integer squared-diameter deficit \(H_d=d-\Delta_d^2\),
\[
\Pr(H_d=j)\longrightarrow1-\exp\!\left(-\frac{c^2}{2j!}\right),\qquad
\Pr(H_d=j+1)\longrightarrow\exp\!\left(-\frac{c^2}{2j!}\right),
\]
and the total probability of all other deficits tends to zero. When \(j=0\), the following identity holds in every dimension and for every retention probability \(p_d\):
\[
\Pr(\Delta_d^2=d)=1-(1-p_d^2)^{2^{d-1}}.
\]

## Assumptions and scope
All geometry is ordinary Euclidean geometry in the canonical \(0/1\)-coordinate realization. The sample law is independent Bernoulli vertex retention, not sampling uniformly from the cube interior, cube boundary, or a uniformly random graph of cube edges. The asymptotic statements hold for each fixed \(s>2\) or fixed pair \((j,c)\); they do not assert uniformity if these parameters vary with dimension. A square of the Euclidean distance between cube vertices equals their integer Hamming distance. Empty samples are assigned zero radius and diameter only to make the random variables total; their probability tends to zero in each asymptotic regime.

## Proof
Put \(N=2^d\), \(m=(1/2,\ldots,1/2)\). Every cube vertex \(v\) satisfies \(\|v-m\|_2^2=d/4\). If \(m\in K_d\), there are nonnegative \(\lambda_v\) summing to one with \(\sum_v\lambda_vv=m\). For any candidate center \(z\),
\[
\max_{v\in K_d}\|v-z\|_2^2
\ \ge\ \sum_v\lambda_v\|v-z\|_2^2
=\frac d4+\|z-m\|_2^2.
\]
The ball centered at \(m\) of radius \(\sqrt d/2\) contains all cube vertices. Therefore, on \(\{m\in K_d\}\), it is the *unique* minimum enclosing ball. This argument needs only that \(m\) belong to the convex hull, not that antipodal vertex pairs have been selected.

To show that the center is captured, if \(m\notin K_d\) then strict separation gives a linear functional positive on every selected translated vertex \(v-m\). Perturb its normal slightly to obtain a generic strict sign pattern. The number of sign patterns of generic homogeneous linear functionals on \(N\) points in \(\mathbb R^d\) is at most \(2\sum_{h=0}^{d-1}\binom{N-1}{h}\le2N^d\). By antipodal symmetry, any such positive halfspace contains at most \(N/2\) cube vertices. A union bound therefore yields, for every \(p_d\),
\[
\Pr(m\notin K_d)\le2N^d(1-p_d)^{N/2}
\le2\exp(d^2\log2-Np_d/2).
\tag{1}
\]
Both specified regimes satisfy \(Np_d/d^2\to\infty\), hence the right side vanishes.

For the polynomial sample, the expected number of unordered retained vertex pairs is at most \(N^2p_d^2/2=d^{2s}/2\). The Hamming distance between independent uniform cube vertices is \(\operatorname{Bin}(d,1/2)\). Hoeffding's bound and a union bound imply, for every fixed \(\varepsilon>0\),
\[
\Pr\{\Delta_d^2\ge(1/2+\varepsilon)d\}
\le\frac12d^{2s}e^{-2\varepsilon^2d}\longrightarrow0.
\]
The sample size has mean \(d^s\), so it exceeds two with probability tending to one. Conditional on having at least two sampled vertices, a uniformly chosen pair of distinct sampled vertices has exactly the distribution of a uniformly chosen pair of *distinct* cube vertices, by permutation symmetry of independent retention. Its Hamming distance, normalized by \(d\), converges in probability to \(1/2\). Since the diameter dominates that pair's distance, this proves \(\Delta_d^2/d\to1/2\). Combining with the exact radius proves the ratio statement.

For the near-antipodal scale, define the finite graph \(F_{d,j}\) on all cube vertices, connecting two distinct vertices if their Hamming distance is at least \(d-j\). For sufficiently large \(d>j\), every vertex has degree
\[
T_{d,j}=\sum_{h=0}^j\binom dh,
\quad |E(F_{d,j})|=2^{d-1}T_{d,j}.
\]
Let \(W_{d,j}\) count edges of \(F_{d,j}\) whose endpoints were both retained. The expectation at the specified sampling scale is
\[
\mu_{d,j}=2^{d-1}T_{d,j}p_d^2
=\frac{c^2 T_{d,j}}{2d^j}\longrightarrow\frac{c^2}{2j!}=:\lambda_j.
\]
For each fixed positive integer \(k\), expand the factorial moment \(\mathbb E(W_{d,j})_k\) over ordered collections of \(k\) *distinct* edges. Vertex-disjoint collections contribute \(\mu_{d,j}^k+o(1)\), because the fraction of such collections among all edge collections tends to one and each uses \(2k\) sampled vertices. For any overlapping collection, suppose its edge-union graph has \(t\) vertices in \(r\) connected components. Each component has at least two vertices, with at least one having three vertices, so \(t>2r\). Its labeled embeddings into a graph with \(N\) vertices and maximum degree \(T_{d,j}\) number at most \(C_kN^rT_{d,j}^{t-r}\) for a constant depending only on \(k\): choose one root per component and then a spanning forest. Multiplying by the retention probability \(p_d^t\) gives
\[
C_k N^{r-t/2}T_{d,j}^{t-r}d^{-jt/2}c^t
=O_{c,j,k}\!\left( N^{r-t/2}d^{j(t/2-r)}\right)=o(1).
\]
There are finitely many edge-union types for fixed \(k\). Thus all fixed factorial moments tend to \(\lambda_j^k\), and the method of moments yields \(W_{d,j}\Rightarrow\operatorname{Poisson}(\lambda_j)\). In particular \(\Pr(W_{d,j}=0)\to e^{-\lambda_j}\).

For \(j\ge1\), the expected number \(W_{d,j-1}\) of even closer pairs tends to zero (for \(j=0\), such a pair cannot exist). In contrast \(\mathbb EW_{d,j+1}\sim c^2d/[2(j+1)!]\to\infty\). Edge indicators on disjoint vertex sets are independent, while two distinct adjacent edges are simultaneously present with probability \(p_d^3\). Hence, for a universal constant, 
\[
\operatorname{Var}(W_{d,j+1})
\le\mathbb EW_{d,j+1}+2^{d}T_{d,j+1}^{2}p_d^3.
\]
The second term is exponentially small times a fixed polynomial in \(d\), and the mean diverges, so Chebyshev implies \(\Pr(W_{d,j+1}=0)\to0\). Consequently the event \(H_d=j\) differs by vanishing probability from \(\{W_{d,j}>0\}\), and the event \(H_d=j+1\) differs by vanishing probability from \(\{W_{d,j}=0\}\). This proves the two-point law. For \(j=0\), \(F_{d,0}\) consists exactly of \(N/2\) disjoint antipodal edges. Each is retained with probability \(p_d^2\), independently across edges, yielding the finite exact identity.

## Verification
An accompanying Python standard-library checker independently exhausts all \(2^{2^d}\) retention subsets for \(d=2,3,4\), compares exact rational full-diameter probabilities with the antipodal-pair formula for two retention probabilities, and verifies the graph edge count and all incident-edge-pair counts for deficit radii \(j\le2\) where \(j<d\). It also tests \(T_{d,j}/(2d^j)\to1/(2j!)\) at finite dimensions and makes independent seeded Bernoulli simulations of the critical-pair event in three configurations. The analytic argument above, not these finite calculations, establishes all-dimensional limits.

To reproduce: from a directory containing `verify.py`, execute `python verify.py`; it prints `BERNOULLI_CUBE_METRIC_CHECKS_PASSED` on success. There are no nonstandard Python dependencies.

## Relationship to prior work
The geometric model of independent random vertex retention is explicit in Newman's *Doubly random polytopes* (arXiv:2006.07000, first public 2020-06-12), but there the initial polytope itself is random and circumscribed about a sphere; its results concern face counts, approximation and facet geometry. Reitzner–Schütt–Werner (arXiv:1911.05917) study continuously sampled boundary points of a fixed simple polytope and their face/volume statistics. Dyer–Füredi–McDiarmid study volume thresholds for random cube-vertex polytopes. None of the examined statements implies this pair of exact Euclidean radius-versus-diameter regimes for Bernoulli-thinned cube vertices. The standard hyperplane-region bound, binomial concentration and Poisson factorial-moment method are established ingredients; the joint metric law is their specialized geometric consequence, not a claim to invent those tools.

## Limitations
The polynomial sample condition \(s>2\) is sufficient, not asserted sharp. The Poisson staircase requires fixed \(j\) and \(c\), and does not extend unchanged to deficits growing with \(d\). This result concerns Euclidean *metric* diameter and minimum enclosing sphere, not graph-theoretic diameter, expected volume, Hausdorff approximation, or affine-invariant radius. Uniform cubical interior samples and arbitrary point configurations are not covered. Older random \(0/1\)-polytope literature, especially inaccessible full-text results by Füredi (1986), presents a historical-priority uncertainty. Independent validation has not been performed.

## References
1. Andrew Newman, *Doubly random polytopes*, arXiv:2006.07000 (first version 2020-06-12); *Random Structures & Algorithms* 61 (2022), 364–382, DOI:10.1002/rsa.21059.
2. Matthias Reitzner, Carsten Schütt and Elisabeth Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first version 2019-11-14), *Discrete & Computational Geometry* 69 (2023), 453–504, DOI:10.1007/s00454-022-00460-2.
3. M. E. Dyer, Z. Füredi and C. McDiarmid, *Volumes spanned by random points in the hypercube*, *Random Structures & Algorithms* 3 (1992), 91–106, DOI:10.1002/rsa.3240030107.
4. Z. Füredi, *Random polytopes in the d-dimensional cube*, *Discrete & Computational Geometry* 1 (1986), 315–319, DOI:10.1007/BF02187704 (full text not inspected).
