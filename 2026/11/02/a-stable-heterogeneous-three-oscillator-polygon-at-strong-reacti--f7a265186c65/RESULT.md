# A stable heterogeneous three-oscillator polygon at strong reactive coupling

## Finding

For a three-node cubic Stuart–Landau network with strictly increasing, *linearly spaced* growth rates, a noncollinear zero-mean phase-locked triangle can be orbitally exponentially attracting at finite complex coupling, although its weakly coupled continuation is transversely unstable. The exact stable example below has a rational characteristic polynomial and strictly positive exact Routh–Hurwitz minors. Thus three active oscillators already suffice for an attracting zero-mean polygon in this model; no neutral polygonal shape mode is present beyond common rotation.

## Assumptions and scope

For \(j=1,2,3\), let

\[
\dot z_j=(\beta_j+i\omega-|z_j|^2)z_j+C\sum_{\ell\ne j}(z_\ell-z_j),\qquad z_j\in\mathbb C,
\]

with \(\omega=4\), \((\beta_1,\beta_2,\beta_3)=(7/4,9/4,11/4)\), and \(C=1/4+i\). Define

\[
w=(1,(-1+i\sqrt{23})/4,(-3-i\sqrt{23})/4).
\]

Then \(z_j(t)=e^{it}w_j\) is an exact nonconstant periodic solution with \(z_1+z_2+z_3=0\). Its orbit is exponentially asymptotically stable *modulo collective phase rotation*, not a stationary fixed point in the original variables. All three amplitudes are positive and unequal.

For the continuation, keep \(\omega\) and \(\beta_j\) fixed and put \(C(\varepsilon)=\varepsilon(1/4+i)\), \(0<\varepsilon\le1\). Every \(\varepsilon\) has a noncollinear zero-mean relative equilibrium with amplitudes \(r_j(\varepsilon)=\sqrt{\beta_j-3\varepsilon/4}\) and angular speed \(4-3\varepsilon\). At sufficiently small positive \(\varepsilon\), each such triangle has two unstable transverse eigenvalues (counting algebraic multiplicity); at \(\varepsilon=1\), the specified representative has none.

## Proof

**1. Exact orbit.** The three vectors have zero sum and squared moduli \(1,3/2,2\). Since \(\beta_j-3/4=|w_j|^2\), the mean-field representation of the vector field gives \(\dot z_j=i(\omega-3C_i)z_j=iz_j\). This verifies the orbit and the exact closure constraint.

**2. Full-amplitude Jacobian.** In the co-rotating frame \(u_j=e^{-it}z_j\), the dynamics is

\[
\dot u_j=(\beta_j-3/4-|u_j|^2)u_j+C\sum_{k=1}^3u_k.
\]

At \(u=w\), complex linearization acts as

\[
\delta\dot u_j=-|w_j|^2\delta u_j-w_j^2\overline{\delta u_j}+C\sum_{k=1}^3\delta u_k.
\]

Expand in coordinates \((\Re u_1,\Im u_1,\Re u_2,\Im u_2,\Re u_3,\Im u_3)\). Direct exact differentiation and determinant expansion give

\[
\det(sI-J)=\frac{s}{64}(64s^5+480s^4+1556s^3+3544s^2+5325s+3519).
\]

One zero eigenvector is \(iw\) (collective phase). The quotient by \(s\) is monic of degree five and has the following five leading Hurwitz determinants, in increasing order:

\[
\frac{15}{2},\quad \frac{4063}{32},\quad\frac{353677}{128},\quad\frac{2996769579}{32768},\quad\frac{10545632148501}{2097152}.
\]

All are strictly positive. By the Routh–Hurwitz criterion, its five roots satisfy \(\Re s<0\); the root at zero is simple. Normal hyperbolicity of the periodic orbit under the phase symmetry proves exponential orbital stability locally.

