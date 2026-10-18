# Exact projection constant of the higher-codimension five-coordinate obstruction family

## Finding

For every integer \(n\ge3\), the real \(n\)-dimensional example \(W_n\subset\ell_\infty^{2n}\) defined below has exact projection constant

\[
\lambda(W_n,\ell_\infty^{2n})=\lambda(W_n)=\frac{845}{659}.
\]

The value improves the explicit bound \(13/10\) in Proposition 3.4 of Deręgowska--Lewandowska (2026) by precisely \(117/6590\). More importantly, this is the sharp threshold: no projection onto these example subspaces has smaller norm. The real statement is uniform in \(n\), without an asymptotic limiting argument.

## Assumptions and scope

Work over the **real** scalar field. Endow \(\mathbb R^m\) with the maximum-coordinate norm \(\|x\|_\infty=\max_i|x_i|\). Define

\[
 u=(1,\tfrac45,\tfrac14,-\tfrac14,-\tfrac45),\qquad
 v=(0,\tfrac35,1,1,\tfrac35),\qquad
 V=\operatorname{span}_{\mathbb R}\{u,v\}\subset\ell_\infty^5.
\]

For \(n\ge3\), define

\[
W_n=\big\{(x_1,\ldots,x_5,s,t_1,t_1,\ldots,t_{n-3},t_{n-3}): (x_1,\ldots,x_5)\in V,\ s,t_j\in\mathbb R\big\}.
\]

The repeated-pair string is absent when \(n=3\). Thus \(W_n\subset\ell_\infty^{2n}\) has dimension \(2+1+(n-3)=n\). For a subspace \(Y\subset X\), write \(\lambda(Y,X)=\inf\{\|P\|:P:X\to Y,\ P|_Y=I_Y\}\). As the finite-dimensional coordinate supremum space is injective, the absolute projection constant equals this relative constant for the displayed embedding.

## Proof

**Step 1: an explicit projection attaining \(845/659\).** Set the coordinate functionals \(a,b\in(\mathbb R^5)^*\) by

\[
 a=\frac1{1318}(1040,105,220,-220,-105),\qquad
 b=\frac1{1318}(0,140,575,575,140).
\]

Direct rational evaluation gives \(a(u)=1\), \(a(v)=0\), \(b(u)=0\), \(b(v)=1\). Hence

\[
 Qx=a(x)u+b(x)v
\]

is a projection from \(\ell_\infty^5\) onto \(V\). For each of the five rows of its matrix, the sum of absolute entries is exactly \(845/659\). Consequently, \(\|Q\|_{\infty\to\infty}=845/659\).

**Step 2: a universal dual lower-bound certificate.** Let

\[
 \rho=\frac1{1318}(208,315,240,240,315),
\]

so that its coordinates are nonnegative and sum to one. Let \(\Sigma=(\sigma_{ij})_{1\le i,j\le5}\) be

\[
\Sigma=\begin{pmatrix}
 1&1&1&-1&-1\\
 1&1&1&1&-257/315\\
 1&1&1&1&1\\
 -1&1&1&1&1\\
 -1&-257/315&1&1&1
\end{pmatrix}.
\]

Every entry of \(\Sigma\) lies in \([-1,1]\). Straight rational arithmetic verifies, separately for each column \(j\),

\[
\sum_{i=1}^{5}\rho_i\sigma_{ij}u_i=\frac{416}{659}u_j,\qquad
\sum_{i=1}^{5}\rho_i\sigma_{ij}v_i=\frac{429}{659}v_j.
\]

Now take an **arbitrary** real projection \(R:\ell_\infty^5\to V\). Since \(u,v\) form a basis of its range, it has the form \(Rx=\alpha(x)u+\beta(x)v\) for coordinate functionals \(\alpha,\beta\) satisfying \(\alpha(u)=\beta(v)=1\), \(\alpha(v)=\beta(u)=0\). Writing \(R_{ij}=u_i\alpha_j+v_i\beta_j\), the two displayed dual identities imply

