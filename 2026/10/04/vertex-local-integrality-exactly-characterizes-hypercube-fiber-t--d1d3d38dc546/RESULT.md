# Vertex-local integrality exactly characterizes hypercube-fiber transfer in lexicographic products

## Finding

Let \(G\) be a finite connected simple graph with adjacency matrix \(A_G\), and let \(g\in V(G)\). Write
\[
\sigma_g(G)=\{\theta:E_\theta e_g\ne0\}
\]
for the adjacency eigenvalue support of \(g\), where \(E_\theta\) is the spectral idempotent of \(A_G\).

Let \(d\ge2\), put \(m=2^d\), and let \(a,b\) be antipodal vertices of the hypercube \(Q_d\). Use the standard continuous-time adjacency walk
\[
U(t)=e^{-itA}
\]
on the lexicographic product
\[
X=G[Q_d],
\qquad
A=A_G\otimes J_m+I\otimes A_{Q_d}.
\]

Then
\[
\boxed{
X\text{ has perfect state transfer from }(g,a)\text{ to }(g,b)
\iff
\sigma_g(G)\subseteq\mathbb Z.
}
\]

If the condition holds, the complete set of positive perfect-transfer times is
\[
t=\frac{(2r+1)\pi}{2},
\qquad r=0,1,2,\ldots,
\]
so the minimum positive transfer time is \(\pi/2\). The transfer phase is
\[
(-i\sin t)^d.
\]

Equivalently, without assuming local integrality in advance, transfer at a time \(t\) is possible exactly when
\[
\cos t=0
\]
and
\[
e^{-i2^d tA_G}e_g=e_g.
\]

This local criterion is strictly weaker than requiring the whole outer graph \(G\) to be integral. A connected example is the seven-vertex tree \(T\) with vertices
\[
\{g,u,v,a_1,a_2,b_1,b_2\}
\]
and edges
\[
gu,\quad gv,\quad ua_1,\quad ua_2,\quad vb_1,\quad vb_2.
\]
Its characteristic polynomial is
\[
\phi_T(x)=x^3(x^2-2)(x^2-4),
\]
so \(T\) is nonintegral because \(\pm\sqrt2\) are eigenvalues. Deleting the middle vertex \(g\) leaves two copies of \(P_3\), hence
\[
\phi_{T-g}(x)=x^2(x^2-2)^2.
\]
The diagonal resolvent identity gives
\[
\bigl((xI-A_T)^{-1}\bigr)_{g,g}
=
\frac{\phi_{T-g}(x)}{\phi_T(x)}
=
\frac{x^2-2}{x(x^2-4)}.
\]
Therefore
\[
\sigma_g(T)=\{-2,0,2\}.
\]
Consequently, for every \(d\ge2\), the connected graph \(T[Q_d]\) has perfect state transfer between the antipodes in the \(g\)-fiber at time \(\pi/2\), even though \(T[Q_d]\) itself is nonintegral: its spectrum contains
\[
d\pm2^d\sqrt2
\]
from the uniform hypercube mode.

## Assumptions and scope

The Hamiltonian is the unnormalized adjacency matrix, so the time variable is the standard one in
\[
e^{-itA}.
\]
This matters because some literature rescales time when comparing families of different graph sizes.

The result concerns transfer between antipodal vertices inside a single hypercube fiber of the standard lexicographic product. It does not classify transfer between different outer fibers, generalized lexicographic products with a non-all-one connection matrix, the case \(d=1\), Laplacian walks, or pretty-good transfer.

The outer graph is assumed finite, simple, and connected. Connectivity is not needed for the local algebra, but it keeps the construction in the conventional perfect-state-transfer setting.

## Proof

