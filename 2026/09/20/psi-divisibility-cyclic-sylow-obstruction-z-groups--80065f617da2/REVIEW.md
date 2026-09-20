# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Let \(G=P\rtimes H\), where \(P\) is a nontrivial cyclic
\(p\)-group, \((|P|,|H|)=1\), and \(C=C_H(P)<H\). Write
\[
t=|P|,\quad A=\psi(P),\quad h=\psi(H),\quad c=\psi(C).
\]
The standard normal-cyclic-Sylow formula gives
\[
\psi(G)=th+(A-t)c.
\]
If \(G\) were \(\psi\)-divisible, the subgroup \(H\) would give
\(h\mid(A-t)c\), while the subgroup \(P\times C\) would give
\(Ac\mid t(h-c)\). Writing \(h=dx,c=dy\) with \((x,y)=1\), the first
divisibility gives \(x\mid A-t\), while the second gives
\(A\mid t(x-y)\). Since \(P\) is cyclic of order \(p^a\),
\[
A=\frac{p^{2a+1}+1}{p+1}\equiv1\pmod p,
\]
so \((A,t)=1\), and hence \(A\mid x-y\). But \(C<H\) implies
\(0<x-y<x\le A-t<A\), a contradiction.

The two subgroup inclusions used in the argument were checked explicitly:
\(H\le G\) by definition of the semidirect product, and
\(PC=P\times C\le G\) because \(C=C_H(P)\) centralizes \(P\) and has
order coprime to \(|P|\). No cancellation of a possibly non-coprime
\(\psi(C)\) factor is used.

For the Z-group corollary, the standard ZM presentation gives a normal cyclic
Hall subgroup \(\langle a\rangle\). For each prime power \(p^a\Vert m\), its
Sylow \(p\)-subgroup is characteristic in \(\langle a\rangle\), hence normal
in the whole group, and \((m,r-1)=1\) ensures that the complement acts
nontrivially. Therefore every nonnilpotent Z-group is excluded. Nilpotent
Z-groups are cyclic, after which the established abelian classification
applies.

## Originality

**PASS, to the best of our knowledge.** Harrington--Jones--Lamarche (2014)
classified only the abelian case and explicitly reported no known nonabelian
\(\psi\)-divisible group. Lazorec (2020/2021) developed the relevant ZM-group
formula and proved a partial nondivisibility theorem for
\(ZM(p^\alpha,n,r)\) subject to an additional exponent inequality; immediately
afterward the paper asked whether any nonnilpotent square-free-order group can
be \(\psi\)-divisible and reported exhaustive computation only through order
\(72000\). Lazorec's 2023 \(\psi\)-divisibility-graph paper still described the
existence of nonabelian \(\psi\)-divisible groups as open.

Targeted searches were made for the exact and synonymous claims involving
\(\psi\)-divisible semidirect products, normal cyclic Sylow subgroups,
Z-groups/ZM-groups, and square-free-order groups. No prior statement of the
two-subgroup divisibility obstruction or the resulting Z-group classification
was located. A 2026 paper of Iorio--Trombetti uses the same standard
normal-cyclic-Sylow formula for a different normalized-\(\psi\) problem, but
does not discuss \(\psi\)-divisibility. A separate 2026 divisibility paper of
Tărnăuceanu studies the different condition
\(|H|-|K|\mid\psi(H)-\psi(K)\).

Residual risk remains because indexing is not exhaustive and a short
unindexed note or equivalent argument under different terminology could
exist. The known semidirect-product formula itself is not claimed as new;
the claimed contribution is the divisibility obstruction derived from using
both \(H\) and \(P\times C_H(P)\), together with its Z-group and square-free
consequences.

## Value

**PASS.** The theorem replaces a restricted arithmetic obstruction by a
structural one: any noncentral normal cyclic Sylow subgroup rules out
\(\psi\)-divisibility. It consequently classifies all \(\psi\)-divisible
Z-groups as the cyclic square-free groups and gives a theoretical negative
answer to Lazorec's square-free-order open problem, removing the previous
finite computational bound.

## Limitations

The broader existence problem for nonabelian \(\psi\)-divisible groups remains
open here. The theorem only treats groups possessing a normal cyclic Sylow
subgroup on which a complement acts nontrivially.
