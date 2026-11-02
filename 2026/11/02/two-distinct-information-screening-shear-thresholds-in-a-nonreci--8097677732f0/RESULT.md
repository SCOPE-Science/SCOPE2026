# Two distinct information-screening shear thresholds in a nonreciprocal Brownian trap

## Finding

Consider a three-coordinate nonreciprocal Langevin model with physical positions \(X,Y\) and a hidden coordinate \(Z\). In the entire stationary regime with positive shear, the stationary Gaussian law has two **different, exactly classified** information-screening transitions: one at which \(X\) and \(Z\) are marginally independent, and another at which they are conditionally independent given \(Y\). The transitions never coincide and are separated by universal, parameter-independent inequalities.

Write \(g=\Gamma/a\), \(k=\Omega/a\), with \(a,T,\Omega>0\), and define
\[
 m(k)=\frac{k^2+2}{2k^2+3},\qquad
 h(k)=\frac{8(k^2+2)^2}{5k^4+18k^2+16+(k^2+2)\sqrt{25k^4+64k^2+64}}.
\]
For any positive stable shear \(0<g<2+k^{-2}\),
\[
 X\perp Z\quad\Longleftrightarrow\quad g=m(k),
 \qquad
 X\perp Z\mid Y\quad\Longleftrightarrow\quad g=h(k).
\]
Moreover, for every \(k>0\),
\[
 \frac12<m(k)<\frac23<\frac45<h(k)<1<2+k^{-2}.
\]
Both thresholds decrease strictly as the hidden-coordinate coupling \(k\) grows. Their limits as \(k\downarrow0\) are \(m(k)\to2/3\), \(h(k)\to1\), and as \(k\to\infty\) are \(m(k)\to1/2\), \(h(k)\to4/5\). In particular, screening by conditioning on the observed coordinate \(Y\) cannot be substituted for marginal decoupling in this model.

## Assumptions and scope

Let \((W_1,W_2,W_3)\) be three independent standard Brownian motions, and consider the real-valued stochastic differential equations
\[
\begin{pmatrix}dX_t\\dY_t\\dZ_t\end{pmatrix}=
 \begin{pmatrix}-a&\Gamma&-\Omega\\0&-a&\Omega\\\Omega&-\Omega&-a\end{pmatrix}
 \begin{pmatrix}X_t\\Y_t\\Z_t\end{pmatrix}\,dt
 +\sqrt{2T}\begin{pmatrix}dW_{1,t}\\dW_{2,t}\\dW_{3,t}\end{pmatrix},
\]
where \(a,T,\Omega>0\), \(\Gamma\geq0\). We discuss the unique stationary law, not arbitrary transient Gaussian distributions. The shear \(\Gamma=0\) is a trivial additional marginal and conditional independence point and is excluded from the claim of unique **positive** thresholds. For \(\Gamma/a\geq2+(a/\Omega)^2\), the stationary probability distribution does not exist. All independence assertions refer to the three-dimensional joint stationary law and have ordinary probabilistic meaning; \(X\perp Z\mid Y\) means conditional independence for almost every value of \(Y\).

The drift is the equal-spring-constant, equal-diffusivity, anti-reciprocal hidden-coordinate coupling specialization of Fernandez--Hess--Klapp's shear-driven trapped-colloid model [1]. The primary mathematical classification is in nonequilibrium stochastic dynamics (MSC2020 82C31).

## Proof

**1. Stability and covariance.** Scale time by \(a\), write \(g=\Gamma/a\), \(k=\Omega/a\), and set the dimensionless drift matrix
\[
K=\begin{pmatrix}-1&g&-k\\0&-1&k\\k&-k&-1\end{pmatrix}.
\]
Its characteristic polynomial is
\[
 q(z)=z^3+3z^2+(3+2k^2)z+(1+2k^2-gk^2).
\]
The cubic Routh--Hurwitz inequalities reduce, for \(g\geq0\), to \(1+2k^2-gk^2>0\); the remaining determinant condition is automatic because \(3(3+2k^2)>1+2k^2-gk^2\). Thus \(K\) is Hurwitz precisely when \(0\leq g<2+k^{-2}\). A positive-definite stationary Gaussian covariance exists and is uniquely given by the convergent matrix integral
\[
 \Sigma=\frac{2T}{a}\int_0^\infty e^{Kt}e^{K^{\mathsf T}t}\,dt.
\]
In particular \(\Sigma=(T/a)C\), where \(C\) solves \(KC+CK^{\mathsf T}+2I=0\).

