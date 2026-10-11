# A finite equilateral Lipschitz-free space separates quantitative \(\Delta\)-geometry from distant molecules

## Finding
Let \(M=\{a_0,a_1,a_2,b_0,b_1,b_2\}\) be the six-point equilateral metric space, with every distance between distinct points equal to \(1\). Work over the real scalar field. Let \(X=\mathcal F(M)\), and identify it with zero-total-mass vectors in \(\mathbb R^6\), equipped with half the \(\ell_1\) norm. Define
\[
 x=\tfrac12\delta_{a_0}+\tfrac14\delta_{a_1}+\tfrac14\delta_{a_2}
 -\tfrac34\delta_{b_0}-\tfrac18\delta_{b_1}-\tfrac18\delta_{b_2}.
\]
Then \(\|x\|=1\), its pointwise Daugavet constant is exactly
\[
 \operatorname{dc}_X(x)=\tfrac34,
\]
and its pointwise \(\Delta\)-constant satisfies
\[
 \delta\operatorname{c}_X(x)\ge\tfrac78.
\]
Nevertheless, in *every* convex representation of \(x\) by unit molecules, the molecule \(m_{a_0b_0}=\delta_{a_0}-\delta_{b_0}\), at distance exactly \(3/4\) from \(x\), carries coefficient at least \(1/4\). Consequently the largest radius admitting a convex decomposition of \(x\) solely into molecules at least that far away is exactly \(3/4\), strictly below the \(\Delta\)-constant lower bound. This is a quantitative obstruction to restricting \(\Delta\)-constant convex-hull witnesses to molecules, even for a finite equilateral metric.

## Assumptions and scope
The ground field is \(\mathbb R\). All six locations are distinct and have mutual metric distance \(1\). Choose any one location as the base point; zero-mass coordinate notation is independent of this choice. For \(z=(z_u)_{u\in M}\) with \(\sum z_u=0\),
\[
 \|z\|_{\mathcal F(M)}=\tfrac12\sum_{u\in M}|z_u|.
\]
Every unit molecule is an oriented difference \(m_{uv}=\delta_u-\delta_v\) with \(u\ne v\); the finite-dimensional unit ball is their convex hull. For \(z\in B_X\), the Daugavet constant and \(\Delta\)-constant are
\[
 \operatorname{dc}_X(z)=\inf_{S\text{ slice of } B_X}\sup_{y\in S}\|y-z\|,
 \qquad
 \delta\operatorname{c}_X(z)=\inf_{\substack{S\text{ slice of } B_X\\z\in S}}\sup_{y\in S}\|y-z\|.
\]
A slice is \(S=\{y\in B_X:f(y)>\sup_{w\in B_X}f(w)-\varepsilon\}\) for a nonzero continuous real linear functional \(f\) and \(\varepsilon>0\).

## Proof
**The Daugavet constant.** For any ordered distinct locations \(u,v\), writing \(x_u^+=\max\{x_u,0\}\) and \(x_v^-=\max\{-x_v,0\}\), the coordinate bound \(|x_u|\le1\) gives
\[
 \|x-m_{uv}\|=2-x_u^+-x_v^-.
\]
The largest positive coordinate of \(x\) is \(1/2\), and the largest negative magnitude is \(3/4\), attained at \(a_0\) and \(b_0\) respectively. Thus the minimum molecule distance equals \(2-1/2-3/4=3/4\). Every nonempty slice of the finite polytope \(B_X\) contains a vertex, hence a molecule, so every slice contains a point at distance at least \(3/4\) from \(x\). Conversely, the vertex \(m_{a_0b_0}\) is strongly exposed: the linear functional taking coordinate potentials \(1\) at \(a_0\), \(-1\) at \(b_0\), and \(0\) elsewhere attains a unique maximum at that molecule. Slices shrinking toward it give the matching upper bound on \(\operatorname{dc}_X(x)\).

**The molecule-only obstruction.** The functional \(\varphi(z)=z_{a_0}+z_{a_1}+z_{a_2}\) is at most \(1\) on every unit molecule and satisfies \(\varphi(x)=1\). Thus a convex decomposition of \(x\) into molecules can use only the nine oriented cross-part molecules \(m_{a_i b_j}\). The coefficients \(\lambda_{ij}\) form a nonnegative transportation matrix with row sums
\[
 (p_0,p_1,p_2)=(\tfrac12,\tfrac14,\tfrac14)
\]
and column sums
\[
 (q_0,q_1,q_2)=(\tfrac34,\tfrac18,\tfrac18).
\]
Since the union of row \(0\) and column \(0\) has mass at most \(1\),
\[
 \lambda_{00}\ge p_0+q_0-1=\tfrac14.
\]
The forced molecule is precisely \(m_{a_0b_0}\), whose distance is \(3/4\). Since all molecules are at least that distant and the unit ball is their convex hull, the supremal molecular-only radius is exactly \(3/4\).

