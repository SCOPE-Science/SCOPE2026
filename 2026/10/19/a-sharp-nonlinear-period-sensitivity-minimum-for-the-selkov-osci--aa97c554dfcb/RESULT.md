# A sharp nonlinear period-sensitivity minimum for the Selkov oscillator

## Finding
For the dimensionless Selkov kinetic system
\[
\dot x=1-xy^\gamma,\qquad \dot y=\alpha(xy^\gamma-y),
\]
fix any real feedback exponent \(\gamma>1\). As \(\alpha\) decreases toward \(\alpha_H=1/(\gamma-1)\) along the unique small, stable, positive periodic-orbit branch, let \(r>0\) denote twice the modulus of the first nonzero Fourier coefficient of the substrate variable \(x\) over the orbit's *least* period \(T\). Let \(\omega_{\rm lin}>0\) be the absolute imaginary part of the eigenvalues of the positive equilibrium's Jacobian at the *actual*, off-Hopf parameter \(\alpha\). Then
\[
\frac{T\omega_{\rm lin}}{2\pi}-1
=\underbrace{\frac{2(\gamma-1)+1+2/(\gamma-1)}{48}}_{C(\gamma)}r^2+o(r^2),
\qquad r^2=8(\gamma-1)(\alpha-\alpha_H)+o(\alpha-\alpha_H).
\]
The coefficient is positive for all \(\gamma>1\) and has the unique, sharp minimum
\[
\inf_{\gamma>1}C(\gamma)=C(2)=\frac5{48};\qquad
C(\gamma)-\frac5{48}=\frac{(\gamma-2)^2}{24(\gamma-1)}.
\]
In particular, shrinking nonlinear oscillations are slower than the linearized oscillation prediction at their *actual* parameter, and the quadratic period response is least sensitive precisely at feedback exponent \(\gamma=2\).

## Assumptions and scope
The exponent \(\gamma\) is any fixed real number strictly greater than one and \(\alpha>0\) varies only in a sufficiently small, \(\gamma\)-dependent neighborhood above \(\alpha_H\). Dynamics are considered in the positive quadrant, where the noninteger powers are smooth near the equilibrium \((1,1)\). The equilibrium is constant in \(\alpha\). Its Jacobian has trace \((\gamma-1)\alpha-1\), determinant \(\alpha\), and positive linearized angular frequency
\[
\omega_{\rm lin}=\sqrt{\alpha-\tfrac14((\gamma-1)\alpha-1)^2}.
\]
The first-harmonic amplitude \(r\) is defined by writing \(x(t)=\sum_{j\in\mathbb Z}c_j\exp(2\pi ijt/T)\), with \(r=2|c_1|\). The result concerns the orbit born at this Hopf point, not arbitrary large periodic orbits. All limits are for each fixed \(\gamma\).

## Proof
Put \(k=\sqrt{\gamma-1}>0\). At \(\alpha_H=k^{-2}\), the Jacobian and Hopf frequency are
\[
A=\begin{pmatrix}-1&-(1+k^2)\\k^{-2}&1\end{pmatrix},\qquad \omega=k^{-1}.
\]
A right eigenvector with first coordinate one and a bilinear left spectral projection are
\[
q=\begin{pmatrix}1\\-(1+i/k)/(1+k^2)\end{pmatrix},\qquad
\ell=\begin{pmatrix}(1+ik)/2&i k(1+k^2)/2\end{pmatrix},
\]
so \(Aq=i\omega q\), \(\ell q=1\), and \(\ell\bar q=0\).

Expand the vector field at \((1,1)\) as \(A\xi+B(\xi,\xi)/2+C_3(\xi,\xi,\xi)/6+O(\|\xi\|^4)\). Put \(d=(-1,k^{-2})^{\mathsf T}\). For vectors \(u,v,w\) with coordinate subscripts, the complete quadratic and cubic tensors are
\[
B(u,v)=d\{\gamma(u_xv_y+u_yv_x)+\gamma(\gamma-1)u_yv_y\},
\]
\[
C_3(u,v,w)=d\,\gamma(\gamma-1)\{u_xv_yw_y+u_yv_xw_y+u_yv_yw_x+(\gamma-2)u_yv_yw_y\}.
\]
With this normalization, the physical-time cubic Hopf resonance coefficient is
\[
G_{21}=\ell\bigl[C_3(q,q,\bar q)-2B(q,A^{-1}B(q,\bar q))
+B(\bar q,(2i\omega I-A)^{-1}B(q,q))\bigr].
\]
Direct exact substitution and simplification yield
\[
\boxed{G_{21}=-\frac12-i\frac{2k^4+k^2+2}{6k^3}}.
\]
The accompanying standalone exact-arithmetic checker recomputes the tensors, projection, and resolvents without using this identity as an input. The parameter crosses Hopf transversely since the real eigenvalue part is \(k^2(\alpha-\alpha_H)/2\). Because \(\Re G_{21}=-1/2<0\), standard smooth planar Hopf theory yields the locally unique stable small periodic orbit for \(\alpha>\alpha_H\). In spectral coordinate \(w\) its radial equation, to leading orders, is
\[
\dot{|w|}=\frac{k^2}{2}(\alpha-\alpha_H)|w|-\frac14|w|^3
+O((\alpha-\alpha_H)^2|w|+|\alpha-\alpha_H||w|^3+|w|^5).
\]
Thus \(|w|^2=2k^2(\alpha-\alpha_H)+o(\alpha-\alpha_H)\). Since \(q_x=1\), the first Fourier harmonic in the physical \(x\) coordinate has \(r=2|w|+O(|w|^2)\), giving the stated amplitude law.

