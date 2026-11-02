# A sharp nonattained gain-recovery window in a four-waveguide chain

## Finding

For every positive pair of coupling strengths \(a,b\), consider the four-mode, nearest-neighbor balanced-gain/loss propagation matrix
\[
H_\gamma=\begin{pmatrix}
 i\gamma&a&0&0\\
 a&0&b&0\\
 0&b&0&a\\
 0&0&a&-i\gamma
\end{pmatrix},\qquad \gamma\geq0.
\]
Here the gain and loss are confined to opposite **end** modes; interior modes are passive. Define the coupling budget \(J=2a+b\), the ratio \(t=a^2/b^2\), and, for \(t>2\),
\[
q=\sqrt{t(t-2)},\qquad x_\pm=2t-1\pm2q.
\]
A **genuine gain-induced symmetry recovery** means that, as \(\gamma\) increases, an open interval with four distinct real eigenvalues is followed by an open interval with nonreal eigenvalues, then by another open interval with four distinct real eigenvalues. This occurs **if and only if**
\[
2<t<1+\sqrt2.
\]
In precisely that range the three successive open intervals and the final loss of reality are
\[
\begin{array}{c|c}
 0<\gamma<b\sqrt{x_-}&\text{four distinct real eigenvalues}\\
 b\sqrt{x_-}<\gamma<b\sqrt{x_+}&\text{nonreal eigenvalues}\\
 b\sqrt{x_+}<\gamma<bt&\text{four distinct real eigenvalues}\\
 \gamma>bt&\text{nonreal eigenvalues}.
\end{array}
\]
At the three transition gains the spectrum is real but defective (except the last transition is a zero-energy double eigenvalue); open-interval statements avoid conflating reality with diagonalizability. The **recovered gain-width** is exactly
\[
W(a,b)=bt-b\sqrt{2t-1+2\sqrt{t(t-2)}}.
\]
Among all positive couplings with prescribed budget \(J=2a+b\) that genuinely exhibit recovery, the exact **sharp, nonattained bound** is
\[
\boxed{\quad 0<W(a,b)<J\,\frac{2-\sqrt3}{2\sqrt2+1}.\quad}
\]
The optimal constant is approximately \(0.0699893673564\). There is no maximizing recovered design: the supremum is approached precisely as \(a^2/b^2\downarrow2\), at which the intervening broken-symmetry interval collapses to a single exceptional gain and no genuine recovery survives. At the other limit \(a^2/b^2\uparrow1+\sqrt2\), the recovered interval closes at a fourth-order exceptional point. Thus an appreciable separated recovery phase requires a strict robustness sacrifice.

## Assumptions and scope

The matrix describes an ideal linear reciprocal four-mode chain with positive real couplings \(a,b,a\) and balanced end gain/loss \(+i\gamma,-i\gamma\). No direct non-nearest-neighbor links, detunings, material dispersion, or nonlinear gain saturation are present. A real spectrum means four eigenvalues counted with algebraic multiplicity are real. A **real-simple interval** additionally requires four distinct eigenvalues. The design budget is the sum \(J=2a+b\) of all three positive coupling magnitudes; it is not a constraint on optical pump power. All statements quantify over every \(a,b>0\) and \(\gamma\geq0\) in this exact model.

## Proof

**1. Characteristic reduction.** Direct continuant expansion gives
\[
\det(\lambda I-H_\gamma)=\lambda^4+(\gamma^2-2a^2-b^2)\lambda^2+a^4-b^2\gamma^2.
\]
For \(u=\lambda^2/b^2\) and \(x=\gamma^2/b^2\), this becomes
\[
P(u)=u^2-(2t+1-x)u+(t^2-x),
\]
with quadratic discriminant
\[
\mathscr D(x)=(x-(2t-1))^2+4t(2-t).
\]
The four mode eigenvalues are real and distinct exactly when \(P\) has two strictly positive distinct roots, equivalently \(\mathscr D(x)>0\), \(2t+1-x>0\), and \(t^2-x>0\).

**2. Reentry is possible only in one ratio interval.** For \(0<t<2\), the discriminant is strictly positive at every nonnegative \(x\); a gain-induced complex interval cannot precede a later real-simple interval. At \(t=2\), the discriminant is \((x-3)^2\), touching zero at a single gain, so there is no open complex interval before the final loss of reality. For \(t>2\), the discriminant is negative precisely on \((x_-,x_+)\), where \(x_\pm=2t-1\pm2\sqrt{t(t-2)}\), and positive immediately outside. On the upper branch \(x>x_+\), both roots of \(P\) are positive exactly when \(x<\min\{2t+1,t^2\}\). Writing \(q=\sqrt{t(t-2)}\), the identities
\[
2t+1-x_+=2(1-q),\qquad t^2-x_+=(1-q)^2
\]
show that a nonempty upper real-simple interval exists if and only if \(q<1\), i.e. \(2<t<1+\sqrt2\). In this range \(t^2<2t+1\), so the interval ends exactly at \(x=t^2\). Similarly, below \(x_-\) the two roots are positive, because \(2t+1-x_-=2(1+q)>0\) and \(t^2-x_-=(1+q)^2>0\). This gives every open spectral phase and the exact recovered width \(W=b(t-\sqrt{x_+})\).

