# Exact five-letter palindrome probabilities in order-four de Bruijn cycles

## Finding
Let \(\Sigma\) be a labeled alphabet with \(q\ge2\) symbols. Choose uniformly from all cyclic de Bruijn words \(C\) of order four over \(\Sigma\), modulo cyclic rotation. Every length-four word appears exactly once as a cyclic factor of \(C\). Let \(X(C)\) count occurrences of length-five palindromes, equivalently the cyclic factors of the form \(abcba\). Then
\[
\boxed{\mathbb E X=q^2-2-\frac2q.}
\]
More precisely, for any ordered triple \((a,b,c)\in\Sigma^3\), the probability that the particular palindrome \(abcba\) appears is zero if \(a=b=c\). Otherwise its probability depends only on the equality pattern:

| Condition on \(a,b,c\) | Probability that \(abcba\) occurs |
| --- | --- |
| \(a=b\ne c\) | \(\displaystyle\frac{q^2-q-1}{q^2(q-1)}\) |
| \(a=c\ne b\) | \(\displaystyle\frac{q^3-2q^2+2q-2}{q^3(q-1)}\) |
| \(b=c\ne a\) | \(\displaystyle\frac{(q-2)(q^2+q+1)}{q^3(q-1)}\) |
| \(a,b,c\) pairwise different | \(\displaystyle\frac{q^3-q^2-2}{q^3(q-1)}\) |

The fourth row is void for \(q=2\). Each palindrome can occur at most once because its four-symbol prefix would otherwise repeat. The expectation therefore counts distinct palindromes as well as occurrences.

## Assumptions and scope
All cycles are labeled and counted once modulo cyclic rotation; neither reversal nor alphabet relabeling is identified. Each has length \(q^4\). The probability space is uniform over these cycles, **not** over arbitrary random edge-order choices made during a traversal. The statement is valid for every integer \(q\ge2\); it is not an asymptotic statement. The name \(abcba\) denotes a five-symbol word in which the displayed variables may coincide, subject to the stated cases.

## Proof
**Step 1: Two-edge events.** Use the standard directed de Bruijn multigraph \(G\) with vertices \(\Sigma^3\) and one *labeled* edge \(xyzt\) from \(xyz\) to \(yzt\) for each \(xyzt\in\Sigma^4\). Loops are allowed. Every vertex has indegree and outdegree \(q\). Cyclic order-four de Bruijn words are precisely Euler tours of \(G\), considered up to edge-list rotation. Fix \((a,b,c)\) that is not constant, and set
\[
s=(a,b,c),\qquad v=(b,c,b),\qquad t=(c,b,a).
\]
The event that \(abcba\) occurs says that edge \(e=abcb:s\to v\) is immediately followed by edge \(f=bcba:v\to t\). The edges are distinct: equality would force \(a=b=c\).

