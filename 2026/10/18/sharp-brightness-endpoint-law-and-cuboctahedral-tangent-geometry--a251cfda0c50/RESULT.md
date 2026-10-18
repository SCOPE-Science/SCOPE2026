# Sharp brightness endpoint law and cuboctahedral tangent geometry for the four-dimensional cross-polytope

## Finding
Let \(C_4=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3,\pm e_4\}\subset\mathbb R^4\), let \(U\) be Haar-uniform on \(S^3\), and let \(B(U)\) denote the three-dimensional Euclidean volume of the orthogonal projection of \(C_4\) onto \(U^\perp\). Normalize the random brightness as \(X(U)=3!B(U)/2^3\). Then \(1/\sqrt2\le X\le1\), and the following **distributional** results hold.

For the full interval \(0<t<1-\sqrt3/2\), the **exact near-maximum probability** is
\[
\boxed{\mathbb P\{X\ge1-t\}=\frac8\pi\left(\arccos(1-t)-(1-t)\sqrt{2t-t^2}\right).}
\]
At the opposite endpoint, as \(t\downarrow0\), the **sharp near-minimum probability** is
\[
\boxed{\mathbb P\{X\le1/\sqrt2+t\}=\frac{320\sqrt2}{\pi^2}t^3+O(t^4).}
\]
There are exactly 24 minimizing *directed* viewing directions, namely the unit vectors with precisely two nonzero coordinates of equal absolute value, and exactly eight maximizing directed directions, namely the signed coordinate axes. The extrema and sharp general Khintchine-type bounds are acknowledged as prior mathematics, **not** new claims here. The new geometric feature is that the tangent unit ball of the brightness deficit at each minimum, after a single coordinate rescaling, is exactly a cuboctahedron of Euclidean volume \(160/3\), yielding the probability constant above.

## Assumptions and scope
The metric is Euclidean and projections are orthogonal onto hyperplanes. The probability is normalized spherical area measure on \(S^3\); antipodal views represent the same hyperplane and count twice in directed extremizer enumeration. The theorem is specific to the four-dimensional regular cross-polytope under the stated coordinate normalization. It does not claim the entire brightness distribution, only the exact upper endpoint window and the sharp lower-tail asymptotic.

For any \(u\in\mathbb R^4\), define
\[
\Phi(u)=\frac1{16}\sum_{\varepsilon\in\{-1,1\}^4}|\varepsilon\cdot u|.
\]
Each of the 16 tetrahedral facets of \(C_4\) has volume \(2/6\) and outward unit normal \(\varepsilon/2\). Cauchy's polytope projection formula therefore gives
\[
B(u)=\frac1{12}\sum_{\varepsilon}|\varepsilon\cdot u|,
\qquad X(u)=\Phi(u),\quad\|u\|_2=1.
\]
The normalization is thus unambiguous and reconstructible directly from the original polytope.

## Proof
**1. Signed-average representation.** The homogeneous function \(\Phi\) is invariant under coordinate signs and permutations. Write the sorted absolute coordinate values of \(u\) as \(a\ge b\ge c\ge h\ge0\). Evaluating the sixteen signed sums gives the exact piecewise-linear expression
\[
\Phi(a,b,c,h)=\max\left\{a,\frac{a+b+c}{2},\frac{3a+b+c+h}{4}\right\}.
\]
One derivation averages over the sign of the fourth coordinate first using \((|y+h|+|y-h|)/2=\max(|y|,h)\), then evaluates the four unsigned first-three-coordinate combinations. The remaining branching depends only on \(p=a-b-c\) relative to \(\pm h\). The checker independently reconstructs the formula on a full grid of rational directions.

**2. Exact equality directions.** Jensen/Cauchy--Schwarz implies
\[
\Phi(u)=\mathbb E_\varepsilon|\varepsilon\cdot u|\le\sqrt{\mathbb E_\varepsilon(\varepsilon\cdot u)^2}=\|u\|_2.
\]
Equality demands that \((\varepsilon\cdot u)^2\) be constant for all sixteen sign vectors, hence all Walsh coefficients \(2u_i u_j\) with \(i\ne j\) must vanish. Thus precisely the eight signed coordinate axes maximize.

