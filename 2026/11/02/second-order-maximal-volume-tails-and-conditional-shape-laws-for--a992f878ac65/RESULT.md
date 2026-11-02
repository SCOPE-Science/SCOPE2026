# Second-order maximal-volume tails and conditional shape laws for random simplices

## Finding
Let \(d\ge3\) be an arbitrary fixed integer and let \(\Delta\subset\mathbb R^d\) be any full-dimensional simplex. Take \(d+1\) independent points \(X_0,\ldots,X_d\) uniformly by volume from \(\Delta\). Define the affine-invariant random daughter-simplex volume fraction
\[
T=\frac{\operatorname{vol}_d\operatorname{conv}(X_0,\ldots,X_d)}{\operatorname{vol}_d(\Delta)},\qquad m=d(d+1).
\]
As \(\varepsilon\downarrow0\), the near-maximal volume probability has the sharp, universal **two-term** expansion
\[
\boxed{\mathbb P(T>1-\varepsilon)=
\frac{(d+1)!(d!)^{d+1}}{m!}\varepsilon^m
\left[1+\frac{m(d^2-1)}{2(m+1)}\varepsilon+O_d(\varepsilon^2)\right].}
\]
In dimension three the leading probability is
\[
\mathbb P(T>1-\varepsilon)=\frac{\varepsilon^{12}}{15400}
\left[1+\frac{48}{13}\varepsilon+O(\varepsilon^2)\right].
\]
In dimension four it is
\[
\mathbb P(T>1-\varepsilon)=\frac{\varepsilon^{20}}{2546168625}
\left[1+\frac{50}{7}\varepsilon+O(\varepsilon^2)\right].
\]
A complementary **conditional shape law** holds. Write \(v_0,\ldots,v_d\) for the parent vertices. Conditional on \(T>1-\varepsilon\), for sufficiently small \(\varepsilon\) each sampled point has a unique nearest parent vertex in the barycentric-neighborhood sense, and these \(d+1\) vertices are all distinct. Relabel so that \(X_i\to v_i\) and denote by \(t_{ji}\ge0\) the barycentric coordinate of \(X_i\) at \(v_j\), \(j\ne i\). Then the joint law of the \(m\) coordinates \((t_{ji}/\varepsilon)_{i\ne j}\), conditional on \(T>1-\varepsilon\), converges weakly to uniform Lebesgue probability on
\[
\mathcal U_m=\left\{(z_{ji})_{i\ne j}:z_{ji}\ge0,\ \sum_{i\ne j}z_{ji}\le1\right\},
\]
whose constant density is \(m!\). The vertex-assignment permutation is exactly uniform over the \((d+1)!\) possibilities, and is independent of the relabeled coordinates. In particular,
\[
\left.\frac{1-T}{\varepsilon}\ \right|\ (T>1-\varepsilon)
\ \xrightarrow{\mathrm{law}}\ \operatorname{Beta}(m,1).
\]

## Assumptions and scope
The dimension \(d\ge3\) is fixed as \(\varepsilon\downarrow0\); the constants in the remainder may depend on \(d\). Each \(X_i\) is sampled independently and uniformly with respect to \(d\)-dimensional volume. All positive-volume parent simplices are included, without restrictions on aspect ratio or regularity: the statement is invariant under invertible affine maps. The threshold is the maximal possible volume fraction \(1\). The conditional limit is a joint law in the original barycentric coordinates after the uniquely determined near-vertex assignment; it is not a claim of Euclidean similarity universality.

## Proof
**1. Localization and affine coordinates.** Normalize affinely so that the parent is the standard simplex with vertices \(e_0,\ldots,e_d\), represented using \(d+1\) barycentric coordinates. Let \(A\) be the column-stochastic matrix with column \(i\) equal to the barycentric vector of \(X_i\). Then \(T=|\det A|\). Since \(\operatorname{conv}(X_0,\ldots,X_d)\subseteq\Delta\), equality \(T=1\) forces equality of these two closed convex sets; thus the set of sampled points equals the parent-vertex set. Equivalently, \(A\) is a permutation matrix. Compactness shows that every configuration with \(T>1-\varepsilon\) lies in the union of disjoint arbitrarily small neighborhoods of these permutation matrices once \(\varepsilon\) is small. The \((d+1)!\) neighborhoods have equal probability by exchangeability.

