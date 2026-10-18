# Steiner design base polytopes have hypersimplex asymmetry except for the Fano plane

## Finding

Let \(\mathcal D\) be any nontrivial Steiner system \(S(2,k,n)\) with \(k\ge3\), \(n>k\): a family \(\mathcal B\) of \(k\)-element blocks on an \(n\)-element set \(E\), each pair of distinct points occurring in exactly one block. Give \(E\) the rank-three matroid whose bases are the three-element subsets not contained in any block. Let
\[
P_{\mathcal D}=\operatorname{conv}\{\mathbf1_T:|T|=3,\ T\nsubseteq B\text{ for every }B\in\mathcal B\}\subset\{x\in\mathbb R^E:x(E)=3\}.
\]
Define Minkowski asymmetry by \(s(P)=\min_{c\in\operatorname{relint}P}\inf\{s\ge1:c-(P-c)/s\subseteq P\}\). Then
\[
\boxed{s(P_{\mathcal D})=\begin{cases}9/5,&(n,k)=(7,3),\\[3pt](n-3)/3,&\text{otherwise.}\end{cases}}
\]
In every case the **unique** minimizing center is
\[
\boxed{c_*=\frac3n\mathbf1_E.}
\]
The exceptional parameters \((7,3)\) give the unique seven-point Steiner triple system, the Fano plane. Every other nontrivial Steiner \(2\)-design has exactly the asymmetry of the rank-three hypersimplex on the same ground set. The conclusion holds without assuming design automorphisms, representability, or uniqueness of the design with its parameters.

## Assumptions and scope

The ground set is finite; \(k\) and \(n\) are integers, \(k\ge3\), and a nontrivial \(S(2,k,n)\) actually exists. No existence claim is made for arbitrary admissible integers. The polytope is measured intrinsically in its affine hull \(x(E)=3\), of dimension \(n-1\); Minkowski asymmetry is affine invariant and does not depend on a Euclidean metric.

Write \(r\) for the number of blocks through a point and \(b\) for the number of blocks. Pair counting gives \(r(k-1)=n-1\) and \(bk=nr\). If \(B\) is any block and \(a\notin B\), the \(k\) distinct blocks through the pairs \(\{a,u\}\) for \(u\in B\) show \(r\ge k\), hence
\[
n\ge k(k-1)+1>2k\quad\text{and}\quad n\ge7.
\]
These inequalities ensure that the complement of every block contains a noncollinear triple.

## Proof

**Step 1: Matroid and exact halfspaces.** The stated three-element bases satisfy basis exchange: if \(T,T'\) are bases and \(i\in T\setminus T'\), the two elements of \(T\setminus\{i\}\) determine a unique block \(L\). If every \(j\in T'\setminus T\) lay in \(L\), then all of \(T'\) would lie in \(L\), contrary to its being a basis. Thus some exchange is again a base. The rank function is \(0\) on the empty set, \(1\) on singletons, \(2\) on subsets of a block having at least two points, and \(3\) on all other sets of at least three points. By the matroid base-polytope rank-inequality theorem (or its greedy support-function proof), this rank function yields precisely
\[
P_{\mathcal D}=\{x\in\mathbb R^E:x(E)=3,\ 0\le x_i\le1\ (i\in E),\ x(B)\le2\ (B\in\mathcal B)\}.
\]
Every displayed one-coordinate functional has minimum \(0\) and maximum \(1\) on the bases. For every block \(B\), the block-sum functional has minimum \(0\) and maximum \(2\): two points of \(B\) plus any point outside \(B\) attain \(2\); and \(n-k>k\) ensures a noncollinear triple entirely outside \(B\), attaining \(0\). In particular \(3\mathbf1_E/n\) satisfies all the halfspaces strictly relative to \(x(E)=3\), so the claimed affine dimension is \(n-1\).

**Step 2: Reflected containment inequalities.** Fix \(s\ge1\) and \(c(E)=3\), and write \(y=c+(c-x)/s\). Applying the exact support extrema from Step 1, the containment \(c-(P_{\mathcal D}-c)/s\subseteq P_{\mathcal D}\) is **equivalent** to
\[
\frac1{s+1}\le c_i\le\frac{s}{s+1}\quad(i\in E),\qquad
\frac2{s+1}\le c(B)\le\frac{2s}{s+1}\quad(B\in\mathcal B).
\]
Summing the coordinate bounds and using \(c(E)=3\) gives
\[
s\ge\frac{n-3}{3},\qquad s\ge\frac3{n-3}.
\]
Summing the block bounds, using \(\sum_{B\in\mathcal B}c(B)=r c(E)=3r\) and \(bk=nr\), gives
\[
s\ge\frac{3k}{2n-3k},\qquad s\ge\frac{2n-3k}{3k}.
\]
All denominators are positive because \(n>2k\). Conversely, the uniform candidate \(c_*=(3/n)\mathbf1_E\) satisfies every coordinate and block inequality at the maximum of these four lower bounds. Therefore
\[
s(P_{\mathcal D})=\max\left\{\frac{n-3}{3},\frac3{n-3},\frac{3k}{2n-3k},\frac{2n-3k}{3k}\right\}.
\]
This equality gives a global lower bound against **every** possible center, not merely an assumption of symmetric optimality.

