# Cotangent screening of arbitrary chord families in cyclic two-summing norms

## Finding
For every integer \(n\ge5\), identify the vertices of the cycle \(C_n\) with \(\mathbb Z/n\mathbb Z\). Let \(\mathcal C\) be any set of unordered nonadjacent vertex pairs. Give each chord \(\{u,v\}\in\mathcal C\) a positive amplitude \(a_{uv}\). Write \(k(u,v)=\min\{|u-v|,n-|u-v|\}\in\{2,\ldots,\lfloor n/2\rfloor\}\), where representatives are chosen in \(\{0,\ldots,n-1\}\), and put
\[
T_{n,k}=\left[\frac{\cot(\pi/(2n))}{\sum_{j=0}^{k-1}\cot((2j+1)\pi/(2n))}\right]^{1/2}.
\]
In the real free two-convex Banach lattice \(\operatorname{FBL}^{(2)}[\ell_2^n(\mathbb R)]\), define
\[
F_{n,\mathcal C,a}=\bigvee_{i\in\mathbb Z/n\mathbb Z}|\delta_{e_i-e_{i+1}}|\ \vee\ \bigvee_{\{u,v\}\in\mathcal C}a_{uv}|\delta_{e_u-e_v}|,
\]
with the second supremum omitted if \(\mathcal C\) is empty. The exact simultaneous screening criterion is
\[
\boxed{\quad \|F_{n,\mathcal C,a}\|=\frac2{\sqrt n}\cot\frac\pi{2n}\quad\Longleftrightarrow\quad a_{uv}\le T_{n,k(u,v)}\ \text{for every chord}.\quad}
\]
The same equality criterion holds for the absolutely two-summing norm \(\pi_2(D_{n,\mathcal C,a})\) of the associated real operator \(D_{n,\mathcal C,a}:\ell_2^n\to\ell_\infty^{n+|\mathcal C|}\), whose coordinate rows are the cycle differences and amplified chord differences.

The criterion is coordinatewise even when all possible chords are introduced simultaneously: chords below their individual thresholds have no collective effect on the norm, whereas any chord above its threshold makes the norm strictly larger. For each admissible \(k\ge2\),
\[
\frac1k<\frac1{\sqrt k}<T_{n,k}<1.
\]
Thus there is a nonempty interval of amplitudes for which adding a chord strictly enlarges the positive lattice element *pointwise*, while leaving its norm unchanged. For example, on \(C_6\), the diameter chord has threshold \(T_{6,3}=\sqrt{(2+\sqrt3)/5}>4/5\). Giving this chord amplitude \(4/5\) preserves the free-lattice norm, even though the potential \(x=(0,1,2,3,2,1)\) has cycle supremum \(1\) and amplified chord value \(12/5\). For fixed \(k\), and for chords joining approximately opposite vertices, respectively,
\[
\lim_{n\to\infty}T_{n,k}=\left(\sum_{j=0}^{k-1}\frac1{2j+1}\right)^{-1/2},\qquad
T_{n,\lfloor n/2\rfloor}\sim\sqrt{\frac2{\log n}}.
\]

## Assumptions and scope
All scalars are real; the generator has its standard Euclidean norm. The evaluation map is \(\delta_v(x)=\langle v,x\rangle\) on the Euclidean dual, and lattice suprema and absolute values are taken pointwise. The infinite-dimensional free-lattice norm is the standard one with two-convexity constant one. Every chord has a positive scalar multiplier; it need not itself be assigned a shortest-path metric length. The result applies to any subset of the \(n(n-3)/2\) possible chords, including the full set, with freely chosen positive amplitudes. Equality concerns the *entire* free-lattice norm and the unrestricted absolutely two-summing norm, not merely a symmetric or finitely restricted candidate.

