# Exact two-orbit two-summing transition for triangular Johnson graphs

## Finding

Fix an integer \(v\ge4\), and write \(N=\binom v2\). Index the standard orthonormal basis of \(E=\ell_2^N(\mathbb R)\) by the two-element subsets \(S\subseteq\{1,\ldots,v\}\). In the real free two-convex Banach lattice \(\operatorname{FBL}^{(2)}[E]\), define
\[
F_{v,a}=\bigvee_{|S\cap T|=1}|\delta_{e_S-e_T}|\ \vee\ \bigvee_{S\cap T=\varnothing}a|\delta_{e_S-e_T}|,
\qquad a>0,
\]
where each unordered pair occurs once and \(\delta_z\) is evaluation at \(z\in E\). The same norm is the absolutely two-summing norm of the linear operator taking coordinate differences of the two types, with amplitudes \(1\) and \(a\), from \(E\) to the associated finite-dimensional \(\ell_\infty\) space.

Put
\[
 c=\frac{v-4}{v-3},\qquad
 P=\sqrt{\frac{2(v-1)}{v-2}},\qquad
 Q=(v-3)\sqrt{\frac{v}{v-2}},\qquad b=a^2,
\]
\[
 \beta_-=\frac{P+Q}{2P+cQ},\qquad
 \beta_+=\begin{cases}
 +\infty,&v=4,\\[2pt]
 \displaystyle\frac{P/\sqrt2+Q/\sqrt c}{\sqrt2P+\sqrt cQ},&v\ge5.
 \end{cases}
\]
Then \(\tfrac12<\beta_-<1<\beta_+\) (allowing \(\beta_+=+\infty\)), and the **exact norm at every positive amplitude** is
\[
\boxed{
\|F_{v,a}\|=
\begin{cases}
P+Q,&0<b\le\beta_-,\\[5pt]
\displaystyle\sqrt{b(2-c)\left(\frac{P^2}{1-cb}+\frac{Q^2}{2b-1}\right)},&\beta_-<b<\beta_+,\\[9pt]
\displaystyle a(\sqrt2P+\sqrt cQ),&v\ge5,\ b\ge\beta_+.
\end{cases}}
\]
Thus the optimal two-summing design passes through **original-edge only**, **mixed**, and (only for \(v\ge5\)) **disjoint-edge only** regimes. At \(v=4\), the last regime never occurs at a finite amplitude, because the graph of disjoint pairs is a disconnected perfect matching. The optimal design is unique in all regimes.

The first transition is also **simultaneous and coordinatewise**: for any nonempty collection \(\mathcal C\) of disjoint two-subset pairs with individual positive amplitudes \(a_{ST}\),
\[
\left\|\bigvee_{|S\cap T|=1}|\delta_{e_S-e_T}|\vee
\bigvee_{\{S,T\}\in\mathcal C}a_{ST}|\delta_{e_S-e_T}|\right\|=P+Q
\quad\Longleftrightarrow\quad
 a_{ST}\le\sqrt{\beta_-}\ \text{for every added pair}.
\]
In this norm-flat region, added pair differences can nonetheless strictly enlarge the positive lattice element pointwise. Finally, as \(v\to\infty\),
\[
\beta_-=1-\frac{\sqrt2-1}{v}+O(v^{-2}),\qquad
\beta_+=1+\frac1{v^2}+O(v^{-3}).
\]
The disjoint-edge-only phase therefore begins just above amplitude one, with a much smaller offset than the original-edge-only phase ends below it.

## Assumptions and scope

All spaces, operators, and lattices are real; the generating space is Euclidean, and the free-lattice exponent is exactly two. The two-subset pairs in each supremum are **unordered**. The parameter range is all integers \(v\ge4\) and all real amplitudes \(a>0\). The norm is the **unrestricted** free-lattice norm, with no symmetry imposed on its finite testing sequences. Statements about the simultaneous addition of disjoint pairs permit arbitrary subsets and arbitrary positive amplitudes. The graph whose edges satisfy \(|S\cap T|=1\) is the triangular Johnson graph \(J(v,2)=L(K_v)\), and the graph of disjoint pairs is its Kneser complement.

## Proof

