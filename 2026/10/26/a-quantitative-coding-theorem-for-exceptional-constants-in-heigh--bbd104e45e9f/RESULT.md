# A Quantitative Coding Theorem for Exceptional Constants in Height-Three Rooted Trees

## Finding

For every computably enumerable set \(W\subseteq\omega\), one can uniformly construct a computable rooted predecessor tree \(T_W\) of height at most three such that

\[
\mu(T_W)=\begin{cases}
|\omega\setminus W|,&\text{if }W\text{ is cofinite},\\
\infty,&\text{otherwise}.
\end{cases}
\]

Here \(\mu(T)\) is the least cardinality of a finite set of named constants whose expansion makes \(T\) ultrahomogeneous; \(\mu(T)=\infty\) if no finite exceptional set exists. Thus the exact finite number of exceptional constants records the size of the complement, not merely whether that complement is finite.

## Assumptions and scope

A rooted predecessor tree is a structure \((T,f)\) with a unique root \(r\), \(f(r)=r\), and each other node mapped by \(f\) to its parent. Height is measured from the root, whose height is zero. All trees in the result have height at most three. The term “ultrahomogeneous” means that every isomorphism between finitely generated substructures in the language containing \(f\) and the named constants extends to an automorphism.

For a level-one node \(x\), let \(C(x)=\{y:f(y)=x\}\), and for each \(y\in C(x)\) let \(d(y)=|\{z:f(z)=y\}|\in\mathbb N\cup\{\omega\}\). Define the local defect

\[
\delta(x)=\min_k |\{y\in C(x):d(y)\ne k\}|,
\]

where the minimum is over \(k\in\mathbb N\cup\{\omega\}\) and is set to \(\infty\) if no finite mismatch set exists. Put \(R=\{x:\delta(x)=0\}\). For \(x\in R\), define its branch shape \(\tau(x)=(h(x),k(x))\), where \(h(x)=|C(x)|\), \(k(x)\) is the common value of \(d(y)\) when \(h(x)>0\), and \(k(x)=0\) when \(h(x)=0\). Let

\[
\varepsilon(T)=\min_{(h,k)\in(\mathbb N\cup\{\omega\})^2}
|\{x\in R:\tau(x)\ne(h,k)\}|,
\]

with \(\varepsilon(T)=0\) if \(R\) is empty and \(\varepsilon(T)=\infty\) if no shape leaves only finitely many nodes of \(R\) outside it.

## Proof

First establish the parameter formula

\[
\mu(T)=\sum_{x\text{ at level }1}\delta(x)+\varepsilon(T).
\]

For a level-one node \(x\), each child \(y\) roots a star, since the tree has height at most three. In an expansion by constants, every child branch containing a named node is anchored: naming a descendant fixes its ancestors because the predecessor function is in the language. All unanchored child branches of \(x\) must therefore have the same number of leaves. At least \(\delta(x)\) distinct child branches must be anchored, and this number is attained by choosing a most frequent child-degree \(k\) and naming each child whose degree differs from \(k\). If no degree has only finitely many exceptions, no finite set can suffice at that node.

After these local defects are anchored, precisely the regular level-one branches with a common shape may remain unanchored. Every regular branch of a different shape needs at least one named node in its subtree; these subtrees are disjoint. The minimum number of such additional anchors is exactly \(\varepsilon(T)\). Conversely, choose a shape attaining \(\varepsilon(T)\), anchor the \(\delta(x)\) exceptional child branches at each node with positive defect, and name each regular root branch of a different shape. All unanchored root branches then have the same shape, and all unanchored child branches within anchored nodes have the same leaf count. Any finite partial isomorphism fixing the constants extends by matching these equal branches and permuting leaves. This proves the formula, including the value \(\infty\) when either term is infinite.

