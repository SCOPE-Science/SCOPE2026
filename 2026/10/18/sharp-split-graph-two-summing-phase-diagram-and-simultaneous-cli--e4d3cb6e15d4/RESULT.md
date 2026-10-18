# Sharp split-graph two-summing phase diagram and simultaneous clique-edge screening

## Finding

Fix integers \(a\ge3\) and \(b\ge2\). Let \(A\) and \(B\) be disjoint labelled vertex sets of sizes \(a\) and \(b\), and put \(H=\ell_2^{A\cup B}(\mathbb R)\). In the real free 2-convex Banach lattice \(\operatorname{FBL}^{(2)}[H]\), write \(\delta_z(x)=\langle z,x\rangle\). For \(t\ge0\), form the positive lattice element
\[
 F_{a,b}(t)=\bigvee_{u\in A,\,v\in B}|\delta_{e_u-e_v}|
 \;\vee\;\bigvee_{\{u,v\}\subset A}t|\delta_{e_u-e_v}|.
\]
Thus \(t=0\) is the complete-bipartite edge-difference element and \(t=1\) is the complete-split-graph element. Define
\[
 K_{a,b}=\frac{b-1}{\sqrt b}+\sqrt{\frac{a+b}{ab}},\qquad
 B_{a,b}=\frac{a-1}{\sqrt a}+K_{a,b},\qquad
 \tau_{a,b}^2=\frac{a-1+\sqrt a\,K_{a,b}}{2a}.
\]
Then the exact unrestricted norm is
\[
 \boxed{\|F_{a,b}(t)\|=
 \begin{cases}
 B_{a,b},&0\le t\le\tau_{a,b},\\[2mm]
 \displaystyle\left(2(a-1)t^2+\frac{2at^2K_{a,b}^2}{2at^2-(a-1)}\right)^{1/2},&t>\tau_{a,b}.
 \end{cases}}
\]
There is a **simultaneous sharp screening rule**: for any set \(\mathcal C\subseteq\binom A2\) and nonnegative amplitudes \(s_{uv}\), let
\[
 F_{\mathcal C,s}=\bigvee_{u\in A,v\in B}|\delta_{e_u-e_v}|
 \;\vee\;\bigvee_{\{u,v\}\in\mathcal C}s_{uv}|\delta_{e_u-e_v}|.
\]
Then \(\|F_{\mathcal C,s}\|=B_{a,b}\) **if and only if** every \(s_{uv}\le\tau_{a,b}\). In particular, an arbitrary number of subthreshold clique edges are screened together, whereas one superthreshold edge forces a strict norm increase. Although the norms agree, whenever any added edge has amplitude above \(1/2\), the augmented positive lattice element is strictly larger at some evaluation point than the bipartite element.

For every fixed \(a\ge3\), as \(b\to\infty\),
\[
 \boxed{\tau_{a,b}=\frac1{\sqrt2}\left(\frac ba\right)^{1/4}
 (1+O_a(b^{-1/2})).}
\]
In particular the largest norm-invisible internal-edge amplitude is unbounded as the independent part grows. Furthermore the scalar norm profile is continuously differentiable at \(t=\tau_{a,b}\), but its right second derivative minus its left second derivative equals
\[
 \boxed{\frac{16\tau_{a,b}^2\sqrt a\,(a-1)}{K_{a,b}B_{a,b}}>0.}
\]

## Assumptions and scope

All spaces, operators and lattices are **real**. Coordinates in \(H\) have their standard Euclidean inner product. The free 2-convex lattice has convexity constant one and the norm normalized by the weakly two-summable-sequence formula of Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky. Every graph-edge evaluation uses the unnormalized difference \(e_u-e_v\), of Euclidean length \(\sqrt2\). A clique amplitude is a multiplier on the evaluation, not a graph distance or an edge probability. Only \(a\ge3\), \(b\ge2\), \(t\ge0\) and the explicitly described clique-edge families are asserted. There is no claim about other convexity exponents, arbitrary background graphs, or non-Euclidean generator norms.

## Proof

