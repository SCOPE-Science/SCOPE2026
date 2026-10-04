# Total and paired domination of the reduced comaximal graph of a semilocal ring

## Finding

Let \(R\) be a commutative ring with identity having exactly \(n\ge2\) maximal ideals \(M_1,\ldots,M_n\), and let \(CG_J(R)\) be the comaximal graph induced on \((R\setminus U(R))\setminus J(R)\). Put \(T_i=M_i\setminus\bigcup_{j\ne i}M_j\). A subset \(D\subseteq V(CG_J(R))\) is a total dominating set if and only if \(D\cap T_i\ne\varnothing\) for every \(i\). Consequently \(\gamma_t(CG_J(R))=n\), and the paired-domination number is \(\gamma_{pr}(CG_J(R))=2\lceil n/2\rceil\). If the vertex set is finite, its total domination polynomial is \[D_t(CG_J(R);x)=(1+x)^{N-\sum_i t_i}\prod_{i=1}^n((1+x)^{t_i}-1),\] where \(N=|V(CG_J(R))|\) and \(t_i=|T_i|\).

The classification is independent of the sizes of the residue fields and of nilpotents in the ring: only the finite maximal spectrum controls the minimum total- and paired-domination parameters. For finite rings it also gives every total dominating set, not just the minimum size.

## Assumptions and scope

Let \(R\) be a commutative ring with identity and exactly \(n\ge2\) maximal ideals \(M_1,\ldots,M_n\). Write \(J(R)=\bigcap_iM_i\), and let \(CG_J(R)\) denote the graph whose vertices are the nonunits outside \(J(R)\), with distinct vertices \(a,b\) adjacent precisely when \(Ra+Rb=R\).

For each \(i\), define the exclusive maximal-ideal cell
\[
T_i=M_i\setminus\bigcup_{j\ne i}M_j.
\]
The Chinese remainder theorem shows that every \(T_i\) is nonempty: prescribe residue \(0\) modulo \(M_i\) and residue \(1\) modulo every other maximal ideal.

## Proof

For any two elements \(a,b\in R\),
\[
Ra+Rb=R
\quad\Longleftrightarrow\quad
\text{no maximal ideal contains both }a\text{ and }b.
\]
Indeed, a proper ideal is contained in a maximal ideal.

Fix \(i\). Again by the Chinese remainder theorem, choose a vertex \(u_i\) with
\[
u_i\notin M_i,
\qquad
u_i\in M_j\quad(j\ne i).
\]
Thus \(u_i\) lies outside \(J(R)\) and is a nonunit. A vertex \(v\) is adjacent to \(u_i\) exactly when \(v\in T_i\): if \(v\) belonged to any \(M_j\) with \(j\ne i\), that maximal ideal would contain both vertices, while if \(v\notin M_i\) as well then \(v\) would be a unit. Therefore every total dominating set must meet \(T_i\). Since this holds for every \(i\),
\[
|D|\ge n.
\]

Conversely, suppose \(D\) meets every \(T_i\), and choose \(d_i\in D\cap T_i\). Every vertex \(v\) lies outside at least one maximal ideal, say \(M_i\), because \(v\notin J(R)\). The element \(d_i\) lies in no maximal ideal except \(M_i\). Hence no maximal ideal contains both \(v\) and \(d_i\), so they are adjacent. This also covers vertices of \(D\): if \(v=d_i\), choose any \(j\ne i\); then \(d_i\) and \(d_j\) are adjacent. Thus \(D\) is total dominating.

This proves the exact classification
\[
D\text{ is total dominating}
\quad\Longleftrightarrow\quad
D\cap T_i\ne\varnothing\text{ for all }i,
\]
and therefore
\[
\gamma_t(CG_J(R))=n.
\]
Every minimum total dominating set consists of exactly one choice from each \(T_i\), and those \(n\) chosen vertices form a clique.

For paired domination, every paired dominating set is total dominating and has even cardinality, so
\[
\gamma_{pr}(CG_J(R))\ge 2\left\lceil\frac n2\right\rceil.
\]
If \(n\) is even, one vertex from each \(T_i\) gives an \(n\)-clique and hence a perfect matching. If \(n\) is odd, choose \(d_i\in T_i\) for all \(i\) and, by the Chinese remainder theorem, choose an additional vertex \(z\) lying in \(M_1\cap M_2\) and in no other maximal ideal. Then \(z\) is adjacent to \(d_3\); pair these two, and perfectly match the remaining even clique on \(n-1\) vertices. Hence
\[
\gamma_{pr}(CG_J(R))=2\left\lceil\frac n2\right\rceil.
\]

