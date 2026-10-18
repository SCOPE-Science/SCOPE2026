# Gaussian angular spectra and a sharp balance law for rank-two matroid base polytopes

## Finding
Let a loopless rank-two matroid have \(m\ge 2\) nonempty parallel classes \(A_1,\ldots,A_m\) of positive sizes \(a_1,\ldots,a_m\), with \(n=\sum_i a_i\). In its canonical Euclidean realization
\[
P=\operatorname{conv}\{e_x+e_y:x\in A_i,\ y\in A_j,\ i\ne j\}\subset\mathbb R^n,
\]
let \(p_{xy}\) denote the spherical measure, in the intrinsic affine-direction space, of the outward normal cone of the vertex \(e_x+e_y\). Equivalently, \(p_{xy}\) is the probability that an isotropic Gaussian linear objective exposes that vertex. Then, **for every** \(x\in A_i\), \(y\in A_j\), \(i\ne j\),
\[
\boxed{p_{xy}=\frac1n\left(\frac1{n-a_i}+\frac1{n-a_j}\right).}
\]
Consequently, the probability that \(s\ge2\) independent isotropic Gaussian directions expose the same vertex is
\[
\boxed{C_s(P)=\sum_{i<j}a_i a_j\left[\frac1n\left(\frac1{n-a_i}+\frac1{n-a_j}\right)\right]^s.}
\]
In particular, setting \(b_i=a_i/(n-a_i)\) yields
\[
\boxed{C_2(P)=\frac1{n^2}\left(\sum_i b_i+2\sum_{i<j}b_ib_j\right).}
\]
For fixed positive integers \(n,m\) with \(2\le m\le n\), this collision probability is **strictly Schur-convex** in the ordered parallel-class sizes: every nontrivial transfer of one element from a class to another class of at least equal size strictly increases \(C_2\). Thus it is minimized, uniquely up to reordering, by classes as equal as possible, and maximized, uniquely up to reordering, by \((n-m+1,1,\ldots,1)\). When \(n=m\) or \(n=m+1\), there is only one size partition, so these descriptions refer to the same orbit. For fixed \(m\ge2\), as \(n\to\infty\), the minimum and maximum obey respectively
\[
\boxed{C_{2,\min}\sim\frac{2m}{(m-1)n^2},\qquad C_{2,\max}\sim\frac1{(m-1)n}.}
\]
The angular spectrum is uniform exactly when \(m=2\) or all class sizes are equal.

A further distinction holds even at the level of two face counts. The class-size vectors \((1,4,5,8)\) and \((2,2,7,7)\) each yield \(109\) vertices and \(1250\) edges, but their Gaussian collision probabilities are, respectively,
\[
\frac{11581}{1253070}\quad\hbox{and}\quad\frac{11617}{1254528},
\qquad
\boxed{\frac{11617}{1254528}-\frac{11581}{1253070}=\frac{2151}{119799680}>0.}
\]
Thus two initial face numbers do not determine the canonical Gaussian angular collision probability, even for rank-two matroid base polytopes.

## Assumptions and scope
All classes have positive integer sizes and the matroid is loopless and of rank two. Every basis contains exactly two elements in different parallel classes. A Gaussian objective is an isotropic centered standard Gaussian in the linear span of differences of vertices (equivalently, the orthogonal projection of an ambient vector of independent standard normal coordinates). Ties in objective values occur with probability zero. The angular normal cones are **outward normal cones**, not the interior/tangent solid angles used in lattice-point solid-angle sums. Disconnected two-class matroids are included: the relevant linear span has dimension \(n-2\), while for at least three classes it has dimension \(n-1\). All conclusions refer to the canonical zero-one Euclidean embedding, not arbitrary affine images.

## Proof
**1. Every specified pair is an exposed vertex.** A basis \(\{x,y\}\) from distinct classes is exposed by a linear functional with strictly larger positive coordinates at \(x,y\) and very negative coordinates elsewhere. Alternatively, each zero-one basis vector is extreme among distinct zero-one vectors of constant coordinate sum. There are no other bases.

