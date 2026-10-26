# Fibonacci–Lucas parity law for fan-graph Hodge projection norms

## Finding

Let \(F_n=K_1\vee P_n\) be the unit-edge fan graph with one apex and \(n\ge2\) ordered path vertices. Denote the Fibonacci and Lucas numbers by \(f_0=0\), \(f_1=1\), \(f_{j+1}=f_j+f_{j-1}\), and \(\ell_n=f_{n-1}+f_{n+1}\). Let \(Q_n\) be the **Euclidean orthogonal projection** of the real edge space onto the cut space, and let \(C_n=I-Q_n\) be the complementary cycle projection. Equip that same edge space with the usual \(\ell_1\) or \(\ell_\infty\) norm when evaluating operator norms.

Then, for every integer \(n\ge2\),

\[
\begin{array}{c|cc}
 &\|Q_n\|_{1\to1}=\|Q_n\|_{\infty\to\infty}&\|C_n\|_{1\to1}=\|C_n\|_{\infty\to\infty}\\\hline
n\text{ even}&2-2/\ell_n&2-1/f_n\\
n\text{ odd}&2-1/f_n&2-2/\ell_n.
\end{array}
\]

For \(n\ge4\), the cut maximum occurs **only** on the central path edge(s), whereas the cycle maximum occurs **only** on the central apex-to-path edge(s). Precisely, a path of even order \(n\) has one central path edge and two central spokes; a path of odd order has two central path edges and one central spoke. For \(n=3\), every edge maximizes the cut norm, and only the central spoke maximizes the cycle norm. For \(n=2\), every edge maximizes both norms.

For \(n\ge3\), the exact alternating gap is

\[
(-1)^n\bigl(\|Q_n\|_{1\to1}-\|C_n\|_{1\to1}\bigr)=\frac{f_{n-3}}{f_{2n}}.
\]

Thus the cut norm is strictly larger for even \(n\), the cycle norm is strictly larger for odd \(n\ge5\), and the norms tie at \(n=3\). At \(n=2\) the norms are \(4/3\) and \(1\), respectively. Both norms tend to \(2\), with an exponentially small parity-dependent difference.

## Assumptions and scope

All graphs are finite, unweighted, connected and simple. The edge space is \(\mathbb R^{2n-1}\), with one coordinate per unoriented edge, given an arbitrary orientation. The cut subspace is the row space of a signed vertex-edge incidence matrix; its Euclidean orthogonal complement is the cycle subspace. Orientations do not affect the asserted norms. These are norms of the **canonical orthogonal projections**, not the smallest norms over all possible projections onto the respective subspaces. No claim is made about an optimal nonorthogonal projection.

## Proof

**1. Green kernel and current signs.** Ground the apex at potential zero. The grounded graph Laplacian on the path vertices is \(A_n=I+L(P_n)\): diagonal entries \(2\) at both endpoints, \(3\) at interior vertices, and nearest-neighbor off-diagonal entries \(-1\). The continuant recurrence for its determinant gives \(\det A_n=f_{2n}\). Its inverse is

\[
G_{ij}=\frac{f_{2\min(i,j)-1}\,f_{2(n-\max(i,j))+1}}{f_{2n}}
\qquad(1\le i,j\le n).
\]

This identity follows directly by multiplying by \(A_n\): for off-source rows the left and right Fibonacci factors satisfy \(u_{j+1}-3u_j+u_{j-1}=0\), the endpoint rows use \(2f_1-f_3=0\), and the source-row jump follows from the Fibonacci addition identity \(f_{a+b}=f_af_{b+1}+f_{a-1}f_b\). Equivalently it is the Green function of the stated positive tridiagonal matrix. In particular, each column of \(G\) is positive and increases up to its source vertex and decreases after it.

Write \(D=f_{2n}\). For an oriented spoke with source at path vertex \(k\), its electrical potential vector is \(v_i=G_{ik}\). The spoke-current absolute sum equals \(\sum_i v_i=1\), because \(A_n\mathbf1=\mathbf1\). The path-current absolute sum is \(2v_k-v_1-v_n\), by monotonicity. The projection's source-edge diagonal is \(G_{kk}\). Therefore the complete spoke column norms are

\[
q_s(k)=1+\frac{2f_{2k-1}f_{2(n-k)+1}-f_{2k-1}-f_{2(n-k)+1}}D,
\qquad
c_s(k)=2-\frac{f_{2k-1}+f_{2(n-k)+1}}D.
\tag{1}
\]

For an oriented path edge between \(k\) and \(k+1\), its potential vector is \(v_i=G_{ik}-G_{i,k+1}\). The Green formula simplifies to

\[
v_i=\begin{cases}
 f_{2i-1}f_{2(n-k)}/D,&i\le k,\\
 -f_{2(n-i)+1}f_{2k}/D,&i\ge k+1.
\end{cases}
\]

Thus potentials are positive and increasing on the left, and negative and increasing on the right. The spoke absolute sum is \(2f_{2k}f_{2(n-k)}/D\), using \(\sum_{i=1}^k f_{2i-1}=f_{2k}\). Kirchhoff's law on the left path segment gives source-edge effective resistance \(r_k=1-f_{2k}f_{2(n-k)}/D\). The total absolute path current is \(2r_k-(f_{2k}+f_{2(n-k)})/D\). Consequently the path-edge column norms are

\[
q_r(k)=2-\frac{f_{2k}+f_{2(n-k)}}D,
\qquad
c_r(k)=1+\frac{2f_{2k}f_{2(n-k)}-f_{2k}-f_{2(n-k)}}D.
\tag{2}
\]

In both derivations \(c=1+q-2r\), since the complementary projection has diagonal entry \(1-r\) and off-diagonal entries opposite to those of the cut projection. All column norms are thus established without an assumption about their maximizing edges.

