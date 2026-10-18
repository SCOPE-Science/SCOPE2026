# A universal sharp conditioning law for projective harmonic interpolation on qutrit SICs

## Finding
Let \(X=\{[v_1],\ldots,[v_9]\}\subset\mathbb{CP}^2\) be **any** nine equiangular complex lines, represented by unit vectors \(v_j\in\mathbb C^3\) satisfying \(|\langle v_i,v_j\rangle|^2=1/4\) for \(i\ne j\). This includes every qutrit symmetric informationally complete configuration; no special fiducial or group covariance is assumed. Let \(\mathcal H_{q,q}\) be the restrictions to the unit sphere \(S^5\) of complex harmonic polynomials homogeneous of degree \(q\) in \(z\) and degree \(q\) in \(\bar z\), with the probability-normalized spherical \(L^2\) norm. Since their values are phase invariant, evaluation \(E_q:\mathcal H_{q,q}\to\mathbb C^9\) is well defined on the projective lines.

For every integer \(q\ge0\), set
\[
 a_q=\frac{P_q^{(1,0)}(-1/2)}{q+1}
     =\frac{2}{3(q+1)}\bigl(P_q(-1/2)-P_{q+1}(-1/2)\bigr),
\]
where \(P_q\) and \(P_q^{(1,0)}\) are the standard Legendre and Jacobi polynomials. The sampling Gram matrix is exactly
\[
 G_q=E_qE_q^*=(q+1)^3\bigl((1-a_q)I_9+a_qJ_9\bigr).
\]
Its eigenvalues are \((q+1)^3(1-a_q)\) with multiplicity eight and \((q+1)^3(1+8a_q)\) with multiplicity one.

**The complete rank law and sharp all-degree conditioning law are**
\[
 \operatorname{rank}E_q=\begin{cases}1,&q=0,\\8,&q=1,2,\\9,&q\ge3,\end{cases}
 \qquad
 \sup_{q\ge3}\frac{\lambda_{\max}(G_q)}{\lambda_{\min}(G_q)}
 =\frac{56}{25},
\]
with equality at **exactly \(q=3\)**. Thus every complex nine-tuple is interpolable by each separate bidegree \((q,q)\) for \(q\ge3\), with sampling condition number at most \(2\sqrt{14}/5\), uniformly over all nine-line SIC choices and all degrees. At \(q=1\) and \(q=2\), the attainable sample vectors are exactly the mean-zero ones. At \(q=3\) the Gram eigenvalues are \(225/4\) (eightfold) and \(126\) (onefold).

## Assumptions and scope
Fix any ordered nine-tuple of distinct unit representatives \(v_j\in\mathbb C^3\) with the displayed equiangular property. A SIC is an existing configuration, not an assumption of existence in arbitrary dimension. Complex harmonic means annihilation by \(\Delta_{\mathbb C}=\sum_{j=1}^3\partial_{z_j}\partial_{\bar z_j}\); the \(L^2\) measure on \(S^5\) has total mass one. Euclidean norm on \(\mathbb C^9\) has no factor of \(1/9\). Singular-value condition number refers to the map from \((\ker E_q)^\perp\) onto its image, and the stated bound applies to its *surjective* cases \(q\ge3\). The more elementary Gram eigenvalue ratio is its square.

## Proof
**1. Harmonic kernel normalization.** The standard complex-spherical harmonic decomposition gives
\[
 \dim\mathcal H_{q,q}=\binom{q+2}{2}^2-\binom{q+1}{2}^2=(q+1)^3=:h_q.
\]
The Jacobi addition theorem, for probability-normalized spherical measure, gives the reproducing kernel
\[
 K_q(z,w)=h_q\frac{P_q^{(1,0)}(2|\langle z,w\rangle|^2-1)}{q+1}.
\]
The diagonal is \(h_q\) because \(P_q^{(1,0)}(1)=q+1\). The fixed SIC squared overlap \(1/4\) makes every off-diagonal entry \(h_qa_q\). Consequently \(G_q=h_q[(1-a_q)I_9+a_qJ_9]\), with the stated spectral decomposition.

