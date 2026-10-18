# Dimension-saturated chord screening for hypercube two-summing norms

## Finding

For an integer \(d\ge3\), put \(V_d=\{0,1\}^d\), \(N=2^d\), and \(M=d2^{d-1}\). Let \(E_d\) be the unordered pairs at Hamming distance one. For \(u\ne v\), let \(b_{uv}=e_u-e_v\in\mathbb R^{V_d}\), and let \(\delta_b(x)=\langle b,x\rangle\) be the canonical free-lattice evaluation. Given **any** set \(\mathcal C\) of distinct nonedges and positive real amplitudes \(a_{uv}\), consider in the real free two-convex Banach lattice over Euclidean \(\ell_2^{V_d}\)

\[
F_{\mathcal C,a}=\bigvee_{\{u,v\}\in E_d}|\delta_{b_{uv}}|\ \vee\ \bigvee_{\{u,v\}\in\mathcal C}a_{uv}|\delta_{b_{uv}}|.
\]

The same norm is the absolutely two-summing norm of \(D_{\mathcal C,a}:\ell_2^{V_d}\to\ell_\infty^{E_d\cup\mathcal C}\) with the indicated edge-difference rows. Put

\[
R_{d,k}=\frac4{2^d}\sum_{j=1}^{d}\frac1{\sqrt{2j}}
 \sum_{\substack{1\le r\le k\\r\ \mathrm{odd}\\0\le j-r\le d-k}}
 \binom{k}{r}\binom{d-k}{j-r},\qquad
T_{d,k}=\sqrt{\frac{R_{d,1}}{R_{d,k}}}\quad(1\le k\le d).
\]

Then the **simultaneous, necessary-and-sufficient screening criterion** is

\[
\boxed{\ \|F_{\mathcal C,a}\|=\pi_2(D_{\mathcal C,a})
=\frac1{\sqrt M}\sum_{j=1}^{d}\binom dj\sqrt{2j}
\quad\Longleftrightarrow\quad
 a_{uv}\le T_{d,k(u,v)}\ \text{for all }\{u,v\}\in\mathcal C.\ }
\]

The uniform probability distribution on the original \(M\) cube edges, assigning zero weight to all new chords, is the **unique** optimal row design whenever these inequalities hold, even at equality. A strict violation by one chord strictly increases the norm. For every \(2\le k\le d\),

\[
\frac1{\sqrt{k}}<T_{d,k}<1,\qquad
T_{d,2}>T_{d,3}>\cdots>T_{d,d}.
\]

The thresholds satisfy the uniform, dimension-saturated asymptotic

\[
\boxed{\ T_{d,k}=1-\frac1{4d}+O(d^{-2})\quad\text{uniformly over }2\le k\le d.\ }
\]

In particular, adding **every** nonedge with the common amplitude \(T_{d,d}\) preserves the norm, although the pointwise order gap is exactly

\[
\boxed{\ \sup_{F_{\varnothing}(x)>0}
\frac{F_{\mathcal C,T_{d,d}}(x)}{F_{\varnothing}(x)}
=dT_{d,d}=d-\frac14+O(d^{-1}).\ }
\]

The baseline norm itself obeys \(\|F_{\varnothing}\|=\sqrt{2N}(1-1/(8d)+O(d^{-2}))\).

## Assumptions and scope

All spaces, norms, and free lattices are **real**. The generator is the Euclidean space with one coordinate per cube vertex, without quotienting constants; the operator and its rows annihilate constants. The free-lattice norm is the standard \(p=2\) free-convex norm with constant one. A chord is an unordered nonedge, occurs at most once, and its amplitude is positive. The statements are for all integers \(d\ge3\), all chord subsets (possibly empty), and all positive amplitudes; there is no symmetry assumption on the chord family. The \(O(\cdot)\) constants in the threshold expansion are absolute, independently of \(k\).

## Proof

**1. A finite-dimensional norm/weight duality.** The representation of the free \(2\)-convex lattice norm [1, formula (1.1), Theorem 6.1] gives \(\|F\|=\pi_2(D)\) for a maximum of absolute finitely many linear evaluation rows. By Pietsch domination for nonnegative homogeneous functions [1, Corollary 7.8] in a finite-dimensional Euclidean space, its square is

\[
\min_{Q\succeq0,\ \operatorname{tr}Q=1}
\max_{e}\,v_e^{\mathsf T}Q^{\dagger}v_e,
\]

where the quadratic form is interpreted as \(+\infty\) when \(v_e\) has a component outside \(\operatorname{ran}Q\). Here \(v_e\) is the signed row vector, incorporating its amplitude. Indeed, \(Q\) is the second-moment matrix of a probability measure on the Euclidean unit sphere; conversely every positive semidefinite trace-one matrix is such a second moment. The domination inequality for a row is equivalent to \(v_ev_e^{\mathsf T}\preceq C^2Q\).