Finally assume the vertex set is finite. The cells \(T_i\) are pairwise disjoint. The classification says that a total dominating set consists of a nonempty subset of each \(T_i\), together with an arbitrary subset of all other vertices. Multiplying the corresponding generating functions gives
\[
D_t(CG_J(R);x)
=(1+x)^{N-\sum_i t_i}
\prod_{i=1}^n\big((1+x)^{t_i}-1\big).
\]

## Verification

The proof is symbolic. The accompanying `verify.py` independently checks the support-set model in which a vertex is a nonempty proper subset of \([n]\) and adjacency is union equal to \([n]\). It exhaustively computes the total- and paired-domination minima through \(n=5\), verifies the forcing cells and constructions through \(n=9\), and directly enumerates every subset of the actual graph for \(\mathbb Z_{30}\) to confirm that the total dominating sets are exactly those meeting all three exclusive prime cells.

```text
VERIFY_OK
support_graph_exact_n=2..5
structural_checks_n=2..9
Z30_total_domination_classification=exact
```

Finite computation is not used as an infinite proof.

## Relationship to prior work

Maimani, Salimi, Sattari, and Yassemi introduced and developed the nonunit comaximal graph and its reduction modulo the Jacobson radical. Samei studied the same reduced graph \(CG_J(R)\), including diameter and dominating-set structure. Mehdi-Nezhad and Rahimi then studied ordinary domination in \(CG_J(R)\). For a ring with finitely many maximal ideals they construct one vertex from each \(T_i\) and explicitly observe that this clique is also a connected and total dominating set; for Artinian rings they obtain only the ordinary-domination bound \(2\le\gamma(CG_J(R))\le n\) in the case \(n\ge3\). Their article does not give a lower bound for total domination, does not classify all total dominating sets, and does not discuss paired domination or a total domination polynomial.

Gadge, Khandekar, and Joshi later describe comaximal graphs of Artinian rings as blow-ups of Boolean graphs/lattices. That structural description is compatible with the support-set proof above, but their paper studies ordered-set representations, perfectness, and Hamiltonicity rather than total or paired domination. Rather's 2026 paper treats independent domination and independence polynomials of full comaximal graphs of \(\mathbb Z_n\); its full text contains no paired-domination result and does not determine the total-domination polynomial considered here.

The present statement is stronger in scope than the finite/Artinian setting: the proof needs only finitely many maximal ideals, so it applies to arbitrary commutative semilocal rings with at least two maximal ideals.

## Limitations

The result concerns the reduced nonunit comaximal graph \(CG_J(R)\), not the full comaximal graph, whose unit vertices make ordinary domination trivial. The total domination polynomial formula requires a finite vertex set; the exact total- and paired-domination numbers themselves do not require finiteness of the ring. No claim is made here about other domination variants such as secure or Roman domination.

A residual originality risk remains because the Boolean blow-up structure makes the lower-bound argument short, so an unindexed note could contain the same deduction. Targeted searches in published-finding corpus and the public literature did not find such a statement.

## References

1. H. R. Maimani, M. Salimi, A. Sattari, and S. Yassemi, “Comaximal graph of commutative rings,” *Journal of Algebra* 319 (2008), 1801–1808. DOI: 10.1016/j.jalgebra.2007.02.003. Preprint public 2007-01-31.
2. K. Samei, “On the Comaximal Graph of a Commutative Ring,” *Canadian Mathematical Bulletin* 57 (2014), 413–423. DOI: 10.4153/CMB-2013-033-7.
3. E. Mehdi-Nezhad and A. M. Rahimi, “Dominating sets of the comaximal and ideal-based zero-divisor graphs of commutative rings,” *Quaestiones Mathematicae* 38 (2015), 613–629. DOI: 10.2989/16073606.2014.981713.
4. P. Gadge, N. Khandekar, and V. Joshi, “On the comaximal graph of a ring,” *AKCE International Journal of Graphs and Combinatorics* 21 (2024), 143–151. DOI: 10.1080/09728600.2024.2302184.
5. B. A. Rather, “Independent Domination Polynomial of Comaximal Graphs of Commutative Rings,” *Algebra Colloquium* 33 (2026), 243–258. DOI: 10.1142/S1005386726000222.
6. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.
