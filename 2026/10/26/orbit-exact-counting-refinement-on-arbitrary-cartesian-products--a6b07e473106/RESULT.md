# Orbit-exact counting refinement on arbitrary Cartesian products of stars

## Finding
For every integer \(k\ge 1\) and arbitrary integers \(p_1,\ldots,p_k\ge 2\), let
\[
G=K_{1,p_1}\square K_{1,p_2}\square\cdots\square K_{1,p_k},
\]
where \(\square\) is the graph Cartesian product. Start ordinary simultaneous counting colour refinement (one-dimensional Weisfeiler–Leman) with **all vertices the same colour**. After at most \(3k+1\) rounds its colour classes are **exactly** the automorphism orbits of \(G\), regardless of the factor sizes.

For each distinct integer \(p\) among the factor sizes, put \(m_p=|\{i:p_i=p\}|\). If \(v\) has exactly \(j_p\) noncentral (leaf) coordinates among its \(m_p\) factors of size \(p\), then its orbit—and its final colour class—has cardinality
\[
\prod_p\binom{m_p}{j_p}p^{j_p}.
\]
Consequently the exact number of stable colours is
\[
\prod_p(m_p+1).
\]

The recovery bound depends on the **number of factors**, not their leaf counts. It holds even when the factors have very different degrees; no distinguished initial vertex is required.

## Assumptions and scope
All graphs are finite, simple, undirected, and unweighted. The star \(K_{1,p}\) has a unique centre \(0\) and \(p\) leaves \(1,\ldots,p\); the restriction \(p\ge2\) guarantees that its centre is identifiable. Cartesian adjacency changes exactly one coordinate along one star edge.

Define \(c_0\) to be the constant vertex colouring and set \(c_{t+1}(v)=(c_t(v),\{\!\{c_t(w):w\sim v\}\!\})\), with identical keys assigned identical fresh colours. The claimed round bound counts these synchronous updates from \(t=0\).

## Proof
**1. Orbit classification without relying on a product automorphism theorem.** Let \(r=(0,\ldots,0)\). A vertex with leaf-coordinate set \(S\subseteq\{1,\ldots,k\}\) has degree \(\sum_i p_i-\sum_{i\in S}(p_i-1)\). Thus \(r\) is the unique vertex of maximum degree and every graph automorphism fixes \(r\).

The neighbours of \(r\) fall into coordinate blocks \(B_i\) of size \(p_i\). Two distinct neighbours belong to **different** blocks precisely when they have a common neighbour other than \(r\): this common neighbour is the unique two-leaf tuple obtained by changing both coordinates. Hence any automorphism permutes blocks of equal size, and may permute leaves within each block. Conversely all these permutations extend to Cartesian-product automorphisms. Finally, each vertex \(v\) is uniquely determined by the set of neighbours of \(r\) that lie on a shortest \(r\)-to-\(v\) path: the members of this set specify its nonzero coordinates and leaf values. Therefore the automorphism orbits are exactly the vectors \((j_p)_p\), with \(0\le j_p\le m_p\). Counting choices yields the stated orbit sizes and number of orbits.

**2. Walk counts lie below colour refinement.** For a colouring with \(r\) given a singleton initial colour, an induction on \(t\) shows that the colour of \(v\) at round \(t\) determines \((A^\ell)_{rv}\) for every integer \(0\le\ell\le t\), where \(A\) is the adjacency matrix. At round zero this is the singleton-root indicator; at each successive round a sum of the known length-\(\ell\) counts over neighbours gives the length-\(\ell+1\) count. Since \(r\) becomes singleton after one update of the **unmarked** colouring, a rooted bound of \(t\) implies an unmarked bound of \(t+1\).

**3. Product-walk generating function.** Put
\[
F_v(z)=\sum_{\ell\ge0}\frac{(A^\ell)_{rv}}{\ell!}z^\ell=(e^{zA})_{rv}.
\]
The adjacency matrices of Cartesian factors act in different tensor coordinates and commute. The star factor satisfies
\[
(e^{zA_{K_{1,p}}})_{0,0}=\cosh(\sqrt p\,z),\qquad
(e^{zA_{K_{1,p}}})_{0,a}=\frac{\sinh(\sqrt p\,z)}{\sqrt p}
\quad(1\le a\le p).
\]
Writing \(S=S(v)\) and \(s=|S|\), obtain
\[
F_v(z)=\left(\prod_{i=1}^k\cosh(\sqrt{p_i}\,z)\right)z^s
\prod_{i\in S}h(p_i z^2),\qquad
h(u)=\frac{\tanh\sqrt u}{\sqrt u},\quad h(0)=1.
\]