\[
\begin{aligned}
\|R\|_{\infty\to\infty}
&=\max_i\sum_j|R_{ij}|
\ge\sum_i\rho_i\sum_j\sigma_{ij}R_{ij}\\
&=\frac{416}{659}\alpha(u)+\frac{429}{659}\beta(v)
=\frac{845}{659}.
\end{aligned}
\]

The first inequality uses only \(\rho_i\ge0\), \(\sum_i\rho_i=1\), and \(|\sigma_{ij}|\le1\). Together with Step 1 this proves the exact constant for \(V\); no numerical optimization premise remains.

**Step 3: all higher-dimensional examples.** Let \(n\ge3\), and let \(P:\ell_\infty^{2n}\to W_n\) be any projection. Embed \(\ell_\infty^5\) as the first five coordinates and restrict the first five output coordinates of \(P\). Because \(W_n\) contains every vector \((x,0,\ldots,0)\) with \(x\in V\), this compression is a projection \(\ell_\infty^5\to V\). Its norm is at most \(\|P\|\), so \(\|P\|\ge845/659\).

Conversely, on the decomposition into a five-coordinate block, the sixth coordinate, and \(n-3\) two-coordinate blocks, use \(Q\), the identity, and \((r,s)\mapsto((r+s)/2,(r+s)/2)\), respectively. This block-diagonal map is a projection onto \(W_n\). Every block after the first has norm one, hence the complete norm is \(845/659\). The lower and upper bounds coincide for every stated \(n\).

## Verification

The accompanying self-contained `check_exact.py` performs all computations over \(\mathbb Q\) using Python's standard-library `fractions.Fraction`. It checks the biorthogonality conditions, the five exact absolute row sums of \(Q\), the nonnegative unit-mass weights and entry bounds of \(\Sigma\), and all ten identities involving the two dual vectors and five columns. It then tests the scalar \(13/10-845/659=117/6590>0\). The printed certificate is determined by exact rational arithmetic. The universal conclusion is proved in Steps 2--3, rather than inferred from finite tests.

## Relationship to prior work

The source is B. Deręgowska and B. Lewandowska, *Projection Constants and Banach-Mazur Distance in Codimension Two* (arXiv:2610.06141v1, publicly posted October 5, 2026), §3, Propositions 3.2--3.4. They introduce the coordinate obstruction family \(W_n\) to show failure of a proposed higher-codimension disjoint-good-sets geometric lemma. Their Proposition 3.4 constructs a projection onto every \(W_n\) of norm \(13/10\); it neither states an infimum nor gives a lower-bound certificate matching the construction. The present result supplies the exact optimal projection norm of that **same** family, with a short explicit weighted-sign dual certificate.

Classical general principles concerning minimal projections and finite-dimensional linear programming can formulate this minimization, but the derived rational optimum and specific dual inequality are additional evaluated information for this source's canonical geometric obstruction. We make no claim to solve the source's general conjecture on Banach--Mazur distances in arbitrary codimension.

## Limitations

This theorem is restricted to the displayed real-coordinate subspaces; it does not assert the same sharp value over the complex scalar field, classify all minimizing projections, or determine the sharp Banach--Mazur distance of \(W_n\). Publication priority for an equivalent but differently formulated old minimal-projection calculation cannot be excluded solely by the available literature search. The proof and exact certificate are fully self-contained once the space is defined.

## References

B. Deręgowska and B. Lewandowska, *Projection Constants and Banach-Mazur Distance in Codimension Two*, arXiv:2610.06141v1 (October 5, 2026), https://arxiv.org/abs/2610.06141, especially Propositions 3.2--3.4.

A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Minimal projections onto spaces of polynomials on real Euclidean spheres*, J. London Math. Soc. 113 (2026), e70429, doi:10.1112/jlms.70429 (different family of ranges).
