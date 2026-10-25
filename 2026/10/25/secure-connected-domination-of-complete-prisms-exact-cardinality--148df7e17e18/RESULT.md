# Secure connected domination of complete prisms: exact cardinality and minimality polynomials

## Finding

Let \(H_n=K_n\square K_2\), where \(n\ge3\). Its vertices are \(a_i,b_i\) for \(i\in[n]\); each of \(\{a_i:i\in[n]\}\) and \(\{b_i:i\in[n]\}\) is a clique, and the only edges between them are \(a_ib_i\). A set \(S\) is *secure connected dominating* (SCD) when it induces a connected graph, dominates every vertex, and for every \(u\notin S\) there is a neighboring \(v\in S\) such that replacing \(v\) with \(u\) still gives a connected dominating set. This is the single-vertex replacement definition, not the distinct secure-alliance definition.

Put \(A=\{i:a_i\in S\}\) and \(B=\{i:b_i\in S\}\). **Exact classification:** \(S\) is SCD if and only if \(A\cap B\ne\varnothing\) and at least one of the following holds:

1. \(|A|\ge2\) and \(|B|\ge2\);
2. \(|A|=1\) and \(B=[n]\);
3. \(A=[n]\) and \(|B|=1\).

The bivariate counting polynomial \(D_n(x,y)=\sum_{S\text{ SCD}}x^{|A|}y^{|B|}\) is

\[
\begin{aligned}
D_n(x,y)={}&\big((1+x)^n-1-nx\big)\big((1+y)^n-1-ny\big)\\
&-\sum_{a=2}^{n-2}\sum_{b=2}^{n-a}\binom na\binom{n-a}b x^a y^b
+n(xy^n+x^{n}y).
\end{aligned}
\]

Here an empty sum is zero. Its cardinality specialization \(D_n(z)=D_n(z,z)\) has the closed form

\[
\begin{aligned}
D_n(z)={}&\big((1+z)^n-1-nz\big)^2-\bigg((1+2z)^n-2(1+z)^n+1\\
&\qquad -2nz\big((1+z)^{n-1}-1\big)+n(n-1)z^2\bigg)+2nz^{n+1}.
\end{aligned}
\]

For inclusion-minimal SCD sets, the cardinality polynomial is

\[
M_n(z)=\binom n2(2n-3)z^4+2nz^{n+1}.
\]

Consequently, the secure connected domination number is \(\gamma_{sc}(H_n)=4\), while the largest inclusion-minimal SCD cardinality is \(n+1\). The difference \(n-3\) is unbounded among these connected \(n\)-regular graphs. For \(n=3\), the two terms of \(M_n\) both have degree four and yield exactly fifteen minimum sets. For \(n\ge4\), the minimum sets are the \(\binom n2(2n-3)\) four-vertex sets specified by \(|A|=|B|=2\) and \(A\cap B\ne\varnothing\); there are exactly \(2n\) additional inclusion-minimal sets of size \(n+1\).

## Assumptions and scope

All graphs are finite, simple and undirected. Fix an integer \(n\ge3\), and use *dominating* in the closed-neighborhood sense; vertices in the selected set do not require a separate neighbor. Every replacement must preserve **both** connectedness and domination. An inclusion-minimal SCD set has no proper subset that is SCD. The labels \(a_i,b_i\) are distinct, so each subset of labeled vertices is counted once. The bivariate variables mark the numbers of selected vertices in the respective clique layers.

## Proof

**Step 1 (connected domination).** If \(A,B\ne\varnothing\), both cliques are internally dominated, and the induced subgraph is connected precisely when \(A\cap B\ne\varnothing\): a selected matching edge is the only possible bridge between layers. If one layer is unrepresented, domination requires selection of the entire other layer; nevertheless this set is not SCD. Indeed, when all \(a_i\) are selected and no \(b_i\) is selected, the only defender of the omitted \(b_j\) is its partner \(a_j\); replacing it leaves \(b_j\) isolated from the selected \(a\)-clique. The symmetric case is identical. Hence every SCD set meets both layers and has a selected matching edge.

**Step 2 (at least two vertices in each layer).** Suppose \(|A|,|B|\ge2\) and choose \(i\in A\cap B\). For any omitted \(a_j\), a selected \(a_k\) can be chosen such that \((A\cap B)\setminus\{k\}\ne\varnothing\). If the intersection has at least two indices, remove any selected \(a_k\); otherwise choose \(k\in A\setminus B\), which exists because \(|A|\ge2\). Since \(a_k\) and \(a_j\) belong to the same clique, the replacement is legal. It preserves the cardinality of each nonempty selected layer and leaves a selected matching edge, hence is connected and dominating. The argument for an omitted \(b_j\) is symmetric. Every set of this type is therefore SCD.

**Step 3 (a singleton layer).** Suppose \(A=\{i\}\). Initial connectedness forces \(i\in B\). If \(B\ne[n]\), choose \(j\notin B\). The omitted vertex \(a_j\) has only one selected neighbor, namely \(a_i\). Replacing \(a_i\) by \(a_j\) destroys all selected matching edges, so the resulting set is disconnected. Thus no such set is SCD. Conversely, if \(B=[n]\), each omitted \(a_j\) is defended by \(a_i\), since \(\{a_j\}\cup\{b_k:k\in[n]\}\) is connected and dominating. All omitted vertices are of this form. Interchanging the layers proves the symmetric statement, completing the classification.

