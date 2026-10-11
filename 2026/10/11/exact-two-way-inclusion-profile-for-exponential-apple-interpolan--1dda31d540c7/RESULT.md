# Exact two-way inclusion profile for exponential–apple interpolants

## Finding

For real \(0\le q\le 1/2\), set \(\phi_q(z)=e^z(1+z)^q\) on the open unit disk \(\mathbb D\), using the principal logarithm. Define \(\mathcal S_q\) as the set of normalized analytic functions \(f(0)=0\), \(f'(0)=1\) for which \(zf'(z)/f(z)\prec\phi_q(z)\). In particular, \(\mathcal S_0\) is the exponential-starlike class and \(\phi_{1/2}(z)=e^z\sqrt{1+z}\) is the apple-like generator.

**Theorem (exact directed comparison).** Every \(\phi_q\) is univalent and has positive real part on \(\mathbb D\). For all \(0\le q\le1/2\), one has \(\mathcal S_0\subseteq\mathcal S_q\), strictly when \(q>0\). The largest \(R_q\in(0,1]\) such that
\[
 f\in\mathcal S_q,\quad 0<r\le R_q\quad\Longrightarrow\quad f(rz)/r\in\mathcal S_0
\]
for every such \(f\) and every \(z\in\mathbb D\) is exactly
\[
 R_0=1,\qquad R_q=1-qW(1/q)\quad (0<q\le1/2),
\]
where \(W\) is the positive real branch of the Lambert function. The associated logarithmic image \(h_q(\mathbb D)\), where \(h_q(z)=z+q\log(1+z)\), has exact centered disk inradius \(1+q\log2\). The boundary loss obeys
\[
 1-R_q=q\bigl(\log(1/q)-\log\log(1/q)+o(1)\bigr)
 \qquad(q\downarrow0).
\]
At the apple-like endpoint \(q=1/2\), the exact forward radius is \(1-W(2)/2=0.5736972489931372543\ldots\), while the reverse inclusion holds on the entire unit disk.

## Assumptions and scope

All parameters \(q\) are real in \([0,1/2]\); all functions are analytic on \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). Subordination means composition with an analytic self-map of \(\mathbb D\) fixing the origin. The logarithm is the principal analytic branch on \(1+\mathbb D\). Inradius means the supremum of radii of open Euclidean disks centered at zero and contained in the indicated image. For \(q=0\), all statements use the continuous endpoint convention. No assertion is made for \(q>1/2\).

## Proof

