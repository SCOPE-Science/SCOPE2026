# Universal moment law for the first Lu Qi-Keng zero created by concentrated radial mass

## Finding

The zero-free property of the ordinary disk Bergman kernel has a sharp, profile-uniform transition under a small radial concentration of additional positive mass. The threshold tends to one third of the background disk's area, and its first two corrections depend only on the concentrated mass's second and fourth radial moments.

**Theorem.** Fix any real \(M>1/3\). There is \(\rho_M>0\) such that the following holds for every \(0<\rho<\rho_M\) and every rotation-invariant Borel probability measure \(\nu\) supported in \(\{z\in\mathbb C:|z|\le\rho\}\). For each \(0\le\kappa\le M\), equip analytic functions on the open unit disk \(\mathbb D\) with the norm
\[
\|f\|_{\kappa,\nu}^2=\int_{\mathbb D}|f(z)|^2\,dA(z)+\pi\kappa\int |f(z)|^2\,d\nu(z),
\]
where \(dA\) is ordinary planar area measure. Let \(K_{\kappa,\nu}(z,w)\) be its Bergman reproducing kernel. There is a unique critical value \(\kappa_c(\nu)\) near \(1/3\), such that:

1. For \(0\le\kappa\le\kappa_c(\nu)\), \(K_{\kappa,\nu}\) is zero-free on \(\mathbb D\times\mathbb D\).
2. For \(\kappa_c(\nu)<\kappa\le M\), its scalar kernel as a function of \(t=z\overline w\) has exactly one zero in \(|t|<1\), counted with multiplicity. That zero is simple and lies on \((-1,0)\). Thus every kernel zero is realized by an antipodal-product pair, and no other product-zero fibres occur.
3. At the transition, the unique scalar boundary zero is \(t=-1\); it crosses transversely into the open disk, with derivative \(dt/d\kappa=9/4+O_M(\rho^2)\).

Writing \(m_1=\int |z|^2\,d\nu\) and \(m_2=\int |z|^4\,d\nu\), the critical value has the uniform expansion
\[
\boxed{\displaystyle
\kappa_c(\nu)=\frac13+\frac{64}{27}m_1+\frac{4736}{243}m_1^2-\frac{16}{3}m_2+O_M(\rho^6).}
\]
Here uniform means that the implied constant depends only on \(M\), not on the radial profile. This is a complete zero/no-zero classification throughout every fixed bounded mass interval \([0,M]\), for sufficiently small support radius; it is not asserted uniformly as \(M\to\infty\).

For the ordinary two-level radial weight
\[
w_{\rho,\kappa}(z)=1+\frac\kappa{\rho^2}\mathbf1_{\{|z|<\rho\}},
\]
the concentrated probability measure is uniform on the disk of radius \(\rho\), and
\[
\boxed{\displaystyle
\kappa_c(\rho)=\frac13+\frac{32}{27}\rho^2+\frac{752}{243}\rho^4+O_M(\rho^6).}
\]
Consequently the jump height at the exact onset is \(\kappa_c(\rho)/\rho^2=1/(3\rho^2)+32/27+(752/243)\rho^2+O_M(\rho^4)\).

## Assumptions and scope

The reference space is the analytic square-integrable Bergman space on \(\mathbb D\). The extra measure may be singular or absolutely continuous, but must be positive, radial, have total probability one, and be supported within radius \(\rho\). The radial measure is fixed as \(\kappa\) varies. All conclusions count zeros in the **scalar complex variable** \(t=z\overline w\); many point pairs can represent the same scalar zero. Every \(|t|<1\) is representable by two points of \(\mathbb D\), so scalar zero-freeness is equivalent to kernel zero-freeness. The value \(t=-1\) is on the boundary and is not represented by an interior point pair.

The support condition implies \(0\le m_n:=\int|z|^{2n}\,d\nu\le\rho^{2n}\) and \(m_0=1\). The result applies to every such radial probability distribution, including thin concentric circles, smooth bumps, and the two-level weight above. The prior mass parameter \(\kappa\) is dimensionless: the added measure has total mass \(\pi\kappa\) relative to a background disk of area \(\pi\).

## Proof

