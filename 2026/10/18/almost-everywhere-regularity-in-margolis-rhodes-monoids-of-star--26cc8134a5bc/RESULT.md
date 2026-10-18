# Almost-everywhere regularity in Margolis–Rhodes monoids of star graphs

## Finding

Let \(m\ge 2\), let \(K_{1,m}\) be the star with centre \(o\) and \(m\) leaves, and let \(M_m=\operatorname{MR}(K_{1,m})\) be its monoid of continuous partial transformations in the inverse-simplex sense. Write \(I_m\) for the number of partial bijections of an \(m\)-element set:

\[
I_m=\sum_{k=0}^{m}\binom{m}{k}^{2}k!.
\]

Then the exact number of elements, noninjective elements, nonregular elements, and idempotents, respectively, are

\[
\begin{aligned}
|M_m|&=(m+2)(I_m+m),\\
|\{f\in M_m:f\text{ is noninjective}\}|&=m+m^2 I_{m-1},\\
|M_m\setminus\operatorname{Reg}(M_m)|&=m\bigl(I_m-mI_{m-1}-1\bigr),\\
|E(M_m)|&=2^{m+1}+m2^{m-1}+m.
\end{aligned}
\]

Every noninjective element is regular. The nonregular elements are **exactly** the injective partial maps whose image consists of at least two leaves and whose domain contains the centre. For a uniformly selected element \(f\in M_m\), as \(m\to\infty\),

\[
\begin{aligned}
\Pr(f\text{ is nonregular})&\sim m^{-1/2},\\
\Pr(f\text{ is injective})&\sim m^{-1/2},\\
\Pr(f\text{ is regular and noninjective})&=1-m^{-1/2}+o(m^{-1/2}).
\end{aligned}
\]

Thus every star with at least two leaves has nonregular elements, yet asymptotically almost every element is both **regular** and **noninjective**. The theorem also gives complete image-rank counts (below).

## Assumptions and scope

The graph has labelled vertex set \(V=\{o\}\sqcup L\), \(|L|=m\), with edges precisely \(\{o,a\}\) for \(a\in L\). A partial map \(f:V\rightharpoonup V\) is continuous precisely when, for every singleton or edge \(\sigma\) of the star, the full inverse image \(f^{-1}(\sigma)\) is empty, a singleton, or an edge of the star. Composition is ordinary composition of partial maps. We call \(f\) regular if there exists \(g\in M_m\) with \(fgf=f\). The empty map is included, and an injective partial map includes rank-zero and rank-one maps. No probabilistic independence assumptions are made.

## Proof

**1. Normal forms for noninjective maps.** A noninjective map has a fibre of size two. Continuity forces that fibre to be \(\{o,a\}\) for a unique leaf \(a\), and excludes any second doubled fibre. If this fibre maps to \(o\), the image has no other point: an additional leaf image would give an edge whose inverse image has at least three vertices. There are exactly \(m\) such maps. If the doubled fibre maps to a leaf \(b\), all remaining image points lie in \(L\setminus\{b\}\), and all remaining domain points lie in \(L\setminus\{a\}\), bijectively. Every such choice is continuous because inverse images of target edges contain at most the doubled fibre. There are \(m^2 I_{m-1}\) choices, yielding the noninjective formula.

**2. Normal forms for injective maps.** For an injective partial map, continuity is equivalent to requiring the inverse bijection from the image to the domain to send every edge of the induced image graph to an edge of the induced domain graph. If its image avoids \(o\), there is no restriction beyond injectivity. The number of such maps is

\[
A_m=\sum_{k=0}^m \binom{m}{k}(m+1)_k,
\]

where \((m+1)_k=(m+1)!/(m+1-k)!\) and \((m+1)_0=1\). If the image contains \(o\), one possibility is \(f(o)=o\) together with any partial bijection between leaf sets (\(I_m\) choices). The other possibilities are: a rank-one map with a leaf sent to \(o\) (\(m\) choices), or a rank-two bijection swapping a source centre–leaf pair onto a target centre–leaf pair (\(m^2\) choices). Hence the injective count is \(A_m+I_m+m+m^2\).

Let \(J_m\) count partial injections from an \(m\)-point source into a fixed \((m-1)\)-point target. Partitioning partial bijections on \(m\) points according to whether a fixed target vertex is used gives \(I_m=J_m+mI_{m-1}\). Similarly, partitioning maps counted by \(A_m\) according to whether their domain contains \(o\) gives \(A_m=I_m+mJ_m\). Thus

\[
A_m=(m+1)I_m-m^2I_{m-1}.
\]

Adding the injective and noninjective counts proves \(|M_m|=(m+2)(I_m+m)\).

**3. Elementwise regularity.** For every finite partial map \(f\), a witness to \(fgf=f\) restricts on \(\operatorname{Im}(f)\) to a section \(s\) of \(f\), with \(fs\) the identity on \(\operatorname{Im}(f)\). Conversely any continuous such section is a regularity witness. Restrictions of continuous maps are continuous, so it suffices to test sections defined just on the image.

A rank-one map always has a continuous section. For a noninjective map with doubled fibre \(\{o,a\}\mapsto b\in L\) and any additional singleton fibres, choose the representative \(a\) of the doubled fibre. All values of this section lie in leaves and its domain is a set of leaves, so it is continuous. The remaining noninjective maps have rank one. Thus **every noninjective map is regular**.

For an injective map the only possible section is its inverse on its image. This section is continuous if and only if the forward map also preserves all edges of the induced domain graph. The injective normal forms from step 2 show that this fails precisely when \(o\in\operatorname{Dom}(f)\) and \(\operatorname{Im}(f)\subseteq L\) has at least two points. Counting maps in this class by their rank \(k\) gives

