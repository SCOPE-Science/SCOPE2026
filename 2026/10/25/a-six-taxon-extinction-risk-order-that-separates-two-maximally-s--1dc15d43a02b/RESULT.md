# A six-taxon extinction-risk order that separates two maximally Sackin-balanced phylogenies

## Finding

**Theorem (complete six-tip order and a shape-changing graft).** Consider rooted, full, non-plane binary phylogenetic trees with six distinguishable species at their leaves and unit length on every edge. Each leaf goes extinct with probability \(0<q<1\). Compare (i) independent extinction and (ii) the exchangeable mixture in which, with probability \(0<\theta\le1\), all species share a single Bernoulli extinction event of parameter \(q\), and otherwise they go extinct independently with parameter \(q\). Denote by \(\Delta_T(q,\theta)\) the excess expected loss of rooted phylogenetic diversity in model (ii) over model (i).

Exactly six unlabeled rooted tree shapes exist. Their \(\Delta_T\) values are **strictly ordered for every** \(q\in(0,1)\) and \(\theta>0\), in the order A (largest loss), B, C, D, E, F (smallest loss), where the tree shapes and their clade polynomials \(F_T(q)\) are:

| Shape | Rooted Newick tree (arbitrary distinct leaf labels) | \(F_T(q)\) |
| --- | --- | --- |
| A | `(a,(b,(c,(d,(e,f)))))` | \(q^2+q^3+q^4+q^5\) |
| B | `(a,(b,((c,d),(e,f))))` | \(2q^2+q^4+q^5\) |
| C | `(a,((b,c),(d,(e,f))))` | \(2q^2+q^3+q^5\) |
| D | `((a,b),(c,(d,(e,f))))` | \(2q^2+q^3+q^4\) |
| E | `((a,(b,c)),(d,(e,f)))` | \(2q^2+2q^3\) |
| F | `((a,b),((c,d),(e,f)))` | \(3q^2+q^4\) |

Here \(F_T(q)=\sum_{v}q^{s(v)}\), summed over the four **non-root internal vertices**, where \(s(v)\) is the number of leaves below \(v\). Specifically,
\[
\Delta_T(q,\theta)=\theta\,[4q-F_T(q)].
\]

The two *Sackin-minimal* shapes E and F have identical leaf-depth multisets \(\{2,2,3,3,3,3\}\) and the same Sackin index \(16\), but
\[
\Delta_E(q,\theta)-\Delta_F(q,\theta)
=\theta q^2(1-q)^2>0.
\]
At \(q=1/2\) and \(\theta=1\), their excesses are respectively \(5/4\) and \(19/16\).

**Graft consequence.** In *any* larger rooted full binary tree with unit edge lengths and these same homogeneous extinction models, replacing a six-leaf fringe subtree E by F, while matching the two leaves at relative depth 2 and the other four at relative depth 3, preserves the leaf-depth vector, total branch length and Sackin index. It decreases excess expected lost diversity by **exactly** \(\theta q^2(1-q)^2\). In particular, no tree globally minimizing this excess can contain the E shape as a fringe subtree. Hence leaf-depth balance alone does not determine this loss, even in arbitrarily large trees.

For four tips the unique loss-minimizing shape has root split \(2+2\), and for five tips it has root split \(2+3\); six tips are the first size at which the unique loss-minimizing tree (root split \(2+4\)) has a root split less even than another Sackin-minimal shape (\(3+3\)).

## Assumptions and scope

A rooted full binary tree with \(n\ge2\) leaves has \(2n-2\) nonroot vertices, each connected to its parent by a unit-length edge. The rooted phylogenetic diversity of surviving leaves is the summed length of the edges on their paths to the root. Extinction loss \(L_T\) is total tree length minus surviving rooted diversity. The edge above a vertex is lost if and only if *all* its descendant species are extinct. We examine unconditional expectations, not a tail risk or an actual realized loss.

The correlated extinction law first selects an independent regime indicator: with probability \(\theta\) it uses a single Bernoulli(\(q\)) extinction indicator shared by all \(n\) species; with probability \(1-\theta\), it uses independent Bernoulli(\(q\)) indicators. Every species has extinction marginal \(q\), and for distinct species their extinction-indicator correlation is \(\theta\). The independent comparison has the same marginals. No assumption is made that the shared-regime indicator evolves by a trait Markov process on the phylogeny.