Let
\[
 F=(1+2k^2-gk^2)(8+4k^2+gk^2),\qquad H=8k^4+20k^2+8.
\]
Direct elimination in the six symmetric entries of the Lyapunov equation yields, with indices \(1=X\), \(2=Y\), \(3=Z\),
\[
\begin{aligned}
C_{11}&=\frac{H-g(k^4+5k^2)+g^2(5k^2+4)-g^3k^2}{F},\\
C_{22}&=\frac{H-g(k^4+5k^2)}{F},\\
C_{33}&=\frac{H-g(4k^4+11k^2)+3g^2k^2}{F},\\
C_{12}&=\frac{g(3k^4+8k^2+4-gk^2)}{F},\\
C_{13}&=\frac{gk((2k^2+3)g-(k^2+2))}{F},\\
C_{23}&=\frac{gk(gk^2+k^2+2)}{F}.
\end{aligned}
\]
Here \(F>0\), and the covariance is strictly positive definite for the entire stable domain. These displayed expressions are an explicit solution certificate: substitution into the six independent equations \(KC+CK^{\mathsf T}+2I=0\) verifies every entry; uniqueness follows from the integral representation.

**2. Marginal screening.** A jointly nondegenerate Gaussian pair is independent exactly when its covariance vanishes. Since \(T/a>0\), \(C_{13}=0\) at positive \(g\) if and only if
\[
 (2k^2+3)g-(k^2+2)=0,
\]
which has the single solution \(m(k)=(k^2+2)/(2k^2+3)\). The bounds \(1/2<m(k)<2/3\) follow immediately from \(k>0\). Differentiation with \(v=k^2\) gives \(dm/dv=-1/(2v+3)^2<0\), with the stated endpoint limits.

**3. Conditional screening.** For a positive-definite Gaussian covariance, \(X\perp Z\mid Y\) if and only if the scalar conditional covariance
\[
 \operatorname{Cov}(X,Z\mid Y)=\frac{T}{a}\left(C_{13}-\frac{C_{12}C_{23}}{C_{22}}\right)
\]
vanishes. Exact cancellation of the covariance expressions gives the factorization
\[
 C_{12}C_{23}-C_{13}C_{22}
 =\frac{gk\,B_k(g)}{(1+2k^2-gk^2)(8+4k^2+gk^2)^2},
\]
where
\[
 B_k(g)=k^2g^2-(5k^4+18k^2+16)g+4(k^2+2)^2.
\]
All denominator factors and \(gk\) are strictly positive on the domain, so conditional independence is equivalent to \(B_k(g)=0\). Set \(v=k^2>0\). Direct substitution yields
\[
 B_k(4/5)=\frac{8(7v+10)}{25}>0,\quad
 B_k(1)=-v(v+1)<0,\quad
 B_k(2+v^{-1})=-\frac{3(v+1)(2v^2+5v+5)}{v}<0.
\]
Since \(B_k\) is an upward-opening quadratic in \(g\), it has exactly one root in \((4/5,1)\) and no other root in the physical interval \((0,2+k^{-2})\). The quadratic formula, rationalizing its smaller root, gives precisely \(h(k)\) stated above. This also proves the universal strict separation \(m(k)<2/3<4/5<h(k)\).