**Step 3: The sole exception.** Since \(n\ge7\), the first displayed ratio dominates \(3/(n-3)\). Since \(k\ge3\), it also dominates \((2n-3k)/(3k)\), as \(k(n-3)\ge2n-3k\) is equivalent to \((k-2)n\ge0\).

For \(k=3\), the replication identity makes \(n\) odd and \(n\ge7\). If \(n=7\), the block upper-bound ratio is \(9/5>4/3\). For \(n\ge9\), the inequality \((n-3)(2n-9)\ge27\) shows that \((n-3)/3\) dominates it. For \(k\ge4\), the design lower bound implies \(n\ge3k+1\); hence
\[
(n-3)(2n-3k)\ge(3k-2)(3k+2)=9k^2-4>9k,
\]
so \((n-3)/3\) again dominates \(3k/(2n-3k)\). This proves the announced asymmetry formula.

**Step 4: Uniqueness.** Except at \((n,k)=(7,3)\), optimality at \(s=(n-3)/3\) forces \(c_i\ge3/n\) for every point. Since \(c(E)=3\), all coordinates equal \(3/n\). In the Fano case, optimality at \(s=9/5\) forces \(c(B)\le9/7\) for each of the seven blocks. Their sums total \(3c(E)=9\); the upper bounds total \(7(9/7)=9\), so every block sum equals \(9/7\). Let \(A\) be the seven-by-seven block-point incidence matrix. Each point lies on three blocks and each pair on exactly one, so \(A^{\mathsf T}A=2I+\mathbf1\mathbf1^{\mathsf T}\), an invertible matrix. Thus the block-sum equations have at most one solution; \(c_*=3\mathbf1_E/7\) is that solution. All minimizing centers are therefore unique.

## Verification

Run `python3 verify.py` using Python's standard library. The script constructs five explicit design instances: the Fano projective plane \(\mathrm{PG}(2,2)\), affine plane \(\mathrm{AG}(2,3)\), projective plane \(\mathrm{PG}(2,3)\), Steiner triple system from \(\mathrm{PG}(3,2)\), and projective plane \(\mathrm{PG}(2,5)\). It independently validates the pair-design axiom, replication, exact functional extrema, all reflected-containment inequalities at the claimed center, and the four competing bounds in rational arithmetic. The recorded successful execution inspected \(4629\) noncollinear triples and \(138927\) reflected block inequalities. These are finite sanity checks; the argument in the Proof section covers every existing nontrivial design.

## Relationship to prior work

Hanely and collaborators developed Ehrhart theory of paving matroid base polytopes. Their Section 8 treats Steiner systems and finite projective planes, proving that designs with the same parameters yield the same Ehrhart polynomial and volume. The present result concerns a different, affine-invariant reflection-dilation quantity and supplies its optimal center and an exceptional Fano case. Ferroni and Schröter calculate face vectors of split matroid base polytopes, including \(\mathrm{PG}(2,3)\) in Example 2.9, without determining reflected-containment asymmetry. Neither inspected primary paper states or mathematically implies this exact symmetry classification from its displayed Ehrhart or face-enumeration conclusions.

## Limitations

This theorem requires a nontrivial Steiner \(2\)-design with block size at least three and does not classify arbitrary rank-three matroids. In particular, it does not assert the existence of a design for every parameter pair, nor determine Euclidean John/Löwner ellipsoids. The computation uses the standard rank-inequality characterization of matroid base polytopes. A full independent priority review has not occurred; equivalent results under other terminology, or a stronger general theorem about matroid-base symmetry, remain possible.

## References

1. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez, M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442 (first posted 28 January 2022), especially Section 8 and Propositions 8.3–8.4. https://arxiv.org/abs/2201.12442
2. L. Ferroni and B. Schröter, *Face enumeration for split matroid polytopes*, arXiv:2310.05487 (first posted 9 October 2023), especially Theorem 2.5, Example 2.9 and Corollary 2.10. https://arxiv.org/abs/2310.05487
3. J. Edmonds, *Submodular functions, matroids, and certain polyhedra*, in *Combinatorial Structures and Their Applications* (1970), 69–87; classical matroid base-polytope rank inequalities.