For a nonroot internal vertex \(v\), write \(s(v)\ge2\) for its number of descendant leaves. An \(n\)-tip full binary tree has \(n-2\) such nonroot internal vertices, and its \(n\) leaf edges contribute \(nq\) to independent expected loss.

## Proof

**1. Exact expectation identity.** Under independent extinction an edge with \(s\) descendant leaves is lost with probability \(q^s\). Under the shared regime the same event has probability \(q\), regardless of \(s\). Therefore its probability under the mixture is \((1-\theta)q^s+\theta q\). By linearity of expectation, for any rooted full binary tree on \(n\) leaves,
\[
\mathbb E_{\mathrm{ind}}L_T=nq+\sum_{v\in I^\circ(T)}q^{s(v)},\qquad
\mathbb E_{\mathrm{mix}}L_T=(1-\theta)\mathbb E_{\mathrm{ind}}L_T+\theta(2n-2)q,
\]
where \(I^\circ(T)\) denotes its internal vertices except the root. Hence
\[
\Delta_T(q,\theta)=\theta\Big((n-2)q-\sum_{v\in I^\circ(T)}q^{s(v)}\Big).
\]
In particular, for six leaves minimizing excess loss is equivalent to maximizing \(F_T(q)\).

**2. Exhaustive shape enumeration.** Every six-leaf rooted non-plane full binary tree has root split \(1+5\), \(2+4\), or \(3+3\). A five-tip rooted subtree has three shapes, a four-tip rooted subtree has two, and a three-tip subtree has one. Thus there are exactly \(3+2+1=6\) shapes. Computing the descendant-leaf counts of their four nonroot internal vertices yields precisely the A–F table in the Finding. The polynomials in that table are independent of the leaf labels, so the classification covers *all* labeled trees via shape.

**3. Strict universal ordering.** The successive differences of clade polynomials in the order A, B, C, D, E, F are, respectively,
\[
\begin{aligned}
F_B-F_A&=q^2(1-q),\\
F_C-F_B&=q^3(1-q),\\
F_D-F_C&=q^4(1-q),\\
F_E-F_D&=q^3(1-q),\\
F_F-F_E&=q^2(1-q)^2.
\end{aligned}
\]
Each is strictly positive for \(0<q<1\). As \(\theta>0\), the excess losses have the strict reverse ordering, proving the first claim. The final identity gives the exact E–F gap.

**4. The balanced-depth tie and graft.** E has two leaves at depth 2 (the singleton in each three-tip rooted subtree) and four at depth 3 (two cherries). F has two leaves at depth 2 (its two-tip rooted subtree) and four at depth 3 (the two cherries in its four-tip rooted subtree). Thus both have Sackin index \(2\cdot2+4\cdot3=16\), the minimum for six-tip binary trees: by the elementary complete-binary-depth bound, leaves only at depths \(\lfloor\log_2 6\rfloor=2\) and \(\lceil\log_2 6\rceil=3\) minimize total leaf depth (also established in the cited Sackin-index classification). Relabel F so that the same two designated leaves remain at depth 2, the other four at depth 3. Replacing E by F inside a larger tree preserves the global depth of every labeled leaf and all ancestor clade sizes outside the graft. All other nonroot internal clade terms remain unchanged, whereas the four changed terms increase by \(q^2(1-q)^2\). The exact expectation identity in Step 1 then decreases the excess by \(\theta q^2(1-q)^2\), strictly. The root case uses the same argument, with the graft root omitted from the clade sum; for a nonroot graft, that root itself has the unchanged clade size 6. Therefore no minimizing tree can contain E as a fringe subtree.

**5. First six-tip imbalance.** For four leaves, the two available clade polynomials are \(2q^2\) (root split \(2+2\)) and \(q^2+q^3\) (root split \(1+3\)); their difference is \(q^2(1-q)>0\). For five leaves, the polynomials are \(2q^2+q^3\) (root split \(2+3\)), \(2q^2+q^4\) and \(q^2+q^3+q^4\) (both root split \(1+4\)). The first exceeds the second by \(q^3(1-q)>0\), and the second exceeds the third by \(q^2(1-q)>0\). Three leaves have one shape. The six-tip table then supplies the first root-split comparison with two Sackin minimizers but a strict excess-loss preference between them.