**2. Normal-cone angles.** Let \(g_1,\ldots,g_n\) be independent standard normal scores. In decreasing score order, the matroid greedy algorithm first selects the global maximum \(x\) and then selects the highest-scoring coordinate \(y\) outside the parallel class of \(x\). This is optimal: any basis contains at most one element of the top class; if a proposed basis omitted the global maximum, replacing its member of that class (or an element in some other class) by the global maximum cannot decrease the sum, and the best independent second element is the largest score outside the chosen class. More directly, for any basis \(\{u,v\}\), ordering the overall top \(x\), either \(u,v\) both avoid its class, in which case \(g_x\) can replace one, or exactly one lies in its class, in which case \(g_x\) improves that member. Thus all optimum bases contain \(x\), and the second is best outside its class. The rank-two argument also covers a negative-valued optimum.

The score ordering is a uniform permutation. The event that \(x\) is globally first and \(y\) is first among the \(n-a_i\) coordinates outside \(A_i\) has probability \(1/[n(n-a_i)]\); the disjoint reversed event has probability \(1/[n(n-a_j)]\). Summing gives the asserted \(p_{xy}\). The affine difference space is orthogonal to the redundant constant-score directions, so projecting the ambient Gaussian leaves the maximizer unchanged and yields an isotropic Gaussian intrinsic direction. Rotational invariance identifies probability with spherical normal-cone measure. Summing \(p_{xy}\) over all bases gives one; each \(C_s\) follows by independence of the \(s\) objectives.

**3. Collision identity.** Expand
\[
 n^2 C_2=\sum_{i<j}a_i a_j\left(\frac1{n-a_i}+\frac1{n-a_j}\right)^2.
\]
The squared terms combine into \(\sum_i a_i/(n-a_i)\), because \(\sum_{j\ne i}a_j=n-a_i\); the mixed terms combine into \(2\sum_{i<j}b_i b_j\). This proves the closed form.

**4. Strict balance law.** On the open domain of positive real \(a_i<n\) with fixed sum \(n\), set \(F=n^2C_2\). Temporarily regard \(n\) as a fixed parameter when differentiating the expression of Step 3. For \(i\ne j\) and \(T=\sum_{k\ne i,j}a_k/(n-a_k)\), direct common-denominator calculation gives
\[
\boxed{\frac{\partial F}{\partial a_i}-\frac{\partial F}{\partial a_j}
=\frac{n(a_i-a_j)\left[a_i+a_j+2(2n-a_i-a_j)T\right]}
{(n-a_i)^2(n-a_j)^2}.}
\]
The bracket is strictly positive. If \(a_i>a_j\), increasing \(a_i\) and decreasing \(a_j\) by a small positive amount strictly increases \(F\), and the same holds throughout any admissible finite transfer. Strict convexity along a transfer in the reverse direction can equivalently be seen by replacing the pair with more equal values: the derivative has the sign of their difference. This is the strict pairwise-transfer criterion for Schur-convexity. For integer sizes, repeated transfers from a larger class to a smaller class differing by at least two decrease the collision probability until sizes differ by at most one. Repeated transfers from any class of size at least two into a class at least as large strictly increase it until only one class is nonsingleton. These yield both equality classifications.

For fixed \(m\), at balanced sizes \(a_i=n/m+O(1)\), each per-vertex cone probability is \(2m/((m-1)n^2)+O(n^{-3})\), and there are \((m-1)n^2/(2m)+O(1)\) bases. For the maximally unbalanced partition, \(n-m+1\) large-class elements each pair with \(m-1\) singleton elements; their cone probabilities are \(1/[(m-1)n]+O(n^{-2})\), while the bounded number of singleton-singleton pairs contribute a lower-order term. These observations prove the two stated asymptotics.