**2. Location of maxima within each edge class.** The expressions are invariant under reflection \(k\mapsto n+1-k\) for spokes and \(k\mapsto n-k\) for path edges. The sums of positive Fibonacci numbers in \(c_s(k)\) and \(q_r(k)\) decrease toward the center, because their one-step changes are respectively \(f_{2k}-f_{2(n-k)}\) and \(f_{2k+1}-f_{2(n-k)-1}\). Hence both types have precisely their central maximum or maxima.

For \(q_s(k)\), put \(g(k)=2f_{2k-1}f_{2(n-k)+1}-f_{2k-1}-f_{2(n-k)+1}\). D'Ocagne's Fibonacci identity gives, whenever \(1\le k<n/2\),

\[
g(k+1)-g(k)=f_{2(n-k)}-f_{2k}-2f_{2(n-2k)}\ge0.
\]

To check the last inequality, put \(a=2k\ge2\) and \(b=2(n-2k)\ge2\), and use

\[
f_{a+b}-f_a-2f_b=f_a(f_{b+1}-1)+(f_{a-1}-2)f_b.
\]

For \(a\ge4\), both summands are nonnegative. For \(a=2\), the expression reduces to \(f_{b-1}-1\ge0\). Thus the largest spoke cut column is central. Similarly, in \(c_r(k)\), the product \(f_{2k}f_{2(n-k)}\) increases toward the middle: its one-step difference for \(k<(n-1)/2\) is \(f_{2(n-2k-1)}\ge0\). Meanwhile its subtracted sum decreases. Therefore the largest path-edge cycle column is also central.

**3. Comparison of the two central edge classes.** Use \(f_{2n}=f_n\ell_n\), \(f_{n-1}f_{n+1}=f_n^2+(-1)^n\), and \(\ell_n-2f_n=f_{n-3}\) for \(n\ge3\). At even \(n\ge4\), subtraction of the central formulas (1) and (2), with common denominator \(D\), yields

\[
D\bigl(\max q_r-\max q_s\bigr)=(f_n+1)f_{n-3}-2>0,
\qquad
D\bigl(\max c_s-\max c_r\bigr)=(f_n-1)f_{n-3}>0.
\]

At odd \(n\ge3\), the corresponding differences are

\[
D\bigl(\max q_r-\max q_s\bigr)=(f_n-1)f_{n-3}\ge0,
\qquad
D\bigl(\max c_s-\max c_r\bigr)=(f_n+1)f_{n-3}+2>0.
\]

The only equality above is at \(n=3\); the \(n=2\) case is verified directly from the triangle. Hence path edges globally maximize \(Q_n\) and spokes globally maximize \(C_n\), with exactly the exceptional ties specified.

For even \(n\), central path-edge Fibonacci sum is \(2f_n\), whereas the central spoke sum is \(\ell_n\). For odd \(n\), those two central sums are reversed. Substitution into (1) and (2) gives the asserted parity-swapped formulas. Their difference is \((\ell_n-2f_n)/(f_n\ell_n)=f_{n-3}/f_{2n}\), with the sign indicated in the statement. Each projection matrix is real symmetric, so its maximum absolute row sum equals its maximum absolute column sum and the \(\ell_1\) and \(\ell_\infty\) norms agree.

## Verification

The included standalone script `check_fan.py` constructs the grounded signed incidence matrix for each \(2\le n\le22\). It independently solves every source-edge Laplacian system using exact rational Gaussian elimination, recomputes all projected-current column norms and complementary norms, verifies (1)–(2), and compares them with the theorem's Fibonacci–Lucas values. All \(483\) complete edge columns across \(21\) graphs agree exactly. Execute with `python3 check_fan.py`; only the Python standard library is needed. These finite checks corroborate, but do not replace, the all-parameter argument above.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii develop the real cycle/cut-space projection framework and analyze invariant and minimal projections, with explicit computations emphasizing tori and Hamming graphs. Their results do not state the fan-graph parity law. Bapat and Gupta derive Fibonacci resistance distances of fan graphs; Sedlák and Slavík reproduce the full grounded Green kernel for fans and compute resistance and Kirchhoff-index quantities. These already supply electrical linear-algebra ingredients, **not** the sharp absolute-current column sums, the maximization over both edge types, or the alternating cut-versus-cycle endpoint norm law. Młotkowski and Obata treat the same graph family but a different invariant, the quadratic embedding constant of its distance matrix. The present result is the norm-and-extremizer classification, not a new resistance formula or general projection-minimality theorem.

## Limitations

Only Euclidean-orthogonal cut/cycle projections with unweighted edge coordinates are considered. No minimum-norm assertion over other projections is made. Earlier exact resistance formulas reduce the amount of new work in the Green-kernel step; novelty rests on the absolute-current maximization and parity-dependent comparison. Bibliographic search cannot exclude a separately phrased prior calculation of these norms. All finite verification is same-author computational corroboration, not an independent mathematical audit.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first public version 21 May 2023), https://arxiv.org/abs/2305.12582.
2. R. B. Bapat, S. Gupta, *Resistance distance in wheels and fans*, Indian J. Pure Appl. Math. 41 (2010), 1–13, DOI:10.1007/s13226-010-0004-2.
3. J. Sedlák, A. Slavík, *Resistance distances and Kirchhoff indices in graph joins*, J. Phys. A 58 (2025), 505203, DOI:10.1088/1751-8121/ae2997, especially Section 3.6.
4. W. Młotkowski, N. Obata, *Quadratic embedding constants of fan graphs and graph joins*, arXiv:2403.16348 (first public version 25 March 2024), https://arxiv.org/abs/2403.16348.
