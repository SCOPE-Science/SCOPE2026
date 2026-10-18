# Unlabelled census of finite commuting two-equivalence frames

## Finding
Let \(X\) be a finite set with two **named** equivalence relations \(E\) and \(F\). They *commute* when \(E\circ F=F\circ E\), with relational composition in either fixed convention. An isomorphism is a bijection preserving both \(E\) and \(F\) separately; it is **not** allowed to swap them.

Write \(u_n\) for the number of isomorphism types on an \(n\)-element set, including the empty type \(u_0=1\), and \(b_n\) for those types for which \(E\vee F\) has exactly one class. Then the following exact ordinary generating functions enumerate every finite size:

\[
\begin{aligned}
B(z)&=\sum_{r,s\geq1}\sum_{\lambda\vdash r}\sum_{\mu\vdash s}
 \frac{1}{z_\lambda z_\mu}
 \prod_{a\in\lambda}\prod_{b\in\mu}
 \left(\frac{z^{\operatorname{lcm}(a,b)}}{1-z^{\operatorname{lcm}(a,b)}}\right)^{\gcd(a,b)}
 =\sum_{m\geq1} b_m z^m,\\
U(z)&=\prod_{m\geq1}(1-z^m)^{-b_m}=\sum_{n\geq0}u_nz^n.
\end{aligned}
\]

For a partition \(\lambda\), its parts occur *with multiplicity*, \(m_d(\lambda)\) denotes the number of parts of size \(d\), and \(z_\lambda=\prod_{d\geq1}d^{m_d(\lambda)}m_d(\lambda)!\). The counts are:

| Size \(n\) | Connected types \(b_n\) | All types \(u_n\) |
| ---: | ---: | ---: |
| 0 | 0 | 1 |
| 1 | 1 | 1 |
| 2 | 3 | 4 |
| 3 | 5 | 9 |
| 4 | 10 | 25 |
| 5 | 14 | 54 |
| 6 | 27 | 136 |
| 7 | 36 | 294 |
| 8 | 64 | 684 |
| 9 | 90 | 1,476 |
| 10 | 150 | 3,271 |
| 11 | 213 | 6,958 |

The finite tables illustrate a theorem for **all** \(n\geq0\), not a conjecture extrapolated from computation.

## Assumptions and scope
A connected component means a class of the join \(E\vee F\) in the equivalence-relation lattice. A row is an \(E\)-class inside one component and a column is an \(F\)-class inside that component. A cell is their intersection. The relation names remain distinguished. The coefficients of \(B(z)\) and \(U(z)\) are formal power-series coefficients: no analytic convergence claim is needed. All matrices below have finitely many rows and columns and strictly positive integer entries.

## Proof
**1. The established matrix representation, reconstructed.** Since \(E\) and \(F\) are equivalence relations, \(E\circ F=F\circ E\) is equivalent to their common product being the join \(E\vee F\). Indeed, when they commute the product is reflexive, symmetric and transitive, and contains both relations; conversely, equality with the join trivially implies commutation. In any join-component \(C\), for any \(E\)-class \(A\subseteq C\) and \(F\)-class \(D\subseteq C\), choose \(x\in A\), \(y\in D\); membership of \((x,y)\) in \(E\circ F\) supplies a point of \(A\cap D\). Hence every cell is nonempty. Conversely, any positive-integer matrix \((m_{ij})\) specifies disjoint cells of sizes \(m_{ij}\), equivalence classes given by its rows and columns, and commuting relations: between any two worlds one can traverse an \(E\)-step followed by an \(F\)-step, or the reverse, through a nonempty intersection. The whole matrix is one join-component. This representation is stated in the 2022 work of Rumenova and Tinchev; it is **not claimed as new**.

**2. Isomorphism types.** Within a connected component, a relation-preserving bijection acts by permuting \(E\)-classes (matrix rows) and \(F\)-classes (matrix columns), and by bijections inside equal-sized cells. Consequently connected isomorphism types with \(r\) rows and \(s\) columns are precisely \(S_r\times S_s\)-orbits of positive-integer \(r\times s\) matrices. The ambient frame is an unordered finite multiset of such connected types, because an isomorphism permutes join-components.

