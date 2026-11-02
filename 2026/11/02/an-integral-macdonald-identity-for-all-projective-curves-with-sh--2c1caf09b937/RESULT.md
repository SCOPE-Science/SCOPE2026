# An integral Macdonald identity for all projective curves, with sharp branch-corrected vanishing

## Finding

Let \(X\) be any projective scheme of dimension at most one over \(\mathbb C\), without hypotheses of reducedness, irreducibility, connectedness or equidimensionality. Write \(S^nX\) for its \(n\)-th symmetric power, \(\mathbf e(Y)=c_{SM}(Y)_0\in CH_0(Y)\), and \(SX=\coprod_{n\ge0}S^nX\). Give \(\prod_{n\ge0}CH_0(S^nX)t^n\) the completed multiplication induced by addition of effective cycles, and let \(\exp\) denote the integral zero-cycle exponential. Then **integrally, without inverting any factorial**, for every \(n\ge0\),

\[
\mathcal E_X(t):=\sum_{n\ge0}\mathbf e(S^nX)t^n=\exp(\mathbf e(X)).\tag{1}
\]

For reduced pure one-dimensional \(X\), let \(\nu:N=\coprod_{i=1}^s C_i\to X\) be its normalization, let \(\Sigma\subset X\) be its finite nonnormal locus and \(b_p=|\nu^{-1}(p)|\) the number of geometric normalization branches at \(p\). Every \(C_i\) is smooth and projective. The stronger explicit branch formula is

\[
\mathcal E_X(t)=\left[\prod_{i=1}^{s}(S\nu_i)_*\mathcal E_{C_i}(t)\right]\prod_{p\in\Sigma}(1-[p]t)^{b_p-1}.\tag{2}
\]

Here every factor is interpreted in the same completed ring on \(SX\); \([p]t\) means the degree-one effective cycle at \(p\), not a scalar. If every normalization component has genus \(g_i\ge1\), then \(\mathcal E_X(t)\) is a polynomial of **exact degree**

\[
D=\sum_{i=1}^{s}(2g_i-2)+\sum_{p\in\Sigma}(b_p-1)=-\chi_{\mathrm{top}}(X).\tag{3}
\]

In particular, \(\mathbf e(S^nX)=0\in CH_0(S^nX)\) for every \(n>D\), while \(\mathbf e(S^DX)\ne0\) since its degree is \((-1)^D\). Thus two smooth elliptic curves glued along \(r\ge1\) distinct pairs of points have

\[
\mathcal E_X(t)=\prod_{j=1}^{r}(1-[p_j]t),\qquad \mathbf e(S^nX)=0\ \text{for }n>r,\quad \deg\mathbf e(S^rX)=(-1)^r.\tag{4}
\]

## Assumptions and scope

The base field is \(\mathbb C\); Chow groups are integral Fulton Chow groups. The degree-zero Chern–Schwartz–MacPherson class is defined using the constructible function \(\mathbf1_Y\), and for nonreduced schemes depends only on the reduced support. A normalization branch is a geometric point of the finite normalization fiber; a cusp has one branch. In formulas (2)–(4), \(X\) is reduced, pure dimensional one, with possibly disconnected components or component intersections. The symbol \(\chi_{\mathrm{top}}\) denotes the ordinary compact-topological Euler characteristic. In (4), the gluing points on each elliptic component are pairwise distinct, producing ordinary nodes; the resulting projective curve need not be irreducible.

## Proof

**1. Reduction and normalization.** Because the reduced subschemes of \(X\) and its symmetric powers have the same geometric points as the original schemes, and their nilpotent thickenings induce isomorphisms on ordinary Chow groups, it suffices to prove (1) for reduced \(X\). The reduced projective curve is a union of finitely many integral projective curves and possibly isolated points. Let \(\nu:N\to X\) be the disjoint union of the normalizations of the one-dimensional components and the isolated points. The map is finite, generically an isomorphism on each component. All fibers containing more than one geometric point occur over a finite set \(\Sigma\), and the number of points in the fiber over \(p\) is \(b_p\). The CSM pushforward applied to \(\mathbf1_N\) gives

