# A single missing edge makes unequal biclique resistance metrics non-Euclidean

## Finding

Let \(m,n\ge 2\) be integers. Remove one edge from the complete bipartite graph \(K_{m,n}\), give every remaining edge unit electrical resistance, and let \(R\) be the effective-resistance distance on all \(m+n\) vertices. Then

\[
\boxed{R\text{ is isometrically Euclidean if and only if }m=n.}
\]

More precisely, let \(G_R=-\frac12 J(R_{uv}^{\,2})_{u,v}J\), where \(J=I-(m+n)^{-1}\mathbf 1\mathbf 1^{\mathsf T}\). Here the square is entrywise, *not* a matrix square. The inertia of \(G_R\), ordered as (positive, zero, negative), is exactly

\[
\operatorname{In}(G_R)=
\begin{cases}
(1,3,0),&m=n=2,\\
(m+n-1,1,0),&m=n\ge3,\\
(m+n-2,1,1),&m\ne n.
\end{cases}
\]

Thus in the balanced nonexceptional case the minimum Euclidean embedding dimension is \(m+n-1\); for \(m=n=2\) it is \(1\). Every unequal case has **exactly one** negative centered squared-resistance eigenvalue.

Write \(\wp(R)\) for the supremal \(p\)-negative-type exponent of the resistance metric. A consequence is the complete qualitative phase separation

\[
\wp(R)\begin{cases}
>2,&m=n\ge3,\\
=2,&m=n=2,\\
\in(1,2),&m\ne n.
\end{cases}
\]

No exact formula for \(\wp(R)\) in the nonexceptional cases is asserted.

## Assumptions and scope

The graph is unweighted, connected, finite and simple, with parts of sizes \(m,n\ge2\) and exactly one deleted cross-edge. Every retained edge has conductance \(1\) (equivalently resistance \(1\)). Distances are effective resistances, not shortest-path distances or their square roots. The term **Euclidean** means that there are vectors \(x_v\) in a real Hilbert space with \(R(u,v)=\lVert x_u-x_v\rVert\) for every vertex pair.

For a finite metric \(d\), \(p\)-negative type means \(\sum_{u,v}\alpha_u\alpha_v d(u,v)^p\le0\) whenever \(\sum_u\alpha_u=0\). Strictness requires strict inequality for every nonzero such vector. Schoenberg's criterion identifies Euclidean embeddability with \(2\)-negative type, and the rank of the centered Gram matrix is the smallest embedding dimension.

## Proof

**1. Independent resistance parametrization.** Name the endpoints of the missing edge \(a_*\) and \(b_*\). Group the remaining vertices as \(A'=A\setminus\{a_*\}\) and \(B'=B\setminus\{b_*\}\). In the four-group order \((\{a_*\},A',\{b_*\},B')\), set

\[
(w_1,w_2,w_3,w_4)=(1,m-1,1,n-1),\quad
(v_1,v_2,v_3,v_4)=(m,0,1-n,1),\quad
K=mn(m-1)(n-1).
\]

In the original \(K_{m,n}\), effective resistance is \(2/n\) within \(A\), \(2/m\) within \(B\), and \(\rho=(m+n-1)/(mn)\) between the parts. Let \(L_0^+\) be its Laplacian pseudoinverse on the zero-sum subspace and \(b=e_{a_*}-e_{b_*}\). Edge deletion replaces \(L_0\) by \(L_0-bb^{\mathsf T}\). Since \(b^{\mathsf T}L_0^+b=\rho<1\), the rank-one inverse update gives

\[
R(u,v)=R_0(u,v)+
\frac{((e_u-e_v)^{\mathsf T}L_0^+b)^2}{1-\rho}.
\]

Here the voltage differences are \((v_i-v_j)/(mn)\) for vertices in groups \(i,j\), and \(1-\rho=(m-1)(n-1)/(mn)\). Therefore for distinct vertices in groups \(i,j\),

\[
\boxed{R(u,v)=R_0(u,v)+\frac{(v_i-v_j)^2}{K}.}
\]

This formula includes pairs in the same group; their correction vanishes. It can be checked directly by grounding any vertex and inverting the reduced Laplacian.

**2. Reduction of the powered-distance form.** Set \(D=(R(u,v)^2)_{u,v}\). The quadratic form relevant to Euclidean geometry is \(-\frac12\alpha^{\mathsf T}D\alpha\) on the hyperplane \(\sum_v\alpha_v=0\). It decomposes as a direct sum of the two within-group mean-zero sectors of dimensions \(m-2\) and \(n-2\), each strictly positive, and a three-dimensional four-group-constant sector. On the two internal sectors the form has positive eigenvalues \(2/n^2\) and \(2/m^2\), respectively.

To describe the remaining sector, use **total coefficient mass per group** rather than a common per-vertex coefficient. For distinct groups let \(r_{ij}\) be the resistance in step 1. Set

\[
M_{ij}=r_{ij}^2\quad(i\ne j),\qquad
M_{ii}=\left(1-\frac1{w_i}\right)\delta_i^2,
\quad (\delta_1,\delta_2,\delta_3,\delta_4)
=(2/n,2/n,2/m,2/m).
\]

The diagonal formula counts ordered *distinct* vertex pairs in one group. A coordinate basis of the zero-sum group-mass space is given by the columns of

\[
U=\begin{pmatrix}1&0&1\\-1&0&0\\0&1&-1\\0&-1&0\end{pmatrix},
\qquad H=-\tfrac12 U^{\mathsf T}MU.
\]

The full centered Gram matrix has the same positive/zero/negative counts as the direct sum of the two positive internal sectors and \(H\), except for the one additional centered constant zero.

