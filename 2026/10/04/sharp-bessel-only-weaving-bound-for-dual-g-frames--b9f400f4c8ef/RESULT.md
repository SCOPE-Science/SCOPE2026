# Sharp Bessel-only weaving bound for dual g-frames
## Finding
Let \(\Lambda=\{\Lambda_j\}_{j\in J}\) and \(\Gamma=\{\Gamma_j\}_{j\in J}\) be dual g-frames on a Hilbert space \(\mathcal U\), with respect to Hilbert spaces \(\{\mathcal V_j\}_{j\in J}\). Assume \(B_\Lambda\) and \(B_\Gamma\) are valid Bessel upper bounds, so
\[
\sum_{j\in J}\|\Lambda_j f\|^2\le B_\Lambda\|f\|^2,
\qquad
\sum_{j\in J}\|\Gamma_j f\|^2\le B_\Gamma\|f\|^2.
\]
Put \(S=B_\Lambda+B_\Gamma\). For every subset \(\sigma\subset J\), the mixed family \(\{\Lambda_j:j\in\sigma\}\cup\{\Gamma_j:j\notin\sigma\}\) has lower g-frame bound
\[
A_*(B_\Lambda,B_\Gamma)=\frac{S-\sqrt{S^2-4}}2.
\]
This constant is optimal if the only numerical information retained about the dual pair is the two Bessel upper bounds: for every \(B_\Lambda,B_\Gamma>0\) satisfying \(B_\Lambda B_\Gamma\ge1\), a real one-dimensional two-index dual pair with these exact bounds has a weave attaining \(A_*(B_\Lambda,B_\Gamma)\).

## Assumptions and scope
Duality means
\[
f=\sum_{j\in J}\Lambda_j^*\Gamma_j f
\]
for every \(f\in\mathcal U\), with the usual Bessel convergence. The result applies to finite or countable index sets and to real or complex Hilbert spaces. The sharp examples are real and one-dimensional. The phrase “optimal” refers to a universal guarantee determined only by the announced upper bounds \(B_\Lambda\) and \(B_\Gamma\); a particular dual pair may have a larger actual universal weaving bound.

Duality itself implies \(B_\Lambda B_\Gamma\ge1\). Indeed, for nonzero \(f\), Cauchy-Schwarz gives
\[
\|f\|^2
=\left|\sum_{j\in J}\langle\Gamma_jf,\Lambda_jf\rangle\right|
\le\sqrt{B_\Gamma B_\Lambda}\,\|f\|^2.
\]
Thus \(S\ge2\), so the displayed square root is real.

## Proof
Fix \(f\) with \(\|f\|=1\) and a subset \(\sigma\subset J\). Define
\[
x=\sum_{j\in\sigma}\|\Lambda_jf\|^2,
\quad y=\sum_{j\notin\sigma}\|\Gamma_jf\|^2,
\]
\[
u=\sum_{j\in\sigma}\|\Gamma_jf\|^2,
\quad v=\sum_{j\notin\sigma}\|\Lambda_jf\|^2.
\]
The mixed weaving energy is \(E=x+y\). Splitting the dual reconstruction pairing over \(\sigma\) and its complement yields
\[
1\le \sqrt{xu}+\sqrt{yv}.
\]
The Bessel bounds give \(u\le B_\Gamma-y\) and \(v\le B_\Lambda-x\). Hence
\[
1\le
\sqrt{x(B_\Gamma-y)}+\sqrt{y(B_\Lambda-x)}.
\]
A second Cauchy-Schwarz inequality gives
\[
1\le\sqrt{(x+y)(B_\Gamma-y+B_\Lambda-x)}
=\sqrt{E(S-E)}.
\]
Therefore \(E(S-E)\ge1\). Since \(0\le E\le S\) and \(S\ge2\), \(E\) lies between the two roots of \(t(S-t)=1\). Consequently
\[
E\ge\frac{S-\sqrt{S^2-4}}2=A_*(B_\Lambda,B_\Gamma).
\]
Homogeneity restores the factor \(\|f\|^2\), proving the lower g-frame inequality for every weave.