Let
\[
s=\frac1{\sqrt m}\mathbf 1
\]
be the normalized all-one vector of the hypercube fiber, and let
\[
P=ss^\ast.
\]
Since
\[
J_m=mP
\]
and the hypercube is \(d\)-regular,
\[
A_{Q_d}s=ds.
\]
Also \(A_{Q_d}\) commutes with \(P\). Thus the product Hilbert space splits orthogonally into
\[
\mathbb C^{V(G)}\otimes\operatorname{span}\{s\}
\]
and
\[
\mathbb C^{V(G)}\otimes s^\perp.
\]
On the first summand the Hamiltonian is
\[
mA_G+dI,
\]
while on the second it is
\[
I\otimes A_{Q_d}.
\]

Suppose first that perfect state transfer occurs:
\[
e^{-itA}(e_g\otimes e_a)
=
\gamma\,e_g\otimes e_b
\]
for a unimodular phase \(\gamma\). Projecting onto the uniform fiber direction gives
\[
e^{-idt}e^{-imtA_G}e_g
=
\gamma e_g.
\]
Projecting onto \(s^\perp\) gives
\[
P^\perp e^{-itA_{Q_d}}e_a
=
\gamma P^\perp e_b.
\]
Hence the vector
\[
e^{-itA_{Q_d}}e_a-\gamma e_b
\]
is constant over the hypercube vertices.

Identify \(Q_d\) with \(\{0,1\}^d\), take \(a=0^d\), and let \(r\) be Hamming distance from \(a\). Since
\[
A_{Q_d}=X_1+\cdots+X_d
\]
with commuting coordinate-flip matrices, the transition amplitude from \(a\) to a vertex at distance \(r\) is
\[
(-i\sin t)^r(\cos t)^{d-r}.
\]
Because \(d\ge2\), there are non-target vertices at distances \(0\) and \(1\). Their amplitudes must be equal. If \(\cos t\ne0\), equality would require
\[
\cos t=-i\sin t,
\]
which is impossible for real \(t\). Therefore
\[
\cos t=0,
\]
so
\[
t=\frac{(2r+1)\pi}{2}
\]
for some integer \(r\). At such a time the hypercube walk is exactly supported on the antipode:
\[
e^{-itA_{Q_d}}e_a
=
(-i\sin t)^d e_b.
\]
Thus
\[
\gamma=(-i\sin t)^d=e^{-idt},
\]
and the uniform-sector equation reduces to
\[
e^{-imtA_G}e_g=e_g.
\]

Now use the spectral decomposition
\[
e_g=\sum_{\theta\in\sigma_g(G)}E_\theta e_g.
\]
The return equation is equivalent to
\[
e^{-imt\theta}=1
\]
for every \(\theta\in\sigma_g(G)\). Since \(m=2^d\) and
\[
t=\frac{(2r+1)\pi}{2},
\]
this says
\[
2^{d-2}(2r+1)\theta\in\mathbb Z.
\]
Every adjacency eigenvalue of a finite simple graph is an algebraic integer. Hence every supported \(\theta\) is both rational and an algebraic integer, so
\[
\theta\in\mathbb Z.
\]
This proves necessity.

Conversely, assume
\[
\sigma_g(G)\subseteq\mathbb Z.
\]
For any odd half-period
\[
t=\frac{(2r+1)\pi}{2},
\]
we have
\[
\frac{mt\theta}{2\pi}
=
2^{d-2}(2r+1)\theta\in\mathbb Z
\]
for every supported \(\theta\), because \(d\ge2\). Therefore
\[
e^{-imtA_G}e_g=e_g.
\]
The hypercube simultaneously sends \(a\) exactly to \(b\), so the two invariant sectors recombine to give
\[
e^{-itA}(e_g\otimes e_a)
=
(-i\sin t)^d e_g\otimes e_b.
\]
This proves sufficiency and also shows that every odd half-period is a transfer time. The necessity argument shows there are no others.

