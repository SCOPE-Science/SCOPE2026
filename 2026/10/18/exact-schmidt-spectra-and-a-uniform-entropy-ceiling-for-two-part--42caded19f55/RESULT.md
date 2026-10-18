# Exact Schmidt spectra and a uniform entropy ceiling for two-particle Grover walks on complete bipartite graphs

## Finding

Consider the exchange-symmetric or exchange-antisymmetric two-particle Grover walk on any complete bipartite graph \(K_{m,n}\), starting from the normalized superposition of the two opposite orientations of one edge. For **every pair of positive integers** \(m,n\), its particle-factor Schmidt spectrum at **every nonnegative integer step** is explicit and depends on the graph through just two numbers \(\mu_+\) and \(\mu_-\). The resulting entropy never exceeds \(\log 8\), irrespective of graph size. The maximally possible entropy \(\log(2mn)\) is attained precisely for \(K_{1,1}\) (at all times) or \(K_{2,2}\) (at steps congruent to \(2\) modulo \(4\)).

Put \(q=mn\) and

\[
\mu_\pm=\frac12\left(1\pm\sqrt{1-\frac{16(m-1)(n-1)}{m^2n^2}}\right),\qquad
h(p)=-p\log p-(1-p)\log(1-p),
\]

with \(0\log0=0\). If \(S_t\) is the von Neumann entropy of the first particle factor, with **natural logarithms**, then

\[
\boxed{S_{4k}=\log2,\quad S_{4k+1}=S_{4k+3}=\log2+h(\mu_+),\quad S_{4k+2}=\log2+2h(\mu_+)}
\]

for every \(k\geq0\) (where the expression for \(4k+3\) is understood for every \(k\geq0\)). The **complete nonzero Schmidt probability spectrum**, with zero entries omitted, is

\[
\begin{array}{c|c}
 t\bmod4 & \text{eigenvalues of the one-particle reduced density matrix}\,\\ \hline
0 & (1/2,1/2)\\
1,3 & (\mu_+/2,\mu_-/2)\ \text{each with multiplicity two}\\
2 & (\mu_i\mu_j/2)_{i,j\in\{+,-\}}\ \text{each with multiplicity two}.
\end{array}
\]

Consequently, for \(m,n\geq2\), the maximum Schmidt rank is exactly \(8\), reached at times \(t\equiv2\pmod4\), independently of \(m,n\). For \(\min(m,n)=1\), the rank remains \(2\) and the entropy stays \(\log2\). The bosonic and fermionic signs produce the same spectrum.

A further size-controlled consequence is that, **among graphs with a fixed number \(q=mn\) of edges**, the largest entropy achieved by this walk increases as \(m+n\) decreases: a pair of complementary factors closest to \(\sqrt q\) is optimal. When both part sizes diverge,

\[
\max_{t\geq0}S_t
=\log 2+\frac{8}{mn}\left(\log\frac{mn}{4}+1\right)
+o\left(\frac{\log(mn)}{mn}\right).
\]

## Assumptions and scope

Let \(m,n\in\mathbb N\) and let \(G=K_{m,n}\) have left vertices \(x_1,\ldots,x_m\) and right vertices \(y_1,\ldots,y_n\). Its directed arc set \(\mathcal A\) consists of both orientations of each edge, so \(|\mathcal A|=2mn\). The two-particle Hilbert space is \(\mathcal H=\mathbb C^{\mathcal A}\otimes\mathbb C^{\mathcal A}\). The dynamics is **not** the tensor product of independent one-particle Grover walks: by definition it is the usual arc-reversal Grover walk on the direct/Kronecker graph product \(G\otimes G\), transported to \(\mathcal H\) via the identification

\[
 |(u,v)\rangle\otimes|(s,w)\rangle\longleftrightarrow|((u,s),(v,w))\rangle.
\]

From an incoming directed product-graph edge \(((u,s),(v,w))\), the usual Grover step sends amplitude to each outgoing edge \(((v,w),(v',w'))\), with coefficient

\[
\frac{2}{\deg_G(v)\deg_G(w)}-\mathbf1_{v'=u}\mathbf1_{w'=s}.
\]

This completely specifies the unitary without relying on an external convention. Define \(a=(x_1,y_1)\), \(b=(y_1,x_1)\) and set

\[
 |\psi_0^\eta\rangle=\frac{|a\rangle\otimes|b\rangle+\eta|b\rangle\otimes|a\rangle}{\sqrt2},\qquad \eta\in\{+1,-1\}.
\]

The state at step \(t\) is \(U^t|\psi_0^\eta\rangle\). Its coefficient matrix \(\Psi_t\), indexed by the first and second particle arcs, determines \(\rho_t=\Psi_t\Psi_t^*\). All logarithms are natural; the entropy is \(-\operatorname{tr}(\rho_t\log\rho_t)\). This is specifically the particle-factor entropy in the tensor-arc convention of the cited Grover-walk model, not a claim about operationally extractable entanglement of identical particles.

