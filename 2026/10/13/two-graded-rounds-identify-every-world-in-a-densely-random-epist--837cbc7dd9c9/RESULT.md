# Two graded rounds identify every world in a densely random epistemic grid

## Finding

**Theorem (sharp typical depth and maximal expressive gap).** Fix \(0<\rho<1\). For each integer \(n\ge 2\), let \(W_n=[n]\times[n]\) have the two named, reflexive equivalence relations \(R\) and \(C\), where \((i,j)R(i',j')\) exactly when \(i=i'\), and \((i,j)C(i',j')\) exactly when \(j=j'\). Independently for each cell, declare the single proposition \(p\) true with probability \(\rho\).

Let \(K_t^{\mathrm{gr}}(n)\) be the number of distinguishable cell types using graded bimodal formulas of nesting depth at most \(t\), with unrestricted finite numerical thresholds, and let \(K_\infty^{\mathrm{ord}}(n)\) be the number of equivalence classes for ordinary bimodal formulas of arbitrary finite depth. Then, as \(n\to\infty\), simultaneously with probability tending to one,

\[
K_0^{\mathrm{gr}}(n)=2,\qquad K_1^{\mathrm{gr}}(n)<n^2,\qquad
K_2^{\mathrm{gr}}(n)=n^2,\qquad K_\infty^{\mathrm{ord}}(n)=2.
\]

The assertions hold for every fixed \(\rho\in(0,1)\). In particular, two modal rounds are typically **necessary and sufficient** for the graded language to distinguish every world, whereas no ordinary modal depth distinguishes more than the two propositional colors. The ratio between the eventual graded and ordinary quotient cardinalities is then exactly \(n^2/2\), the largest possible value for a genuinely two-colored \(n^2\)-world model. The depth-two graded-definable subsets comprise the entire powerset algebra, of cardinality \(2^{n^2}\); the ordinarily definable algebra has four elements.

The source-inspired question is motivated by finite graded multimodal types and counting message passing. The probabilistic two-round theorem and its matrix-degree proof are the claim evaluated here; the general graded-type/refinement correspondence is prior work.

## Assumptions and scope

The frame has exactly the two **named** row and column relations, each including its diagonal. Counting modalities can express that at least \(k\) successors satisfy a formula for any finite integer \(k\ge0\). The only atomic proposition is \(p\). Each cell receives an independent Bernoulli \(\rho\) value, with \(\rho\) fixed independently of \(n\). All probabilities refer to these independent product measures; the theorem is asymptotic and makes no uniform claim as \(\rho\) tends to zero or one with \(n\).

For a deterministic marking matrix \(X=(X_{ij})\in\{0,1\}^{n\times n}\), write its row and column degrees
\[
D_i=\sum_j X_{ij},\qquad E_j=\sum_i X_{ij}.
\]
Define the marked-column-degree histogram of row \(i\) and the marked-row-degree histogram of column \(j\) by
\[
H_i(v)=\sum_j X_{ij}\mathbf1_{\{E_j=v\}},\qquad
J_j(u)=\sum_i X_{ij}\mathbf1_{\{D_i=u\}}.
\]
Here \(u,v\in\{0,\ldots,n\}\). These histograms are deterministic functions of \(X\), not independent variables.

## Proof

**Step 1: the two-round deterministic criterion.** At graded depth zero the type of cell \((i,j)\) is just \(X_{ij}\). Since each row and column equivalence class consists of exactly \(n\) cells, counting its marked successors gives the depth-one type exactly as the triple
\[
\tau_1(i,j)=(X_{ij},D_i,E_j).
\]
This follows directly from counting modal semantics; each coordinate of the triple is expressible using a depth-one formula. The full depth-two row-successor multiset of types contains, for each \(v\), exactly \(H_i(v)\) successors with \(X=1\) and column degree \(v\). The corresponding column-successor multiset contains all values \(J_j(u)\). Hence if the \(n\) vectors \(H_i\) are pairwise distinct, and so are the \(n\) vectors \(J_j\), two distinct cells \((i,j)\ne(i',j')\) have distinct depth-two types: when \(i\ne i'\) the row multiset separates them, and when \(j\ne j'\) the column multiset separates them. This is a sufficient criterion, not an equivalence assumed without proof.

