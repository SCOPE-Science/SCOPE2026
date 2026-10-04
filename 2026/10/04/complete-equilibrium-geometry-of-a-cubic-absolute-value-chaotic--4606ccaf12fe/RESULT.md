# Complete equilibrium geometry of a cubic–absolute-value chaotic flow

## Finding
Consider the two-parameter system
\[
\dot x=yz,\qquad \dot y=x^3-y^3,\qquad \dot z=a|x|-by^3-xy,
\]
with \(a,b>0\), introduced by Moysis et al. The equilibrium set is not only the line \(\{(0,0,z):z\in\mathbb R\}\). There is always one isolated positive equilibrium \(E_{+}=(r_{+},r_{+},0)\), where
\[
r_{+}=\frac{\sqrt{1+4ab}-1}{2b}>0.
\]
If \(0<4ab<1\), there are also two isolated negative equilibria
\[
r_{-,\pm}=\frac{-1\pm\sqrt{1-4ab}}{2b},\qquad E_{-,\pm}=(r_{-,\pm},r_{-,\pm},0).
\]
At \(4ab=1\) these two negative equilibria coalesce at \(r=-1/(2b)\), while for \(4ab>1\) no negative isolated equilibrium exists.

At every isolated equilibrium \(E_r=(r,r,0)\), the characteristic polynomial is
\[
p_r(\lambda)=\lambda^3+3r^2\lambda^2-br^3\lambda+3r^4(1+2br).
\]
The positive branch is unstable with two eigenvalues in the open right half-plane. When the two negative branches exist, the more-negative branch is unstable with one eigenvalue in the open right half-plane. The less-negative branch is asymptotically stable exactly for
\[
\frac{2}{9}<ab<\frac14,
\]
is unstable for \(0<ab<2/9\), and at \(ab=2/9\) has the exact factorization
\[
p_r(\lambda)=\frac{(3b^2\lambda+1)(27b^2\lambda^2+1)}{81b^4},
\]
so its linearization has one negative eigenvalue and one purely imaginary conjugate pair. At \(ab=1/4\), the coalesced negative equilibrium has a zero eigenvalue.

For the journal article's displayed chaotic parameter choice \(a=0.65\), \(b=0.1\), the isolated equilibria have
\[
r\approx0.6124860802,\quad -0.6988373665,\quad -9.3011626335,
\]
and all three are unstable. Thus the published statement that the equilibria lie on the line \((0,0,z)\) is false. In particular, the classification of the reported chaotic attractor as hidden cannot follow merely from the claimed line-equilibrium geometry: the defining basin condition must also be checked near these omitted isolated equilibria.

## Assumptions and scope
The parameters satisfy \(a,b>0\). The equilibrium and stability classification is for the exact continuous-time vector field above. The absolute-value term is nondifferentiable on \(x=0\), but every isolated equilibrium has \(r\ne0\), so the vector field is smooth in a neighborhood of each isolated equilibrium and ordinary linearization applies there.

The conclusion about hiddenness is deliberately limited. It does not assert that the published chaotic attractor is self-excited, because that would require information about its basin near the isolated equilibria. It establishes that the paper's stated equilibrium set is incomplete and therefore that its equilibrium-based inference of hiddenness is insufficient.

The primary classification is MSC 34C28, complex behavior and chaotic systems of ordinary differential equations.

## Proof
At an equilibrium, \(x^3-y^3=0\). Over the reals this gives \(x=y\). The first equation becomes \(xz=0\).

If \(x=0\), then \(y=0\), and the third equation vanishes for every \(z\). This gives the full equilibrium line \((0,0,z)\).

If \(x\ne0\), then \(z=0\), and the third equation reduces to
\[
a|x|-bx^3-x^2=0.
\]
For \(x>0\), division by \(x\) gives
\[
a-x-bx^2=0,
\]
whose unique positive root is \(r_{+}\) above. For \(x<0\), division by \(-x\) gives
\[
a+x+bx^2=0.
\]
Its discriminant is \(1-4ab\), yielding the two, one double, or zero negative roots stated above. This proves the equilibrium classification.

At an isolated equilibrium write \(s=\operatorname{sgn}(r)\). Since \(|r|=sr\), the equilibrium relation can be written
\[
as=r+br^2.
\]
The Jacobian is
\[
J_r=\begin{pmatrix}
0&0&r\\
3r^2&-3r^2&0\\
as-r&-3br^2-r&0
\end{pmatrix}.
\]
Substituting the equilibrium relation into \(\det(\lambda I-J_r)\) gives the displayed cubic \(p_r\).

