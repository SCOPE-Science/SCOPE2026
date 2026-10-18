# Exact Airy folds and universal quadratic Doppler-threshold census for quartic-chirped Gaussian ambiguity

## Finding

Let \(f_\lambda(t)=2^{1/4}\exp(-\pi t^2+i\lambda t^4)\), with real \(\lambda\ne0\), and use the symmetric ambiguity convention
\[
A_\lambda(\tau,\nu)=\int_{\mathbb R}f_\lambda(t+\tau/2)\overline{f_\lambda(t-\tau/2)}e^{-2\pi i\nu t}\,dt.
\]
Set \(\kappa=|\lambda|\). Let \(0<u_1<u_2<\cdots\) be all positive zeros of the Airy function on the negative ray, i.e. \(\operatorname{Ai}(-u_j)=0\). For each \(j\ge1\) define, for \(q>0\),
\[
V_j(q)=\frac{\kappa q^3}{2\pi}+\frac{\pi}{6\kappa q}+\frac{u_j(12\kappa q)^{1/3}}{2\pi}.
\]
Then the *entire real zero set* of the ambiguity function is the disjoint union
\[
\boxed{\;\{(s q,\,s\operatorname{sgn}(\lambda)V_j(q)):q>0\}:\quad s\in\{-1,1\},\quad j\ge1.\;}
\]
Every zero is transverse to the Doppler direction (\(\partial_\nu A_\lambda\ne0\)). No zero lies on either coordinate axis or in the two quadrants \(\lambda\tau\nu<0\). Each of these disjoint real-analytic zero curves is a proper embedded curve, with Doppler magnitude tending to infinity at both ends.

