# Joint principal-ideal dimension spectrum of radical-square-zero quiver algebras

## Finding
Let \(Q=(V,E)\) be any finite quiver with \(n=|V|\ge 1\) vertices and \(m=|E|\) arrows, including loops and parallel arrows. For every prime power \(q\), put \(A=\mathbb F_qQ/J^2\), where \(J\) is the arrow ideal. Define the generator-weighted principal-ideal dimension polynomial
\[
P_Q^{(q)}(X,Y)=\sum_{x\in A}X^{\dim_{\mathbb F_q}(xA)}Y^{\dim_{\mathbb F_q}(Ax)}.
\]
For a vertex \(v\), let \(d^+(v)\) and \(d^-(v)\) be its outgoing and incoming arrow counts, with multiplicity. For \(S\subseteq V\), let \(E[S]=\{a\in E:s(a),t(a)\in S\}\), and for \(F\subseteq E\) let \(T(F)=\{t(a):a\in F\}\), \(U(F)=\{s(a):a\in F\}\). Then the entire joint distribution is
\[
\boxed{P_Q^{(q)}(X,Y)=\sum_{S\subseteq V}(q-1)^{n-|S|}q^{m-|E[S]|}
 X^{\sum_{v\notin S}(1+d^+(v))}
 Y^{\sum_{v\notin S}(1+d^-(v))}
 \sum_{F\subseteq E[S]}(q-1)^{|F|}X^{|T(F)|}Y^{|U(F)|}.}
\]
The formula is valid in every characteristic, without acyclicity, connectedness, or simplicity assumptions. It counts algebra elements as generators; it does **not** count distinct one-sided ideals.

For the three orientations of the underlying three-vertex path, the number of elements generating a one-dimensional right ideal is, respectively,
\[
\begin{array}{c|c}
\text{orientation}&\#\{x:\dim(xA)=1\}\\\hline
1\to2,\ 1\to3&2(q-1)(q+1)\\
2\to1,\ 3\to1&(q-1)(q^2+q+1)\\
1\to2\to3&(q-1)(q+2)
\end{array}
\]
and these counts are pairwise distinct for all prime powers \(q\ge2\). Thus the one-sided generator-rank spectrum distinguishes the three possible path orientations, even though the pairwise-commuting tuple equations of the square-zero quiver algebras are invariant under edge reversal.

## Assumptions and scope
Paths of length two are set to zero. The algebra has basis \(\{e_v:v\in V\}\sqcup\{a:a\in E\}\); the vertex idempotents are orthogonal, \(e_{s(a)}a=a=ae_{t(a)}\), and products of two arrows vanish. A loop counts once as both an incoming and an outgoing arrow. Polynomial exponents are ordinary vector-space dimensions and hence nonnegative integers. The source and target sets in the formula disregard multiplicities but the edge subsets and vertex degrees preserve them. No assumption on the characteristic is made. The zero algebra from an empty vertex set is excluded only to avoid degenerate notation.

## Proof
Write an arbitrary element uniquely as \(x=\sum_{v\in V}\lambda_ve_v+\sum_{a\in E}\mu_aa\). The precise multiplication equations, for each vertex \(v\) and arrow \(a\), are
\[
 xe_v=\lambda_ve_v+\sum_{t(a)=v}\mu_aa,\qquad xa=\lambda_{s(a)}a;
\quad e_vx=\lambda_ve_v+\sum_{s(a)=v}\mu_aa,\qquad ax=\lambda_{t(a)}a.
\]
Fix the zero-scalar vertex set \(S=\{v:\lambda_v=0\}\), and let \(F=\{a\in E[S]:\mu_a\ne0\}\). To compute \(\dim(xA)=\operatorname{rank}(L_x)\), first take the image of every arrow basis vector. Those columns span exactly the arrow-coordinate vectors with sources outside \(S\), a subspace of dimension \(\sum_{v\notin S}d^+(v)\). Next, for each \(v\notin S\), the column \(xe_v\) has nonzero \(e_v\)-coordinate, so these columns contribute precisely \(n-|S|\) further independent dimensions. Modulo their span and that of the arrow images, the remaining vertex columns are supported on internal arrows \(E[S]\). For \(v\in S\), the residual column is \(\sum_{a\in E[S],\ t(a)=v}\mu_aa\); it is nonzero exactly when \(v\in T(F)\). Distinct targets have disjoint arrow-coordinate supports, hence these residual columns are linearly independent. Therefore
\[
\dim(xA)=\sum_{v\notin S}(1+d^+(v))+|T(F)|.
\]
Repeating the argument with right multiplication, whose arrow images have targets outside \(S\), gives
\[
\dim(Ax)=\sum_{v\notin S}(1+d^-(v))+|U(F)|.
\]
For fixed \(S,F\), the nonzero vertex scalars can be chosen in \((q-1)^{n-|S|}\) ways; each internal supported arrow coefficient has \(q-1\) choices, each unsupported internal coefficient is zero, and all \(m-|E[S]|\) external arrow coefficients are unrestricted. The stratum has exactly \((q-1)^{n-|S|}(q-1)^{|F|}q^{m-|E[S]|}\) elements. Summing these disjoint strata gives the boxed bivariate formula, proving all coefficients without reliance on finite experiments.