**Step 1: exact kernel coefficients.** Rotation invariance makes the monomials orthogonal. Directly,
\[
\|z^n\|_{\kappa,\nu}^2=\frac\pi{n+1}+\pi\kappa m_n,
\qquad n=0,1,2,\ldots.
\]
Hence
\[
\pi K_{\kappa,\nu}(z,w)=\mathcal K_{\kappa,\nu}(t)
=\sum_{n=0}^\infty\frac{n+1}{1+\kappa(n+1)m_n}t^n,
\qquad t=z\overline w.
\]
The series is analytic for \(|t|<1\) and, after subtraction of the classical rational Bergman kernel, has an analytic remainder on \(|t|<\rho^{-2}\).

**Step 2: uniform perturbation of the point-mass model.** Set \(c_\kappa=\kappa/(1+\kappa)\). Extracting the \(n=0\) coefficient gives
\[
\mathcal K_{\kappa,\nu}(t)=\frac1{(1-t)^2}-c_\kappa+E_{\kappa,\nu}(t),
\]
where
\[
E_{\kappa,\nu}(t)=-\sum_{n=1}^\infty
\frac{\kappa(n+1)^2m_n}{1+\kappa(n+1)m_n}\,t^n.
\]
For \(0\le\kappa\le M\), \(m_n\le\rho^{2n}\) implies that the remainder and its first derivatives in \(t\) and \(\kappa\) are uniformly \(O_M(\rho^2)\) on any fixed disk \(|t|\le1+\eta\), provided \(\rho\) is small enough. Indeed, their terms are bounded by constant multiples of \((n+1)^3\rho^{2n}(1+\eta)^n\). This also justifies differentiation under the sum and all analytic continuations used below.

Multiplying by \((1-t)^2\) defines a holomorphic function across \(t=1\):
\[
G_{\kappa,\nu}(t)=(1-t)^2\mathcal K_{\kappa,\nu}(t)
=1-c_\kappa(1-t)^2+(1-t)^2E_{\kappa,\nu}(t).
\]
For \(|t|<1\), multiplication neither creates nor removes zeros. Its limiting polynomial is
\[
G_{\kappa,0}(t)=1-c_\kappa(1-t)^2.
\]
For \(\kappa>0\), the two polynomial zeros are \(t_\pm=1\pm\sqrt{(1+\kappa)/\kappa}\). The positive one exceeds \(2\). The negative one enters \(|t|<1\) exactly when \(\kappa>1/3\), meeting the unit circle at \(t=-1\) when \(\kappa=1/3\). At \(\kappa=0\), \(G_{0,0}=1\).