Replace these two labeled edges by one tagged edge \(s\to t\), obtaining a balanced directed multigraph \(G'\). A cyclic Euler tour of \(G\) containing the ordered consecutive pair \((e,f)\) contracts uniquely to a cyclic Euler tour of \(G'\); expanding the tagged edge is the inverse, including if it is a loop or parallels another edge. Every outdegree in \(G'\) is \(q\), except the outdegree of \(v\), which is \(q-1\). For the standard BEST theorem, let \(\tau(H)\) denote the number of spanning in-arborescences of a balanced directed graph \(H\) rooted at any fixed vertex, with edge labels distinguished. All root cofactors are equal for balanced graphs, including the zero case. The BEST formula for cyclic Euler tours gives
\[
\mathbb P(abcba\text{ occurs})
=\frac{\tau(G')}{(q-1)\tau(G)}. \tag{1}
\]
In particular, this identity correctly returns zero when \(G'\) has no Euler tour; contraction does not presume strong connectivity.

**Step 2: A rank-one Laplacian update.** Index vertices by triples and put \(P_{xyz,yzt}=1/q\) for every \(t\in\Sigma\), with zero otherwise. This is the row-stochastic transition matrix of the uniform-shift Markov chain on triples. Let \(L=q(I-P)\) be the row Laplacian of \(G\). With \(e_u\) the unit column at vertex \(u\), the deletion of \(s\to v\) and \(v\to t\), followed by the addition of \(s\to t\), gives exactly
\[
L'=L+(e_s-e_v)(e_v-e_t)^{\mathsf T}. \tag{2}
\]
Write \(N=q^3\) and \(J=N^{-1}{\bf1}{\bf1}^{\mathsf T}\). Three random appended symbols erase the initial state, hence \(P^3=J\). Since \(PJ=JP=J\), the group inverse of \(L\) on zero-sum vectors is
\[
L^{\#}=\frac1q(I+P+P^2-3J),\qquad
LL^{\#}=L^{\#}L=I-J. \tag{3}
\]
For completeness, delete the same root row and column in \(L,L'\), and apply the ordinary matrix determinant lemma. The perturbed vectors in (2) both have coordinate sum zero. Solving \(Lx=e_s-e_v\) by \(x=L^{\#}(e_s-e_v)\), then subtracting a constant to make the root coordinate zero, shows that the determinant-lemma bilinear form is unchanged, because \((e_v-e_t)^{\mathsf T}{\bf1}=0\). Consequently,
\[
\frac{\tau(G')}{\tau(G)}=
1+(e_v-e_t)^{\mathsf T}L^{\#}(e_s-e_v). \tag{4}
\]
This argument does not require \(L'\) to be invertible on the zero-sum subspace; it uses the invertible unperturbed cofactor.

**Step 3: Evaluate the three overlaps.** Let \(\delta_{xy}=1\) when symbols \(x,y\) coincide and zero otherwise. For \(j=0,1,2\), the entry \((P^j)_{u,w}\) is \(q^{-j}\) if the length-\((3-j)\) suffix of \(u\) equals the corresponding prefix of \(w\), and is zero otherwise. Applying this to \(s,v,t\), and recalling \((a,b,c)\) is nonconstant, gives
\[
\begin{aligned}
(e_v-e_t)^{\mathsf T}(I)(e_s-e_v)&=-1-\delta_{ac},\\
(e_v-e_t)^{\mathsf T}P(e_s-e_v)&=\frac{2\delta_{ac}-\delta_{bc}-\delta_{ab}}q,\\
(e_v-e_t)^{\mathsf T}P^2(e_s-e_v)&=\frac{2\delta_{ab}-2}{q^2}.
\end{aligned}
\]
The \(J\)-term in (3) vanishes between zero-sum vectors. Equations (1)--(4) now yield the single indicator formula
\[
\mathbb P(abcba\text{ occurs})=
\frac{1}{q-1}\left[
1-\frac1q-\frac{\delta_{ac}}q+
\frac{2\delta_{ac}-\delta_{bc}-\delta_{ab}}{q^2}+
\frac{2\delta_{ab}-2}{q^3}
\right],\qquad (a,b,c)\text{ nonconstant}. \tag{5}
\]
Substitution of the four equality patterns gives precisely the four probabilities in the statement. If \(a=b=c\), then \(abcba\) has two overlapping occurrences of the four-symbol factor \(aaaa\), which cannot happen in an order-four de Bruijn cycle; its probability is therefore zero.

**Step 4: Sum the local laws.** Each of the three nonconstant patterns with exactly two equal symbols contains \(q(q-1)\) ordered triples; the pairwise-distinct pattern contains \(q(q-1)(q-2)\). Since a given palindrome can appear at most once, linearity of expectation and the four displayed probabilities give
\[
\mathbb E X=
q(q-1)(p_{ab}+p_{ac}+p_{bc})+
q(q-1)(q-2)p_{\mathrm{distinct}}
=q^2-2-\frac2q.
\]
The proof is complete.

## Verification
Run the attached standalone Python program `check_pal_mean.py` using Python 3 and SymPy. It (i) enumerates all 16 binary order-four cyclic de Bruijn words up to rotation, finding eight with zero length-five palindromes and eight with two; (ii) verifies every binary palindrome probability; (iii) independently computes exact directed Laplacian cofactors for representative equality types for \(q=2\) and \(q=3\), comparing them to formula (5); and (iv) checks the symbolic mean identity by exact rational arithmetic for \(2\le q\le15\). The cofactor computation checks the nonstandard contraction step rather than merely recomputing the expectation from its final formula.

For example, the binary cyclic word `0000101100111101` has no length-five palindromic factors, whereas `0000100110101111` has two. This explicitly shows why the five-letter statistic is not fixed by the order-four de Bruijn property alone. Computation supplements, rather than replaces, the all-alphabet proof above.

## Relationship to prior work
Orenstein's work on reverse de Bruijn coverings and Orenstein--Shamir's related reverse-complement sequence constructions use palindrome and reversal constraints together with Eulerian graph traversals. They address *shorter covering sequences* modulo reversal, not the frequency, under a uniform distribution over **ordinary** order-four de Bruijn cycles, of a specified five-letter palindrome. The fixed number of length-four palindromes in every order-four de Bruijn cycle does not imply these length-five probabilities; the two binary examples above refute such an implication. Fici and Gabory's work on generalized de Bruijn words and Burrows--Wheeler transforms supplies additional graph-theoretic context, not these local probabilities. The novelty asserted here is only the evaluated four-type law and its exact expectation, not BEST, the matrix-tree theorem, or the de Bruijn/Euler correspondence.

## Limitations
The distribution is uniform over *all* labeled cyclic de Bruijn words; a randomized Euler-tour generator need not sample this measure uniformly. The result concerns ordinary reversal palindromes of length five and order-four de Bruijn cycles, not reverse-complement palindromes, arbitrary order, variance, or the full distribution of the count. Publication-priority searches cannot exclude an equivalent result in unindexed literature. The related 2018 conference chapter was accessible in abstract and appendix but its complete publisher PDF was not obtainable; the 2020 journal extension was compared using its indexed technical sections, so uninspected material remains an originality risk. The scientific proof is self-contained subject to the classical BEST and directed matrix-tree theorems.

## References
- Y. Orenstein, *Reverse de Bruijn: Utilizing Reverse Peptide Synthesis to Cover All Amino Acid k-mers*, RECOMB 2018, first online April 18, 2018, DOI: 10.1007/978-3-319-89929-9_10; expanded journal article, *Journal of Computational Biology* 27 (2020), DOI: 10.1089/cmb.2019.0448.
- Y. Orenstein and R. Shamir, *Design of shortest double-stranded DNA sequences covering all k-mers with applications to protein-binding microarrays and synthetic enhancers*, *Bioinformatics* 29 (2013), DOI: 10.1093/bioinformatics/btt213.
- G. Fici and E. Gabory, *Generalized De Bruijn Words, Invertible Necklaces, and the Burrows--Wheeler Transform*, MFCS 2025, DOI: 10.4230/LIPIcs.MFCS.2025.48.
- The directed matrix-tree theorem and the de Bruijn--van Aardenne-Ehrenfest--Smith--Tutte (BEST) theorem are used in their standard labeled-multigraph forms.
