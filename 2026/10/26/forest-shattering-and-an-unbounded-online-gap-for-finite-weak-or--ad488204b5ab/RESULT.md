# Forest shattering and an unbounded online gap for finite weak-order comparisons

## Finding
For every integer \(n\ge1\), let \(\mathcal W_n\) consist of all total preorders (weak orders, or rankings allowing ties) of \([n]\). Their Boolean strict-comparison concept class is
\[
\mathcal H_n=\bigl\{h_\rho:(i,j)\mapsto\mathbf1[\rho(i)<\rho(j)]:\rho\in\mathcal W_n,\ i,j\in[n],\ i\ne j\bigr\}.
\]
Here \(\rho\) denotes a normalized integer rank map with equal ranks for ties, and the query domain is the set of **ordered** pairs of distinct labels. In particular, the negative answer to \((i,j)\) means \(\rho(i)\ge\rho(j)\), allowing equality.

**Theorem.** A set \(S\) of ordered-pair queries is VC-shattered by \(\mathcal H_n\) if and only if it never contains both orientations of one unordered pair and its underlying undirected simple graph is a forest. Consequently, for all \(n\ge1\),
\[
\operatorname{VCdim}(\mathcal H_n)=n-1.
\]
The exact initial Littlestone dimensions are
\[
(\operatorname{Ldim}(\mathcal H_1),\operatorname{Ldim}(\mathcal H_2),
\operatorname{Ldim}(\mathcal H_3),\operatorname{Ldim}(\mathcal H_4))=(0,1,3,5).
\]
Thus three elements give the first strict static/adaptive shattering gap. Moreover, for every integer \(s\ge1\),
\[
\operatorname{Ldim}(\mathcal H_{4s})\ge5s,
\qquad \operatorname{Ldim}(\mathcal H_{4s})-\operatorname{VCdim}(\mathcal H_{4s})\ge s+1.
\]
The gap is unbounded within one natural sequence of finite relational concept classes; the displayed lower bound does **not** assert equality in the Littlestone dimension for larger sizes.

## Assumptions and scope
A weak order is a partition of the labeled domain into a linearly ordered sequence of nonempty tie blocks. Encode its blocks by consecutive ranks \(0,1,\ldots,k-1\) for some \(1\le k\le n\). Only strict pairwise comparison membership, not three-valued feedback and not the usual simultaneous complete-ranking prediction problem, is considered. The two oriented queries \((i,j)\) and \((j,i)\) are distinct coordinates. Static shattering requires all binary answer assignments on a fixed set of coordinates; a Littlestone tree has a coordinate at every internal node, possibly depending on earlier answers, and each root-to-leaf answer sequence must be realized by a single weak order.

## Proof
**Static characterization.** If both ordered orientations of an unordered pair belong to \(S\), the assignment giving both answer \(1\) is inconsistent with asymmetry of strict comparison. Suppose instead that \(S\) has one chosen orientation per edge and its underlying undirected graph contains a cycle. Traverse that cycle cyclically. Give answer \(1\) to every query oriented with the traversal, and answer \(0\) to every query oriented against it. Along the traversal, every edge then imposes a weak nondecreasing rank inequality, strict wherever an answer is \(1\). Choose the direction of traversal so that at least one answer is \(1\) (one of the two directions has this property). A cyclic chain of weak inequalities with at least one strict inequality is impossible. Hence \(S\) cannot be shattered.

Conversely, when the underlying graph is a forest, take any prescribed \(0/1\) labeling. Orient each queried forest edge in its stated direction for a \(1\), and in the reverse direction for a \(0\). Every orientation of a forest is acyclic, so it has a linear extension. Use the distinct ranks of that linear extension as a weak order: all prescribed positive answers hold, while the reversed strict inequalities make the negative answers hold. This realizes every labeling. An \(n\)-vertex forest contains at most \(n-1\) edges, and a spanning tree has exactly \(n-1\), proving the VC formula, including \(n=1\).