## Proof
**1. Reduction to a trace-square-root optimization.** For a finite list \(v_1,\ldots,v_M\in\mathbb R^n\), let \(f(x)=\max_r|\langle v_r,x\rangle|\). The defining free two-convex norm, in the normalization of Jardón-Sánchez et al., takes the supremum of \((\sum_{j=1}^q f(x_j)^2)^{1/2}\) over all finite test lists whose row matrix \(U\) satisfies \(\|U\|_{\ell_2^n\to\ell_2^q}\le1\). For fixed assignments \(r_j\), introduce a unit vector \(z\in\ell_2^q\) to dualize the outer Euclidean norm. Operator/nuclear-norm duality gives
\[
\sup_{\|U\|_{\rm op}\le1}\sum_jz_j\langle v_{r_j},x_j\rangle
=\left\|\begin{pmatrix}z_1v_{r_1}^{\mathsf T}\\\vdots\\z_qv_{r_q}^{\mathsf T}\end{pmatrix}\right\|_*
=\operatorname{tr}\sqrt{\sum_jz_j^2v_{r_j}v_{r_j}^{\mathsf T}}.
\]
Every probability distribution on the finite list is realized by taking one test index per row and \(z_j=\sqrt{w_j}\). Hence, *with no restriction on the number or symmetry of tests*,
\[
\|f\|=\pi_2\bigl(x\mapsto(\langle v_r,x\rangle)_r\bigr)
=\max_{w_r\ge0,\ \sum_rw_r=1}\operatorname{tr}\sqrt{\sum_rw_rv_rv_r^{\mathsf T}}.\tag{1}
\]
The positive-semidefinite matrix square-root trace is concave.

**2. The optimum for the unperturbed cycle.** Write \(b_i=e_i-e_{i+1}\) and \(L_n=\sum_i b_ib_i^{\mathsf T}\). By concavity and cyclic rotational invariance, averaging any admissible weights over rotations proves that \(w_i=1/n\) is a global maximizer for the original \(n\) rows. The corresponding matrix is \(L_0=L_n/n\). Its restriction to the mean-zero subspace is positive definite, and its nonzero eigenvalues are \(4\sin^2(\pi r/n)/n\), \(1\le r<n\). Consequently
\[
\Phi_0=\operatorname{tr}\sqrt{L_0}
=\frac2{\sqrt n}\sum_{r=1}^{n-1}\sin(\pi r/n)
=\frac2{\sqrt n}\cot(\pi/(2n)).\tag{2}
\]
The common derivative of the objective with respect to any old edge weight at this point is \(\Phi_0/2\), since the objective is homogeneous of degree \(1/2\) in the weights.

**3. Exact all-chord optimality test.** On the mean-zero subspace, the derivative of \(\operatorname{tr}\sqrt L\) in a rank-one direction \(vv^{\mathsf T}\) at \(L_0\) is \(\frac12v^{\mathsf T}L_0^{-1/2}v\). Put
\[
\rho_{n,k}=(e_0-e_k)^{\mathsf T}L_n^{-1/2}(e_0-e_k),
\]
where the inverse square root is zero on constants. The gradient for a chord of amplitude \(a\) and cyclic distance \(k\) is \(\frac12\sqrt n\,a^2\rho_{n,k}\). A concave differentiable function on the probability simplex is globally maximized at the original uniform weight vector (zero mass on every new chord) exactly when each newly available coordinate gradient is at most the common original gradient. Thus, using the old-edge identity \(\rho_{n,1}=(2/n)\cot(\pi/(2n))\), the necessary and sufficient test is
\[
 a^2\rho_{n,k}\le\rho_{n,1}\quad\text{for every chord}.\tag{3}
\]
When any inequality is violated, transferring an arbitrarily small positive weight from the old uniform edge distribution to that chord has strictly positive first derivative, hence strictly increases (1). When all inequalities hold, the supporting hyperplane inequality for the concave objective bounds *every* weight vector, including all combinations of new chords, by \(\Phi_0\). This establishes the asserted absence of collective effects.

**4. Evaluation of the spectral kernel.** Fourier diagonalization of \(L_n\) gives
\[
\rho_{n,k}=\frac2n\sum_{r=1}^{n-1}\frac{\sin^2(\pi kr/n)}{\sin(\pi r/n)}.
\]
The trigonometric identity \(\sin^2((k+1)z)-\sin^2(kz)=\sin((2k+1)z)\sin z\) implies
\[
\rho_{n,k+1}-\rho_{n,k}=\frac2n\sum_{r=1}^{n-1}\sin((2k+1)\pi r/n)
=\frac2n\cot((2k+1)\pi/(2n)).
\]
Since \(\rho_{n,0}=0\), telescoping yields
\[
\rho_{n,k}=\frac2n\sum_{j=0}^{k-1}\cot((2j+1)\pi/(2n)),\quad1\le k\le\lfloor n/2\rfloor.\tag{4}
\]
Combining (2)--(4) proves the exact threshold and baseline norm.