**3. Sharp budget bound.** Normalize by \(J=b(2\sqrt t+1)\). For \(2<t<1+\sqrt2\), \(0<q<1\) and
\[
\frac{W}{J}
=\frac{t-\sqrt{x_+}}{2\sqrt t+1}
=\frac{(1-q)^2}{(t+\sqrt{x_+})(2\sqrt t+1)}.
\]
As \(t\) increases over this interval, \(q\) and \(x_+\) strictly increase. Thus the numerator is strictly decreasing and both factors in the denominator strictly increase. The ratio strictly decreases, and its endpoint limits are
\[
\lim_{t\downarrow2}\frac{W}{J}=\frac{2-\sqrt3}{2\sqrt2+1},\qquad
\lim_{t\uparrow1+\sqrt2}\frac{W}{J}=0.
\]
The first endpoint is excluded by the definition of genuine recovery. This proves strictness, sharpness, and nonattainment.

**4. Exceptional endpoints and robustness tradeoff.** For any eigenvalue, the nonzero nearest-neighbor couplings recursively determine all components of an eigenvector from its first component, so its geometric eigenspace has dimension at most one. Every repeated root is therefore defective. At \(t=2\), \(x=3\), the characteristic polynomial equals \((\lambda^2-b^2)^2\) and the intermediate complex-gain interval has zero length. At \(t=1+\sqrt2\), \(x=t^2=x_+\), it is \(\lambda^4\), producing one Jordan block of order four. Moreover, writing \(B=b(\sqrt{x_+}-\sqrt{x_-})\) for the broken-phase gain-width, Taylor expansion as \(t\downarrow2\) gives the dimensionless Pareto-edge law
\[
\frac{W}{J}=\frac{2-\sqrt3}{2\sqrt2+1}-\frac{B}{2J}+O\!\left(\frac{B^2}{J^2}\right).
\]
This quantifies the first-order loss of recovered-window robustness when a genuinely nonzero broken-symmetry window is introduced.

## Verification

The standalone program `verify.py` checks the characteristic determinant and discriminant symbolically; confirms both factorization identities and the endpoint exceptional polynomials; numerically diagonalizes the original complex matrix independently of the quadratic root criterion on samples from each open phase; checks strictness and monotonicity of the normalized recovery width; and tests the Pareto-edge expansion. Run it with `python verify.py` in the extracted package directory. No infinite claim relies on finite tests; monotonicity and the spectral classifications are proved above.

## Relationship to prior work

Liang, Scott and Joglekar (2014, arXiv:1402.2544) established gain-induced restoration in finite lattices with **two oscillatory gain/loss potentials** and evaluated corresponding phase diagrams. Their accessible original text uses a site-dependent Aubry–André potential, not the present reciprocal four-mode, three-link chain under a fixed coupling-sum budget. Rivolta and Maes (2015, doi:10.1364/OL.40.003922) identified recovery in a **four-mode transversal gain/loss configuration** and analyzed coupling ratios; the accessible author/publisher preview specifies two gain-carrying upper modes and two lossy lower modes, unlike the opposite-end-only gain/loss matrix here. The full Rivolta–Maes article could not be independently inspected, so whether any analogous normalized robustness bound occurs in that paper remains an explicit priority risk. Phang and colleagues (2016, doi:10.1038/srep20499) analyzed gain/loss modulation and termination modes in finite photonic resonator chains, not the specified fixed-budget sharp supremum. The new quantitative conclusion is the complete reentry existence interval together with the **sharp nonattained ratio bound on the recovered gain-width for this explicit model**; the general phenomenon of restoration is acknowledged as established.

## Limitations

The result does not claim discovery of gain-induced symmetry restoration in general, and it does not establish priority over all historical non-Hermitian coupled-mode studies. At transition gains the real spectrum can be defective, with polynomial-in-propagation factors; hence the real-spectrum statement must not be interpreted as bounded propagation at exceptional points. The sharp bound uses the declared sum-of-couplings budget; alternate power, geometry, loss, and fabrication constraints could yield different optima. Optical Maxwell dispersion, saturation and sensitivity to asymmetry beyond this model are not treated.

## References

1. C. Liang, D. D. Scott and Y. N. Joglekar, *PT-restoration via increased loss-gain in PT-symmetric Aubry–André model*, arXiv:1402.2544, first submitted 2014-02-11. https://arxiv.org/abs/1402.2544
2. N. X. A. Rivolta and B. Maes, *Symmetry recovery for coupled photonic modes with transversal PT symmetry*, Optics Letters 40 (2015), 3922–3925. https://doi.org/10.1364/OL.40.003922
3. S. Phang et al., *Localized Single Frequency Lasing States in a Finite Parity-Time Symmetric Resonator Chain*, Scientific Reports 6 (2016), 20499. https://doi.org/10.1038/srep20499
