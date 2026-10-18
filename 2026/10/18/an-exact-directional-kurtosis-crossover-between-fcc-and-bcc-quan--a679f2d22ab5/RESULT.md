# An exact directional-kurtosis crossover between FCC and BCC quantization cells

## Finding

Let \(F\) be the rhombic dodecahedral Voronoi cell of the face-centered cubic lattice, and let \(B\) be the truncated-octahedral Voronoi cell of the body-centered cubic lattice, with their fourfold axes aligned. Use the explicit Euclidean models
\[
 F=\{x\in\mathbb R^3:|x_i|+|x_j|\le1\quad(1\le i<j\le3)\},\qquad
 B=\{x\in\mathbb R^3:|x_i|\le1,\ \sum_{i=1}^3|x_i|\le3/2\}.
\]
Let \(X_F,X_B\) be independently uniform in the respective cells. For \(Q\in\{F,B\}\), define the radial ratios \(R_{2k}(Q)=\mathbb E\|X_Q\|^{2k}/(\mathbb E\|X_Q\|^2)^k\) and the directional kurtosis \(K_Q(u)=\mathbb E[(u\cdot X_Q)^4]/(\mathbb E[(u\cdot X_Q)^2])^2\), for every unit \(u\in S^2\).

**Theorem.** For every \(u\in S^2\), writing \(w(u)=u_1^4+u_2^4+u_3^4\),
\[
 K_F(u)=\frac{28+8w(u)}{15},\qquad
 K_B(u)=\frac{3408+864w(u)}{1805},\qquad
 \boxed{K_F(u)-K_B(u)=\frac{4(74w(u)-29)}{5415}}.
\]
Thus the two directional kurtoses are equal **if and only if** \(w(u)=29/74\); the FCC directional kurtosis is smaller on \(w(u)<29/74\) (including body diagonals) and larger on \(w(u)>29/74\) (including coordinate axes). Both strict regions are nonempty and the transition is sharp. Simultaneously,
\[
 \boxed{R_4(F)-R_4(B)=\frac{308}{48735}>0},\qquad
 \boxed{R_6(F)-R_6(B)=\frac{1758278}{58335795}>0}.
\]
Hence radial standardized fourth/sixth moments rank BCC ahead of FCC, but the directional standardized fourth moment reverses that ranking near body-diagonal viewing directions.

## Assumptions and scope

The FCC lattice is \(D_3=\{n\in\mathbb Z^3:\sum_i n_i\ \text{is even}\}\). The BCC lattice is \(2\mathbb Z^3\cup((1,1,1)+2\mathbb Z^3)\). Their displayed origin Voronoi cells have respective Euclidean volumes \(2\) and \(4\). The comparison involves independent points uniform with respect to normalized three-dimensional Lebesgue measure, not points distributed on their boundaries. The coordinate axes are identified with the natural common fourfold symmetry axes of the two cubic lattices. All ratios are invariant under an independent uniform rescaling of either lattice; the cubic-axis alignment, however, is essential for the pointwise comparison at the same direction.

## Proof

**1. Voronoi models.** For \(D_3\), the twelve lattice vectors of the form \(\pm e_i\pm e_j\) give exactly \(|x_i|+|x_j|\le1\). These constraints imply \(|x_i|\le1\). Every lattice vector has either zero or two odd coordinates. For an even integer \(m\), \(|mx_i|\le m^2/2\). For an odd integer \(m\), \(|mx_i|\le(m^2-1)/2+|x_i|\). In the two-odd-coordinate case, the remaining terms total at most \(|x_i|+|x_j|\le1\). Therefore for every \(n\in D_3\), \(|x\cdot n|\le\|n\|^2/2\); no further Voronoi halfspace cuts \(F\).

For the BCC lattice the six vectors \(\pm2e_i\) give \(|x_i|\le1\), and the eight \((\pm1,\pm1,\pm1)\) give \(\sum_i|x_i|\le3/2\). Every other lattice vector is either coordinatewise even or coordinatewise odd. The even case follows from \(|x_i|\le1\) as above. In the odd case, sum the odd-integer inequality over three coordinates: \(|x\cdot n|\le(\|n\|^2-3)/2+\sum_i|x_i|\le\|n\|^2/2\). Thus these inequalities give the full Voronoi cell \(B\).

**2. Exact simplex integration.** For a polynomial \(P\) symmetric in the three coordinates and even in each variable, let \(L_h(P)\) denote its integral over \(\{s_i\ge0:\sum_i s_i\le h\}\). Every monomial is integrated by
\[
 L_h(s_1^as_2^bs_3^c)=\frac{a!b!c!}{(a+b+c+3)!}\,h^{a+b+c+3}\quad(a,b,c\in\mathbb Z_{\ge0}).
\]
Within the nonnegative sorted FCC chamber \(x_1\ge x_2\ge x_3\), the only active bound is \(x_1+x_2\le1\). Set
\[
 x_1=s_1+(s_2+s_3)/2,\qquad x_2=(s_2+s_3)/2,\qquad x_3=s_3/2.
\]
This sends the unit simplex bijectively onto that chamber with Jacobian \(1/4\). Accounting for its \(48\) signed-permutation chambers gives
\[
 \int_F P(x)\,dx=12L_1(P(s_1+(s_2+s_3)/2,(s_2+s_3)/2,s_3/2)).
\]
The positive octant of \(B\) is the simplex \(\sum_i x_i\le3/2\) minus the three mutually disjoint sub-simplices where one coordinate exceeds \(1\). Translation of each removed piece yields
\[
 \int_B P(x)\,dx=8\bigl[L_{3/2}(P)-3L_{1/2}(P(s_1+1,s_2,s_3))\bigr].
\]
The second formula uses permutation invariance of \(P\); no claim is made that it works for nonsymmetric monomials.

