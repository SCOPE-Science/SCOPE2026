# Rigidity and Bessel interlacing of Fourier zeros of concentric annuli

## Finding

For every integer dimension \(d\ge2\) and every inner-radius ratio \(0<r<1\), the Fourier transform of the annulus
\[\mathcal A_{d,r}=\{x\in\mathbb R^d:r<|x|<1\}\]
has only simple positive radial zeros, and **exactly one** in each interval between successive positive zeros of \(J_{d/2-1}\). There are no other positive radial zeros. Moreover each indexed zero moves real-analytically as the inner radius varies, connecting the \(J_{d/2}\) zero of the solid ball to the \(J_{d/2-1}\) zero of the limiting sphere. The radial zero count is \(R/\pi+O_d(1)\), with an error uniform over all \(0<r<1\).

The dimension restriction is sharp: for the one-dimensional shell \((-1,-r)\cup(r,1)\), positive Fourier zeros of multiplicity two occur infinitely often exactly when the reduced rational expression for \((1+r)/(1-r)\) has odd numerator and even denominator. Otherwise all positive Fourier zeros are simple.

## Assumptions and scope

Use \(\widehat f(\xi)=\int_{\mathbb R^d}f(x)e^{-i\xi\cdot x}\,dx\) and \(t=|\xi|\). Set \(\nu=d/2\); for \(d\ge2\), \(\nu\ge1\). Let \(j_{\alpha,k}\) denote the \(k\)-th strictly positive zero of the Bessel function \(J_\alpha\) for \(\alpha\ge0\). For fixed \(0<r<1\), define
\[G_{\nu,r}(t)=J_\nu(t)-r^\nu J_\nu(rt),\qquad t>0.\]
The exact annular transform is
\[\widehat{\mathbf1_{\mathcal A_{d,r}}}(\xi)=(2\pi)^\nu t^{-\nu}G_{\nu,r}(t),\qquad t>0.\]
Its value at \(t=0\) is \(\pi^\nu(1-r^{2\nu})/\Gamma(\nu+1)>0\). Hence nonzero real Fourier zeros correspond precisely to positive roots of \(G_{\nu,r}\), reflected as concentric spheres in frequency space. A radial root is *simple* when its first derivative in \(t\) is nonzero; this means that the Fourier-zero sphere is a smooth regular level set.

