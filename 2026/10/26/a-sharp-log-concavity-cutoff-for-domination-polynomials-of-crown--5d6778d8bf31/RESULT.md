# A sharp log-concavity cutoff for domination polynomials of crown graphs

## Finding

Let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph, obtained by deleting a perfect matching from the complete bipartite graph on two labelled parts of size \(n\). For every integer \(n\ge2\), its ordinary domination polynomial is
\[
D(\operatorname{Cr}_n;t)=\left((1+t)^n-1-nt\right)^2+2nt^2(1+t)^{n-1}-nt^2+2t^n.
\]
Its full coefficient sequence is log-concave **if and only if \(2\le n\le12\)**. For \(n\ge13\), the failure occurs already between degrees \(2\), \(3\), and \(4\), and persists for all larger orders. Nevertheless, for every \(n\ge4\), the coefficients on its positive support increase strictly up to the unique mode at degree \(n\), then decrease strictly.

In contrast, for every \(n\ge2\), the total-domination polynomial is log-concave on its nonzero interval of degrees:
\[
D_{\mathrm t}(\operatorname{Cr}_n;t)=\left((1+t)^n-1-nt\right)^2.
\]
The formula for the total-domination polynomial is an earlier result of Shyama and Anil Kumar; the assertion here concerns the contrast with the ordinary domination-polynomial cutoff.

## Assumptions and scope

All graphs are finite, simple and undirected; their vertices are labelled. Write the bipartition as \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with \(a_i b_j\) an edge exactly when \(i\ne j\). A set \(S\) is **dominating** if each vertex lies in \(S\) or has a neighbour in \(S\), and **total dominating** if every vertex has a neighbour in \(S\). Write \(D(G;t)=\sum_{k=0}^{|V(G)|}d_k(G)t^k\). A nonnegative sequence is log-concave if \(d_k^2\ge d_{k-1}d_{k+1}\) for all interior indices; zero coefficients at the beginning are allowed. Unimodality refers to weak increase followed by weak decrease of the coefficient sequence.

The crown graph is connected, regular bipartite and vertex-transitive for \(n\ge3\). The case \(n=2\) is the disjoint union of two edges and is included explicitly in the formulas.

## Proof

**Classification of dominating sets.** Set \(s=|S\cap A|\) and \(u=|S\cap B|\). If \(s,u\ge2\), each unselected vertex has a selected neighbour in the opposite part; the generating polynomial of this class is \(A_n(t)^2\), where \(A_n(t)=(1+t)^n-1-nt\). If \(s=1\) and \(u\ge1\), let \(a_i\) be the selected vertex of \(A\). The unselected vertex \(b_i\) has no neighbour in \(S\cap A\), so domination requires \(b_i\in S\). This condition suffices for all vertices. These sets contribute \(nt^2(1+t)^{n-1}\). The symmetric \(u=1\) case contributes the same polynomial. The overlap consists of the \(n\) matched nonedges \(\{a_i,b_i\}\), counted twice, hence subtract \(nt^2\). Finally, a dominating set supported entirely on one side must contain that whole side; these two sets contribute \(2t^n\). This proves the claimed identity without omissions or hidden multiplicities.

For \(n\ge5\), its initial coefficients are
\[
d_2=n,\qquad d_3=2n(n-1),\qquad
 d_4=\binom n2^2+2n\binom{n-1}2.
\]
Consequently,
\[
\Delta_{n,3}:=d_3^2-d_2d_4
=-\frac{n^2(n-1)(n^2-13n+8)}4.
\]
For each integer \(n\ge13\), the factor \(n^2-13n+8\) is strictly positive (it equals \(8\) at \(n=13\), and then increases). Thus \(\Delta_{n,3}<0\), proving non-log-concavity for the entire infinite tail. The exceptional low orders \(n=2,3,4\) are not inserted into the displayed coefficient identities.

**Exhaustive positive cutoff.** The coefficient of \(t^k\) in the identity is the exact integer
\[
d_k=\sum_{\substack{2\le i\le n\\2\le k-i\le n}}
\binom ni\binom n{k-i}+2n\binom{n-1}{k-2}-n\mathbf1_{k=2}+2\mathbf1_{k=n},
\]
where out-of-range binomial coefficients vanish. Hence the eleven orders \(2\le n\le12\) require finitely many, explicitly specified integer inequalities, not an extrapolation. For reproducibility, the following table gives the smallest interior minor \(d_k^2-d_{k-1}d_{k+1}\), for \(3\le k\le2n-1\), together with its location. The standalone source file `verify.py` computes all individual coefficients and inequalities directly with integer arithmetic.

| \(n\) | Minimum interior minor | Attained at \(k\) |
| ---: | ---: | ---: |
| 2 | 12 | 3 |
| 3 | 21 | 5 |
| 4 | 36 | 7 |
| 5 | 55 | 9 |
| 6 | 78 | 11 |
| 7 | 105 | 13 |
| 8 | 136 | 15 |
| 9 | 171 | 17 |
| 10 | 210 | 19 |
| 11 | 253 | 21 |
| 12 | 300 | 23 |

