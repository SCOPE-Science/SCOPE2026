# Sharp centro-affine spectral gap along the cube–octahedron interpolation

## Finding
For every \(1<c<3\), define
\[
K_c=[-1,1]^3\cap\left\{x\in\mathbb R^3:\sum_{i=1}^3|x_i|\le c\right\}.
\]
Equip the fourteen facets of \(K_c\) with the Hu–Ivaki weighted facet-network operator, defined precisely below. Its **complete antipodally even generalized spectrum** is
\[
\boxed{0^{[1]},\quad T(c)^{[3]},\quad S(c)^{[2]},\quad M(c)^{[1]}},
\]
where a superscript in square brackets denotes multiplicity. All nonzero eigenvalues are positive; coincidences are combined with their multiplicities.

Let \(u,v,a,d,b\) denote respectively the mass of one diagonal facet, the mass of one coordinate facet, the conductance of a diagonal–coordinate ridge, a diagonal–diagonal ridge, and a coordinate–coordinate ridge. For \(1<c\le2\),
\[
\begin{aligned}
u&=\frac c2(-2c^2+6c-3),&v&=2(c-1)^2,\\
a&=c(c-1),&d&=\frac{c^2(2-c)}2,&b&=0.
\end{aligned}
\]
For \(2\le c<3\),
\[
\begin{aligned}
u&=\frac c2(3-c)^2,&v&=4-2(3-c)^2,\\
a&=c(3-c),&d&=0,&b&=2(c-2).
\end{aligned}
\]
The two parameter descriptions agree at \(c=2\). The three positive branches are
\[
\boxed{T(c)=\frac{4d+3a}{u},\quad S(c)=\frac{4a+6b}{v},\quad M(c)=\frac{3a}{u}+\frac{4a}{v}.}
\]
In particular the first nonconstant even eigenvalue is
\[
\boxed{\lambda_{1,e}(K_c)=
\begin{cases}
\dfrac{2(-2c^2+7c-3)}{-2c^2+6c-3},&1<c\le c_*,\\[2pt]
\dfrac{2c}{c-1},&c_*\le c\le2,\\[2pt]
\dfrac{4c(3-c)+12(c-2)}{4-2(3-c)^2},&2\le c<3,
\end{cases}}
\]
where
\[
\boxed{c_*=\frac{7+\sqrt{13}}6\in(1,2),\qquad
\max_{1<c<3}\lambda_{1,e}(K_c)=1+\sqrt{13},}
\]
and \(c_*\) is the **unique** maximizer. The lowest nonconstant eigenspace has multiplicity three for \(1<c<c_*\), multiplicity five at \(c_*\), and multiplicity two for \(c_*<c<3\). The spectral crossing lies strictly inside a single polytope-combinatorial chamber, not at the cuboctahedral transition \(c=2\).

## Assumptions and scope
The facets are indexed by the eight signs \(\sigma\in\{\pm1\}^3\), with outer unit normals \(\sigma/\sqrt3\) and supports \(h_\sigma=c/\sqrt3\), and the six signed coordinate normals \(\pm e_i\), with supports \(1\). For every facet \(F\), define the positive mass
\[
m_F=h_F\mathcal H^2(F).
\]
For distinct facets sharing an edge, define
\[
w_{FG}=\frac{h_F h_G\mathcal H^1(F\cap G)}{\sin\theta_{FG}},
\]
where \(\theta_{FG}\) is the angle of the two unit normals; for nonadjacent facets put \(w_{FG}=0\). Define the finite-dimensional Dirichlet form
\[
\mathcal E(f)=\sum_{\{F,G\}}w_{FG}(f_F-f_G)^2
\]
and the weighted mean \(\bar f=(\sum_F m_F f_F)/(\sum_Fm_F)\). Eigenvalues are those of \((\operatorname{diag}m)^{-1}L\), where \(L\) is the graph Laplacian of \(w\), on the space satisfying \(f_{-F}=f_F\). The first positive eigenvalue minimizes \(\mathcal E(f)/\sum_Fm_F(f_F-\bar f)^2\) among nonconstant even functions. No local-minimality assumption is made.

## Proof
**Facets and conductances.** For \(1<c<2\), each diagonal facet is a hexagon with vertices obtained by permuting \((1,c-1,0)\), with the appropriate coordinate signs; its area is \(\sqrt3[c^2-3(c-1)^2]/2\). Each coordinate facet is a diamond of area \(2(c-1)^2\). A diagonal facet meets three coordinate facets in edges of length \(\sqrt2(c-1)\), and three other diagonal facets, obtained by flipping one sign, in edges of length \(\sqrt2(2-c)\). Two diagonal normals differing in one sign have \(\sin\theta=2\sqrt2/3\); a diagonal and coordinate normal have \(\sin\theta=\sqrt{2/3}\). Substitution into the mass and conductance definitions gives the first group of formulas.

For \(2<c<3\), a diagonal facet is a triangle with vertices obtained by permuting \((1,1,c-2)\) and applying its fixed outward sign pattern, of area \(\sqrt3(3-c)^2/2\). A coordinate facet is the octagon obtained from \([-1,1]^2\) by clipping four triangles of leg length \(3-c\), so its area is \(4-2(3-c)^2\). Each diagonal facet meets three coordinate facets in edges of length \(\sqrt2(3-c)\), and each coordinate facet meets four other coordinate facets in edges of length \(2(c-2)\). Distinct coordinate normals are perpendicular. The second group of formulas follows. The limiting formulas at \(c=2\) agree with the cuboctahedron's triangular and square facets; zero-length edges have zero conductance.

