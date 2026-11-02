# A leaf erases the online-shattering excess of rooted two-edge arms

## Finding
For integers \(t\ge1\) and \(s\ge0\), let \(P_{t,s}\) be a finite poset with a least point \(r\), precisely \(t\) mutually incomparable two-step arms \(r<a_i<b_i\), and \(s\) mutually incomparable single-step arms \(r<c_j\). There are no comparabilities between distinct arms. Let \(\mathcal J_{t,s}\) comprise all downsets, including \(\varnothing\), interpreted as Boolean hypotheses on the points of the poset.

The exact hypothesis count and the fixed and adaptive shattering dimensions are
\[
|\mathcal J_{t,s}|=1+3^t2^s,\qquad
\operatorname{VCdim}(\mathcal J_{t,s})=t+s,
\]
\[
\operatorname{Ldim}(\mathcal J_{t,s})=
\begin{cases}
t+1,&s=0,\\
t+s,&s\ge1.
\end{cases}
\]
In particular, the connected height-three tree with \(t\) two-step arms has one round of adaptive excess for every \(t\ge1\). Appending one single-step arm increases its VC dimension but does *not* increase its Littlestone dimension; the excess vanishes.

## Assumptions and scope
All posets and concept classes are finite. A hypothesis is a downset \(I\subseteq P_{t,s}\); a query at a point \(x\) returns \(1\) exactly when \(x\in I\). VC dimension means shattering a fixed set of distinct points. Littlestone dimension means the depth of a complete binary query tree whose every root-to-leaf answer sequence has at least one realizing ideal. The query at a tree node can depend on earlier answers. These are *not* the usual order dimension of a poset, its Boolean dimension, or its Dushnik--Miller dimension.

A two-step arm contains two elements above \(r\); a single-step arm contains one. For the inductive proof only, \(P_{0,s}\) denotes the root together with \(s\) leaves, so \(P_{0,0}\) is a singleton poset.

## Proof
**1. The hypothesis space and VC dimension.** Every nonempty ideal contains \(r\). Conditional on containing it, each two-step arm has exactly three possible initial segments: neither point, its lower point only, or both. Each single-step arm has two options. They can be selected independently, giving \(1+3^t2^s\) ideals after including the empty ideal. The upper endpoints \(b_i\) and the leaves \(c_j\) form an antichain of size \(t+s\), and every zero-one labeling of this antichain extends to a downset. Conversely, two comparable points cannot both belong to a shattered support because the label \(1\) at the upper point and \(0\) at its lower point cannot occur. The width is \(t+s\) for \(t\ge1\), proving the VC formula.

**2. Product lemma.** Suppose the query ground sets of two nonempty finite Boolean concept classes are disjoint and the class consists of all independent choices of one hypothesis in each class. Then the Littlestone dimensions add. One inequality is obtained by concatenating complete query trees, with the first tree independent of the second. For the reverse inequality, induct on the number of distinct product hypotheses, using the exact recurrence \(L(\mathcal H)=\max_x\{1+\min(L(\mathcal H_{x=0}),L(\mathcal H_{x=1}))\}\) over nontrivial splits (and rank zero for singleton classes). A split on a query in the first factor replaces only that factor by one of its two restrictions; by induction its value is at most \(L(\mathcal H_1)+L(\mathcal H_2)\), since the displayed recurrence for the first factor bounds \(1+\min(L(\mathcal H_{1,x=0}),L(\mathcal H_{1,x=1}))\) by \(L(\mathcal H_1)\). The other factor is symmetric.

A three-state chain of nested membership answers has Littlestone dimension one: it has a nontrivial query but has fewer than four hypotheses, precluding depth two. A two-state factor also has dimension one. Therefore the subfamily of all **nonempty** ideals has Littlestone dimension exactly \(d=t+s\). Adding one further hypothesis can raise the dimension by at most one: any nontrivial first split has at least one branch avoiding that additional hypothesis, and that branch is a restriction of the product subfamily of rank at most \(d\). Thus \(L(\mathcal J_{t,s})\le d+1\).

