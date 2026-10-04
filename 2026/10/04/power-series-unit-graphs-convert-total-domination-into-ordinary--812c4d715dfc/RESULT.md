# Power-series unit graphs convert total domination into ordinary domination

## Finding

Let \(R\) be a finite commutative ring with nonzero identity and suppose \(2\notin U(R)\). If \(G(R)\) is the simple unit graph, then the formal-power-series unit graph satisfies \[\gamma(G(R[[x]]))=\gamma_t(G(R)).\] Equivalently, \(G(R[[x]])\) is obtained from \(G(R)\) by replacing every vertex with an infinite independent fiber and every base edge with a complete bipartite graph between the corresponding fibers. In particular, if \(R\) is finite local and its residue field has characteristic \(2\), then \(\gamma(G(R[[x]]))=2\).

The equality is a parameter-transfer principle: ordinary domination of the infinite power-series graph is exactly total domination of the finite base unit graph. It is not merely an upper bound coming from the unit set.

## Assumptions and scope

Let \(R\) be a finite commutative ring with \(1\neq0\), and write \(G(R)\) for the simple unit graph whose distinct vertices \(a,b\in R\) are adjacent exactly when \(a+b\in U(R)\). Assume \(2\notin U(R)\).

Let
\[
\pi:R[[x]]\to R
\]
be the constant-term map. For \(a\in R\), put
\[
F_a=\pi^{-1}(a)=a+xR[[x]].
\]
Each \(F_a\) is infinite.

The total domination number \(\gamma_t(G(R))\) is well-defined here because \(G(R)\) has no isolated vertices: for any \(a\in R\), the vertex \(1-a\) is adjacent to \(a\), and \(1-a\neq a\) because equality would give \(2a=1\), forcing \(2\in U(R)\).

## Proof

A formal power series over a commutative ring is a unit exactly when its constant term is a unit. Hence distinct \(f,g\in R[[x]]\) are adjacent in \(G(R[[x]])\) exactly when
\[
\pi(f)+\pi(g)\in U(R).
\]

If \(f,g\in F_a\), then their constant-term sum is \(2a\). Since \(2\notin U(R)\), no element \(2a\) can be a unit: if \(2a\) were invertible, then \(2\) would have inverse \(a(2a)^{-1}\). Therefore every fiber \(F_a\) is independent.

If \(a\neq b\), then every vertex of \(F_a\) is adjacent to every vertex of \(F_b\) exactly when \(a+b\in U(R)\). Thus the power-series unit graph is the infinite independent-fiber blow-up of \(G(R)\).

For the upper bound, let \(S\subseteq R\) be a minimum total dominating set of \(G(R)\). Embed \(S\) as constant power series. Given any \(f\in F_a\), total domination gives some \(b\in S\) adjacent to \(a\), so \(a+b\in U(R)\). Hence \(f\) is adjacent to the constant series \(b\). Therefore
\[
\gamma(G(R[[x]]))\le |S|=\gamma_t(G(R)).
\]

For the reverse inequality, let \(D\) be a minimum dominating set of \(G(R[[x]])\). The preceding construction shows that \(D\) is finite. Put \(S=\pi(D)\). For each \(a\in R\), choose a series \(f_a\in F_a\setminus D\), which is possible because \(F_a\) is infinite and \(D\) is finite. Since \(D\) dominates, there is some \(d\in D\) adjacent to \(f_a\). Therefore
\[
a+\pi(d)\in U(R),
\]
so \(a\) has a neighbor in \(S\). This holds for every \(a\in R\), including every element of \(S\), so \(S\) is a total dominating set of \(G(R)\). Consequently
\[
\gamma_t(G(R))\le |S|\le |D|=\gamma(G(R[[x]])).
\]
Combining the two inequalities proves the equality.

For the local-ring corollary, let \(\mathfrak m\) be the maximal ideal and \(k=R/\mathfrak m\). If \(2\notin U(R)\), then \(\operatorname{char}k=2\). In a local ring, \(a+b\) is a unit exactly when its residue is nonzero. In characteristic \(2\), this means the residues of \(a\) and \(b\) are different. Hence \(G(R)\) is the complete \(|k|\)-partite graph whose parts are the residue classes modulo \(\mathfrak m\). Any two vertices from distinct parts form a total dominating set, so \(\gamma_t(G(R))=2\), and therefore \(\gamma(G(R[[x]]))=2\).

## Verification

The proof is structural and does not rely on finite experiments. The accompanying `verify.py` checks two finite truncations \(R[x]/(x^2)\), whose adjacency also depends only on constant terms. It verifies a local example and a nonlocal example where the transferred value is not \(2\):

```text
VERIFY_OK
Z4: gamma_t(G(R))=2, gamma(G(R[x]/(x^2)))=2
F2xF2: gamma_t(G(R))=4, gamma(G(R[x]/(x^2)))=4
finite_truncation_check=constant-term blow-up agrees with theorem
```

The \(\mathbb F_2\times\mathbb F_2\) example is useful as a boundary check: its base unit graph is a disjoint union of two edges, so its total domination number is \(4\), and the corresponding truncated blow-up has ordinary domination number \(4\).

## Relationship to prior work

Afkhami and Khosh-Ahang (2013) studied unit graphs under polynomial and formal-power-series extensions. Their Remarks 2.2 state that adjacency in \(G(R[[x]])\) is determined by the constant terms, note that base edges generate infinite complete bipartite subgraphs, and record an equivalence for whether the full unit set is a dominating set. They did not state the minimum-domination transfer above.

Kiani, Maimani, Pournaki, and Yassemi (2015) studied domination and total domination of unit graphs for finite commutative rings and classified rings with domination number below four. Their finite-ring results supply the natural base parameter \(\gamma_t(G(R))\), but the infinite power-series graph is outside their stated finite setting.

Later domination work on generalized unit/unitary Cayley graphs and recent domination-parameter work likewise explicitly treats finite rings. Targeted searches using `power series`, `formal power series`, `unit graph`, `domination`, and `total domination` found no prior statement reducing \(\gamma(G(R[[x]]))\) to \(\gamma_t(G(R))\).

## Limitations

The hypothesis \(2\notin U(R)\) is essential for the independent-fiber description. When \(2\in U(R)\), some constant-term fibers contain edges because \(2a\) can be a unit, and the exact domination parameter becomes a loop-sensitive variant of domination on the base ring rather than ordinary total domination.

The theorem is stated for finite base rings so that a finite minimum total dominating set exists and every infinite fiber contains a vertex outside a minimum dominating set. A broader cardinal version for infinite base rings is not claimed here.

## References

1. M. Afkhami and F. Khosh-Ahang, “Unit graphs of rings of polynomials and power series,” *Arabian Journal of Mathematics* 2 (2013), 233–246. DOI: 10.1007/s40065-013-0067-0. Published online 2013-02-15.
2. S. Kiani, H. R. Maimani, M. R. Pournaki, and S. Yassemi, “Classification of rings with unit graphs having domination number less than four,” *Rendiconti del Seminario Matematico della Università di Padova* 133 (2015), 173–195. DOI: 10.4171/RSMUP/133-9.
3. T. Tamizh Chelvam, S. Anukumar Kathirvel, and M. Balamurugan, “Domination in generalized unit and unitary Cayley graphs of finite rings,” *Indian Journal of Pure and Applied Mathematics* 51 (2020), 533–556. DOI: 10.1007/s13226-020-0415-7.
4. T. Du and A. Gan, “Domination Parameters of Unit Graphs of Rings,” *Axioms* 14 (2025), 399. DOI: 10.3390/axioms14060399.