**1. The unrestricted norm as a concave design problem.** Let \(\{b_r\}\) be any finite family of vectors in a real Euclidean space, and set \(f(z)=\max_r|\langle b_r,z\rangle|\). The explicit free-two-convex norm formula of Jardón-Sánchez et al. (equation (1.1), Theorem 6.1) gives
\[
\|f\|^2=\sup_{\sum_j z_jz_j^\mathsf T\preceq I}\sum_j \max_r|\langle b_r,z_j\rangle|^2.
\]
Split the vectors \(z_j\) according to a maximizing index \(r\) and put \(H_r=\sum_{j:r(j)=r}z_jz_j^\mathsf T\). Conversely, every finite family of positive semidefinite \(H_r\) decomposes into such rank-one vectors. Consequently
\[
\|f\|^2=\max_{H_r\succeq0,\ \sum_rH_r\preceq I}
\sum_r b_r^\mathsf TH_rb_r
=\min_{Y\succeq b_rb_r^\mathsf T\ (\forall r)}\operatorname{tr}Y.
\]
The last equality is elementary finite-dimensional semidefinite duality, with strict feasible points. On the span of the \(b_r\), one can write the dual constraints as \(b_r^\mathsf TY^{-1}b_r\le1\). Introducing nonnegative multipliers \(\lambda_r\) and minimizing over positive \(Y\) yields \(2\operatorname{tr}\sqrt{\sum_r\lambda_rb_rb_r^\mathsf T}-\sum_r\lambda_r\); this follows from the matrix identity \(\inf_{Y\succ0}[\operatorname{tr}Y+\operatorname{tr}(Y^{-1}M)]=2\operatorname{tr}\sqrt M\). Normalizing \(\lambda_r=t w_r\) with \(w\) a probability vector and optimizing the scalar \(t\ge0\) therefore proves
\[
\boxed{\|f\|=\max_{w_r\ge0,\ \sum_rw_r=1}
\operatorname{tr}\sqrt{\sum_r w_rb_rb_r^\mathsf T}.}
\tag{1}
\]
No symmetry or finite-test restriction was inserted in this identity. The use of rank-deficient matrices is justified by continuity.

**2. Full symmetry reduction and the two spectra.** For the family in the finding, the symmetric group on \(v\) letters permutes the two-subset coordinates and is transitive on each of the two kinds of unordered pairs. The map \(M\mapsto\operatorname{tr}\sqrt M\) is concave, so averaging any probability design over this group cannot decrease (1). Thus an optimum assigns total mass \(x\) uniformly to the original graph edges and total mass \(1-x\) uniformly to disjoint pairs, for some \(0\le x\le1\).

There are \(m_1=N(v-2)\) original edges and \(m_2=N(v-2)(v-3)/4\) disjoint-pair edges. Let \(L_1,L_2\) be their unweighted graph Laplacians. To compute the spectra, let \(B\) be the unsigned vertex-versus-two-subset incidence matrix of \(K_v\). Then the adjacency matrix of \(J(v,2)\) equals \(BB^\mathsf T-2I\), while \(B^\mathsf TB=(v-2)I+\mathbf1\mathbf1^\mathsf T\). On the space perpendicular to constants, this gives two orthogonal invariant spaces \(E_1,E_2\) with dimensions \(v-1\) and \(v(v-3)/2\), respectively, on which
\[
\begin{array}{c|cc}
& E_1 & E_2\\ \hline
L_1 & v & 2(v-1)\\
L_2 & N-v & N-2(v-1)
\end{array}.
\tag{2}
\]
The second line also follows from \(L_1+L_2=NI-\mathbf1\mathbf1^\mathsf T\). Notice that the second eigenvalue of \(L_2\) vanishes exactly at \(v=4\).

The design matrix in (1) is \(M_x=(x/m_1)L_1+(a^2(1-x)/m_2)L_2\). Substituting (2) and simplifying gives the exact unrestricted optimization
\[
\|F_{v,a}\|=\max_{0\le x\le1}
U_b(x),\qquad
U_b(x)=P\sqrt{2b+(1-2b)x}+Q\sqrt{cb+(1-cb)x}.
\tag{3}
\]

