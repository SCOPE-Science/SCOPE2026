# Roman domination polynomial of whiskered complete graphs
## Finding
For every integer \(n\ge2\), let \(H_n=K_n\odot K_1\). Write the core clique as \(c_1,\ldots,c_n\), and let \(\ell_i\) be the private leaf adjacent only to \(c_i\). A Roman dominating function is a map
\[
f:V(H_n)\to\{0,1,2\}
\]
such that every vertex labeled \(0\) has a neighbor labeled \(2\). Its weight is
\[
\omega(f)=\sum_{v\in V(H_n)}f(v).
\]
Define the Roman domination polynomial
\[
R(H_n;x)=\sum_{f}x^{\omega(f)},
\]
where the sum ranges over all Roman dominating functions.

Then
\[
R(H_n;x)=\bigl(x+3x^2+2x^3+x^4\bigr)^n-\bigl(x+2x^2+x^3\bigr)^n+\bigl(2x^2+x^3\bigr)^n.
\]
Consequently
\[
\gamma_R(H_n)=n+1,
\]
there are exactly \(n\) minimum-weight Roman dominating functions, and
\[
R(H_n;1)=7^n-4^n+3^n.
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. The corona \(K_n\odot K_1\) is the graph obtained from a clique \(K_n\) by attaching one private leaf to each clique vertex. The theorem is stated for \(n\ge2\). The exceptional graph \(H_1=K_2\) is excluded because, when no second core vertex exists, a core vertex labeled \(0\) cannot be defended by a different core vertex labeled \(2\); the uniform local factorization below therefore uses \(n\ge2\).

The result enumerates every Roman dominating function by weight. The scalar Roman domination number is included only as a corollary of the polynomial.

## Proof
Partition the Roman dominating functions according to whether at least one core vertex is labeled \(2\).

First suppose that at least one core vertex is labeled \(2\). Once this global condition holds, a pair \((c_i,\ell_i)\) can have the following local labels.

If \(f(c_i)=2\), then \(f(\ell_i)\in\{0,1,2\}\), giving local weight polynomial
\[
x^2+x^3+x^4.
\]
If \(f(c_i)=1\), then \(f(\ell_i)\in\{1,2\}\), because a leaf labeled \(0\) would have no neighbor labeled \(2\). This contributes
\[
x^2+x^3.
\]
If \(f(c_i)=0\), then \(f(\ell_i)\in\{1,2\}\). The core vertex \(c_i\) is defended by some other core vertex labeled \(2\), while the leaf again cannot be labeled \(0\). This contributes
\[
x+x^2.
\]
Thus the unrestricted local polynomial under the global existence of a core label \(2\) is
\[
T(x)=x+3x^2+2x^3+x^4.
\]
Among the assignments counted by \(T(x)^n\), those with no core label \(2\) have local polynomial
\[
U(x)=x+2x^2+x^3.
\]
Therefore the functions with at least one core label \(2\) contribute exactly
\[
T(x)^n-U(x)^n.
\]

Now suppose that no core vertex is labeled \(2\). If \(f(c_i)=0\), its private leaf must have label \(2\), because no core neighbor carries label \(2\). If \(f(c_i)=1\), its leaf may have label \(1\) or \(2\), but not \(0\). Hence the only local patterns are
\[
(0,2),\qquad(1,1),\qquad(1,2),
\]
with local weight polynomial
\[
V(x)=2x^2+x^3.
\]
These choices are independent across the \(n\) pairs, so the no-core-\(2\) functions contribute \(V(x)^n\). Adding the two disjoint cases gives the asserted polynomial.

For the minimum weight, a function in the core-\(2\) case has baseline local weight \(1\) on every pair and must replace at least one such pair by a core-\(2\) pattern of minimum local weight \(2\). Hence its weight is at least \(n+1\). Equality is attained by choosing one index \(i\), setting
\[
(f(c_i),f(\ell_i))=(2,0),
\]
and setting
\[
(f(c_j),f(\ell_j))=(0,1)
\]
for every \(j\ne i\). These are the only weight-\(n+1\) functions, so there are exactly \(n\) of them. In the no-core-\(2\) case every pair has weight at least \(2\), giving total weight at least \(2n\ge n+1\). Finally, substituting \(x=1\) gives
\[
R(H_n;1)=7^n-4^n+3^n.
\]

## Verification
The accompanying `verify.py` independently enumerates all \(3^{2n}\) labelings for each \(2\le n\le6\), tests the Roman domination condition directly from adjacency, and compares the complete weight histogram with the displayed polynomial. Across these five graph orders it checks \(597861\) labelings and \(60\) nonzero coefficient positions. It also checks the minimum weight, the exact number \(n\) of minimum functions, and the total-count formula.

The computation is a finite stress test only. The all-orders statement follows from the exhaustive case split in the proof, not from the finite enumeration.

## Relationship to prior work
Cockayne, Dreyer, Hedetniemi, and Hedetniemi introduced the standard Roman domination framework in 2004. Chambers, Kinnersley, Prince, and West subsequently studied extremal Roman domination and list \(05C69\) as the primary classification, supporting the graph-domination ownership of the present statement.

Roman domination has also been studied on corona constructions. A 2014 paper by Siva Parvathi and Maheswari treats Roman and total Roman dominating functions on coronas of a path with a star; its full text concerns a different base-and-attachment family and does not give an all-weight Roman domination polynomial for \(K_n\odot K_1\). Later rooted-product work studies Roman domination numbers on a broader graph construction; such minimum-value results do not enumerate every Roman dominating function by weight.

The Roman domination polynomial is an established enumerative refinement. A 2025 paper of Alqesmah and Gangabylaih explicitly defines the polynomial and computes it for commuting and non-commuting graphs associated with dihedral groups. Its objects and formulas do not cover the whiskered complete graphs considered here.

Targeted searches under the aliases “whiskered complete graph,” “corona \(K_n\odot K_1\),” and “Roman domination polynomial” did not locate an equivalent all-weight formula. The closest indexed results concern complete multipartite graphs, chain graphs, or other Roman-domination variants and do not imply this corona formula.

## Limitations
The theorem is specific to one pendant leaf per core vertex of a complete graph. It does not give a Roman domination polynomial for arbitrary coronas \(G\odot K_1\), for \(K_n\odot H\) with larger attachments, or for general rooted products. The proof relies essentially on the clique among the core vertices.

The literature search cannot exclude an unindexed or differently named prior computation of the same special-case polynomial. The scalar minimum \(\gamma_R(H_n)=n+1\) may also follow from broader rooted-product or corona results and is therefore not treated as the originality-bearing part of the finding.

## References
1. E. J. Cockayne, P. A. Dreyer Jr., S. M. Hedetniemi, and S. T. Hedetniemi, “Roman domination in graphs,” *Discrete Mathematics* 278 (2004), 11–22. DOI 10.1016/j.disc.2003.06.004.
2. E. W. Chambers, W. Kinnersley, N. Prince, and D. B. West, “Extremal Problems for Roman Domination,” *SIAM Journal on Discrete Mathematics* 23 (2009), 1575–1586. DOI 10.1137/070699688.
3. R. Siva Parvathi and B. Maheswari, “Roman Dominating and Total Dominating Functions of Corona Product Graph of a Path with a Star,” *International Journal of Civil Engineering and Technology* 5 (2014), 13–20.
4. A. Alqesmah and D. Gangabylaih, “On the Roman domination polynomial of the commuting and non-commuting graphs associated to the dihedral groups,” *Annals of Mathematics and Computer Science* 27 (2025), 44–54. DOI 10.56947/amcs.v27.482.
5. A. Cabrera Martínez, I. Peterin, and I. G. Yero, “Roman domination in direct product graphs and rooted product graphs,” arXiv:2105.10006 (2021).