**5. Uniform angular spectrum.** With two classes, every vertex has probability \(1/(a_1a_2)\). With three or more classes, equality of all values \(p_{xy}\) requires all \(1/(n-a_i)+1/(n-a_j)\) to be equal. Comparing pairs sharing one class forces \(a_i=a_j\) for all classes. Conversely, equal class sizes plainly give equal probabilities.

**6. Coincident vertex and edge counts with different collisions.** The number of bases, hence of vertices, is \(f_0=\sum_{i<j}a_ia_j\). By the standard matroid basis-exchange edge criterion, two base vertices are adjacent exactly when their bases share one element; fixing the common element in class \(i\) leaves \(n-a_i\) possible partners, and each edge is counted once. Thus \(f_1=\sum_i a_i\binom{n-a_i}{2}\). Both displayed class-size vectors at \(n=18\) give \(f_0=109\) and \(f_1=1250\). Substitution into the closed collision formula produces the two exact rational values and their strictly positive difference.

## Verification
The standalone Python checker `check.py` uses only the Python standard library and exact rational arithmetic. Run `python3 check.py` from the directory containing this document and the checker. It exhausts every ordering of labels for each of the \(58\) nontrivial integer class partitions with \(2\le n\le8\), independently constructs the greedy exposed basis, and compares each per-basis frequency against the closed probability formula. It separately checks \(3065\) integer reverse-Robin-Hood transfers for strict collision growth through \(n=15\), all related minimizing/maximizing bounds, and the exact \(18\)-element two-face-number example. This finite replay supplements but does not replace the proof for all \(n\). The statements about strictness, asymptotic rates and all class sizes are deduced analytically in Steps 1–6.

## Relationship to prior work
Pineda-Villavicencio and Schröter (2020/2022) establish the canonical base-polytope setting, basis-exchange graph criterion, and reconstructibility questions (especially their Sections 3–4); they do not calculate the intrinsic Gaussian normal-cone measures or the balance extremizers here. Jochemko and Ravichandran (2019/2022) treat generalized permutahedra and lattice solid-angle polynomials; their Section 4.3 concerns *tangent/interior* solid angles at lattice points and therefore does not imply these outward normal-cone probabilities. The classical matroid greedy algorithm is used as known mathematics.

A previously described deletion formula for sparse-paving matroids covers the special rank-two situation where every nontrivial parallel class has size two and its excluded pairs are disjoint. The present claim covers arbitrary positive parallel-class sizes, proves the new global strict majorization theorem, and exhibits the two-face-number angular separation; the special case is not claimed as newly discovered. Related treatments of rank-two matroid Euclidean inradii, Minkowski asymmetry, and basis-exchange graph spectra determine different functionals, and neither those statements nor their parameters imply the Gaussian angular distribution or its strict collision extremizers.

## Limitations
The extremal result is for two-direction collision \(C_2\); the explicit formula for \(C_s\) does not assert Schur-convexity for other \(s\). Equality of the first two face counts in the example does **not** assert equality of the complete face vector or abstract graphs. The theorem does not assert robustness under nonspherical Gaussian covariance, arbitrary affine embeddings, higher matroid rank, or matroids with loops. No assertion of independent external validation is made. Although targeted mathematical-record and primary-literature comparisons revealed no general covering theorem, an equivalent probability law under random-order matroid greedy terminology may predate this work.

## References
1. G. Pineda-Villavicencio and B. Schröter, *Reconstructibility of matroid polytopes*, arXiv:2010.10227 (first posted 2020-10-20); SIAM J. Discrete Math. 36 (2022), 490–508. https://arxiv.org/abs/2010.10227
2. K. Jochemko and M. Ravichandran, *Generalized permutahedra: Minkowski linear functionals and Ehrhart positivity*, arXiv:1909.08448 (first posted 2019-09-18); Mathematika 68 (2022), 217–236. https://arxiv.org/abs/1909.08448
3. J. Oxley, *Matroid Theory*, 2nd ed., Oxford University Press (2011). Used for standard rank-two parallel classes and the matroid greedy property, not as a claim of originality.