**1. The norm is a finite spectral-design problem.** For any finite family of nonzero row vectors \(d_e\in H\), set \(D:H\to\ell_\infty^E\), \((Dx)_e=\langle d_e,x\rangle\), and \(f=\bigvee_e|\delta_{d_e}|\). By the defining weak-2 norm of the free 2-convex lattice, \(\|f\|=\pi_2(D)\). We recall and justify the precise Hilbert-space identity
\[
 \boxed{\pi_2(D)=\max_{w_e\ge0,\,\sum_e w_e=1}
 \operatorname{tr}\Bigl(\sum_e w_e d_ed_e^\mathsf T\Bigr)^{1/2}.}\tag{1}
\]
Pietsch's finite-dimensional domination theorem identifies \(\pi_2(D)^2\) with the least \(c\) such that there is a positive covariance \(R\) with \(\operatorname{tr}R=1\) and \(d_e^\mathsf TR^\dagger d_e\le c\) for every row (with the usual support requirement). Indeed a probability measure on the Euclidean unit ball has such a covariance, and conversely the spectral decomposition of any such \(R\) gives a measure. On the common span of the rows, replace \(R\) by positive definite approximants. Since the maximal row quadratic form is the maximum over probability vectors \(w\) of \(\operatorname{tr}(R^{-1}C_w)\), where \(C_w=\sum w_ed_ed_e^\mathsf T\), convex-linear finite-dimensional minimax permits the order of infimum in \(R\) and maximum in \(w\) to be reversed. For each fixed \(C_w\ge0\), Hilbert--Schmidt Cauchy--Schwarz yields
\[
 \inf_{R>0,\,\operatorname{tr}R=1}\operatorname{tr}(R^{-1}C_w)
 =(\operatorname{tr}\sqrt{C_w})^2,
\]
with equality approached by \(R\propto\sqrt{C_w}\). The continuous boundary limits complete (1). One may work throughout on the zero-sum subspace, since all incidence rows annihilate constants.

**2. Exact orbit reduction and spectrum.** The matrix-square-root trace is concave in its positive-semidefinite argument. Averaging any design \(w\) over the coordinate-permutation group \(S_a\times S_b\) therefore does not decrease (1). Every maximizer has an equally good two-orbit design: a total probability mass \(u\) spread uniformly over the \(\binom a2\) clique edges and mass \(1-u\) spread uniformly over the \(ab\) cross edges, where \(0\le u\le1\). The associated Laplacian
\[
 C_u=\frac{ut^2}{\binom a2}L_{K_A}
 +\frac{1-u}{ab}L_{K_{A,B}}
\]
has eigenvalue zero on constants and the following three nonzero eigenspace values:
\[
 \begin{array}{c|c|c}
 \text{space}&\text{dimension}&\text{eigenvalue}\\\hline
 \{x:\operatorname{supp}x\subset A,\ \sum_A x=0\}&a-1&
 \frac{1-u}{a}+\frac{2t^2u}{a-1}\\
 \{x:\operatorname{supp}x\subset B,\ \sum_B x=0\}&b-1&\frac{1-u}{b}\\
 \text{vectors constant on each class and globally centered}&1&
 \frac{(a+b)(1-u)}{ab}.
 \end{array}
\]
Writing \(d=2t^2/(a-1)-1/a\) and \(K=K_{a,b}\), formula (1) becomes the **unrestricted** scalar maximum
\[
 \|F_{a,b}(t)\|=
 \max_{0\le u\le1}\left[(a-1)\sqrt{\frac1a+du}
 +K\sqrt{1-u}\right].\tag{2}
\]
Every derivative and endpoint in (2) follows from the original spectral matrix rather than a restriction on admissible test vectors.

**3. Exact threshold and post-threshold formula.** The objective in (2) is strictly concave on \((0,1)\) because \(K>0\). Its right derivative at zero has the sign of
\[
 \frac{(a-1)d\sqrt a-K}{2}
 =\frac{2t^2\sqrt a-(a-1)/\sqrt a-K}{2}.
\]
This derivative is nonpositive precisely for \(t^2\le\tau_{a,b}^2\), proving the first branch and its sharpness. Above the threshold \(d>0\); the derivative is positive at zero and tends to minus infinity at one, so the unique maximizing \(u\) is interior. Put \(X=\sqrt{1/a+du}\), \(Y=\sqrt{1-u}\). They satisfy \(X^2+dY^2=1/a+d=2t^2/(a-1)\). Cauchy--Schwarz gives the exact attained maximum
\[
 (a-1)X+KY
 =\sqrt{\left((a-1)^2+\frac{K^2}{d}\right)
 \left(\frac1a+d\right)}.
\]
Squaring and simplifying yields the second branch. For reproducibility the interior orbit mass is
\[
 u_*=
 \frac{(a-1)^2d^2-K^2/a}{(a-1)^2d^2+K^2d}
 \quad( t>\tau_{a,b}),
\]
which lies strictly between zero and one. The formulas agree at the boundary.

**4. Any number of independently weighted clique edges.** Let \(C_0\) be the cross-only design with probability \(1/(ab)\) per cross edge. It is positive definite on the zero-sum subspace. Its eigenvalues are \(1/a\) on the \(A\)-zero-sum space, \(1/b\) on the \(B\)-zero-sum space, and \((a+b)/(ab)\) on the between-class direction. For the concave function \(\Phi(w)=\operatorname{tr}\sqrt{\sum w_ed_ed_e^\mathsf T}\), differentiation at this design gives
\[
 \left.\frac{\partial\Phi}{\partial w_e}\right|_{C_0}
 =\tfrac12 d_e^\mathsf TC_0^{-1/2}d_e.
\]
Every cross edge has derivative \(B_{a,b}/2\) by transitivity and Euler's homogeneous trace identity. An added clique edge with amplitude \(s_e\) lies entirely in the \(A\)-zero-sum eigenspace and has derivative \(s_e^2\sqrt a\). Thus **all** clique-edge derivatives are at most the common active-cross derivative exactly when \(s_e^2\le B_{a,b}/(2\sqrt a)=\tau_{a,b}^2\) for all \(e\). In this case, the supporting-hyperplane inequality for the globally concave \(\Phi\) shows that no probability design can outperform \(C_0\). If even one inequality fails, moving a sufficiently small probability mass from the active cross edges onto that offending edge has positive first derivative and strictly increases the norm. This proves the simultaneous if-and-only-if without any symmetry assumption on the added edge set.