## Proof

**1. Reduction to a balanced complete bipartite component and period four.** The product graph \(K_{m,n}\otimes K_{m,n}\) has two components: \(K_{m^2,n^2}\), on same-side ordered vertex pairs, and \(K_{mn,mn}\), on opposite-side ordered pairs. Both directed tensor arcs in the initial state belong to the **second**, balanced component \(K_{q,q}\), where \(q=mn\). All subsequent states remain there. Let \(R_q=2\mathbf1\mathbf1^{\mathsf T}/q-I_q\), the degree-\(q\) Grover reflection. On each directed-edge orientation sector of \(K_{q,q}\), the second power of the Grover step is equivalent, after ordering source and target endpoints, to \(R_q\otimes R_q\). Because \(R_q^2=I_q\), the walk has \(U^4=I\) on the supported component. It suffices to inspect steps \(0,1,2,3\).

**2. An explicit rank-two rectangular matrix.** Label the arcs of \(G\) by \(A_{ij}=(x_i,y_j)\) and \(B_{ji}=(y_j,x_i)\). Define the real \(m\)-by-\(n\) matrix

\[
G_{ij}=\frac2q-\mathbf1_{i=1}\mathbf1_{j=1}.
\]

It is the sum of two rank-one matrices. Its squared Frobenius norm is

\[
\|G\|_F^2=q\left(\frac2q\right)^2-2\left(\frac2q\right)+1=1.
\]

For \(m,n\geq2\), every nonzero two-by-two minor is a minor with rows \(1,i\), columns \(1,j\) for \(i,j>1\), and its determinant is \(-2/q\). By the Cauchy–Binet identity the product of the two nonzero eigenvalues of \(GG^{\mathsf T}\) is therefore

\[
\frac{4(m-1)(n-1)}{q^2}.
\]

Those eigenvalues sum to \(1\), giving exactly \(\mu_+,\mu_-\) above. If a part has size one, \(G\) has rank one and the same formula gives \(\mu_+=1,\mu_-=0\). Reality of the square root follows from \(m^2\geq4(m-1)\) and \(n^2\geq4(n-1)\); equality in both inequalities holds precisely when \(m=n=2\).

**3. Explicit coefficient blocks at steps one and three.** Order all \(A\)-type arcs first and all \(B\)-type arcs second. At each step, the state has a coefficient matrix of the form

\[
\Psi_t=\begin{pmatrix}0&X_t\\\eta X_t^{\mathsf T}&0\end{pmatrix},
\]

possibly with a harmless overall sign or with the \(A\) and \(B\) sectors interchanged. At step \(1\), the first Grover update acts at the endpoint pair of each initial product arc. The resulting \(A\)-to-\(B\) block has support on rows \(A_{1j}\) and columns \(B_{1i}\), with entries \(\eta G_{ij}/\sqrt2\), up to transposition of the rectangular active block. The reverse block is its signed transpose. Thus **each block has nonzero squared singular values \(\mu_+/2,\mu_-/2\)**. Step \(3\) equals step \(-1\) by period four; the inverse Grover step instead scatters into the arcs incident to the initial origins and produces the same active rectangular matrix \(G\), up to row/column permutations and transposition. Its squared singular values are consequently identical. This establishes the stated doubled Schmidt probabilities for both odd residue classes.

**4. Explicit tensor block at step two.** Under two Grover steps on the balanced product-graph component, a directed edge from one side to the other acquires the product of two reflection coefficients \(2/q-\delta\), one at each product-graph endpoint. In tensor-arc coordinates this gives, for arbitrary valid indices,

\[
 (X_2)_{A_{ij},B_{k\ell}}=\frac1{\sqrt2}
 G_{ik}G_{\ell j}.
\]

With the standard lexicographic ordering of \(A_{ij}\) and \(B_{k\ell}\), this is exactly

\[
 X_2=\frac1{\sqrt2}\left(G\otimes G^{\mathsf T}\right).
\]

The reverse block is its signed transpose. The squared singular values of a Kronecker product are pairwise products of the squared singular values of its factors. Hence the eigenvalues of \(\Psi_2\Psi_2^*\) are precisely \(\mu_i\mu_j/2\), each twice, and all other eigenvalues vanish. Step zero has only two equal Schmidt probabilities \(1/2\).