On the common mean-zero span, use \(\max_e z_e=\max_{w\in\Delta}\sum_e w_ez_e\), convexity in positive-definite \(Q\), linearity in the simplex variable \(w\), and minimax (regularize by \(Q\succeq\varepsilon I\) and then let \(\varepsilon\downarrow0\)). For \(A=\sum_e w_ev_ev_e^{\mathsf T}\), the trace Cauchy–Schwarz inequality yields

\[
\min_{Q\succeq0,\ \operatorname{tr}Q=1}
\operatorname{tr}(AQ^{\dagger})
=(\operatorname{tr}\sqrt A)^2,
\]

with the optimizer proportional to \(\sqrt A\) on its range. Thus, **over all row weights and with no symmetry restriction**, 

\[
\boxed{\ \|F\|=\max_{w_e\ge0,\ \sum_e w_e=1}
\operatorname{tr}\sqrt{\sum_e w_ev_ev_e^{\mathsf T}}.\ }\tag{1}
\]

For a connected original graph the trace-square-root objective is differentiable on the positive mean-zero cone, with derivative \(\partial_{w_e}\operatorname{tr}\sqrt A=\tfrac12v_e^{\mathsf T}A^{-1/2}v_e\). It is strictly concave in \(A\) on this cone: in an eigenbasis with positive eigenvalues \(\lambda_i\), its second directional differential at a nonzero symmetric \(H\) is

\[
-\frac12\sum_{i,j}\frac{|H_{ij}|^2}
{\sqrt{\lambda_i\lambda_j}(\sqrt{\lambda_i}+\sqrt{\lambda_j})}<0.
\]

**2. The unique old optimizer and the first-order criterion.** The cube automorphism group is edge transitive. Symmetrizing any old-edge weight design cannot decrease the concave objective, so the uniform original-edge design is optimal. Strict concavity in its Laplacian matrix and injectivity of weights into off-diagonal Laplacian entries make it unique. Write \(L=\sum_{e\in E_d}b_eb_e^{\mathsf T}\) and \(A_0=L/M\), considered on the mean-zero subspace. Its old-edge derivatives are equal, so first-order concavity says that \(A_0\) remains a global maximizer after arbitrarily many new chord rows precisely if every new derivative does not exceed an old derivative. With \(R_{d,k}=b_{uv}^{\mathsf T}L^{\dagger1/2}b_{uv}\) for a pair at Hamming distance \(k\), this is exactly

\[
a_{uv}^{2}R_{d,k}\le R_{d,1}.\tag{2}
\]

For necessity, transfer infinitesimal mass from the old uniform design to a violating new row. Its directional derivative is strictly positive, hence the optimal norm strictly increases. For sufficiency, concavity supplies the global supporting-hyperplane inequality, simultaneously for **every** chord. Even at an equality in (2), strict concavity in the Laplacian and injectivity of all distinct unordered-pair weights establish uniqueness of the original design. The argument covers weights supported only on the original edges and all possible new supports: it never assumes the new optimizer is symmetric.

**3. Walsh computation.** The Walsh vectors \(\varphi_S(u)=2^{-d/2}(-1)^{\sum_{i\in S}u_i}\) diagonalize \(L\), with eigenvalue \(2|S|\). For endpoints differing in the coordinate set \(K\) of size \(k\), the squared Walsh coefficient of \(b_{uv}\) is \(4/2^d\) exactly when \(|S\cap K|\) is odd, and zero otherwise. Summing over levels \(|S|=j\) proves the displayed finite formula for \(R_{d,k}\), including the zero eigenvalue's harmless omission. The same spectrum gives

\[
\operatorname{tr}\sqrt{L/M}=M^{-1/2}\sum_{j=1}^{d}\binom dj\sqrt{2j}.
\]

**4. Strict Hamming ordering and bounds.** The Laplace identity for the positive spectrum gives the absolutely convergent integral

\[
R_{d,k}=\frac2{\sqrt\pi}\int_0^\infty
s^{-1/2}e^{-ds}(\cosh s)^d\bigl(1-(\tanh s)^k\bigr)\,ds.\tag{3}
\]

Because \(0<\tanh s<1\) for every positive \(s\), this is strictly increasing in \(k\). For \(k\ge2\), the Walsh expression and the elementary parity bound \(\mathbf 1_{\{|S\cap K|\text{ odd}\}}\le |S\cap K|\) imply \(R_{d,k}<kR_{d,1}\), with strict inequality witnessed by a Walsh subset containing two elements of \(K\). Combining gives \(R_{d,1}<R_{d,k}<kR_{d,1}\), proving all strict threshold assertions.

