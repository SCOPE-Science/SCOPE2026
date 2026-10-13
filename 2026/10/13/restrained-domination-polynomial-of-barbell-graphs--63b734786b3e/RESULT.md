# Restrained-domination polynomial of barbell graphs
## Finding
For every integer \(n\ge3\), let \(B_n\) be the barbell graph formed from two disjoint cliques \(L,R\cong K_n\) by adding one bridge \(uv\), where \(u\in L\) and \(v\in R\). A restrained dominating set is a dominating set \(D\) such that the induced graph on \(V(B_n)\setminus D\) has no isolated vertex. Put \(X=L\setminus D\) and \(Y=R\setminus D\).

Then \(D\) is restrained dominating if and only if \(X\) and \(Y\) are proper subsets of their respective cliques and the only permitted singleton complements are bridge-rescued singletons:

\[
|X|=1\Longrightarrow X=\{u\}\text{ and }v\in Y,
\qquad
|Y|=1\Longrightarrow Y=\{v\}\text{ and }u\in X.
\]

There is no further restriction when a complement side is empty or has at least two vertices. With
\[
A_n(x)=(1+x)^n-nx^{n-1}-1,
\]
the complete restrained-domination polynomial is
\[
D_r(B_n;x)=A_n(x)^2+2x^{n-1}\bigl((1+x)^{n-1}-1\bigr)-x^{2n-2}.
\]
Hence
\[
\gamma_r(B_n)=2,
\qquad
d_r(B_n,2)=n^2,
\]
and the total number of restrained dominating sets is
\[
D_r(B_n;1)=(2^n-n-1)^2+2^n-3.
\]

For the disconnected graph \(2K_n\), the restrained-domination polynomial is \(A_n(x)^2\). Thus the single bridge contributes exactly
\[
2x^{n-1}\bigl((1+x)^{n-1}-1\bigr)-x^{2n-2},
\]
which is coefficientwise nonnegative. This gives a sharp contrast with ordinary domination, for which the bridge of the barbell is known to be irrelevant.

## Assumptions and scope
Graphs are finite, simple, and undirected. The theorem is stated for \(n\ge3\). The polynomial convention is
\[
D_r(G;x)=\sum_D x^{|D|},
\]
where the sum is over all restrained dominating sets \(D\) of \(G\). The case \(n=2\), where the barbell is \(P_4\), is outside the stated theorem.

## Proof
Let \(D\subseteq V(B_n)\), \(X=L\setminus D\), and \(Y=R\setminus D\). First, \(D\) must meet both cliques. If \(D\cap L=\varnothing\), then every nonbridge vertex of \(L\) has no neighbor in \(D\), contradicting domination; the same argument applies to \(R\). Therefore \(X\) and \(Y\) are proper subsets.

Once \(D\) meets each clique, every vertex outside \(D\) has a neighbor in \(D\) inside its own clique. Thus the remaining restrained condition is exactly that the graph induced by \(X\cup Y\) have no isolated vertices. A complement side of size at least two contains no isolated vertex because it lies in a clique. An empty complement side creates no condition. A singleton \(X=\{w\}\) is isolated unless \(w=u\) and \(v\in Y\); symmetrically a singleton \(Y\) is allowed exactly when it equals \(\{v\}\) and \(u\in X\). This proves the structural characterization.

Now mark omitted vertices by \(q\). On one clique, complements that are empty or have size at least two while remaining proper have generating polynomial
\[
C_n(q)=1+\sum_{k=2}^{n-1}\binom{n}{k}q^k=(1+q)^n-nq-q^n.
\]
Pairs of such regular complements contribute \(C_n(q)^2\). The remaining valid configurations are those involving a bridge singleton. The pair \(X=\{u\},Y=\{v\}\) contributes \(q^2\). If exactly one side is a bridge singleton, the other side must contain its bridge endpoint and at least one, but not all, nonbridge vertices; together the two orientations contribute
\[
2q^2\bigl((1+q)^{n-1}-1-q^{n-1}\bigr).
\]
Hence the complement enumerator is
\[
Q_n(q)=C_n(q)^2+q^2+2q^2\bigl((1+q)^{n-1}-1-q^{n-1}\bigr).
\]
Since a set with \(|X|+|Y|\) omitted vertices has size \(2n-|X|-|Y|\),
\[
D_r(B_n;x)=x^{2n}Q_n(x^{-1}).
\]
Using
\[
x^nC_n(x^{-1})=(1+x)^n-nx^{n-1}-1=A_n(x),
\]
and simplifying the bridge-singleton terms gives the stated formula.