**Step 2: exact cancellation for a pair of rows.** Fix distinct row indices \(a,b\). For each column \(j\), remove the contributions of those rows and put
\[
T_j=\sum_{i\notin\{a,b\}}X_{ij}.
\]
The \(T_j\) are independent with law \(\mathrm{Bin}(n-2,\rho)\), and are jointly independent of all pairs \((X_{aj},X_{bj})\). For every integer \(k\), the difference of the two histograms has the **exact** representation
\[
H_a(k+1)-H_b(k+1)=\sum_{j:T_j=k}(X_{aj}-X_{bj}).\tag{1}
\]
Indeed, if the two row entries coincide, their contribution to the histogram difference vanishes; if they differ, their column degree is \(T_j+1\). The identity avoids the tempting but incorrect assumption that full column degrees are independent of the two compared row entries.

Conditional on all the \(T_j\), the sums on the right of (1), for different \(k\), are independent. Each is the sum of \(M_k=|\{j:T_j=k\}|\) independent copies of a symmetric random variable \(Y\), with
\[
\Pr(Y=1)=\Pr(Y=-1)=b:=\rho(1-\rho),\qquad \Pr(Y=0)=1-2b.
\]
There is a constant \(A_\rho<\infty\) such that for all \(m\ge1\),
\[
\Pr(Y_1+\cdots+Y_m=0)\le A_\rho m^{-1/2}.\tag{2}
\]
To verify (2), Fourier inversion gives \((2\pi)^{-1}\int_{-\pi}^{\pi}[1-2b(1-\cos t)]^m\,dt\). Since \(0<b\le1/4\), the bracket lies in \([0,1]\), and \(1-\cos t\ge2t^2/\pi^2\) on this interval. Bounding the integrand by \(\exp(-4bmt^2/\pi^2)\) and integrating proves (2).

