# Total Roman \(\{2\}\) weight enumerator of crown graphs

## Finding

For every integer \(n\ge 3\), let \(\operatorname{Cr}_n=K_{n,n}-M\) be the crown graph obtained by deleting the paired perfect matching from a complete bipartite graph. Its two labeled vertex classes are \(\{a_1,\ldots,a_n\}\) and \(\{b_1,\ldots,b_n\}\); the edge \(a_i b_j\) exists precisely when \(i\ne j\).

Let \(\mathcal T_n(z)=\sum_f z^{\omega(f)}\), summed over all total Roman \(\{2\}\)-dominating functions \(f\) on \(\operatorname{Cr}_n\), where \(\omega(f)=\sum_v f(v)\). Define the following explicit polynomials, all depending on \(n\):

\[
\begin{aligned}
T(z)&=1+z+z^2,\\
R_n(z)&=T(z)^n-1-nz-\left(n+\binom n2\right)z^2-n(n-1)z^3,\\
F_{1,n}(z)&=(z+z^2)T(z)^{n-1}-z-nz^2-2(n-1)z^3,\\
F_{2,n}(z)&=(z+z^2)^2T(z)^{n-2}-z^2-2z^3.
\end{aligned}
\]

Then the **complete weight polynomial** is

\[
\boxed{\begin{aligned}
\mathcal T_n(z)={}&R_n(z)^2+n(n-1)z^2F_{2,n}(z)\\
&+2n(n-1)z^3F_{1,n}(z)\\
&+\binom n2z^4+2n(n-1)z^5+n^2(n-1)z^6.
\end{aligned}}
\]

In particular, the minimum total Roman \(\{2\}\) weight is \(4\), and the complete counts of minimum- and next-weight functions are

\[
[z^4]\mathcal T_n(z)=\binom n2,\qquad [z^5]\mathcal T_n(z)=n^2(n-1).
\]

Every minimum function labels, with value \(1\), exactly the two vertices indexed by one two-element subset on **each** side of the bipartition, and labels everything else \(0\). This minimum value is consistent with, and in principle also obtainable from, established domination-number inequalities; the contribution here is the full enumerator and its exact multiplicities.

The total number of admissible functions has the compact closed form

\[
\boxed{\mathcal T_n(1)=9^n-(11n^2+25n+18)3^{n-2}
+\frac{9n^4-14n^3+39n^2-2n+4}{4}.}
\]

Consequently, the fraction of all ternary labelings that are admissible equals

\[
1-\frac{11n^2+25n+18}{9\cdot3^n}
+O\!\left(\frac{n^4}{9^n}\right)
\]

as \(n\to\infty\). Thus the excluded proportion decays exponentially even though each crown graph has \(2n\) vertices.

## Assumptions and scope

All graphs are finite, simple, undirected, with the indicated labeled vertices. The integer \(n\) is at least three. A function \(f:V(\operatorname{Cr}_n)\to\{0,1,2\}\) is total Roman \(\{2\}\)-dominating if (i) every vertex \(v\) with \(f(v)=0\) satisfies \(\sum_{u\in N(v)}f(u)\ge2\), and (ii) every vertex with a positive label has a neighbor with a positive label. The weight is the total sum of labels. Each labeling, including its distinct named vertices, is counted exactly once. No quotient by graph automorphisms is taken.

## Proof

**1. A forced support condition.** Write \(A_i=f(a_i)\), \(B_i=f(b_i)\). Let \(s_A\) and \(s_B\) denote the number of positive labels on the respective sides. Any admissible function satisfies \(s_A,s_B\ge2\). Indeed, if only one vertex \(b_j\) is positive on the \(B\)-side, vertex \(a_j\), which has no neighbors in the positive \(B\)-support, fails either the zero-defense condition (if \(A_j=0\)) or the positive-neighbor condition (if \(A_j>0\)). If there is no positive \(B\)-vertex, every positive \(A\)-vertex is isolated among positives, while the all-zero assignment fails defense. Symmetry gives the other side. Conversely, when both side supports have size at least two, every positive vertex has a positive neighbor: among two positive vertices on the opposite side, at least one has a different index.

**2. The three classes of one-side assignments.** Fix the \(B\)-side and let \(W_B=\sum_i B_i\). Zero-defense at \(a_i\) is precisely \(W_B-B_i\ge2\). Restricting to side assignments with at least two positive labels, there are three mutually disjoint types:

* **Robust:** \(W_B\ge4\), or \(W_B=3\) consisting of three labels equal to \(1\). In either case, \(W_B-B_i\ge2\) for every index. The weight enumerator is \(R_n(z)\). It is obtained by subtracting from \(T(z)^n\) the empty labeling, singleton positive labelings, two \(1\)'s of weight two, and ordered \(2,1\) pairs of weight three.
* **Weak-two:** exactly two \(1\)'s, at a two-element index set \(I\); this side has weight \(2\) and requires every opposite label indexed by \(I\) to be positive.
* **Weak-three:** one \(2\) at an index \(i\) and one \(1\) at an index \(j\ne i\); this side has weight \(3\) and requires the opposite label at \(i\) to be positive.

The same classification applies with the sides exchanged. These cases are exhaustive: weight below two cannot support two positive vertices; the remaining weight-two and weight-three cases are exactly those described.

**3. Count robust assignments with required positive positions.** If one particular index must be positive, the unrestricted side polynomial is \((z+z^2)T(z)^{n-1}\). Delete all assignments that are not robust: a singleton \(1\) or \(2\) at that index, the \(n-1\) weak-two assignments containing it, and the \(2(n-1)\) weak-three assignments containing it. This gives exactly \(F_{1,n}(z)\). When two specified indices must be positive, the unrestricted polynomial is \((z+z^2)^2T(z)^{n-2}\). Its nonrobust assignments are just the all-\(1\) pair and the two \(2,1\) assignments on those indices; removing them gives \(F_{2,n}(z)\).

