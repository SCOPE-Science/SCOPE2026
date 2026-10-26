# Exact endpoint cut–cycle norms on halved hypercubes

## Finding

For every integer \(n\ge6\), let \(H_n\) be the **halved hypercube** whose vertices are the even-weight binary words in \(\{0,1\}^n\), with an (unweighted, undirected) edge exactly when two words differ in two coordinates. Give its real edge space \(\mathbb R^{E(H_n)}\) any fixed orientation and its standard coordinate \(\ell_1\) and \(\ell_\infty\) norms. Let \(Q_n\) be the Euclidean-orthogonal projection onto the graph cut space and \(P_n=I-Q_n\) the complementary projection onto the real cycle space. Then

\[
\boxed{\|Q_n\|_{1\to1}=\|Q_n\|_{\infty\to\infty}=\frac{n+5}{4}-\frac{1}{n-1}.}
\]

Moreover,

\[
\boxed{\|P_n\|_{1\to1}=\|P_n\|_{\infty\to\infty}
=\frac{n+9}{4}-\frac{1}{n-1}-\frac{8-2^{4-n}}{n(n-1)}.}
\]

Every edge column of each projection has the same absolute column sum, so every column attains the stated norm. In particular,

\[
\lim_{n\to\infty}\frac{\|Q_n\|_{1\to1}}n=
\lim_{n\to\infty}\frac{\|P_n\|_{1\to1}}n=\frac14,
\qquad \|P_n\|_{1\to1}-\|Q_n\|_{1\to1}\to1.
\]

This gives exact linear endpoint amplification on the distance-two even-parity cube, a graph of degree \(\binom n2\), with slope one-half the cut-projection slope of the ordinary cube under the same ambient-dimension convention.

## Assumptions and scope

All graphs are finite, simple, connected and unweighted. The integer \(n\) is arbitrary with \(n\ge6\); no limit, probabilistic qualification, or assumption about a particular orientation is needed. Write \(D\) for an oriented vertex–edge incidence matrix and \(L=DD^{\mathsf T}\) for the vertex Laplacian. Then \(Q_n=D^{\mathsf T}L^+D\), where \(L^+\) denotes the Moore–Penrose inverse, and \(P_n=I-Q_n\). The induced endpoint norms are the usual real operator norms, not minimum norms over all (possibly nonorthogonal) projections. The formula does not involve conductance optimization.

For a fixed edge joining the zero word to the word with the first two bits equal to one, let \(f\) be the unique mean-zero solution of

\[Lf=\delta_{0}-\delta_{\{1,2\}}.\]

The absolute currents \(|f(x)-f(y)|\) over all graph edges constitute the absolute column of \(Q_n\) for that edge.

## Proof

**1. Fourier solution.** The vertex group consists of even-weight words under bitwise addition. Its characters are restrictions of Walsh characters \(\chi_S(x)=(-1)^{|S\cap x|}\), with indices \(S\subseteq[n]\) identified under complementation. Since graph steps flip exactly two bits, \(L\chi_S=2|S|(n-|S|)\chi_S\). In the Fourier inversion formula for the dipole at \(0\) and \(\{1,2\}\), the indices for which \(|S\cap\{1,2\}|\) is even have zero coefficients. Thus the zero eigenvalue creates no ambiguity.

Put \(m=n-2\). If the first two bits of \(x\) are different, the paired Walsh contributions cancel and \(f(x)=0\). If those bits are both zero (respectively, both one), the remaining \(m\) bits have an even number \(r\) of ones, and \(f(x)=a_r\) (respectively, \(f(x)=-a_r\)), where

\[
 a_r=\frac{1}{2^m(m+2)}\int_0^1(1-u)^r(1+u)^{m-r}\,du,
 \qquad 0\le r\le m,\quad r\ \text{even}.
\]

To derive this, write the Walsh sum over the remaining coordinates with their index size \(b\). Its denominator is \((b+1)(m+1-b)\). The partial-fraction identity

\[
\frac1{(b+1)(m+1-b)}=\frac1{m+2}
\left(\frac1{b+1}+\frac1{m+1-b}\right)
\]

and the complement symmetry of an even-weight \(r\)-subset make the two terms equal after summation. Integrating \(u^b\) yields the displayed positive integral.

In particular \(a_r>0\). For consecutive admissible even indices, \(a_r>a_{r+2}\), because the integrands differ by the strictly positive factor

\[(1+u)^2-(1-u)^2=4u\quad (0<u<1).\]

These inequalities rigorously determine the signs of all nonzero edge-current differences.

**2. Exact current enumeration.** Define

\[
S_m=\sum_{\substack{0\le r\le m\\r\text{ even}}}\binom mr a_r,
\qquad
U_m=\sum_{\substack{0\le r\le m\\r\text{ even}}}\binom mr(m-2r)a_r.
\]

An edge of \(H_n\) either flips both distinguished bits, flips one distinguished and one remaining bit, or flips two remaining bits. The first class contributes \(2S_m\) to the total absolute current; the second contributes \(4mS_m\). The final class has nonzero current only within the two classes where the first distinguished bits agree. Counting edges that raise the remaining weight from \(r\) to \(r+2\), this contribution is

