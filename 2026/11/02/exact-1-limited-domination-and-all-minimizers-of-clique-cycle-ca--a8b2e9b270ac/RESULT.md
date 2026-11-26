# Minimum one-limited dominating sets of clique–cycle products at lengths not divisible by four

## Finding
Let \(m\ge3\), \(n\ge5\), and \(4\nmid n\). For the labelled Cartesian product \(G=K_m\square C_n\), define
\[h=2\lfloor n/4\rfloor+\mathbf1_{n\equiv3\ (\mathrm{mod}\ 4)}.\]
The minimum size of a 1-limited dominating set is \(m(n-h)\). All minima are obtained by omitting \(h\) whole clique columns whose cyclic omission indicator avoids \(111\) and \(101\), except that when \((m,n)=(3,6)\) there are also three minima obtained by omitting one entire row \(\{i\}\times C_6\). On the labelled graph the number of minima is
\[
\begin{cases}
n,&n\equiv1,3\pmod4,\\
n^2/4,&n\equiv2\pmod4
\end{cases}
+3\mathbf1_{(m,n)=(3,6)}.
\]

## Assumptions and scope
A set \(D\) is 1-limited dominating if each vertex outside it has a neighbor in it, and each vertex in it has at most one neighbor outside it. All graphs are finite, undirected and simple. Columns are the copies of \(K_m\) indexed by the vertices of \(C_n\); rows are the copies of \(C_n\) indexed by the vertices of \(K_m\). Counts do not quotient by rotations or automorphisms.

## Proof
Write \(S=V(G)\setminus D\). Every column is full (all omitted), empty (none omitted), or singleton (one omitted): a selected vertex of a partially omitted clique is adjacent to all omissions in that clique. Three full columns in a row would prevent domination in the middle column. A selected vertex in a non-full column between two full columns would have two omitted cyclic neighbors. Thus if there are \(b\ge1\) full blocks of total length \(f\), their lengths lie in \(\{1,2\}\) and their separating gaps \(g_1,\ldots,g_b\) each have length at least two. In particular \(f\le2b\) and \(n\ge f+2b\ge2f\). If \(n=4q+2\), then \(f=2q+1\) would require \(b\ge q+1\), contradicting \(n\ge f+2b\). In all cases \(f\le h\).

No singleton can be adjacent to a full column, as its selected vertices would have both a clique omission and a cyclic omission as neighbors. Nor can one be at distance two: the intervening column must be empty, and in the row of the singleton's omission its selected vertex has two omitted cyclic neighbors. Thus the number of singleton columns is at most \(\sum_i(g_i-4)_+\). If \(e_i=g_i-2\ge0\), then \(\sum_i(e_i-2)_+\le(\sum_i e_i-2)_+\) (if any summands are positive, at least one subtraction of two is made). Consequently
\[
|S|\le mf+(n-f-2b-2)_+\le mf+(n-2f-2)_+\le mh-(m-2)(h-f).
\]
The last inequality uses \(n-2h\le2\). If \(f<h\) the bound is strict; if \(f=h\) there can be no singleton. Conversely, every allowed cyclic word with \(h\) full columns gives a feasible omission set: \(111\) would leave a full column undominated and \(101\) would put two omissions next to a selected vertex; avoiding the two words is sufficient when all non-full columns are empty.

If there are no full columns then \(|S|\le n\). By the formula for \(h\), \(n\le mh\), with equality in this scope exactly at \((3,6)\): for \(m=3\), \(3h-n=2q-r+3\mathbf1_{r=3}\) with \(n=4q+r\), and for \(m>3\) it increases strictly. At equality every column omits one vertex. Consecutive omissions must be in the same row, or a selected vertex would see both a clique omission and a cyclic omission. Each of the three whole rows at \((3,6)\) is feasible, since each selected vertex then has just one omitted clique neighbor and every omitted vertex has selected clique neighbors.

It remains to count the full-column words and show attainment. For given \((b,f)\) the count is
\[
\frac nb\binom{b}{f-b}\binom{n-f-b-1}{b-1}.
\]
Choose the length-two blocks, distribute the extra gap length \(n-f-2b\) over the \(b\) ordered gaps, and place the first block at one of the \(n\) labelled positions. Each word is obtained once for each of its \(b\) choices of first block. If \(n=4q+1\) then \(f=2q\) requires \(b=q\) and the count is \(n\). If \(n=4q+2\) then \(f=2q\) allows \(b=q\) and \(b=q+1\), giving counts \(n(q+1)/2\) and \(nq/2\), totaling \(n^2/4\). If \(n=4q+3\) then \(f=2q+1\) requires \(b=q+1\) and the count is \(n\). These positive counts prove attainment and the labelled formula.

## Relationship to prior work
The cycle value \(n-h\) is given by Božović et al. [1, Cor. 8]; Tepeh [2, Thm. 7] gives the general Cartesian-product upper bound that becomes \(m(n-h)\). The underlying cyclic words also complement the minimum total dominating sets of a cycle: each cycle vertex must have a nonomitted neighbor, equivalent to avoiding \(111\) and \(101\). Their count here is just the base-cycle count, not a separate claim of originality. The product result proves optimality and that all minima lift these cycle patterns, apart from the listed row exception.

The \(n=3\) slice is covered by the rook-graph classification [3], since \(C_3\cong K_3\). For \(4\mid n\), the general lower and upper bounds coincide at \(mn/2\); equality forces each vertex on either side to have exactly one neighbor across the cut, so a clique of size \(m\ge3\) cannot be split. Then the full-column word consists of repeated \(1100\), with four labelled placements. Neither slice is part of the finding. Circular ladders [4] have clique size two and different minima.

The companion `verify.cpp` checks some finite examples directly from graph adjacency and others by a local column dynamic program. It includes examples outside the narrowed scope as contextual checks. The preceding proof, not the finite tests, supplies the universal classification.

1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević and A. Tepeh, *On \(k\)-limited domination in graphs*, [DOI:10.1007/s40314-026-03902-2](https://doi.org/10.1007/s40314-026-03902-2).
2. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, [arXiv:2606.22428v2](https://arxiv.org/abs/2606.22428v2).
3. *Exact limited domination and low-capacity rigidity for rectangular rook graphs*, [record](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-exact-limited-domination-and-low-capacity-rigidity-for-rectangul--3f6b93fa9eef).
4. *Complete one-limited domination polynomial of circular ladders*, [record](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-complete-one-limited-domination-polynomial-of-circular-ladders--4d83cdec888e).