\[
\mathbf e(X)=\nu_*\mathbf e(N)-\sum_{p\in\Sigma}(b_p-1)[p].\tag{5}
\]

This follows from \(\nu_*\mathbf1_N=\mathbf1_X+\sum_p(b_p-1)\mathbf1_{\{p\}}\), valid also for unibranch singular points (whose correction is zero).

**2. Disjoint unions.** For any disjoint union \(Y=Y_1\sqcup Y_2\), the degree-\(n\) symmetric power splits as the disjoint union \(\coprod_{a+b=n}S^aY_1\times S^bY_2\). The external-product identity for CSM classes implies \(\mathcal E_Y=\mathcal E_{Y_1}\mathcal E_{Y_2}\). For each smooth projective curve, \(\mathcal E_{C_i}=\exp(\mathbf e(C_i))\) integrally by the smooth-curve theorem of Fantechi–Göttsche. An isolated point has series \(1+[p]t+[2p]t^2+\cdots=\exp([p])\). Hence \(\mathcal E_N=\exp(\mathbf e(N))\) for every disconnected normalization described in step 1.

**3. A gluing lemma without an irreducibility hypothesis.** Suppose \(f:Y\to Z\) is the finite point-pushout that identifies two distinct reduced points \(q_1,q_2\in Y\) to one point \(p\in Z\), and is an isomorphism elsewhere; \(Y\) may be disconnected or reducible. For an effective cycle \(\xi\in S^nZ\) containing \(p\) with multiplicity \(m\), the geometric fiber of \(S^nf\) has exactly \(m+1\) points, corresponding to distributions of those \(m\) copies between \(q_1\) and \(q_2\). The fiber contribution of the composition \(S^{n-1}Y\to S^{n-1}Z\xrightarrow{\,+[p]\,}S^nZ\) is \(m\) when \(m\ge1\), and zero for \(m=0\). Consequently, for every \(n\ge1\),

\[
\mathbf1_{S^nZ}=(S^nf)_*\mathbf1_{S^nY}-(+[p])_*(S^{n-1}f)_*\mathbf1_{S^{n-1}Y}.\tag{6}
\]

Pushforward here means Euler-characteristic integration of constructible functions, not the degree of a potentially nonreduced scheme fiber. The CSM natural transformation commutes with proper pushforward. Applying its degree-zero part to (6), summing in \(n\), and using compatibility of the integral exponential with proper pushforward produces

\[
\mathcal E_Z=(Sf)_*\mathcal E_Y(1-[p]t).\tag{7}
\]

Since \(f_*\mathbf1_Y=\mathbf1_Z+\mathbf1_{\{p\}}\), we also have \(\mathbf e(Z)=f_*\mathbf e(Y)-[p]\). If \(\mathcal E_Y=\exp(\mathbf e(Y))\), then (7) becomes \(\mathcal E_Z=\exp(\mathbf e(Z))\). No step uses irreducibility or connectedness.

**4. Finite point-pinching and residual bijection.** The finite normalization map factors into (a) a finite sequence of simple point-gluings that identifies every set \(\nu^{-1}(p)\) over all \(p\in\Sigma\), followed by (b) a finite bijective morphism onto \(X\). Finite point-pinching exists for projective curves, including disconnected sources: locally one uses the subring of functions whose values agree at the chosen two closed points; globally this is the standard finite pushout construction. Once all fibers have been identified, the residual map is finite bijective. The proof in step 3 applies inductively. A finite bijective map over \(\mathbb C\) remains bijective on effective zero cycles; its constructible-function pushforward is the indicator function. Thus the CSM class and integral exponential commute with this map. This proves (1) for reduced curves and, by step 1, for any projective scheme of dimension at most one.

**5. The explicit formula.** Each identification of a fiber of size \(b_p\) requires exactly \(b_p-1\) point gluings. Iteration of (7) followed by the bijective pushforward gives (2), and applying (5) and exponential multiplicativity proves that (2) agrees with (1).