The phase normal form is
\[
\dot\theta=\omega_{\rm lin}+\frac{\Im G_{21}}2|w|^2+o(|w|^2),
\]
where \(\omega_{\rm lin}\) is evaluated at the actual parameter, not frozen at Hopf. Consequently \(T\omega_{\rm lin}/(2\pi)-1=-\Im G_{21}\,r^2/(8\omega)+o(r^2)\). Substituting the exact imaginary coefficient gives \(C(\gamma)=(2k^4+k^2+2)/(48k^2)\).

Finally,
\[
C(\gamma)=\frac5{48}+\frac{(k-k^{-1})^2}{24}
=\frac5{48}+\frac{(\gamma-2)^2}{24(\gamma-1)}.
\]
Equality holds exactly when \(k=1\), equivalently \(\gamma=2\). This also proves the sharpness and uniqueness of the minimum.

## Verification
Run `python check.py` with Python 3 and SymPy from the package directory. This reconstructs \(A,q,\ell,B,C_3,G_{21}\) and certifies exact equality of the complex cubic coefficient and minimum identity. Independent numerical integrations at exponents \(\gamma=1.5,2,3\) and small positive Hopf offsets show the normalized period coefficient approaching its predicted value; the algebraic argument, not the integrations, establishes the asymptotic theorem. `NUMERICAL.txt` records example estimates and their finite-offset deviations.

## Relationship to prior work
Sel'kov's 1968 original study derives the equilibrium stability threshold and the **zero-order** frequency \(1/\sqrt{\gamma-1}\) (its formula (14)); the numerical comparison at \(\gamma=2\) concerns finite amplitude. Brechmann and Rendall (2018), Section 2, establish nondegenerate supercritical Hopf for the same normalized system and its global alternatives; they calculate the sign of the first Lyapunov coefficient but not this physical-time complex resonance or the sharp period-sensitivity minimum. Roy, Bhattacharjee and Mallik (2011) use Poincaré–Lindstedt methods to compute frequency shifts in a **different** polynomial Selkov variant \(\dot X=-X+aY+X^2Y,\ \dot Y=b-aY-X^2Y\); its exponent is fixed and its parameterized vector field is not the same real-\(\gamma\) family. Hence that calculation does not imply the present full-exponent minimization. d'Onofrio (2010) studies uniqueness/global attraction of cycles, a different invariant. These antecedents are relevant and are not claimed to be absent. Database and published-record searches did not yield a dominating exact statement; non-retrieval alone cannot certify priority.

## Limitations
Only the local small-cycle branch is analyzed. No global monotonicity in period, no behavior at large amplitude or nonpositive concentrations, and no uniform limit as \(\gamma\downarrow1\) or \(\gamma\to\infty\) is established. The coefficient depends on the specified physical clock, on the chosen substrate observable, and on the first Fourier-harmonic amplitude; it is not invariant under arbitrary time or observable rescaling. Possible unindexed equivalent calculations remain a historical-priority risk. The foundational source is dated March 1968 without a verified exact day; date-only bookkeeping uses the first day of that month as a month-resolution encoding, not a claim of day-level publication.

## References
- E. E. Sel'kov, *Self-Oscillations in Glycolysis 1. A Simple Kinetic Model*, European Journal of Biochemistry **4** (1968), 79–86, DOI: `10.1111/j.1432-1033.1968.tb00175.x` (original full text inspected).
- P. Brechmann and A. D. Rendall, *Dynamics of the Selkov oscillator*, arXiv:`1803.10579` (first posted 28 March 2018), Mathematical Biosciences **306** (2018), 152–159 (full preprint inspected).
- T. Roy, J. K. Bhattacharjee and A. K. Mallik, *Periodic orbits in glycolytic oscillators: From elliptic orbits to relaxation oscillations*, European Physical Journal E **34** (2011), article 19, DOI: `10.1140/epje/i2011-11019-6` (author-uploaded full text inspected).
- A. d'Onofrio, *Uniqueness and global attractivity of glycolytic oscillations suggested by Selkov's model*, Journal of Mathematical Chemistry **48** (2010), 339–346, DOI: `10.1007/s10910-010-9674-6` (abstract and subsequent detailed quotation inspected; full text not obtained).