**2. Reduction to an exact Legendre recurrence.** Define
\[
 Q_q(x)=\frac{P_q(x)-P_{q+1}(x)}{1-x}.
\]
This is a polynomial of degree \(q\), since the numerator vanishes at \(x=1\). For any polynomial \(r\) of degree less than \(q\), Legendre orthogonality implies
\[
 \int_{-1}^1(1-x)Q_q(x)r(x)\,dx
 =\int_{-1}^1(P_q(x)-P_{q+1}(x))r(x)\,dx=0.
\]
Moreover \(Q_q(1)=P_{q+1}'(1)-P_q'(1)=q+1\). By uniqueness of the endpoint-normalized Jacobi polynomial with weight \(1-x\), \(Q_q=P_q^{(1,0)}\). Evaluation at \(x=-1/2\) gives the second expression for \(a_q\). Hence all needed finite values follow from the exact rational recurrence
\[
 P_0(x)=1,\quad P_1(x)=x,\qquad
 (q+1)P_{q+1}(x)=(2q+1)xP_q(x)-qP_{q-1}(x).
\]
In particular \(a_0=1\), \(a_1=a_2=-1/8\), and \(a_3=31/256\).

**3. Exact finite cutoff.** Exact rational recurrence for every \(3\le q\le19\) yields
\[
 \max_{3\le q\le19}a_q=\frac{31}{256}\quad\text{(only at }q=3\text{)},\qquad
 \min_{3\le q\le19}a_q=-\frac{47}{1024}\quad\text{(at }q=5\text{)}.
\]
All seventeen individual rational values and the exact test are included in `spectrum_certificate.json` and `check_sic_spectrum.py`; both are reproducible using only the Python standard library.

**4. Analytic tail, including all uncomputed degrees.** For every integer \(n\ge0\) and \(-1\le x\le1\), the classical Legendre integral representation
\[
 P_n(\cos\theta)=\frac1\pi\int_0^\pi
 (\cos\theta+i\sin\theta\cos t)^n\,dt
\]
immediately implies \(|P_n(x)|\le1\). Consequently, for **every** \(q\ge20\),
\[
 |a_q|\le\frac{4}{3(q+1)}\le\frac4{63}
 <\frac{31}{473}<\frac{31}{256}.
\]
Thus the complete tail, not just a sampled finite set, has \(a_q\in(-31/473,31/256)\), and in particular \(-1/8<a_q<1\). The finite values from the preceding paragraph enjoy the same strict positivity condition \(-1/8<a_q<1\) for \(q\ge3\). This proves that both Gram branches are positive for every such \(q\), yielding the rank law. The low-degree values give ranks one, eight, and eight.

**5. Sharp worst condition number.** For \(a\in(-1/8,1)\), let
\[
 \mathcal C(a)=\frac{\max\{1-a,1+8a\}}{\min\{1-a,1+8a\}}.
\]
On the positive branch \(a\ge0\), the inequality \(\mathcal C(a)\le56/25\) is equivalent to \(a\le31/256\). On the negative branch \(a<0\), it is equivalent to \(a\ge-31/473\). Step 3 proves the positive condition sharply and the negative condition strictly through degree 19, since \(-47/1024>-31/473\). Step 4 proves both strictly for all \(q\ge20\). Only \(q=3\) attains the resulting sharp bound. There \(h_3=64\) and \(a_3=31/256\), so the two exact Gram eigenvalues are \(64\cdot225/256=225/4\) and \(64\cdot63/32=126\).