Every entry is positive, and the initial degree and remaining zero coefficients also satisfy log-concavity. This establishes the positive side of the exact cutoff.

**Unimodality despite loss of log-concavity.** Let \(r_k=d_k/\binom{2n}k\). Coupling a random uniformly chosen \(k\)-subset with a random uniformly chosen \((k+1)\)-superset shows that \(r_k\) is nondecreasing, because domination is preserved under adding vertices. Since \(\binom{2n}k\) is strictly increasing for \(k<n\) and \(d_2>0\), this implies \(d_2<d_3<\cdots<d_n\), provided \(n\ge4\). For \(k\ge n+1\), every \(k\)-set is dominating because every closed neighbourhood has size \(n\), so \(d_k=\binom{2n}k\) and the tail is strictly decreasing. At degree \(n\), exactly the \(2n\) complements of distinct closed neighbourhoods fail domination, hence \(d_n=\binom{2n}n-2n\). The strict peak inequality \(d_n>d_{n+1}\) follows from \(\binom{2n}n>2n(n+1)\), true at \(n=4\) and preserved by the usual central-binomial recurrence for larger \(n\). Thus the unique mode is degree \(n\) for all \(n\ge4\), with strict increase and decrease on the nonzero coefficient interval. The low-order coefficient sequences are \((4,4,1)\) and \((3,14,15,6,1)\) on their positive supports for \(n=2,3\), respectively.

**Total domination.** A set totally dominates \(\operatorname{Cr}_n\) precisely when it contains at least two vertices in each bipartition class, proving the previously published identity \(D_{\mathrm t}=A_n^2\). The coefficient sequence of \(A_n(t)\) is the contiguous truncation \(\binom n2,\binom n3,\ldots,\binom nn\), preceded by zeros; it is log-concave with no internal zeros. Convolution of two nonnegative log-concave sequences with interval support preserves log-concavity: their Toeplitz matrices have nonnegative contiguous \(2\times2\) minors, and the Cauchy–Binet identity applies to their matrix product. The convolution is precisely the coefficient sequence of \(A_n^2\), proving the contrast for every \(n\ge2\).

## Verification

The standalone `verify.py` uses only the Python standard library and integer arithmetic. It reconstructs the ordinary and total polynomials by direct closed-neighbourhood tests of every labelled vertex subset for orders \(2\le n\le7\) (21,840 subsets). Separately it checks every log-concavity minor for \(2\le n\le12\), the symbolic degree-three identity and its negative sign for \(13\le n\le60\), and the mode and binomial-tail identities for \(4\le n\le60\). The expected terminal signature is `VERIFY_OK`. These finite tests certify the bounded exceptional range and serve as independent reproducibility checks; the infinite-order conclusions use the symbolic formulas proved above.

For \(n=13\), the first coefficient obstruction is explicit: \((d_2,d_3,d_4)=(13,312,7800)\), with \(312^2-13\cdot7800=-4056\). At \(n=12\), the same minor is \(1584>0\).

## Relationship to prior work

Omar's 2026 work on unimodality of domination polynomials formulates the coefficient-shape problem and proves log-concavity for threshold graphs; it does not cover the non-threshold crown family. Du, Heilman and Panova provide other graph families with non-log-concave domination sequences, but the present exact regular, vertex-transitive bipartite cutoff is not identified in their inspected discussion. The total-domination polynomial of this crown family is already explicitly given in Theorem 2.17 of Shyama and Anil Kumar (2019), and is **not** claimed as a new formula here. Beaton and Brown provide the general normalized-coefficient monotonicity used in the unimodality argument. Earlier studies of domination roots of related graphs, including Brown–Tufts, leave a residual literature-priority risk; the equivalent cutoff was not located in accessible materials.

## Limitations

This theorem concerns ordinary and total dominating sets of the crown family only. It does not classify all regular bipartite graphs or explain log-concavity for arbitrary graph classes. The bounded proof for \(2\le n\le12\) uses transparent finite exact-integer verification; it is a complete finite check, not a closed analytic positivity inequality uniform over that bounded range. The prior-work assessment is bounded by accessible source material; independent historical-priority checks and independent proof review have not been performed.

## References

1. Mohamed Omar, *New Perspectives on the Unimodality of Domination Polynomials*, arXiv:2601.14494v1 (first posted 2026-01-20), https://arxiv.org/html/2601.14494v1.
2. Alina Du, Steven Heilman, Greta Panova, *Trees and Graphs with Non Log-concave Dominating Set Sequence via AI Tools*, arXiv:2605.02193v1 (2026), https://arxiv.org/html/2605.02193v1.
3. Shyama M. P. and Anil Kumar V., *Total Domination Stable Graphs*, 2019, Theorem 2.17, https://fs.unm.edu/IJMC/TotalDominationStableGraphs.pdf.
4. Iain Beaton and Jason I. Brown, *On the Unimodality of Domination Polynomials*, arXiv:2012.11813, https://arxiv.org/abs/2012.11813.
5. Jason I. Brown and Julia Tufts, *On the Roots of Domination Polynomials*, Graphs and Combinatorics 30 (2014), 527–547, https://doi.org/10.1007/s00373-013-1306-z (relevant prior roots paper; full text not inspected).
