# Sharp mass-budget threshold and balanced design for the second phonon defect mode

## Finding
Consider the infinite nearest-neighbor harmonic chain with uniform spring constant \(k>0\), host mass \(m>0\), and two lighter masses at sites \(0\) and \(d\geq 1\): \(m_0=(1-a)m\) and \(m_d=(1-b)m\), where \(0<a,b<1\). Let \(\lambda=m\omega^2/k\). There is always one simple square-summable normal mode with \(\lambda>4\), and there is a second such mode **if and only if**
\[
\frac{4dab}{a+b}>1.
\]
There are no other point-spectrum modes outside the propagation band \([0,4]\), nor embedded square-summable modes in that band. At equality, the second mode is replaced by a bounded, non-square-summable band-edge resonance at \(\lambda=4\).

With a fixed total mass deficit \(s=a+b\in(0,2)\), a second mode is possible for some allowed distribution **if and only if** \(ds>1\). Whenever it exists, its frequency is maximized uniquely by the balanced allocation \(a=b=s/2\). Thus the cheapest total deficit permitting a second mode has sharp unattained threshold \(s=1/d\).

For each \(d\), as parameters approach any strictly positive threshold pair from the two-mode side, set \(\eta=4dab/(a+b)-1\) and
\[
C(a,b,d)=\frac{4abd^2(a^2+b^2)}{(a+b)^3}.
\]
Then the smaller eigenvalue above the band obeys the quadratic onset law
\[
\lambda_{\mathrm{weak}}-4=\frac{\eta^2}{C(a,b,d)^2}\bigl(1+O(\eta)\bigr).
\]
Here the parameter path is assumed to remain in a compact subset of \((0,1)^2\) and approach a threshold pair. The spatial localization length in lattice spacings is asymptotic to \(C(a,b,d)/\eta\).

## Assumptions and scope
At each integer site \(j\), displacement amplitude \(u_j\) satisfies \(2u_j-u_{j-1}-u_{j+1}=\lambda w_j u_j\), with \(w_0=1-a\), \(w_d=1-b\), and all other \(w_j=1\). Modes are elements of \(\ell^2(\mathbb Z)\), and the two impurities modify masses only, not the common nearest-neighbor spring stiffness. All masses remain positive. The model has no damping or external substrate potential; there is no assertion about nonlinear lattice dynamics, other impurity types, or finite-chain boundary effects.

## Proof
Write \(L u=\lambda W u\), where \((L u)_j=2u_j-u_{j-1}-u_{j+1}\) and \(W=I-aP_0-bP_d>0\). The selfadjoint operator \(W^{-1/2}LW^{-1/2}\) is a finite-rank perturbation of \(L\), so its essential spectrum is \([0,4]\). It is nonnegative. Outside the defects the recurrence has only oscillatory or affine solutions for \(0\leq\lambda\leq4\), including both edges, so no nonzero \(\ell^2\) solution can lie in the band.

For \(\lambda>4\), introduce \(t>0\) by \(\lambda=2+2\cosh t=4\cosh^2(t/2)\). The free Green function is
\[
(\lambda I-L)^{-1}_{ij}=\frac{(-1)^{|i-j|}e^{-t|i-j|}}{2\sinh t}.
\]
The Birman--Schwinger condition reduces exactly to the eigenvalue \(1\) of the positive definite two-by-two matrix
\[
K(t)=\coth(t/2)
\begin{pmatrix}
a&(-1)^d\sqrt{ab}\,e^{-dt}\\
(-1)^d\sqrt{ab}\,e^{-dt}&b
\end{pmatrix}.
\]
Its eigenvalues are
\[
F_{\pm}(t)=\frac{\coth(t/2)}2\left(a+b\pm\sqrt{(a-b)^2+4ab e^{-2dt}}\right).
\]
They decrease strictly as \(t\) increases: for \(\lambda>4\), the positive operator \(\lambda(\lambda I-L)^{-1}\) has derivative \(-L(\lambda I-L)^{-2}\), strictly negative on the two-dimensional impurity subspace. Consequently, both Birman--Schwinger eigenvalue branches are strictly decreasing with \(\lambda\). As \(t\to\infty\), \(F_\pm(t)\to\max(a,b),\min(a,b)<1\). As \(t\downarrow0\), \(F_+(t)\to\infty\) whereas \(F_-(t)\to4dab/(a+b)\). The asserted mode counts and strict transition follow; simplicity follows from the strict ordering \(F_+(t)>F_-(t)\) for finite \(t>0\).