For the three path orientations substitute \(n=3\) and the respective two-arrow sets in the formula, then take the coefficient of \(X^1\) after setting \(Y=1\). The displayed expressions follow directly. Dividing by \(q-1>0\), their factors are \(2q+2\), \(q^2+q+1\), and \(q+2\), strictly ordered as \(q^2+q+1>2q+2>q+2\) for every integer \(q\ge2\). This proves the orientation distinction for every finite field.

The contrast with commuting tuples is not a new claim about those tuples: for \(x=\sum\lambda_ve_v+\sum\mu_aa\) and \(y=\sum\eta_ve_v+\sum\nu_aa\), the arrow coefficient in their commutator is
\[
[x,y]_a=(\lambda_{s(a)}-\lambda_{t(a)})\nu_a-(\eta_{s(a)}-\eta_{t(a)})\mu_a.
\]
Reversing an arrow multiplies this defining polynomial by \(-1\) after matching the arrow coordinates. Thus the pairwise-commuting tuple equations are unchanged by reversing any collection of arrows; our principal-ideal spectra are not.

## Verification
The accompanying standalone \(`verify_principal_ideal_ranks.py`\) independently constructs the left- and right-multiplication matrices from the basis product table and computes their ranks by Gaussian elimination. It compares their complete bivariate count with an independently enumerated vertex-zero/arrow-support sum for 56 finite-field/quiver configurations over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), including loops, parallel arrows, oriented cycles, isolated vertices, and connected/disconnected quivers. The script prints \(`VERIFY_OK_PRINCIPAL_RANK_BIVARIATE`\) on success. The path-orientation rank-one coefficients are also checked directly. The proof covers all finite quivers and finite fields; the finite tests are corroboration only.

## Relationship to prior work
The algebras \(kQ/J^2\) and their left/right module structures are standard objects; earlier work examines homological dimensions, singular equivalences, and conjugacy classes of one-sided ideals. Elia--Gorla (2014) express dimensions of principal one-sided ideals of **group algebras** through regular-representation matrix ranks and give an algorithm for individual generators, a different algebra family and question. In particular, Lanzilotta--Marcos--Mata analyze Igusa--Todorov functions (2015), Nasr-Isfahani studies quiver operations preserving singular equivalence (2016), and Męcel classifies when the semigroup of conjugacy classes of left ideals is finite (2016). These results are not presented as new. The distinct invariant assessed here is the **element-weighted, two-variable complete distribution** of the dimensions of \(xA\) and \(Ax\), with an exact formula for every quiver and finite field. Previously established orientation-invariance of commuting-tuple equations and adjoint-rank formulas concerns commutators, not the two one-sided image ranks; indeed the three path orientations have the same commuting equations yet different coefficients here. No priority claim is based solely on a failed search.

## Limitations
The theorem applies to radical-square-zero basic path algebras over finite fields. It does not determine the number of *distinct* principal ideals, nor does it cover algebras with nonzero length-two paths, nonsplit vertex division rings, or the distribution of isomorphism types of principal ideal modules. The connectedness and representation type of the quiver are irrelevant to the asserted formula. An equivalent older enumeration under principal-ideal or matrix-support terminology cannot be ruled out by the available source comparisons; independent mathematical and historical validation has not been performed.

## References
1. M. Elia, E. Gorla, *Computing the dimension of ideals in group algebras, with an application to coding theory*, arXiv:1403.7920v1, first posted 31 March 2014. https://arxiv.org/abs/1403.7920
2. M. Lanzilotta, E. N. Marcos, G. Mata, *Igusa-Todorov functions for radical square zero algebras*, arXiv:1506.05894v1, first posted 19 June 2015. https://arxiv.org/abs/1506.05894
3. A. Nasr-Isfahani, *Singular equivalence of finite dimensional algebras with radical square zero*, arXiv:1603.04191v1, first posted 14 March 2016. https://arxiv.org/abs/1603.04191
4. A. Męcel, *On the finiteness of the semigroup of conjugacy classes of left ideals for algebras with radical square zero*, Colloquium Mathematicum **142** (2016), 1--49, DOI:10.4064/cm142-1-1. https://doi.org/10.4064/cm142-1-1