**3. Exact induction.** We show the auxiliary formulas \(L(\mathcal J_{0,0})=1\) and \(L(\mathcal J_{0,s})=s\) for \(s\ge1\), and for \(t\ge1\):
\[
L(\mathcal J_{t,s})=\begin{cases}t+1,&s=0,\\t+s,&s\ge1.\end{cases}
\]
The singleton poset has two ideals and hence rank one. For \(t=0,s\ge1\), the product of the \(s\) leaves, restricted to nonempty ideals, gives lower bound \(s\). A root query leaves a singleton negative branch; a leaf query has a positive branch of rank \(s-1\), because it excludes the empty ideal and fixes that leaf. Thus no first query has both branches of rank \(s\); the exact recurrence gives upper bound \(s\).

Now fix \(t\ge1\), put \(d=t+s\), and assume the formulas for smaller \(t\). The nonempty-ideal product gives \(L\ge d\). A query at \(r\) has a singleton negative branch. A query at \(b_i\), or at a leaf \(c_j\), has a positive branch in which one whole coordinate is fixed, leaving product rank \(d-1\); it therefore cannot yield rank \(d+1\). A query at a lower arm point \(a_i\) has a positive branch with a binary choice of \(b_i\) and all other \(d-1\) coordinates unchanged, so its rank is exactly \(d\). The negative branch is isomorphic, as a membership-query concept class, to \(\mathcal J_{t-1,s}\): the queried arm is forced empty and may be deleted.

If \(s\ge1\), the induction hypothesis says that negative branch has rank \((t-1)+s=d-1\); hence no first query has two branches of rank \(d\). Therefore \(L=d\). If \(s=0\), the negative branch has rank \(t\), including the base case \(t-1=0\), while the positive branch also has rank \(t\). Querying \(a_i\) at the root of a mistake tree therefore realizes rank at least \(t+1\). The one-extra-hypothesis upper bound proves equality. This completes the induction.

## Verification
Two standalone, differently encoded exhaustive recurrences are supplied. `verify_poset.py` enumerates actual downsets of the explicitly constructed posets and computes VC dimension by all query supports and Littlestone dimension by full version-space branching. `verify_product.py` instead enumerates abstract coordinate truth vectors (including the exceptional all-zero hypothesis) and computes the exact mistake-tree rank without using downset enumeration. Both independently check every parameter pair \(0\le t,s\le4\) satisfying \(3^t2^s\le175\), including the auxiliary \(t=0\) cases. There are 20 parameter pairs in each check, and all pass.

For instance, \((t,s)=(2,0)\) yields \(10\) ideals with dimensions \((2,3)\), while \((2,1)\) yields \(19\) ideals with dimensions \((3,3)\); similarly \((3,0)\) gives \(28\) ideals and \((3,4)\), while \((3,1)\) gives \(55\) ideals and \((4,4)\). To reproduce, run `python3 verify_poset.py` and `python3 verify_product.py` from the directory containing the three files. No third-party packages are required.

## Relationship to prior work
Thicket/Littlestone dimension and its complete binary mistake-tree recurrence are standard (Bhaskar, 2017; Walker, 2022). The standard VC dimension of the full downset class of a finite poset is its width. General height-and-width bounds and the maximum possible adaptive dimension for a given height and width are also known in related work. None of these facts alone determines the exact dimension of this connected, height-three two-parameter family, particularly the discontinuity when a single new leaf is appended. The new assertion is the exact two-parameter online/static classification above, not the basic recurrence or additivity lemma.

## Limitations
This theorem concerns one least element with disjoint branches of length one or two only. It is not a formula for all rooted forests or arbitrary branch lengths, nor a characterization of all posets with no adaptive/static gap. Historical priority under the language of Horn implication systems or thicket ranks remains a possible risk. Computational checks are finite corroboration; the infinite parameter range is justified by the displayed induction.

## References
1. Siddharth Bhaskar, *Thicket Density*, arXiv:1702.03956, originally submitted 13 February 2017. https://arxiv.org/abs/1702.03956
2. Roland Walker, *Tree Dimension and the Sauer--Shelah Dichotomy*, arXiv:2203.12211, originally submitted 23 March 2022. https://arxiv.org/abs/2203.12211
