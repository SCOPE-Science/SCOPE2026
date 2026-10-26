# A graph-independent gap bound for inhomogeneous Lee–Yang fields

## Finding

For every finite graph \(G=(V,E)\) with \(n=|V|\) qubits, let \(H=\sum_{\{i,j\}\in E}H_{ij}\), where \(H_{ij}=-w^z_{ij}Z_iZ_j+w^x_{ij}X_iX_j+w^y_{ij}Y_iY_j+w^{xy}_{ij}X_iY_j+w^{yx}_{ij}Y_iX_j\) has real coefficients satisfying, on every edge,
\[
w^z_{ij}\ge\tfrac12\sqrt{(w^x_{ij}-w^y_{ij})^2+(w^{xy}_{ij}+w^{yx}_{ij})^2}+\tfrac12\sqrt{(w^x_{ij}+w^y_{ij})^2+(w^{xy}_{ij}-w^{yx}_{ij})^2}.
\]
For arbitrary positive site-dependent longitudinal fields \(h_i>0\), define \(H_{\mathbf h}=H-\sum_{i\in V}h_iZ_i\) and \(h_*:=\min_{i\in V}h_i\). Then \(H_{\mathbf h}\) has a unique ground state and its spectral gap \(E_1-E_0\) is at least \(h_*/4\), independently of graph size and the allowed coupling strengths.

## Assumptions and scope

The graph and Hilbert space are finite. Each edge interaction is of the displayed two-qubit form and satisfies the Lee–Yang inequality above. The field is longitudinal (in the \(Z\) direction), site-dependent, and strictly positive at every site; \(h_*>0\). The result does not cover zero or mixed-sign fields, arbitrary one-site terms, or interactions outside this Lee–Yang class. The gap is the finite-volume difference between the two lowest eigenvalues, counted with multiplicity.

## Proof

Write \(W=\sum_{\{i,j\}\in E}w^z_{ij}\) and \(\Gamma=3W+\sum_i h_i\). The Lee–Yang inequality implies the zero-freeness of the Trotterized partition polynomial \(\mathcal Z_\epsilon(\mathbf y)\) whenever every coordinate satisfies \(|y_{i,m}|<1\). Choose an ordering of the edges and set \(L=\prod_{\{i,j\}\in E}\exp(-\epsilon H_{ij}/2)\), with the product in that fixed order. The symmetric Trotter step is
\[
\mathcal S_\epsilon=L\exp\!\left(\epsilon\sum_i h_iZ_i\right)L^*,
\]
and its physical polynomial coordinates are \(y^*_{i,m}=e^{-2\epsilon h_i}\); unlike the uniform-field case, these coordinates depend on \(i\).

The support lemma for the Taylor series of \(\log\mathcal Z_\epsilon\) is unchanged: a monomial contributing to the connected correlator of \(Z_S=\prod_{i\in S}Z_i\) between Trotter layers \(0\) and \(k\) must touch both layers. Its total degree is therefore at least \(d_k=\min(k,M-k)+1\), where \(M=\beta/\epsilon\). This argument uses only the rank-one cut at a layer whose variables are set to zero, not equality of the fields across sites.

Set \(h_* = \min_i h_i\). On the circle \(|\lambda|=e^{\epsilon h_*}\), every coordinate on the radial path \(\lambda\mathbf y^*\) satisfies
\[
|\lambda y^*_{i,m}|=e^{\epsilon h_*-2\epsilon h_i}\le e^{-\epsilon h_*}\le e^{-\epsilon h_*/2}.
\]
Thus the same Borel–Carathéodory bound used for the uniform field applies with \(h\) replaced by \(h_*\): for \(C_*:=\max\{n,6\beta W\}\) and \(\epsilon h_*\le2\), the logarithm is bounded by \(16C_*/(\epsilon h_*)\) on the smaller polydisc. The maximum-modulus argument and the degree bound then give, for the Trotterized connected correlator,
\[
|f_{S,\epsilon}(k)|\le {128C_*\over\epsilon h_*}e^{-\epsilon h_*d_k}.
\]

