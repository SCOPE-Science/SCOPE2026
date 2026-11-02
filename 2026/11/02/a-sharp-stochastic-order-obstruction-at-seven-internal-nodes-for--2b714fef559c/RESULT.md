# A sharp stochastic-order obstruction at seven internal nodes for conditional Catalan cherry counts

## Finding

Let \(T_n\) be a uniform plane rooted full binary tree with exactly \(n\) internal nodes, and let \(K\) be the number of internal nodes in its left root subtree. A **cherry** is an internal node whose two children are leaves. Write \(Y_{n,k}\) for the number of cherries conditional on \(K=k\).

**Theorem.** For every integer \(n\geq 3\), \(Y_{n,0}\leq_{\mathrm{st}}Y_{n,1}\). For every integer \(n\geq4\), \(Y_{n,2}\leq_{\mathrm{st}}Y_{n,1}\). Despite these two comparable boundary moves, for **every integer \(n\geq7\)** the two laws \(Y_{n,2}\) and \(Y_{n,3}\) are incomparable in ordinary stochastic order. In fact
\[
\mathbb E[Y_{n,2}]>\mathbb E[Y_{n,3}],
\]
while the distribution indexed by \(3\) has strictly more mass at an upper-tail threshold where the distribution indexed by \(2\) cannot dominate it. Among all inward one-unit root-split moves in uniform full binary trees, \(n=7\) is the smallest size where stochastic incomparability occurs.

The obstruction is explicit at the first size:
\[
\Pr(Y_{7,2}=2)=\frac{16}{28},\quad\Pr(Y_{7,2}=3)=\frac{12}{28},
\]
\[
\Pr(Y_{7,3}=2)=\frac{16}{25},\quad\Pr(Y_{7,3}=3)=\frac8{25},\quad\Pr(Y_{7,3}=4)=\frac1{25}.
\]
Thus \(\Pr(Y_{7,2}\geq3)=3/7>9/25=\Pr(Y_{7,3}\geq3)\), whereas \(\Pr(Y_{7,2}\geq4)=0<1/25=\Pr(Y_{7,3}\geq4)\). The result concerns the conditional **distributions**, not the already-known conditional means.

## Assumptions and scope

A plane full binary tree has left/right-ordered children and every internal vertex has exactly two children. Size always means number of **internal** vertices; a lone leaf has size zero. Let \(\mathrm{Cat}_m=\binom{2m}{m}/(m+1)\), and let \(Z_m\) be the cherry count of a uniform tree with \(m\) internal vertices; \(Z_0=0\). For a given root split \(K=k\), the subtrees are independent uniform trees with \(k\) and \(n-1-k\) internal vertices. Consequently
\[
Y_{n,k}\ \overset{d}=\ Z_k+Z'_{n-1-k},
\]
where the two random variables on the right are independent. These are finite, exact, unweighted uniform plane-tree distributions—not unordered trees, ranked trees, tanglegrams, or Yule trees. For integer-valued random variables, \(U\leq_{\mathrm{st}}V\) means \(\Pr(U\geq t)\leq\Pr(V\geq t)\) for every integer \(t\).

## Proof

**1. Cherry-count coefficients.** Write \(A_m(j)\) for the number of plane full binary trees with \(m\) internal vertices and \(j\) cherries. Set \(A_0(0)=1\), with all other \(A_0(j)=0\). The bivariate tree generating function, with an additional factor \(u\) for each cherry, is
\[
F(z,u)=1+z\bigl(F(z,u)^2+u-1\bigr).
\]
Indeed the subtracted \(1\) removes the ordinary weight of the tree with both children leaves, and \(u\) restores its cherry weight. Putting \(W=F-1\) gives \(W=z(W^2+2W+u)\). Lagrange inversion then gives, for \(m\geq1\) and \(1\leq j\leq\lfloor(m+1)/2\rfloor\),
\[
A_m(j)=\frac1m\binom mj\binom{m-j}{j-1}2^{m-2j+1},
\]
with zero coefficients outside that range. The positive-support maximum cherry count is \(\lfloor(m+1)/2\rfloor\). By differentiating the same generating function in \(u\) and setting \(u=1\),
\[
f(m):=\mathbb E Z_m=\frac{m(m+1)}{2(2m-1)}\quad(m\geq1),\qquad f(0)=0.
\]

**2. The first two stochastic comparisons.** There is a direct uniform growth coupling \((T_m,T_{m+1})\) in which the cherry count never decreases and rises by at most one. Start from a uniform \(T_m\), pick one of its \(2m+1\) vertices uniformly, and replace that vertex by a new internal vertex carrying the old vertex/subtree and one new leaf in a fair random left/right order. Every output tree has exactly \(m+2\) reverse deletions (delete one of its leaves and suppress its parent). As
\[
2(2m+1)\,\mathrm{Cat}_m=(m+2)\,\mathrm{Cat}_{m+1},
\]
this is a uniform coupling. Insertion at an old internal vertex changes no cherries; insertion at an old leaf creates a cherry and may destroy the cherry at its former parent, so the net cherry increment is either zero or one. Hence \(Z_m\leq_{\mathrm{st}}Z_{m+1}\leq_{\mathrm{st}}Z_m+1\) for every \(m\geq1\). The root-split decomposition now yields
\[
Y_{n,0}=_{d}Z_{n-1},\quad
Y_{n,1}=_{d}1+Z_{n-2},\quad
Y_{n,2}=_{d}1+Z_{n-3},
\]
where the last identity uses \(Z_2\equiv1\). The two stated boundary inequalities follow immediately, including the small-size equality cases.

