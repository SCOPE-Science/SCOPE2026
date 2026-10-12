# Principal finite-type loci of richly branching R-trees are exact metric cubes

## Finding

Let \(T=\mathrm{rbRT}_r\) be Carlisle and Henson's complete continuous theory of richly branching pointed \(\mathbb R\)-trees of radius \(r>0\). For \(n\ge 1\), let
\[
P_n=\{q\in S_n(T):q\text{ is principal}\}.
\]
The paper uses “principal” for what is now usually called “isolated.”

For \(\mathbf t=(t_1,\ldots,t_n)\in[0,r]^n\), put \(q_{\mathbf t}\) for the type of a tuple \((a_1,\ldots,a_n)\) lying on one geodesic segment from the distinguished point \(p\), with
\[
d(p,a_i)=t_i\qquad(1\le i\le n).
\]
Then radial coordinates give an exact isometry
\[
\boxed{([0,r]^n,\|\cdot\|_\infty)\ \cong\ (P_n,d)}.
\]
In particular, every principal finite type is determined uniquely by its ordered list of radial distances, and the metric between two principal types is
\[
\boxed{d(q_{\mathbf t},q_{\mathbf s})=\max_{1\le i\le n}|t_i-s_i|.}
\]
Thus the principal locus is a compact separable metric cube in every arity.

The same ingredients also give the exact finite-arity density spectrum
\[
\boxed{\operatorname{dens}S_1(T)=\aleph_0,\qquad
\operatorname{dens}S_n(T)=2^{\aleph_0}\ \text{for every }n\ge2.}
\]
Since \(P_n\) is compact and hence closed, the nonprincipal subspace \(S_n(T)\setminus P_n\) itself has metric density \(2^{\aleph_0}\) for every \(n\ge2\). Hence arity \(2\) is the exact point at which nonseparability appears, and it appears entirely outside the separable principal cube.

## Assumptions and scope

The statement concerns types over the empty set in the theory \(\mathrm{rbRT}_r\) for a fixed real radius \(r>0\), with the standard metric on continuous-logic type spaces. Repeated coordinates are allowed, so points on the boundary and diagonals of \([0,r]^n\) are included.

No description is claimed for the metric on all of \(S_n(T)\) when \(n>1\). Carlisle and Henson explicitly remark that such a precise general description seems very complex. The result isolates the distinguished principal subspace, on which the metric becomes completely explicit.

## Proof

Carlisle and Henson prove quantifier elimination and show that an \(n\)-type over the empty set is determined by the resulting finite tree pseudometric. Their Theorem 11.4 characterizes a type as principal exactly when every realization, after a suitable permutation of the coordinates, lies on a single piecewise segment with \(p\) as an endpoint.

Take a principal type \(q\) and a realization \(\mathbf a=(a_1,\ldots,a_n)\). Set
\[
t_i=d(p,a_i).
\]
Because all coordinates lie on one geodesic segment issuing from \(p\),
\[
d(a_i,a_j)=|t_i-t_j|.
\]
Quantifier elimination and the pseudometric description of types therefore show that \(q\) is exactly \(q_{\mathbf t}\). Conversely, any \(\mathbf t\in[0,r]^n\) can be realized by taking the indicated points on one geodesic segment of length \(r\), and Theorem 11.4 makes the resulting type principal. This proves that \(\mathbf t\mapsto q_{\mathbf t}\) is a bijection from \([0,r]^n\) onto \(P_n\).

For the metric, let \(\mathbf t,\mathbf s\in[0,r]^n\). For arbitrary realizations \(\mathbf a\models q_{\mathbf t}\) and \(\mathbf b\models q_{\mathbf s}\), the triangle inequality gives, coordinatewise,
\[
d(a_i,b_i)\ge |d(p,a_i)-d(p,b_i)|=|t_i-s_i|.
\]
Hence the definition of the type metric yields
\[
d(q_{\mathbf t},q_{\mathbf s})\ge \|\mathbf t-\mathbf s\|_\infty.
\]
For the reverse inequality, realize both tuples simultaneously on the same geodesic segment from \(p\). Then
\[
d(a_i,b_i)=|t_i-s_i|
\]
for every coordinate, so
\[
d(q_{\mathbf t},q_{\mathbf s})\le \|\mathbf t-\mathbf s\|_\infty.
\]
This proves the isometry.