## Verification

The standalone `verify.py` uses Python standard-library exact fractions. It recursively constructs all six rooted full-binary six-tip shapes, independently derives the four nonroot internal descendant counts, checks all five polynomial-difference identities, and checks the four- and five-tip maximizers. For each six-tip shape, four rational values of \(q\), and three rational values of \(\theta\), it enumerates all \(2^6=64\) extinction states and compares exact expected edge loss with the closed formula. It also checks the shared-regime mixture and the equal depth profiles of E and F. Executing `python verify.py certificate.json` generates the included deterministic `certificate.json`; the enumerated tests and formulas are reproducible without external packages.

These finite checks are consistency checks: universal strict inequalities and the larger-tree graft follow from the symbolic identities in the Proof, not by extrapolating the test cases.

## Relationship to prior work

Faller and Steel (2009, arXiv:0911.3441, subsequent journal publication 2012) study trait-dependent extinction and prove increased expected phylogenetic diversity loss under correlated extinction compared with matching independent marginals. Their edgewise expected-loss framework motivates the model here, but the present theorem uses a simpler global-shock mixture rather than their general trait-dependent Markov model. The all-shape strict ordering, exact gap between Sackin-minimizers, and any-size local graft are the claims evaluated here; the general direction of the correlated-versus-independent inequality is **not** claimed as new.

Fischer (2018/2021) characterizes trees minimizing the Sackin index, explicitly showing two six-tip minimizers of index 16. The new assertion is that these tied balance minimizers have **strictly different correlated-extinction excess losses**, with a closed factorization, despite identical leaf-depth multisets. Maliet, Gascuel and Lambert (2018) investigate ranked tree shapes and nonrandom extinctions in a three-parameter random-tree model, including simulated evolutionary-diversity losses. Their available abstract does not state a six-tip universal order or a depth-preserving graft for an exchangeable common-shock mixture; the full text was not accessible, and this remains a specific bibliographic risk. The 2019 article *Split sizes and extremal tree shapes* optimizes functionals of **unrooted smaller-side split sizes** under degree constraints. Its formulation is not an immediate implication of the rooted oriented clade-size sum \(\sum_v q^{s(v)}\), though broader unexamined tree-optimization literature remains a possible novelty risk.

## Limitations

The result concerns a mathematically specified exchangeable catastrophe mixture, not measured phylogenetic extinction patterns or all correlation mechanisms. It requires common extinction probability, unit edge lengths, strictly positive mixture weight, rooted full binary trees, and the *expectation* of rooted phylogenetic diversity loss. At \(q=0\), \(q=1\), or \(\theta=0\), the strict comparisons collapse. The arbitrary-size graft comparison preserves global leaf depths but does not classify every globally optimal tree for general \(n\). Larger-tree branches of unequal length can alter the conclusion. An earlier result under another name could cover the same six-shape ranking; bibliographic uniqueness is not mathematically established.

## References

1. B. Faller and M. Steel, *Trait-dependent extinction leads to greater expected biodiversity loss*, arXiv:0911.3441v1 (18 November 2009), https://arxiv.org/abs/0911.3441; later SIAM Journal on Discrete Mathematics 26 (2012), 472–481, doi:10.1137/090776743.
2. M. Fischer, *Extremal values of the Sackin tree balance index*, arXiv:1801.10418 (31 January 2018); Annals of Combinatorics 25 (2021), 515–541, doi:10.1007/s00026-021-00539-2.
3. O. Maliet, F. Gascuel, and A. Lambert, *Ranked Tree Shapes, Nonrandom Extinctions, and the Loss of Phylogenetic Diversity*, Systematic Biology 67 (2018), 1025–1040, doi:10.1093/sysbio/syy030.
4. *Split sizes and extremal tree shapes*, Advances in Applied Mathematics 104 (2019), 135–164, doi:10.1016/j.aam.2018.12.004.
