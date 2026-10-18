# Complete two-polygon phase-retrieval criterion for polynomials of every degree

## Finding

**Theorem (balanced concentric polygon classification).** For every integer \(d\geq1\), positive radii \(r,s\), and real offsets \(\phi,\psi\), set
\[
\mathcal X=\{r e^{i(\phi+j\pi/d)}:0\leq j<2d\}\ \cup\ \{s e^{i(\psi+j\pi/d)}:0\leq j<2d\}.
\]
For the complex polynomial space \(\mathcal P_d=\{f(z)=\sum_{k=0}^d a_k z^k:a_k\in\mathbb C\}\), the measurements \(\{|f(z)|^2:z\in\mathcal X\}\) determine **every** polynomial up to multiplication by a complex scalar of modulus one if and only if
\[
\boxed{r\ne s\quad\text{and}\quad\sin(d(\psi-\phi))\ne0.}
\]
The criterion is valid for arbitrarily large degrees and arbitrary complex coefficients, including vanishing endpoint coefficients and repeated roots. The two grids contain exactly \(4d\) sample positions when the criterion holds.

The proof also gives explicit recovery of the *complete intensity trigonometric polynomial* on each circle from the \(4d\) measurements, by two short discrete Fourier transforms and a real two-by-two system. After normalizing the highest Fourier coefficient by the appropriate radius power, that system has singular values
\[
\boxed{\sqrt{1+|\cos(d(\psi-\phi))|}\quad\text{and}\quad
\sqrt{1-|\cos(d(\psi-\phi))|}.}
\]
Thus the highest-harmonic linear demixing is optimally conditioned exactly when \(d(\psi-\phi)\equiv\pi/2\pmod\pi\). This subsidiary singular-value formula is **not** a claim of global nonlinear noise stability.

## Assumptions and scope

Polynomials are complex-valued, of degree *at most* \(d\), with \(d\) an arbitrary positive integer. Radii are arbitrary strictly positive real numbers; neither must equal one nor lie inside the unit disk. Each ring is a regular \(2d\)-gon. Two polynomials \(f,g\) represent the same phase-equivalence class if \(f=\lambda g\) with \(|\lambda|=1\). Measurements are ordered by ring and angular index; in the successful case the circles are distinct, so there are \(4d\) distinct locations. The uniqueness assertion is for **all** coefficient vectors, not generic vectors alone.

## Proof

**Step 1: Fourier coefficients and the unique angular alias.** Suppose \(f(z)=\sum_{k=0}^d a_k z^k\) and \(g(z)=\sum_{k=0}^d b_k z^k\) have identical measurements. Define for \(R>0\)
\[
H_R(\theta)=|f(Re^{i\theta})|^2-|g(Re^{i\theta})|^2
=\sum_{k=-d}^{d} C_k(R)e^{ik\theta}.
\]
For \(0\leq k\leq d\), direct coefficient multiplication gives
\[
C_k(R)=R^k\sum_{j=0}^{d-k}(a_{j+k}\overline{a_j}-b_{j+k}\overline{b_j})R^{2j},
\qquad C_{-k}(R)=\overline{C_k(R)}.
\]
Fix the first circle \(R=r\), \(\alpha=\phi\). The elementary roots-of-unity identity for the \(2d\) equally spaced angles shows that the sample values of \(H_r\) vanish only if \(C_k(r)=0\) for \(-d<k<d\). The two endpoint terms \(k=\pm d\) collide in the same discrete Fourier bin, giving exactly
\[
2\operatorname{Re}(C_d(r)e^{id\phi})=0.
\]
The analogous statements hold at \(R=s\), \(\alpha=\psi\). For the endpoint term there is only one summand in the coefficient formula:
\[
C_d(R)=R^d\,v,\qquad v=a_d\overline{a_0}-b_d\overline{b_0}.
\]
The two endpoint equations are therefore \(\operatorname{Re}(v e^{id\phi})=\operatorname{Re}(v e^{id\psi})=0\). Their real coefficient matrix has determinant \(\sin(d(\phi-\psi))\), up to the harmless choice of row/column orientation. Under the asserted angular condition it is invertible, hence \(v=0\). In particular, **all** Fourier coefficients of \(H_r\) and of \(H_s\) vanish. We have proved
\[
|f(re^{i\theta})|=|g(re^{i\theta})|,\qquad
|f(se^{i\theta})|=|g(se^{i\theta})|\qquad(\text{every }\theta\in\mathbb R).
\]

**Step 2: Two-circle rational rigidity.** If either polynomial is zero, then its partner has at least \(2d\) distinct zeros on the first circle, exceeding its degree, hence both are zero. Otherwise set the rational function \(h=f/g\) and its coefficient-conjugate \(h^\sharp(z)=\overline{h(\overline z)}\). The modulus-one condition on a circle \(|z|=R\), away from finitely many possible poles, yields
\[
h(z)h^\sharp(R^2/z)=1.
\]
Since the two sides are rational functions agreeing at infinitely many points, this is a rational identity. Applying it at both radii and cancelling \(h\) gives
\[
h^\sharp(w)=h^\sharp(qw),\qquad q=s^2/r^2>0,\quad q\ne1.
\]
A rational function admitting this scaling invariance is constant: in a punctured neighborhood of the origin, write its convergent Laurent series \(\sum_{k=-m}^{\infty}c_k w^k\). Equality under \(w\mapsto qw\) gives \((q^k-1)c_k=0\) for every integer \(k\). As \(q\ne1\) is positive, all coefficients except \(c_0\) vanish. Analytic continuation of rational functions finishes the argument. Therefore \(h\) is constant, and its modulus on either circle is one. Thus \(f=\lambda g\), \(|\lambda|=1\).

