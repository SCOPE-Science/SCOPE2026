# Exact analytic-center resonance lines for a finite-tumble run-and-tumble particle

## Finding

A one-dimensional particle in a harmonic potential has run velocities \(\pm V\) and a zero-velocity tumble state. Runs terminate at rate \(\gamma_R>0\); tumbles end at rate \(\gamma_T>0\), with the next run direction chosen independently and fairly. With trap relaxation \(b>0\), the **stationary total-position density is analytic at the trap center if and only if**
\[
\gamma_T=\gamma_R+(2n+1)b,\qquad n\in\mathbb Z_{\ge0}.
\]
The result gives an infinite family of exact polynomial-times-beta densities, together with the complete converse: every other positive rate pair has a genuine fractional-power or logarithmic central nonanalyticity. The result concerns analyticity in a neighborhood of the center; behavior at the confining endpoints may remain singular.

## Assumptions and scope

The velocity state is \(S_t\in\{-1,0,1\}\); the position obeys \(\dot X_t=-bX_t+VS_t\). From either running state the chain enters the tumble state at rate \(\gamma_R\), and the tumble state enters each running state at rate \(\gamma_T/2\). All four physical parameters are strictly positive. The unique stationary position measure is supported on \([-V/b,V/b]\). Rescale \(x=bX/V\), \(u=\gamma_R/b\), \(v=\gamma_T/b\). The theorem addresses the **unconditional position density** after summing over the three velocity states. It does not claim that every velocity-conditioned density is analytic.

Put \(c=(u+1)/2\). For \(n\ge0\) let
\[
B_{u,n}(x)=\frac{\Gamma(u+n+1/2)}{\sqrt\pi\,\Gamma(u+n)}(1-x^2)^{u+n-1},\quad |x|<1,
\]
and let \(Hf=-\tfrac12\partial_x(xf)\). On the resonance line \(v=u+1+2n\), the stationary density is exactly
\[
f_{u,n}=\frac{1}{(c)_n}\left(\prod_{j=0}^{n-1}(H+c+j)\right)B_{u,n}.
\]
The empty product is the identity. All derivatives are taken on the open support; the constructed functions vanish sufficiently strongly at intermediate steps for the integrations by parts below. The final density has the form \((1-x^2)^{u-1}P_{u,n}(x^2)\), with a polynomial \(P_{u,n}\) of degree at most \(n\). The normalization is exact and its nonnegativity follows from equality with the unique stationary probability law.

The first two families are
\[
f_{u,0}(x)=\frac{\Gamma(u+1/2)}{\sqrt\pi\Gamma(u)}(1-x^2)^{u-1},
\]
\[
f_{u,1}(x)=\frac{\Gamma(u+3/2)}{\sqrt\pi\Gamma(u+1)}\frac{u}{u+1}(1+x^2)(1-x^2)^{u-1}.
\]
For \(u=1\) these include the exactly uniform density at \(v=2\), as well as the nonconstant analytic density \(f(x)=3(1+x^2)/8\) at \(v=4\).

## Proof

**1. Source transform and moments.** The exact 1D stationary characteristic function established by Sun, Ye and Podgornik (arXiv:2409.00578, Section III, Eq. 38) in dimensionless variables is
\[
\varphi(q)={}_1F_2\left(a;b_*,c;-q^2/4\right),\quad a=v/2,\quad b_*=(u+v)/2,\quad c=(u+1)/2.
\]
(The physical-space scaling is \(x=bX/V\); the dimensionless Fourier argument is \(q\).) The source's exact even moments are therefore
\[
M_{2m}=\frac{(1/2)_m(a)_m}{(b_*)_m(c)_m},\qquad m=0,1,2,\ldots .
\]
These determine a unique probability measure because support is compact. This use of the published forward transform is explicitly prior work, not a new derivation.

**2. Resonance construction.** On \(v=u+1+2n\), we have \(a=c+n\) and \(b_*=u+n+1/2\). The beta density \(B_{u,n}\) has even moments \((1/2)_m/(b_*)_m\). Integration by parts gives, for any integrable density with adequate boundary decay, \(\int x^{2m}Hf(x)\,dx=m\int x^{2m}f(x)\,dx\). Because every intermediate step of the displayed operator product has factor \((1-x^2)^{u+n-1-j}\), with exponent at least \(u>0\) before the last step, there are no boundary terms. The proposed \(f_{u,n}\) consequently has moments
\[
\frac{(1/2)_m}{(b_*)_m}\frac{(c+m)_n}{(c)_n}=
\frac{(1/2)_m(c+n)_m}{(b_*)_m(c)_m},
\]
using the Pochhammer identity \((c+m)_n/(c)_n=(c+n)_m/(c)_m\). These equal the published stationary moments for every \(m\ge0\). Both measures have support in \([-1,1]\), so equality of all moments (polynomial density in continuous functions) establishes equality of their measures. The construction is therefore normalized and nonnegative. Each differential operation lowers the boundary power by at most one, so the final density equals \((1-x^2)^{u-1}\) times a polynomial of degree at most \(n\) in \(x^2\); this is analytic for \(|x|<1\).