**Twelve distant nonmolecular witnesses.** Parameterize a unit vector in the same exposed face by two probability vectors \(r,s\in\mathbb R_+^3\):
\[
 y(r,s)=\sum_{i=0}^2r_i\delta_{a_i}-\sum_{j=0}^2s_j\delta_{b_j},
 \qquad
 \|x-y(r,s)\|=\tfrac12(\|p-r\|_1+\|q-s\|_1).
\]
Take the following three prototype pairs, in the coordinate order \(0,1,2\):
\[
\begin{aligned}
 A:&\quad r=(0,0,1), &s=(7/8,1/8,0),\\
 B:&\quad r=(1/8,0,7/8), &s=(1,0,0),\\
 C:&\quad r=(1,0,0), &s=(1/2,1/2,0).
\end{aligned}
\]
For each pair, independently interchange coordinates \(1\) and \(2\) of \(r\) and of \(s\), giving four equally weighted orbit entries (allowing repetitions). Every resulting vector \(y\) is in \(S_X\), and exact coordinate subtraction gives \(\|x-y\|=7/8\). Let \(\overline A,\overline B,\overline C\) denote the corresponding orbit averages as vectors of \(X\). Their positive-side and negative-side distributions are respectively
\[
\begin{aligned}
 \overline A:&\quad (0,1/2,1/2), &(7/8,1/16,1/16),\\
 \overline B:&\quad (1/8,7/16,7/16), &(1,0,0),\\
 \overline C:&\quad (1,0,0), &(1/2,1/4,1/4).
\end{aligned}
\]
A direct rational identity gives
\[
 x=\tfrac2{11}\overline A+\tfrac4{11}\overline B+\tfrac5{11}\overline C.
\]
Thus \(x\) is a convex combination of twelve unit vectors, each at distance \(7/8\). For every slice \(S\) containing \(x\), at least one of these twelve vectors belongs to \(S\) (apply the defining strict affine inequality to the convex combination). Therefore \(\sup_{y\in S}\|y-x\|\ge7/8\), proving \(\delta\operatorname{c}_X(x)\ge7/8\).

## Verification
A standalone exact-rational checker, `check_certificate.py`, enumerates the four orbit entries for each prototype, checks their norms and all twelve distances, reconstructs the barycenter, enumerates all thirty oriented molecules, and checks the forced-mass inequality. Run it with `python check_certificate.py` using the standard Python library. The mathematical proof above does not depend on this calculation.

## Relationship to prior work
Choi and Jung introduced and developed pointwise Daugavet and \(\Delta\)-constants. Their general denting-point characterization determines the Daugavet constant here, and their general convex-hull characterization motivates the need for nonmolecular witnesses for the \(\Delta\)-constant. They provided a different infinite-dimensional example separating the two constants, whereas the present construction concerns a finite equilateral Lipschitz-free space and explicitly separates distant *molecule-only convex hulls* from distant unrestricted convex hulls. Abrahamsen and coauthors characterized representations of finitely supported exact \(\Delta\)-points as convex combinations of exact \(\Delta\)-molecules; that qualitative endpoint theorem does not assert the same representation at intermediate quantitative radii. The current witness is strictly below the endpoint value \(2\).

## Limitations
The example yields \(\delta\operatorname{c}_X(x)\ge7/8\), not an exact evaluation of that constant. No minimality of six points and no classification of all equilateral configurations is asserted. The molecule-only statement concerns convex representations of this particular \(x\), not every Lipschitz-free-space element. Independent mathematical review remains outstanding.

## References
1. G. Choi and M. Jung, *The Daugavet and Delta-constants of points in Banach spaces*, arXiv:2307.10647, first submitted 20 July 2023, especially Definition 2.1, Proposition 2.3 and Theorem 3.12. https://arxiv.org/abs/2307.10647
2. T. A. Abrahamsen, R. J. Aliaga, V. Lima, A. Martiny, Y. Perreau, A. Procházka and T. Veeorg, *Delta-points and their implications for the geometry of Banach spaces*, Journal of the London Mathematical Society (2024), DOI:10.1112/jlms.12913, especially Theorem 6.9. https://doi.org/10.1112/jlms.12913
