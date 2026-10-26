# Sharp topological reversibility and persistent triple fibres for all weighted tree Huygens maps

## Finding
Let \(n\ge1\), let \(K\) be any real symmetric positive-definite \(n\times n\) matrix, and let \(A=\operatorname{diag}(a_1,\ldots,a_n)\) have positive diagonal entries. Put \(S=A^{1/2}KA^{1/2}\) and \(\lambda=\lambda_{\max}(S)>0\). For every \(h>0\), define the torus map \(F_h:\mathbb T^n\to\mathbb T^n\), \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), by
\[
 F_h(z)=z+hKA\sin z\pmod{2\pi}.
\]
Then exactly three topological regimes occur: (i) for \(0<h<1/\lambda\), \(F_h\) is a real-analytic diffeomorphism; (ii) for \(h=1/\lambda\), \(F_h\) remains a homeomorphism but is not a local diffeomorphism; (iii) for every \(h>1/\lambda\), there exists a nonempty open subset of \(\mathbb T^n\) for which every regular target has at least three distinct regular preimages. In fact a nonempty open set of regular targets has this property. Thus the exact global injectivity threshold includes the singular endpoint, and injectivity never returns at larger coupling.

For every finite tree with \(n+1\) vertices and positive edge weights \(a_i\), write \(B\) for its oriented vertex-edge incidence matrix. In independent edge-difference coordinates the sinusoidal discrete Huygens quotient is precisely this map with \(K=B^TB\), which is positive definite, and \(A\) the edge-weight matrix. No diagonal-dominance or balanced-weight assumption is required.

## Assumptions and scope
Real coordinates of \(\mathbb R^n\) are lifted modulo \(2\pi\). All matrix eigenvalues, definiteness and orientation signs below are real. The result concerns topological injectivity and multiplicity of inverse branches; it does not imply Morse–Smale dynamics or transversality. The graph conclusion concerns **trees**, whose edge differences are independent; an arbitrary graph with cycles has additional edge constraints and is not asserted to satisfy this theorem.

