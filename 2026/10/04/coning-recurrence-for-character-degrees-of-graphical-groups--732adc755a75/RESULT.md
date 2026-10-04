# Coning recurrence for character degrees of graphical groups

## Finding

Let \(\Gamma\) be a finite simple graph on \(n\) vertices. For a prime power \(q\), write
\[
\rho_i(\Gamma;q)
=
\#\left\{
y\in\mathbf F_q^{E(\Gamma)}:
\operatorname{rank}B_\Gamma(y)=2i
\right\},
\]
where \(B_\Gamma(y)\) is the alternating matrix supported on the edges of \(\Gamma\).

Let
\[
\widehat{\Gamma}=K_1\vee\Gamma
\]
be the cone over \(\Gamma\), obtained by adjoining one universal vertex. Then
\[
\rho_0(\widehat{\Gamma};q)=1
\]
and, for every \(i\ge1\),
\[
\boxed{
\rho_i(\widehat{\Gamma};q)
=
q^{2i}\rho_i(\Gamma;q)
+
\left(q^n-q^{2i-2}\right)\rho_{i-1}(\Gamma;q).
}
\]

Therefore, whenever every \(\rho_i(\Gamma;q)\) is polynomial in \(q\), the same is true for every cone over \(\Gamma\), and hence for every iterated cone
\[
K_t\vee\Gamma.
\]
Combining this recurrence with the published all-characteristic character-rank formula for graphical groups shows that polynomial character-degree enumeration is likewise preserved by coning.

As an explicit new family, let
\[
\Gamma=K_{a,b}.
\]
For
\[
0\le r\le\min(a,b),
\]
write
\[
N_{a,b,r}(q)
=
\#\{M\in M_{a\times b}(\mathbf F_q):\operatorname{rank}M=r\}
=
\prod_{j=0}^{r-1}
\frac{(q^a-q^j)(q^b-q^j)}{q^r-q^j},
\]
with \(N_{a,b,0}(q)=1\) and \(N_{a,b,r}(q)=0\) outside the displayed range.

For the complete tripartite graph \(K_{1,a,b}=K_1\vee K_{a,b}\),
\[
\boxed{
\operatorname{ch}(K_{1,a,b},r;q)
=
q^{a+b+1-2r}
\left(
q^{2r}N_{a,b,r}(q)
+
\left(q^{a+b}-q^{2r-2}\right)N_{a,b,r-1}(q)
\right).
}
\]
This holds for every prime power \(q\). Iterating the cone recurrence gives polynomial character-degree multiplicities for the larger complete multipartite family
\[
K_t\vee K_{a,b}
=
K_{\underbrace{1,\ldots,1}_{t\text{ singleton parts}},a,b}.
\]

## Assumptions and scope

For a finite simple graph \(\Gamma=(V,E)\), the edge-supported alternating matrix \(B_\Gamma(y)\) is the matrix whose \((u,v)\)-entry is the edge coordinate \(y_{\{u,v\}}\) up to the alternating sign convention, and is zero on nonedges.

For the associated graphical group \(\mathbf G_\Gamma(\mathbf F_q)\), write
\[
\operatorname{ch}(\Gamma,i;q)
=
\#\left\{
\chi\in\operatorname{Irr}(\mathbf G_\Gamma(\mathbf F_q)):
\chi(1)=q^i
\right\}.
\]
A published all-characteristic character-rank theorem gives
\[
\operatorname{ch}(\Gamma,i;q)
=
q^{|V|-2i}\rho_i(\Gamma;q)
\]
for every prime power \(q\).

The new statement proved here is the exact transformation law for the entire alternating rank distribution under the natural graph operation of adjoining a universal vertex, together with its character-enumeration consequences.

## Proof

Order the old vertices first and the new universal vertex last. After specializing all edge variables, the alternating matrix of the cone has the block form
\[
\widetilde B
=
\begin{pmatrix}
B&x\\
-x^{\mathsf T}&0
\end{pmatrix},
\]
where
\[
B=B_\Gamma(y)
\]
and \(x\in\mathbf F_q^n\) is arbitrary.

We use the following bordered-alternating rank lemma.

Suppose
\[
\operatorname{rank}B=2s.
\]
Then
\[
\operatorname{rank}\widetilde B
=
\begin{cases}
2s,&x\in\operatorname{im}B,\\
2s+2,&x\notin\operatorname{im}B.
\end{cases}
\]

Indeed, if \(x=Bz\), a simultaneous elementary row-and-column congruence replacing the new basis vector by the new basis vector minus \(z\) removes the border \(x\). Hence \(\widetilde B\) is congruent to \(B\oplus0\).

If \(x\notin\operatorname{im}B\), let
\[
R=\ker B.
\]
For an alternating matrix,
\[
\operatorname{im}B=R^\perp.
\]
Thus some \(u\in R\) satisfies
\[
x^{\mathsf T}u\ne0.
\]
Choose a complement \(W\) of \(R\) on which the alternating form represented by \(B\) is nondegenerate. The \(W\)-component of the border can be removed by congruence because the restriction of \(B\) to \(W\) is invertible. What remains pairs the new basis vector nontrivially with \(u\), contributing one nondegenerate alternating plane. Hence the rank rises by exactly \(2\). This argument is valid in characteristic \(2\) as well.