**3. Weighted Burnside lemma.** Fix row and column permutations with respective cycle types \(\lambda\vdash r\) and \(\mu\vdash s\). The Cartesian product of a row-cycle of length \(a\) and a column-cycle of length \(b\) decomposes into \(\gcd(a,b)\) cell-orbits, each of size \(\operatorname{lcm}(a,b)\). A fixed positive-integer matrix is constant on each orbit. If the common value is \(t\geq1\), its contribution to total cell-sum is \(t\operatorname{lcm}(a,b)\). Therefore the weight series for each orbit is \(z^{\operatorname{lcm}(a,b)}/(1-z^{\operatorname{lcm}(a,b)})\). Multiplying over all row/column-cycle pairs and averaging over permutations gives exactly the displayed \(B(z)\), with cycle-type weight \(1/(z_\lambda z_\mu)\). There is no extra division by interchanging \(r\) and \(s\), since the relation symbols are named.

**4. Multiset transform.** Every frame uniquely decomposes into a multiset of connected components. For each of the \(b_m\) connected types of weight \(m\), one can choose an arbitrary nonnegative multiplicity; its series is \((1-z^m)^{-1}\). The product over all sizes and types gives \(U(z)\). Each coefficient is finite because any matrix with \(r\) rows and \(s\) columns has total size at least \(rs\), so only \(rs\leq n\) contributes through degree \(n\). This also proves that truncating the algorithm at \(rs\leq n\) is exhaustive.

## Verification
The bundled self-contained `verify.py` computes \(B(z)\) exactly with integer-partition cycle indexes and rational polynomial arithmetic, then computes the Euler product through degree 11. It separately generates **every set partition** of \(\{0,\dots,n-1\}\) for \(1\leq n\leq6\), tests the equality \(E\circ F=F\circ E\) directly using existential relational composition for all ordered pairs of worlds, and canonicalizes each passing pair by constructing its components and independently permuting matrix rows and columns. These brute-force checks give respectively \(1,4,19,117,864,7459\) labelled pairs and \(1,4,9,25,54,136\) isomorphism classes, agreeing with the generating formula. The labelled totals agree with OEIS A354458 and are prior known information, not claimed as a new result. Run `python verify.py` (Python standard library only); success prints `VERIFY_OK`.

## Relationship to prior work
Rumenova and Tinchev (January 14, 2022 slides; published paper February 8, 2022) introduce and analyze the class of frames with two commuting equivalence relations, including their decomposition into matrices of nonempty row/column cells. The present finding **starts from that representation** and counts connected types modulo separate row/column permutations, then counts arbitrary finite frames modulo isomorphism. OEIS A354458, published May 30, 2022, already counts **labelled** commuting relation pairs: it does not give the number of unlabelled isomorphism types, and the labelled totals alone do not determine orbit counts under relabeling. General Burnside and multiset principles are standard ingredients, not presented as independent discoveries. Searches did not locate a published version of the specific weighted unlabelled series or its displayed coefficients.

## Limitations
The proof treats finite carriers, two named relations, and no additional valuations or designated worlds; swapping the relation names is not an allowed isomorphism. No claim is made about other equivalence-relation pairs or asymptotics. A 2021 conference abstract on the same frame class is also prior, but its book records only a 2021 year and a July 19–24 meeting interval rather than a verified exact public-release day. The first precisely dated public reference used here is the January 14, 2022 author presentation. The authors' complete 2022 published article was not accessible for a full-page comparison; their January 2022 slide deck was inspected materially, along with an accessible publisher preview, and is a substantive source for the matrix representation. A prior unindexed exact unlabelled enumeration under another vocabulary cannot be excluded. The research review is not an independent external audit.

## References
1. Y. Rumenova and T. Tinchev, *Modal definability of some classes of modal products: Two commuting equivalence relations*, World Logic Day slides, 14 January 2022, https://www.math.bas.bg/algebra/seminarAiL/Mezhdunaroden%20den%20na%20logikata%202022/slides/YanaRumenova.pdf .
2. Y. Rumenova and T. Tinchev, *Modal Definability: Two Commuting Equivalence Relations*, Logica Universalis 16 (2022), 177–194, https://doi.org/10.1007/s11787-022-00299-4 .
3. G. Critzer, *Number of commuting pairs of equivalence relations on \([n]\)*, OEIS A354458, first posted 30 May 2022, https://oeis.org/A354458 .
4. Y. Rumenova and T. Tinchev, *Undecidability of modal definability: the class of frames with two commuting equivalence relations*, Logic Colloquium 2021 Book of Abstracts, p. 126, https://pure.uva.nl/ws/files/69687940/LC21_book_of_abstracts_19_07.pdf .
