# Action-blind conjugacy-class graphs of abelian-by-cyclic Frobenius groups

## Finding

Let
\[
G=K\rtimes H
\]
be a finite Frobenius group with nontrivial abelian kernel \(K\) and cyclic complement
\[
H=\langle h\rangle\cong C_m,
\qquad m>1.
\]
Put
\[
k=|K|,
\qquad
A=\frac{k-1}{m}.
\]

On the noncentral conjugacy classes, let \(\Gamma_{\mathrm{CCC}}(G)\), \(\Gamma_{\mathrm{NCC}}(G)\), and \(\Gamma_{\mathrm{SCC}}(G)\) be the commuting, nilpotent, and solvable conjugacy class graphs. Then
\[
\boxed{
\Gamma_{\mathrm{CCC}}(G)
\cong
\Gamma_{\mathrm{NCC}}(G)
\cong
K_A\sqcup K_{m-1},
}
\]
and
\[
\boxed{
\Gamma_{\mathrm{SCC}}(G)
\cong
K_{A+m-1}.
}
\]

Thus the three graphs depend only on \((|K|,m)\), not on the fixed-point-free action of the complement.

This action blindness gives uniform nonisomorphic collisions. Let \(p\equiv1\pmod 3\) be prime and choose \(\omega\in\mathbf F_p^\times\) of order \(3\). Define
\[
G_{\mathrm{sc}}
=
\mathbf F_p^2\rtimes_{\omega I} C_3
\]
and
\[
G_{\mathrm{sp}}
=
\mathbf F_p^2\rtimes_{\operatorname{diag}(\omega,\omega^{-1})} C_3.
\]
Both actions are fixed-point-free, but the groups are nonisomorphic. Nevertheless
\[
\Gamma_{\mathrm{CCC}}(G_{\mathrm{sc}})
\cong
\Gamma_{\mathrm{CCC}}(G_{\mathrm{sp}})
\cong
K_{(p^2-1)/3}\sqcup K_2,
\]
\[
\Gamma_{\mathrm{NCC}}(G_{\mathrm{sc}})
\cong
\Gamma_{\mathrm{NCC}}(G_{\mathrm{sp}})
\cong
K_{(p^2-1)/3}\sqcup K_2,
\]
and
\[
\Gamma_{\mathrm{SCC}}(G_{\mathrm{sc}})
\cong
\Gamma_{\mathrm{SCC}}(G_{\mathrm{sp}})
\cong
K_{(p^2-1)/3+2}.
\]

For example, at \(p=7\), both commuting and nilpotent graphs are
\[
K_{16}\sqcup K_2,
\]
while the solvable graph is \(K_{18}\). The two groups are distinguished group-theoretically by their normal subgroups of order \(7\): the scalar action fixes all eight projective lines, whereas the split action fixes exactly its two eigenspaces.

## Assumptions and scope

A Frobenius group \(K\rtimes H\) is used in its standard finite-group sense: every nonidentity element of \(H\) fixes no nonidentity element of \(K\). In particular, \((|K|,|H|)=1\).

The graph convention is the one used in the recent conjugacy-class-graph literature: vertices are the noncentral conjugacy classes. Two distinct classes are adjacent in the commuting graph when some representatives generate an abelian subgroup; in the nilpotent or solvable graph, “abelian” is replaced respectively by “nilpotent” or “solvable”.

The kernel is assumed abelian and the complement cyclic. Neither irreducibility nor elementary abelianity of the kernel is required for the structural graph formula. Elementary abelian kernels are used only for the explicit nonisomorphic collision family.

## Proof

First,
\[
Z(G)=1.
\]
A central element of \(K\) would be fixed by \(H\), so fixed-point-freeness forces it to be the identity. An element outside \(K\) has nontrivial image in \(H\) and cannot centralize \(K\), again by fixed-point-freeness.

Let \(1\ne x\in K\). Since \(K\) is abelian, conjugation by \(K\) fixes \(x\), while the complement orbit \(x^H\) has size \(m\). Hence every nontrivial kernel conjugacy class has size \(m\), and there are exactly
\[
A=\frac{|K|-1}{m}
\]
such classes.

Now fix \(1\le j<m\). The endomorphism
\[
1-h^j:K\longrightarrow K
\]
is injective because \(h^j\) has no nontrivial fixed point. Since \(K\) is finite, it is bijective. Conjugating \(h^j\) by elements of \(K\) therefore runs through the whole coset
\[
Kh^j.
\]
Thus \(Kh^j\) is one conjugacy class. Distinct values of \(j\) give distinct classes because they have distinct images in \(G/K\cong C_m\). Hence there are \(m-1\) noncentral classes outside the kernel.

Any two kernel classes are adjacent in all three graphs because representatives lie in the abelian group \(K\). Any two outside classes are adjacent in all three graphs because they contain the commuting representatives \(h^i\) and \(h^j\) in the cyclic complement.

There is no commuting edge between a kernel class and an outside class. Indeed, if \(1\ne x\in K\) commuted with an element \(y\in Kh^j\), then conjugation by \(y\) on \(K\) would fix \(x\). Its action on \(K\) is the same as the action of \(h^j\), contradicting fixed-point-freeness.

