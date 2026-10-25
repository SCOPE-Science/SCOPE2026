# Binary de Bruijn coverage with exactly two surplus windows

## Finding

Let \(k\ge2\) be an integer. A *directed cyclic binary word* is a binary word considered up to cyclic rotation, but not reversal. A cyclic length-\(k\) window is read with wraparound. Call a cyclic word *two-surplus universal of order \(k\)* when its length is exactly \(2^k+2\) and every binary word of length \(k\) appears among its cyclic windows at least once.

Let \(A_k=0101\cdots\) and \(\overline A_k=1010\cdots\) denote the two alternating binary words of length \(k\), and set
\[
 B_k=2^{2^{k-1}-k},\qquad R_k=\frac53+\frac{(-1)^k}{3\,2^{k-2}}.
\]
For a two-surplus universal circle, subtract one from the multiplicity of each length-\(k\) word. The remaining two windows form exactly one of these four multisets:
\[
\{0^k,0^k\},\quad\{0^k,1^k\},\quad\{1^k,1^k\},\quad\{A_k,\overline A_k\}.
\]
The first three types contain exactly \(B_k\) different circles each; the fourth contains exactly \(B_kR_k\). Consequently the exact total is
\[
 T_k=B_k(3+R_k)=2^{2^{k-1}-k}\left(\frac{14}{3}+\frac{(-1)^k}{3\,2^{k-2}}\right).
\]
The initial totals for \(k=2,3,4,5,6\) are \(5,9,76,9472,314572800\). Every listed type is realized.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), the window length is \(k\ge2\), the circumference is \(2^k+2\), and windows are counted with multiplicity at every cyclic starting position. Two circles are equivalent only under rotation. There are no fixed representatives, hidden endpoint conventions, or probabilistic assumptions. The formula is an exact integer count for every specified \(k\), not an asymptotic approximation.

## Proof

**1. Conservation of the surplus.** Use the standard de Bruijn digraph \(G_k\) whose vertices are all \((k-1)\)-bit words and whose directed arcs are all \(k\)-bit words, with the shift-and-append incidence rule. A cyclic word of length \(2^k+2\) gives a closed walk that uses every arc at least once and two arcs additionally, counted with repetition. The base graph has indegree and outdegree two at every vertex, so the two additional arcs themselves form a balanced directed multigraph. A balanced directed multigraph with just two arcs consists of two loops (possibly the same loop twice) or a directed two-cycle between distinct vertices. In \(G_k\), the only loops are \(0^k\) and \(1^k\). A directed two-cycle must alternate bits, so its arcs are precisely \(A_k\) and \(\overline A_k\). This proves the classification and exhaustiveness of the four types.

**2. Euler-tour normalization.** Choose, in every surplus type, a fixed \(k\)-mer that is still used once; this is possible because \(2^k\ge4\) and only two surplus uses are present. Every cyclic word corresponds to precisely one Euler tour starting with that uniquely occurring arc. With \(\tau(H)\) denoting the number of directed spanning in-trees towards the tail of that arc, the BEST theorem, after forgetting labels on indistinguishable parallel arcs, gives the number of cyclic words represented by a balanced multigraph \(H\):
\[
 \tau(H)\frac{\prod_v(d_H^+(v)-1)!}{\prod_e m_H(e)!}.
\]
Here \(m_H(e)\) counts how many times a \(k\)-mer arc is present, and the fixed initial arc has multiplicity one. Every circle is primitive because several windows appear exactly once, so rotation introduces no correction. For the base \(G_k\), every outdegree is two and every multiplicity one, hence this number is the usual binary de Bruijn count \(\tau(G_k)=B_k=2^{2^{k-1}-k}\).

**3. Two loops.** Loop additions leave all spanning in-trees unchanged. Adding two copies of the same loop raises one outdegree from two to four: its factorial contribution is \(3!=6\), canceled by the \(3!\) ways to label the three identical arc occurrences. Adding one copy of each loop raises two outdegrees to three, contributing \(2!\cdot2!=4\), canceled by the two arc-multiplicity factorials \(2!\cdot2!=4\). Each of the three loop patterns therefore contributes exactly \(B_k\) circles.

**4. The alternating two-cycle.** Let \(u\) and \(v\) be the alternating \((k-1)\)-bit vertices starting in zero and one, respectively. The extra arcs \(u\to v\) and \(v\to u\) are parallel to preexisting arcs. Their two degree-factorial increments cancel their two multiplicity-factorial increments; the count is therefore \(\tau(G_k+\{u\to v,v\to u\})\). We now calculate the ratio to \(\tau(G_k)\), rather than leaving it as a graph determinant.