To identify all minima without invoking a nontrivial external equality-case theorem, subdivide the sorted nonnegative cone into \(p\ge h\), \(-h\le p\le h\), and \(p\le-h\). Their extreme rays are respectively
\[
\begin{aligned}
&\{(1,0,0,0),(1,1/3,1/3,1/3),(1,1/2,1/2,0),(1,1,0,0)\},\\
&\{(1,1/3,1/3,1/3),(1,1/2,1/2,0),(1,1,0,0),(1,1,1,1)\},\\
&\{(1,1/2,1/2,0),(1,1,0,0),(1,1,1,0),(1,1,1,1)\}.
\end{aligned}
\]
The lists are obtained by intersecting all triples of ordering and branch-boundary hyperplanes; the standalone checker reconstructs the sets exactly from rational determinants. Every ray \(v\) satisfies \(\Phi(v)^2\ge\|v\|_2^2/2\), with equality only on \((1,1,0,0)\). Because \(\Phi\) is linear on each cone and every vector is a nonnegative combination of its rays, \(\Phi(v)\ge\|v\|_2/\sqrt2\) throughout by the Euclidean triangle inequality; equality can occur only on the indicated ray. After signed permutations, the 24 directions \((\pm e_i\pm e_j)/\sqrt2\), with \(i<j\), are all and only the minimizers.

**3. Exact upper probability.** The two branches other than \(a\) are at most \(\sqrt3/2\) on the unit sphere. Indeed, the coefficient-vector Euclidean norms of \((a+b+c)/2\) and \((3a+b+c+h)/4\) are \(\sqrt3/2\) and \(\sqrt{12}/4=\sqrt3/2\). Hence the event \(\Phi(U)>\sqrt3/2\) occurs precisely when \(\max_i|U_i|>\sqrt3/2\), with \(\Phi(U)=\max_i|U_i|\) there. For \(0<t<1-\sqrt3/2\), the threshold event \(X\ge1-t\) is the disjoint union of eight coordinate-centered caps on \(S^3\). One cap with angular height threshold \(1-t\) has normalized probability
\[
\frac1\pi\left(\arccos(1-t)-(1-t)\sqrt{2t-t^2}\right).
\]
The eight caps give exactly the first boxed formula.

**4. Cuboctahedral tangent geometry.** Fix the minimum \(u_*=(e_1+e_2)/\sqrt2\) and choose its tangent basis \(q=(e_1-e_2)/\sqrt2,e_3,e_4\). Set
\[
u(s,z,w)=\frac{u_*+sq+ze_3+we_4}{\sqrt{1+s^2+z^2+w^2}}.
\]
For sufficiently small \(|s|+|z|+|w|\), conditioning the first two Rademacher signs on agreement or opposition yields the **exact local formula**
\[
\Phi(u(s,z,w))=\frac{1/\sqrt2+\frac12N(\sqrt2s,z,w)}{\sqrt{1+s^2+z^2+w^2}},
\]
where
\[
N(y,z,w)=\frac14\sum_{\eta,\theta\in\{-1,1\}}|y+\eta z+\theta w|
=\max\left\{|y|,|z|,|w|,\frac{|y|+|z|+|w|}{2}\right\}.
\]
This is a genuine norm. Since the denominator differs from one by order \(s^2+z^2+w^2\), the local brightness deficit has the uniform expansion
\[
\Phi(u(s,z,w))-1/\sqrt2=\frac12N(\sqrt2s,z,w)+O(s^2+z^2+w^2).
\]
Its first-order \(t\)-rescaled sublevel body is therefore exactly
\[
K=\{(s,z,w):N(\sqrt2s,z,w)\le2\}.
\]
In coordinates \(y=\sqrt2s\), this is the cuboctahedron
\[
\{|y|,|z|,|w|\le2,\quad |y|+|z|+|w|\le4\}.
\]
Its volume is the volume \(4^3=64\) of the containing cube, minus eight corner tetrahedra of volume \(2^3/6\) each, namely \(160/3\). Undoing the \(\sqrt2\) scaling gives \(\operatorname{vol}_3(K)=80\sqrt2/3\).

