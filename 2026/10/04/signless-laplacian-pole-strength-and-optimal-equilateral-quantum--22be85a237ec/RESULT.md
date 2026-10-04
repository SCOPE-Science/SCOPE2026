# Signless-Laplacian pole strength and optimal equilateral quantum-graph resonators

## Finding

Let \(G=(V,E)\) be a finite connected simple graph with \(d=|V|\ge3\). Regard every vertex as boundary, replace every edge by an interval of common length \(\ell>0\), and impose no internal vertex condition because there are no internal vertices. Let \(\Lambda_G(\lambda)\) be the resulting Dirichlet-to-Neumann map for
\[
-u''=\lambda u.
\]
For an odd integer \(n\ge1\), set
\[
\lambda_0=\left(\frac{n\pi}{\ell}\right)^2
\]
and define the local pole strength by
\[
C_*(G)=
\lim_{\lambda\to\lambda_0,\ \lambda\ne\lambda_0}
|\lambda-\lambda_0|\,
\sigma_{\min}\!\left(\Lambda_G(\lambda)\right).
\]
Then, writing \(Q(G)=D(G)+A(G)\) for the signless Laplacian and \(q_{\min}(G)\) for its least eigenvalue,
\[
C_*(G)=\frac{2\lambda_0}{\ell}\,q_{\min}(G).
\]

Thus the uniform pole estimate used in resonant gap opening has positive sharp asymptotic coefficient exactly when \(G\) is non-bipartite. More precisely, for every \(C<C_*(G)\) there is a punctured neighborhood of \(\lambda_0\) on which
\[
\|\Lambda_G(\lambda)\phi\|
\ge
\frac{C}{|\lambda-\lambda_0|}\,\|\phi\|
\]
for all boundary data \(\phi\), while no \(C>C_*(G)\) can satisfy such an estimate arbitrarily close to \(\lambda_0\).

For fixed boundary size \(d\), the complete graph is the unique optimal simple equilateral all-boundary decoration:
\[
C_*(G)\le
\frac{2\lambda_0}{\ell}(d-2),
\]
with equality exactly for \(G=K_d\).

At an even Dirichlet resonance the corresponding local coefficient is zero. For the degree-four triangle-with-one-pendant-edge example described by Do--Kuchment--Ong,
\[
q_{\min}=\frac{5-\sqrt{17}}{2},
\qquad
C_*=\frac{\lambda_0}{\ell}\left(5-\sqrt{17}\right).
\]
The complete four-vertex decoration has
\[
C_*(K_4)=\frac{4\lambda_0}{\ell},
\]
an exact improvement factor
\[
\frac{C_*(K_4)}{C_*(\text{triangle plus pendant})}
=
\frac{5+\sqrt{17}}{2}
\approx 4.56155.
\]

As another specialization, an odd cycle \(C_m\) has
\[
q_{\min}(C_m)=2-2\cos\!\left(\frac{\pi}{m}\right),
\]
so among odd-cycle-only all-boundary resonators the triangle has the largest pole strength.

## Assumptions and scope

All edges have the same positive length \(\ell\), the differential expression is the free one-dimensional Laplacian, every graph vertex is included in the boundary set, and \(G\) is a finite connected simple graph. The result identifies the sharp *local Dirichlet-to-Neumann pole coefficient* near a prescribed edge-Dirichlet resonance. It does not by itself claim an exact spectral-gap width for an arbitrary host network, because the gap proof of Do--Kuchment--Ong also uses information about the host graph and its distance from the relevant Dirichlet spectrum.

The optimization is over simple \(d\)-vertex all-boundary equilateral decorations at the same \(\ell\) and the same odd resonance. Decorations with internal vertices, multiple edges, unequal edge lengths, potentials, or other vertex conditions are outside the claim.

## Proof

Write \(\lambda=k^2\), with \(k>0\), and suppose first that \(\sin(k\ell)\ne0\). On an edge \(uv\), with coordinate \(x\) increasing from \(u\) to \(v\), boundary values \(f_u\) and \(f_v\) give the unique solution
\[
u_e(x)=
f_u\frac{\sin(k(\ell-x))}{\sin(k\ell)}
+
f_v\frac{\sin(kx)}{\sin(k\ell)}.
\]
Its outgoing derivative at \(u\) is
\[
\partial_\nu u_e(u)
=
\frac{k}{\sin(k\ell)}
\left(f_v-\cos(k\ell)f_u\right).
\]
Summing over edges incident to every boundary vertex gives the exact matrix formula
\[
\Lambda_G(k^2)
=
\frac{k}{\sin(k\ell)}
\left(A(G)-\cos(k\ell)D(G)\right).
\]

Now let \(k_0=n\pi/\ell\). If \(n\) is odd, then \(\cos(k_0\ell)=-1\), so
\[
A(G)-\cos(k\ell)D(G)\longrightarrow A(G)+D(G)=Q(G).
\]
Also,
\[
\lim_{k\to k_0}
|k^2-k_0^2|
\left|\frac{k}{\sin(k\ell)}\right|
=
\frac{2k_0^2}{\ell}
=
\frac{2\lambda_0}{\ell}.
\]
Continuity of singular values therefore yields
\[
C_*(G)
=
\frac{2\lambda_0}{\ell}\,
\sigma_{\min}(Q(G)).
\]
Since \(Q(G)\) is real symmetric positive semidefinite,
\[
\sigma_{\min}(Q(G))=q_{\min}(G),
\]
which proves the pole formula.

For a connected graph, \(q_{\min}(G)=0\) exactly when \(G\) is bipartite. Hence the odd-resonance pole is uniform in all boundary directions exactly for non-bipartite \(G\). If \(n\) is even, then the numerator tends \(A(G)-D(G)=-L(G)\), which has the constant vector in its kernel, and therefore the corresponding \(C_*\) is zero.