**4. Count the disjoint global regimes.** Two robust sides contribute \(R_n^2\). A weak-two side and a robust opposite side contribute \(2\binom n2z^2F_{2,n}=n(n-1)z^2F_{2,n}\), accounting for either orientation. A weak-three side and a robust opposite side contribute \(2n(n-1)z^3F_{1,n}\). For two weak-two sides, the two required index sets must coincide, yielding \(\binom n2z^4\). For a weak-two side paired with a weak-three side, their two-element supports must coincide; there are \(2n(n-1)\) choices including orientation, yielding \(2n(n-1)z^5\). Finally, for two weak-three sides, choose the first ordered \(2,1\) pair in \(n(n-1)\) ways. If its \(2\)-index is \(i\) and \(1\)-index is \(j\), the opposite \(2\)-index must be either \(i\) (then its \(1\)-index has \(n-1\) choices) or \(j\) (then its \(1\)-index must be \(i\)). Thus there are exactly \(n\) choices for the second side, producing \(n^2(n-1)z^6\). Summing the disjoint cases proves the boxed polynomial.

**5. Minimum weight, total count and asymptotics.** Each side has at least two positive labels, so every admissible function weighs at least four. Weight four forces two labels \(1\) on each side; by step 4 their two supports coincide, giving exactly \(\binom n2\) functions. Taking the coefficient of degree five in the displayed polynomial gives \(n^2(n-1)\). Evaluation at \(z=1\), with \(T(1)=3\), \(R_n(1)=3^n-1-2n-3\binom n2\), \(F_{1,n}(1)=2\cdot3^{n-1}-3n+1\), and \(F_{2,n}(1)=4\cdot3^{n-2}-3\), simplifies to the closed form above. Dividing by the total number \(3^{2n}=9^n\) of ternary assignments proves the asymptotic.

## Verification

The standalone standard-library program `verify.py` constructs the crown graph by adjacency, tests both original feasibility conditions directly, exhaustively enumerates all ternary assignments for \(n=3,4,5,6\), and compares **every** coefficient against the polynomial formula. The complete search covers \(3^6+3^8+3^{10}+3^{12}=597{,}780\) assignments. Valid totals are respectively \(328, 4422, 48974, 488266\). It separately checks polynomial identities, nonnegativity, low-degree coefficients, and the total-count expression for \(7\le n\le60\). Run `python3 verify.py`; expected output is in `verify_output.txt`. These finite checks are supplementary to the proof for arbitrary \(n\).

## Relationship to prior work

Cabrera García et al., *Total Roman \(\{2\}\)-domination in graphs* (online 28 November 2019; freely available manuscript arXiv:2101.02537), introduce the underlying parameter and obtain general bounds, equivalences with double domination at equality, and results on paths, cycles and trees. Ahangar et al., *Total Roman \(\{2\}\)-Dominating Functions in Graphs* (freely available manuscript arXiv:2402.07968), present a related treatment of general bounds and complexity. Neither inspected document supplies the crown-graph all-weight polynomial above. A published enumerator for **complete multipartite** graphs uses a different adjacency relation; \(\operatorname{Cr}_n\) is a proper spanning subgraph of \(K_{n,n}\), not a complete multipartite graph, so its full function enumerator does not follow by substituting part sizes. Published results for perfect Roman domination of crown graphs concern a different zero-defense condition and likewise do not imply the polynomial here. Prior general inequalities can account for the minimum numerical value, so no claim of discovery is made for that scalar alone.

## Limitations

The theorem applies to ordinary total Roman \(\{2\}\)-dominating functions on named crown graphs with \(n\ge3\); the small disconnected case \(n=2\) is excluded. It is not a formula for total Roman domination, perfect Roman domination, or all bipartite graphs. The proof does not classify functions up to graph automorphism. A relevant 2024 paper on Cartesian products of paths and cycles and a 2024 survey could not be fully inspected in this examination; no claim about their whole-document contents is inferred from abstracts. Equivalent results in unindexed literature remain a priority risk. Independent mathematical validation has not been performed.

## References

1. S. Cabrera García, A. Cabrera Martínez, F. A. Hernández Mira, I. G. Yero, *Total Roman \(\{2\}\)-domination in graphs*, *Quaestiones Mathematicae* 44 (2021), 411–434, first published online 28 November 2019. DOI: 10.2989/16073606.2019.1695230. Freely available manuscript: https://arxiv.org/pdf/2101.02537.
2. H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami, J. C. Valenzuela-Tripodoro, *Total Roman \(\{2\}\)-Dominating Functions in Graphs*, *Discussiones Mathematicae Graph Theory* 42 (2022), 937–958. DOI: 10.7151/dmgt.2316. Freely accessible text: https://rodin.uca.es/bitstream/10498/24377/1/SC2020_308.pdf.
3. Q. Chen, *Algorithmic aspect on total Roman \(\{2\}\)-domination of Cartesian products of paths and cycles*, *RAIRO–Operations Research* 58 (2024), 2029–2044. DOI: 10.1051/ro/2023121. Only the abstract was accessible in this examination.
4. *Survey on Roman \(\{2\}\)-Domination*, *Mathematics* 12 (2024), article 2771. DOI and indexing: https://www.mdpi.com/2227-7390/12/17/2771. The relevant indexed section was consulted; full-text retrieval was restricted.
