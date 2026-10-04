# Chordality of commuting graphs for \(\mathrm{PSL}_2(q)\)
## Finding
For every prime power \(q\ge 4\), the commuting graph \(\Gamma(\mathrm{PSL}_2(q))\) is chordal if and only if \(q\) is even or \(q=5\).

Thus, within the rank-one simple family \(\mathrm{PSL}_2(q)\), the only chordal commuting graphs are the characteristic-two family together with the isomorphic exceptional case \(\mathrm{PSL}_2(5)\cong \mathrm{PSL}_2(4)\).

## Assumptions and scope
The commuting graph here has all group elements as vertices, with two distinct vertices adjacent exactly when they commute. Chordal means that there is no induced cycle of length at least four.

The statement concerns prime powers \(q\ge 4\). The cases \(q=2,3\), where \(\mathrm{PSL}_2(q)\) is not non-abelian simple, are outside the claim.

For odd \(q\), write
\[
\chi=\begin{cases}
1,&q\equiv 1\pmod 4,\\
-1,&q\equiv 3\pmod 4.
\end{cases}
\]

## Proof
First suppose that \(q\) is even. Every nonidentity element of \(\mathrm{PSL}_2(q)\) has abelian centralizer: an involution has an elementary abelian centralizer of order \(q\), while a noninvolution has cyclic centralizer of order \(q-1\) or \(q+1\). Hence \(\mathrm{PSL}_2(q)\) is a CA-group. In any CA-group, if two noncentral elements commute, then their centralizers coincide, so the commuting graph on noncentral elements is a disjoint union of cliques. Adding the central vertices cannot create an induced cycle of length at least four. Therefore the commuting graph is chordal.

For \(q=5\), \(\mathrm{PSL}_2(5)\cong A_5\). Its nonidentity centralizers are cyclic or Klein four, hence abelian, so the same CA-group argument proves chordality.

Now let \(q>5\) be odd and put \(G=\mathrm{PSL}_2(q)\). Let \(X\) be the unique conjugacy class of involutions and let \(\Delta=\Gamma(G)[X]\) be the induced commuting graph on \(X\).

The standard involution-centralizer structure in \(G\) gives
\[
|G|=\frac{q(q^2-1)}2,\qquad |C_G(t)|=q-\chi
\]
for \(t\in X\), with \(C_G(t)\) dihedral. Consequently
\[
|X|=\frac{|G|}{q-\chi}=\frac{q(q+\chi)}2.
\]
Set \(m=(q-\chi)/2\). Since \(q-\chi\) is divisible by \(4\), \(m\) is even, and \(C_G(t)\) is a dihedral group of order \(2m\). Such a dihedral group has \(m+1\) involutions: its central involution \(t\) and \(m\) reflections. Therefore every vertex of \(\Delta\) has degree
\[
k=m=\frac{q-\chi}{2}.
\]
It follows that, with \(n=|X|\),
\[
|E(\Delta)|=\frac{nk}{2}=\frac{q(q^2-1)}8.
\]

Also \(\omega(\Delta)\le 3\). Indeed, any clique containing \(t\) lies among the involutions of the dihedral group \(C_G(t)\). In a dihedral group with even rotation order, at most two reflections commute with one another in a pair, and together with the central involution this gives at most three pairwise commuting involutions.

We use the elementary chordal-graph bound
\[
|E(H)|\le 2|V(H)|-3
\]
for every chordal graph \(H\) with clique number at most \(3\) and at least two vertices. To see this, take a perfect elimination ordering. Every vertex has at most two later neighbors, the penultimate vertex has at most one, and the last has none; summing later degrees gives the bound.

For every odd \(q>5\),
\[
k=\frac{q-\chi}{2}\ge 4,
\]
so
\[
|E(\Delta)|=\frac{nk}{2}\ge 2n>2n-3.
\]
Thus \(\Delta\) cannot be chordal. Since chordality is inherited by induced subgraphs and \(\Delta\) is induced in \(\Gamma(G)\), the full commuting graph \(\Gamma(G)\) is not chordal.

Combining the even, \(q=5\), and odd \(q>5\) cases proves the claim.

## Verification
A standard-library replay script is supplied at `artifacts/verify.py`. It reconstructs \(\mathrm{PSL}_2(p)\) for \(p=5,7,11,13\), checks the involution counts, regular degrees, and edge formula, verifies an explicit induced \(6\)-cycle for \(q=7\), and checks the density inequality over a broad arithmetic range. It prints `VERIFY_OK` on success.

The finite computations are sanity checks only. The proof above is uniform for every prime power in the stated range and does not infer the infinite theorem from finite enumeration.

## Relationship to prior work
Arvind, Ma, Cameron, and Maslova study forbidden induced subgraphs in commuting graphs and explicitly leave the classification of finite simple groups with chordal commuting graph open. In their Lie-type analysis they treat cographs rather than chordal graphs; for \(\mathrm{PSL}_2(q)\) they prove that the commuting graph is a cograph exactly in characteristic two (up to the isomorphism \(\mathrm{PSL}_2(5)\cong\mathrm{PSL}_2(4)\)). Their first public version appeared on 12 May 2023.

Bryden and Rowley later analyze the commuting involution graphs of \(\mathrm{PSL}_2(q)\), including their local structure and automorphism groups. Their results supply compatible structural information about commuting involutions but do not state the chordality classification proved here.

The present argument uses the involution class as an induced subgraph and combines its exact regular density with the sharp edge bound for chordal graphs of clique number at most three. This settles the complete \(\mathrm{PSL}_2(q)\) slice of the simple-group chordality problem.

## Limitations
This result does not classify chordal commuting graphs for the other finite simple groups. It also does not assert a classification for non-simple central extensions such as \(\mathrm{SL}_2(q)\).

The originality check found no statement implying this exact \(\mathrm{PSL}_2(q)\) chordality classification in the inspected literature or indexed result database. As with any literature search, an unindexed equivalent result remains a residual risk.

## References
1. V. Arvind, X. Ma, P. J. Cameron, N. V. Maslova, *Aspects of the commuting graph*, arXiv:2305.07301, first public version 12 May 2023; revised version 27 July 2025.
2. J. Bryden, P. Rowley, *Automorphism Groups of the \(\mathrm{PSL}_2(q)\) Commuting Involution Graphs*, arXiv:2509.25901, first public version 30 September 2025.