Now construct \(T_W\) uniformly from a stage enumeration \((W_s)_{s\in\omega}\) of \(W\). Its nodes are a root \(r\), nodes \(x_n\) for \(n\in\omega\), and nodes \(y_{n,s},z_{n,s}\) for \(n,s\in\omega\). Let \(e(n,s)\) mean that stage \(s\) is the first stage at which \(n\) enters \(W_s\). For each \(n\), let \(\pi_n(s)\) be the \(s\)-th stage at which \(e(n,t)\) is false. This is a total computable function: at most one stage is excluded, so a finite search always finds the requested stage, uniformly in \(n,s\) and the c.e. index.

Set

\[
f(r)=r,\qquad f(x_n)=r,\qquad
f(y_{n,s})=\begin{cases}x_n,&e(n,s),\\r,&\neg e(n,s),\end{cases}
\qquad f(z_{n,s})=y_{n,\pi_n(s)}.
\]

The map \(\pi_n\) bijects all stage indices onto the stages that are not first-entry stages. Therefore every non-entry node \(y_{n,t}\) is a root child with exactly one child \(z_{n,s}\), while an entry-stage node \(y_{n,s}\) is a child of \(x_n\) and has no children. Every node reaches \(r\), and the height is at most three.

If \(n\in W\), exactly one node \(y_{n,s}\) is a child of \(x_n\), and that child has no children; hence \(x_n\) has shape \((1,0)\). If \(n\notin W\), the node \(x_n\) has no children and has shape \((0,0)\). Every non-entry node \(y_{n,s}\) is a root child with one child \(z\) of degree zero, so it has shape \((1,0)\). There are infinitely many such padding branches, because each \(n\) has at most one first-entry stage and infinitely many non-entry stages. All level-one nodes have local defect zero. Consequently, shape \((1,0)\) occurs infinitely often, while shape \((0,0)\) occurs exactly \(|\omega\setminus W|\) times. The parameter formula gives the asserted value of \(\mu(T_W)\): it is the finite complement size when that size is finite, and is infinite when both shapes occur infinitely often. The construction and the count are exact; no finite-stage approximation is being used as a proof of infinitude.

## Verification

The parent function is total and computable: evaluating \(f(y_{n,s})\) checks a finite-stage first-entry event, while evaluating \(f(z_{n,s})\) computes the requested non-entry stage by a terminating finite search. The tree has no nodes above level three. The only root-branch shapes are \((1,0)\) and \((0,0)\); the former occurs infinitely often in every instance, and the latter occurs once for each nonmember of \(W\). The minimum-cost formula is proved above by matching the necessary branch anchors with an explicit sufficient set. No claim is made about the computational complexity of finding \(\mu(T)\) from an arbitrary presentation.

## Relationship to prior work

Adams and Cenzer characterize weakly ultrahomogeneous predecessor trees by a finite-subtree criterion and give explicit branching conditions for trees of height at most three. Their results establish the qualitative distinction between having a finite exceptional set and having none. The present statement adds an explicit uniform construction whose minimum number of constants is exactly the finite complement size of an arbitrary computably enumerable set. It does not claim a new characterization of weak ultrahomogeneity, nor does it claim that the qualitative index-set complexity is new.

## Limitations

The height bound of three and the predecessor-function language are essential to this proof: the local child branches are stars, so their isomorphism types are determined by leaf counts. The formula is not asserted for trees of greater height or for the relational partial-order presentation, where the substructure notion differs. The result encodes the finite complement size but does not classify all index sets for exact values of \(\mu\).

## References

- F. Adams and D. Cenzer, “Computability and Categoricity of Weakly Ultrahomogeneous Structures,” arXiv:1608.01254v1, first posted 2016-08-03, especially Theorem 7.11 and Proposition 7.13. https://arxiv.org/abs/1608.01254
- F. Adams and D. Cenzer, “Computability and Categoricity of Weakly Ultrahomogeneous Structures,” *Computability* 6(4) (2017), 365–389. DOI: https://doi.org/10.3233/COM-170070