It remains to prove sharpness. Write \(L=B_\Lambda\) and \(G=B_\Gamma\), with \(LG\ge1\). Choose vectors \(\lambda,\gamma\in\mathbb R^2\) satisfying
\[
\|\lambda\|^2=L,
\qquad
\|\gamma\|^2=G,
\qquad
\lambda\cdot\gamma=1.
\]
Such vectors exist exactly because \(LG\ge1\). Let \(J\) denote rotation by ninety degrees and set
\[
M=\lambda\lambda^{\mathsf T}+(J\gamma)(J\gamma)^{\mathsf T}.
\]
Then \(\operatorname{tr}M=L+G=S\), while
\[
\det M=\det[\lambda,J\gamma]^2=(\lambda\cdot\gamma)^2=1.
\]
Thus the eigenvalues of \(M\) are the two roots of \(t^2-St+1=0\), and its smaller eigenvalue is \(A_*(L,G)\). Choose a unit eigenvector \(w\) for that eigenvalue and use \((w,Jw)\) as the coordinate basis of the two-element index space. In these coordinates, write \(\lambda'\) and \(\gamma'\) for the same two vectors. They satisfy
\[
\|\lambda'\|^2=L,
\qquad
\|\gamma'\|^2=G,
\qquad
\lambda'\cdot\gamma'=1.
\]
Hence, on the one-dimensional Hilbert space \(\mathbb R\), the scalar analysis maps \(\Lambda_j f=\lambda'_j f\) and \(\Gamma_j f=\gamma'_j f\) form a dual pair with exact Bessel bounds \(L\) and \(G\). For the weave selecting \(\Lambda_1\) and \(\Gamma_2\), its energy at \(f=1\) is
\[
|\lambda'_1|^2+|\gamma'_2|^2
=w^{\mathsf T}Mw
=A_*(L,G).
\]
No larger bound depending only on \(L\) and \(G\) can therefore hold universally.

Finally,
\[
A_*(B_\Lambda,B_\Gamma)
=\frac{2}{S+\sqrt{S^2-4}
>\frac1{2\max\{B_\Lambda,B_\Gamma\}},
\]
because \(S+\sqrt{S^2-4}<2S\le4\max\{B_\Lambda,B_\Gamma\}\). Thus the improvement over the previously stated bound is strict for every admissible finite pair of Bessel bounds.

## Verification
The proof was checked independently at the level of its quantifiers and boundary cases. The infinite-index case uses only convergent Bessel sums and Cauchy-Schwarz. The boundary \(B_\Lambda B_\Gamma=1\) is included. When \(S=2\), necessarily \(B_\Lambda=B_\Gamma=1\) and the formula gives the exact lower bound \(1\). The sharpness construction preserves the norms and duality pairing under the common orthogonal change of coordinates, and the determinant identity gives the claimed extremal eigenvalue without numerical approximation.

## Relationship to prior work
Xiao, Zhao and Zhou state in Corollary 5.2 that a g-frame and any dual g-frame are woven with universal lower bound \(1/(2\max\{B_\Lambda,B_\Gamma\})\) and upper bound \(B_\Lambda+B_\Gamma\). They identify this as the earlier dual-weaving theorem of Deepshikha and Samanta. The present result keeps exactly the same hypotheses but replaces the lower bound by the best possible guarantee obtainable from \(B_\Lambda\) and \(B_\Gamma\) alone.

Earlier work on frame duality and weaving gives sufficient conditions for canonical, alternate, or approximate duals, rather than this sharp two-parameter universal constant. A 2025 paper on operator-valued weaving states at abstract level that it estimates optimal universal bounds and proves an operator-valued frame is woven with its dual. Its theorem body was not materially available for comparison; no accessible statement located there gives the Bessel-only formula proved here. This remains the principal literature risk.

## Limitations
The theorem does not compute the exact universal weaving bound of a fixed dual pair from its full geometry; it determines the sharp worst-case lower guarantee from the two Bessel bounds alone. It does not address the more general \(K\)-g-frame setting where reconstruction and the lower norm are modified by an operator. The unresolved literature risk is a potentially equivalent sharp formula in material not available for full-text comparison, especially the 2025 operator-valued weaving paper.

## References
X. Xiao, G. Zhao and G. Zhou, “Redundancy, weaving and Q-dual of K-g-frames in Hilbert spaces,” Hacettepe Journal of Mathematics and Statistics 53 (2024), 595-607, DOI 10.15672/hujms.1130102.

Deepshikha and A. Samanta, “On Weaving Generalized Frames and Generalized Riesz Bases,” Bulletin of the Malaysian Mathematical Sciences Society 45, 361-378, DOI 10.1007/s40840-021-01193-w; preprint arXiv:2001.09432.

F. Arabyani Neyshaburi and A. A. Arefijamaal, “Weaving Hilbert Space Frames and Duality,” preprint arXiv:1909.08835.

Y.-N. Li, Y.-Z. Li and Z.-C. Yan, “On weaving operator-valued frames,” International Journal of Wavelets, Multiresolution and Information Processing 23 (2025), article 2550006, DOI 10.1142/S0219691325500067.
