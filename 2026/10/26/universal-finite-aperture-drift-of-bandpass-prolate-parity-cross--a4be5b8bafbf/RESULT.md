# Universal finite-aperture drift of bandpass-prolate parity crossings

## Finding
For a fixed separation parameter \(a>0\), let \(0<\varepsilon<a\) and put
\[
E_\varepsilon=[-a-\varepsilon,-a+\varepsilon]\cup[a-\varepsilon,a+\varepsilon].
\]
For \(W>0\), let \(K_{\varepsilon,W}\) be the positive compact low-pass concentration operator on \(L^2(E_\varepsilon)\),
\[
(K_{\varepsilon,W}f)(x)=\int_{E_\varepsilon}
\frac{\sin(W(x-y))}{\pi(x-y)}f(y)\,dy,
\]
with the continuous diagonal value \(W/\pi\). Let \(\lambda_+(\varepsilon,W)\) and \(\lambda_-(\varepsilon,W)\) be the largest eigenvalues in the reflection-even and reflection-odd subspaces, respectively.

**Theorem.** For every fixed \(a>0\) and positive integer \(n\), write \(W_n^0=n\pi/(2a)\). There are \(\delta_n,\varepsilon_n>0\) and a unique real-analytic even function \(\varepsilon\mapsto W_n(\varepsilon)\) on \((-\varepsilon_n,\varepsilon_n)\), with values in \((W_n^0-\delta_n,W_n^0+\delta_n)\), satisfying
\[
\lambda_+(\varepsilon,W_n(\varepsilon))=\lambda_-(\varepsilon,W_n(\varepsilon))
\]
for all \(0<\varepsilon<\varepsilon_n\), and no other equality in that bandwidth neighborhood. The crossing location obeys the **sharp finite-aperture law**
\[
\boxed{W_n(\varepsilon)=\frac{n\pi}{2a}
\left(1+\frac{\varepsilon^2}{6a^2}+O_{a,n}(\varepsilon^4)\right).}
\]
At this bandwidth the largest eigenvalue of the full concentration operator has multiplicity **exactly two**, with one even and one odd eigenfunction. The crossing is transverse:
\[
\left.\frac{\partial}{\partial W}
(\lambda_+-\lambda_-)\right|_{W=W_n(\varepsilon)}
=\frac{4\varepsilon(-1)^n}{\pi}+O_{a,n}(\varepsilon^3).
\]
Thus the maximizing parity switches on passing the crossing, and its finite-width displacement is strictly toward higher bandwidths. The statement is for each *fixed* \(n\); it does not assert a uniform small-width range for arbitrarily growing \(n\).

