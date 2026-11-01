# Deleted-edge cliques: a linear spectral formula and first symmetry-breaking Hilbert extremizers

## Finding

Let \(m\ge1\) be an integer, \(N=m+2\), and \(G_m=K_N\setminus\{uv\}=K_m\vee\overline{K_2}\), with unit graph distance and counting measure. Write \(M_m\) for the *centered* Hardy–Littlewood maximal map
\[
M_mf(v)=\max_{r\ge0}\frac1{|B(v,r)|}\sum_{w\in B(v,r)}|f(w)|.
\]
For every \(m\ge1\), the sharp squared real \(\ell^2\) norm admits the following **explicit linear-size spectral formula**, involving at most \(4(m+1)\) matrices of size at most four:
\[
\boxed{\ \|M_m\|_{2\to2}^{\,2}=\max_{0\le k\le m}\ \max_{\varepsilon_1,\varepsilon_2\in\{0,1\}}
\max\{\mathbf1_{\{k\ge2\}},\rho(T_{m,k,\varepsilon_1,\varepsilon_2}^{\mathsf T}T_{m,k,\varepsilon_1,\varepsilon_2})\}.\ }
\]
Here \(\rho\) is the largest eigenvalue of a symmetric positive-semidefinite matrix, \(\ell=m-k\), and the matrix \(T\), with rows and columns indexed by the nonempty groups \(H_{\rm self}\), \(H_{\rm whole}\) followed by two individual nonadjacent vertices, is specified by these full four-coordinate rows before deletion of any empty-group row and column:
\[
\begin{aligned}
R_{\rm self}&=(1,0,0,0),\\
R_{\rm whole}&=\left(\frac{\sqrt{k\ell}}{N},\frac\ell N,\frac{\sqrt\ell}N,\frac{\sqrt\ell}N\right),\\
R_1^{(0)}&=\left(\frac{\sqrt k}{m+1},\frac{\sqrt\ell}{m+1},\frac1{m+1},0\right),\\
R_1^{(1)}&=\left(\frac{\sqrt k}{N},\frac{\sqrt\ell}N,\frac1N,\frac1N\right),\\
R_2^{(0)}&=\left(\frac{\sqrt k}{m+1},\frac{\sqrt\ell}{m+1},0,\frac1{m+1}\right),\\
R_2^{(1)}&=\left(\frac{\sqrt k}{N},\frac{\sqrt\ell}N,\frac1N,\frac1N\right).
\end{aligned}
\]
Take \(T\) to have the first two applicable rows followed by \(R_1^{(\varepsilon_1)}\), \(R_2^{(\varepsilon_2)}\), deleting both the first row and first column if \(k=0\), and both the second row and second column if \(\ell=0\). The indicator is zero when \(k<2\). This formula is exact, not a numerical approximation or an unresolved optimization over input functions.

There is also a strict *edge-deletion effect*: for every \(m\ge1\),
\[
\boxed{\ \|M_{K_N\setminus\{uv\}}\|_{2\to2}>\|M_{K_N}\|_{2\to2}.\ }
\]
Every nonnegative extremizer on \(G_m\) has both nonadjacent-vertex entries strictly smaller than the arithmetic mean of its \(m\) universal-vertex entries; in particular, no radius-zero average is active at either nonadjacent vertex.

The first mixed universal-vertex extremizers occur at \(m=3\). On \(K_5\setminus\{uv\}\), the exact squared norm is the unique real root \(\lambda_*\in(1.416,1.417)\) above \(1\) of
\[
\boxed{400\lambda^3-655\lambda^2+126\lambda-1=0,\qquad
\|M_3\|_{2\to2}=\sqrt{\lambda_*}\approx1.190101843.}
\]
Its three labeled nonnegative extremizing rays have values \(1,1,b_*,c_*,c_*\) after permuting the three universal vertices, where
\[
b_*=1-\lambda_*^{-1},\qquad
c_*=\frac{41(3\lambda_*-1)}{\lambda_*(400\lambda_*-57)}.
\]
Here precisely two universal vertices have value \(1\), the third has value \(b_*\), and the two nonadjacent vertices share value \(c_*\). Every nonzero real extremizer is obtained from one of these rays by nonzero scaling and independent coordinate signs. At \(m=1,2\) the maximizing ball selections instead keep *every* universal-vertex radius-zero row; thus \(m=3\) is the first member with a genuine high/low split within the universal clique.

## Assumptions and scope

All graphs are finite, simple and unweighted; all vertices have counting mass one. The graph family has exactly one missing edge, joining the two named nonadjacent vertices. The norm is the strong real \(\ell^2(V)\) norm of the nonlinear, positive, centered graph-distance-ball maximal map (not the edge-variation seminorm). The spectral expression applies for each integer \(m\ge1\), including the three-vertex path. For complex-valued signals the same norm statement follows from taking absolute values; the displayed sign classification concerns real extremizers.