**5. Entropy, perfect saturation, and optimization.** For each time class, the Schmidt probability distribution is the product of a fair two-point distribution and respectively zero, one, or two independent copies of \((\mu_+,\mu_-)\). Additivity of the entropy of product distributions yields the three displayed formulas. Since \(h\leq\log2\), the entropy is bounded by \(\log8\). The particle Hilbert space per factor has dimension \(2mn\). If \(m=1\) or \(n=1\), all entropies equal \(\log2\), which reaches \(\log(2mn)\) only for \(m=n=1\). Otherwise the supported density has rank at most eight, so maximal entropy requires \(2mn\leq8\). Among \(m,n\geq2\), this forces \(m=n=2\); there \(\mu_+=\mu_-=1/2\), and the eight probabilities at steps \(2\bmod4\) are all \(1/8\). At the other residue classes the rank is smaller than eight. This proves the complete saturation classification.

For fixed edge number \(q=mn\), the product of nonzero squared singular values equals \(4(q+1-m-n)/q^2\). On the permitted range of this product, \(\mu_-\) and hence \(h(\mu_+)\) increase strictly with it, except that pairs exchanged by reflection have equal values. Thus minimizing \(m+n\), equivalently taking the closest complementary factors of \(q\), maximizes the peak entropy. Finally, if both \(m,n\to\infty\), then \(\mu_-=4/(mn)(1+o(1))\). Using \(h(p)=p(1-\log p)+O(p^2)\) as \(p\downarrow0\) proves the displayed entropy asymptotic.

## Verification

The accompanying `verify.py` implements the full arc-by-arc Grover evolution on \(\mathbb C^{\mathcal A}\otimes\mathbb C^{\mathcal A}\), **without using** the reduced Kronecker-block update in the simulation. It compares all nonzero squared singular values and their entropy with the closed formulas at times \(0,1,2,3,4\), for nine pairs of part sizes including stars, symmetric bicliques, and irregular bicliques, in both exchange-symmetry sectors. All **90 exact-time spectral/entropy comparisons** passed within the specified numerical tolerances. Separate comparisons verify the balancing rule at six fixed edge numbers. These computations test finite instances; the derivation above proves the formulas for every positive integer \(m,n\) and every integer \(t\geq0\).

To reproduce in an environment with NumPy installed, execute `python3 verify.py` from the same directory. For example, at \((m,n)=(2,3)\), the two eigenvalues of \(GG^\mathsf{T}\) are \(2/3\) and \(1/3\); at step two the Schmidt probabilities are \(2/9\) twice, \(1/9\) four times, and \(1/18\) twice. At \((m,n)=(2,2)\), they are eight copies of \(1/8\).

## Relationship to prior work

Kubota, Matsubara, and Segawa (2026) introduce the specific two-particle Grover walk on \(G\otimes G\), prove exchange symmetry, and classify perfect entropy saturation for the **regular** family \(K_{n,n}\), using its four-periodic evolution. Their paper supplies the model, the initial Bell-like states, and relevant explicit amplitude formulas. The new statement here is the **entire Schmidt probability spectrum** and a closed entropy profile on the **larger irregular family \(K_{m,n}\)**, including the uniform rank bound, sharp entropy optimum at fixed edge count, and vanishing entropy enhancement as both parts grow. The regular-case saturation result is acknowledged as prior work, not asserted as new. The present calculation specializes consistently to it.

Carson, Loke, and Wang (2015) study entanglement dynamics of discrete-time two-particle walks with a **different local phase interaction**: the two-particle coin is a tensor product of single-particle Grover coins except at coincident positions, where it is modified. That is not the degree-product Grover reflection at every vertex of \(G\otimes G\) used here, so their results do not directly imply the stated exact spectrum. Standard facts about singular values of Kronecker products, Schmidt decomposition, and entropy additivity are used openly rather than treated as new.

## Limitations

The result applies only to complete bipartite graphs, to the specified symmetrized or antisymmetrized opposite-edge initial state, and to the Grover coin **on the graph product**. It does not cover arbitrary initial states, local-interaction coined walks, weighted/non-Grover coins, or general graph families. The entropy is the source's particle-factor reduced-density entropy for indistinguishable particles; it need not coincide with an operationally accessible entanglement resource under particle-superselection restrictions. The numerical checker is a finite reproducibility test and is not an infinite classification algorithm. Originality has been compared with accessible primary literature and indexed research claims, but complete exclusion of unknown or implicit consequences of broader quantum-walk theorems is not established.

## References

1. Sho Kubota, Haruhiko Matsubara, Etsuo Segawa, *Entanglement entropy in two-particle Grover walks on graphs* (2026), arXiv:2607.09066v1, first submitted 2026-07-10. Full public text: https://arxiv.org/html/2607.09066v1.
2. G. R. Carson, T. Loke, J. B. Wang, *Entanglement dynamics of two-particle quantum walks* (2015), arXiv:1511.04828v1. Full public text: https://arxiv.org/html/1511.04828v1.
3. M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information*, 2010, for the standard reduced-density entanglement entropy and its maximality criterion.