For \(n\ge3\), the coefficient of \(x\) in \(A_n(x)\) is \(n\), while the bridge-correction term has degree at least \(n\). Therefore the smallest nonzero degree is \(2\), with coefficient \(n^2\). Evaluating the polynomial at \(x=1\) yields the stated total count. For \(2K_n\), no bridge can rescue a singleton complement, so only the \(C_n(q)^2\) term remains, giving \(D_r(2K_n;x)=A_n(x)^2\).

## Verification
A standalone exhaustive checker enumerates every subset of \(V(B_n)\) for \(3\le n\le8\), tests the definition directly, independently tests the structural criterion, and compares every coefficient against the closed formula. It also checks \(n=2\) as an unclaimed boundary case. Its output is:

`VERIFY_OK n_range=3..8 subset_checks=87360 valid_sets=79957 coefficient_checks=72 boundary_n2=P4_checked max_order=16`

The finite computation is a consistency check only; the theorem for all \(n\ge3\) is established by the symbolic proof above.

## Relationship to prior work
Restrained domination was studied by the late 1990s. An exact day-level public record for Henning's paper *Graphs with large restrained domination number* is 28 February 1999; the earlier Telle--Proskurowski partial-tree paper is a reported indirect precursor, but only issue-level dating was verified here. The restrained-domination polynomial was later studied explicitly by Kanagavel and Kokilambal; the accessible abstract lists complete graphs, complete bipartite graphs, paths, cycles, and products of \(K_2\) with \(K_k\), not barbells. A later paper treats join and corona operations.

For the same graph family, Jahari and Alikhani prove that the bridge of \(B_n\) is irrelevant for the ordinary domination polynomial and obtain the same ordinary domination polynomial as \(2K_n\). That theorem does not imply the present result: restrained domination imposes the additional isolate-free condition on the complement, and the formula above identifies exactly the configurations rescued by the bridge.

Searches under the aliases “restrained domination polynomial barbell graph”, “all restrained dominating sets barbell graph”, “restrained domination barbell clique bridge”, and “restrained domination polynomial barbell \(B_n\)” located no statement covering this barbell formula. The closest indexed results concern chain graphs, crown graphs, and restrained Roman domination on complete multipartite graphs; none contains barbell graphs for \(n\ge3\) or implies the bridge-correction formula.

## Limitations
The theorem is restricted to equal-clique barbells \(B_n\) with \(n\ge3\); unequal clique sizes and longer connecting paths are not treated. The full text of the 2019 restrained-domination-polynomial paper was not available through the lawful access route used for this review, so its abstract-level family list leaves a residual literature risk. The historical first-public-date field uses the earliest exact day-level public source date verified here; an indirect 1997 precursor is known at issue-level resolution but no exact public day was verified.

## References
- M. A. Henning, *Graphs with large restrained domination number*, Discrete Mathematics 197--198 (1999), 415--429. DOI: 10.1016/S0012-365X(99)90095-X.
- G. S. Domke, J. H. Hattingh, S. T. Hedetniemi, R. C. Laskar, and L. R. Markus, *Restrained domination in graphs*, Discrete Mathematics 203 (1999), 61--69. DOI: 10.1016/S0012-365X(99)00016-3.
- S. Jahari and S. Alikhani, *On \(\mathcal{D}\)-equivalence classes of some graphs*, arXiv:1511.00159.
- K. Kanagavel and G. Kokilambal, *Restrained domination polynomial in graphs*, Journal of Discrete Mathematical Sciences and Cryptography 22 (2019), 761--775. DOI: 10.1080/09720529.2019.1681693.
- S. Velmurugan and R. Kala, *Restrained domination polynomial of join and corona of graphs*, Discrete Mathematics, Algorithms and Applications 15 (2023), 2250118. DOI: 10.1142/S179383092250118X.