**Step 3: Both geometric conditions are necessary.** If \(r=s=R\), take \(f(z)=z\) and \(g(z)=R\), which have identical moduli at every point of that circle but are not phase multiples. If \(\sin(d(\psi-\phi))=0\), take
\[
f(z)=1+i e^{-id\phi}z^d,\qquad g(z)=1-i e^{-id\phi}z^d.
\]
At either sampling polygon, the quantity \(e^{-id\phi}z^d\) is real: on the second polygon this follows from \(e^{id(\psi-\phi)}\in\{1,-1\}\). Hence \(|1+it|^2=|1-it|^2\) for every measured real \(t\). The two displayed polynomials are not phase multiples because their constant terms coincide but their degree-\(d\) terms are negatives. This proves necessity, including simultaneous failure of both conditions.

**Step 4: Explicit Fourier demixing and its angular singular values.** For an individual \(f\), write \(F_R(\theta)=|f(Re^{i\theta})|^2\). At either grid, for \(|k|<d\), its true Fourier coefficient is directly recovered by
\[
\widehat F_R(k)=\frac1{2d}\sum_{j=0}^{2d-1}
 F_R(\alpha+j\pi/d)e^{-ik(\alpha+j\pi/d)}.
\]
The one remaining complex coefficient \(w=a_d\overline{a_0}\) obeys
\[
\frac1{2R^d}\left[\frac1{2d}\sum_{j=0}^{2d-1}(-1)^jF_R(\alpha+j\pi/d)\right]
=\operatorname{Re}(w e^{id\alpha}).
\]
The two right sides for \(\alpha=\phi,\psi\) form a real system with matrix whose rows are \((\cos(d\alpha),-\sin(d\alpha))\). The eigenvalues of its Gram matrix are \(1\pm|\cos(d(\psi-\phi))|\), yielding the asserted singular values and optimal angular staggering. Recovering \(w\) recovers the positive and negative highest harmonics on both circles, so both entire functions \(F_r,F_s\) are known.

## Verification

A standalone deterministic checker `verify.py` tests polynomial Fourier-coefficient interpolation and top-bin demixing over degrees \(1\) through \(8\), multiple randomly seeded complex coefficient vectors, the rank of the real Hermitian intensity sampling map in each degree, and explicit failure witnesses for both geometric obstructions. The checker reports `VERIFY_OK 5784 deterministic finite comparisons; tested degrees 1 through 8`. These finite computations are corroboration, **not** a proof for arbitrary degree. The proof above supplies the universal quantifiers independently of the checker.

## Relationship to prior work

Bodmann and Hammen (2013/2015) established phase-retrieval constructions using *intersecting circles*, with a shared-point geometry and an irrational intersection angle; their sampling geometry is not two concentric regular \(2d\)-gons. Pohl, Li, and Boche (2017) provide a \(4d\)-sample construction on *concentric* circles using an unbalanced distribution of \(2d+1\) points on one ring and \(2d-1\) on the other. The present result classifies the **balanced regular** allocation by exact necessary-and-sufficient conditions, not merely the existence of some \(4d\)-sample design.

Chalendar and Partington (2024), Theorem 2.16, show uniqueness when equal moduli are known on both entire noncoincident nested circles, a background ingredient also proved directly above. They do not give the present discrete \(2d+2d\) alias-demixing criterion. The recent de Dios Pont–Greilhuber–Liehr–Taylor (2026) result studies uniformly discrete phase-retrieval sets in infinite-dimensional short-time Fourier-transform spaces, distinct from this finite-degree two-polygon classification.

The quadratic and cubic instances are special cases of the all-degree theorem; verifying these two degrees alone cannot establish the universal claim. Neither two-circle continuous uniqueness alone nor existence of a different measurement geometry alone entails the exact balance-and-stagger criterion without additional Fourier analysis. These comparisons do not establish absolute historical priority.

## Limitations

The theorem establishes noiseless injectivity and the conditioning of a specified two-by-two highest-harmonic linear subsystem. It does not establish a uniform noise-stability bound for nonlinear polynomial phase recovery, nor any lower bound for the number of measurements among **all possible** phase-retrieval frames. The full literature might contain an earlier equivalent statement under a different parametrization. The argument assumes exact complex polynomial samples and exactly regular angular grids.

## References

1. J. de Dios Pont, J. Greilhuber, L. Liehr, M. A. Taylor, *Phase retrieval from a uniformly discrete point set*, arXiv:2609.28341, first publicly posted September 23, 2026. https://arxiv.org/abs/2609.28341.
2. B. G. Bodmann, N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487 (2013), published in Advances in Computational Mathematics 41 (2015). https://arxiv.org/html/1302.5487v1.
3. V. Pohl, N. Li, H. Boche, *Phase Retrieval in Spaces of Analytic Functions on the Unit Disk*, SampTA (2017), DOI:10.1109/SAMPTA.2017.8024411. Author presentation: https://www.ce.cit.tum.de/fileadmin/w00cgn/lti/pdf/vortraege/Pohl-Phase_Retrieval_in_Spaces_of_Analytic_Functions_on_the_Unit_Disk.pdf.
4. I. Chalendar, J. R. Partington, *Phase Retrieval on Circles and Lines*, arXiv:2403.16255 (2024), especially Theorems 2.11 and 2.16. https://arxiv.org/pdf/2403.16255.