**3. Necessity and the logarithmic exceptional case.** The same paper's exact inverse Fourier formula (Section III, Eq. 39) splits the density near zero into an even analytic series in \(x^2\) and a branch
\[
A(u,v)|x|^{v-1}\bigl(1+O(x^2)\bigr),
\]
where, for positive \(u,v\) with \(v\notin\{1,3,5,\ldots\}\),
\[
A(u,v)=\frac{\sqrt\pi\,\Gamma((u+v)/2)\Gamma((u+1)/2)}{\Gamma(v/2)\Gamma(u/2)\cos(\pi v/2)\Gamma((u+1-v)/2)\Gamma((v+1)/2)}.
\]
All gamma factors away from the reciprocal gamma are finite and nonzero. Thus \(A(u,v)=0\) exactly when \((u+1-v)/2\) is a nonpositive integer, precisely the proposed resonance lines. Off those lines, when \(v\) is not an odd positive integer, \(v-1\) is not an even nonnegative integer, so the nonzero branch cannot be analytic at zero. At odd positive integer \(v_0=2m+1\), take the parameter limit \(v\to v_0\) in Eq. 39. Since \(1/\cos(\pi v/2)\) has a simple pole and \(|x|^{v-1}=x^{2m}(1+(v-v_0)\log|x|+\cdots)\), the finite limiting density has an \(x^{2m}\log|x|\) term whose coefficient is the nonzero residue of \(A(u,v)\), unless \(1/\Gamma((u+1-v_0)/2)=0\). The latter condition is again exactly a resonance line. The analytic branch of Eq. 39 cannot cancel the logarithm. This completes the if-and-only-if classification.

## Verification

The included executable \(`verify.py`\) performs 140 exact symbolic checks using SymPy. For integer \(u\in\{1,2,3\}\), \(n\in\{0,1,2,3,4\}\), it constructs the operator-defined density, reconstructs the zero-velocity component from the stationary conservation law, verifies the two independent stationary generator equations, and compares even moments through order ten with the hypergeometric formula. It also checks the two explicit special cases and three off-resonance branch amplitudes. The checker was run on the packaged content and completed successfully. These finite tests support the all-positive-parameter analytic proof; they are not offered as a substitute for it. To reproduce: install SymPy and execute \(`python verify.py`\).

## Relationship to prior work

Sun, Ye and Podgornik (2024 preprint; 2025 journal publication) derived the general 1D hypergeometric characteristic function and density. Their Section III discusses cusp thresholds, conjectures derivative existence based on numerical evidence, and notes the isolated uniform case \(u=1,v=2\), but does not state the full infinite analyticity-resonance classification or the finite differential-operator family. The present finding depends on those published formulas and claims only their systematic **regularity classification, polynomial family and converse**. Basu et al. (2019 preprint, 2020 journal publication) considered the equal-rate three-state model, which cannot satisfy \(v=u+1+2n\) and so does not contain these positive-rate resonance lines. Guéneau, Majumdar and Schehr (2026) study a different instantaneous-tumble model; their beta distributions do not classify the present finite-tumble rate resonances.

## Limitations

The theorem assumes positive finite run/tumble rates, exactly zero active velocity during tumbling, isotropic independent post-tumble signs, and no thermal Brownian diffusion. It is restricted to the unconditional one-dimensional stationary position density and to analyticity at interior point \(x=0\). It does not classify full differentiability at support endpoints, time-dependent laws, or robustness under noise. This mathematical derivation has not undergone independent external scientific validation. Publication-priority searches cannot exclude all broader or unindexed special-function theorems. The use of the source's exact forward density and characteristic function is acknowledged as prior work.

## References

1. A. Sun, F. Ye, and R. Podgornik, *Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578v1 (September 1, 2024), and revised version v2 (April 16, 2025), Section III, equations (38)–(43). https://arxiv.org/html/2409.00578v2
2. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (October 22, 2019). https://arxiv.org/abs/1910.10083
3. M. Guéneau, S. N. Majumdar, and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (February 9, 2026). https://arxiv.org/abs/2602.08436