For \(r>0\), its coefficients in descending order are \(1\), \(3r^2\), \(-br^3\), and \(3r^4(1+2br)\). The Routh first column has signs \(+,+,-,+\), so there are two eigenvalues in the open right half-plane.

For the more-negative root, \(1+2br=-\sqrt{1-4ab}<0\), so the constant coefficient of \(p_r\) is negative while the leading coefficient is positive. The Routh first column has one sign change, hence one eigenvalue lies in the open right half-plane.

For the less-negative root, all cubic coefficients are positive. The cubic Hurwitz condition reduces to
\[
(3r^2)(-br^3)>3r^4(1+2br),
\]
which is equivalent to
\[
-3br>1.
\]
With \(r=(-1+\sqrt{1-4ab})/(2b)\), this is equivalent to \(\sqrt{1-4ab}<1/3\), hence to \(ab>2/9\). Together with existence, \(ab<1/4\), this gives the exact stable interval. Equality \(ab=2/9\) gives \(r=-1/(3b)\) and the stated factorization. At \(ab=1/4\), \(1+2br=0\), so \(p_r(0)=0\).

## Verification
The accompanying script `artifacts/verify_equilibria.py` reconstructs the Jacobian and characteristic polynomial symbolically, checks the source parameter example with exact radicals, and verifies the \(ab=2/9\) factorization. Its recorded output is in `artifacts/verification_output.txt`. These computations are checks of the algebra; the proof above is exact and does not rely on numerical experiments.

The source equations and the line-only equilibrium statement were inspected in the full published article. The earlier conference version contains the same vector field and likewise states that the system has a line of equilibrium points and therefore belongs to systems with hidden attractors. The journal article explicitly identifies itself as an extension of that conference work.

## Relationship to prior work
The earliest verified source is the MOCAST 2020 conference paper by Moysis et al., presented in Bremen on 7–9 September 2020 and published as DOI 10.1109/MOCAST49295.2020.9200286. It gives the same system and states that it has a line of equilibrium points. The expanded Telecom article, DOI 10.3390/telecom1030019, again states that the equilibria lie on \((0,0,z)\) and uses that statement in its hidden-attractor classification.

Targeted searches of the published-finding corpus mathematical findings database using the source title, the exact nonlinearities, equilibrium terminology, hidden-attractor terminology, and the omitted-root formulation returned no record for this system or this equilibrium/stability classification. The closest records concern equilibrium corrections or recurrence laws for different vector fields, including Halvorsen, Rössler, Shimizu–Morioka/Rucklidge, and Rabinovich–Fabrikant systems; none implies the algebraic root structure or the Routh–Hurwitz partition derived here.

Targeted public-literature searches by exact title, DOI, equation fragments, and combinations of the authors' names with equilibrium and hidden-attractor terminology found the conference and journal sources and later papers citing related line-equilibrium systems, but no correction of this equilibrium set or the stability partition above.

## Limitations
The hidden-attractor definition is a basin-of-attraction condition. Finding omitted isolated equilibria does not by itself prove that a particular attractor is self-excited. A rigorous reclassification of the reported chaotic attractor would require a basin analysis near every equilibrium; finite numerical trajectories would not by themselves prove that condition.

The originality search cannot rule out an equivalent correction in unindexed commentary, theses, or literature using substantially different notation. The equilibrium classification and stability partition are exact consequences of the displayed vector field, but the significance claim is limited to correcting the published equilibrium geometry and the inference that was based on it.

## References
1. L. Moysis, C. Volos, I. Stouboulos, S. Goudos, S. Çiçek, V.-T. Pham, and V. K. Mishra, “A Novel Chaotic System with Application to Secure Communications,” 2020 9th International Conference on Modern Circuits and Systems Technologies (MOCAST), 2020, pp. 1–4. DOI: https://doi.org/10.1109/MOCAST49295.2020.9200286
2. L. Moysis, C. Volos, I. Stouboulos, S. Goudos, S. Çiçek, V.-T. Pham, and V. K. Mishra, “A Novel Chaotic System with a Line Equilibrium: Analysis and Its Applications to Secure Communication and Random Bit Generation,” Telecom 1 (2020), 283–296. DOI: https://doi.org/10.3390/telecom1030019
3. Mathematical Reviews and zbMATH, Mathematics Subject Classification 2020, 34C28: complex behavior and chaotic systems of ordinary differential equations. https://mathscinet.ams.org/mathscinet/msc/msc2020.html