**5. Strict pointwise growth and asymptotics.** For \(2\le k\le\lfloor n/2\rfloor\), the \(k\) cotangents in (4) are strictly positive and decreasing, so \(\rho_{n,1}<\rho_{n,k}<k\rho_{n,1}\), proving \(1/\sqrt{k}<T_{n,k}<1\). A real vector with slopes one along the short arc of length \(k\) and slopes \(-k/(n-k)\) along the complementary arc has maximal original edge difference one and endpoint difference \(k\). Every amplitude exceeding \(1/k\) therefore makes the new lattice element strictly larger at that vector. For fixed \(k\), the cotangent arguments tend to zero, yielding the stated odd-harmonic limit. Finally, for \(k=\lfloor n/2\rfloor\), the uniform estimate \(\cot x=1/x+O(1)\) on \((0,\pi/2]\) gives
\[
\sum_{j=0}^{k-1}\cot((2j+1)\pi/(2n))
=\frac{2n}\pi\sum_{j=0}^{k-1}\frac1{2j+1}+O(n)
=\frac n\pi\log n+O(n).
\]
As \(\cot(\pi/(2n))=2n/\pi+O(1/n)\), the opposite-vertex asymptotic follows. \(\square\)

## Verification
The accompanying `check_cycles.py` numerically reconstructs the full mean-zero Laplacian, independently maximizes (1) over unrestricted edge-weight simplices, tests one- and two-chord screening on both sides of the exact threshold, and independently checks the spectral derivative and baseline formula. The executed suite passed 77 configurations. Its floating-point optimizations corroborate the proof, and are not presented as certificates for the universal statement. Equations (1)--(4) and the supporting-hyperplane argument are the infinite-family proof.

## Relationship to prior work
Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky (first posted January 10, 2021) establish the free two-convex norm representation for arbitrary Banach generators; the first equality in (1) relies on that representation. They do not give the cycle-chord threshold, the all-chord simultaneous criterion, or the cotangent/geometric separation. A prior record on graph edge-difference absolutely two-summing norms provides general Laplacian bounds and an exact value for edge-transitive graphs, including the **unperturbed** cycle, but its stated claim does not contain (3)--(4) or any augmented-cycle saturation criterion. Published complete-bipartite and tripartite free-lattice calculations concern different graph families. A cycle Riesz/Hilbert-transform result evaluates a related half-grid cotangent kernel; its operator and endpoint norms differ, and its full statement does not imply the two-summing optimization criterion. These related formulas are credited rather than counted as new.

## Limitations
This is an exact equality criterion for the *baseline* norm, not a formula for the increased norm once some chord exceeds its threshold. The argument assumes the real Euclidean generator, exponent two, identical unit amplitude on original cycle edges, and arbitrary positive amplitudes on nonadjacent chord rows; it does not cover complex scalars, other convexity exponents, arbitrary weighted base cycles, or generic graphs. The finite checks provide no independent scientific audit or proof of novelty. An equivalent statement under operator-ideal or experimental-design terminology in unindexed literature remains a residual risk.

## References
Jardón-Sánchez, H., Laustsen, N. J., Taylor, M. A., Tradacete, P., and Troitsky, V. G., *Free Banach lattices under convexity conditions*, arXiv:2101.03510 (first posted January 10, 2021); RACSAM 116, article 15 (2022), DOI 10.1007/s13398-021-01155-8. Primary MSC2020 46B42. In particular, Sections 1 and 6 furnish the free two-convex norm.

Prior mathematical record, *Sharp spectral bounds and equality for graph-gradient two-summing norms*, identifier de73f9fb-4574-4349-88d3-b006cad4e0c9. Its stated result supplies general Laplacian bounds and the edge-transitive unperturbed case, but not the new cycle-chord criterion. This comparison concerns its claim, not possible extensions of its proof methods.

Published research record, *Cycle Riesz transforms as parity blocks of doubled cyclic Hilbert transforms* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cycle-riesz-transforms-as-parity-blocks-of-doubled-cyclic-hilber--241f167596e5. Its half-grid cotangent identity concerns a different endpoint operator norm, not the chord-screening law for absolutely two-summing norms.
