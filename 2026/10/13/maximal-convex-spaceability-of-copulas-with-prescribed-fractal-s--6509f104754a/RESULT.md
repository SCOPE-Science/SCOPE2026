# Maximal convex spaceability of copulas with prescribed fractal support dimension

## Finding

For **every** real \(s\in(1,2)\), let
\[
\mathscr S_s=\{C:\ C\text{ is a bivariate copula and }\dim_H(\operatorname{supp}\mu_C)=s\}.
\]
With bivariate copulas embedded in \(C([0,1]^2)\) in the supremum norm, \(\mathscr S_s\) contains a **closed convex set having a continuum-sized linearly independent subset**. Consequently it is *maximally convex spaceable*, in precisely the sense of Definition 2.5 in de Amo, Fernández-Sánchez, García-Fernández and Úbeda-Flores (2026). This strengthens their Theorem 3.2 (maximal convex lineability) and answers the fractal-support spaceability question explicitly left open in their conclusion.

An explicit witness is obtained by fixing a compact self-similar set \(K_r\), a full-support copula measure \(\mu_0\) on it, and \(\eta\in(0,1)\), and setting
\[
\mathscr A_{r,\eta}=\{C:\ C\text{ a bivariate copula},\ \mu_C(K_r)=1,\ \mu_C\ge \eta\mu_0\}.
\]
The inequality is the order inequality of finite Borel measures on the square, not a pointwise inequality of distribution functions. Every member of \(\mathscr A_{r,\eta}\) has **exactly** support \(K_r\) and hence support dimension \(s\). The witness is compact, convex, and contains the linearly independent continuum family constructed below.

## Assumptions and scope

All parameters are real. Fix \(r\in(0,1/2)\) and \(a\in(0,r)\). On \([0,1]^2\) define the four corner similarities and the central similarity by
\[
\begin{aligned}
S_{00}(u,v)&=(ru,rv),\\
S_{01}(u,v)&=(ru,1-r+rv),\\
S_{10}(u,v)&=(1-r+ru,rv),\\
S_{11}(u,v)&=(1-r+ru,1-r+rv),\\
S_c(u,v)&=(r+(1-2r)u,r+(1-2r)v).
\end{aligned}
\]
Assign probabilities \(w_{00}=w_{11}=r-a\), \(w_{01}=w_{10}=a\), and \(w_c=1-2r\). All five weights are strictly positive and sum to one. Let \(\mu_{r,a}\) be the unique invariant probability measure of this contractive weighted iterated function system, and let \(C_{r,a}\) be its bivariate distribution function. Let \(K_r\) be the unweighted five-map attractor (independent of \(a\)). Define \(\mu_0=\mu_{r,a_0}\) for any fixed \(a_0\in(0,r)\).

The term *maximally convex spaceable* here means a closed convex subset of the target class that contains continuum many linearly independent distribution functions; it does **not** mean a nonzero closed linear subspace of copulas (which cannot exist because copulas have fixed normalization). The theorem addresses \(s\in(1,2)\), not the endpoint dimensions nor every possible prescribed compact support.

## Proof

**1. Uniform margins and copula status.** The three horizontal first-level bands have respective widths \(r,1-2r,r\). Their total branch probabilities are likewise \((r-a)+a=r\), \(1-2r\), and \(a+(r-a)=r\). The same holds vertically. Therefore the first-coordinate marginal of the weighted IFS is a stationary probability for the one-dimensional affine maps sending \([0,1]\) to \([0,r]\), \([r,1-r]\), and \([1-r,1]\), with probabilities equal to their interval lengths. Lebesgue measure on \([0,1]\) is stationary, as follows by partitioning an integral over the three intervals and changing variables. Uniqueness of the invariant measure for these strict contractions implies that the marginal is Lebesgue. The second-coordinate argument is identical. Hence \(C_{r,a}\) is a copula for every admissible \(r,a\).