**Step 3: a single transverse zero crossing and global completeness.** Choose a sufficiently small closed disk centered at \(-1\), and a fixed small interval about \(1/3\). The polynomial family has exactly one simple zero in that disk, and its other zero is far outside the closed unit disk. Uniform holomorphic convergence and Rouché's theorem give exactly one perturbed zero in the chosen disk. Because the Taylor coefficients are real, the disk is conjugation-invariant, and that zero is unique, the perturbed zero is real. The holomorphic implicit-function theorem makes it a continuously differentiable function \(t_\nu(\kappa)\) of the real mass parameter. At the limiting point,
\[
\partial_tG_{1/3,0}(-1)=1,
\qquad\partial_\kappa G_{1/3,0}(-1)=-\frac94,
\]
so \(t_\nu'(\kappa)=9/4+O_M(\rho^2)>0\) near the crossing. It follows that the equation \(t_\nu(\kappa)=-1\) has a unique solution \(\kappa_c(\nu)=1/3+O_M(\rho^2)\). On the high-mass side the zero lies in \((-1,0)\), while on the low-mass side it lies to the left of \(-1\).

No further zeros can arise: on the compact subset of the closed unit disk outside that small neighborhood of \(-1\), the limiting family is uniformly separated from zero for masses near \(1/3\); for the remaining masses in the fixed interval \([0,M]\), Rouché's theorem on the unit circle preserves the reference zero count. All these separation and perturbation estimates are uniform in the radial profile since they use only \(m_n\le\rho^{2n}\). The simple scalar zero remains negative throughout the supercritical interval by conjugation symmetry and continuous perturbation of the negative reference zero. At \(\kappa=\kappa_c\), its location \(t=-1\) is not an interior kernel zero.

**Step 4: the universal moment expansion.** Evaluate the kernel at the negative boundary point, using the rational part for Abel continuation and the absolutely convergent remainder. Expanding the \(n=1\) and \(n=2\) coefficients, with all \(n\ge3\) controlled by \(m_n\le\rho^{2n}\), gives uniformly for \(0\le\kappa\le M\)
\[
\mathcal K_{\kappa,\nu}(-1)
=\frac14-\frac\kappa{1+\kappa}
+4\kappa m_1-8\kappa^2m_1^2-9\kappa m_2+O_M(\rho^6).
\]
The same uniform bound holds for its \(\kappa\)-derivative. At the critical mass, this expression vanishes. Inserting \(\kappa=1/3+A m_1+B m_1^2+C m_2+O_M(\rho^6)\), and comparing coefficients through radial order four, yields
\[
A=\frac{64}{27},\qquad B=\frac{4736}{243},\qquad C=-\frac{16}{3}.
\]
The derivative of the leading scalar equation at \(\kappa=1/3\) is \(-9/16\ne0\), so the remainder is rigorously \(O_M(\rho^6)\) by the implicit-function theorem and the preceding uniform estimates. For the uniform disk of radius \(\rho\), its radial moments are \(m_1=\rho^2/2\), \(m_2=\rho^4/3\), giving the stated two-level-weight expansion.

## Verification

The companion standalone Python script `checker.py` uses symbolic coefficient matching for the order-four expansion, independent radial integrals for five monomial norms, and high-precision scalar-kernel computations for three radial profiles: uniform disk, radially increasing density, and a uniform circular measure. At three small radii for each profile it solves \(\mathcal K_{\kappa,\nu}(-1)=0\), compares with the second-order moment formula, and checks a simple interior negative zero above the computed transition. Its output is included separately. These finite calculations are consistency tests and do not substitute for the global Rouché and implicit-function arguments.

## Relationship to prior work

Zeytuncu (2010, Section 2) proved existence of a zero for a specific two-level radial disk weight and remarked that other radial jump weights and smooth radial approximations can also exhibit zeros. The present theorem classifies the entire zero count on every bounded added-mass range once the bump is sufficiently concentrated, gives the universal sharp critical mass, and computes the profile-dependent order-four correction. Its point-mass limit is a standard rank-one kernel perturbation and is not claimed as new.

Boas (2000, Sections 6–7) discussed weighted-kernel zero phenomena and concrete parameter thresholds for boundary-distance weights; those weights do not concentrate their added mass at the disk center. Perälä (2017, Section 3) gave constructions of radial weights with prescribed finite numbers of zeros, not the present small-support threshold and moment law. Published studies of Euclidean boundary-distance power weights and of radial power-deficit weights concern different families and do not imply this mass-concentration classification.

## Limitations

The theorem is asymptotic as the added radial mass is concentrated, with the allowable radius depending on an arbitrary but fixed upper mass bound \(M\). It makes no claim for arbitrary large mass at a fixed radius, for nonradial concentrations, or for the complete zero geometry of unrelated weighted Bergman spaces. It does not claim the universal \(O_M(\rho^6)\) remainder has an optimal constant. The profile-independent coefficients arise from perturbing a known rank-one limit, so publication priority for the full combined classification still requires independent historical review, especially among older kernel-variation papers.

## References

1. Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: \(L^p\) Regularity and Zeros*, arXiv:1009.2806v1, initially public 2010-09-14, especially Section 2. https://arxiv.org/pdf/1009.2806
2. A. Perälä, *Vanishing Bergman Kernels on the Disk*, arXiv:1703.05976v1, initially public 2017-03-17, especially Section 3. https://arxiv.org/pdf/1703.05976
3. H. P. Boas, *Lu Qi-Keng's problem*, Journal of the Korean Mathematical Society 37 (2000), 253–267, especially Sections 6–7. https://haroldpboas.gitlab.io/preprints/zeroes-survey.pdf