**3. The mean direction of the third move.** As \(Z_3\) takes values one and two with counts four and one, \(\mathbb E Z_3=f(3)=6/5\). For \(n\geq7\),
\[
Y_{n,3}=_{d}Z_3+Z'_{n-4},\qquad
\mathbb E[Y_{n,2}]-\mathbb E[Y_{n,3}]
=\bigl(f(n-3)-f(n-4)\bigr)-\bigl(f(3)-f(2)\bigr).
\]
For \(m\geq2\) define \(\Delta_m=f(m+1)-f(m)\). Direct calculation gives
\[
\Delta_m=\frac{(m-1)(m+1)}{(2m-1)(2m+1)},\qquad
\Delta_{m+1}-\Delta_m=\frac3{(2m-1)(2m+1)(2m+3)}>0.
\]
Thus \(\Delta_{n-4}>\Delta_2=1/5\) for every \(n\geq7\). So \(Y_{n,2}\leq_{\mathrm{st}}Y_{n,3}\) is impossible, since stochastic domination implies ordering of expectations.

**4. An upper-tail reversal for every size.** For odd \(n=2r+1\geq7\), \(Y_{n,2}\) has largest possible value \(r\), while \(Y_{n,3}\) has largest possible value \(r+1\), attained with strictly positive probability. Thus \(Y_{n,3}\leq_{\mathrm{st}}Y_{n,2}\) is impossible. For even \(n=2r\geq8\), both random variables have maximum \(r\), but the exact coefficient formula from step 1 shows
\[
\frac{\Pr(Y_{n,3}=r)}{\Pr(Y_{n,2}=r)}=\frac{2n-7}{5}>1.
\]
To verify this simplification, let \(m=n-3=2r-3\); use \(Z_2\equiv1\), \(\Pr(Z_3=2)=1/5\),
\[
A_m(r-1)=\frac1{r-1}\binom{2r-4}{r-2},\qquad
A_{m-1}(r-2)=\binom{2r-4}{r-2},
\]
and \(\mathrm{Cat}_m/\mathrm{Cat}_{m-1}=(4r-7)/(r-1)\). This proves that the conditional law at split three has a strictly larger maximal tail for every even \(n\geq8\). In both parities \(Y_{n,3}\leq_{\mathrm{st}}Y_{n,2}\) fails, completing incomparability.

**5. Sharpness of seven.** Moving the left subtree toward the midpoint means comparing \(k\) with \(k+1\) for integers \(0\leq k<\lfloor(n-1)/2\rfloor\). For \(n\leq6\), the only nontrivial moves have \(k=0\) or \(k=1\), already ordered by step 2; any central reflected pair is equal in law. At \(n=7\) the new move \(k=2\) to \(k=3\) first appears, and step 4 exhibits its failure. The threshold is therefore minimal.

## Verification

The accompanying standalone standard-library script `verify.py` computes the exact cherry-count polynomials by two independent routes (Lagrange coefficients and root splitting); it also enumerates each actual plane binary shape through nine internal vertices. It checks all stated inequalities and incomparabilities for the first 99 sizes, formula and normalization identities through 159 sizes, all parity-dependent maximum-tail ratios through the tested range, and the explicit first counterexample. On execution it passed **14,279 exact checks**. These finite checks supplement, rather than substitute for, the all-size algebraic and coupling arguments in steps 1–5. Run with `python verify.py`.

## Relationship to prior work

Janson's treatment of conditioned Galton–Watson and simply generated trees identifies uniform full binary trees with the offspring law supported at zero and two; this establishes the probabilistic model and not the finite conditional stochastic ordering here. The uniform growth mechanism is classical (Rémy). Konvalinka and Wagner study cherry counts and root branches in connection with random tanglegrams, with asymptotic statements; McKenzie and Steel discuss cherry-count distributions in other tree sampling models. Earlier known results include an exact **conditional mean regression** for cherries given root split; its negative dependence alone neither identifies stochastic-order comparability nor proves the all-size top-tail obstruction. The new statement is a sharp distributional boundary, not the classical cherry enumeration or the conditional mean formula.

## Limitations

The distributions are conditional on the exact root split in uniform **plane** full binary trees. The result does not assert a complete ordering of all pairs of splits, nor transfer without proof to unordered, ranked, uniform-label PDA, Yule, or tanglegram laws. A bounded literature and published-result comparison is not a universal novelty certificate; an older general stochastic-order theorem may imply part of the result. The proof is mathematical and the checks are finite; independent audit has not been performed.

## References

- Svante Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, first public version 2011-12-02, especially Example 9.3 on uniform full binary trees. https://arxiv.org/abs/1112.0510
- Matjaž Konvalinka and Stephan Wagner, *The shape of random tanglegrams*, first public version 2015-12-03, especially Section 3 on cherry counts and root branches. https://arxiv.org/abs/1512.01168
- A. McKenzie and M. Steel, *Distributions of cherries for two models of trees*, 1999 preprint. https://ir.canterbury.ac.nz/bitstreams/246ff6f4-967f-4550-9f98-c4b3d671fe84/download
- Jean-Luc Rémy, *Un procédé itératif de dénombrement d'arbres binaires et son application à leur génération aléatoire*, RAIRO Informatique théorique 19 (1985), 179–195. https://www.numdam.org/item/ITA_1985__19_2_179_0/