There is also no nilpotent edge between a kernel class and an outside class. Suppose
\[
L=\langle x,y\rangle
\]
were nilpotent with \(1\ne x\in K\) and \(y\in Kh^j\). The subgroup
\[
N=L\cap K
\]
is nontrivial and is a Hall subgroup for the primes dividing \(|K|\), because \(L/N\) embeds in the cyclic group \(H\) and \((|K|,|H|)=1\). In a finite nilpotent group the Hall subgroups of coprime order commute. Writing \(y\) as a product of its \(N\)-part and its complementary Hall part would therefore make \(y\) centralize \(N\), and in particular \(x\), contradicting the preceding paragraph. Consequently
\[
\Gamma_{\mathrm{CCC}}(G)
=
\Gamma_{\mathrm{NCC}}(G)

after identifying their common vertex set, and both are exactly
\[
K_A\sqcup K_{m-1}.
\]

Finally, \(G\) is metabelian because both \(K\) and \(H\) are abelian. Every subgroup generated by two representatives is therefore solvable. Thus every pair of distinct noncentral conjugacy classes is adjacent in \(\Gamma_{\mathrm{SCC}}(G)\), giving
\[
K_{A+m-1}.
\]

For the collision family, both matrices \(\omega I\) and \(\operatorname{diag}(\omega,\omega^{-1})\) have order \(3\), and neither they nor their squares have eigenvalue \(1\). Hence both semidirect products are Frobenius groups. Also
\[
[G,G]=\mathbf F_p^2
\]
because \(h-1\) is invertible. The derived subgroup is characteristic, so an isomorphism must preserve the induced \(C_3\)-module structure up to inversion of the complement generator. In the scalar-action group every one-dimensional subspace is invariant, giving \(p+1\) normal subgroups of order \(p\). In the split-action group only the two eigenspaces are invariant. Therefore the groups are nonisomorphic, while the graph formulas above show that all three conjugacy-class graphs coincide.

## Verification

The included verifier constructs the two semidirect products for \(p=7\) and \(p=13\) directly from their multiplication laws.

For each action it independently enumerates every conjugacy class and then computes commuting-conjugacy-class adjacency by checking representatives. It verifies that the two connected components are complete and have sizes
\[
\frac{p^2-1}{3}
\quad\text{and}\quad
2.
\]
For every mixed kernel/outside pair of representatives it verifies orders \(p\) and \(3\) and verifies noncommutation; this excludes nilpotence of the generated subgroup because elements of coprime order commute in a finite nilpotent group. It also checks that commutators lie in the abelian kernel, confirming the metabelian solvability used for the complete solvable graph.

Finally, it counts invariant projective lines. The scalar action has \(p+1\), while the split action has exactly two, certifying the stated nonisomorphism invariant.

The verifier returns `VERIFY_OK`.

Finite checks are not used to prove the universal theorem.

## Relationship to prior work

Cameron, Jannat, Nath, and Sharafdini survey commuting, nilpotent, and solvable conjugacy class graphs and pose the problem of determining which finite groups are uniquely determined by these graphs. The theorem above gives a uniform obstruction: even the triple of graphs can be insensitive to the complement action.

Herzog, Longobardi, and Maj prove a broader connectivity theorem for finite solvable groups. Their classification of the disconnected commuting conjugacy class graph includes Frobenius groups and establishes the structural source of disconnection, but it does not state the exact two-clique decomposition above, the vertex counts, equality with the nilpotent graph, or action blindness.

Ray, Arora, and Ma investigate forbidden induced subgraphs for commuting and nilpotent conjugacy class graphs. Their stated families include EPPO, nilpotent, dihedral, dicyclic, and generalized dihedral groups. Those results constrain graph types in overlapping special cases but do not supply the arbitrary abelian-kernel cyclic-complement formula or the nonisomorphic action-collision family stated here.

Mohammadian and Erfanian study connected components and diameters of nilpotent conjugacy class graphs. Only the public abstract was available for direct comparison here, so possible overlap hidden in the full article is retained as a bibliographic risk rather than treated as evidence of noncoverage.

Targeted searches using Frobenius, abelian kernel, cyclic complement, commuting conjugacy class graph, nilpotent conjugacy class graph, two complete components, and action-module terminology did not locate the displayed theorem.

## Limitations

The exact graph formula uses both hypotheses: the kernel is abelian and the complement is cyclic. With a nonabelian kernel, kernel conjugacy classes need not form a clique; with a noncyclic complement, the outside classes need not form a clique.

The result gives a family of groups not uniquely determined by the graphs; it does not classify all finite groups that are or are not graph-determined.

The 2009 commuting-graph connectivity theorem already places Frobenius groups in the disconnected regime. The new content is the exact graph isomorphism type under the abelian/cyclic hypotheses, its equality with the nilpotent graph, the complete solvable graph, and the action-blind collision consequence.

A full-text comparison with the 2017 nilpotent-conjugacy-class article was unavailable. That access limitation is a residual originality risk.

## References

1. P. J. Cameron, F. E. Jannat, R. K. Nath, and R. Sharafdini, “A survey on conjugacy class graphs of groups,” arXiv:2403.09423v1, first public version 14 March 2024; *Expositiones Mathematicae* 42 (2024), 125585, DOI 10.1016/j.exmath.2024.125585.
2. M. Herzog, P. Longobardi, and M. Maj, “On a commuting graph on conjugacy classes of groups,” *Communications in Algebra* 37 (2009), 3369–3387, DOI 10.1080/00927870802502779.
3. P. Ray, S. Arora, and X. Ma, “Forbidden subgraphs on conjugacy class graphs of groups,” arXiv:2406.01305v1, first public version 3 June 2024.
4. A. Mohammadian and A. Erfanian, “On the nilpotent conjugacy class graph of groups,” *Note di Matematica* 37 (2017), no. 2, 77–89, DOI 10.1285/i15900932v37n2p77.