**6. Attainability and minimum-norm reconstruction.** Put \(P_{\mathrm c}=J_9/9\) and \(P_\perp=I_9-P_{\mathrm c}\). Then
\[
 G_q=h_q[(1-a_q)P_\perp+(1+8a_q)P_{\mathrm c}].
\]
For \(q=1,2\) only the constant spectral branch vanishes, so \(\operatorname{ran}E_q=\{y:\sum_jy_j=0\}\). For \(q=0\), only constant vectors are attained. For \(q\ge3\), put
\[
 G_q^{-1}=h_q^{-1}\left[\frac{P_\perp}{1-a_q}+\frac{P_{\mathrm c}}{1+8a_q}\right].
\]
For every prescribed \(y\in\mathbb C^9\), its unique minimum-norm interpolant in \(\mathcal H_{q,q}\) is
\[
 f_y(z)=\sum_{j=1}^{9}(G_q^{-1}y)_j K_q(z,v_j),
 \qquad \|f_y\|_{L^2(S^5)}^2=y^*G_q^{-1}y.
\]
For the non-surjective cases the same formula holds with the Moore–Penrose pseudoinverse and \(y\in\operatorname{ran}E_q\). The representer theorem follows directly by orthogonally decomposing the harmonic Hilbert space into the span of the nine kernel sections and its evaluation-nullspace.

## Verification
Run `python3 check_sic_spectrum.py` in the directory containing the accompanying certificate. The standard-library checker calculates every \(a_q\) exactly for \(0\le q\le19\), certifies the finite extrema and the rational tail threshold, verifies every finite full-rank Gram condition, and constructs a nine-point Weyl–Heisenberg SIC to check the equiangular geometry and Jacobi-kernel entries through degree eleven. The Python run completed successfully. The analytic proof above, not the finite experiment, establishes all degrees and the sharp infinite supremum. The checker uses floating-point tolerances only for its independent geometric spot checks; the claimed exceptional degrees and extremal ratios use rational arithmetic.

## Relationship to prior work
Renes, Blume-Kohout, Scott, and Caves construct SICs and establish their frame significance; these SIC definitions and the qutrit existence premise are prior results. Roy and Suda develop the complex spherical harmonic decomposition and the Jacobi addition theorem; the low-degree projective design vanishing at bidegrees \((1,1)\) and \((2,2)\) is likewise prior knowledge. Tabia and Appleby study nontrivially varying families of qutrit SICs and their probability geometry. These sources are not claimed to be new. The statement distinguished here is the simultaneous **all-degree exact interpolation cutoff** and **sharp uniform worst-degree conditioning bound** for every such SIC. The proof does not assume the Hesse SIC: only the pairwise squared overlap enters. Earlier calculations for *charged* harmonics of bidegree \((q+3,q)\) do not imply this phase-invariant \((q,q)\) classification; the Jacobi parameter is different.

## Limitations
This is a theorem conditional on the existence of a nine-line SIC in \(\mathbb C^3\), which is known. It does not claim a theorem for all SIC dimensions, arbitrary sampling geometries, or unequal bidegrees. The inverse condition number refers to exact harmonic interpolation and not to phase-retrieval stability, experimental noise outside the sampled nine values, or a physical measurement protocol. Mathematical publication priority is not independently certified; equivalent earlier results under projective-design or Jacobi terminology remain possible.

## References
1. J. M. Renes, R. Blume-Kohout, A. J. Scott, C. M. Caves, *Symmetric Informationally Complete Quantum Measurements*, arXiv:quant-ph/0310075, first posted 2003-10-13, especially sections II–IV.
2. A. Roy, S. Suda, *Complex spherical designs and codes*, arXiv:1104.4692, first posted 2011-04-25, especially section 2 (harmonic dimension, normalized Jacobi kernels and addition theorem) and example 5.5.
3. G. N. M. Tabia, D. M. Appleby, *Exploring the geometry of qutrit state space using symmetric informationally complete probabilities*, arXiv:1304.8075, first posted 2013-04-30, especially section II (nine-projector SIC families).
4. Classical Legendre and Jacobi orthogonality and three-term recurrences; these are proved or reduced to explicit standard identities in the argument above.