**5. Strict pointwise growth, scaling and curvature.** Choose two distinct clique vertices with potentials \(+1\) and \(-1\), and set all other vertex coordinates to zero. Every cross-edge absolute difference is at most one, while the chosen added edge gives \(2s_e\); hence \(s_e>1/2\) strictly increases the lattice element at that evaluation point. Since \(\sqrt{(a+b)/(ab)}>1/\sqrt a\), the constant \(K>1/\sqrt a\), so \(\tau_{a,b}^2>1/2\); pointwise growth with norm equality therefore occurs for all parameters in the specified domain. For fixed \(a\), \(K_{a,b}=\sqrt b+1/\sqrt a+O_a(b^{-1/2})\), yielding the stated fourth-root asymptotic. Finally set \(z=t^2\). The square of the post-threshold norm equals
\[
 G(z)=2(a-1)z+\frac{2azK^2}{2az-(a-1)}.
\]
At \(z=\tau_{a,b}^2\), \(G=B_{a,b}^2\), \(G'=0\), and \(G''=8\sqrt a\,(a-1)/K\). The chain rule gives right second derivative \(16\tau_{a,b}^2\sqrt a\,(a-1)/(KB_{a,b})\), whereas the norm is constant on the left. This proves the differentiability statement.

## Verification

The included `verify_split.py` constructs the full incidence Laplacian on the \((a+b-1)\)-dimensional zero-sum space, rather than relying on the orbit eigenvalue formula when evaluating numerical objective values. It verifies the spectral expression at predicted masses, independently optimizes the orbit mass, runs unrestricted simplex-weight maximizations with explicit matrix-square-root gradients, and checks KKT-style global-support inequalities for the candidate designs. It also tests heterogeneous clique-edge families on both sides of the exact threshold and evaluates high-imbalance asymptotics. Reproduce with `python verify_split.py` in an environment with NumPy and SciPy. A successful local execution reported 58 passed configurations. Numerical tests corroborate the finite-matrix formulas, but the all-parameter theorem, simultaneous necessity/sufficiency, and asymptotic law rest on the proof above.

## Relationship to prior work

Jardón-Sánchez et al. establish existence and the defining norm representation for free 2-convex Banach lattices. The pre-existing exact complete-bipartite norm is the \(t=0\) baseline and is **not claimed as new**. The spectral-design equivalence uses the standard two-summing/Pietsch principle; neither this equivalence nor the general concavity method is claimed as new. Related exact results for three-cluster complete multipartite edge lattices, cyclic chords, hypercube chords, and Johnson schemes concern distinct edge families. Here the object is a complete bipartite graph with a weighted *clique* inserted into one part; the contribution is the full closed two-parameter deformation law, simultaneous nonuniform screening, a sharp amplitude-dependent contact transition, and a fourth-root imbalance law. In related complete-split-graph spectral literature, the graph Laplacian spectrum is studied but the present optimized two-summing invariant was not identified in the sources inspected.

## Limitations

All results are for real exponent two and Euclidean generators. The theorem supplies the optimized norm but not a classification of **all** non-symmetric optimizing probability designs. The numerical verification is finite and cannot substitute for the minimax and concavity arguments. The bibliographic comparison is based on accessible primary material, recorded mathematical claims and targeted searches, not an exhaustive theorem database; an equivalent formulation in less readily indexed operator-ideal or optimal-design literature remains possible. No independent mathematical audit has been performed.

## References

1. H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete and V. G. Troitsky, *Free Banach lattices under convexity conditions*, arXiv:2101.03510, first version January 10, 2021; RACSAM **116** (2022), article 15, DOI: 10.1007/s13398-021-01155-8. The relevant norm formula is equation (1.1) and Section 6.
2. A. Pietsch, *Operator Ideals*, North-Holland, 1980. Standard domination and factorization principle for absolutely summing operators; the finite-dimensional spectral specialization used here is derived in the proof.
3. K. C. Das and M. Liu, *Complete split graph determined by its (signless) Laplacian spectrum*, Discrete Applied Mathematics **205** (2016), 45–51, DOI: 10.1016/j.dam.2016.01.003. Its accessible abstract concerns spectral determination of the graph, not this operator-ideal norm.
