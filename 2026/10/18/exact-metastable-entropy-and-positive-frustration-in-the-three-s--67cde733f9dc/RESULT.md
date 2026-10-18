# Exact metastable entropy and positive frustration in the three-state antiferromagnetic Potts prism

## Finding

For every integer \(n\ge3\), let \(G_n=C_n\square K_2\), with two vertices in each of \(n\) cyclically indexed rungs. Equip each vertex with one of three labeled colors and use the antiferromagnetic energy \(H(\sigma)=J\sum_{\{u,v\}\in E(G_n)}\mathbf{1}_{\{\sigma_u=\sigma_v\}}\), where \(J>0\). Call a configuration *weakly one-spin stable* when no recoloring of any one vertex to either other color strictly decreases \(H\). Neutral recolorings are allowed in this definition.

Let \(Z_n\) count these weakly stable configurations. Then the exact integer sequence is obtained by the explicit \(81\)-state transfer matrix below: \(Z_n=\operatorname{tr}(M^n)\). Its unique dominant eigenvalue is the real number \(\alpha=3.6730996940923286\ldots\) in \((3,4)\) satisfying
\[
\alpha^6-4\alpha^5+\alpha^4-\alpha^3+7\alpha^2-2\alpha-1=0.
\]
Consequently, with an absolute implied constant,
\[
Z_n=\alpha^n+O(3^n),\qquad
\lim_{n\to\infty}\frac{\log Z_n}{2n}=\frac{\log\alpha}{2}=0.65051795444237\ldots.
\]

All ground states are proper three-colorings and their exact count is \(G_n=3^n+1+2(-2)^n\). Thus ground states constitute an exponentially vanishing fraction of the weakly stable ensemble, with exponential rate \(\log(\alpha/3)>0\). Among these ground states, the number strictly stable against *every* nontrivial single-site recoloring is exactly \(12\) if \(3\mid n\) and \(0\) otherwise; this last fact is included as a comparison with classical fall-coloring constraints, not asserted to define a new kind of coloring.

If \(\Sigma_n\) is uniform on the weakly stable ensemble, then
\[
\frac{H(\Sigma_n)}{Jn}\xrightarrow{\mathbb P}\mu,
\qquad \mu=0.21744173751868\ldots>0.
\]
More precisely, \(\mu\) is specified exactly by the Perron eigenvectors of a finite matrix in the proof. Hence a typical weak local minimum has a positive extensive energy excess even though zero-energy proper colorings exist for every \(n\).

## Assumptions and scope

The graph has \(2n\) labeled vertices, edges along each row between consecutive columns modulo \(n\), and one transverse edge in each column. For \(n=3\), each row is the simple triangle, and no edge is counted twice. Each configuration uses labeled colors \(\{0,1,2\}\), and the energy counts monochromatic graph edges in units of \(J\). Stability refers to *strictly energy-decreasing one-vertex recolorings*; it does not forbid equal-energy moves and does not describe a distribution produced by a quench.

A rung is \(b=(b_0,b_1)\in\{0,1,2\}^2\). For rungs \(a,b,c\), set \(I(a,b,c)=1\) exactly when, for each row \(r\in\{0,1\}\), the occurrence count of \(b_r\) in the neighbor multiset \((a_r,c_r,b_{1-r})\) is no larger than either other color's count. Otherwise set \(I=0\). This is the precise weak-stability criterion because a recoloring changes the monochromatic-edge count by the new color's neighbor multiplicity minus the old color's multiplicity.

## Proof

**1. Exact finite-state representation.** Index \(81\) states by ordered pairs \((a,b)\) of the nine possible rungs. Define
\[
M_{(a,b),(u,c)}=\mathbf1_{\{u=b\}}I(a,b,c).
\]
A closed length-\(n\) walk corresponds bijectively to the cyclic succession of rung pairs in one labeled \(n\)-column configuration. Every permitted transition verifies weak stability of the central rung, and every rung is checked once. Therefore \(Z_n=\operatorname{tr}(M^n)\), with no boundary or rotation quotient.