It remains to optimize over graphs of order \(d\). For the complement \(\overline G\),
\[
Q(G)+Q(\overline G)=Q(K_d)=(d-2)I+J.
\]
For any nonzero vector \(x\perp\mathbf 1\),
\[
\frac{x^\mathsf TQ(G)x}{\|x\|^2}
=
(d-2)-
\frac{x^\mathsf TQ(\overline G)x}{\|x\|^2}
\le d-2,
\]
because \(Q(\overline G)\) is positive semidefinite. Thus
\[
q_{\min}(G)\le d-2.
\]
For \(K_d\), the signless Laplacian is \((d-2)I+J\), whose least eigenvalue is \(d-2\), so equality is attained.

The equality case is unique. If \(G\ne K_d\), choose an edge \(uv\) of \(\overline G\), and let
\[
x=e_u+e_v-\frac{2}{d}\mathbf 1.
\]
Then \(x\perp\mathbf1\), while the signless-Laplacian quadratic form
\[
x^\mathsf TQ(\overline G)x
=
\sum_{ab\in E(\overline G)}(x_a+x_b)^2
\]
is strictly positive because the term corresponding to \(uv\) is nonzero for \(d\ge3\). Therefore the Rayleigh quotient of \(Q(G)\) at this \(x\) is strictly below \(d-2\), and so
\[
q_{\min}(G)<d-2.
\]
This proves that \(K_d\) is the unique optimizer.

For the four-vertex triangle with one pendant edge, direct factorization gives
\[
\det(tI-Q)
=
(t-2)(t-1)(t^2-5t+2),
\]
hence the least eigenvalue is \((5-\sqrt{17})/2\). The stated improvement factor follows by division.

Finally, the signless-Laplacian spectrum of the cycle \(C_m\) is
\[
2+2\cos\!\left(\frac{2\pi j}{m}\right),
\qquad
0\le j<m.
\]
For odd \(m\), its minimum is \(2-2\cos(\pi/m)\), which decreases strictly with \(m\).

## Verification

`verify_resonator_strength.py` independently checks the finite graph algebra. It enumerates every simple graph through five vertices, reconstructs \(Q(G)\), numerically verifies \(q_{\min}(G)\le d-2\) with equality only for the complete graph, verifies the exact characteristic polynomial of the four-vertex triangle-plus-pendant example by integer polynomial arithmetic, and checks the odd-cycle formula for several sizes.

The checker also evaluates the exact Dirichlet-to-Neumann matrix formula near odd and even resonances for representative non-bipartite and bipartite graphs and confirms convergence of
\[
|\lambda-\lambda_0|\,\sigma_{\min}(\Lambda_G(\lambda))
\]
to the predicted coefficient. These finite checks are supplementary; the general theorem is proved algebraically above.

## Relationship to prior work

Do, Kuchment, and Ong introduced the resonant “spider” decoration mechanism in this setting. Their Theorem 2.1 obtains a lower bound of the form
\[
\|\Lambda(\lambda)\phi\|
\ge
\frac{C}{|\lambda-\lambda_0|}\|\phi\|
\]
when every nonzero boundary datum produces a pole, and their Theorem 2.2 supplies a sufficient odd-cycle construction at odd edge-Dirichlet resonances. Their concluding remark explicitly notes that gap size depends on the constant \(C\) and asks how \(C\) depends on the decoration in order to choose more effective designs.

The present statement evaluates the sharp local coefficient exactly for the natural subclass in which every vertex of a simple equilateral decoration is a boundary vertex. In this subclass the resonant residue reduces to the signless Laplacian. The standard signless-Laplacian fact that a connected graph has positive least signless-Laplacian eigenvalue exactly when it is non-bipartite recovers the odd-cycle obstruction in spectral form.

Targeted searches found general signless-Laplacian graph theory, general quantum-graph Dirichlet-to-Neumann work, and later quantum-graph gap constructions, but did not locate the displayed pole formula or the fixed-\(d\) complete-graph optimization. The closest source remains the Do--Kuchment--Ong paper itself, whose stated design question is being answered here only for the all-boundary equilateral simple-graph class.

## Limitations

The optimized quantity is the asymptotic pole coefficient \(C_*(G)\), not an exact universal gap width. A host-network gap width can depend on additional constants in the gap argument. The complete-graph optimality theorem is restricted to simple graphs with a fixed number of boundary vertices and common edge length. Adding internal vertices, unequal lengths, magnetic phases, edge potentials, or generalized vertex conditions can change the residue matrix and may produce stronger designs outside this class.

The literature search cannot rule out an equivalent identity in unindexed notes or in work using different \(M\)-function terminology. Because the derivation is short once the all-boundary equilateral restriction is imposed, the originality claim is intentionally limited to this explicit reduction and optimization rather than a broad priority claim about resonant quantum-graph design.

## References

1. N. T. Do, P. Kuchment, and B. Ong, “On resonant spectral gap opening in quantum graph networks,” arXiv:1601.04774, first submitted 19 January 2016.
2. N. T. Do, P. Kuchment, and B. Ong, “On resonant spectral gaps in quantum graphs,” in *Functional Analysis and Operator Theory for Quantum Physics*, EMS, 2017, pp. 213–222, DOI: 10.4171/175-1/10.
3. S. Kirkland and D. Paul, “Bipartite Subgraphs and the Signless Laplacian Matrix,” *Applicable Analysis and Discrete Mathematics* 5 (2011), DOI: 10.2298/AADM110205006K.
4. D. Cvetković, P. Rowlinson, and S. K. Simić, “Signless Laplacians of finite graphs,” *Linear Algebra and its Applications* 423 (2007), 155–171, DOI: 10.1016/j.laa.2007.01.009.