## Proof

**1. The ball geometry and a finite matrix principle.** Write the universal vertices as \(h_1,\ldots,h_m\), the nonadjacent vertices as \(u,v\), put \(S=\sum_i x(h_i)\), \(U=(S+x(u)+x(v))/N\), and take \(x=|f|\ge0\). The possible centered averages are
\[
M_mx(h_i)=\max\{x(h_i),U\},\qquad
M_mx(u)=\max\left\{x(u),\frac{S+x(u)}{m+1},U\right\},
\]
with the analogous formula for \(v\). Every possible simultaneous selection of one average at each vertex is a nonnegative row-stochastic matrix \(A\). For any such matrix, \(Ax\le M_mx\) coordinatewise on nonnegative \(x\), so \(\|A\|_{2\to2}\le\|M_m\|_{2\to2}\). Conversely, selecting a maximizing row at every vertex for any \(x\ge0\) gives \(M_mx=Ax\); hence the maximal-map norm equals the maximum of the spectral norms of its row-selection matrices. Since \(A\ge0\), a top singular vector can be taken nonnegative.

**2. Strict dominance over the complete graph.** On \(K_N\), the only average choices are singleton and whole-vertex means. If \(k\) rows choose the singleton and \(\ell=N-k\) choose the mean, the top squared singular value is the larger eigenvalue
\[
\Phi(\ell/N)=\frac{1+\ell/N+\sqrt{1+2\ell/N-3(\ell/N)^2}}{2}
\]
of the two-group compression, with endpoints \(k=0,N\) giving norm one. The function \(\Phi(t)\) increases strictly until \(t=2/3\) and then decreases. Therefore a maximizing selection has \(\ell\ge2\), hence \(1\le k\le N-2=m\). Its positive Perron vector equals \(a\) on the \(k\) singleton rows and \(b\) on the remaining rows, with \(a>b>0\): if \(\lambda\) denotes the squared singular value and \(U\) the mean, its two eigenvector equations are \(\lambda a=a+\ell U/N\), \(\lambda b=\ell U/N\), yielding \(a-b=a/\lambda>0\). Thus the selected averages are active, and this vector really is a maximizing input for the complete graph.

Place all \(k\) larger coordinates on universal vertices of \(G_m\); both nonadjacent entries are \(b\). At either nonadjacent vertex the neighborhood average is
\[
\frac{ka+(\ell-1)b}{N-1}=U+\frac{k(a-b)}{N(N-1)}>U,
\]
while the complete-graph maximal value there is \(U>b\). At all universal vertices the graph and complete-graph maximal values agree. Consequently the squared output norm increases strictly at fixed input. This proves \(\|M_m\|>\|M_{K_N}\|\).

**3. A structural exclusion at every extremizer.** Let \(A_0=S/m\) be the universal-vertex mean. If \(x(u)\ge A_0\), the radius-one average at \(u\) does not exceed \(x(u)\). For \(v\), if \(x(v)\ge A_0\), its radius-one average does not exceed \(x(v)\); if \(x(v)<A_0\), then
\[
S+x(v)<(m+1)x(u),
\]
so its radius-one average is strictly smaller than \(U\). Thus for every nonnegative input with \(x(u)\ge A_0\), both nonadjacent-vertex maximal values coincide with the corresponding complete-graph values; universal rows always coincide. The same holds after exchanging \(u,v\). Since \(\|M_m\|>\|M_{K_N}\|\), no extremizer can satisfy either condition. Both nonadjacent entries must be below \(S/m\), which forces their radius-one average to exceed their singleton value strictly. Only the radius-one and whole-graph rows may be active there.

**4. Symmetry compression and the exact all-size formula.** Now choose \(k\) universal rows as singletons and \(\ell=m-k\) as whole-graph rows, and choose independently either the radius-one or whole-graph row for each of \(u,v\). By permuting universal vertices, only \(4(m+1)\) representatives remain. For a fixed representative, decompose the input orthogonally into vectors constant on each nonempty universal group, the two individual nonadjacent coordinates, and zero-sum contrasts within each universal group. On the group-constant subspace, normalized by square roots of group sizes, the averaging matrix is exactly the displayed matrix \(T\). A contrast inside the singleton group is carried identically (squared singular value \(1\)); a contrast inside the whole-graph group is annihilated (squared singular value \(0\)). These subspaces and their output images are orthogonal. Hence the full squared spectral norm is \(\max\{\mathbf1_{\{k\ge2\}},\rho(T^{\mathsf T}T)\}\), proving the announced formula. Every candidate is an actual legal row-selection matrix, so no artificial upper-bound gap is introduced.