**Small adaptive upper bounds.** The number of weak orders on \(n\) labels is the ordered Bell number \(\sum_{k=1}^{n}k!\,\bigl\{\begin{smallmatrix}n\\k\end{smallmatrix}\bigr\}\); for \(n=1,2,3,4\) these counts are \(1,3,13,75\). Any complete binary depth-\(d\) shattered tree needs at least \(2^d\) *distinct* hypotheses, because one hypothesis follows only one full answer path. Hence \(\operatorname{Ldim}(\mathcal H_2)\le1\) and \(\operatorname{Ldim}(\mathcal H_3)\le3\). For four labels, fix any root query \((i,j)\). Exactly \(13\) weak orders tie \(i\) and \(j\), by collapsing these two labels into one; swapping \(i\) and \(j\) pairs the remaining orders between the two strict orientations. Thus the root answer-\(1\) branch has exactly \((75-13)/2=31\) hypotheses. A depth-six shattered tree would require a depth-five subtree on this branch, with at least \(32\) different hypotheses, a contradiction. Therefore \(\operatorname{Ldim}(\mathcal H_4)\le5\).

**Small adaptive lower bounds.** One nonconstant comparison shatters a depth-one tree on two labels. The attached `adaptive_preorder_trees.json` contains complete binary query trees of depths three and five on three and four labels, respectively. It specifies every internal ordered-pair query and one normalized rank vector at every leaf. The independent `verify_preorder.py` enumerates *all* ordered set partitions using a block-subset recursion, checks each query response along each certificate path, checks distinct witnesses, and separately computes the two dimensions by an exact finite recurrence. It finds eight consistent leaves at depth three and 32 consistent leaves at depth five, providing direct finite mathematical certificates for both lower bounds.

**Unbounded gap.** On \(4s\) labeled elements, partition the labels into \(s\) consecutive blocks of four. Restrict attention to weak orders that place every element of an earlier block strictly before every element of a later block, while allowing an arbitrary weak order *within* each block. This is a valid subclass of \(\mathcal W_{4s}\), isomorphic on the within-block query coordinates to the Cartesian product of \(s\) copies of \(\mathcal H_4\). Concatenate the depth-five shattered trees of the different blocks: on each path their leaf weak orders combine to a unique compatible global weak order, proving a complete tree of depth \(5s\). Since the VC formula already gives \(4s-1\), subtraction yields the asserted gap.

## Verification
Run `python verify_preorder.py adaptive_preorder_trees.json` with Python 3 and no third-party packages. It independently enumerates \(1,3,13,75\) weak orders on one through four labels; verifies the exact VC and Littlestone profiles \((0,1,2,3)\) and \((0,1,3,5)\); replays the depth-three and depth-five certificates; and checks the 31-hypothesis strict-positive root count. The recorded output is in `verifier_output.txt`. The certificate generator `generate_certificate.py` is included only for reproducibility: the verifier does **not** use its dynamic-programming implementation to decide whether a leaf is valid.

## Relationship to prior work
Raman, Subedi and Tewari (2023a) study online learnability of multilabel ranking under relevance-score feedback via threshold restrictions of *permutation-valued predictions*. Raman, Subedi and Tewari (2023b) develop set-valued feedback and a different ranking Littlestone dimension. Neither inspected framework directly states the static forest criterion, four-label binary strict-comparison rank, or the within-block amplification for weak orders allowing ties. Chase, Freitag and Reyzin (2023) address abstract Littlestone dimension in randomized equivalence-query learning and compression, rather than evaluating this concrete family. Results on compatibility set systems between partial and total orders use a different domain and incidence relation from membership of ordered pairs. These comparisons do not constitute proof of historical priority.

## Limitations
No exact formula for \(\operatorname{Ldim}(\mathcal H_n)\) is claimed when \(n\ge5\), nor is the displayed lower bound claimed optimal. The finite depth certificates are mathematical witnesses but still benefit from independent audit of the implementation and premise. No claim of exhaustive bibliographic priority or external certification is made. Only the specific binary strict-comparison feedback model is addressed.

## References
- V. Raman, U. Subedi, A. Tewari, *On the Learnability of Multilabel Ranking*, arXiv:2304.03337 (first posted 2023-04-06), NeurIPS 2023.
- V. Raman, U. Subedi, A. Tewari, *Online Learning with Set-valued Feedback*, arXiv:2306.06247 (first posted 2023-06-09).
- H. Chase, J. Freitag, L. Reyzin, *Applications of Littlestone Dimension to Query Learning and to Compression*, arXiv:2310.04812 (first posted 2023-10-07).
- B. Duan, M. Ouyang, Z. Wang, *VC-dimensions Between Partially Ordered Sets and Totally Ordered Sets*, arXiv:2412.06402 (first posted 2024-12-09; cited solely for distinguishing mathematical incidence relations).
