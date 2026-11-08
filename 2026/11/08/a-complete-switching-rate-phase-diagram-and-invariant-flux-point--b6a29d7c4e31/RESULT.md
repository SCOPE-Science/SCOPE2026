# A complete switching-rate phase diagram and invariant-flux point for telegraph-noisy resonance fluorescence

## Finding

A two-level optical transition in the weak-excitation regime undergoes symmetric random-telegraph spectral diffusion: its detuning from a monochromatic laser is \(\bar\Delta\pm v\), where \(v>0\), and the environmental state switches in either direction at rate \(\beta>0\). Let \(a=\gamma/2>0\) be the coherence-decay half-linewidth due to spontaneous emission, and introduce
\[
x=|\bar\Delta|/a,\qquad s=v/a>0,\qquad t=2\beta/a>0.\]
The total stationary scattered intensity divided by the noiseless, resonant, weak-excitation intensity \(I_0\) is
\[
L_{x,s}(t)=\frac{(1+t)(1+t+s^2)+x^2}{(1+t+s^2-x^2)^2+x^2(2+t)^2}.
\]
For every \(x\geq0\), \(s>0\), this function has at most one stationary point on \(t>0\). Its **complete strict shape classification** is as follows, with all comparisons exact.

* If \(0\leq x<1\), it has a unique strict global **minimum** precisely if \(\sqrt 2-1<x<1\) and \(0<s^2<x^2+2x-1\). Its location is \(t_*=(x^2+2x-1-s^2)/(1-x)\). Otherwise it is strictly increasing on \(t>0\).
* If \(x=1\), it is strictly decreasing when \(0<s^2<2\), strictly increasing when \(s^2>2\), and identically \(1/2\) when \(s^2=2\).
* If \(x>1\), it has a unique strict global **maximum** precisely in either of two disjoint regions: \(s^2>x^2+2x-1\), with location \(t_*=(1+s^2-x^2-2x)/(x-1)\); or \(0<s^2<x^2-2x-1\), necessarily with \(x>1+\sqrt2\), with location \(t_*=(x^2-2x-1-s^2)/(x+1)\). Else it is strictly decreasing on \(t>0\).

In particular, for every fixed \(x>1+\sqrt2\), increasing the *spectral-jump amplitude* passes successively through a low-amplitude switching-enhancement region, an intermediate strict-suppression region, and a high-amplitude switching-enhancement region. Each enhancement region has exactly one finite optimal switching rate.

There is exactly one nontrivial, switching-rate-independent point among all \(s>0\): \(x=1\), \(s=\sqrt 2\). At this point, the normalized optical response amplitude and its integrated coherent and incoherent scattering contributions are, for \(t>0\),
\[
A(t)=\frac12+\frac{it}{2(t+2)},\qquad
\frac{I_{\mathrm{tot}}}{I_0}=\frac12,\qquad
\frac{I_{\mathrm{el}}}{I_0}=\frac14+\frac{t^2}{4(t+2)^2},\qquad
\frac{I_{\mathrm{inel}}}{I_0}=\frac{t+1}{(t+2)^2}.
\]
Consequently, increasing the switching rate transfers intensity strictly from the incoherent component to the coherent component while preserving the total integrated intensity. The point \(t=0\) is understood throughout as the \(t\downarrow0\) limit of an ergodic switching process, rather than as a uniquely stationary zero-rate environment.

## Assumptions and scope

We work to the leading nonvanishing order \(O(\Omega^2)\) in monochromatic drive strength \(\Omega\), with \(\Omega\) tending to zero at fixed positive \(a,v,\beta\). The transition has spontaneous-emission rate \(\gamma=2a\), no extra homogeneous dephasing, and environmental frequency shift \(\pm v\) with equal stationary probabilities. The Markov environment jumps from either state to the other at rate \(\beta\). The measured quantity is the **frequency-integrated**, stationary resonance-fluorescence intensity, not the fluorescence at a chosen output frequency. Coherent and incoherent here mean the elastic Rayleigh component and its complement at leading weak-excitation order. Finite instrumental broadening does not alter the integrated intensity. The mathematical statement concerns positive switching rates; endpoint values are limits.

## Proof

**Stationary optical response.** With \(C=\left(\begin{smallmatrix}-\beta&\beta\\\beta&-\beta\end{smallmatrix}\right)\) and stationary environment vector \(p=(1/2,1/2)^T\), the weak-excitation conditional coherences solve a resolvent equation with diagonal detunings \(\bar\Delta\pm v\). In units of \(a\), letting \(u=1+t-ix\), their summed normalized coherence is
\[
A(t)=\mathbf1^T\begin{pmatrix}
1+t/2-i(x-s)&-t/2\\
-t/2&1+t/2-i(x+s)
\end{pmatrix}^{-1}\!p
=\frac{u}{(1-ix)u+s^2}.
\]
For negative \(\bar\Delta\), the amplitude is complex conjugated, so intensity depends only on \(x=|\bar\Delta|/a\). The familiar weak-excitation optical response identity gives \(I_{\mathrm{tot}}/I_0=\operatorname{Re}A\) and \(I_{\mathrm{el}}/I_0=|A|^2\). The latter is the squared stationary coherent amplitude, as also follows from the rank-one stationary projector in the Markov-noise scattering formula. Defining
\[
p_0=1+t+s^2-x^2,\qquad q_0=x(2+t),
\]
we have \((1-ix)u+s^2=p_0-iq_0\). Its modulus is strictly positive: if \(x>0\) then \(q_0>0\), and if \(x=0\) then \(p_0>0\). Taking the real part yields exactly the displayed rational expression for \(L_{x,s}\).

