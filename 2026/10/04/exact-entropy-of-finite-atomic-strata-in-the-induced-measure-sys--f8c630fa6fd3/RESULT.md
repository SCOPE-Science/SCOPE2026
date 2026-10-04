# Exact entropy of finite-atomic strata in the induced measure system
## Finding
Let \(X\) be a compact metric space, let \(T:X\to X\) be continuous, and let \(K\subseteq X\) be nonempty, compact, and forward invariant. For \(m\ge1\), define
\[\mathcal M_{\le m}(K)=\{\mu\in\mathcal M(K):|\operatorname{supp}\mu|\le m\}.\]
Then \(\mathcal M_{\le m}(K)\) is compact and forward invariant under \(T_*\), and
\[h_{\mathrm{top}}\!\left(T_*\big|_{\mathcal M_{\le m}(K)}\right)=m\,h_{\mathrm{top}}\!\left(T\big|_K\right).\]
The equality is interpreted in \([0,\infty]\).

## Assumptions and scope
The phase space is compact metric, \(T\) is continuous, and \(K\) is a nonempty compact set with \(T(K)\subseteq K\). The measure space carries its usual weak-* topology. No injectivity, expansivity, specification, or finite-dimensional hypothesis is imposed. The result concerns the ordinary topological entropy of the compact invariant systems \((K,T|_K)\) and \((\mathcal M_{\le m}(K),T_*)\).

## Proof
Let
\[\Delta_{m-1}=\{(p_1,\ldots,p_m)\in[0,1]^m:\ p_1+\cdots+p_m=1\}.\]
Define
\[\Psi:\Delta_{m-1}\times K^m\longrightarrow\mathcal M_{\le m}(K),\qquad \Psi(p,x)=\sum_{i=1}^m p_i\delta_{x_i}.\]
This map is continuous and onto: a measure with fewer than \(m\) atoms is represented by allowing zero weights and repeated coordinates. Hence \(\mathcal M_{\le m}(K)\) is compact. Since \(T(K)\subseteq K\), it is also forward invariant. Moreover,
\[T_*\circ\Psi=\Psi\circ(\operatorname{id}_{\Delta_{m-1}}\times T^{\times m}).\]
Thus the finite-atomic system is a factor of \(\operatorname{id}_{\Delta_{m-1}}\times T^{\times m}\). Monotonicity of topological entropy under factors and the standard product formula give
\[h_{\mathrm{top}}\!\left(T_*\big|_{\mathcal M_{\le m}(K)}\right)\le h_{\mathrm{top}}(\operatorname{id}_{\Delta_{m-1}}\times T^{\times m})=m\,h_{\mathrm{top}}(T|_K).\]

For the opposite inequality, choose
\[a_i=\frac{2^{i-1}}{2^m-1},\qquad 1\le i\le m,\]
and set
\[\Phi_m(x_1,\ldots,x_m)=\sum_{i=1}^m a_i\delta_{x_i}.\]
Distinct subsets of \(\{1,2,4,\ldots,2^{m-1}\}\) have distinct sums. Therefore, even when some coordinates coincide, the mass assigned to each atom uniquely determines the set of coordinate indices occupying that atom. Consequently \(\Phi_m\) is injective. It is continuous, so compactness of \(K^m\) makes it a homeomorphism onto its image. It is equivariant:
\[T_*\circ\Phi_m=\Phi_m\circ T^{\times m}.\]
Hence \(\Phi_m(K^m)\subseteq\mathcal M_{\le m}(K)\) is an invariant subsystem conjugate to \((K^m,T^{\times m})\). Entropy monotonicity for subsystems and the product formula now give
\[h_{\mathrm{top}}\!\left(T_*\big|_{\mathcal M_{\le m}(K)}\right)\ge h_{\mathrm{top}}(T^{\times m}|_{K^m})=m\,h_{\mathrm{top}}(T|_K).\]
Combining the inequalities proves the claim.

## Verification
The upper bound and lower bound are logically independent. The upper bound uses the full simplex parametrization of all measures with at most \(m\) atoms; the lower bound uses binary weights to embed the entire \(m\)-fold product without collisions. The binary-subset-sum argument handles repeated coordinates and is the critical injectivity point. Standard entropy identities used are factor monotonicity, subsystem monotonicity, zero entropy of an identity map on a compact space, and finite-product additivity.

## Relationship to prior work
Huo and Wang study entropy amplification from a compact set to the space of all probability measures supported on it. Their Lemma 3.1 uses exactly the binary-weight embedding \(\Phi_m\), and their Proposition 3.2 derives the corresponding lower bound for upper-capacity entropy; their main results concern zero/positive/infinite behavior of the full supported-measure space. The finite-atomic filtration considered here supplies the matching factor upper bound and therefore an exact entropy value at every finite level. In particular, the formula quantifies the amplification mechanism before passage to the full measure space.

## Limitations
This statement concerns compact forward-invariant \(K\) and ordinary topological entropy. It does not assert the analogous exact formula for non-invariant local Bowen or packing entropies, nor for measure strata defined by geometric restrictions other than support cardinality. Although targeted searches and inspection of the motivating paper did not locate this finite-stratum equality, historical priority outside the inspected literature remains a residual risk.

## References
1. Q. Huo and X. Wang, *Entropies of compact subsets and supported measures*, arXiv:2608.09702v1, 2026.
2. P. Walters, *An Introduction to Ergodic Theory*, Graduate Texts in Mathematics 79, Springer, 1982.