**2. Exact characteristic polynomial and dominant eigenvalue.** Computing the determinant of the explicitly defined integer matrix by exact polynomial arithmetic gives
\[
\begin{aligned}
\det(xI-M)={}&x^{27}(x-1)^2(x+1)^2(x^2-x-1)(x^2+x+1)^3\\
&\cdot(x^6+x^4+x^3-x^2+1)\\
&\cdot(x^6-4x^5+x^4-x^3+7x^2-2x-1)\\
&\cdot(x^7-2x^5+x^4-3x^3+x^2-x+1)^2\\
&\cdot(x^8+x^7+2x^6+5x^5-2x^4+6x^2-2x+1)^2.
\end{aligned}
\]
These factors are finite, exact-arithmetic identities, reconstructed directly from the matrix in the included verification program; they are not inferred from numerical roots.

On the circle \(|x|=3\), the absolute value of the term \(-4x^5\) in the distinguished sextic is \(4\cdot3^5=972\), which exceeds the sum of the absolute values of all the remaining terms, bounded by \(907\). Rouché's theorem therefore places five sextic roots strictly inside \(|x|<3\) and one outside. The sextic is negative at \(x=3\) and positive at \(x=4\), so that remaining root is the real \(\alpha\in(3,4)\). Every other displayed factor has all roots strictly within \(|x|<3\): for the remaining sextic the leading-term bound is \(729>118\), for the septic \(2187>661\), and for the octic \(6561>5083\); the quadratic and linear factors are immediate. Thus \(\alpha\) is the only eigenvalue of modulus greater than three and is simple. The trace formula gives \(Z_n=\alpha^n+O(3^n)\); dividing its logarithm by the \(2n\) spins gives the entropy result.

**3. Ground-state and strict-stability comparison.** Zero energy is equivalent to a proper coloring of \(G_n\). Proper rungs must have distinct row colors. Their six-state adjacency transfer allows a successor rung when both horizontal edges are bichromatic. Its exactly calculated characteristic polynomial is \(x^2(x-3)(x-1)(x+2)^2\), hence its closed-walk trace is \(G_n=3^n+1+2(-2)^n\). A proper coloring is strictly stable precisely when each vertex sees at least one neighbor in *each* of the two colors other than its own. On the \(18\) possible adjacent proper-rung pairs, use the same pair-memory construction, now requiring this two-color condition at each central rung. Its exact characteristic polynomial is \(x^6(x-1)^4(x^2+x+1)^4\). Its trace is \(4+4\bigl(\omega^n+\bar\omega^n\bigr)\), where \(\omega\) is a primitive cube root of unity, giving \(12\) for multiples of three and zero otherwise. Since \(\alpha>3\), the ground-state fraction has exponential decay as stated.

**4. Energy concentration.** For every permitted transition \((a,b)\to(b,c)\), give it weight
\[
e(b,c)=\mathbf1_{\{b_0=b_1\}}+\mathbf1_{\{b_0=c_0\}}+\mathbf1_{\{b_1=c_1\}}.
\]
The total transition weight around a closed walk equals \(H/J\). Define \(M(z)_{(a,b),(b,c)}=I(a,b,c)z^{e(b,c)}\), zero elsewhere. It follows for every positive \(z\) that \(Z_n(z)=\operatorname{tr}(M(z)^n)=\sum_{\sigma\;\mathrm{weak}} z^{H(\sigma)/J}\).