**6. Sharp vanishing.** For a genus-\(g_i\ge1\) smooth curve, a general regular differential has a reduced canonical zero divisor \(q_{i1}+\cdots+q_{i,2g_i-2}\), and the smooth-curve formula gives

\[
\mathcal E_{C_i}(t)=\prod_{j=1}^{2g_i-2}(1-[q_{ij}]t),\tag{8}
\]

with the empty product understood as \(1\) for an elliptic curve. Formula (2) is therefore a finite product of exactly \(D\) linear factors. Its top coefficient is \((-1)^D\) times the class of a single degree-\(D\) effective zero cycle on \(X\), so its degree is \((-1)^D\ne0\). The equality \(D=-\chi_{\mathrm{top}}(X)\) follows from the normalization Euler-characteristic relation \(\chi(X)=\sum_i(2-2g_i)-\sum_p(b_p-1)\). This proves (3). The elliptic example (4) is obtained by taking \(g_1=g_2=1\) and \(b_{p_j}=2\) at precisely \(r\) nodes.

## Verification

All equalities are integral statements in Chow groups, not merely equalities after degree or after inverting factorials. The critical numerical fiber count in (6) can be checked for any multiplicity \(m\): there are \(m+1\) nonnegative integer pairs summing to \(m\), while after placing one distinguished copy of \(p\) there are \(m\) pairs summing to \(m-1\). The difference is one, including \(m=0\). For the union of two elliptic curves meeting in \(r=1,2,3\) nodes, the predicted degree series are respectively \(1-t\), \((1-t)^2\), and \((1-t)^3\), consistent with the normalization Euler-characteristic computation. The infinite result follows from steps 1–6; these finite examples are illustrations, not an exhaustive proof.

## Relationship to prior work

Fantechi and Göttsche, *Chern-Schwartz-MacPherson classes of symmetric powers and applications*, arXiv:2610.31826v1 (2026-10-22), formulate the integral identity as Conjecture 4.26 and prove it for smooth projective curves (Theorem 5.2) and for complete **reduced irreducible** curves (the explicit definition preceding Proposition 5.6, then Theorem 5.13). The present result extends the same integral identity to the complete one-dimensional projective class, including reducible and nonreduced schemes, and records a branch formula and the sharp finite-support result in the absence of rational normalization components. Its gluing mechanism is adapted from their Propositions 5.9–5.12; it is not an independent proof of the smooth-curve base theorem. This is a deliberately bounded extension, not a solution of Conjecture 4.26 in higher dimension.

## Limitations

The base is \(\mathbb C\) (characteristic zero); no assertion is made for positive characteristic or for projective schemes of dimension at least two. The formula concerns the degree-zero component of CSM classes, not the full graded CSM class. The finite-degree vanishing (3) requires that each one-dimensional normalization component have positive genus and that \(X\) have no isolated zero-dimensional components; it is not asserted for rational components. The explicit formula uses geometric fibers of the normalization, not scheme-theoretic lengths or analytic singularity types. The literature overlap risk is that the irreducible-curve proof already supplies most of the point-gluing ideas, making the extension potentially implicit in the cited source. Mathematical priority and independent audit have not been established.

## References

1. B. Fantechi and L. Göttsche, *Chern-Schwartz-MacPherson classes of symmetric powers and applications*, arXiv:2610.31826v1, posted 2026-10-22, especially Conjecture 4.26, Theorem 5.2, the definition of curve in §5.2, and Propositions 5.9–5.12 and Theorem 5.13. https://arxiv.org/html/2610.31826v1
2. D. Ferrand, *Conducteur, descente et pincement*, Bulletin de la Société Mathématique de France 131 (2003), finite pinching construction, cited as reference [15] and Theorem 5.4 in the preceding paper.
3. R. MacPherson, *Chern classes for singular algebraic varieties*, Annals of Mathematics 100 (1974), 423–432 (CSM proper pushforward and constructible functions).