Carlisle and Henson's Lemma 8.7 gives \(S_1(T)\cong[0,r]\), so its metric density is \(\aleph_0\). Their Proposition 8.8 proves
\[
\operatorname{dens}S_2(T)=2^{\aleph_0}.
\]
For each \(n\ge2\), repeat the second coordinate to obtain
\[
S_2(T)\longrightarrow S_n(T),\qquad
q(x_1,x_2)\longmapsto q'(x_1,x_2,x_2,\ldots,x_2).
\]
Projection back to the first two coordinates shows that this is an isometric embedding. Thus \(\operatorname{dens}S_n(T)\ge2^{\aleph_0}\). By the source's finite-pseudometric description, an \(n\)-type over the empty set is determined by finitely many real distances, so \(S_n(T)\) has cardinality at most \(2^{\aleph_0}\). Hence equality follows.

Finally, \(P_n\) is isometric to the compact cube \([0,r]^n\), hence is closed and separable. If the complement had density strictly below \(2^{\aleph_0}\), adjoining a countable dense subset of \(P_n\) would give a dense subset of all of \(S_n(T)\) of density strictly below \(2^{\aleph_0}\), contradicting the preceding equality. Therefore the complement has density \(2^{\aleph_0}\) when \(n\ge2\).

## Verification

An exact-arithmetic replay checks the finite metric identities behind the proof on rational grids. It verifies that radial coordinates induce the tree pseudometric \(d(a_i,a_j)=|t_i-t_j|\), that the piecewise-segment length telescopes correctly after sorting the radii, that simultaneous same-ray realization attains the \(\ell_\infty\) distance, and that coordinate repetition preserves the relevant maximum metric. The bundled checker returns

`VERIFY_OK 3366437 exact assertions`.

The computation is only a replay of finite identities. The all-arity theorem is established by the symbolic argument above together with the cited model-theoretic results.

## Relationship to prior work

Carlisle and Henson already provide all structural ingredients: quantifier elimination; the isometry \(S_1(T)\cong[0,r]\); continuum metric density of \(S_2(T)\); and the qualitative characterization of principal finite types as tuples lying on one piecewise segment from \(p\). They also state that a precise metric description of \(S_n(A)\) for \(n>1\) seems very complex.

The additional statement here is the exact metric geometry of the entire principal locus in every finite arity, together with the resulting complete finite-arity density spectrum and the observation that the nonprincipal locus already carries all of the continuum-density obstruction from arity \(2\) onward.

Targeted searches for formulations combining richly branching \(\mathbb R\)-trees, principal or isolated types, metric cubes, and higher-arity type metrics located the source characterization but not this cube-isometry statement or the full density-spectrum formulation. Broader searches in continuous model theory likewise located later work adapting \(\mathbb R\)-tree methods, but no equivalent theorem. Because the deduction from the source ingredients is short, an uncatalogued folklore observation remains possible.

## Limitations

The result does not simplify the full metric on \(S_n(T)\) for \(n>1\); it identifies only the principal subspace. It is also specific to types over \(\varnothing\); over parameters, principal-type geometry can interact with the convex subtree generated by the parameter set.

The originality assessment is literature-search based and cannot rule out unpublished notes or seminar folklore. The finite checker validates only the elementary metric identities on finite rational grids and is not a substitute for the model-theoretic proof.

## References

Sylvia Carlisle and C. Ward Henson, *Model theory of R-trees*, arXiv:1810.00242, first public version 2018-09-29; *Journal of Logic & Analysis* 12:3 (2020), 1–51, DOI 10.4115/jla.2020.12.3. Relevant results are Lemma 8.7, Proposition 8.8, the pseudometric description following Lemma 8.7, and Theorem 11.4.
