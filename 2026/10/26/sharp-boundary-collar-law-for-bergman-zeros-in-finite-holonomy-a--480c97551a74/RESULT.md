# Sharp boundary-collar law for Bergman zeros in finite-holonomy annulus bundles

## Finding
Let \(E=\mathbb C/(\mathbb Z+i\mathbb Z)\), \(X=E\setminus\{[0]\}\), and let \(H\) be the square-lattice holomorphic function with \(H(t+1)=H(t)\) and \(H(t+i)=H(t)-2\pi i\) used in [1]. Put \(\psi=\operatorname{Re}H\), \(L=\log 2\), and, for each real \(a\),
\[
 B_a=\{(x,u)\in X\times\mathbb C^*:1<|u|e^{a\psi(x)}<2\}.
\]
This is a connected pseudoconvex Stein domain, and the fixed Runge embedding of \(X\times\mathbb C\) from [1] realizes every \(B_a\) as a pseudoconvex domain \(\Omega_a\subset\mathbb C^2\). All conclusions concern the canonical Bergman kernel (equivalently, the ordinary Bergman kernel of \(\Omega_a\) under the embedding).

**Theorem.** The Bergman kernel is zero-free on \(\Omega_a\times\Omega_a\) if and only if \(a\) is irrational. If \(a=p/q\) in lowest terms, \(q\ge1\), there are exactly \(2q\) scalar off-diagonal zero fibres, all simple, in the global product variable \(\eta=v(P)\overline{v(Q)}\), where locally \(v=e^{aH(t)}u\). Their angles are exactly \(\arg\eta=(2j+1)\pi/q\), \(0\le j<q\), on each of two concentric circles, with radii \(r_{q,-}\in(1,2)\) and \(r_{q,+}\in(2,4)\) satisfying \(r_{q,-}r_{q,+}=4\). Here a fibre means a possible scalar value of \(\eta\); it is **not** a count of zeros of the kernel for each fixed second point. Different lift choices permute the listed fibres, but their union is well defined.

The new asymptotic location statement is as follows. With \(S=\eta^q\), write the two negative real zeros of the scalar kernel as \(S_{q,-}\in(-2^q,-1)\) and \(S_{q,+}=4^q/S_{q,-}\in(-4^q,-2^q)\). Then, as positive integers \(q\to\infty\),
\[
 S_{q,-}=-2q\log 2+2+O(q^{-1}),\qquad S_{q,+}=4^q/S_{q,-}.
\]
In particular, the two escaping zero circles obey the **sharp logarithmic boundary-collar laws**
\[
 q\log r_{q,-}-\log q\longrightarrow\log(2\log2),\qquad
 q\log(4/r_{q,+})-\log q\longrightarrow\log(2\log2).
\]
Thus the zero locus leaves every fixed compact region of possible product values as finite holonomy orders increase, but approaches both boundary circles at logarithmic-over-linear radial depth. This location asymptotic, rather than the classical two-zero theorem on an annulus, is the distinct quantitative conclusion.

## Assumptions and scope
The base is the punctured square elliptic curve; \(H\) is fixed as in [1], and the bundle parameter is real. For rational \(a\), \(q\) always denotes its positive reduced denominator. The kernel is interpreted as a section of the external tensor product of canonical bundles. Because \(\beta_0=dt\wedge du/u\) is a global nowhere-vanishing holomorphic canonical form, its scalar coefficient determines zeros without a choice of coordinate Jacobian. The local annular variable \(v=e^{aH(t)}u\) is changed by a unit scalar on changing lifts, and \(S=(v(P)\overline{v(Q)})^q\) is globally defined for \(a=p/q\). Its attainable range on pairs of points is the complete annulus \(1<|S|<4^q\).

## Proof
**Step 1: canonical Fourier decomposition.** Lift \(B_a\) to \((\mathbb C\setminus\Lambda)\times\{1<|v|<2\}\), with \(v=e^{aH(t)}u\). A holomorphic square-integrable canonical form has an expansion \(\beta_0\sum_{k\in\mathbb Z}c_k(t)v^k\). Orthogonality of annular monomials and Fubini show that each \(c_k\) extends across the lattice punctures by the removable singularity theorem for square-integrable holomorphic functions. The quasiperiodicity relations are \(c_k(t+1)=c_k(t)\) and \(c_k(t+i)=e^{2\pi iak}c_k(t)\). Their absolute values are lattice-periodic, so the entire \(c_k\) are bounded and constant. Such a constant is nonzero only if \(ak\in\mathbb Z\). Therefore the only Laurent degree is zero for irrational \(a\), whereas for \(a=p/q\) precisely the degrees \(k=q\ell\), \(\ell\in\mathbb Z\), occur. The irrational kernel is a nonzero constant times \(\beta_0(P)\overline{\beta_0(Q)}\), hence zero-free. This decomposition and the diagonal norm formula already occur in earlier work [1,3]; they are input, not a novelty claim.

**Step 2: reduction to the classical annulus.** Relative to \(\beta_0(P)\overline{\beta_0(Q)}\), and up to the nonzero factor \(1/(2\pi)\), the rational kernel is the function
\[
 F_q(S)=\frac1L+\sum_{m=1}^\infty\frac{2qm}{1-4^{-qm}}\left[\left(\frac{S}{4^q}\right)^m+S^{-m}\right],
 \qquad 1<|S|<4^q.
\]
The series and all derivatives converge normally on compact subsets. Indeed \(\|\beta_0v^k\|^2=2\pi I_k\), with \(I_0=L\) and \(I_k=(2^{2k}-1)/(2k)\) for nonzero integers \(k\).