Each \(V_j\) has a unique nondegenerate global minimum at \(q_j(\kappa)>0\). The values \(m_j(\kappa)=V_j(q_j(\kappa))\) are strictly increasing and unbounded. For any nonzero Doppler frequency \(\nu\), the *exact number of zero delays* (on the uniquely permitted side of zero delay) equals
\[
\boxed{\;2\#\{j:m_j(\kappa)<|\nu|\}+\#\{j:m_j(\kappa)=|\nu|\}.\;}
\]
Thus every threshold is a nondegenerate fold of the level sets of a smooth nodal curve, never a singularity of the two-variable zero set.

The high-index fold thresholds and their minimizing delays obey the *chirp-independent* asymptotic constants
\[
\boxed{\;m_j(\kappa)\sim\frac{2}{3^{1/4}}\sqrt j,\qquad
\kappa q_j(\kappa)\sim\frac{\pi}{3^{3/4}\sqrt j}.\;}
\]
In particular,
\[
\boxed{\;\#\{j:m_j(\kappa)\le R\}\sim\frac{\sqrt3}{4}R^2\quad(R\to\infty),\;}
\]
for *every fixed* \(\kappa>0\). At fixed nonzero delay \(\tau\), the number of Doppler zeros on the permitted ray with magnitude at most \(R\) instead satisfies
\[
\boxed{\;\#\{j:V_j(|\tau|)\le R\}\sim
\frac{2\sqrt{2\pi}}{3\sqrt{3\kappa|\tau|}}R^{3/2}.\;}
\]
The different exponents reflect the accumulation of increasingly small-delay fold minima.

## Assumptions and scope

The signal is in \(L^2(\mathbb R)\) and has unit norm because \(\sqrt2\int_{\mathbb R}e^{-2\pi t^2}\,dt=1\). We use the real-variable ambiguity function, not a spectrogram or Wigner distribution, with the displayed \(2\pi\)-frequency convention. All zero and counting statements concern real \((\tau,\nu)\). Statements with \(j\to\infty\) hold for each fixed nonzero chirp strength; no uniformity as \(\kappa\downarrow0\) is asserted.

The numerical Airy roots are not inputs to the proof beyond classical facts: \(\operatorname{Ai}\) has simple negative real zeros, and \(u_j\sim(3\pi j/2)^{2/3}\). These are standard Airy-function theorems [4].

## Proof

**1. Exact reduction.** Expanding the quartic phase and the two Gaussian factors gives
\[
A_\lambda(\tau,\nu)=\sqrt2\,e^{-\pi\tau^2/2}\int_{\mathbb R}
  \exp\left(-2\pi t^2+i\frac{b t^3}{3}+ict\right)dt,
\quad b=12\lambda\tau,\quad c=\lambda\tau^3-2\pi\nu.
\]
For \(b\ne0\), let \(\alpha=\operatorname{sgn}(b)|b|^{1/3}\). We use the Gaussian-damped Airy transform identity, valid for every \(a>0\) and nonzero real \(b\):
\[
\int_{\mathbb R}e^{-a t^2+i b t^3/3+ict}\,dt
=\frac{2\pi}{|\alpha|}
\exp\!\left(\frac{2a^3}{3b^2}+\frac{ac}{b}\right)
\operatorname{Ai}\!\left(\frac{c+a^2/b}{\alpha}\right).
\tag{1}
\]
For completeness, in the tempered-distribution sense at \(a=0\), the left side is \((2\pi/|\alpha|)\operatorname{Ai}(c/\alpha)\) by the Airy Fourier representation. Multiplication by \(e^{-at^2}\) corresponds to applying the heat semigroup \(e^{a\partial_c^2}\). The elementary identity
\[
e^{s\partial_x^2}\operatorname{Ai}(x)
=e^{2s^3/3+sx}\operatorname{Ai}(x+s^2),\qquad s>0,
\]
follows by differentiation, \(\operatorname{Ai}''(x)=x\operatorname{Ai}(x)\), and uniqueness of the heat evolution of tempered initial data. Apply it with \(s=a/\alpha^2\) and \(x=c/\alpha\) to obtain (1), including the sign of \(b\). This also makes the Fourier normalization explicit. With \(a=2\pi\),
\[
A_\lambda(\tau,\nu)=\frac{2\sqrt2\pi}{|b|^{1/3}}
\exp\!\left(-\frac{\pi\tau^2}{2}+\frac{16\pi^3}{3b^2}+\frac{2\pi c}{b}\right)
\operatorname{Ai}\!\left(\frac{c+4\pi^2/b}{\operatorname{sgn}(b)|b|^{1/3}}\right).
\tag{2}
\]
The exponential prefactor is strictly positive. At zero delay, direct Gaussian integration gives \(A_\lambda(0,\nu)=e^{-\pi\nu^2/2}>0\).

**2. Exhaustive zero geometry.** As the argument of \(\operatorname{Ai}\) in (2) is real and affine in \(\nu\), its zeros occur exactly when that argument is \(-u_j\). Solving for \(\nu\) gives the displayed curves. For \(\lambda>0\), \(\tau>0\) the three summands defining \(V_j\) are strictly positive; conjugation and parity give the other cases. Classical simplicity of Airy zeros, together with the nonzero coefficient of \(\nu\) inside (2), yields \(\partial_\nu A_\lambda\ne0\) at every zero. Since \(u_{j+1}>u_j\), the branches are pointwise strictly ordered and cannot intersect. Each tends to infinite Doppler magnitude as \(q\to0^+\) or \(q\to\infty\), hence is proper. This proves the exhaustive nodal description without extending numerical root searches to infinity.

**3. Exactly one fold on every branch.** Differentiating gives
\[
q^2 V_j'(q)
=\frac{3\kappa q^4}{2\pi}+
\frac{u_j(12\kappa)^{1/3}q^{4/3}}{6\pi}
-\frac{\pi}{6\kappa}=:H_j(q).
\]
The function \(H_j\) is strictly increasing from a negative value to infinity, so has exactly one positive root \(q_j\). At that root, \(V_j''(q_j)=H_j'(q_j)/q_j^2>0\). Every level strictly above \(m_j\) therefore intersects that branch twice, equality once, and every smaller level not at all. The minima are strictly ordered: at a minimizer of \(V_{j+1}\), the pointwise inequality \(V_{j+1}>V_j\ge m_j\) implies \(m_{j+1}>m_j\). The nonvanishing Doppler derivative from step 2 shows that these folds are not singularities of the planar nodal curves.

**4. Sharp universal minima.** Put \(u=u_j\) and \(r=\kappa q\). Then
\[
V_j(q)=\frac{r^3}{2\pi\kappa^2}
+\frac{\pi}{6r}+\frac{u\,12^{1/3}r^{1/3}}{2\pi}.
\]
Set \(r=u^{-3/4}y\). Dividing by \(u^{3/4}\) leaves
\[
\frac{\pi}{6y}+\frac{12^{1/3}y^{1/3}}{2\pi}
+\frac{u^{-3}y^3}{2\pi\kappa^2}.
\tag{3}
\]
The first two terms are coercive at both ends of \((0,\infty)\) and have the unique minimizer
\[
y_0=\frac{\pi^{3/2}}{12^{1/4}},
\qquad\min_{y>0}\left(\frac{\pi}{6y}+\frac{12^{1/3}y^{1/3}}{2\pi}\right)
=\frac{2\pi}{3y_0}.
\]
The positive last term in (3) vanishes uniformly on compact subsets for fixed \(\kappa\). Comparing the minimizer with \(y_0\), then using coercivity to confine minimizers to a compact interval, proves \(\kappa q_j\sim y_0u_j^{-3/4}\) and \(m_j\sim(2\pi/(3y_0))u_j^{3/4}\). The classical Airy zero law \(u_j\sim(3\pi j/2)^{2/3}\) yields exactly the two displayed constants. Since \(m_j\) is strictly increasing, inversion yields the quadratic threshold census. No extrapolation from finitely many roots is used.

**5. Doppler zeros at fixed delay.** With \(q>0\) fixed, the leading dependence \(V_j(q)=u_j(12\kappa q)^{1/3}/(2\pi)+O_{\kappa,q}(1)\) and the Airy counting asymptotic \(\#\{j:u_j\le U\}\sim (2/(3\pi))U^{3/2}\) give the last formula.

## Verification

A standalone checker (`checker.py`) evaluates the original Gaussian-cubic Fourier integral independently of the closed Airy expression in six high-precision cases, verifies 75 critical points by the derivative equation and local inequalities, checks zeros and quadrant signs, and compares the large-index constants for three distinct chirp strengths. Execute `python checker.py` with `mpmath` and `scipy`. A saved output file records the actual result. The analytic arguments in steps 1–5, not the finite tests, prove the unbounded classification and asymptotics.

## Relationship to prior work

Babusci, Dattoli and Sacchetti [1] develop the Airy Fourier transform underlying (1); that transform is not claimed as new. Balazs, Bayer, Jaillet and Søndergaard [2] study how phase-space transform zeros affect local phase behavior, not quartic-Gaussian ambiguity thresholds. Moore and Filip [3] establish a considerably broader Airy-transform method for *Wigner functions* after cubic or quartic phase gates, including Gaussian inputs. Their Wigner formula is important antecedent and makes an Airy representation of related nonlinear-phase quantities plausible; their inspected statements do not classify the zero set of this ambiguity function, show the unique Doppler-fold minima, or derive the universal \(\sqrt3/4\) counting coefficient. The Airy root facts in [4] are classical. These inputs are combined here with a direct independent transform calculation and exact minimization to give a global nodal theorem for the ambiguity function itself.

## Limitations

Only real zeros and the stated even quartic-phase Gaussian family are classified; the full complex-frequency zero set and general non-Gaussian amplitude envelopes are not treated. The high-index asymptotics are for fixed nonzero strength, not uniform as that strength tends to zero. No physical detection guarantee follows from mathematical zeros. This is a mathematical derivation and self-review, not an independently audited or certified priority claim. Although targeted literature and mathematical-record comparisons did not reveal an equivalent global ambiguity-threshold theorem, older radar or optical literature could contain one; in particular [3] creates a substantive neighboring-results priority risk.

## References

[1] D. Babusci, G. Dattoli, D. Sacchetti, *The Airy transform and the associated polynomials*, arXiv:1002.2517, first public version 2010-02-12. https://arxiv.org/abs/1002.2517

[2] P. Balazs, D. Bayer, F. Jaillet, P. Søndergaard, *The Pole Behaviour of the Phase Derivative of the Short-Time Fourier Transform*, arXiv:1103.0409, first public version 2011-03-02. https://arxiv.org/abs/1103.0409

[3] D. W. Moore, R. Filip, *Nonlinear Phase Gates as Airy Transforms of the Wigner Function*, arXiv:2504.04851v1, first public version 2025-04-07. https://arxiv.org/html/2504.04851v1

[4] NIST Digital Library of Mathematical Functions, §9.9 (Airy zeros, simplicity and asymptotic expansions). https://dlmf.nist.gov/9.9