**5. From tangent volume to the sharp constant.** The Jacobian of the unit-sphere chart above is \((1+s^2+z^2+w^2)^{-2}=1+O(s^2+z^2+w^2)\). Because \(N\) is a norm, the exact local identity implies that the relevant sublevel set near \(u_*\) is trapped between homothetic copies \((t+O(t^2))K\) with relative scale \(1+O(t)\). Indeed the positive norm bounds the tangent-coordinate Euclidean norm, so every point with brightness deficit at most \(t\) has \(\|(s,z,w)\|=O(t)\), making the quadratic remainder uniformly \(O(t^2)\). It follows that one minimum contributes spherical volume
\[
\operatorname{vol}_3(K)t^3+O(t^4)=\frac{80\sqrt2}{3}t^3+O(t^4).
\]
The 24 minima are isolated, and compactness provides a positive brightness gap outside small disjoint neighborhoods. Hence for small \(t\) these are all the contributions. Since \(\operatorname{area}(S^3)=2\pi^2\), their total normalized probability is
\[
\frac{24}{2\pi^2}\frac{80\sqrt2}{3}t^3+O(t^4)
=\frac{320\sqrt2}{\pi^2}t^3+O(t^4).
\]
This proves the second boxed formula. The argument derives a continuum limit from a norm approximation and complete minimizer classification, not from finite random samples.

## Verification
Run `python3 verify.py` from the package directory. The standalone checker uses rational arithmetic to compare the signed-average formula with its explicit sixteen-sign definition on \(2400\) nonzero integer directions; reconstructs all extreme rays of the three linearity cones from rational facet determinants; and verifies the four-dimensional tangent norm identity on \(1331\) rational triples. It checks the cuboctahedron's volume exactly and compares the exact near-maximum formula with \(150000\) independent sampled unit directions. Its successful terminal marker is `ALL_CHECKS_OK`. The sampled checks are corroboration, never an infinite-dimensional or asymptotic proof.

## Relationship to prior work
The best Khintchine \(L^1\) constant and the global projection-volume endpoints are classical or previously established. Ivanov's 2018 cross-polytope projection paper treats exact extrema in lower projection ranks, and his 2026 all-dimensional maximal-projection theorem gives the upper bound and equality directions independently of the present argument. Neither inspected paper gives the **Haar brightness endpoint probabilities** or the **cuboctahedral tangent volume**. Kabluchko--Litvak--Zaporozhets (2015) study random **one-dimensional** projection lengths of regular polytopes; their moments and limits do not specify the four-dimensional body's **three-dimensional hyperplane** projection-volume tails. Böröczky--Henk (1997) treat random face counts, not those volume probabilities.

The relevant published exact Platonic-solid brightness-variance paper determines second moments, not these endpoint probabilities. A published three-dimensional regular-simplex projection endpoint theorem, combined with the known tetrahedron/octahedron brightness equivalence, covers the **three-dimensional** octahedral analogue. Accordingly **no three-dimensional tail law is part of the present new claim**. Likewise exact octahedral width and inradius distributions concern different invariants. The checked published-finding corpus records and recoverable local research claims contain no covering theorem for the *four-dimensional* brightness endpoint law, but searchable databases are not novelty certificates. A 2026 random-width/brightness preprint was accessible only in abstract form; complete historical priority remains provisional.

## Limitations
This result establishes a sharp three-dimensional **projection-volume** probability law for a **four-dimensional** convex body under Haar-uniform viewing. It neither gives the full distribution away from the endpoints nor an exact lower probability at finite thresholds. The proof's \(O(t^4)\) statement is a fixed-body small-threshold remainder, not a uniform family result. Generalizations to dimensions five or above, arbitrary affine images, and nonuniform viewing are not asserted. Independent external mathematical validation and definitive historical-priority verification have not been performed.

## References
1. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1, first public 26 November 2015, https://arxiv.org/abs/1511.08479.
2. K. Böröczky Jr. and M. Henk, *Random Projections of Regular Polytopes*, preprint SC-97-21 (1997), https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf.
3. G. Ivanov, *On the volume of projections of the cross-polytope*, arXiv:1808.09165v1, 28 August 2018, https://arxiv.org/abs/1808.09165.
4. G. Ivanov, *The maximal volume of projections of the cross-polytope*, arXiv:2607.12072v1, 13 July 2026, https://arxiv.org/abs/2607.12072.
5. U. Haagerup, *The best constants in the Khintchine inequality*, Studia Math. 70 (1981), 231--283, DOI:10.4064/sm-70-3-231-283.
6. E. Tsukerman and E. Veomett, *A Simple Proof of Cauchy's Surface Area Formula*, arXiv:1604.05815v1, 20 April 2016, https://arxiv.org/abs/1604.05815.
7. *Exact orientation-variance spectrum of Platonic shadow areas*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-orientation-variance-spectrum-of-platonic-shadow-areas--76ed33fc3859.
8. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202v1 (2026), https://arxiv.org/abs/2609.26202 (abstract read; no full-document noncoverage assertion).