A more general local expansion, useful for reproducing the calculation, is as follows. Set \(d=2a\), \(k(s)=\sin(Ws)/(\pi s)\), \(k(0)=W/\pi\), \(h_\pm=k(0)\pm k(d)\), and let primes denote derivatives with respect to \(s\). Uniformly for \(W\) in compact subsets of \((0,\infty)\),
\[
\boxed{\lambda_\pm=2\varepsilon h_\pm+
\frac{2\varepsilon^3}{3}\left(k''(0)\pm k''(d)+\frac{k'(d)^2}{h_\pm}\right)+O(\varepsilon^5).}
\]
In particular,
\[
\frac{\lambda_+-\lambda_-}{4\varepsilon}
=k(d)+\frac{\varepsilon^2}{3}
\left(k''(d)-\frac{k'(d)^2k(d)}{k(0)^2-k(d)^2}\right)
+O(\varepsilon^4).
\]
These estimates refer to the top eigenvalue in each parity sector, not to all eigenvalues.

## Assumptions and scope
All integrals use Lebesgue measure, angular frequency \(W\), and the Fourier convention \(\widehat f(\omega)=\int f(x)e^{-i\omega x}\,dx\). The low-pass operator is the orthogonal Fourier projection onto \([-W,W]\), compressed to \(E_\varepsilon\). Since \(a>0\) and \(\varepsilon<a\), the two intervals are disjoint. The existence, uniqueness, derivative and asymptotic statements are local near each fixed positive resonant bandwidth. The two top parity eigenvalues are simple individually for sufficiently small \(\varepsilon\).

## Proof
**1. Parity reduction.** The kernel is real, symmetric, entire in its argument and positive definite because
\[
\langle K_{\varepsilon,W}f,f\rangle
=\frac1{2\pi}\int_{-W}^W\left|\int_{E_\varepsilon}
 f(x)e^{-i\omega x}\,dx\right|^2d\omega.
\]
It commutes with reflection. Via the natural unitary identification of either parity sector with \(L^2([-1,1])\), its restriction becomes
\[
(T_\eta(\varepsilon,W)g)(s)=\varepsilon\int_{-1}^1
\{k(\varepsilon(s-t))+\eta k(d+\varepsilon(s+t))\}g(t)\,dt,
\qquad \eta\in\{+1,-1\}.
\]
The sign in the second kernel is exactly the reflection parity. At \(\varepsilon=0\), divide by \(\varepsilon\) and extend analytically: \(T_\eta/\varepsilon=h_\eta J\), where \(Jg=\int_{-1}^1g(t)dt\). The top eigenvalue of \(h_\eta J\) is the simple eigenvalue \(2h_\eta\) with normalized eigenfunction \(e_0=1/\sqrt2\). Moreover \(h_\eta>0\) for \(W,d>0\), since \(|\sin(Wd)/(Wd)|<1\). All other eigenvalues are zero at the limit. Analytic perturbation of this isolated eigenvalue therefore applies locally in \((\varepsilon,W)\), with a uniform gap for \(W\) near any fixed positive value.

**2. The quadratic perturbation coefficient.** Expanding \(T_\eta/\varepsilon\) gives \(A_0+\varepsilon A_1+\varepsilon^2 A_2+O(\varepsilon^3)\), where the kernels are
\[
A_0:h_\eta,\qquad
A_1:\eta k'(d)(s+t),\qquad
A_2:\frac12k''(0)(s-t)^2+\frac\eta2 k''(d)(s+t)^2.
\]
The first-order Rayleigh coefficient vanishes because \(\langle e_0,A_1e_0\rangle=0\). The direct second-order coefficient equals
\[
\langle e_0,A_2e_0\rangle=\frac23\{k''(0)+\eta k''(d)\}.
\]
Also \(A_1e_0(s)=\eta\sqrt2 k'(d)s\), perpendicular to \(e_0\), and
\[
\frac{\|A_1e_0\|^2}{2h_\eta}
=\frac23\frac{k'(d)^2}{h_\eta}.
\]
These identities follow directly from \(\int_{-1}^1s^2ds=2/3\). The rank-one analytic-eigenvalue perturbation formula gives the displayed \(\varepsilon^3\) coefficient. Reflection \(Ug(s)=g(-s)\) conjugates the analytic kernel family at \(\varepsilon\) to that at \(-\varepsilon\); hence the perturbed eigenvalue of \(T_\eta/\varepsilon\) is even analytic in \(\varepsilon\), making the next remainder \(O(\varepsilon^4)\), or \(O(\varepsilon^5)\) after restoring its prefactor.

**3. Crossing and its displacement.** Subtracting the two parity expansions yields the stated gap formula. At \(W_n^0=n\pi/d\),
\[
k(d)=0,\quad \partial_W k(d)=\frac{(-1)^n}{\pi},\quad
k''(d)=-\frac{2W_n^0(-1)^n}{\pi d^2}.
\]
Dividing the gap by \(4\varepsilon\) extends it analytically and evenly through \(\varepsilon=0\). Its derivative with respect to \(W\) at \((0,W_n^0)\) is nonzero. The analytic implicit function theorem thus gives a unique even analytic root near that point. Differentiating its expansion in \(\varepsilon^2\) yields
\[
W_n(\varepsilon)-W_n^0
=-\frac{\varepsilon^2}{3}
\frac{k''(d)}{\partial_Wk(d)}\bigg|_{W=W_n^0}
+O(\varepsilon^4)
=\frac{2W_n^0\varepsilon^2}{3d^2}+O(\varepsilon^4),
\]
which equals the stated coefficient \(\varepsilon^2/(6a^2)\). Differentiating the gap proves transversality and the parity reversal.

**4. Exact multiplicity in the full space.** In each parity sector the leading eigenvalue is \(2\varepsilon h_\eta+O(\varepsilon^3)\), of order \(\varepsilon\). All other eigenvalues of that sector are \(o(\varepsilon)\) by operator-norm convergence of \(T_\eta/\varepsilon\) to the rank-one limit. Thus at the crossing the two equal, simple sector maxima are exactly the two largest eigenvalues of the whole operator, and their common value has multiplicity two, not higher. This completes the proof.

## Verification
The standalone checker `verify.py` uses Gauss–Legendre Nyström quadrature to diagonalize the independently integrated parity kernels at several bandwidths and widths. It locates the crossings numerically for \(n=1,2,3\), compares against the predicted \(\varepsilon^2\) displacement and checks that the remaining spectrum stays below the leading pair. It also checks the trace identity \(\operatorname{Tr}K_{\varepsilon,W}=4\varepsilon W/\pi\) and transverse parity swaps. The output file `CHECKER_OUTPUT.txt` records actual results. These finite checks support, but do not replace, the analytic proof.

## Relationship to prior work
Slepian and Pollak (1961) established the classical single-interval concentration framework. Morrison (1963) studied eigenfunctions *conditional on degeneracy* of the bandpass kernel. SenGupta–Sun–Jiang–Chen–Mariani (published online in 2011) studied the symmetric disjoint-band concentration operator, proved its time/frequency dual spectral equivalence, and supplied numerical methods. Hogan and Lakey (2013), particularly the discussion below Figure 2, explicitly acknowledge prior observations of bandpass-prolate eigenvalue degeneracies and of odd/even changes in the leading optimizer. Thus **the existence of degeneracies and the underlying operator are not claimed as new**. The present result is a local, all-fixed-mode, **quantitative small-aperture crossing law with its explicit positive second-order drift, uniqueness, transversality and exact leading multiplicity**. The geometrically different detachment perturbation addressed in a published Paley–Wiener concentration record concerns displacement of a small fragment of a connected interval and does not imply the bandwidth crossing law.

## Limitations
The crossing neighborhoods and allowable aperture widths depend on \(a,n\); neither uniformity in growing \(n\) nor a classification of all crossings at finite aperture is claimed. The higher eigenvalue branches may have additional crossings that are not analyzed. No noise/conditioning bound for eigenfunction recovery is provided. The relevant 1963 Morrison full paper was unavailable for material comparison, so a concealed stronger quantitative statement there remains a publication-priority risk; its accessible abstract and the substantive 2012 discussion describe conditional degeneracy/eigenfunction relations, not the stated aperture drift. The result has only self-review, not independent review or validation.

## References
1. D. Slepian and H. O. Pollak, *Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty—I*, Bell System Technical Journal **40** (1961), 43–63, DOI `10.1002/j.1538-7305.1961.tb03976.x`; bibliographic source: `https://www.nokia.com/bell-labs/publications-and-media/publications/prolate-spheroidal-wave-functions-fourier-analysis-and-uncertainty-i/`.
2. J. A. Morrison, *On the eigenfunctions corresponding to the bandpass kernel, in the case of degeneracy*, Quarterly of Applied Mathematics **21** (1963), 13–19, DOI `10.1090/qam/145306` (abstract and secondary discussion inspected; full text inaccessible).
3. I. SenGupta, B. Sun, W. Jiang, G. Chen and M. C. Mariani, *Concentration Problems for Bandpass Filters in Communication Theory over Disjoint Frequency Intervals and Numerical Solutions*, Journal of Fourier Analysis and Applications **18** (2012), 182–210; online 12 October 2011, DOI `10.1007/s00041-011-9197-y`. Accessible full-text rendering: `https://www.researchgate.net/publication/257319946_Concentration_Problems_for_Bandpass_Filters_in_Communication_Theory_over_Disjoint_Frequency_Intervals_and_Numerical_Solutions`.
4. J. A. Hogan and J. D. Lakey, *Letter to the Editor: On the Numerical Evaluation of Bandpass Prolates*, Journal of Fourier Analysis and Applications (online 9 January 2013), DOI `10.1007/s00041-012-9257-y`; open text `https://www.math.ucdavis.edu/~saito/data/ONR15/hogan-lakey_bandpassprolates.pdf`.
5. F. J. Simons, *Slepian functions and their use in signal estimation and spectral analysis* (2009), arXiv `0909.5368` (general context).