**4. All power sums are visible with a bounded delay.** The classical product identities for \(\sinh\) and \(\cosh\) give the convergent power series near zero
\[
\log h(u)=\sum_{j\ge1}a_j u^j,\qquad
 a_j=\frac{(-1)^{j+1}(2-4^j)\zeta(2j)}{j\pi^{2j}}\ne0.
\]
Indeed, expand the logarithms of \(\sinh z/z=\prod_{n\ge1}(1+z^2/(\pi n)^2)\) and \(\cosh z=\prod_{n\ge1}(1+4z^2/(\pi(2n-1))^2)\). The displayed coefficients follow by summing even reciprocal powers of all and of odd positive integers. All factors here are analytic near zero.

If \(F_v\) and \(F_w\) have identical Taylor coefficients through order \(3k\), their lowest nonzero orders give \(|S(v)|=|S(w)|=s\). Divide by the common nonvanishing \(\prod_i\cosh(\sqrt{p_i}\,z)\) and by \(z^s\). Because \(s+2s\le3k\), the resulting products of \(h\) agree through degree \(2s\). Formal logarithms and nonzero \(a_j\) imply
\[
\sum_{i\in S(v)}p_i^j=\sum_{i\in S(w)}p_i^j
\quad\text{for every }1\le j\le s.
\]
By Newton's identities these first \(s\) power sums uniquely determine the multiset of \(s\) positive integers \(\{p_i:i\in S\}\). Thus \(v,w\) have the same orbit profile \((j_p)_p\).

**5. Conclude exact refinement.** By step 2, same colour after \(3k\) rounds with singleton-root initial colouring implies equality of the walk coefficients through order \(3k\), hence by step 4 equality of orbit profiles. Automorphisms preserve every colour at every round, so no orbit splits. The rooted refinement equals the orbit partition by round \(3k\); the unmarked refinement equals it by round \(3k+1\). QED.

## Verification
Run `python check_star_products.py` with Python 3 and no external packages. Its direct adjacency-based implementation checks 75 factor multisets, including dimension five, against the algebraic orbit profile, the exact class cardinalities, and the claimed depth bound. It also independently computes the first ten integer walk counts in 344 vertices and compares them with products of exact Taylor polynomials. The replay output is in `verification_output.txt`.

A useful nontriviality example is \(K_{1,2}\square K_{1,3}\square K_{1,4}\square K_{1,5}\). A vertex with leaf coordinates in sizes \(2,5\) and another with leaves in sizes \(3,4\) have the same distance \(2\) from \(r\) and the same degree \(9\), but lie in different orbits. The full walk signature distinguishes them (their second size-power sums are \(29\) and \(25\)). Thus distance and degree alone do not establish the theorem.

## Relationship to prior work
General colour refinement and its walk-based implementation are classical; see Kersting–Mladenov–Garnett–Grohe (2014). Klavžar–Zhu (online 2005, print 2007) analyse distinguishing labellings of Cartesian powers and use Cartesian factorization, but their two-label symmetry-breaking invariant is different from the coarsest equitable/orbit partition in the theorem here. The classical Cartesian-prime factorization theory of Sabidussi and Vizing is consistent with the elementary orbit argument above but is not needed in the proof.

Earlier related orbit-recovery results for Cartesian products of paths and for Hamming graphs involve path or complete-graph factors, respectively, not arbitrary star leaf counts; the present statement includes all branching stars and mixed factor multiplicities. The no-initial-marks, factor-number-only round bound and complete class-size formula are the additional assertions established here.

## Limitations
The \(3k+1\) bound is an upper bound, not generally optimal. The hypothesis \(p_i\ge2\) is essential to the proof's uniquely identifiable centre; allowing \(p_i=1\) requires a different orbit analysis. The theorem concerns ordinary one-dimensional counting refinement on Cartesian products of stars, not arbitrary tree products or arbitrary Cartesian graph factors. A literature search is not a proof of publication priority, and specialized earlier results may exist.

## References
- S. Klavžar and X. Zhu, *Cartesian powers of graphs can be distinguished by two labels*, European Journal of Combinatorics **28** (2007), 303–310, DOI: 10.1016/j.ejc.2005.07.001; publicly available online 2005-08-01. Author-hosted paper: https://users.fmf.uni-lj.si/klavzar/preprints/EuJC-2007-scan.pdf
- K. Kersting, M. Mladenov, R. Garnett, M. Grohe, *Power Iterated Color Refinement*, AAAI 2014, DOI: 10.1609/aaai.v28i1.8992. Full text: https://ojs.aaai.org/index.php/AAAI/article/view/8992/8851
- G. Sabidussi, *Graph Multiplication*, Mathematische Zeitschrift **72** (1960), 446–457 (classical background; not required by the proof).