At the critical equality, set \(u_j=(-1)^j v_j\). Take \(v_0=b\), \(v_d=-a\); interpolate linearly between those two values and hold each exterior tail constant. This bounded non-decaying sequence solves the equation at \(\lambda=4\) exactly when \(4dab=a+b\), proving the stated threshold resonance and its non-normalizability.

For fixed \(s=a+b\), put \(p=ab\). For every \(t>0\),
\[
F_-(t)=\frac{\coth(t/2)}2\left(s-\sqrt{s^2-4p(1-e^{-2dt})}\right)
\]
is strictly increasing in \(p\). The product is uniquely maximized, under the admissible fixed-sum constraints, at \(a=b=s/2\), where the band-edge value becomes \(ds\). Since \(F_-\) decreases strictly with \(\lambda\), its crossing level \(\lambda_{\mathrm{weak}}\), when present, is uniquely maximized by that balanced choice. The sharp existence and mass-budget statements follow.

Finally, expansion at \(t=0\) yields, uniformly near any positive threshold pair,
\[
F_-(t)=\frac{4dab}{a+b}
-\frac{4abd^2(a^2+b^2)}{(a+b)^3}\,t+O(t^2).
\]
Solving \(F_-(t)=1\) gives \(t=\eta/C+O(\eta^2)\). Because \(\lambda-4=2(\cosh t-1)=t^2+O(t^4)\), the quadratic gap law follows. Exterior eigenvectors decay as \(e^{-t|j|}\), giving the localization-length statement.

## Verification
A standalone numerical checker constructs a finite large-section generalized mass-weighted chain, compares its above-band eigenvalues with the exact two-by-two Birman--Schwinger roots over varying unequal impurities and spacings, checks the predicted mode-count inequalities, and tests strict balanced-allocation enhancement and near-threshold scaling. Finite truncations may miss extremely weak bound states; the universal theorem is established by the analytic proof above, not by finite tests.

## Relationship to prior work
The classical defect-Green-function theory of Montroll and Potts (1955), the transfer-matrix investigation of disordered chains by Hori and Asahi (1957), and later studies of one- and two-impurity granular chains provide the spectral foundation. The present statement concerns the exact **joint unequal-mass, separation, fixed-total-deficit optimization, and critical-onset** classification in a uniform-spring infinite chain; it does not claim to originate impurity bound states or their Green-function description. Theocharis and collaborators (2009) report one-versus-two defect modes in a physically different granular contact model, while Man and collaborators (2012) provide approximate few-site frequency descriptions and measurements. Luo (2016) treats a single mass impurity and finite-chain boundary effects. The older broad transfer-matrix treatments may contain equivalent or stronger special results; see the explicit priority limitation below.

## Limitations
Historical priority is provisional. Complete primary text was unavailable for the 1955 Montroll--Potts and 1957 Hori--Asahi articles, so an equivalent exact two-defect budget/equality theorem in those papers cannot be excluded. Their general Green-function and transfer-matrix techniques might subsume parts of the present calculation, and no exhaustive independence or literature-completeness claim is made. The mode-count theorem is for strictly positive masses, two light defects, a uniform-spring infinite chain and square-summable modes. The quadratic asymptotic excludes degenerating threshold paths where either defect strength tends to zero. No independent validation has been performed.

## References
1. E. W. Montroll and R. B. Potts, *Effect of Defects on Lattice Vibrations*, Phys. Rev. **100** (1955), 525--543, DOI: 10.1103/PhysRev.100.525.
2. J. Hori and T. Asahi, *On the Vibration of Disordered Linear Lattice*, Prog. Theor. Phys. **17** (1957), 523--542, DOI: 10.1143/PTP.17.523.
3. G. Theocharis et al., *Localized Breathing Modes in Granular Crystals with Defects*, arXiv:0906.4094 (2009), DOI: 10.1103/PhysRevE.80.066601.
4. Y. Man et al., *Defect Modes in One-dimensional Granular Crystals*, arXiv:1103.2483 (2011), DOI: 10.1103/PhysRevE.85.037601.
5. Q. Luo, *Local vibrational mode of impurity in a monatomic linear chain under open and periodic boundary conditions*, arXiv:1607.06946 (2016).