**Step 4 (all-set polynomial).** Among ordered pairs \((A,B)\) with \(|A|,|B|\ge2\), the unrestricted bivariate generating function is the product of the two factors in the first line of \(D_n(x,y)\). For disjoint \(A,B\) with sizes \(a,b\), the number of choices is \(\binom na\binom{n-a}b\); these are exactly the forbidden pairs with no selected matching edge. The remaining two types have, respectively, \(n\) choices for the singleton in \(A\), and \(n\) choices for the singleton in \(B\), contributing \(n(xy^n+x^{n}y)\). This proves the bivariate identity.

For the univariate identity, the forbidden disjoint nonempty pairs contribute \((1+2z)^n-2(1+z)^n+1\). To restrict both disjoint sets to size at least two, subtract twice \(nz((1+z)^{n-1}-1)\), then restore the \(n(n-1)z^2\) ordered pairs of disjoint singletons. Substituting gives the claimed closed form.

**Step 5 (inclusion-minimal sets).** Every SCD set with \(|A|,|B|\ge2\) contains a four-vertex SCD subset: pick \(i\in A\cap B\), then one other index from each of \(A\) and \(B\). Every such four-vertex set is inclusion-minimal because no SCD set of cardinality less than four exists for \(n\ge3\). For each two-element \(A\), exactly \(\binom n2-\binom{n-2}2=2n-3\) two-element \(B\)'s intersect it, giving \(\binom n2(2n-3)\) four-vertex sets. Each singleton/full-layer set is also inclusion-minimal: any proper subset has at most one selected vertex in the singleton layer and an incomplete opposite layer, or is confined to a single layer, and hence fails the classification. There are \(2n\) such sets, and there are no others. Their sizes are four and \(n+1\), giving the stated parameters, with coincident sizes when \(n=3\).

## Verification

The standalone, standard-library-only `verify.py` constructs the edge sets of \(H_n\), computes ordinary connected domination using adjacency and graph traversal, and checks security directly by searching all legal one-vertex replacements. It compares this independently implemented predicate against the structural classification, the coefficient formula, and the inclusion-minimal classification on **every** labeled vertex subset for \(3\le n\le8\). This comprises 87,360 subsets. All comparisons passed, with total SCD-set counts \(22,123,636,3001,13322,56951\) at orders \(n=3,4,5,6,7,8\), respectively. The infinite-family theorem is proved by Steps 1–5; finite checks do not establish it on their own.

To reproduce, place `verify.py` in the working directory and run `python verify.py`. No downloads or auxiliary data are required.

## Relationship to prior work

Cabaro, Canoy and Aniversario (2014) introduced the single-replacement secure connected domination invariant, including a general defender criterion. Cabaro and Canoy (2015) developed join and lexicographic-composition results; their graph operations do not identify the present Cartesian prism with a covered family. Pavan Kumar, Venkata Subba Reddy and Arumugam (2020 preprint) studied secure connected domination on, among other families, the ladder \(P_n\square K_2\), not the complete prism \(K_n\square K_2\). Those findings supply the motivation and definitions, but not the displayed all-set or minimality polynomials.

Terminology matters: Johnson and Jones (2013), and Andoyo and Rulete (2026), study a *secure set* in the defensive-alliance sense before imposing domination and connectivity. This is mathematically different from requiring that every omitted vertex can replace one selected neighbor while maintaining connected domination. Their similarly named counting polynomials therefore do not directly cover the present predicate. Published results on secure (without connected) or secure total domination of complete multipartite graphs likewise address different graphs and/or predicates; a complete prism is not a complete multipartite graph when \(n\ge3\).

## Limitations

The classification concerns single-vertex replacement security only, not successive-attack eternal security or secure defensive alliances. The polynomial counts labeled vertex subsets, not isomorphism classes of configurations. The result does not give formulas for arbitrary Cartesian products or for two cliques joined by an arbitrary partial matching. A targeted literature and indexed-claim search found no published equivalent under the tested aliases, but it cannot rule out an unindexed or differently formulated prior result. Independent mathematical audit has not been performed.

## References

1. A. G. Cabaro, S. S. Canoy Jr., and I. S. Aniversario, *Secure Connected Domination in a Graph*, International Journal of Mathematical Analysis 8 (2014), 2065–2074, DOI: 10.12988/ijma.2014.47221. Open text: https://www.m-hikari.com/ijma/ijma-2014/ijma-41-44-2014/cabaroIJMA41-44-2014.pdf
2. A. G. Cabaro and S. R. Canoy Jr., *Secure Connected Dominating Sets in the Join and Composition of Graphs*, International Journal of Mathematical Analysis 9 (2015), 1241–1248, DOI: 10.12988/ijma.2015.5247. Open text: https://www.m-hikari.com/ijma/ijma-2015/ijma-25-28-2015/p/cabaroIJMA25-28-2015.pdf
3. J. Pavan Kumar, P. Venkata Subba Reddy, and S. Arumugam, *Algorithmic Complexity of Secure Connected Domination in Graphs*, arXiv:2002.00713 (first arXiv posting 2020-02-03), https://arxiv.org/abs/2002.00713; journal DOI: 10.1016/j.akcej.2019.08.012.
4. P. Johnson and C. Jones, *Secure-dominating sets in graphs*, preprint dated 2013-08-30; accessible text: https://www.researchgate.net/publication/328231364_SECURE-DOMINATING_SETS_IN_GRAPHS.
5. J. D. Andoyo and R. F. Rulete, *On Connected Secure Domination Polynomial of Some Graphs*, Annals of Communications in Mathematics 9 (2026), DOI: 10.62072/acm.2026.09025; different (secure-alliance) predicate.
