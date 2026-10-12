# No normalized-Laplacian perfect state transfer on trees of even order greater than two

## Finding

**Theorem.** Let \(T\) be any finite, simple, unweighted tree with an even number \(n\ge4\) of vertices. Its normalized Laplacian Hamiltonian \(\mathcal L=I-D^{-1/2}AD^{-1/2}\) admits **no perfect state transfer between any two distinct vertices at any real time**. Equivalently, if \(U(t)=\exp(it\mathcal L)\), then \(|U(t)_{b,a}|<1\) for all distinct vertices \(a,b\) and all \(t\in\mathbb R\). The boundary is exact: the two-vertex tree \(P_2\) does admit perfect state transfer at \(t=\pi/2\).

A structural ingredient is an even-order spectral parity obstruction: if \(0<\theta<2\) is a rational normalized-Laplacian eigenvalue of an even-order tree and \(\theta=p/q\) is in lowest terms with \(q>0\), then \(p\) is **odd**. More generally, the same obstruction holds for any connected bipartite graph having an odd number of edges and an odd number of spanning trees. This excludes all nonendpoint eigenvalues that could carry the requisite even-numerator transfer phases.

## Assumptions and scope

A tree means a finite connected simple graph without cycles. Here \(A\) is its unweighted adjacency matrix, \(D=\operatorname{diag}(d_v)\) its positive degree matrix, \(L=D-A\) its ordinary combinatorial Laplacian, and \(\mathcal L=D^{-1/2}LD^{-1/2}\). State transfer from \(a\) to \(b\) means \(U(t)e_a=\eta e_b\) for some real \(t\) and unit complex scalar \(\eta\); equivalently \(|U(t)_{b,a}|=1\). Either sign in the exponential gives the same existence question. Every claim concerns single-vertex states, not arbitrary superpositions, pretty good transfer, or nonuniform edge weights.

The graph is bipartite, with a diagonal sign matrix \(J\) satisfying \(J^2=I\) and \(J\mathcal L J=2I-\mathcal L\). Its normalized-Laplacian eigenspace projectors are \(E_\theta\); the simple eigenvalues \(0\) and \(2\) have unit eigenvectors \(D^{1/2}\mathbf1/\sqrt{2m}\) and \(JD^{1/2}\mathbf1/\sqrt{2m}\), where \(m=|E(T)|=n-1\). Thus \((E_0)_{a,a}=(E_2)_{a,a}=d_a/(2m)\).

## Proof

**1. An integer characteristic-polynomial obstruction.** Put \(F(z)=\det(zD-L)\in\mathbb Z[z]\). This polynomial is \((\prod_vd_v)\det(zI-\mathcal L)\), so its roots are exactly the normalized-Laplacian eigenvalues. Since a connected graph has simple zero eigenvalue, \(F(z)/z\in\mathbb Z[z]\) is nonzero at zero. The matrix-tree theorem, or directly the all-one adjugate of the Laplacian of a tree, gives
\[
F'(0)=(-1)^{n-1}\sum_vd_v=(-1)^{n-1}2(n-1).
\]
Indeed, every cofactor of \(L\) is the tree's spanning-tree count, namely one. For a rational eigenvalue \(\theta=p/q\ne0\) with coprime integers \(p,q\), \(q>0\), the rational-root theorem applied to the *integer polynomial* \(F(z)/z\) forces \(p\mid 2(n-1)\). As \(n\) is even, \(n-1\) is odd, hence no such numerator can be divisible by four. Now assume \(0<\theta<2\) and \(p\) is even. Reducedness makes \(q\) odd. Bipartite spectral reflection places \(2-\theta=(2q-p)/q\) in the spectrum; this fraction remains reduced, has positive numerator, and that numerator is divisible by four because \(p\equiv2\pmod4\) and \(q\) is odd. Contradiction. Therefore every reduced rational eigenvalue strictly between zero and two has **odd numerator**.

