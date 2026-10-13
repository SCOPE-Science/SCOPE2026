# Minimum zero forcing sets of crown graphs
## Finding
For every integer \(n\ge 3\), let
\[
\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\},
\]
with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). The scalar value
\[
Z(\operatorname{Cr}_n)=2n-4
\]
is known from the tensor-product identity \(\operatorname{Cr}_n\cong P_2\times K_n\) together with the even-path theorem of Benson et al. The additional structural result is that every minimum zero forcing set can be described exactly.

A set \(S\subseteq V(\operatorname{Cr}_n)\) is a minimum zero forcing set if and only if \(|S\cap A|=|S\cap B|=n-2\) and, after defining
\[
I=\{i:a_i\notin S\},\qquad J=\{j:b_j\notin S\},
\]
the two 2-subsets \(I,J\subseteq[n]\) are distinct. Therefore the number of minimum zero forcing sets is
\[
\binom{n}{2}\left(\binom{n}{2}-1\right).
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. Standard zero forcing is used: a blue vertex with exactly one white neighbor forces that neighbor blue. The result concerns \(n\ge3\). No claim is made that the scalar formula for \(Z(\operatorname{Cr}_n)\) is new; the finding is the all-bases classification and exact count.

## Proof
Let \(S\) be any initial blue set. Put
\[
p=|A\setminus S|,\qquad q=|B\setminus S|.
\]
For a blue vertex \(a_i\), the number of white neighbors is
\[
q-\mathbf 1_{\{i\in J\}},
\]
and for a blue vertex \(b_i\) it is
\[
p-\mathbf 1_{\{i\in I\}}.
\]

Suppose \(p+q\ge5\). By symmetry assume \(p\ge3\). Then every blue vertex in \(B\) has at least two white neighbors in \(A\), so no force from \(B\) to \(A\) can occur while \(p\ge3\). Any force that does occur must therefore go from \(A\) to \(B\), which can only decrease \(q\), leaving \(p\) unchanged. Once all possible such forces are exhausted, at least three vertices of \(A\) remain white and no vertex of \(B\) can force. Hence a zero forcing set must satisfy \(p+q\le4\). Thus every zero forcing set has size at least \(2n-4\).

At equality \(p+q=4\), the same argument excludes \(p\ge3\) and, symmetrically, \(q\ge3\). Therefore \(p=q=2\). Write the two omitted-index sets as \(I,J\).

If \(I=J\), every initially blue vertex sees either zero or two white neighbors on the opposite side; in particular no initial force exists. Hence such a set is not zero forcing.

Now suppose \(I\ne J\). Choose \(x\in I\setminus J\) and \(z\in J\setminus I\), and write
\[
I=\{x,y\},\qquad J=\{z,w\}.
\]
Because \(x\notin J\), the vertex \(b_x\) is blue, and among the two white vertices \(a_x,a_y\) it is adjacent only to \(a_y\). Hence \(b_x\) forces \(a_y\). Similarly, \(a_z\) is blue and forces \(b_w\). At that point only \(a_x\) and \(b_z\) are white. The vertex \(a_w\) is blue either initially or because \(w=y\) and \(a_y\) was just forced; since \(w\ne z\), it forces \(b_z\). Finally \(b_z\) forces \(a_x\). Thus every pair of distinct omitted 2-subsets gives a zero forcing set of size \(2n-4\).

The omitted set on side \(A\) can be chosen in \(\binom n2\) ways and the omitted set on side \(B\) can then be any of the remaining \(\binom n2-1\) 2-subsets. This proves the count.

## Verification
A standalone exhaustive checker independently constructs \(\operatorname{Cr}_n\), runs the standard zero forcing process over subsets, and compares the computed minimum sets with the stated characterization for every \(3\le n\le9\). Its replay result is:

`VERIFY_OK n_range=3..9 subset_checks=346739 basis_checks=6671 max_order=18`

The finite computation is a boundary and implementation check only; the proof above establishes the statement for all \(n\ge3\).

## Relationship to prior work
The foundational zero-forcing paper introduced the parameter and establishes its minimum-rank context. More importantly for this family, Benson et al. prove that for even \(t\ge2\) and \(n\ge3\),
\[
Z(P_t\times K_n)=(n-2)t.
\]
Since \(P_2\times K_n\cong\operatorname{Cr}_n\), their theorem already gives \(Z(\operatorname{Cr}_n)=2n-4\). The present finding therefore does not claim the scalar value as new.

The new content is the exact description and enumeration of every minimum set. The relevant graph-product theorem constructs minimum forcing sets but does not state an all-minimum-set classification or a count. The zero forcing polynomial literature supplies the general counting framework, but the inspected family formulas do not cover crown graphs. Searches under the equivalent descriptions “crown graph,” “\(K_{n,n}\) minus a perfect matching,” “\(P_2\times K_n\),” “bipartite double cover of \(K_n\),” and “matching-deleted complete bipartite graph” did not locate a stronger published statement implying this classification.

## Limitations
The claim is only about minimum standard zero forcing sets of crown graphs. It does not determine the full zero forcing polynomial, propagation-time distribution, positive-semidefinite zero forcing, skew zero forcing, or reconfiguration structure. The originality comparison is limited by ordinary literature access and terminology: a specialized catalogue could conceivably encode the same minimum-set classification under another name, although the principal tensor-product and zero-forcing-polynomial sources were inspected directly.

## References
1. AIM Minimum Rank – Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
2. Katherine F. Benson, Daniela Ferrero, Mary Flagg, Veronika Furst, Leslie Hogben, Violeta Vasilevska, and Brian Wissman, “Zero forcing and power domination for graph products,” *Australasian Journal of Combinatorics* 70(2) (2018), 221–235.
3. Kirk Boyer, Boris Brimkov, Sean English, Daniela Ferrero, Ariel Keller, Rachel Kirsch, Michael Phillips, and Carolyn Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910.