**The exact spectrum.** On even functions, the eight diagonal facets form four antipodal pairs and the six coordinate facets form three pairs. Write their values as \(t_1,\ldots,t_4\) and \(s_1,s_2,s_3\). Every diagonal pair is linked to each of the three coordinate pairs by one edge of weight \(a\) per representative. For \(1<c<2\), the three diagonal–diagonal neighbors of a representative become the three other diagonal pairs, each with weight \(d\). For \(2<c<3\), the four coordinate–coordinate neighbors of a representative become two neighbors in each of the two other coordinate pairs, each with conductance \(b\).

With \(\Sigma_t=\sum_{i=1}^4t_i\) and \(\Sigma_s=\sum_{j=1}^3s_j\), the generalized eigen-operator is
\[
\begin{aligned}
(\mathcal L t)_i&=\frac{(4d+3a)t_i-d\Sigma_t-a\Sigma_s}{u},\\
(\mathcal L s)_j&=\frac{(4a+6b)s_j-a\Sigma_t-2b\Sigma_s}{v}.
\end{aligned}
\]
The diagonal zero-sum subspace (dimension three) has eigenvalue \(T=(4d+3a)/u\). The coordinate zero-sum subspace (dimension two) has eigenvalue \(S=(4a+6b)/v\). The two-dimensional subspace constant separately on the diagonal and coordinate classes has eigenvalues \(0\) and \(M=3a/u+4a/v\). These subspaces are independent and span the seven-dimensional even space, proving the complete list.

**Ordering and maximization.** On \(1<c<2\), we have \(M>S\), and
\[
M-T=4\left(\frac a v-\frac d u\right)>0,
\]
because the numerator \(au-dv=c^2(c-1)/2\) is strictly positive. On \(2\le c<3\), \(M>T=6/(3-c)\) and \(T\ge6\), while \(S\) decreases strictly from \(4\) to the limit \(3\). Hence the least positive eigenvalue is always \(\min\{T,S\}\).

On \(1<c<2\), the difference \(T-S\) has the sign of \(3c^2-7c+3\). This polynomial has the unique root \(c_*=(7+\sqrt{13})/6\) in \((1,2)\), so the stated branches and multiplicities follow. Direct differentiation yields
\[
T'(c)=\frac{2(2c^2-3)}{(-2c^2+6c-3)^2},\qquad
S'(c)=-\frac2{(c-1)^2}\quad(1<c<2),
\]
and for \(2<c<3\) the derivative of the displayed upper-chamber \(S\) is
\[
S'(c)=\frac{4(c-3)}{(c^2-6c+7)^2}<0.
\]
Thus \(T\) first decreases, then increases on \((1,c_*)\), with endpoint limit \(4\) at \(c\downarrow1\), and \(S\) strictly decreases on \((c_*,3)\). Since \(S(c_*)=2c_*/(c_*-1)=1+\sqrt{13}>4\), the unique sharp global maximum is attained at \(c_*\).

## Verification
The standalone `verify.py` constructs the **full fourteen-facet** weighted graph independently from the two possible edge-adjacency patterns, then checks seven exact eigenvectors spanning the even subspace for eleven distinct rational parameters on both sides of \(c=2\). It uses Python's standard-library exact fractions only. The result is `VERIFY_OK exact even facet-network eigenvectors, 11 rational parameters`. These finite checks corroborate, but do not replace, the symbolic facet classification and all-parameter proof.

## Relationship to prior work
Hu and Ivaki [1] introduced the facet masses, conductances, and spectral-gap problem and proved a conditional lower bound for local minimizers. The theorem here determines **every even eigenvalue** of an explicit one-parameter family, with no local-minimizer premise. The conditional bound alone cannot imply these four branches, the eigenvalue crossing, or the sharp algebraic maximum.

A published calculation [2] gives the exact even spectrum of all parallelotopes, including the cubical endpoint, where the first even eigenvalue is \(3\). Its fixed-shape statement cannot imply the nonconstant profile on \(1<c<3\). A different published calculation [3] determines the **ordinary illumination number** of the same cube–octahedron interpolation; illumination and the Hu–Ivaki weighted facet spectrum are mathematically different invariants, and neither determines the other. Related spectral-polyhedra literature [4] concerns matrix-eigenvalue-invariant convex sets rather than the present facet-network spectrum.

## Limitations
The theorem is restricted to this three-dimensional cube–octahedron intersection family and to the antipodally even Hu–Ivaki facet operator. It does not assert a universal spectral inequality or spectral rigidity for arbitrary centrally symmetric polytopes, nor does it establish any local-minimizing property in an ambient polytope class. The primary text of [1] was unavailable through the attempted open-access routes; accessible abstract/secondary descriptions and the full published comparison [2] did not establish this exact profile, but a previously unindexed calculation remains an originality risk. No independent audit has been performed.

## References
[1] Y. Hu and M. N. Ivaki, *Centro-affine spectral geometry of polytopes*, arXiv:2609.21670v1, first public 2026-09-18, especially the definitions of facet masses and ridge conductances.

[2] *Exact even centro-affine facet spectrum of parallelotopes*, public mathematical record, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-even-centro-affine-facet-spectrum-of-parallelotopes--96d0f3f42485.

[3] *Exact illumination phase profile of the cube–octahedron intersection family*, public mathematical record, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-illumination-phase-profile-of-the-cube-octahedron-intersec--20022a556c31.

[4] R. Sanyal and J. Saunderson, *Spectral Polyhedra*, Forum of Mathematics, Sigma 13 (2025), e30, DOI:10.1017/fms.2024.62.