**Step 3: sufficiently many independent central bins.** Standard Stirling bounds for the binomial distribution, with \(\rho\) fixed, yield constants \(\alpha_\rho,\beta_\rho>0\) and a set \(I_n\) of at least \(\alpha_\rho\sqrt n\) consecutive integers such that
\[
\Pr(T_j=k)\ge\beta_\rho n^{-1/2}\quad\text{for every }k\in I_n
\]
for all sufficiently large \(n\). One may take a fixed-width multiple of the standard-deviation window about \((n-2)\rho\). By a Chernoff lower-tail bound, for each such \(k\),
\[
\Pr\big(M_k<\tfrac12\beta_\rho\sqrt n\big)
\le\exp(-\beta_\rho\sqrt n/8).
\]
A union bound shows that all bins in \(I_n\) have at least \(\tfrac12\beta_\rho\sqrt n\) columns, except with probability at most \(O_\rho(\sqrt n e^{-c_\rho\sqrt n})\). On this event, conditional independence across the bins, (1), and (2) imply
\[
\Pr(H_a=H_b)
\le O_\rho(\sqrt n e^{-c_\rho\sqrt n})
 +\big(A'_\rho n^{-1/4}\big)^{\alpha_\rho\sqrt n}
 =o(n^{-2}).\tag{3}
\]
The same argument, interchanging rows with columns, proves \(\Pr(J_a=J_b)=o(n^{-2})\) for each pair of distinct columns. Union bounds over all pairs imply that all row histograms and all column histograms are simultaneously pairwise distinct with probability \(1-o(1)\). Step 1 proves \(K_2^{\mathrm{gr}}(n)=n^2\) on this event.

**Step 4: graded depth one is insufficient.** Chernoff/Hoeffding inequalities and a union bound give, with probability tending to one,
\[
\max_i|D_i-n\rho|+\max_j|E_j-n\rho|
 =O_\rho(\sqrt{n\log n}).
\]
Thus each of the sets of occurring row degrees and column degrees has size \(O_\rho(\sqrt{n\log n})\). By the exact depth-one triple in Step 1,
\[
K_1^{\mathrm{gr}}(n)\le2\,O_\rho(n\log n)=o(n^2).
\]
Moreover, both propositional colors occur with probability tending to one, yielding \(K_0^{\mathrm{gr}}(n)=2\).

**Step 5: all ordinary depths collapse to two types.** Every row and every column contains both colors except with probability at most
\[
2n\big(\rho^n+(1-\rho)^n\big)=o(1).
\]
On the complementary event, the relation identifying all cells of the same propositional color is an ordinary two-modal bisimulation: matching any outgoing row or column move requires only the existence of a successor of the requested color, and both colors occur in every row and every column. No ordinary formula, at any depth, distinguishes cells of the same color. Since both colors occur, precisely two ordinary classes remain.

All five high-probability events can be intersected. A finite model with every world singled out by depth-two graded formulas has every subset definable by a Boolean combination of such formulas, so its depth-two definable algebra is the powerset. With exactly two ordinary types, the ordinarily definable Boolean algebra has four elements. The ratio \(n^2/2\) is maximal among models realizing at least two propositional colors, because graded types number at most \(n^2\) and ordinary types number at least two. \(\square\)

## Verification

The accompanying standalone standard-library program `verify.py` implements independent row/column multiset refinement and ordinary set refinement; checks the explicit depth-one degree triple as an equivalence partition; checks the sufficient histogram criterion; exhaustively tests every binary square matrix of sizes one, two, and three (\(2+16+512=530\) matrices); and tests 2,100 independently generated matrices across 21 specified combinations of sizes and densities with a fixed random seed. It reports small-size exact counts and each large-size depth-two success rate. The finite checks validate semantics and boundary cases, not the all-height probabilistic limit, which rests on (1)–(3) and concentration bounds.

Run with `python3 verify.py`. No third-party packages are required.

## Relationship to prior work

Ahvonen, Heiman, and Kuusisto (2024) develop graded multimodal types and their equivalence to multichannel counting message passing and Weisfeiler–Leman-style refinement. Their full accessible article describes general syntax and expressivity, not a dense-random matrix model or a two-round high-probability spectrum. Nunn and Schwarzentruber (2023) connect counting modal constructs to graph neural networks; their examined material addresses logical transformations and satisfiability, not the Bernoulli grid limit. Classical results of Babai, Erdős, and Selkow (1980) concern canonical labeling of almost all unstructured random graphs; they do not directly state this fixed-equivalence-grid and cell-label theorem.

Earlier constructions of maximal ordinary/graded quotient separation show that the extremal ratio alone is not new. Earlier random-grid work at sparsity \((\log n+c)/n\) finds a different, isolated-row/column limiting law for **ordinary**, rather than graded, definability. The present contribution is the **dense typical-case sharp modal depth two**, together with the elementary independent-bin proof of full graded separation and simultaneous ordinary collapse. An undiscovered reduction to older random bipartite color-refinement literature remains a novelty risk.

## Limitations

The density \(\rho\) is fixed strictly between zero and one; no assertion is made for sparse, vanishing-density or almost-complete regimes. The estimate is asymptotic: particular finite matrices may need greater depth, fail to separate, or separate already at depth one. The proof is mathematical and supported by finite computation; independent mathematical audit and complete historical priority review have not been performed.

## References

1. V. Ahvonen, D. Heiman and A. Kuusisto, *Graded modal logic and counting message passing automata*, arXiv:2401.06519 (first submitted 2024-01-12), sections 2–4, https://arxiv.org/html/2401.06519v2.
2. P. Nunn and F. Schwarzentruber, *A Modal Logic for Explaining some Graph Neural Networks*, arXiv:2307.05150 (first submitted 2023-07-11), https://arxiv.org/html/2307.05150.
3. L. Babai, P. Erdős and S. M. Selkow, *Random Graph Isomorphism*, SIAM Journal on Computing 9 (1980), 628–635, https://doi.org/10.1137/0209047.
