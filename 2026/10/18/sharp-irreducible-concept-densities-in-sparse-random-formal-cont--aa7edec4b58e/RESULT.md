# Sharp irreducible-concept densities in sparse random formal contexts

## Finding

Fix real constants \(\alpha,c>0\). For each integer \(n>c\), let a formal context have \(n\) labelled objects, \(m_n=\lfloor\alpha n\rfloor\) labelled attributes, and independent incidence probability \(p_n=c/n\); restrict to sufficiently large \(n\) that \(m_n\ge2\). Write \(J_n\) and \(K_n\) for the numbers of **nonbottom join-irreducible** and **nontop meet-irreducible** concepts in its concept lattice. Define

\[
\begin{aligned}
F_J(\alpha,c)&=1-(1+\alpha c)e^{-\alpha c}\\
&\quad+\alpha\left(1-e^{-c e^{-\alpha c}}\right)
 e^{-c(1-e^{-\alpha c})}\left[1+c(1-e^{-\alpha c})\right],\\
F_K(\alpha,c)&=\alpha\left[1-(1+c)e^{-c}\right]\\
&\quad+\left(1-e^{-\alpha c e^{-c}}\right)
 e^{-\alpha c(1-e^{-c})}\left[1+\alpha c(1-e^{-c})\right].
\end{aligned}
\]

Then

\[
\mathbb E\left[\left|\frac{J_n}{n}-F_J(\alpha,c)\right|
 +\left|\frac{K_n}{n}-F_K(\alpha,c)\right|\right]
 =O_{\alpha,c}(n^{-1/2}),
\]

and the expectations admit bounded errors:

\[
\mathbb E J_n=nF_J(\alpha,c)+O_{\alpha,c}(1),\qquad
\mathbb E K_n=nF_K(\alpha,c)+O_{\alpha,c}(1).
\]

These are the asymptotic object and attribute sizes of the canonical irreducible representation of the concept lattice. They distinguish distinct irreducible concepts from the number of individually indispensable *labelled* input objects. In particular, if \(R_n\) counts labelled objects whose intent is **not** an intersection of the intents of a subset of the other objects (empty intersection permitted), put
\(a=c e^{-\alpha c}\) and \(b=c(1-e^{-\alpha c})\). Then

\[
\frac{J_n-R_n}{n}\ \xrightarrow{L^1}\
\alpha\left[1-(1+a)e^{-a}\right]e^{-b}(1+b)>0.
\]

Thus treating individually reducible duplicate rows as jointly deletable systematically undercounts the irreducible context by a positive linear fraction.

## Assumptions and scope

For a finite context \((G,M,I)\), derivation means the sets of common attributes and of common objects; a formal concept is a mutually derived extent–intent pair, ordered by inclusion of extents. A join-irreducible is an element other than the least element which cannot be joined from two strictly smaller elements; meet-irreducibility is dual. Let \(\deg(g)\) be the number of attributes incident to object \(g\). For an attribute \(a\), define \(A_a\) as the number of objects with intent exactly \(\{a\}\), and \(B_a\) as the number of objects incident to \(a\) with degree at least two. Define the local proxy

\[
\widetilde J=\#\{g:\deg(g)\ge2\}+\#\{a:A_a\ge1,\ B_a\le1\}.
\]

The dual proxy \(\widetilde K\) is obtained by exchanging objects and attributes. Let \(Q\) be the number of (not necessarily induced) four-cycles in the bipartite incidence graph. For **every** finite context with at least two vertices on each side,

\[
|J-\widetilde J|\le4Q+2,\qquad |K-\widetilde K|\le4Q+2.
\]

This deterministic estimate is also part of the finding. It does not assume any random-graph limit or that the incidence graph is a forest.

## Proof

**1. The four-cycle stability lemma.** Every concept is the join of the object concepts of the objects in its extent. Hence each join-irreducible is an object concept. Object concepts are identified by their object intents: a join of object concepts has intent equal to the intersection of their intents. Equivalently, a distinct object concept is join-irreducible if its intent has exactly one upper cover in the inclusion poset of distinct object intents augmented by the full attribute set (the standard finite-context criterion).

Call a vertex *bad* if it belongs to a four-cycle. An object of degree at least two which is not bad cannot share two attributes with any other object. Its intent therefore has no strict containing object intent. Unless it is the full attribute set (which represents the bottom), it gives one distinct join-irreducible concept. There is at most one exceptional full-intent concept to subtract. For an attribute \(a\) which is not bad, a singleton row with intent \(\{a\}\) exists exactly when \(A_a\ge1\). Strictly larger object intents containing \(a\) correspond to the \(B_a\) higher-degree neighbors. No two distinct such neighbors have another attribute in common, because that would make a four-cycle through \(a\). Therefore the singleton intent is join-irreducible exactly when \(B_a\le1\). Every object of degree zero represents the same top concept, contributing at most one unaccounted join-irreducible. The bad objects and bad attributes number at most \(2Q\) each. This proves \(|J-\widetilde J|\le4Q+2\). Transposing the incidence relation proves the meet bound.

**2. Exact finite mean of the proxy.** Temporarily write \(r=|G|\), \(m=|M|\) and \(p\) for any Bernoulli incidence probability. Put
\(q=p(1-p)^{m-1}\) and \(h=p[1-(1-p)^{m-1}]\). For each fixed attribute, its incident rows partition independently into singleton rows (probability \(q\)), higher-degree rows (probability \(h\)), and nonincident rows (probability \(1-p\)). Thus

\[
\Pr(A_a\ge1,B_a\le1)=(1-h)^r-(1-p)^r
 +rh\left[(1-h)^{r-1}-(1-p)^{r-1}\right].
\]

