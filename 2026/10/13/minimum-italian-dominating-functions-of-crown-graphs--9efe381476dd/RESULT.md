# Minimum Italian dominating functions of crown graphs

## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and deleted pairs \(a_i b_i\). For an Italian (Roman \({2}\)) dominating function \(f:V(\operatorname{Cr}_n)\to\{0,1,2\}\), the minimum weight is \(3\) when \(n=3\) and \(4\) when \(n\ge4\). For \(n=3\), the only minimum functions assign label \(1\) to every vertex of one bipartition class and label \(0\) to the other. For \(n=4\), there are exactly \(12\) minimum functions: the two all-one-side functions, the four functions with \(f(a_i)=f(b_i)=2\) for one index \(i\), and the six functions assigning label \(1\) to \(a_i,b_i,a_j,b_j\) for one two-element index set \(\{i,j\}\). For every \(n\ge5\), the minimum functions are exactly the latter two types, so their number is \(n+\binom{n}{2}=\binom{n+1}{2}\).

Equivalently, once \(n\ge5\), every optimum labeling has side-weight \(2\) on both bipartition classes, and the deleted perfect matching forces the two sides to use the same index support. This is the structural feature lost in the complete bipartite graph.

## Assumptions and scope
The crown graph is \(\operatorname{Cr}_n=K_{n,n}-M_n\), where \(M_n=\{a_i b_i:1\le i\le n\}\). An Italian dominating function, equivalently a Roman \({2}\)-dominating function, is a map \(f:V\to\{0,1,2\}\) such that every vertex labeled \(0\) receives total label weight at least \(2\) from its open neighborhood. Its weight is \(\omega(f)=\sum_{v\in V}f(v)\), and \(\gamma_I(G)\) is the minimum weight.

The claim concerns only minimum-weight functions. It does not enumerate all feasible Italian dominating functions of larger weight.

## Proof
Write \(x_i=f(a_i)\), \(y_i=f(b_i)\), and let \(W_A=\sum_i x_i\) and \(W_B=\sum_i y_i\). Because \(a_i\) is adjacent to every vertex of \(B\) except \(b_i\), a zero-labeled \(a_i\) is feasible exactly when
\[
W_B-y_i\ge2.
\]
Similarly, a zero-labeled \(b_i\) is feasible exactly when
\[
W_A-x_i\ge2.
\]
These two inequalities are the only feasibility conditions.

For \(n=3\), assigning label \(1\) to all vertices of one side and label \(0\) to the other has weight \(3\), so \(\gamma_I(\operatorname{Cr}_3)\le3\). A labeling of total weight at most \(2\) has one side of weight at most \(1\). Every zero on the opposite side would then see neighborhood weight at most \(1\), so that opposite side would have to contain no zero. It would therefore have weight at least \(3\), a contradiction. Hence the minimum is \(3\). At weight \(3\), any split with positive weight on both sides has a side of weight at most \(1\) and therefore fails by the same argument. Thus the only minimum functions are the two all-one-side functions.

Now let \(n\ge4\). There are weight-4 functions: for any index \(i\), assigning label \(2\) to \(a_i\) and \(b_i\) and label \(0\) elsewhere is feasible. Therefore \(\gamma_I(\operatorname{Cr}_n)\le4\). If a labeling had total weight at most \(3\), one side would have weight at most \(1\). Every zero on the other side would then fail, so all \(n\) vertices on that other side would have to be positive, forcing total weight at least \(n\ge4\). Thus no labeling of weight at most \(3\) is feasible, and \(\gamma_I(\operatorname{Cr}_n)=4\).

It remains to classify the weight-4 labelings. If one side has weight at most \(1\), the other side must contain no zero. For \(n\ge5\) this is impossible at total weight \(4\). For \(n=4\), it yields exactly the two labelings that are all \(1\) on one side and all \(0\) on the other. All remaining minimum functions have \(W_A=W_B=2\).

A side of weight \(2\) has exactly one of two forms: a single label \(2\), or two labels \(1\). Since \(W_B=2\), every zero \(a_i\) requires \(y_i=0\); hence every nonzero index on side \(B\) must also be nonzero on side \(A\). By symmetry, the nonzero index sets on the two sides must be equal. Equality of supports rules out a mixed single-4versus-double support. If the common support has size \(1\), both supported vertices carry label \(2\), giving \(n\) functions. If it has size \(2\), all four supported vertices carry label \(1\), giving \(\binom{n}{2}\) functions. This proves the classification and the stated counts.

## Verification
The accompanying `verify.py` independently enumerates every \(\{0,1,2\}\)-labeling of total weight at most \(4\) for \(3\le n\le12\). It checks the graph-neighborhood definition directly, checks the two side-weight inequalities above, verifies the minimum weight, and verifies both directions of the claimed classification. The replay result is:

`VERIFY_OK n_range=3..12 low_weight_labelings=62067 lemma_checks=62067 classification_checks=358 expected_form_checks=358 max_order=24`

The computation is a finite consistency check; the proof above supplies the quantification over every \(n\ge3\).

## Relationship to prior work
Chellali, Haynes, Hedetniemi, and McRae introduced Roman \({2}\)-domination in 2016. Their general theory supplies the definition, comparisons with other domination parameters, and complexity results; the accessible indexed material does not supply the crown-graph minimum-function classification proved here. A 2024 survey describes itself as assembling nearly every published work on Roman \({2}\)-domination; targeted searches of its accessible text and independent web searches did not locate a crown-graph, bipartite-Kneser \(H(n,1)\), or complete-bipartite-minus-perfect-matching formula matching this statement.

A published database result gives the full Roman \({2}\)-weight enumerator for complete multipartite graphs, including \(K_{n,n}\). It does not imply the present claim because \(\operatorname{Cr}_n\) is obtained by deleting a perfect matching and is not complete multipartite for \(n\ge3\). The proof above identifies the exact new obstruction caused by those deleted edges: at optimum weight \(2+2\), support indices on the two sides must align.

## Limitations
The originality comparison is evidence-based rather than a proof of absence from all literature. The publisher PDF of the 2016 foundational paper was not available through the accessible full-text path during this check; indexed portions, repository metadata, a broad 2024 survey, published-finding corpus searches, and targeted alias searches were inspected instead. An older or poorly indexed equivalent result could therefore still exist. The result concerns ordinary Italian/Roman \({2}\)-domination, not independent, total, secure, perfect, or covering variants.

## References
1. M. Chellali, T. W. Haynes, S. T. Hedetniemi, and A. A. McRae, “Roman \({2}\)-domination,” *Discrete Applied Mathematics* 204 (2016), 22–28. DOI: 10.1016/j.dam.2015.11.013. Exact-day public repository record: 2016-05-11, https://dc.etsu.edu/etsu-works/15031/.
2. A. Almulhim, B. Al Subaiei, and S. R. Mondal, “Survey on Roman \({2}\)-Domination,” *Mathematics* 12 (2024), 2771. DOI: 10.3390/math12172771.
3. L. Fernández and V. Leoni, “New complexity results on Roman \({2}\)-domination,” *RAIRO - Operations Research* 57 (2023), 1905–1912. DOI: 10.1051/ro/2023049. This paper records MSC 05C69 for Roman \({2}\)-domination.