**2. Determinant expansion.** Work in the neighborhood of the identity permutation. For \(i\ne j\), set \(t_{ji}=A_{ji}\ge0\), and put
\[
s_i=\sum_{j\ne i}t_{ji},\quad S=\sum_i s_i,
\quad A_{ii}=1-s_i,\quad E=A-I.
\]
There are \(m=d(d+1)\) off-diagonal variables. When \(S\) is sufficiently small, their only domain constraints are \(t_{ji}\ge0\). Using the quadratic determinant identity
\[
\det(I+E)=1+\operatorname{tr}E+
\frac{(\operatorname{tr}E)^2-\operatorname{tr}(E^2)}2+O_d(\|E\|^3),
\]
and \(\operatorname{tr}E=-S\), obtain
\[
1-\det A=S-B_2(t)+O_d(S^3),\qquad
B_2(t)=\sum_{0\le i<j\le d}(s_i s_j-t_{ij}t_{ji}).
\]
The error is uniform over nonnegative \(t\) with small \(S\), since the determinant is a polynomial. In this neighborhood \(\det A>0\), so the absolute value disappears. The linear term also implies \(S=O_d(\varepsilon)\) on the near-maximal event.

**3. Radial-simplex integration.** Write \(t=S p\), where \(p\ge0\) and \(\sum_{i\ne j}p_{ji}=1\). For every such \(p\), the deficit is
\[
\delta(S,p)=S-S^2B_2(p)+O_d(S^3).
\]
Its derivative in \(S\) equals \(1+O_d(S)\), uniformly over the compact \(p\)-simplex. Hence the unique radial boundary \(\delta(S_\varepsilon(p),p)=\varepsilon\) satisfies, uniformly,
\[
S_\varepsilon(p)=\varepsilon+B_2(p)\varepsilon^2+O_d(\varepsilon^3).
\]
For each point, its \(d\) nonvertex barycentric coordinates have joint density \(d!\) on the standard \(d\)-simplex. The density of all \(m\) variables in this neighborhood is therefore \((d!)^{d+1}\). Writing \(\mathbb E_p\) for the uniform Dirichlet distribution on \(\sum p=1\), the probability from this neighborhood is exactly
\[
\frac{(d!)^{d+1}}{m!}\mathbb E_p[S_\varepsilon(p)^m]
=\frac{(d!)^{d+1}}{m!}\varepsilon^m
\left(1+m\mathbb E_p[B_2(p)]\varepsilon+O_d(\varepsilon^2)\right).
\]
All \((d+1)!\) permutation neighborhoods contribute equally.

**4. Evaluation of the second coefficient.** For any two *distinct* coordinates of the uniform \(m\)-component Dirichlet vector,
\[
\mathbb E_p[p_a p_b]=\frac1{m(m+1)}.
\]
For each unordered pair \(i<j\), the polynomial \(s_i s_j\) has \(d^2\) pairwise-distinct coordinate products, whereas \(t_{ij}t_{ji}\) removes exactly one. Thus
\[
\mathbb E_p[B_2(p)]
=\frac{\binom{d+1}{2}(d^2-1)}{m(m+1)}
=\frac{d^2-1}{2(m+1)}.
\]
Substitution yields the asserted leading constant and positive first relative correction. Uniformity of the local determinant expansion and the radial implicit function gives the claimed relative \(O_d(\varepsilon^2)\) remainder.

**5. Conditional law.** Rescale \(t=\varepsilon z\). The conditioning event becomes
\[
\sum z_{ji}-\varepsilon B_2(z)+O_d(\varepsilon^2\|z\|^3)<1.
\]
Its indicator tends almost everywhere to the indicator of \(\mathcal U_m\). Localization bounds \(z\) uniformly, so dominated convergence proves convergence of normalized integrals against each bounded continuous test function to uniform measure on \(\mathcal U_m\). Exchangeability gives exact equiprobability and independence of the assignment permutation. Finally \((1-T)/\varepsilon=\sum z_{ji}+O_d(\varepsilon)\), and the sum of \(m\) coordinates under uniform measure on \(\mathcal U_m\) has CDF \(r^m\) on \([0,1]\), namely \(\operatorname{Beta}(m,1)\).