**3. Exact three-dimensional inertia certificate.** Direct rational simplification gives

\[
H_{11}=
\frac{m\bigl((m-1)(2n^2-1)+1\bigr)}
{n^2(m-1)^2(n-1)^2}>0.
\]

Put \(x=m-2\), \(y=n-2\), \(s=x+y\), \(z=xy\), and

\[
\begin{aligned}
P(s,z)={}&6s^4+29s^3z+36s^3+33s^2z^2+154s^2z+72s^2\\
&+14sz^3+125sz^2+265sz+48s+2z^4+28z^3+116z^2+146z.
\end{aligned}
\]

For \(H_{[1,2]}\), the leading two-by-two principal submatrix,

\[
\det H_{[1,2]}=
\frac{2P(s,z)}{m^2n^2(m-1)^4(n-1)^4}.
\]

Every coefficient of \(P\) is nonnegative; \(P>0\) when \(m,n\ge2\) and \((m,n)\ne(2,2)\). For the full three-by-three matrix put

\[
A=m^2(m-n)+(n-2)(m+1),\qquad
B=n^2(m-n)-(m-2)(n+1).
\]

Then

\[
\boxed{\det H=-\frac{4AB}{m^2n^2(m-1)^4(n-1)^4}.}
\]

These determinant identities are finite polynomial identities, obtained by substitution from the explicitly defined \(M,U\). They are also checked at exact rational samples by the included verifier.

When \(m=n=q\ge3\), \(A=(q-2)(q+1)>0\) and \(B=-A\), so all three leading principal minors of \(H\) are positive. Sylvester's criterion makes \(H\) positive definite.

When \(m>n\), let \(h=m-n\ge1\). Then \(A>0\) and

\[
B=h(n^2-n-1)-(n-2)(n+1)\ge1.
\]

When \(m<n\), let \(h=n-m\ge1\). Then \(B<0\) and

\[
A=-h(m^2-m-1)+(m-2)(m+1)\le-1.
\]

Thus \(AB>0\) whenever the sizes differ, so \(\det H<0\). Together with the strictly positive leading two-by-two block, this gives **exactly one negative eigenvalue** and two positive eigenvalues. The internal sectors remain positive. When \(m=n=2\), the graph is a four-vertex path and resistance equals ordinary unit path distance; the metric is collinear and its squared-distance centered Gram has rank one. This proves the stated inertia and Euclidean criterion.

**4. Exponent phase separation.** On any connected electrical network, \(\sum\alpha_v=0\) implies

\[
\sum_{u,v}\alpha_u\alpha_v R(u,v)
=-2\alpha^{\mathsf T}L^+\alpha<0
\quad\text{for }\alpha\ne0,
\]

so the resistance metric has strict \(1\)-negative type. On a *finite* metric, strict \(p\)-negative type persists for exponents in a sufficiently small interval above \(p\). Hence the unequal cases have \(\wp(R)>1\) but \(\wp(R)<2\) because the \(2\)-negative-type condition fails, while the balanced cases \(q\ge3\) have \(\wp(R)>2\). For \(q=2\), the path contains three collinear successive vertices at distances \(1,1,2\); the coefficient vector \((1,-2,1)\) violates \(p\)-negative type for every \(p>2\), whereas the line has \(2\)-negative type. Thus \(\wp(R)=2\).

## Verification

Run `python verify_missing_edge_resistance.py` using Python 3, SymPy and NumPy. Its construction does not call a graph-resistance package: it independently grounds the last vertex, exactly inverts the remaining graph Laplacian and reconstructs all resistances. It checks the four-class rank-one formula, the two determinant identities and the entire centered Gram inertia for every integer \(2\le m,n\le6\). Its last line is `ALL_DELETED_BICLIQUE_RESISTANCE_CHECKS_OK`. The all-orders inequalities in the proof, rather than this finite test range, establish the theorem.

## Relationship to prior work

Sánchez (2011, arXiv:1108.0451), especially Theorem 3.1, computes generalized roundness for complete bipartite graphs using *shortest-path* metrics. Its statement does not cover effective-resistance metrics or removal of an edge. Ge and Dong (2019, arXiv:1904.07766), especially Theorem 5.7 and Section 5.3, give full effective-resistance formulas for \(K_{m,n}\) minus a matching, including a single deleted edge, and compute related Kirchhoff indices. Those prior resistance formulas supply an alternative input to the present calculations, but the inspected theorem and applications do not evaluate the *squares* of those resistances under Schoenberg's zero-sum test, classify their Euclidean embeddings, or identify the one-negative-eigenvalue obstruction. Gervacio (2016) studies exact resistance values for complete multipartite graphs (not, generally, the present missing-edge graphs). The distinction is **not** claimed to establish priority against every unindexed result.

## Limitations

The classification assumes one missing edge and equal unit conductances on the remaining edges; it does not address multiple-edge deletions, arbitrary edge weights or nonbipartite graphs. The signs and Euclidean ranks are exact, but the supremal negative-type exponents away from the four-vertex path are bounded qualitatively and not evaluated numerically. An independent scientific review has not been performed. An equivalent unindexed criterion remains a possible originality risk.

## References

- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, publicly posted 2011-08-02; especially Definitions 1.1 and Theorem 3.1. https://arxiv.org/abs/1108.0451
- J. Ge and F. Dong, *Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs*, arXiv:1904.07766, 2019-04-16; especially Theorem 5.7. https://arxiv.org/abs/1904.07766
- S. V. Gervacio, *Resistance distance in complete n-partite graphs*, Discrete Applied Mathematics 203 (2016), 53–61, DOI:10.1016/j.dam.2015.09.017. Published online 2015/2016; exact first public date not used for the time classification.