**5. The first mixed-hub case, with an exact finite certificate.** At \(m=3\), there are \(2^3 3^2=72\) legal centered ball-selection matrices. The attached standard-library integer verifier checks, by Sylvester's leading-principal-minor criterion, that \((7/5)I-A^{\mathsf T}A\) is positive definite for exactly \(69\) selections. The other three are exactly the permutations of the choice having two singleton universal rows, one whole-graph universal row, and both nonadjacent rows using their four-vertex neighborhoods. Its representative matrix is
\[
A=\begin{pmatrix}
1&0&0&0&0\\0&1&0&0&0\\1/5&1/5&1/5&1/5&1/5\\1/4&1/4&1/4&1/4&0\\1/4&1/4&1/4&0&1/4
\end{pmatrix}.
\]
Exact determinant evaluation gives
\[
\det(zI-A^{\mathsf T}A)=\frac{(z-1)(16z-1)(400z^3-655z^2+126z-1)}{6400}.
\]
The cubic is strictly increasing for \(z\ge1\) (its derivative is positive and increasing there) and changes sign between \(1.416\) and \(1.417\). Its unique root above one is therefore the top eigenvalue, larger than \(7/5\). For \(b=1-z^{-1}\) and \(c=41(3z-1)/[z(400z-57)]\), direct algebra gives
\[
(A^{\mathsf T}A-zI)(1,1,b,c,c)^{\mathsf T}
=-\frac{400z^3-655z^2+126z-1}{z(400z-57)}(1,1,1,0,0)^{\mathsf T}.
\]
At \(z=\lambda_*\) this is a positive eigenvector. Rational bounds from the displayed root interval give
\[
0<c<b<U<L<1,
\quad U=\frac{2+b+2c}{5},\quad L=\frac{2+b+c}{4}.
\]
Thus both leading universal rows select singleton values, the lower universal row selects \(U\), and both nonadjacent rows select \(L\) strictly. The positive eigenvector attains the nonlinear norm. Every other selection is bounded below the gap threshold, and the top eigenvalue of each exceptional matrix is simple because its characteristic factors have distinct roots at the top; this proves the three-ray equality classification. The verifier also checks all \(18\) and \(36\) selections at \(m=1\) and \(m=2\), respectively, isolating their unique maximizing row patterns and establishing the first mixed-hub occurrence at \(m=3\).

## Verification

Run `python verify.py` using only the Python standard library. It checks all \(126\) selections for \(m\in\{1,2,3\}\), with \(121\) strict exclusions and \(5\) exceptional matrices across the three graph sizes; it checks the representative characteristic polynomial by exact integer determinant interpolation and isolates the relevant root using rational arithmetic. For the five-vertex graph the decisive tally is \(72=69+3\), with strict exclusion threshold \(7/5\). Exact arithmetic checks support the finite equality classification. The universal \(m\ge1\) spectral reduction and strict inequality follow from Steps 1–4 and are not extrapolated from this finite enumeration.

## Relationship to prior work

Soria–Tradacete (arXiv:1410.6204, original public version 2014-10-22) introduced the finite-graph maximal framework and established pointwise complete-graph minimality. González-Riquelme–Madrid (arXiv:2005.03146, first public version 2020-05-06) determined sharp strong Hilbert norms for complete graphs and stars, including their extremizers. Their complete-graph norm formula is compatible with Step 2 but does not provide the deleted-edge clique spectral reduction or the five-vertex mixed universal-clique equality classification. The sequel (arXiv:2011.02630, first public version 2020-11-05) extends star-graph exponent and variation results without covering this family. A separate complete-split-graph negative-type invariant does not imply maximal-operator norms. General finite row-selection enumeration is an elementary principle and is not claimed as novel; the contribution is the strict leaf-branch exclusion, exact linear-size low-rank reduction for all deleted-edge cliques, and the first mixed-hub sharp case.

## Limitations

The exact all-size expression is a finite maximum of up to \(4(m+1)\) low-order algebraic spectral quantities, not a single radical expression valid for all \(m\). The proof does not identify the winning universal-row count for every large \(m\), nor does it extend to deleting multiple edges, weighted graph measures, uncentered averages, or \(\ell^p\) exponents other than two. Absolute publication priority is not established; equivalent unindexed computations remain possible. Independent scientific validation has not been performed.

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy-Littlewood maximal operator on finite graphs*, arXiv:1410.6204, initial submission 2014-10-22; later J. Math. Anal. Appl. 436 (2016), 661–682. https://arxiv.org/abs/1410.6204
2. C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146, initial submission 2020-05-06. https://arxiv.org/abs/2005.03146
3. C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630, initial submission 2020-11-05. https://arxiv.org/abs/2011.02630
