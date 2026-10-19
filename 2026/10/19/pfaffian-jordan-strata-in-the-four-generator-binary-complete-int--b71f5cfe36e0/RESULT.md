# Pfaffian Jordan strata in the four-generator binary complete intersection

## Finding

Let \(q\) be any positive power of \(2\), let
\[
R_q=\mathbb F_q[x_1,x_2,x_3,x_4]/(x_1^2,x_2^2,x_3^2,x_4^2),
\qquad \mathfrak m=(x_1,x_2,x_3,x_4),
\]
and set \(\rho(u)=\operatorname{rank}_{\mathbb F_q}(\mu_u)\) for multiplication \(\mu_u:R_q\longrightarrow R_q\), \(v\mapsto uv\). The complete rank-generating polynomial for the fifteen-dimensional radical is
\[
\boxed{\begin{aligned}
\mathcal J_q(T)=\sum_{u\in\mathfrak m}T^{\rho(u)}
={}&1+(q-1)T+q(q^4-1)T^2\\
&+q^5(q^2+1)(q^3-1)T^4\\
&+q^7(q-1)(q^3-1)T^6\\
&+q^{11}(q^4-1)T^8.
\end{aligned}}
\]
No other ranks occur. Because \(u^2=0\) for every \(u\in\mathfrak m\), the Jordan partition of \(\mu_u\) is exactly \((2^{\rho(u)},1^{16-2\rho(u)})\). Thus the polynomial determines the entire Jordan-type distribution of all radical elements, not merely the generic type.

There is also a geometric classification. Write an element of \(\mathfrak m^2\) uniquely as \(u=\alpha+\beta+\gamma\), with homogeneous pieces in degrees \(2,3,4\), and write
\[
\alpha=\sum_{1\le i<j\le4} a_{ij}x_ix_j,
\qquad
P(\alpha)=a_{12}a_{34}+a_{13}a_{24}+a_{14}a_{23}.
\]
Then \(\rho(u)=6\) precisely when \(P(\alpha)\ne0\), and \(\rho(u)=4\) precisely when \(\alpha\ne0\) and \(P(\alpha)=0\). In particular, the rank-four exceptional stratum is the nonzero Pfaffian cone in degree two, times the free degree-three and degree-four coordinates.

## Assumptions and scope

All assertions hold for every finite field of characteristic \(2\), not only prime fields. The algebra has vector-space basis \(x_S=\prod_{i\in S}x_i\) for \(S\subseteq\{1,2,3,4\}\), so \(\dim R_q=16\) and \(\dim\mathfrak m=15\). Coefficients are allowed in all positive degrees; no homogeneity condition is imposed on \(u\).

The exact rank classification is: \(\rho(u)=8\) if the linear component is nonzero; if it vanishes, ranks \(6,4\) are characterized by the above degree-two Pfaffian; if all degree-two coefficients vanish, rank \(2\) occurs exactly when the cubic component is nonzero, rank \(1\) exactly when only the quartic component is nonzero, and rank \(0\) exactly at zero.

The algebra is also the group algebra \(\mathbb F_q[(C_2)^4]\), after identifying \(x_i\) with \(g_i-1\). Thus this is the regular-module radical Jordan spectrum of that modular group algebra. As a geometric assertion, the rank loci are understood as constructible subsets of the fifteen-dimensional affine radical parameter space over \(\mathbb F_q\). Their Zariski closures after extension to an algebraic closure, not the closures of the finite sets of rational points, form the chain
\[
\{0\}\subset\mathfrak m^4\subset\mathfrak m^3\subset
\{u\in\mathfrak m^2:P(\alpha)=0\}\subset\mathfrak m^2\subset\mathfrak m,
\]
corresponding respectively to closures of the rank \(0,1,2,4,6,8\) strata.

## Proof

**1. Square-zero property and the open stratum.** Since every positive-degree squarefree monomial has square zero and the characteristic is two, \(u^2=0\) for all \(u\in\mathfrak m\). If the linear component of \(u\) is nonzero, make an invertible linear change of variables so that it is \(x_1\). The substitution \(x_1\mapsto u\), \(x_j\mapsto x_j\) for \(j=2,3,4\) is a well-defined endomorphism because all images square to zero. It induces the identity on \(\mathfrak m/\mathfrak m^2\), hence is an automorphism by Nakayama's lemma (or by induction on the radical filtration). Therefore \(\mu_u\) is conjugate to \(\mu_{x_1}\) as a linear endomorphism, and its rank is \(8\). There are \((q^4-1)q^{11}\) such elements, because eleven coefficients in degrees at least two are unrestricted.

**2. Quadratic stratum.** Suppose the linear component vanishes and \(\alpha\ne0\). Multiplication respects the degree filtration: \(\mu_u(1)\) has nonzero degree-two component \(\alpha\); the map on degree one, after projecting to degree three, is \(v\mapsto\alpha v\); and the map \(R_{q,2}\to R_{q,4}\) is the nonzero functional \(w\mapsto\alpha w\) by the perfect complementary-degree product pairing. Hence the degree-zero image contributes one dimension, the degree-two domain contributes the degree-four line, and the degree-one image contributes exactly the rank of \(v\mapsto\alpha v\) modulo that line. Higher-degree terms in \(u\) only add degree-four components already spanned by the image of \(R_{q,2}\). Therefore
\[
\rho(u)=2+\operatorname{rank}(R_{q,1}\xrightarrow{\alpha\cdot}R_{q,3}).
\]
Using the monomial bases and the volume-form identification \(R_{q,3}\cong R_{q,1}^*\), the displayed map is a \(4\)-by-\(4\) alternating matrix whose independent entries are the six coefficients of \(\alpha\), up to permutation. Its rank is \(4\) if the Pfaffian \(P(\alpha)\) is nonzero and \(2\) otherwise, since \(\alpha\ne0\).