**5. Uniform asymptotics.** In (3), the tail \(s\ge1\) is uniformly exponentially small in \(d\) for \(1\le k\le d\): writing \(P(s)=((1+e^{-2s})/2)^d\), one has \(P(s)\le((1+e^{-2})/2)^d\) and \(1-\tanh^k s\le2d e^{-2s}\). On \(0\le s\le1\), \(e^{-ds}(\cosh s)^d\le e^{-ds/2}\), so Watson's expansion at the origin is uniform. Specifically, \(\log\cosh s=s^2/2+O(s^4)\), \(\tanh s=s+O(s^3)\), and \(0\le(\tanh s)^k\le s^2\) for all \(k\ge2\). Integration against \(s^{-1/2}e^{-ds}\) gives

\[
R_{d,1}=2d^{-1/2}\left(1-\frac1{8d}+O(d^{-2})\right),\qquad
R_{d,k}=2d^{-1/2}\left(1+\frac3{8d}+O(d^{-2})\right)
\]

uniformly for \(2\le k\le d\). Taking their square-root ratio proves \(T_{d,k}=1-1/(4d)+O(d^{-2})\). For the baseline norm, if \(J\sim\operatorname{Bin}(d,1/2)\), its exact expression is \(\sqrt{2N/d}\,\mathbb E\sqrt{2J}\); a second-order centered-binomial expansion gives \(\sqrt{2N}(1-1/(8d)+O(d^{-2}))\).

**6. Full-chord amplification.** Take \(\mathcal C\) to contain all nonedges, each of amplitude \(T_{d,d}\). Since the thresholds strictly decrease in distance, condition (2) holds for every chord, and the lattice norm remains the base norm. For any nonconstant vertex potential \(x\), summing differences along a shortest cube path gives \(|x_u-x_v|\le k(u,v)F_{\varnothing}(x)\), hence \(F_{\mathcal C,T_{d,d}}(x)\le dT_{d,d}F_{\varnothing}(x)\); here \(dT_{d,d}>1\) follows from the strict bound above. Taking \(x(u)=\sum_i u_i\) achieves equality at antipodal endpoints, proving the exact pointwise ratio and its asymptotic expansion.

## Verification

Run `python check.py` with NumPy and SciPy installed. It constructs the cube incidence matrix independently of the Walsh formula and compares \(R_{d,k}\) for all distances in dimensions three through six with a direct spectral inverse-square-root calculation. It also checks the strict inequalities, the exact baseline spectral trace, chord-weight optimizations below and above their thresholds (dimensions three and four), and the leading dimension-asymptotic coefficient. The delivered execution passed **44** separate checks. Finite tests corroborate, but do not establish, the all-dimensional claims. The complete proof is above.

## Relationship to prior work

The functional representation of the free \(p\)-convex lattice and its relationship with nonlinear \(p\)-summing maps are due to [1], with a broad subsequent treatment in [2]. The classical hypercube Walsh spectrum and ordinary effective-resistance/Kirchhoff-index framework are covered, for example, by [3]. Classical resistance uses \(L^\dagger\); the norm-support threshold here uses \(L^{\dagger1/2}\). The new assertions are the **exact simultaneous hypercube Hamming-distance thresholds**, their strict ordering, the **uniform near-unit high-dimensional screening law**, uniqueness of optimal row weights, and the resulting exact order-amplification phenomenon. A related cycle-specific chord-screening calculation does not give the cube's Walsh sums or their dimension-saturated asymptotics. General norm representation and the abstract concavity argument are not claimed as new.

## Limitations

No formula is asserted for the increased norm beyond threshold. The theorem is for the real Hilbert generator, exponent two, finite binary cubes, and row amplitudes as specified; no extension to other exponents or infinite-dimensional cube limits is claimed. Independent scientific audit has not occurred, and an equivalent formulation in operator-ideal or graph-design literature cannot be ruled out solely by database searches.

## References

[1] H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete, and V. G. Troitsky, *Free Banach lattices under convexity conditions*, first publicly available 2021-01-10, arXiv:2101.03510, https://arxiv.org/abs/2101.03510. Formula (1.1), Theorem 6.1, and Corollary 7.8.

[2] T. Oikhberg, M. A. Taylor, P. Tradacete, and V. G. Troitsky, *Free Banach lattices*, arXiv:2210.00614, first publicly available 2022-10-02, https://arxiv.org/abs/2210.00614.

[3] J. Liu, J. Cao, X.-F. Pan, and A. Elaiw, *The Kirchhoff Index of Hypercubes and Related Complex Networks*, Discrete Dynamics in Nature and Society (2013), article 543189, https://doi.org/10.1155/2013/543189.