**2. Common full fractal support and attainable dimensions.** All branch probabilities are positive, so the support of \(\mu_{r,a}\) is the unique compact attractor \(K_r\): every basic cylinder has positive mass, and cylinder diameters shrink to zero. The interiors of the four corner images and the central image of the unit square are pairwise disjoint. The open-set condition therefore holds, and the standard similarity-dimension theorem (Moran's formula) gives \(\dim_H(K_r)=s(r)\), the unique solution in \((1,2)\) of
\[
4r^{s(r)}+(1-2r)^{s(r)}=1.
\]
Indeed the left side is strictly decreasing in its exponent, while at exponent \(1\) its value is \(1+2r>1\), and at exponent \(2\) its value is \(1+4r(2r-1)<1\). The root depends continuously on \(r\). For each \(\varepsilon>0\), as \(r\downarrow0\) one has \(4r^{1+\varepsilon}+(1-2r)^{1+\varepsilon}<1\) for all sufficiently small \(r\), since \(r^{1+\varepsilon}=o(r)\). Thus \(s(r)\to1\). As \(r\uparrow1/2\), for each \(t<2\), the expression \(4r^t+(1-2r)^t\) tends to \(4(1/2)^t>1\), so \(s(r)\to2\). By continuity, **every** \(s\in(1,2)\) is equal to \(s(r)\) for some \(r\in(0,1/2)\).

**3. Linear independence by cylinder moments.** Fix such an \(r\) and let \(Q_k=[0,r^k]^2\) for each integer \(k\ge0\), with \(Q_0=[0,1]^2\). Because all copula marginals are Lebesgue, their measures assign mass zero to the vertical and horizontal boundaries of the basic squares. The only level-\(k\) word reaching the interior of \(Q_k\) is the word consisting of \(k\) repeated maps \(S_{00}\). Consequently
\[
\mu_{r,a}(Q_k)=(r-a)^k\qquad(k=0,1,2,\ldots).
\]
Suppose \(\sum_{i=1}^m c_i C_{r,a_i}=0\) as functions for distinct \(a_i\in(0,r)\). By the rectangle-increment formula, their associated finite signed measures satisfy \(\sum_i c_i\mu_{r,a_i}=0\). Evaluating on \(Q_k\) for \(k=0,\ldots,m-1\) gives \(\sum_i c_i(r-a_i)^k=0\). This is a Vandermonde system at distinct nodes \(r-a_i\), hence \(c_1=\cdots=c_m=0\). Therefore \(\{C_{r,a}:0<a<r\}\) is linearly independent of cardinality continuum. This step is proved directly here, without treating the literature's mutual-singularity statements as unverified black boxes.

**4. Anchored closed convex set.** Choose any \(a_0\in(0,r)\) and \(\eta\in(0,1)\). Define \(\mathscr A_{r,\eta}\) as in the finding. It is convex because copula measures, the fixed support concentration condition, and measure domination are preserved by convex mixtures. It is closed in the supremum topology: if copulas \(C_n\to C\) uniformly, then the corresponding probability measures converge weakly to \(\mu_C\), since the limiting bivariate CDF has continuous uniform margins. As \(K_r\) is closed and \(\mu_{C_n}(K_r)=1\), the portmanteau theorem implies \(\mu_C(K_r)=1\). For every nonnegative continuous \(f\),
\[
\int f\,d\mu_C=\lim_n\int f\,d\mu_{C_n}
\ge\eta\int f\,d\mu_0,
\]
so \(\mu_C\ge\eta\mu_0\) by positivity of finite Borel measures. The copula space is compact in the supremum norm, so this closed subset is also compact. Every \(C\in\mathscr A_{r,\eta}\) has support contained in \(K_r\) from concentration, and containing \(\operatorname{supp}\mu_0=K_r\) from domination. Thus \(\operatorname{supp}\mu_C=K_r\), and \(\mathscr A_{r,\eta}\subset\mathscr S_{s(r)}\).

**5. Continuum independence survives anchoring.** For each \(a\in(0,r)\), let
\[
D_a=\eta C_{r,a_0}+(1-\eta)C_{r,a}.
\]
Its copula measure is \(\eta\mu_0+(1-\eta)\mu_{r,a}\), so \(D_a\in\mathscr A_{r,\eta}\). Suppose a finite relation \(\sum_{i=1}^m d_iD_{a_i}=0\) holds for distinct parameters. Evaluation at \((1,1)\) gives \(\sum_i d_i=0\), and cancellation of the shared anchored term yields \((1-\eta)\sum_i d_iC_{r,a_i}=0\). By Step 3, all coefficients vanish. The family \(\{D_a:0<a<r\}\) is therefore continuum-sized and linearly independent, while all its members lie in the **closed convex** set \(\mathscr A_{r,\eta}\subset\mathscr S_s\).

Finally, the full ambient function space \(C([0,1]^2)\) has cardinality continuum, since its elements are determined by values on a fixed countable dense subset and a continuous injection from \([0,1]\) is immediate. No linearly independent family within it can have larger cardinality. The constructed continuum family is maximal. This proves the claim for every \(s\in(1,2)\). \(\square\)

## Verification

The analytic proof above establishes the entire continuum statement. The accompanying `CHECK.py` uses exact rational arithmetic to check the five weights, both marginal mass partitions, finite cylinder-mass Vandermonde determinants and their anchored versions; it also uses bisection to confirm example similarity-dimension roots. Run `python CHECK.py` with an ordinary Python 3 interpreter; it has no external dependencies. Its finite tests are reproducibility checks, **not** substitutes for the weak-convergence, Moran-dimension, or universal Vandermonde arguments.

## Relationship to prior work

De Amo et al. (2026), Definition 2.5, define maximal convex spaceability and in Theorem 3.2 prove only maximal convex **lineability** for copulas of prescribed fractal support dimension, using invariant copulas with shared support. Section 4 expressly leaves convex spaceability of fractal-support copulas unresolved. The new step is to impose a **fixed positive measure component**: domination by \(\eta\mu_0\) prevents loss of full support in weak limits, while an affine anchoring map preserves linear independence because normalized copula distribution functions all take the value one at \((1,1)\).

De Amo, Díaz Carrillo and Fernández-Sánchez (2012), in their Section 3.2 and Proposition 3.24, construct the underlying two-parameter self-similar measures and prove their mutual singularity despite sharing support. They do not formulate this closed convex support-stabilized family or maximal convex spaceability. The present proof independently derives the particular cylinder identities needed for the linearly independent family, instead of claiming originality for the 2012 construction or the classical Moran theorem.

## Limitations

The result uses **exact support dimension** \(s\in(1,2)\), not the Hausdorff dimension of a measure, and not an arbitrary specified support set. It gives a closed convex witness carrying continuum independent elements under the precise published definition; it does not claim that the witness is a linear subspace or that the ambient fractal-support class itself is closed. The mathematical proof is analytic; exact-rational finite tests alone cannot establish universal claims. Priority remains subject to unindexed or contemporaneous literature, and this work has not undergone independent scientific audit.

## References

1. E. de Amo, J. Fernández-Sánchez, D. García-Fernández and M. Úbeda-Flores, "Convex Lineability in Copula and Quasi-copula Sets," *Mediterranean Journal of Mathematics* 23, article 131 (2026), DOI: `10.1007/s00009-026-03129-9`; preprint arXiv: `2602.06918`, first posted 6 February 2026, version 1; Definition 2.5, Theorem 3.2 and Section 4.
2. E. de Amo, M. Díaz Carrillo and J. Fernández-Sánchez, "Copulas and associated fractal sets," *Journal of Mathematical Analysis and Applications* 386 (2012), 528–541, DOI: `10.1016/j.jmaa.2011.08.017`; Sections 2–3, notably Proposition 3.24, and its fractal construction.
3. G. A. Fredricks, R. B. Nelsen and J. A. Rodríguez-Lallena, "Copulas with fractal supports," *Insurance: Mathematics and Economics* 37 (2005), 42–48; cited for the classical self-similar copula background, not for the present spaceability conclusion.