To prove monotonicity, write
\[
 B(g,v)=(4-5g)v^2+(g^2-18g+16)v+16(1-g).
\]
For each \(g\in(4/5,1)\), \(B(g,0)>0\) and \(4-5g<0\); therefore, as a quadratic in \(v\), \(B\) has exactly one positive simple root, at which \(\partial_vB<0\). Meanwhile \(\partial_gB=2vg-(5v^2+18v+16)<0\) for \(v>0\), \(g\in(4/5,1)\). Along the root curve, implicit differentiation gives \(h'(v)=-(\partial_vB)/(\partial_gB)<0\). Taking \(v\downarrow0\) and \(v\to\infty\) in this strictly bounded root equation yields \(h\to1\) and \(h\to4/5\), respectively. Neither limiting endpoint is attained for a finite positive \(k\).

**4. A rational witness separating the two notions.** At \(k=1\), \(g=3/5\), \(a=T=1\), exact solution of the Lyapunov system gives
\[
 C_{13}=0,\qquad C_{12}=2/7,\qquad C_{23}=1/14,\qquad C_{22}=15/14.
\]
Consequently \(\operatorname{Cov}(X,Z\mid Y)=-2/105\neq0\), although \(X\perp Z\). Conversely, at \(k=1\) and \(g=h(1)=(39-\sqrt{1377})/2\) conditional covariance is zero while the marginal covariance is nonzero. Both shears lie strictly below the physical stability limit \(g=3\). This establishes genuine separation, not merely two parameterizations of the same independence condition.

## Verification

The included standalone `checker.py` (Python 3 standard library only) separately constructs the exact six-by-six linear system for the stationary covariance and solves it by rational Gaussian elimination, without using the displayed closed covariance formulas. It compares all nine matrix entries against the theorem's formulas at 360 seeded positive-rational parameter choices inside the stable domain; checks the conditional-covariance factorization at those choices; exactly reproduces the rational witness; and tests the universal separation and strict monotonicity on 249 numerical coupling values. A complete successful run prints `PASS: 4103 independent exact-rational, masking and threshold diagnostics`. These are finite diagnostics, not a replacement for the all-parameter symbolic proof above. To reproduce, run `python3 checker.py` in the folder containing the extracted files.

## Relationship to prior work

Fernandez, Hess and Klapp [1] introduce precisely the three-variable nonreciprocal trapped-colloid model, derive its linear moment equations, and calculate the shear-driven loss of stationarity; their Appendix B notes that all stationary second moments can in principle be solved. Their main discussion concerns positional anisotropy, entropy production, and the stationary instability, rather than zero marginal versus conditional correlations involving the hidden state. Thus the present statement is an additional **exact parameter-wide independence classification**, not a new model or an independent derivation of the previously known stability boundary. The general stationary covariance equations of [1] logically permit its recovery by algebraic elimination and a sign analysis; this preexisting structural implication is explicitly acknowledged.

The related many-coordinate analysis by Hess and collaborators [2] concerns general stationary second-moment systems and shear escape, not the simultaneous marginal/conditional screening classification for the special equal-coupling three-coordinate family. Loos and Klapp [3] analyze informational and thermodynamic effects of nonreciprocal coupling more generally, without specifying these two shear thresholds. Standard Gaussian graphical-model identities give the *criteria* for independence and conditional independence; they alone do not give the two noncoincident roots, their unique physical selection, or their strict all-coupling ordering. These comparisons support the limited scientific contribution, subject to the source-coverage risks below.

## Limitations

The theorem is restricted to the equal positive friction and trap rate \(a\), equal isotropic independent thermal noise strengths \(T\), and the specified three-coordinate antisymmetric auxiliary coupling. The findings concern stationary Gaussian independence, not stochastic dynamical decoupling or vanishing physical entropy production. In particular, marginal independence does **not** imply the absence of causal or memory coupling. The singular limit \(k\downarrow0\) is not itself included; at zero hidden coupling the variables decouple by a different degeneracy. For nonstationary supercritical shear the independence criteria are not applicable. The motivating published covariance equations permit, but do not explicitly state, these algebraic consequences; an unindexed supplement or an unrelated stronger Gaussian-network theorem could affect publication priority. No claim of independent audit is made.

## References

[1] Lea Fernandez, Siegfried Hess and Sabine H. L. Klapp, *Nonequilibrium dynamics and entropy production of a trapped colloidal particle in a complex nonreciprocal medium*, arXiv:2402.10579v1 (first submitted 2024-02-16), Phys. Rev. E **109** (2024), 054129; https://arxiv.org/abs/2402.10579 .

[2] Siegfried Hess and collaborators, *Shear-flow-induced distortion of the density distribution and transition from a stationary to an instationary non-equilibrium state of a colloidal particle in a trap*, Atti Accad. Peloritana Pericolanti Cl. Sci. Fis. Mat. Nat. **101** (2023), DOI:10.1478/AAPP.1011A3; https://doi.org/10.1478/AAPP.1011A3 .

[3] Sarah A. M. Loos and Sabine H. L. Klapp, *Irreversibility, heat and information flows induced by non-reciprocal interactions*, arXiv:2008.00894 (2020); https://arxiv.org/abs/2008.00894 .