Consider the ordinary annulus \(A_q=\{1<|V|<2^q\}\). Its canonical Bergman kernel, expressed relative to \(dV/V\), has scalar coefficient \(F_q(V\overline W)/q\), up to the same nonzero angular factor, because its Laurent norm is \(2\pi q I_{q\ell}\). Consequently its scalar zero set is **identical** to that of \(F_q\). The classical annulus zero-location theorem [2, Section 2] says that this function has exactly two simple negative-real scalar zeros, one on either side of \(-2^q\), and no others in the product annulus. Its inversion symmetry \(F_q(S)=F_q(4^q/S)\) then gives \(S_{q,+}S_{q,-}=4^q\). Taking each \(q\)-th root gives exactly \(2q\) simple scalar fibres for \(\eta\), with the angles and product of radii stated above. Every product is attained: on one fixed base fibre, choose \(|v(P)|=|v(Q)|=\sqrt{|\eta|}\) and choose their phases to realize \(\eta\). No zero is on the diagonal, since the evaluation kernel is positive.

**Step 3: the nonstandard sharp scale.** On a fixed complex neighbourhood of \(y=-2L\) excluding zero, substitute \(S=qy\). The negative-frequency series can be expanded uniformly as
\[
 \sum_{m\ge1}\frac{2qm}{1-4^{-qm}}(qy)^{-m}
 =\frac2y+\frac4{qy^2}+O(q^{-2}).
\]
The positive-frequency series is exponentially small there: its first term is \(O(q^2/4^q)\), and the later terms form a geometrically dominated series. It follows, uniformly on that neighbourhood, that
\[
 F_q(qy)=\frac1L+\frac2y+\frac4{qy^2}+O(q^{-2})+O(q^2 4^{-q}).
\]
The limiting function \(L^{-1}+2/y\) has a unique simple zero at \(y_0=-2L\). The holomorphic implicit-function argument (or Rouche's theorem on a sufficiently small fixed circle) gives one simple nearby root. Writing \(y_q=y_0+c/q+O(q^{-2})\) and comparing coefficients yields
\[
 -\frac{2c}{y_0^2}+\frac4{y_0^2}=0,\quad\text{so }c=2.
\]
Thus \(S_{q,-}=qy_q=-2Lq+2+O(q^{-1})\). The classical exact two-zero classification identifies this nearby root with the unique negative root of modulus less than \(2^q\). The other root follows by inversion. Taking logarithms, using \(|S_{q,-}|=2Lq-2+O(q^{-1})\), gives
\[
 \log r_{q,-}=\frac{\log q+\log(2L)}q+O(q^{-2}),\qquad
 \log\frac4{r_{q,+}}=\log r_{q,-},
\]
which proves both limits. The zero radii are positive, and no branch ambiguity enters these logarithms.

## Verification
The independent analytic ingredients are the square-integrable Laurent decomposition in [1], the two-zero annulus theorem in [2], and the uniformly dominated singular perturbation above. The accompanying `CHECK.py` evaluates the exact convergent Laurent series with high precision for several denominators, locates the inner negative root, checks inversion symmetry, and compares \(S_{q,-}+2q\log2\) to its proven limit \(2\). Its finite computations are diagnostics, not a substitute for the infinite-series argument or the cited exact two-zero theorem.

## Relationship to prior work
Yuan [1] introduced the punctured-elliptic-curve construction at irrational monodromy to produce one-dimensional Bergman spaces. An earlier diagonal-density result [3] already classifies the finite/infinite holonomy dimensions and gives the exact diagonal scalar kernel; those facts are not new here. Jacobson [2, Chapter 2], building on classical work of Suita and Yamada, already proves exactly two negative product zeros for the ordinary annulus, and hence (after the elementary power-map reduction) implies the qualitative two-family count. The present contribution is the sharp \(-2q\log2+2\) root expansion and resulting logarithmic-over-linear escape law for the off-diagonal zero fibres of the new pseudoconvex bundle family, together with an explicit interpretation of the inherited zero/nonzero phase. The prior exact annulus and diagonal results are not relabelled as independent discoveries.

## Limitations
This is a statement about **scalar product-value fibres**, not about the number of zeros for any fixed point in a two-variable Bergman kernel. It does not classify all complex-geometric invariants of \(\Omega_a\), and the expansion is asymptotic for large reduced denominator, not an explicit error bound for every finite \(q\). The full geometry of zeros as the two base coordinates vary is not determined. Historical priority for analogous annulus asymptotics outside the inspected sources remains a risk; no independent validation has occurred.

## References
[1] Yuan Yuan, *Pseudoconvex domains in complex Euclidean space with one-dimensional Bergman spaces*, arXiv:2610.21749v1, first publicly available 2026-10-15; Sections 2.1--2.2, especially Proposition 7. https://arxiv.org/abs/2610.21749

[2] Robert L. Jacobson, *Weighted Bergman Kernel Functions and the Lu Qi-keng Problem*, Texas A&M University dissertation (2012), Chapter 2, §§2.1--2.4, especially the two-root classification and Corollaries 2.3--2.5. https://oaktrust.library.tamu.edu/bitstreams/b6456417-1768-47a6-bdc0-48f4819ebd0a/download

[3] *Finite- and infinite-holonomy Bergman dimensions and diagonal kernels on punctured-elliptic annulus bundles*, earlier mathematical result concerning the same twisted bundle, cited for the already established canonical-degree and diagonal identities.