\[
2\sum_{\substack{0\le r\le m-2\\r\text{ even}}}
\binom mr\binom{m-r}{2}(a_r-a_{r+2})=(m-1)U_m.
\]

The equality follows from \(\binom mr\binom{m-r}{2}=\binom m{r+2}\binom{r+2}{2}\) and \(\binom{m-r}{2}-\binom r2=(m-1)(m-2r)/2\).

Both aggregate terms have exact values. The even-binomial identities

\[
\sum_{r\text{ even}}\binom mr(1-u)^r(1+u)^{m-r}
=2^{m-1}(1+u^m)
\]

and

\[
\sum_{r\text{ even}}\binom mr(m-2r)(1-u)^r(1+u)^{m-r}
=m2^{m-1}(u+u^{m-1})
\]

follow by taking the even parts of the binomial expansion and its first weighted derivative. Integrating from zero to one gives

\[S_m=\frac1{2(m+1)},\qquad U_m=\frac14.\]

Consequently the sum of absolute currents in the chosen cut-projection column equals

\[
 (2+4m)S_m+(m-1)U_m
=\frac{m+7}{4}-\frac1{m+1}
=\frac{n+5}{4}-\frac1{n-1}.
\]

**3. Sharpness for every column, and the cycle norm.** Translating by even-weight words and permuting coordinates acts transitively on the unoriented edges of \(H_n\). It conjugates \(Q_n\) and \(P_n\) by signed permutations, so all absolute column sums agree. As these projections are real symmetric, their maximum row and column sums also agree.

The graph has \(2^{n-1}\) vertices and \(2^{n-2}\binom n2\) edges. Since \(Q_n\) is an orthogonal projection of rank \(2^{n-1}-1\), edge transitivity and the trace yield its constant diagonal entry

\[
 q_n=\frac{2^{n-1}-1}{2^{n-2}\binom n2}
=\frac{4-2^{3-n}}{n(n-1)}.
\]

Because \(0<q_n<1\), replacing the \(Q_n\) column by the corresponding \(I-Q_n\) column changes its absolute sum by exactly \(1-2q_n\). Substitution gives the stated cycle-projection formula, completing the proof.

## Verification

The accompanying standard-library Python checker uses exact rational arithmetic to reconstruct the integral potential, verify \(Lf=\delta_0-\delta_{\{1,2\}}\) at every vertex, enumerate every current on the full graph, and check both stated endpoint formulas and the diagonal trace. It runs these tests for dimensions \(3\) through \(11\) (including all dimensions \(6\) through \(11\) covered by the theorem). For dimensions \(3\) through \(6\), it separately solves a grounded Laplacian by exact rational Gauss–Jordan elimination and compares every recovered potential up to the necessary additive constant. The resulting successful output is:

`HALVED_CUBE_ENDPOINT_EXACT_OK dimensions=9 grounded_dimensions=4 full_graph_edges=47102`

Reproduction: `python3 check_halved_cube.py`. The unrestricted proof is analytical; this finite computation is a consistency check, not an exhaustive verification over all dimensions.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii proved the exact canonical cut-projection norm \((n+1)/2\) for the ordinary binary Hamming cube, as Theorem 45 in their paper first publicly available on 21 May 2023. Their proof also determines the complementary cube cycle norm (Corollary 60). In contrast, the present graph uses edges at Hamming distance **two** on a single parity class; the ordinary Hamming cube uses edges at distance **one** on the full binary vertex set. Neither cited cube formula specializes to the distance-two even-parity graph, and the proof here uses a different positive integral to determine every current sign.

The halved-cube graph and its distance-regular structure are standard objects in algebraic graph theory. Its eigenvalues alone do not determine the absolute edge-current sum evaluated above. Standard spectral and resistance-distance identities explain the diagonal term, but not by themselves the off-diagonal absolute-current norm or its exact linear coefficient.

A specialized earlier calculation of these same norms under alternate graph terminology is not ruled out by the available bibliographic comparisons; no assertion of independent verification is made.

## Limitations

The theorem covers canonical Euclidean-orthogonal cut and cycle projections in the real, unweighted edge space of \(H_n\) for every \(n\ge6\). It makes no statement about minimizing over all nonorthogonal projections, weighted halfcubes, graph modifications, or induced \(\ell_p\) norms for \(1<p<\infty\). The verification script checks finitely many dimensions, while the proof uses exact identities valid for every integer \(n\ge6\). Bibliographic originality remains subject to independent specialist examination.

## References

1. Stephen J. Dilworth, Denka Kutzarova, Mikhail I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first version dated 2023-05-21; *Proceedings of Symposia in Pure Mathematics* **106** (2024), DOI: 10.1090/pspum/106/01929. In particular, §2.7, Theorem 45 and Corollary 60.
2. A. E. Brouwer, A. M. Cohen, A. Neumaier, *Distance-Regular Graphs*, Springer, 1989 (background on halfcube/distance-regular graphs; bibliographic reference cited in the MathWorld graph entry).
3. E. W. Weisstein, *Halved Cube Graph*, MathWorld (graph definition and common notation), https://mathworld.wolfram.com/HalvedCubeGraph.html.