## Proof
**1. Strict injectivity through the critical parameter.** On the real lift set \(\widetilde F_h(z)=z+hKA\sin z\). For distinct \(x,y\in\mathbb R^n\), let \(v=x-y\ne0\). By the strict global Lipschitz inequality of sine,
\[
 v_i(\sin x_i-\sin y_i)>-v_i^2\quad\text{whenever }v_i\ne0,
\]
which is strict because \(\sin'\) takes the value \(-1\) only at isolated points. Therefore
\[
 v^TK^{-1}(\widetilde F_h(x)-\widetilde F_h(y))
 =v^TK^{-1}v+h\sum_i a_i v_i(\sin x_i-\sin y_i)
 >v^TK^{-1}v-hv^TAv.
\]
Writing \(w=A^{1/2}v\), the Rayleigh principle gives \(v^TK^{-1}v=w^TS^{-1}w\ge\lambda^{-1}v^TAv\). Hence the displayed pairing is positive when \(0<h\le1/\lambda\). The lift is injective, and it is proper since \(\widetilde F_h(z)-z\) is bounded. Invariance of domain and properness make this lift a homeomorphism of \(\mathbb R^n\). Because \(\widetilde F_h(z+2\pi k)=\widetilde F_h(z)+2\pi k\), its inverse is equivariant, so it descends to a torus homeomorphism.

**2. Smooth regime and singular boundary.** Put \(D(z)=\operatorname{diag}(\cos z_1,\ldots,\cos z_n)\). By conjugating with \(A^{1/2}\) and then symmetrizing with \(S^{1/2}\), the derivative \(I+hKA D(z)\) is similar to the real symmetric matrix \(I+hS^{1/2}D(z)S^{1/2}\). Its eigenvalues lie in \([1-h\lambda,1+h\lambda]\). Thus for \(0<h<1/\lambda\) the Jacobian is everywhere invertible with positive determinant, and the torus homeomorphism is a real-analytic diffeomorphism. At \(h=1/\lambda\), choosing \(z=(\pi,\ldots,\pi)\) gives \(DF_h=I-hKA\) with a zero eigenvalue, so no local differentiable inverse exists there; step 1 still proves a homeomorphism.

**3. One negative direction for every supercritical coupling.** Fix \(h>1/\lambda\). Choose a unit top eigenvector \(u\) of \(S\), and an index \(j\) with \(u_j\ne0\). For sufficiently small \(\delta>0\), take \(t=(h\lambda)^{-1}-\delta\in(0,1)\), and choose \(\varepsilon\) satisfying \(\delta/u_j^2<\varepsilon<1-t\). Prescribe a torus point by \(\cos z_i=-t\) for \(i\ne j\) and \(\cos z_j=-t-\varepsilon\). In the symmetric Jacobian representation we obtain
\[
 H=I-htS-h\varepsilon S^{1/2}e_je_j^TS^{1/2}.
\]
The first term \(I-htS\) is positive definite, and the second term has rank one and is negative semidefinite. Consequently \(H\) has **at most one** negative eigenvalue and no more than one nonpositive eigenvalue. But
\[
 u^THu=1-ht\lambda-h\varepsilon\lambda u_j^2
 =h\lambda(\delta-\varepsilon u_j^2)<0.
\]
Thus \(H\) has exactly one negative eigenvalue, all its other eigenvalues are positive, and \(\det DF_h(z)<0\) at this regular point. The argument works even when the largest eigenvalue has multiplicity greater than one; no spectral simplicity is needed.

**4. Persistent regular triple fibres.** The map \(F_h\) is homotopic to the torus identity through \(z\mapsto z+shKA\sin z\), so its topological degree is \(+1\). Around the negative-orientation regular point from step 3, the inverse function theorem provides an open set of target points having one negative-orientation regular preimage. Sard's theorem gives regular values in that open set; moreover the regular values form an open set because the critical-value set of a smooth map from a compact manifold is compact and has measure zero. For any such regular value, its finite collection of preimages has signs summing to \(+1\). One negative sign forces at least two positive signs, hence at least three distinct regular preimages. This also proves failure of global injectivity for every \(h>1/\lambda\).

## Verification
The associated standalone script `verify.py` checks exact rational Jacobian determinants for scalar and two-edge path instances, the non-diffeomorphic critical threshold, and elementary degree-sign consistency. These examples illustrate the rank-one construction; the universally quantified result follows from steps 1–4, not from finite testing.

## Relationship to prior work
Buescu, D'Aniello and Oliveira (2026), arXiv:2610.10993v1, §3 and Theorems 4.1, 4.6, prove the strict small-coupling diffeomorphism regime for sinusoidal networks and strong Morse–Smale results under diagonal-dominance hypotheses. Their Remark 4.4 and Corollary 5.3 establish **loss of local diffeomorphism** at and beyond the threshold, but this does not by itself settle global topological injectivity at the singular endpoint or robust multiplicity for *all* higher couplings. The present result supplies those topological conclusions for the entire positive-definite weighted matrix class, including every weighted tree without diagonal dominance. Buescu and Oliveira (2026), arXiv:2610.19953v1, concerns cycle constraints and is not used to claim a corresponding arbitrary-graph result. Prior specialized cycle multiplicity results concern a constrained topology rather than this universal weighted-tree conclusion.

## Limitations
The result does not establish exact fibre counts (only an open set of at least three), persistent dynamical attractors, nor a sharp threshold for graphs with cycles. A positive-definite arbitrary-matrix statement does not imply transversality of invariant manifolds. Earlier equivalent treatments under alternative global-inversion terminology cannot be ruled out by bibliography searches alone. The cited source supplies the model and spectral background; the new steps are independently proved here. Independent validation has not been performed.

## References
1. J. Buescu, C. D'Aniello and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (first public 2026-10-07), especially Theorems 3.2, 4.1, 4.6, Corollary 5.3, Remark 4.4. https://arxiv.org/abs/2610.10993
2. J. Buescu and H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1 (first public 2026-10-14). https://arxiv.org/abs/2610.19953
3. Standard results used: invariance of domain, Sard's theorem, and the topological-degree formula for regular values of smooth maps between oriented closed manifolds.