The finite-step comparison remains valid with \(\Gamma=3W+\sum_i h_i\): the operator norm of \(H_{\mathbf h}\) is at most \(\Gamma\), and the field term commutes with every \(Z_S\), so the insertion-commutator estimate is unchanged. In particular, the source proof's Trotter comparison bound holds with \(C_T=48(\beta\Gamma^2+W)\). Choosing \(G=2\max\{C_T,\Gamma,h_*,1\}\) and the adaptive step size of order \(e^{-h_*\tau/2}/G\), where \(\tau=\min(t,\beta-t)\), yields the exact-correlator estimate
\[
|f_S(t)|\le K e^{-h_*\tau/2},\qquad K={256C_*G\over h_*}+2.
\]
For fixed finite graph, couplings, and fields, \(K\) grows at most polynomially in \(\beta\).

Finally, at separation \(t=\beta/2\), the spectral representation of \(f_S\) is a sum of nonnegative terms weighted by \(e^{-\beta(E_j+E_\ell)/2}\). Fix \(0<\delta<h_*/4\) and consider the span of eigenvectors with energy at most \(E_0+\delta\). Combining the spectral representation with the correlation bound shows that every matrix element of \(Z_S-\langle Z_S\rangle_\beta\) between such vectors has squared modulus at most
\[
2^nK e^{-\beta(h_*/4-\delta)},
\]
which tends to zero as \(\beta\to\infty\). Since the products \(Z_S\), together with the identity, span the diagonal operator algebra, two orthonormal vectors in this low-energy span would have to have both disjoint and equal-magnitude amplitudes at every computational-basis vector, an impossibility. The span is therefore one-dimensional for every \(\delta<h_*/4\). The ground state is unique and \(E_1-E_0\ge h_*/4\). This completes the finite-volume proof.

## Verification

The proof reduces to the explicit radial estimate \(e^{\epsilon h_*}e^{-2\epsilon h_i}\le e^{-\epsilon h_*}\), the unchanged layer-support argument, and the source's finite-step and spectral-representation estimates with \(\Gamma=3W+\sum_i h_i\). No numerical extrapolation or finite-size computation is used as proof. The constants are uniform in graph size and edge couplings, but the prefactors in the correlation estimate may depend on the finite graph, couplings, fields, and inverse temperature; the exponential rate is what yields the gap bound.

## Relationship to prior work

Rayudu and Takahashi prove the same \(h/4\) gap bound for a uniform field \(h\) in *Spectral gap of Lee–Yang Hamiltonians* (arXiv:2607.10765, submitted 2026-07-12), using Trotterized Lee–Yang zero-freeness, imaginary-time correlation decay, and a low-energy spectral argument. The present statement allows an arbitrary positive field profile and replaces the uniform field by \(h_* = \min_i h_i\). The key comparison is not a change of notation: the physical zero-free evaluation point becomes a nonconstant vector, and the radial contour must be controlled coordinatewise by its smallest field. The inspected work *Lee–Yang tensors and Hamiltonian complexity* (arXiv:2602.03605) studies Lee–Yang radii and conjectural gaps for EPR-like Hamiltonians, not this inhomogeneous-field theorem. Björnberg and Ueltschi (2015) study transverse fields and transverse correlations, which are different observables and a different field direction.

## Limitations

The bound is a lower bound, not a claim that the constant \(1/4\) is optimal. Strict positivity of every field is essential to this argument; if \(h_*=0\), the radial contour no longer yields exponential decay at a positive rate. The proof concerns finite graphs. A sequence of finite graphs inherits a uniform positive lower bound only when the minimum field is bounded away from zero uniformly along the sequence.

## References

1. C. Rayudu and J. Takahashi, “Spectral gap of Lee-Yang Hamiltonians,” arXiv:2607.10765v1, submitted 2026-07-12, especially Theorems 10–11 and Appendices A–B.
2. B. Wong, S. Bravyi, D. Gosset, and Y. Liu, “Lee-Yang tensors and Hamiltonian complexity,” arXiv:2602.03605v1, submitted 2026-02-03, especially Sections 5.5–5.6 and Section 6.
3. J. E. Björnberg and D. Ueltschi, “Decay of transverse correlations in quantum Heisenberg models,” *Journal of Mathematical Physics* 56 (2015), 043303; arXiv:1501.02109.