The directed support of \(M(1)\) has one largest strongly connected component with \(48\) states; it is strongly connected and aperiodic (closed walks of lengths four and five exist). The other nontrivial components have three vertices each. The exact root bounds in step 2 make the Perron eigenvalue of this \(48\)-state component isolated and strictly dominant. Let \(B(z)\) be the restriction of \(M(z)\) to this component and \(l,r\) respectively strictly positive left and right eigenvectors of \(B(1)\) for \(\alpha\). Put \(D=B'(1)\). The exact number
\[
\mu=\frac{l^{\mathsf T}Dr}{\alpha\,l^{\mathsf T}r}
\]
is independent of eigenvector normalization and has the numerical value reported above. The component has at least one positive-energy transition, so \(D\ne0\) and the strict positivity of \(l,r\) proves \(\mu>0\).

Analytic perturbation of the simple isolated eigenvalue gives a positive analytic function \(\lambda(t)\) near \(t=0\), with \(\lambda(0)=\alpha\) and derivative \(\lambda'(0)=\alpha\mu\), for the weighted transfer \(B(e^t)\). Spectral separation yields
\[
\mathbb E[e^{tH/(J)}]=\frac{Z_n(e^t)}{Z_n(1)}
=\left(\frac{\lambda(t)}{\alpha}\right)^n\bigl(1+O(\eta^n)\bigr)
\]
uniformly in a sufficiently small complex neighborhood of zero, for some \(0<\eta<1\). Differentiation of the cumulant generating function shows \(\mathbb E[H/J]=n\mu+O(1)\) and \(\operatorname{Var}(H/J)=O(n)\). Chebyshev's inequality proves the claimed convergence in probability.

## Verification

Run \(\texttt{python3 artifacts/verify.py}\) after installing the packages listed in \(\texttt{artifacts/requirements.txt}\). The script constructs the original transfer matrix from the stated local neighbor rule and computes its \(81\)-degree characteristic polynomial using exact rational/integer arithmetic. It checks the \(48\)-state component, the proper-coloring and strictly stable transfer polynomials, and compares complete physical configuration enumeration for \(n=3,4,5,6\) (respectively \(36,294,660,2496\) weak minima) with transfer-matrix counts and the total energy sum. It also checks the numerical Perron root and energy density. The analytic root bounds, spectral asymptotics, and concentration argument above constitute the proof for all lengths; small finite tests are checks, not substitutes for those arguments.

## Relationship to prior work

Exact equilibrium partition functions, chromatic polynomials, and antiferromagnetic Potts ground-state entropies on cyclic ladders are established in Shrock's ladder work and related chromatic-polynomial studies. Those equilibrium objects count configurations using Boltzmann weights or proper colorings, whereas the present transfer imposes a *one-spin local optimality constraint*; its entropy base exceeds the proper-coloring base \(3\). The definition of strict stable proper colorings is connected to previously studied fall-coloring constraints and is not itself claimed novel. Studies of zero-temperature Potts coarsening concern dynamic trapping and frequently ferromagnetic couplings rather than the uniform weak-minima census of this antiferromagnetic prism. The claimed addition is the exact metastable transfer spectrum, dominant sextic entropy law, and positive typical excess energy for this particular natural family.

## Limitations

Only exactly three labeled spin colors, the uniform antiferromagnetic nearest-neighbor coupling, and cyclic two-row prisms of \(n\ge3\) are treated. One-spin local minima can move by neutral recolorings and need not be absorbing under a dynamics that accepts equal-energy changes. Uniform sampling of weak minima is not the outcome distribution of zero-temperature quenches. The energy-density approximation is numerical evaluation of an exact Perron-eigenvector expression. A possible equivalent computation in less accessible finite-width metastability literature has not been eliminated, and independent expert audit remains outstanding.

## References

1. R. Shrock, “Exact Potts Model Partition Functions on Ladder Graphs,” arXiv:cond-mat/0001389v1 (first posted 2000-01-26). https://arxiv.org/abs/cond-mat/0001389
2. R. Shrock and S.-H. Tsai, “Ground State Entropy of the Potts Antiferromagnet on Cyclic Strip Graphs,” arXiv:cond-mat/9903233 (1999). https://arxiv.org/abs/cond-mat/9903233
3. J. Olejarz, P. L. Krapivsky and S. Redner, “Zero-Temperature Coarsening in the 2d Potts Model,” arXiv:1305.1038 (2013). https://arxiv.org/abs/1305.1038
4. A. Silva, “Fall-colorings and b-colorings of graph products,” arXiv:1607.08453 (2016). https://arxiv.org/abs/1607.08453