For the more general stated spectral observation, replace the tree cofactor one by the spanning-tree count \(\tau(G)\): \(F'(0)=(-1)^{n-1}2|E(G)|\tau(G)\). When both factors are odd the same argument applies, using bipartite reflection. The subsequent state-transfer theorem only needs the tree case.

**2. Phase and spectral-sign facts.** Suppose transfer from distinct vertices \(a\) to \(b\) occurs. Spectral projection gives \(e^{it\theta}E_\theta e_a=\eta E_\theta e_b\) for every eigenvalue. Projection at the simple zero eigenvalue, whose unit eigenvector has all positive coordinates, forces \(d_a=d_b\) and \(\eta=1\). It follows from realness that for each eigenvalue in the support of \(a\),
\[
E_\theta e_a=s_\theta E_\theta e_b,\qquad e^{it\theta}=s_\theta\in\{+1,-1\}.
\]
The signs are unambiguous on supported eigenspaces. The signs at \(0\) and \(2\) are respectively \(+1\) and \(+1\) if \(a,b\) lie in the same bipartition class, or \(+1\) and \(-1\) if they lie in opposite classes. For vertices in the same class, reflection \(E_{2-\theta}=JE_\theta J\) preserves the sign \(s_\theta\).

**3. Opposite bipartition classes.** Since \(s_2=-1\), one has \(e^{2it}=-1\), so \(t=(2h+1)\pi/2\) for some integer \(h\). At any supported interior eigenvalue \(0<\theta<2\), the requirement \(e^{it\theta}=\pm1\) implies \(\theta=2j/(2h+1)\) for an integer \(j\). In lowest terms this is a rational number with **even numerator**, contrary to step 1. Thus only \(0\) and \(2\) occur in the support of \(a\) and likewise of \(b\). Consequently
\[
1=(E_0)_{a,a}+(E_2)_{a,a}=d_a/m,
\]
so \(d_a=m=n-1\); similarly \(d_b=n-1\). A tree with at least four vertices cannot have two distinct vertices of degree \(n-1\). This case is impossible.

**4. Same bipartition class: the negative-support restriction.** Now \(s_2=+1\), so \(t=h\pi\) for a nonzero integer \(h\). Every supported eigenvalue is rational because \(e^{it\theta}=\pm1\). There must be at least one eigenvalue with negative sign: otherwise summing the projectors would give \(e_a=e_b\). Let \(\theta=p/q\in(0,2)\) be a negatively signed eigenvalue in lowest terms. Take an integer, primitive-coordinate eigenvector \(w\) of the rational generalized eigenproblem \(Lw=\theta Dw\), with nonzero entry at \(a\). Such a vector exists because this kernel is defined over \(\mathbb Q\). The negative projector sign together with \(d_a=d_b\) implies \(w_a=-w_b\).

Reduce the equations \(qLw=pDw\) modulo \(p\). They say \(\sum_{u\sim v}(w_v-w_u)\equiv0\pmod p\) at every vertex. On a finite tree, leaf removal shows that every edge has congruent endpoint coordinates: a leaf has its unique difference zero, and after removing that leaf the remaining equations retain the same form; iterate. Hence all coordinates of \(w\) are congruent to a single \(c\) modulo \(p\). Primitivity gives \(\gcd(c,p)=1\). But \(w_a=-w_b\) implies \(2c\equiv0\pmod p\), so \(p\mid2\). The interior spectral parity from step 1 excludes even \(p\), leaving \(p=1\).

Because \(a,b\) occupy the same bipartition class, the reflected eigenvalue \(2-\theta=(2q-1)/q\) is also negatively signed; its reduced numerator must likewise divide two and be odd. Therefore \(2q-1=1\), hence \(q=1\), and \(\theta=1\). **Every negative-sign eigenvalue is exactly \(1\)**.

**5. Same-class support cannot close.** As the negative support consists only of eigenvalue \(1\),
\[
e_a-e_b=2E_1e_a.
\]
Applying \(\mathcal L-I=-D^{-1/2}AD^{-1/2}\) shows \(D^{-1/2}AD^{-1/2}(e_a-e_b)=0\). As \(d_a=d_b\), the vertices have identical open neighborhoods. In a tree of at least three vertices, distinct open-neighborhood twins are necessarily sibling leaves. Thus \(d_a=d_b=1\), \((E_1)_{a,a}=1/2\), and
\[
(E_0)_{a,a}+(E_1)_{a,a}+(E_2)_{a,a}
=\frac1m+\frac12<1\qquad(m=n-1\ge3).
\]
There is therefore another supported eigenvalue \(\theta\in(0,2)\setminus\{1\}\). It must have positive sign. Since \(e^{it}=e^{ih\pi}=-1\), \(h\) is odd, while \(e^{ih\pi\theta}=+1\) forces \(\theta=2j/h\) for some integer \(j\). This has even numerator in lowest terms, contrary to step 1. Hence same-class transfer is also impossible. Together with step 3 this proves the theorem.

The two-vertex exception is immediate: its normalized Laplacian has eigenvalues \(0,2\), and \(U(\pi/2)\) swaps its two basis states.

## Verification

The companion Python 3 standard-library script `verify.py` independently calculates the integer generalized characteristic polynomial \(F\) from the matching expansion valid on a tree. On 34 explicitly generated even-order trees (paths, stars, double stars, and brooms, up to 16 vertices), it checks \(F(0)=F(2)=0\), the exact coefficient \(F'(0)=-2(n-1)\), and 2,788 nonzero rational evaluations with reduced even numerators and odd denominators in \((0,2)\). Run from the extracted package root with `python3 verify.py`. The script's expected success line is:

`VERIFY_OK tree_cases=34 parity_probes=2788 derivative_and_endpoint_identities=102`

These are **finite corroborative calculations**. The universal statement is proved analytically in steps 1--5, using the matrix-tree theorem, the rational-root theorem, and tree leaf reduction; the finite probes alone would not establish it.

## Relationship to prior work

Coutinho and Baptista, *Quantum Walks in the Normalized Laplacian* (first arXiv version, 2022), give a characterization of perfect state transfer and a necessary same-bipartition twin-leaf condition in trees. They explicitly leave open the assertion that no trees other than \(P_2\) and \(P_3\) admit such transfer (Section 5, pp. 12--13). The present proof resolves their conjectural exclusion **for all even-order trees** by a two-adic constraint on rational normalized-Laplacian eigenvalues. It reproves the needed sign restriction rather than importing an unsupported global no-transfer claim.

Alvir, Dever, Lovitz, Myer, Tamon, Xu, and Zhan (2014) rule out antipodal normalized-Laplacian transfer on paths beyond three vertices and construct transfer under tensor products; that path-specific theorem does not imply arbitrary even-order trees. Banerjee and Mehatari (2014/2015) derive normalized-Laplacian tree characteristic polynomials in terms of weighted matchings, but do not identify the transfer obstruction proved here in the inspected sections. Standard matrix-tree and rational-root theorems are ingredients, not themselves equivalent to the normalized-Laplacian quantum-transfer conclusion.

## Limitations

This theorem does **not** settle the remaining odd-order-tree case for \(n\ge5\), where the constant coefficient \(2(n-1)\) has additional powers of two and the parity obstruction need not apply. It does not rule out **pretty good** state transfer, including examples on even-order trees, or transfer of general superposition states; it does not address edge-weighted trees. The exact claimed novelty is the universal even-order no-perfect-transfer theorem and its identified two-adic mechanism, not the known two-vertex exception or general state-transfer definitions.

## References

1. G. Coutinho and P. F. Baptista, *Quantum Walks in the Normalized Laplacian*, arXiv:2209.04668v1, first posted 2022-09-10, especially Theorems 5 and 7, Corollaries 8--9, and concluding conjecture. https://arxiv.org/abs/2209.04668
2. R. Alvir, S. Dever, B. Lovitz, J. Myer, C. Tamon, Y. Xu, and H. Zhan, *Perfect State Transfer in Laplacian Quantum Walk*, arXiv:1409.5840 (2014), especially Section 6.2 on normalized-Laplacian paths. https://arxiv.org/abs/1409.5840
3. A. Banerjee and R. Mehatari, *Characteristics polynomial of normalized Laplacian for trees*, arXiv:1406.7769 (2014), Applied Mathematics and Computation 271 (2015), 838--844, Theorem 2.1. https://arxiv.org/abs/1406.7769
4. F. R. K. Chung, *Spectral Graph Theory*, CBMS 92, AMS (1997), standard normalized-Laplacian and matrix-tree background.