The main statements, valid for all integers \(d\ge2\), all \(r\in(0,1)\), and every integer \(k\ge1\), are
\[
 j_{\nu-1,k}<\tau_k(r)<j_{\nu-1,k+1},
 \qquad G_{\nu,r}(\tau_k(r))=0,
\]
with exactly one root in each displayed interval and none below \(j_{\nu-1,1}\). Every root is simple, and
\[
 \lim_{r\downarrow0}\tau_k(r)=j_{\nu,k},
 \qquad \lim_{r\uparrow1}\tau_k(r)=j_{\nu-1,k}.
\]
The standard zero asymptotics give, uniformly in \(r\in(0,1)\),
\[N_{d,r}(R):=\#\{k:\tau_k(r)\le R\}=\frac R\pi+O_d(1),\quad R\to\infty.\]
The count concerns distinct positive radii, not the infinitely many vectors on each spherical zero set.

## Proof

**1. Exact transform.** The standard spherical Fourier integral yields
\[\int_{|x|<a}e^{-i\xi\cdot x}\,dx=(2\pi)^\nu a^\nu t^{-\nu}J_\nu(at).\]
Subtract the inner ball at \(a=r\) from the unit ball. The value at frequency zero equals the annular volume as stated.

**2. Strict Bessel energy monotonicity.** Define, for \(\nu\ge1\),
\[E_\nu(t)=t^{2\nu}\bigl(J_{\nu-1}(t)^2+J_\nu(t)^2\bigr),\qquad t>0.\]
The elementary recurrences
\[J_\nu'=J_{\nu-1}-\frac\nu tJ_\nu,\qquad
J_{\nu-1}'=\frac{\nu-1}tJ_{\nu-1}-J_\nu\]
give the exact identity
\[E_\nu'(t)=(4\nu-2)t^{2\nu-1}J_{\nu-1}(t)^2.\]
Since \(\nu\ge1\), this derivative is nonnegative and positive except at the discrete zeros of \(J_{\nu-1}\). Thus \(E_\nu\) is strictly increasing and for every \(0<r<1\), \(t>0\),
\[
 J_{\nu-1}(t)^2+J_\nu(t)^2
 >r^{2\nu}\bigl(J_{\nu-1}(rt)^2+J_\nu(rt)^2\bigr). \tag{1}
\]
The strictness follows by integrating the positive derivative on \((rt,t)\), not merely by a pointwise nonnegative derivative.

**3. Nonvanishing at bracket endpoints.** If \(t=j_{\nu-1,k}\), then \(J_{\nu-1}(t)=0\), so (1) implies
\[|J_\nu(t)|>r^\nu|J_\nu(rt)|.\]
Consequently \(G_{\nu,r}(t)\) has exactly the sign of \(J_\nu(t)\). Classical contiguous-order interlacing of the Bessel zeros gives
\[j_{\nu-1,k}<j_{\nu,k}<j_{\nu-1,k+1},\]
and the signs of \(J_\nu(j_{\nu-1,k})\) alternate, beginning positive for \(k=1\). Hence \(G_{\nu,r}\) has at least one zero in each consecutive-endpoint interval, and none is an endpoint.

**4. All zeros are simple, with a prescribed crossing orientation.** At any positive zero \(t\) of \(G_{\nu,r}\), cancellation of its \(J_\nu\)-terms in (1) gives
\[|J_{\nu-1}(t)|>r^\nu |J_{\nu-1}(rt)|.\]
By differentiating \(G_{\nu,r}\) and using the first recurrence,
\[G_{\nu,r}'(t)=J_{\nu-1}(t)-r^{\nu+1}J_{\nu-1}(rt)\quad\text{when }G_{\nu,r}(t)=0.\]
Because \(r<1\), the second term has strictly smaller magnitude than the first. Therefore
\[G_{\nu,r}'(t)\ne0,\qquad
\operatorname{sgn}G_{\nu,r}'(t)=\operatorname{sgn}J_{\nu-1}(t).\tag{2}\]
The last sign is constant throughout each interval \((j_{\nu-1,k},j_{\nu-1,k+1})\). Two distinct simple zeros in that interval would require alternating signs of their crossing derivatives, contradicting (2). Thus each interval has **exactly one** zero.

Near zero the Bessel series gives
\[G_{\nu,r}(t)=\frac{1-r^{2\nu}}{2^\nu\Gamma(\nu+1)}t^\nu(1+O_{\nu,r}(t^2))>0.\]
If there were a first zero before \(j_{\nu-1,1}\), it would cross from positive to negative and thus have negative derivative, contrary to (2), since \(J_{\nu-1}>0\) there. This proves the complete zero census and simplicity, including the absence of an endpoint zero.

**5. Analytic motion and limiting shapes.** The zeros remain in disjoint intervals, and their first derivatives never vanish; the real-analytic implicit-function theorem makes each \(\tau_k(r)\) real-analytic on \((0,1)\). On compact positive-frequency sets,
\[\lim_{r\downarrow0}G_{\nu,r}(t)=J_\nu(t),\qquad
\lim_{r\uparrow1}\frac{G_{\nu,r}(t)}{1-r}=tJ_{\nu-1}(t),\]
with locally uniform convergence (also of derivatives). The sole \(J_\nu\) zero in the \(k\)-th interval is \(j_{\nu,k}\), establishing the first endpoint limit. For the thin-shell limit, take any fixed interior point \(t\) immediately to the right of \(j_{\nu-1,k}\). The limiting scaled function has the sign of \(J_{\nu-1}(t)\), opposite the sign of \(G_{\nu,r}(j_{\nu-1,k})\). Hence the unique intervening zero lies to the left of that chosen point for all sufficiently large \(r\); letting the point approach the bracket's left endpoint forces \(\tau_k(r)\to j_{\nu-1,k}\). Finally, asymptotics of the fixed-order Bessel zeros, together with the brackets, give the stated uniform counting law.

**6. The sharp one-dimensional exception.** For \(d=1\), direct integration gives
\[\widehat{\mathbf1_{\mathcal A_{1,r}}}(t)
=\frac{2(\sin t-\sin rt)}{t}
=\frac{4}{t}\sin\left(\frac{1-r}{2}t\right)
\cos\left(\frac{1+r}{2}t\right).\]
A positive zero is double exactly when both trigonometric factors vanish. This holds precisely if
\[\frac{1+r}{1-r}=\frac{2n+1}{2m}\quad\text{for integers }m\ge1,\ n\ge0.\]
Such a ratio is a reduced rational with odd numerator and even denominator, and conversely every such reduced ratio produces infinitely many intersections by odd integer dilation. Each factor has a simple zero in \(t\), so the product has multiplicity exactly two there and never greater. At all other positive frequencies the zeros are simple. This shows that the higher-dimensional simplicity conclusion cannot be extended to dimension one.

## Verification

The standalone `checker.py` evaluates Bessel zeros by independent sign-change bracketing and verifies the uniqueness brackets, derivative sign in (2), and the strict energy inequality for 112 positive roots across dimensions \(2,3,4,6\) and four annular ratios. It compares 12 direct radial Fourier integrals in dimensions two and three with the Bessel representation, and verifies a one-dimensional double zero at \(r=1/5\), \(t=5\pi/2\). A saved output file records the executed diagnostics; `requirements.txt` identifies the needed numerical library. The proof above, not this finite check, establishes the universal statements.

To reproduce: run `python checker.py` with Python 3 and the dependency given in `requirements.txt`.

## Relationship to prior work

The Fourier–Bessel transform of radial functions, the Bessel recurrences, and contiguous-order Bessel zero interlacing are classical. Urcid and Padilla (2005), including their equations (20) and (23), derive the annular-aperture diffraction amplitude as a difference of two Jinc profiles. Ghobber and Jaming (2010) develop Fourier–Bessel uncertainty principles, and Gallatin (2011/2012) establishes general Fourier formulas for geometric indicators. The DLMF records the classical interlacing between individual \(J_{\nu-1}\) and \(J_\nu\) zeros. None of those inspected statements gives the unique-zero classification for the *difference of differently scaled Bessel functions*, its no-multiplicity consequence, or the all-dimension ball-to-sphere zero continuation. In particular, the classical contiguous-order interlacing is not an interlacing statement about \(J_\nu(t)-r^\nu J_\nu(rt)\); the strict energy comparison (1) supplies the missing implication. Earlier annular-optics literature may have made equivalent observations without phrasing them as a theorem; priority is not independently certified.

## Limitations

The statement concerns real radial frequencies, concentric shells, and dimensions \(d\ge1\). It does not classify complex-frequency zeros, nonconcentric or nonradial shells, arbitrary radial weights, or the locations of individual zeros more accurately than the proved interlacing bounds. Simplicity refers to radial zeros of the amplitude, not to the order-two vanishing of its squared optical intensity. The numerical diagnostics are finite and cannot certify universal zero counts. A plausible unindexed earlier Bessel-difference interlacing lemma remains a literature-priority risk.

## References

- G. Urcid and A. Padilla, *Far-field diffraction patterns of circular sectors and related apertures*, Applied Optics **44** (2005), 7677–7696; DOI: 10.1364/AO.44.007677 (full author-uploaded text inspected, including equations (20), (23) and discussion of diffraction patterns).
- S. Ghobber and P. Jaming, *Strong annihilating pairs for the Fourier-Bessel transform*, arXiv:1009.1710v1 (public September 9, 2010), J. Math. Anal. Appl. **377** (2011), 501–515 (full PDF inspected for definitions and stated uncertainty results).
- G. M. Gallatin, *Fourier, Gauss, Fraunhofer, Porod and the shape from moments problem*, arXiv:1109.5262v1 (September 24, 2011), J. Math. Phys. **53** (2012), 013509 (lawful NIST full PDF inspected).
- NIST Digital Library of Mathematical Functions, §§10.6 and 10.21, especially equation 10.21.2 (Bessel contiguous-order zero interlacing) and §10.21(vi) (fixed-order zero asymptotics), https://dlmf.nist.gov/10.21.
