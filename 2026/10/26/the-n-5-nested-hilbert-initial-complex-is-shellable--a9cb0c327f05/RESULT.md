# The \(n=5\) nested-Hilbert initial complex is shellable

## Finding

Let \(V=[6]\times[5]\), so \(|V|=30\), and let \(A=k[w_{ij}:(i,j)\in V]\) over any field \(k\). Define the squarefree monomials
\[
 x_h=\prod_{i=2}^{h-1}w_{i,7-i}\prod_{i=h+1}^{6}w_{i,8-i}\quad(2\le h\le6),
\]
\[
 y_h=\prod_{i=1}^{h-1}w_{i,6-i}\prod_{i=h+1}^{6}w_{i,7-i}\quad(2\le h\le6),
\]
and
\[
 z_h=\prod_{i=3}^{h-1}w_{i,8-i}\prod_{i=h}^{6}w_{i,7-i}\prod_{i=h+1}^{6}w_{i,9-i}\quad(3\le h\le6),
\]
where an empty product is \(1\). Put
\[
 \mathfrak K_5=(x_2,\ldots,x_6,y_2,\ldots,y_6,z_3,\ldots,z_6)
\]
and let \(\Delta_5\) be its Stanley–Reisner complex. Then \(\Delta_5\) is pure and shellable: it has exactly \(130\) facets, each containing \(26\) vertices. The supplied order in `data/shelling_order.json` is a shelling order. Consequently, the Stanley–Reisner ring \(k[\Delta_5]\) is Cohen–Macaulay for every field \(k\).

## Assumptions and scope

The definition is the \(n=5\) instance of the squarefree monomial ideal in Ramkumar–Sammartano, *Rational singularities of nested Hilbert schemes*, Section 7. A c-facet is the complement in \(V\) of a facet of \(\Delta_5\); equivalently, it is a minimal vertex cover of the 14 generator supports of \(\mathfrak K_5\). Coordinates in the certificate are one-based matrix coordinates \([i,j]\). The claim concerns this finite simplicial complex only; it does not assert shellability for all \(n\).

## Proof

The cited paper proves for the family \(\Delta^{(n)}\) that every c-facet has size four, that the complex is pure of codimension four, and that its facet count is
\[
 \frac{(n-1)n(n+1)(3n-2)}{12}.
\]
At \(n=5\) this is \(130\), and the facets have size \(30-4=26\).

For the explicit certificate, the verification program constructs the 14 supports from the displayed formulas. It computes all minimal hitting sets by the complete transversal recursion: start with the empty set, process each generator, extend a cover by one vertex whenever it misses the new generator, and discard every cover containing a smaller cover. It also independently checks all \(\binom{30}{4}=27{,}405\) four-subsets. The two methods return the same 130 minimal covers, all of size four. This establishes that the listed complements are exactly the facets, not a partial sample.

Write the listed c-facets in order as \(C_1,\ldots,C_{130}\), and put \(F_j=V\setminus C_j\). The pure shelling criterion says that for every \(i<j\), there must be some \(k<j\) with
\[
 F_i\cap F_j\subseteq F_k\cap F_j,\qquad |F_k\cap F_j|=25.
\]
Since every c-facet has size four, the second condition is equivalent to \(|C_k\cup C_j|=5\). The inclusion is equivalent to \(C_k\setminus C_j\subseteq C_i\setminus C_j\). The program checks this criterion directly for every earlier/current facet pair, and separately checks the equivalent complement condition used to construct the order. Both checks pass for all 130 facets. Thus the order is a shelling. Pure shellability implies Cohen–Macaulayness of the Stanley–Reisner ring over every field.

## Verification

Run `python verify.py` from the artifact directory. It uses only the Python standard library and reconstructs the order deterministically. The recorded run reports: 30 vertices; 14 generators; 27,405 four-subsets examined; 130 minimal hitting sets, all of size four; agreement between full transversal recursion and four-subset enumeration; 130 facets of size 26; and `direct_facet_shelling_check=PASS`. The program also checks that the stored certificate exactly matches the reconstructed order.

## Relationship to prior work

Ramkumar–Sammartano prove the general purity and facet-count statements and establish Cohen–Macaulayness in characteristic zero, but explicitly ask whether the complex is shellable or vertex-decomposable (Question 7.13; see also Question 9.7). Their paper does not provide a shelling order for \(n=5\). This result resolves the shellability question for that one parameter value; it does not resolve the uniform question for all \(n\). Searches in published-finding corpus for the paper title, the \(n=5\) parameter, the Stanley–Reisner description, and the shellability question returned no exact matching finding. The closest returned complexes have different defining data.

## Limitations

This is a finite certificate for \(\Delta_5\), not a proof of shellability for \(\Delta^{(n)}\) at arbitrary \(n\). The search for prior work was bounded to the accessible primary paper and targeted semantic/database searches; absence of a search hit alone is not a novelty proof. Independent audit has not been performed.

## References

Ritvik Ramkumar and Alessio Sammartano, “Rational singularities of nested Hilbert schemes,” arXiv:2109.09002v1, first publicly posted 18 September 2021, especially Section 7 (definition of \(\mathfrak K\), Theorem 7.10, Corollary 7.12, Question 7.13) and Section 9.3 (Question 9.7). https://arxiv.org/abs/2109.09002