Write \(N=2^{k-1}\) and \(P\) for the row-stochastic matrix of the unbiased shift-and-append walk on the \((k-1)\)-bit vertices. Its Laplacian is \(L=2(I-P)\). After exactly \(k-1\) random appended bits, the state is uniform and independent of the initial vertex, so \(P^{k-1}=\Pi\), the matrix with every entry \(1/N\). On zero-sum vectors, the group inverse of \(L\) is
\[
 L^{\#}=\frac12\sum_{j=0}^{k-2}(P^j-\Pi).
\]
The extra opposite arcs change \(L\) by the rank-one matrix \(ss^{\mathsf T}\), where \(s=e_u-e_v\). The directed matrix-tree theorem and the matrix determinant lemma for any reduced Laplacian give
\[
 \frac{\tau(G_k+\{u\to v,v\to u\})}{\tau(G_k)}
 =1+s^{\mathsf T}L^{\#}s.
\]
This group-inverse form is valid since \(s\) has coordinate sum zero; deleting the same row and column to form a cofactor changes its inverse solution only by an additive constant, which disappears upon pairing with \(s\).

For \(0\le j\le k-2\), shifting an alternating word by \(j\) places and appending \(j\) fair bits returns to the same alternating vertex precisely when \(j\) is even, and to the other one precisely when \(j\) is odd. The indicated transition has probability \(2^{-j}\); the other has probability zero. Thus
\[
 s^{\mathsf T}P^js=2(-1)^j2^{-j},\quad
 1+s^{\mathsf T}L^{\#}s
 =1+\sum_{j=0}^{k-2}(-1/2)^j
 =\frac53+\frac{(-1)^k}{3\,2^{k-2}}=R_k.
\]
Hence the alternating pattern contributes exactly \(B_kR_k\), proving the total. Every augmented graph is strongly connected and balanced, so Euler tours exist and the four possible types really occur.

## Verification

Run `python3 near_debruijn_verify.py` with standard-library Python. The checker independently exhausts every binary cyclic word at orders \(k=2,3,4\), retaining words whose cyclic length-\(k\) windows cover all \(2^k\) possibilities; it normalizes by minimal rotation and groups them by the exact surplus multiset. It reproduces totals \(5,9,76\) and every separate type count. A separately implemented exact-integer Bareiss determinant verifies the matrix-tree ratio at orders \(2\) through \(7\). The calculations are finite checks of the symbolic proof, not the justification for all orders.

## Relationship to prior work

De Bruijn's 1946 theorem supplies the baseline exact count \(B_k\) of perfect binary universal circles. Kandel–Matias–Unger–Winkler (1996) provide general uniform shuffling of strings with fixed \(k\)-let multiplicities via Euler tours. Alhakim (2010) studies preference-function constructions for exact de Bruijn cycles. Tesler (arXiv:1708.03654, 2017) develops general counting formulas for *uniform* \(k\)-mer multiplicity, with every \(k\)-mer occurring the same number of times, and explicitly discusses the BEST theorem and Kandel et al. None of the inspected statements supplies this four-type **nonuniform two-surplus** classification or its alternating-case closed determinant ratio. General Euler-tour and matrix-tree formulas are indispensable prior tools; the specialization requires the balance classification and exact rank-one evaluation above.

## Limitations

The result treats only binary cyclic words with exactly two windows beyond the perfect de Bruijn length; it does not count arbitrary multiplicity vectors or larger excess. No independent mathematical audit has been performed. Historical priority has residual uncertainty because the full primary article of Kandel et al. could not be inspected; its accessible abstract describes general algorithms and the later Tesler full text references it as such. An equivalent specialized enumeration under a different name remains possible. The formula counts rotation classes, not reversal classes.

## References

1. N. G. de Bruijn, *A Combinatorial Problem*, Proc. Koninklijke Nederlandse Akademie van Wetenschappen 49 (1946), 758–764, communicated June 29, 1946. Authoritative scan: https://pure.tue.nl/ws/portalfiles/portal/4442708/597473.pdf.
2. D. Kandel, Y. Matias, R. Unger, P. Winkler, *Shuffling Biological Sequences*, Discrete Applied Mathematics 71 (1996), 171–185, https://doi.org/10.1016/S0166-218X(97)81456-4; accessible abstract https://cris.tau.ac.il/en/publications/shuffling-biological-sequences/.
3. A. Alhakim, *Spans of Preference Functions for De Bruijn Sequences*, arXiv:1012.1796, first posted December 8, 2010, https://arxiv.org/abs/1012.1796.
4. G. Tesler, *Multi de Bruijn Sequences*, arXiv:1708.03654, first posted August 11, 2017, https://arxiv.org/abs/1708.03654.
5. OEIS A016031, classical binary de Bruijn cycle count, https://oeis.org/A016031.
