# Total and paired domination after deleting zero from the total torsion element graph

## Finding

Let \(R\) be a commutative ring with nonzero identity and let \(M\) be a finite nonzero unitary \(R\)-module such that its torsion set \(T(M)\) is a submodule. Put \(\alpha=|T(M)|\) and \(\beta=|M/T(M)|\), and let \(T^0(\Gamma(M))\) be the total torsion element graph induced on \(M\setminus\{0\}\). Then \(T^0(\Gamma(M))\) has a total dominating set, equivalently a paired dominating set, exactly when \(\alpha\ge3\) or \(\alpha=1\) and \(2\notin Z(R)\). Whenever these sets exist, \[\gamma_t(T^0(\Gamma(M)))=\gamma_{\mathrm{pr}(T^0(\Gamma(M)))=\begin{cases}\beta-1,&\alpha=1,\ 2\notin Z(R),\\2\beta,&\alpha\ge3,\ 2\in Z(R),\\\beta+1,&\alpha\ge3,\ 2\notin Z(R).\end{cases}\] The obstruction is sharp: if \(\alpha=2\), deleting zero leaves an isolated torsion vertex, while if \(\alpha=1\) and \(2\in Z(R)\), every nonzero vertex lies in an isolated singleton component.

Equivalently, the zero-deleted graph has the component decomposition
\[
T^0(\Gamma(M))\cong K_{\alpha-1}\sqcup
\begin{cases}
(\beta-1)K_\alpha,&2\in Z(R),\\
\dfrac{\beta-1}2K_{\alpha,\alpha},&2\notin Z(R),
\end{cases}
\]
where an empty \(K_0\) component is omitted. The strengthened domination formulas follow componentwise from this decomposition.

## Assumptions and scope

Throughout, \(R\) is a commutative ring with nonzero identity and \(M\) is a finite nonzero unitary \(R\)-module. The torsion set is
\[
T(M)=\{m\in M:rm=0\text{ for some }0\ne r\in R\},
\]
and it is assumed to be a submodule. Write
\[
\alpha=|T(M)|,\qquad \beta=|M/T(M)|.
\]
The graph \(T^0(\Gamma(M))\) has vertex set \(M\setminus\{0\}\), with distinct \(x,y\) adjacent exactly when
\[
x+y\in T(M).
\]
A total dominating set requires every vertex, including every selected vertex, to have a selected neighbor. A paired dominating set is a dominating set whose induced subgraph contains a perfect matching.

## Proof

First separate the torsion and nontorsion vertices. If \(t\in T(M)\setminus\{0\}\) and \(x\notin T(M)\), then \(t+x\notin T(M)\), because otherwise
\[
x=(t+x)-t\in T(M),
\]
a contradiction. Hence there are no edges between these two parts. Any two distinct nonzero torsion elements are adjacent, so the torsion part is
\[
K_{\alpha-1}.
\tag{1}
\]

Now let \(x\notin T(M)\). Adjacency among nontorsion elements depends only on their cosets modulo \(T(M)\), because
\[
(x+t_1)+(y+t_2)\in T(M)
\iff x+y\in T(M).
\tag{2}
\]
Thus a coset \(x+T(M)\) can be adjacent only to its negative coset \(-x+T(M)\).

Suppose first that \(2\in Z(R)\). Choose \(0\ne a\in R\) with \(2a=0\). Then for every \(x\in M\),
\[
a(2x)=0,
\]
so \(2x\in T(M)\). In particular
\[
x+T(M)=-x+T(M).
\]
By (2), every nonzero quotient coset therefore induces a clique \(K_\alpha\), and different cosets have no edges between them. There are \(\beta-1\) such cosets, giving
\[
T^0(\Gamma(M))\cong K_{\alpha-1}\sqcup(\beta-1)K_\alpha.
\tag{3}
\]

Suppose instead that \(2\notin Z(R)\). For nontorsion \(x\), one has \(2x\notin T(M)\): if \(0\ne r\in R\) satisfied \(r(2x)=0\), then \((2r)x=0\), and \(2r\ne0\) because \(2\) is not a zero-divisor, contradicting \(x\notin T(M)\). Hence
\[
x+T(M)\ne -x+T(M).
\]
Each nonzero quotient coset is independent, and by (2) it is completely joined to its distinct negative coset and to no other coset. Therefore the nonzero quotient cosets pair up and
\[
T^0(\Gamma(M))\cong K_{\alpha-1}\sqcup\frac{\beta-1}2K_{\alpha,\alpha}.
\tag{4}
\]

A graph with an isolated vertex has no total dominating set. It also has no paired dominating set, since a paired dominating set must dominate the isolated vertex and every selected vertex must have a matching partner. Equations (3) and (4) show that an isolated vertex occurs exactly in either of two cases:
\[
\alpha=2,
\]
when the torsion component is \(K_1\), or
\[
\alpha=1\text{ and }2\in Z(R),
\]
when all nonzero quotient cosets are singleton cliques. This proves the existence criterion.

Every clique \(K_m\) with \(m\ge2\) and every complete bipartite graph \(K_{m,m}\) with \(m\ge1\) has both total and paired domination number \(2\): an edge is enough, and fewer than two vertices cannot totally dominate. Since distinct components cannot dominate or match across one another, both invariants equal twice the number of nontrivial components.

If \(\alpha=1\) and \(2\notin Z(R)\), (4) has \((\beta-1)/2\) components, so both values are \(\beta-1\). If \(\alpha\ge3\) and \(2\in Z(R)\), (3) has \(\beta\) components, giving \(2\beta\). If \(\alpha\ge3\) and \(2\notin Z(R)\), (4) has \((\beta+1)/2\) components, giving \(\beta+1\). This proves the formula.

## Verification

The standalone `verify.py` constructs \(T^0(\Gamma(M))\) directly for regular modules \(M=R=\mathbb Z/n\mathbb Z\) with
\[
n\in\{2,3,4,5,8,9\},
\]
computes torsion elements from annihilation, builds adjacency from the defining sum condition, and exhaustively determines total and paired domination whenever possible. These examples realize all four boundary regimes: torsion-free characteristic two, torsion-free odd characteristic, \(|T(M)|=2\), and both branches with \(|T(M)|\ge3\).

The checker also replays the component-count argument on a bounded grid of abstract admissible parameter profiles.

Exact output:

```text
VERIFY_OK
Zmod_case=(2, 1, 2, True, None, None, [0])
Zmod_case=(3, 1, 3, False, 2, 2, [1, 1])
Zmod_case=(4, 2, 2, True, None, None, [0, 1, 1])
Zmod_case=(5, 1, 5, False, 4, 4, [1, 1, 1, 1])
Zmod_case=(8, 4, 2, True, 4, 4, [2, 2, 2, 3, 3, 3, 3])
Zmod_case=(9, 3, 3, False, 4, 4, [1, 1, 3, 3, 3, 3, 3, 3])
abstract_parameter_profiles_checked=110
```

The finite calculations are corroborative only. The theorem for arbitrary finite \(M\) follows from the coset proof above.

## Relationship to prior work

Atani and Habibi introduced the total torsion element graph and gave the basic coset structure when \(T(M)\) is a submodule. Saraei's 2014 paper then introduced and studied the zero-deleted graph \(T^0(\Gamma(M))\), which is the exact object considered here.

Goswami and Sarmah later studied domination in the full graph \(T(\Gamma(M))\). Their full text records the nontorsion component decomposition and states total-domination formulas for the full graph, but searches of that paper found no occurrence of paired domination and it does not give the zero-deleted existence boundary above. Deleting zero is not innocuous for strengthened domination: it changes the torsion component from \(K_\alpha\) to \(K_{\alpha-1}\), creating an isolated vertex exactly when \(\alpha=2\), while for \(\alpha=1\) it removes the torsion component entirely.

Targeted searches using the exact zero-deleted graph title together with “total domination” and “paired domination,” as well as searches under the equivalent component decomposition, did not locate the stated classification.

## Limitations

The theorem assumes that \(T(M)\) is a submodule; without additive closure, the coset decomposition used in the proof is unavailable.

The module is assumed finite so that the domination numbers are finite integers and the component counts are literal finite counts.

The complete 2014 article on \(T^0(\Gamma(M))\) was not available through the inspected full-text path; its abstract and bibliographic metadata were inspected. This is the principal residual literature risk. No claim is made that the theorem reconstructs the module from the graph.

## References

1. F. Esmaeili Khalil Saraei, “The total torsion element graph without the zero element of modules over commutative rings,” *Journal of the Korean Mathematical Society* 51 (2014), 721–734. DOI: 10.4134/JKMS.2014.51.4.721.
2. S. Ebrahimi Atani and S. Habibi, “The total torsion element graph of a module over a commutative ring,” *Analele Ştiinţifice ale Universităţii Ovidius Constanţa, Seria Matematică* 19 (2011), 23–34.
3. J. Goswami and M. Sarmah, “On domination in the total torsion element graph of a module,” *Proyecciones Journal of Mathematics* 42 (2023), 795–814. DOI: 10.22199/issn.0717-6279-4904.
4. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206.
