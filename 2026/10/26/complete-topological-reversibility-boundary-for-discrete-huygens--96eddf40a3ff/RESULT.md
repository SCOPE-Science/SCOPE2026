# Complete topological reversibility boundary for discrete Huygens rings

## Finding
Fix \(n\ge3\). Index the vertices and edges of the unweighted cycle by \(\mathbb Z/n\mathbb Z\), and orient all edges consistently around the cycle: edge \(j\) points from vertex \(j\) to vertex \(j+1\). Let \(B\) be the incidence matrix with columns \(e_{j+1}-e_j\), and set \(K=B^{\mathsf T}B\). On the edge-difference torus
\[
\mathcal Z_n=\{z\in(\mathbb R/2\pi\mathbb Z)^n:\sum_j z_j\equiv0\pmod{2\pi}\},
\]
consider \(F_h(z)=z+hK\sin z\) for \(h>0\), with coordinatewise sine and output modulo \(2\pi\). Put
\[
\Lambda_n=\begin{cases}4,&n\text{ even},\\2+2\cos(\pi/n),&n\text{ odd},\end{cases}
\qquad h_n^*=1/\Lambda_n.
\]
The exact global injectivity regime is \(0<h\le h_n^*\). For \(0<h<h_n^*\) the map is a real-analytic diffeomorphism. At \(h=h_n^*\) it is a homeomorphism with singular differential at some configurations, so its inverse is not \(C^1\). For **every** \(h>h_n^*\) there is a nonempty open set of regular target values each with at least **three distinct regular preimages**. Thus injectivity never returns at larger coupling. The strict-subcritical diffeomorphism is prior work; the principal claim here is the persistence of open regular triple fibres over the entire supercritical parameter interval on the constrained cycle torus.