To count the rank-two alternating matrices, choose their two-dimensional radical, in \({4\brack2}_q\) ways, and then a nondegenerate alternating form on the two-dimensional quotient, in \(q-1\) ways. Hence their number is
\[
{4\brack2}_q(q-1)=(q^2+1)(q^3-1).
\]
Of the \(q^6-1\) nonzero alternating matrices, the remainder have rank four; their number is \(q^2(q-1)(q^3-1)\). Five independent coefficients of degrees three and four remain free. Multiplying these counts by \(q^5\) gives the coefficients of \(T^4\) and \(T^6\).

**3. Higher-degree strata.** If the linear and quadratic terms vanish but the cubic term \(\beta\) is nonzero, then \(\mu_u(1)=\beta+\gamma\) contributes one dimension in degree three, and \(R_{q,1}\to R_{q,4}\), \(v\mapsto\beta v\), is a nonzero functional, contributing a second. Thus rank is \(2\), and there are \((q^4-1)q\) choices. A nonzero pure quartic contributes rank \(1\), with \(q-1\) choices. Zero contributes rank \(0\). This exhausts all \(q^{15}\) radical elements; summing the six coefficients independently recovers \(q^{15}\).

**4. Geometry.** Over the algebraic closure the Pfaffian \(P\) is a nondegenerate split quadratic form in six coefficients, with nonempty nonsingular locus and irreducible zero hypersurface. Thus the rank-four stratum is dense in its Pfaffian hypersurface, the rank-six stratum is dense in \(\mathfrak m^2\), the cubic-nonzero stratum is dense in \(\mathfrak m^3\), and the quartic-nonzero stratum is dense in \(\mathfrak m^4\). The linear-nonzero stratum is dense in \(\mathfrak m\). This gives the closure chain. The nondiagonal rank strata do not merge because the closures have different defining equations and dimensions.

## Verification

Run `python3 verify_rank_spectrum.py` from the same directory as this document, using Python 3 with no third-party packages. The checker enumerates all \(2^{15}=32768\) radical elements of the binary case, constructs their full multiplication ranks by independent binary elimination, and checks the six theoretical counts. It also enumerates all \(4^6=4096\) quadratic coefficients over \(\mathbb F_4\), independently computes the complete \(16\)-by-\(16\) multiplication rank, and checks \(300\) seeded full-coefficient samples over \(\mathbb F_4\). The resulting binary histogram is \(\{0:1,1:1,2:30,4:1120,6:896,8:30720\}\). The quaternary quadratic histogram is \(\{0:1,4:1071,6:3024\}\). The general-field statements are proved above; finite tests are not used as their proof.

## Relationship to prior work

Iarrobino, Macias Marques and McDaniel (arXiv:1802.07383, initial posting 2018-02-21) develop Jordan-type loci for Artinian modules, including nonhomogeneous radical elements. Their general framework makes the present rank distribution a natural question, but the inspected introduction, general Jordan-type results, examples, and discussion of loci do not supply its explicit characteristic-two four-generator Pfaffian equation or finite-field multiplicities. The present result is not a claim to have introduced Jordan-type loci.

Costa and Gondim (arXiv:1811.02072, 2018) compute Jordan types from mixed Hessians and discuss low socle degrees, assuming characteristic zero and concentrating on multiplication by linear forms. In particular their socle-degree-four classification does not imply this characteristic-two census of *all* radical elements. Korhonen (arXiv:2101.01365, 2021) treats Jordan blocks on exterior and symmetric squares induced by nilpotent/unipotent linear operators; those are not multiplication operators by arbitrary elements of the exterior algebra. Altafi, Iarrobino and Khatami (arXiv:1810.00716, 2018) treat linear-form Jordan types for two-variable complete intersections in characteristic zero or sufficiently large characteristic.

The potentially novel content is the **complete all-radical finite-field frequency and algebraic rank-locus stratification**, with a Pfaffian wall separating ranks four and six. All standard alternating-form counts, the identification with an exterior algebra in characteristic two, and general Jordan-type formalism are acknowledged prerequisites rather than novelty claims.

## Limitations

The claimed formula is confined to four generators over fields of characteristic two; it does not enumerate analogous ranks in five or more generators or in odd characteristic. It does not classify all modules of the group algebra, only its regular module. Rank strata are not claimed to distinguish individual algebra-automorphism orbits. The full historical priority of the exact six-term formula and its geometric formulation has not been established independently; an older equivalent exterior-algebra multiplication-rank result could exist under different terminology. Computational checks over two finite fields do not prove the result for every field; the proof uses an arbitrary field of characteristic two.

## References

- A. Iarrobino, P. Macias Marques and C. McDaniel, *Artinian algebras and Jordan type*, arXiv:1802.07383, initially posted 2018-02-21, https://arxiv.org/abs/1802.07383.
- B. Costa and R. Gondim, *The Jordan type of graded Artinian Gorenstein algebras*, arXiv:1811.02072, initially posted 2018-11-05, https://arxiv.org/html/1811.02072v2.
- N. Altafi, A. Iarrobino and L. Khatami, *Complete intersection Jordan types in height two*, arXiv:1810.00716, initially posted 2018-10-01, https://arxiv.org/abs/1810.00716.
- M. Korhonen, *Decomposition of exterior and symmetric squares in characteristic two*, arXiv:2101.01365, initially posted 2021-01-05, https://arxiv.org/abs/2101.01365.