\[
Q_m=\sum_{k=2}^{m}\binom{m}{k-1}\binom{m}{k}k!.
\]

Equivalently, among the \(A_m\) injective maps with leaf-only image, exclude the \(I_m\) maps with leaf-only domain and the \(m\) rank-one maps whose domain is just the centre. Thus

\[
Q_m=A_m-I_m-m=m(I_m-mI_{m-1}-1).
\]

This is the asserted nonregular count.

**4. Idempotents.** The injective idempotents are exactly partial identities, contributing \(2^{m+1}\). A noninjective idempotent collapses \(\{o,a\}\) onto \(o\), with no further values (\(m\) possibilities), or collapses \(\{o,a\}\) onto \(a\) and fixes any chosen subset of the other \(m-1\) leaves (\(m2^{m-1}\) possibilities). In either case the fixed-point condition \(f(f(v))=f(v)\) is immediate. No other singular map has all image points fixed. This gives the idempotent count.

**5. Rank distribution (exact refinement).** For \(0\le k\le m+1\), the number \(R_{m,k}\) of rank-\(k\) elements is the sum of

\[
\begin{aligned}
R^{\mathrm{inj}}_{m,k}&=\mathbf1_{k\le m}\binom{m}{k}(m+1)_k
+\mathbf1_{1\le k\le m+1}\binom{m}{k-1}(m)_{k-1}
+m\mathbf1_{k=1}+m^2\mathbf1_{k=2},\\
R^{\mathrm{sing}}_{m,k}&=m\mathbf1_{k=1}
+\mathbf1_{1\le k\le m}m^2\binom{m-1}{k-1}^{2}(k-1)!.
\end{aligned}
\]

The number of nonregular rank-\(k\) elements is \(\binom{m}{k-1}\binom{m}{k}k!\) for \(2\le k\le m\) and zero otherwise. Indicator terms outside their indicated ranges are zero; no falling factorial with a negative subscript is evaluated.

**6. Asymptotics without extrapolation.** Give a uniformly random partial bijection of an \(m\)-set its deficiency \(D_m=m-\operatorname{rank}(f)\). Its probability weights before normalization are

\[
w_{m,j}=\frac{(m!)^2}{(j!)^2(m-j)!},\quad 0\le j\le m;
\qquad\frac{w_{m,j+1}}{w_{m,j}}=\frac{m-j}{(j+1)^2}.
\]

For each fixed \(\varepsilon\in(0,1)\), these successive ratios are uniformly greater than \(1+c_\varepsilon\) below \((1-\varepsilon)\sqrt m\) and uniformly less than \(1-c_\varepsilon\) above \((1+\varepsilon)\sqrt m\), for sufficiently large \(m\). Comparison with a point in the intermediate band shows that both outside-tail probabilities are \(O(m\exp(-c'_\varepsilon\sqrt m))\). Since \(0\le D_m\le m\), this proves

\[
\mathbb E[D_m]/\sqrt m\longrightarrow1.
\]

A termwise comparison of the weights at sizes \(m\) and \(m-1\) gives the **exact** identity

\[
m^2I_{m-1}=\sum_{j=0}^m(m-j)w_{m,j}=(m-\mathbb E[D_m])I_m.
\]

Consequently \(Q_m=I_m\mathbb E[D_m]-m\) and the injective count equals \((\mathbb E[D_m]+2)I_m+m^2+m\). As \(I_m\ge m!\), the total is asymptotic to \(mI_m\). Dividing these exact identities by the total yields both \(m^{-1/2}\) laws. Since every noninjective map is regular, the final joint law follows. \(\square\)

## Verification

The standalone `verify_star.py` constructs every partial map on the labelled star for \(1\le m\le5\), tests the defining inverse-simplex condition without using the normal forms, computes regularity by enumerating all possible continuous sections, and compares counts of all elements, noninjective elements, regular elements, idempotents, rank strata and nonregular rank strata against the formulas. It separately verifies the partial-bijection recurrence through size \(149\). The script uses only the Python standard library. Running `python verify_star.py` terminates with `VERIFY_OK` on success. Finite enumerations are corroboration, not a proof of the infinite assertions.

## Relationship to prior work

Margolis and Rhodes (2026, arXiv:2609.39370) define the graph monoid, give a general matching/injective normal-form lemma (their Lemma 3.8), prove that only empty or complete graphs have a globally regular monoid (Proposition 4.4), and enumerate the monoids associated with paths and cycles. Their general framework is essential here; the present result **does not** claim a new definition, the general decomposition, or global nonregularity of stars. It supplies a new exact star-family census, precise classification of which individual maps are nonregular, a complete rank profile, and the counterintuitive asymptotic fact that almost all elements of these nonregular monoids are regular and singular. Their earlier foundational paper (arXiv:2005.02606) develops the inverse-simplex continuity definition.

## Limitations

The results concern the labelled star family only. The asymptotics fix the graph family and let the number of leaves grow; no conclusion is asserted for other trees. The counting identities and elementwise regularity are proved directly, while the statement that the formulas were not previously published remains subject to discovery of unindexed literature. No independent external mathematical audit has been performed.

## References

1. S. Margolis and J. Rhodes, *The Margolis-Rhodes Monoid of a Graph*, arXiv:2609.39370, initially public 2026-09-30; in particular Sections 3, 4, 7, 8.
2. S. W. Margolis and J. Rhodes, *Degree 2 Transformation Semigroups as Continuous Maps on Graphs: Foundations and Structure*, arXiv:2005.02606 (2020), Sections 1–2.
3. S. W. Margolis and J. Rhodes, *Degree 2 transformation semigroups as continuous maps on graphs: Complexity and examples*, *Int. J. Algebra Comput.* **33** (2023), 289–316, DOI:10.1142/S0218196723500157 (context for degree-two semigroup examples).