## Assumptions and scope
The phases are modulo \(2\pi\), and the sole quotient of the vertex-phase torus is by simultaneous rotation. If edge orientations are changed to \(B'=BS\) for a diagonal sign matrix \(S\), the new variables are \(z'=Sz\), the matrix is \(K'=SKS\), and the new domain is \(S\mathcal Z_n=\{z':\mathbf1^{\mathsf T}Sz'\equiv0\pmod{2\pi}\}\). Since \(\sin(Sz)=S\sin z\), the two maps are conjugate by \(S\) on these domains. The unsigned closure formula is used only in the consistent orientation. Regularity refers to the derivative on the \((n-1)\)-dimensional torus. No stability or convergence assumption is imposed.

## Proof

**1. Injectivity through the threshold.** Put \(L=BB^{\mathsf T}\) and \(E=\mathbf1^\perp\subset\mathbb R^n\). The cycle Laplacian has eigenvalues \(2-2\cos(2\pi k/n)\) for \(0\le k<n\), by the Fourier basis. Its maximum is \(\Lambda_n\), simple for even \(n\) and of multiplicity two for odd \(n\). The map \(z=B^{\mathsf T}\theta\) from the vertex torus is onto \(\mathcal Z_n\) by successive summation of edge differences, and its kernel is exactly the simultaneous rotations. The vertex lift
\[
\widetilde F_h(\theta)=\theta+hB\sin(B^{\mathsf T}\theta)
\]
induces \(F_h\) on this quotient. It commutes with simultaneous phase translations and satisfies \(\widetilde F_h(\theta+2\pi k)=\widetilde F_h(\theta)+2\pi k\) for \(k\in\mathbb Z^n\).

For \(s\ne t\), \((s-t)(\sin s-\sin t)>-(s-t)^2\), since \(1+\cos u\) is nonnegative and not identically zero on any interval of positive length. For \(d=\theta-\phi\ne0\) with \(B^{\mathsf T}d\ne0\), the componentwise strict inequality gives
\[
d\cdot(\widetilde F_h(\theta)-\widetilde F_h(\phi))>\|d\|^2-h\|B^{\mathsf T}d\|^2\ge(1-h\Lambda_n)\|d\|^2\ge0
\]
when \(h\le h_n^*\). If \(B^{\mathsf T}d=0\) the left side is \(\|d\|^2>0\). The lift is injective, and lattice equivariance gives injectivity on the vertex torus. The torus map has degree one by homotopy to the identity, so it is onto and, by compactness, a homeomorphism. Equivariance under rotations then gives the quotient homeomorphism as well.

The derivative of the vertex lift is \(I+hB\operatorname{diag}(\cos(B^{\mathsf T}\theta))B^{\mathsf T}\); its restriction to \(E\) represents the quotient derivative up to conjugacy. It is positive definite for \(h<h_n^*\) since \(B\operatorname{diag}(\cos z)B^{\mathsf T}\succeq-L\). Thus the inverse is analytic there. At \(h=h_n^*\), for even \(n\) take all edge phases equal to \(\pi\). The quotient derivative is \(I-L/\Lambda_n\) on \(E\) and has a kernel. For odd \(n\) take one zero edge phase and all other edges equal to \(\pi\); this too obeys closure. With \(b\) the column of the exceptional edge, the quotient derivative is \(I-L/\Lambda_n+2bb^{\mathsf T}/\Lambda_n\) on \(E\). The two-dimensional top eigenspace of \(L\) has a nonzero vector in \(b^\perp\), giving a kernel. The chain rule excludes a \(C^1\) inverse at either example.

**2. A regular negative-orientation source at every supercritical step.** Fix \(h>h_n^*\) and put \(c_*=-1/(h\Lambda_n)\in(-1,0)\). For \(c\) near \(c_*\) in \((-1,0)\), put \(a=\arccos c\).

If \(n\) is even, assign \(+a\) to half the edges and \(-a\) to half. This obeys closure. The derivative is \(J(c)=I+hcL\) on \(E\), and \(J(c_*)\) has a simple zero eigenvalue and all others positive. For \(c<c_*\) close enough it has exactly one negative eigenvalue and no zero eigenvalues.

If \(n\) is odd, assign \(+a\) and \(-a\) each to \((n-1)/2\) edges and zero to the remaining edge, with column \(b\). Again closure holds. On \(E\) the derivative is
\[
J(c)=I+h\big(cL+(1-c)bb^{\mathsf T}\big),\qquad
J(c_*)=I-L/\Lambda_n+h(1-c_*)bb^{\mathsf T}.
\]
The summands in \(J(c_*)\) are positive semidefinite. Their common kernel is the intersection of the top eigenspace of \(L\) with \(b^\perp\). The Fourier character of frequency \((n-1)/2\) has a nonzero difference across every edge, so projection of \(b\) onto the real two-dimensional top eigenspace is nonzero. The common kernel therefore has dimension one. For a vector \(v\ne0\) spanning it, \(J(c)v=(1+hc\Lambda_n)v\) for all \(c\); the other eigenvalues remain positive when \(c\) is sufficiently close to \(c_*\). Thus taking \(c<c_*\) close enough gives exactly one negative eigenvalue and no zero eigenvalues for odd \(n\) as well.

**3. Degree and the open set of triple fibres.** The map on \(\mathcal Z_n\) has degree \(+1\) by the homotopy \(F_{sh}\) for \(0\le s\le1\). The negative-orientation source in Step 2 is regular, so a local inverse branch with negative orientation exists on a nonempty open target set \(W\). By Sard's theorem \(W\) contains regular values of the full map. The critical-value set is closed by compactness of the domain, so the regular values in \(W\) form a nonempty open set. At such a value there are finitely many preimages, and their signed count is \(N_+-N_-=1\). The negative branch supplies \(N_-\ge1\), whence \(N_+\ge2\). All three or more preimages are distinct and regular. This proves the claimed sharp global injectivity regime.

## Verification
The accompanying `verify.py` uses the consistent cycle orientation. It checks the cycle Laplacian eigenvalues, endpoint nullity and the single-negative-eigenvalue construction in finite numerical examples: \(3\le n\le40\) at six supercritical coupling ratios for each \(n\), including ratios just above one and as large as one hundred. The recorded output is `VERIFY_OK negative_orientation_samples=228 ring_sizes=38`. The proof above, rather than the finite floating-point checks, establishes the all-parameter and topological conclusions.

## Relationship to prior work
Buescu and Oliveira [1, Theorem 2.1] prove strict-subcritical global diffeomorphism and separately analyze potential decrease. Buescu, D’Aniello and Oliveira [2, Theorem 3.2 and Remark 3.3] give an invertibility bound for reciprocal networks and a sharpness statement for sinusoidal trees. Endpoint singular configurations and local cubic inverse branching on this cycle were studied in [3]; local branching just above the threshold does not settle the arbitrary-step claim. The positive-definite full-torus result in [4] has a closely related degree argument, but its prescribed edge cosines are unconstrained and the graph application has no cycle closure. Here \(K\) is singular and the source of negative orientation is constructed inside the cycle's closed edge-difference torus, including the odd case where the all-\(\pi\) source is unavailable.

## Limitations
The statement is for unweighted cycles. It gives a persistent lower bound on regular fibre size, not an exact inverse-count function. It does not address attractors, Lyapunov functions beyond the known descent regime, or convergence under iteration. Historical priority beyond the inspected statements is not asserted.

## References
1. J. Buescu and H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, [arXiv:2610.19953v1](https://arxiv.org/html/2610.19953v1), §2, Theorem 2.1.
2. J. Buescu, E. D’Aniello and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, [arXiv:2610.10993v1](https://arxiv.org/html/2610.10993v1), Theorem 3.2 and Remark 3.3.
3. *Parity-dependent cubic onset of noninjectivity in discrete Huygens rings*, [Resultary](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-parity-dependent-cubic-onset-of-noninjectivity-in-discrete-huyge--8b2e707e76b5).
4. *Sharp topological reversibility and persistent triple fibres for all weighted tree Huygens maps*, [Resultary](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-sharp-topological-reversibility-and-persistent-triple-fibres-for--a9b6ba912b20).