It follows by linearity that

\[
\begin{aligned}
\mathbb E\widetilde J={}&r\left[1-(1-p)^m-mp(1-p)^{m-1}\right]\\
&+m\left[(1-h)^r-(1-p)^r+rh\big((1-h)^{r-1}-(1-p)^{r-1}\big)\right].
\end{aligned}
\]

The dual formula swaps \(r\) and \(m\). With \(r=n,m=\lfloor\alpha n\rfloor,p=c/n\), the two formulas equal \(nF_J+O_{\alpha,c}(1)\) and \(nF_K+O_{\alpha,c}(1)\). Meanwhile

\[
\mathbb E Q=\binom n2\binom{m_n}{2}(c/n)^4=O_{\alpha,c}(1).
\]

The deterministic lemma yields both asserted expectation errors.

**3. Quantitative concentration.** Expose the \(n\) independent incidence rows and replace one row by an independent copy. This can change \(\widetilde J\) only through that row's degree-at-least-two indicator and the attribute indicators at the attributes present in its old or replacement row. The absolute change is bounded by \(1+D+D'\), with \(D,D'\) independent binomial random variables having parameters \((m_n,c/n)\). Their second moments are uniformly bounded. Efron–Stein therefore gives \(\operatorname{Var}(\widetilde J)=O_{\alpha,c}(n)\). Apply the identical argument to independent incidence columns to get \(\operatorname{Var}(\widetilde K)=O_{\alpha,c}(n)\). Cauchy–Schwarz, the proxy expectation formulas and the four-cycle error give the asserted joint \(L^1\) rate.

**4. Individually nonreducible rows versus irreducible concepts.** Outside the bad vertices and the at-most-two degenerate top/bottom cases, a degree-at-least-two row cannot be expressed as an intersection of other intents. A singleton row at attribute \(a\) is individually nonreducible precisely when it is the *only* singleton row there and \(B_a\le1\); two identical singleton rows can each be removed individually, even though one representative is needed in a joint reduced context. Hence, up to absolute error bounded by a constant times \(Q+1\),

\[
J-R=\#\{a:A_a\ge2,\ B_a\le1\}.
\]

For one attribute the two counts converge jointly to independent Poisson variables with respective means \(a=c e^{-\alpha c}\) and \(b=c(1-e^{-\alpha c})\). Their joint event has probability \([1-(1+a)e^{-a}]e^{-b}(1+b)\). Applying the row-replacement variance bound to this bounded local indicator sum and the four-cycle error proves the \(L^1\) discrepancy limit. Its constant is strictly positive since \(a,b>0\).

## Verification

Run `python3 verify.py` from the containing directory. The standalone checker constructs the entire concept lattice directly from Galois-closed extents; it counts join-irreducibles by lower covers, repeats the construction on the transposed relation for meet-irreducibles, and compares each with the distinct local proxy and its four-cycle error bound. It exhaustively checks 74,384 contexts at six small rectangular sizes plus the four-by-four size, including 22,882 square-free contexts, checks eight exact rational mean identities, and tests 1,500 further deterministic pseudorandom contexts. Expected terminal result begins with `VERIFY_OK`. The finite computations test the deterministic lemma and elementary mean formulas; they do not prove asymptotic concentration, which is proved above.

## Relationship to prior work

Syau, Lin and Liau characterize join-irreducible and meet-irreducible concepts using upper covers in object-intent and attribute-extent posets; that deterministic general criterion is used and credited. Their study does not analyze sparse random-context densities, four-cycle error bounds, or rates. Sakurai studies the expected *total number* of formal concepts of random contexts and a dense-case lower bound, not the numbers of irreducibles. Felde and Hanika's random-context generation work provides model motivation, not an irreducibility law. Earlier exact work on the reducibility probability of an individually selected input object is logically different: duplicate singleton rows are each individually removable but still create one distinct join-irreducible concept, producing the strictly positive correction proved here. Standard binomial asymptotics and Efron–Stein concentration are not claimed as new techniques.

## Limitations

The density and rate hold for fixed positive \(\alpha,c\), with incidence probability \(c/n\) and linearly many attributes. They do not provide a central limit theorem, a uniform estimate for growing \(c\), or joint fluctuation laws. The deterministic estimate can be coarse on graphs with many four-cycles. Finite tests are corroborative only. A literature search cannot establish absolute priority, especially against terminology from lattice reduction or random graph theory; independent external mathematical assessment remains outstanding.

## References

1. Y.-R. Syau, E.-B. Lin and C.-J. Liau, *An Order-Theoretic Study on Formal Concept Analysis*, preprint posted 13 September 2023, https://www.preprints.org/manuscript/202309.0865 ; journal version, *Axioms* **12** (2023), 1099, DOI:10.3390/axioms12121099. Relevant: Propositions 2–3.
2. T. Sakurai, *On formal concepts of random formal contexts*, arXiv:2101.11023v1 (26 January 2021), https://arxiv.org/pdf/2101.11023. Relevant: Proposition 4.1 and Theorem 5.1.
3. M. Felde and T. Hanika, *Formal Context Generation using Dirichlet Distributions*, arXiv:1809.11160v1 (28 September 2018), https://arxiv.org/abs/1809.11160. Model background.
4. J. Zhou, S. Yang, X. Wang and W. Liu, *Concept and Attribute Reduction Based on Rectangle Theory of Formal Concept*, arXiv:2111.00005v1 (29 October 2021), https://arxiv.org/abs/2111.00005. Different concept-cover reduction problem.
5. B. Ganter and R. Wille, *Formal Concept Analysis: Mathematical Foundations*, Springer, 1999. Standard concept-lattice representation and reduction background.