**3. Noncollinear continuation.** At coupling \(C(\varepsilon)\), the nonnegative squared amplitudes are \(r_j^2=\beta_j-3\varepsilon/4\). On \([0,1]\), \(r_1^2\ge1\), \(r_2^2=r_1^2+1/2\), and \(r_3^2=r_1^2+1\). Therefore \(r_3^2=r_2^2+1/2<r_2^2+r_1^2<(r_2+r_1)^2\). The largest side is shorter than the sum of the other two, so there are noncollinear triangles \(\sum_j r_je^{i\theta_j}=0\) for every \(\varepsilon\). Such triangles depend continuously on \(\varepsilon\), up to common rotation and reflection, and are exact relative equilibria.

**4. Weak-coupling instability.** At zero coupling the radial Floquet exponents are \(-2\beta_j<0\) and the three phase exponents vanish. For \(\varepsilon\downarrow0\), the first-order perturbation of the phase eigenvalues is \(\varepsilon\) times the spectrum of the real \(3\times3\) matrix

\[
T_{jk}=\frac{r_k(0)}{r_j(0)}\Re\big[(1/4+i)e^{i(\theta_k(0)-\theta_j(0))}\big].
\]

The zero-mean identity gives \(T\mathbf1=0\). The matrix is diagonally similar to \(K_{jk}=\Re[(1/4+i)e^{i(\theta_k-\theta_j)}]\), which has rank at most two. Its trace is \(3/4\), while its two nonzero eigenvalues have product

\[
\big((1/4)^2+1\big)\sum_{1\le j<k\le3}\sin^2(\theta_j(0)-\theta_k(0))>0.
\]

Noncollinearity makes the last inequality strict. The two roots of the resulting quadratic thus both have positive real parts: their sum is positive and their product is positive. Standard perturbation of the normally attracting radial directions gives two eigenvalues with positive real part for all sufficiently small \(\varepsilon>0\). This is genuinely distinct from the stable endpoint \(\varepsilon=1\). No uniqueness or nondegeneracy of the intervening stability transition is asserted.

## Verification

Run `python3 verify.py` with Python 3 and SymPy installed. It reconstructs the six-by-six real Jacobian by differentiating the complete co-rotating nonlinear vector field, checks the exact orbit and characteristic polynomial, and evaluates all five leading Hurwitz determinants in rational arithmetic. It does not use numerical eigensolvers or finite sampling. The weak-coupling statement and nonlinear orbital conclusion use the analytic arguments above.

## Relationship to prior work

Zhao and Uchida (2026, arXiv:2610.08239v1) derive polygonal zero-mean solutions and their general Jacobian, and report that the triangular sector is unstable *within their sampled eight-oscillator, linearly spaced-growth parameter plane*. Those existence and linearization mechanisms are prior results. The present result is a distinct **three-oscillator** analytic parameter witness, with all nodes active and with a full exact Hurwitz stability certificate and weak-versus-strong comparison. It does not contradict the reported eight-node sample.

León and Pazó (2020, arXiv:2006.02159) establish stability theory near incoherent states for **identical** Stuart–Landau oscillators, and Berner et al. (2021, arXiv:2105.06694) provide generalized-splay stability theory for phase oscillator networks. Neither inspected result supplies this full-amplitude, *heterogeneous*, linearly spaced three-node stable certificate; the phase-only small-coupling trace calculation is credited as a familiar splay mechanism, not claimed independently new.

## Limitations

Only local orbital stability is established, not global attraction or basin size. The location, type and number of stability-changing transitions along the coupling homotopy remain undetermined. The result is a single explicit positive-parameter witness and its open persistence neighborhood, not a complete stability region. General historical priority beyond inspected primary and search materials has not been exhaustively established. No independent audit has been performed.

## References

- L. Zhao and N. Uchida, *Heterogeneity-induced chaos in globally coupled Stuart–Landau oscillators*, arXiv:2610.08239v1 (first posted 2026-10-06), https://arxiv.org/html/2610.08239v1, especially Sections 2 and 5.
- I. León and D. Pazó, *Quasi phase reduction of all-to-all strongly coupled \(\lambda\)-\(\omega\) oscillators near incoherent states*, arXiv:2006.02159 (2020), https://arxiv.org/abs/2006.02159, Sections I, III–V.
- R. Berner, S. Yanchuk, Y. Maistrenko and E. Schöll, *Generalized splay states in phase oscillator networks*, arXiv:2105.06694 (2021), https://arxiv.org/abs/2105.06694.