**Step 1: legitimate starlike generators.** Put \(h_q(z)=z+q\log(1+z)\). Since \(\operatorname{Re}(1/(1+z))>1/2\) on \(\mathbb D\), the derivative \(h_q'(z)=1+q/(1+z)\) has positive real part. Integrating this derivative along the segment between any two points of the convex disk proves that \(h_q\) is univalent. To see that \(\phi_q=e^{h_q}\) is univalent and has positive real part, use the harmonic maximum principle on the imaginary part of \(h_q\). For \(z=e^{i\theta}\) with \(0\le\theta<\pi\),
\[
 \operatorname{Im}h_q(z)=\sin\theta+\frac{q\theta}{2}
 \le\sin\theta+\frac{\theta}{4}.
\]
The last function has unique maximum at \(\theta_* =\arccos(-1/4)<2\), giving a maximum smaller than \(\sqrt{15}/4+1/2<3/2<\pi/2\). The negative semicircle is conjugate-symmetric; the limiting imaginary values at \(z=-1\) are \(\pm q\pi/2\). Hence \(|\operatorname{Im}h_q(z)|<\pi/2\) on the entire disk. Consequently \(\operatorname{Re}e^{h_q(z)}>0\). The exponential cannot identify two values in this horizontal strip of width less than \(\pi\), so \(\phi_q\) is univalent. The standard starlikeness criterion shows that each \(\mathcal S_q\) consists of normalized starlike univalent functions.

**Step 2: exact centered image disk.** The identity
\[
 \frac{h_q(z)}z=1+q\int_0^1\frac{dt}{1+tz}
\]
holds also at \(z=0\) by continuity. For \(|z|<1\) and \(0\le t\le1\), the Möbius disk estimate \(\operatorname{Re}(1/(1+tz))\ge1/(1+t)\) follows either from the image disk of \(1/(1+tz)\), or directly by multiplying positive denominators. Therefore
\[
 \operatorname{Re}\frac{h_q(z)}z\ge 1+q\log2=:c_q,
 \qquad |h_q(z)|\ge c_q|z|.
\]
If \(|w|<c_q\), choose \(r<1\) with \(|w|<c_qr\). On \(|z|=r\), \(|h_q(z)|>|w|\); Rouché's theorem shows that \(h_q(z)-w\) has the same one zero in \(|z|<r\) as \(h_q\). Thus \(\{|w|<c_q\}\subset h_q(\mathbb D)\). Conversely \(\operatorname{Re}h_q(z)\le |z|+q\log(1+|z|)<1+q\log2=c_q\), so the boundary point \(c_q\) is not in the image. The centered inradius is exactly \(c_q\). Since \(c_q\ge1\), \(\mathbb D\subset h_q(\mathbb D)\), and exponentiation plus injectivity implies \(e^{\mathbb D}\subseteq\phi_q(\mathbb D)\). Both generators take zero to one; therefore \(\phi_0\prec\phi_q\) and \(\mathcal S_0\subseteq\mathcal S_q\).

**Step 3: sharp forward radius.** The power series
\[
 -h_q(-z)=(1+q)z+q\sum_{n=2}^\infty\frac{z^n}{n}
\]
has nonnegative coefficients. For any \(0<r<1\) its exact radial maximum is
\[
 \max_{|z|\le r}|h_q(z)|=r-q\log(1-r)=:M_q(r),
\]
with equality at \(z=-r\). Since \(|\operatorname{Im}h_q|<\pi/2\), the injective logarithm identifies \(\phi_q(r\mathbb D)\subset e^{\mathbb D}\) exactly when \(M_q(r)\le1\). For \(q>0\), \(M_q\) increases strictly from zero to infinity, so the unique critical \(R_q\) satisfies \(R_q-q\log(1-R_q)=1\). Putting \(u=1-R_q\) gives \(u\exp(u/q)=1\), hence \(u=qW(1/q)\). For \(q=0\), \(M_0(r)=r\) and \(R_0=1\).

For any \(f\in\mathcal S_q\), write \(zf'(z)/f(z)=\phi_q(\omega(z))\) with \(\omega(0)=0\) and \(|\omega(z)|<1\). Schwarz's lemma yields \(|\omega(rz)|\le r|z|\), so \(zf_r'(z)/f_r(z)=\phi_q(\omega(rz))\in e^{\mathbb D}\) whenever \(r\le R_q\); the value at zero is one, giving subordination to \(e^z\). Sharpness follows from the canonical normalized starlike function
\[
 f_q(z)=z\exp\left(\int_0^z\frac{\phi_q(t)-1}{t}\,dt\right),
 \qquad\frac{zf_q'(z)}{f_q(z)}=\phi_q(z).
\]
For \(R_q<r\le1\), choose \(R_q<s<r\) and \(z=-s/r\in\mathbb D\). Then the logarithm of \(\phi_q(-s)\) is the real number \(-M_q(s)<-1\); consequently \(\phi_q(-s)\notin e^{\mathbb D}\), so \(f_q(rz)/r\notin\mathcal S_0\). This also makes the reverse class inclusion strict for \(q>0\).

**Step 4: endpoint asymptotic.** Set \(L=\log(1/q)\) and \(w=W(1/q)\). Since \(w+\log w=L\), one has \(w=L-\log L+o(1)\) as \(q\downarrow0\). Multiplication by \(q\) proves the asserted logarithmic boundary loss.

## Verification

The exact formula at \(q=1/2\) gives \(R_{1/2}=0.5736972489931372543\ldots\) and \(M_{1/2}(R_{1/2})=1\). The standalone standard-library program `verify_radius.py` recomputes this value using high-precision decimal bisection, checks the defining scalar equations for several rational parameters, and samples the generator's imaginary-angle bound as a diagnostic. These finite numerical checks are supplementary: the universal theorem, including the exact image disk and sharpness for every real parameter, follows from the preceding analytic proof.

## Relationship to prior work

Sana, Saliu and Riaz (first published May 12, 2026) introduced the apple-like function \(e^z\sqrt{1+z}\) and studied coefficient, distortion, and determinant properties. Das and Sarkar studied related coefficient problems. The Geometric Function Atlas studies directed inclusion radii systematically and supplies proved cases for other generators; its released class catalog and all 702 recorded ordered radius comparisons contain no apple-like generator or power-product interpolation. The present exact two-way inclusion law concerns a different explicit natural geometric invariant and adds a continuous interpolation with a singular small-parameter transition. General subordination and Schwarz lemmas used in the proof are standard and not claimed as new.

## Limitations

Only the stated real parameter range is treated; nothing here proves that the full family is a Ma–Minda family in the stronger geometric sense for every parameter. The original apple-like publisher HTML section structure and result prose were examined, but embedded mathematical expressions were incompletely available in extracted text. Thus equivalent statements in formula-inaccessible passages or unindexed literature remain a novelty risk. Numerical diagnostics are not a substitute for the analytic inequalities. Independent review has not been performed.

## References

1. A. Sana, A. Saliu and S. Riaz, *Coefficient Inequalities Related With Apple-Like Functions*, Journal of Function Spaces 2026, article 5570573 (first published May 12, 2026), DOI: 10.1155/jofs/5570573.
2. P. Das and N. Sarkar, *Sharp coefficient Estimates for the class* \(\mathcal S_{\mathcal{AP}}^*\), arXiv:2606.15488 (June 13, 2026).
3. P. Devadiga et al., *The Geometric Function Atlas: A Software System for Radius and Coefficient Problems*, arXiv:2608.15697 (August 16, 2026); released data files `classes.json` and `radii_snapshot.json` in the geometric-function-atlas public source repository.