**Complete monotonicity and extremum classification.** Direct differentiation is particularly simple at the complex-resolvent level:
\[
\frac{dA}{dt}=\frac{s^2}{[(1-ix)u+s^2]^2},\qquad
\frac{dL_{x,s}}{dt}=\frac{s^2(p_0^2-q_0^2)}{(p_0^2+q_0^2)^2}.
\]
The only sign-changing factor is \((p_0-q_0)(p_0+q_0)=F_-(t)F_+(t)\), where
\[
F_\pm(t)=(1\pm x)t+1+s^2-x^2\pm2x.
\]
For \(0\le x<1\), \(F_+(t)>0\) and \(F_-(t)\) is strictly increasing; its unique positive zero exists if and only if \(s^2<x^2+2x-1\), necessarily \(x>\sqrt2-1\), yielding a negative-to-positive derivative and the stated minimum. At \(x=1\), \(F_-=s^2-2\) and \(F_+>0\), so the three possibilities follow. For \(x>1\), \(F_-\) strictly decreases and \(F_+\) strictly increases, with \(F_-(0)<F_+(0)\). A positive-to-negative sign change occurs exactly if they both start positive, \(s^2>x^2+2x-1\), or both start negative, \(s^2<x^2-2x-1\). The intervening region has strictly negative derivative on \(t>0\). Solving the appropriate affine zero yields each location. Since the derivative has no other positive zero and changes strictly at that zero, the extrema are unique and global.

**Uniqueness of the invariant point.** For \(s>0\), a constant function requires \(F_-F_+\equiv0\) as a polynomial in \(t\). Because \(F_+\) has positive slope \(1+x\), necessarily \(F_-\equiv0\), which forces \(x=1\) and \(s^2=2\). Conversely at these parameters,
\[
(1-ix)u+s^2=(t+2)(1-i),\qquad A(t)=\frac12+\frac{it}{2(t+2)}.
\]
Then \(\operatorname{Re}A=1/2\), \(|A|^2=1/4+t^2/[4(t+2)^2]\), and \(I_{\mathrm{inel}}/I_0=\operatorname{Re}A-|A|^2=(t+1)/(t+2)^2\). Their derivatives on \(t>0\) are respectively \(+t/(t+2)^3\) and \(-t/(t+2)^3\). This proves strict coherentization at constant total flux. There are no other parameter regimes.

## Verification

Run `python check.py` with Python 3 and SymPy. The included self-contained checker verifies the resolvent and rational formulas symbolically, their exact derivative factorization, the unique invariant response and coherent/incoherent identities, the two endpoint formulas, six exact phase witnesses, and 475 independent exact-rational matrix-resolvent/derivative comparisons. The checker is an aid; the all-parameter statements are established by the analytic affine-factor proof above. An illustrative far-detuned example is \(x=7/2\): the intensity has a strict finite-rate maximum for \(s^2=1\), is strictly decreasing for \(s^2=8\), and has another strict finite-rate maximum for \(s^2=24\). The corresponding normalized optimal rates are \(13/18\) and \(23/10\).

## Relationship to prior work

Bogaczewicz and Machnikowski (2023), specifically the Markov-noise framework and Eqs. (18)–(19), establish the full weak-excitation response and derive spectra for symmetric and asymmetric telegraph noise. Their Sec. 5.2 discusses limits, the merger of spectral peaks, and the intensity behavior at two selected laser frequencies. The rational response here is a specialization of that existing formalism. The contribution assessed here is the **all-detuning, all-jump-amplitude global switching-rate optimization and monotonicity classification**, the two disconnected enhancement regimes, and the unique invariant-total-flux point with its exact elastic/inelastic redistribution. No new general master equation or general noise spectrum is claimed.

Sun, Zou, Maizelis, and Chan (2015) analyze the mathematically analogous complex response of a driven mechanical resonator with telegraph frequency noise and show motional narrowing; the inspected full text does not state this real-part/global-maximum phase classification. Anderson (1954) is a foundational source on random-frequency-modulation line shapes. Its directly accessible abstract does not resolve whether its full text or its subsequent literature already implies or states some part of the exact classification; this remains a priority risk. These results are straightforwardly reducible to a known two-state resolvent, so implicit derivability must not be mistaken for independence from prior work.

## Limitations

The theorem applies only to symmetric two-state Markov spectral diffusion and the weak-excitation integrated signal; it does not assert anything about strong-driving Mollow triplets, asymmetric switching, non-Markov frequency noise, arbitrary frequency-resolved spectral weights, or finite observation-time photon statistics. The invariant point conserves **integrated** power but not coherent/incoherent composition or the spectrum's shape. The value at zero switching is a limiting stationary-ensemble value; with exactly zero switching the environmental chain is not ergodic and the distinction between elastic and arbitrarily narrow inelastic components depends on the order of limits. Historical Kubo–Anderson formulas can imply this classification even without explicit prior statements; publication novelty therefore remains conditional on broader full-text specialist review. Independent scientific verification has not been carried out.

## References

1. R. A. Bogaczewicz and P. Machnikowski, *Resonance fluorescence of noisy systems* (2023), arXiv:2303.01531, first public version 2023-03-02, https://arxiv.org/abs/2303.01531. Relevant: Secs. 3–5 and Eqs. (18)–(19).
2. F. Sun, J. Zou, Z. A. Maizelis, and H. B. Chan, *Telegraph frequency noise in electromechanical resonators* (2015), arXiv:1511.00893, first public version 2015-11-03, https://arxiv.org/abs/1511.00893. Relevant: Secs. III–IV, Eqs. (3)–(9).
3. P. W. Anderson, *A Mathematical Model for the Narrowing of Spectral Lines by Exchange or Motion*, J. Phys. Soc. Jpn. **9** (1954), 316–339, https://doi.org/10.1143/JPSJ.9.316. Foundational abstract and bibliographic record inspected; full text was not obtained.