For the tree \(T\), the resolvent formula
\[
\bigl((xI-A_T)^{-1}\bigr)_{g,g}
=
\frac{\phi_{T-g}(x)}{\phi_T(x)}
\]
has poles exactly at the eigenvalues in the support of \(g\). Cancelling the displayed characteristic polynomials leaves poles only at
\[
-2,\quad0,\quad2.
\]
Thus the example follows.

## Verification

`verify_local_hypercube_pst.py` is a standalone checker. It computes the characteristic polynomials of \(T\) and \(T-g\) by exact integer polynomial arithmetic and verifies
\[
\phi_T(x)=x^3(x^2-2)(x^2-4),
\qquad
\phi_{T-g}(x)=x^2(x^2-2)^2.
\]
It then independently diagonalizes the seven-vertex adjacency matrix with a pure-Python Jacobi routine and checks that the state at \(g\) returns at the required outer evolution times for \(d=2,3,4,5\). Finally, it checks the hypercube amplitude formula at the corresponding odd half-period and confirms unit transfer amplitude in the product decomposition.

These finite computations are supplementary. The all-\(G\), all-\(d\ge2\) characterization is proved by the invariant-subspace and algebraic-integer argument above.

## Relationship to prior work

Ge, Greenberg, Perez, and Tamon introduced the lexicographic-product construction in this perfect-state-transfer setting. Their Lemma 5 gives a sufficient condition using the entire spectrum of the outer graph:
\[
t_H|V_H|\operatorname{Spec}(G)\subseteq2\pi\mathbb Z.
\]
They then state that \(G[Q_d]\) has perfect state transfer for every integral \(G\) and \(d\ge2\). The proof already displays the spectral decoupling that motivates the present question, but the condition is global in \(G\) and is presented as sufficient.

Godsil's survey develops eigenvalue support as the correct local spectral object for state transfer and periodicity. It also cites the lexicographic-product results of Ge and collaborators. The inspected survey does not state the hypercube-fiber equivalence above.

Bhattacharjya, Monterde, and Pal later studied adjacency quantum walks on blow-up graphs, a special lexicographic product in which the fiber is an independent set. They explicitly describe the Ge conditions as sufficient conditions for lexicographic products and develop local eigenvalue-support criteria for their different blow-up problem. Their results do not cover a hypercube fiber.

The finding above combines the exact hypercube factorization with vertex support to turn the global sufficient condition into a local necessary-and-sufficient criterion. The seven-vertex tree shows that this is a strict extension: the outer graph and the resulting lexicographic product are nonintegral, so the earlier integral-graph corollary does not apply.

Targeted searches for “lexicographic product,” “hypercube,” “perfect state transfer,” and “eigenvalue support” did not locate this exact equivalence or the nonintegral tree example.

## Limitations

The proof uses the unusually rigid antipodal propagator of the hypercube. For a different regular fiber \(H\), perfect transfer in the orthogonal-to-uniform sector need not force the same time condition, so the local-integrality classification does not automatically generalize.

The result is a sharp refinement of known product machinery rather than a new physical model. The ingredients—lexicographic-product spectral decomposition, hypercube transfer, and local eigenvalue support—are established separately in prior work. An equivalent corollary may exist in literature not surfaced by the searches, especially work phrased in terms of periodic vertices or graph compositions.

The case \(d=1\) has a different parity condition and is intentionally excluded.

## References

1. Y. Ge, B. Greenberg, O. Perez, and C. Tamon, “Perfect state transfer, graph products and equitable partitions,” *International Journal of Quantum Information* 9 (2011), 823–842, arXiv:1009.1340, DOI: 10.1142/S0219749911007472.
2. C. Godsil, “State transfer on graphs,” *Discrete Mathematics* 312 (2012), 129–147, DOI: 10.1016/j.disc.2011.06.032.
3. B. Bhattacharjya, H. Monterde, and H. Pal, “Quantum walks on blow-up graphs,” *Journal of Physics A: Mathematical and Theoretical* 57 (2024), 335303, arXiv:2308.13887, DOI: 10.1088/1751-8121/ad6653.