Now fix a specialization \(y\) with
\[
\operatorname{rank}B_\Gamma(y)=2s.
\]
There are exactly
\[
|\operatorname{im}B_\Gamma(y)|=q^{2s}
\]
choices of \(x\) that preserve the rank, and
\[
q^n-q^{2s}
\]
choices that raise it by \(2\).

To obtain cone rank \(2i\), either the old rank was already \(2i\) and the border lies in the old image, or the old rank was \(2i-2\) and the border lies outside the old image. Therefore
\[
\rho_i(\widehat{\Gamma};q)
=
q^{2i}\rho_i(\Gamma;q)
+
\left(q^n-q^{2i-2}\right)\rho_{i-1}(\Gamma;q),
\]
as claimed.

The recurrence immediately preserves polynomiality in \(q\), and iteration proves the assertion for \(K_t\vee\Gamma\).

For \(\Gamma=K_{a,b}\), after ordering the two parts the old alternating matrix is
\[
\begin{pmatrix}
0&M\\
-M^{\mathsf T}&0
\end{pmatrix},
\]
whose rank is twice the rank of \(M\). Hence
\[
\rho_r(K_{a,b};q)=N_{a,b,r}(q).
\]
Applying the cone recurrence with \(n=a+b\) gives
\[
\rho_r(K_{1,a,b};q)
=
q^{2r}N_{a,b,r}(q)
+
\left(q^{a+b}-q^{2r-2}\right)N_{a,b,r-1}(q).
\]
Multiplication by the character-rank factor
\[
q^{a+b+1-2r}
\]
gives the displayed character-degree formula.

## Verification

The included replay independently constructs edge-supported alternating matrices over the prime fields \(\mathbf F_2\) and \(\mathbf F_3\).

It exhaustively checks the cone recurrence for every simple graph on at most four vertices. For each such graph, it enumerates every edge specialization and every new universal-vertex border, computes matrix ranks by modular Gaussian elimination, and compares the directly observed cone rank histogram with the theorem.

It separately enumerates \(K_{1,a,b}\) for
\[
1\le a,b\le2
\]
over \(\mathbf F_2\) and \(\mathbf F_3\), checks the closed rank formula using the standard rectangular rank count \(N_{a,b,r}(q)\), and checks the graphical-group sum-of-squares identity implied by the character multiplicities.

The replay returns `VERIFY_OK`.

The finite replay is not used to prove the universal statement.

## Relationship to prior work

Rossmann asked how the degree multiplicities
\[
\operatorname{ch}(\Gamma,i;q)
\]
depend on \(q\), and reduced the odd-characteristic problem to rank counts of edge-supported alternating matrices. In that paper, polynomial character enumeration was recorded only for edgeless graphs, paths, and complete graphs. The same paper develops join formulas for conjugacy-class enumeration, not for irreducible-character degree multiplicities.

A later published result establishes, for every characteristic, the general character-rank identity
\[
\operatorname{ch}(\Gamma,i;q)=q^{|V|-2i}\rho_i(\Gamma;q)
\]
and gives explicit rank counts for complete bipartite graphs and complete graphs. It does not state a transformation law for \(\rho_i\) under coning or the complete-tripartite formula above.

A later paper on ask zeta functions proves strong join formulas for average kernel-size generating functions and studies adding generic rows to arbitrary matrices of linear forms. Its full text is concerned with average kernel sizes and graphical-group class-counting zeta functions; it does not state irreducible-character degree formulas, a full finite-field rank-distribution recurrence for cones, or the \(K_{1,a,b}\) character formula.

Thus the new ingredient is not the general conversion of rank counts to character counts, nor the complete-bipartite rank count. It is the exact two-term transformation of the complete rank distribution under a universal-vertex extension, which yields a closure principle and new explicit character-enumeration families.

## Limitations

The theorem treats the operation of adjoining universal vertices. It does not give a comparably simple recurrence for an arbitrary join \(\Gamma_1\vee\Gamma_2\).

The bordered-alternating rank lemma is elementary linear algebra; the mathematical contribution is its exact finite-field counting consequence for graphical groups and the resulting closure of Rossmann's character-enumeration problem under coning.

The originality comparison found no equivalent cone recurrence or \(K_{1,a,b}\) character formula in the inspected literature and published-result database. A differently phrased equivalent result could still exist, particularly in literature on bordered alternating matrix spaces.

## References

1. Tobias Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” *Bulletin of the London Mathematical Society* 54 (2022), 1923–1943, DOI 10.1112/blms.12665; first public version arXiv:2107.05564, 12 July 2021.
2. “All-characteristic character rank formula for graphical groups,” published scientific record, identifier `a74f4be4d9c8`.
3. Tobias Rossmann and Christopher Voll, “Ask zeta functions of joins of graphs,” arXiv:2505.10263, first public version 15 May 2025.