**3. Both sharp phase boundaries and closed interior value.** For fixed \(b>0\), \(U_b\) is strictly concave in \(x\). At \(x=1\),
\[
U_b'(1)=\tfrac12\bigl[P(1-2b)+Q(1-cb)\bigr],
\]
which is nonnegative precisely for \(b\le\beta_-\). For \(v\ge5\), the derivative at \(x=0\) has the same sign as
\[
\frac P{\sqrt2}(1-2b)+\frac Q{\sqrt c}(1-cb);
\]
this is nonpositive precisely for \(b\ge\beta_+\). For \(v=4\), the second summand in (3) equals \(Q\sqrt x\), so \(U_b'(0^+)=+\infty\) at every finite \(b\). Direct comparison yields \(\tfrac12<\beta_-<1<\beta_+\). These derivative tests and strict concavity give the three asserted optimization regions and the dimension-four exception.

In the interior, set \(u=2b-1>0\) and \(z=1-cb>0\). If \(s=2b-ux\) and \(t=cb+zx\), then \(zs+ut=b(2-c)\). Weighted Cauchy–Schwarz yields
\[
(P\sqrt s+Q\sqrt t)^2\le b(2-c)
\left(\frac{P^2}{z}+\frac{Q^2}{u}\right).
\]
Equality holds exactly at the unique maximizer
\[
x_* = \frac{2bQ^2z^2-cbP^2u^2}
{uz(Q^2z+P^2u)}\in(0,1).
\]
This proves the middle branch. Endpoint substitution gives the first and last branches. For \(b=1\), the optimal mass is \(x_*=4/(v+1)\), precisely the proportion of original edges among all edges of the complete graph on \(N\) vertices; (3) then reduces to \(\|F_{v,1}\|=\sqrt{2(N-1)}\), an independent normalization check.

Strict concavity of the trace-square-root functional implies uniqueness of its optimizing information matrix on the orthogonal complement of constants. Every individual edge weight is recoverable from a distinct off-diagonal entry of that matrix (amplitudes are positive), so the full **unrestricted design itself is unique**, not only its symmetric representative.

**4. Arbitrary simultaneous disjoint-pair additions.** At the original-edge design \(M_0=L_1/m_1\), the matrix is positive definite on the zero-sum space. Each old edge has the same directional derivative \(\tfrac12 d_1\), where \(d_1=b_e^\mathsf T M_0^{-1/2}b_e\), and each unscaled disjoint-pair edge has derivative \(\tfrac12 d_2\). Concavity of (1) says that the old design remains globally optimal under an arbitrary finite addition if and only if every new-edge marginal \(a_{ST}^2d_2\) is at most \(d_1\); strict violation raises the norm. Equation (3), evaluated at \(x=1\), shows \(d_1/d_2=\beta_-\). This proves the simultaneous coordinatewise criterion, including necessity. Any such added pair has graph distance two in \(J(v,2)\). Taking a distance-to-one-endpoint potential produces all original differences of modulus at most one and that pair's difference of modulus two. Hence for \(1/2<a_{ST}\le\sqrt{\beta_-}\), the positive lattice element is strictly larger pointwise despite equal norms.

**5. Asymptotic boundaries.** Expand the explicit expressions for \(c,P,Q\) in powers of \(v^{-1}\). They give \(\beta_-=1-(\sqrt2-1)v^{-1}+O(v^{-2})\) and \(\beta_+=1+v^{-2}+O(v^{-3})\). All limits follow from explicit radicals, without extrapolation from finite computations.

## Verification

The standalone scripts `verify_symbolic.py` and `verify_johnson.py` provide independent checks of the key finite-dimensional identities. The former compares exact integer spectra of both graphs for \(v=4,5,6,7,8\). The latter compares the formula with explicit full Laplacian eigenspectra in 89 parameter configurations and with 15 numerical optimizations over **all individual edge weights**, not just invariant designs, for \(v=4,5,6\). Both scripts print `PASS` on success. The infinitude of parameter values is addressed by the proof above, not by the finite tests.

## Relationship to prior work

The explicit norm of free two-convex Banach lattices is due to Jardón-Sánchez, Laustsen, Taylor, Tradacete, and Troitsky (2021 preprint; 2022 journal), and is a required prior input, not a new claim. The triangular Johnson graph is the classical line graph of a complete graph; its two nonzero Laplacian eigenspaces and the analogous complementary Kneser graph are standard algebraic-combinatorial objects. General concave spectral optimal-design methods are also established prior tools. The contribution here is the **complete amplitude-dependent unrestricted two-summing norm** for the competing Johnson/Kneser edge-difference systems, with both transitions, the exceptional disconnected-complement case, unique optimal designs, and coordinatewise stability under arbitrary subfamilies. Results about ordinary graph spectra, projection norms onto cycle spaces, and free-lattice norms for different graph families do not by themselves imply this weighted two-orbit optimization.

## Limitations

The result is specific to real Hilbert-generated free two-convex lattices; neither other exponents nor other Johnson ranks are asserted. The disjoint-pair amplitude is uniform in the complete-profile theorem, although the norm-flat criterion allows arbitrary amplitudes on arbitrary subfamilies. No claim is made about the free-lattice elements being equal pointwise within the norm-flat region; the proof explicitly shows strict inequality for suitable potentials. The bibliographic comparison cannot exclude an equivalent result under different terminology. Numerical optimizations are corroborative, not a replacement for analytical arguments.

## References

1. H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete, and V. G. Troitsky, *Free Banach lattices under convexity conditions*, arXiv:2101.03510 (first publicly available 2021-01-10); RACSAM **116**, article 15 (2022), DOI:10.1007/s13398-021-01155-8, especially equation (1.1) and Theorem 6.1.
2. M. de Jeu and X. Jiang, *Free Banach lattices over pre-ordered Banach spaces*, arXiv:2408.06630 (2024), sections 1 and 6; more general free-lattice existence and function-lattice constructions.
3. R. A. Bailey and P. J. Cameron, *Combinatorics of optimal design*, in *Surveys in Combinatorics 2009*, London Mathematical Society Lecture Note Series **365** (2009), pp. 19–73; context for graph-Laplacian spectral design criteria.
4. J. Kiefer, *General equivalence theory for optimum designs (approximate theory)*, Annals of Statistics **2** (1974), 849–879, DOI:10.1214/aos/1176342810; general design optimality principles.