## Verification
Run `python3 verify.py` in a standard Python 3 environment. The script uses only the standard library. It checks the determinant expansion by exact-rational polynomial computation and a separately implemented exact elimination determinant, verifies the stated constants for several dimensions, and performs deterministic-seed importance sampling in the near-permutation neighborhoods. During preparation, 132 exact arithmetic/constant checks passed. At deficit \(\varepsilon=0.015\), with 50,000 draws per dimension, the simulated ratios of the tail probability to its leading term were \(1.016091\) in dimension two (cross-check only), \(1.058371\) in dimension three, and \(1.116357\) in dimension four. The corresponding analytic two-term ratios are \(1.019286\), \(1.055385\), and \(1.107143\). The computations are finite corroboration; the proof above establishes the formulas for every fixed \(d\ge3\).

## Relationship to prior work
Alagar (1977) obtained the *full area distribution* of a triangle sampled inside a parent triangle: consequently the planar case is explicitly excluded from the new priority claim. Mannion (1994) computed the mean and selected low moments of a daughter tetrahedron's volume in a parent tetrahedron, not an explicitly stated near-full-volume tail in the accessible abstract; the full text was not accessible for a decisive comparison. Letac and Scarsini (1998) study repeated nested random simplices and the limiting position of their eventual collapse point, which is a different iterative limit from the fixed-single-step high-volume conditioning here.

Rademacher (2010) and Reichenwallner–Reitzner (2016) study (non)monotonicity of random-simplex volume moments across containing bodies; their inspected primary works do not state the fixed-parent, fixed-dimension endpoint expansion or conditional off-vertex law. Frieze, Pegden, and Tkocz (2020) instead analyze how *many* samples (exponential in the growing dimension) are required for their hull to fill most of a simplex. The present theorem fixes exactly \(d+1\) samples and lets the relative volume deficit vanish in fixed dimension. These comparisons distinguish objects, quantifiers, and limits; absence from a search is not treated as a proof of historical uniqueness.

## Limitations
No formula for the full random-simplex volume distribution is claimed, and no asymptotics uniform as \(d\to\infty\) are proved. The parent must itself be a nondegenerate simplex, not an arbitrary convex body. The shape convergence uses barycentric rather than Euclidean-displacement coordinates; its affine universality does not imply a universal Euclidean point-cloud shape. The planar analogue is already covered by Alagar. Historical priority is not independently certified: an inaccessible full 1994 tetrahedron paper and older thesis-level literature remain a specific residual overlap risk. All computational evidence is finite and supplementary.

## References
1. V. S. Alagar, “On the distribution of a random triangle,” *Journal of Applied Probability* **14** (1977), 284–297, DOI: 10.2307/3212999.
2. D. Mannion, “The Volume of a Tetrahedron whose Vertices are Chosen at Random in the Interior of a Parent Tetrahedron,” *Advances in Applied Probability* **26** (1994), 577–596, DOI: 10.2307/1427809.
3. G. Letac and M. Scarsini, “Random nested tetrahedra,” *Advances in Applied Probability* **30** (1998), 619–627, DOI: 10.1239/aap/1035228119.
4. L. Rademacher, “On the monotonicity of the expected volume of a random simplex,” arXiv:1008.3944, first available 2010-08-24; *Mathematika* **58** (2012), 77–91.
5. B. Reichenwallner and M. Reitzner, “On the monotonicity of the moments of volumes of random simplices,” arXiv:1601.07295, first available 2016-01-27; *Mathematika* **62** (2016), 949–958.
6. A. Frieze, W. Pegden and T. Tkocz, “Random volumes in \(d\)-dimensional polytopes,” arXiv:2002.11693 (2020), available author manuscript at `https://www.math.cmu.edu/~af1p/Texfiles/VolSimplex.pdf`.