Evaluating these identities for \(P=1\), \(P=\sum_i x_i^2\), \(P=(\sum_i x_i^2)^2\), \(P=(\sum_i x_i^2)^3\), \(P=\sum_i x_i^4\), and \(P=\sum_{i<j}x_i^2x_j^2\), and dividing by volume, gives the complete exact table

| Cell | Volume | \(\mathbb E\|X\|^2\) | \(\mathbb E\|X\|^4\) | \(\mathbb E\|X\|^6\) | \(A=\mathbb EX_1^4\) | \(C=\mathbb EX_1^2X_2^2\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| FCC | \(2\) | \(3/8\) | \(41/240\) | \(1397/16128\) | \(3/80\) | \(7/720\) |
| BCC | \(4\) | \(19/32\) | \(409/960\) | \(27217/80640\) | \(89/960\) | \(71/2880\) |

**3. Kurtosis and sharp transition.** Signed-coordinate and permutation symmetries imply \(\mathbb E(u\cdot X)^2=(\mathbb E\|X\|^2)/3\), and, for \(\|u\|=1\),
\[
 \mathbb E(u\cdot X)^4=3C+(A-3C)\sum_i u_i^4.
\]
Substitution of the two exact table rows produces the asserted formula for \(K_F-K_B\). Cauchy--Schwarz and \(\sum_i u_i^2=1\) imply \(1/3\le\sum_i u_i^4\le1\), attained at body-diagonal and coordinate-axis directions. Since \(1/3<29/74<1\), the equality locus exists, both strict comparison regimes occur, and the signs are exactly as stated.

Finally \(R_4(F)=164/135\), \(R_4(B)=6544/5415\), \(R_6(F)=2794/1701\), and \(R_6(B)=3483776/2160585\). Direct reduction of the rational differences yields the two positive displayed gaps. This finishes the proof.

## Verification

The standalone `verify.py` implements both simplex-chamber polynomial integration and a separate, exact-determinant integration over origin-pyramids based on independently reconstructed convex hull facets. They agree on cell volumes, radial moments of degrees two/four/six, and both independent quartic tensor coefficients. In its tested environment with Python, SymPy, NumPy, and SciPy, the program reconstructs \(24\) triangular boundary pieces of the FCC dodecahedron and \(44\) of the BCC octahedron, and all rational assertions pass. The analytic Voronoi inequality and symmetry arguments above, not merely the output of a finite computation, establish applicability to every direction.

## Relationship to prior work

Conway and Sloane's 1982 study identifies the quantization-cell problem and computes second moments, including for the truncated octahedron. Barnes and Sloane (1983) prove BCC minimizes the normalized **second** moment among three-dimensional lattice quantizers. Sloane and Beferull-Lozano (2002; submitted 17 July 2002) describe the BCC/FCC lattices and their intersection honeycombs and tabulate second moments of honeycomb cells. None of the inspected relevant statements gives the present **direction-dependent fourth-moment crossover surface** or the exact pair of higher-radial-moment comparisons. The standard Dirichlet formula for integrating monomials on a simplex is prior art; the originality claim is the evaluated comparison and its sharp cubic-angular sign change, not the integration method or the known quadratic optimality.

## Limitations

The comparison is for two fixed cubic Voronoi cells, canonical alignment of their cubic axes, and uniform interior points; it does not establish fourth-moment optimality of BCC among all lattices, stochastic dominance of radial error distributions, or a comparison of arbitrarily rotated cells at the same direction. Searches and inspected primary texts do not certify definitive priority over all historical crystallographic moment tables. All computed values are exact in the stated normalization.

## References

1. J. H. Conway and N. J. A. Sloane, “Voronoi Regions of Lattices, Second Moments of Polytopes, and Quantization,” *IEEE Transactions on Information Theory* **28** (1982), 211–226. DOI: `10.1109/TIT.1982.1056483`.
2. E. S. Barnes and N. J. A. Sloane, “The Optimal Lattice Quantizer in Three Dimensions,” *SIAM Journal on Algebraic Discrete Methods* **4** (1983), 30–41. DOI: `10.1137/0604005`.
3. N. J. A. Sloane and B. Beferull-Lozano, “Quantizing Using Lattice Intersections,” arXiv:`math/0207147v1`, submitted 2002-07-17. See sections 3, 5, and 6.
4. The companion `verify.py`, containing two rational polynomial integrations of the stated cells.
