# A localization clock and self-similar rates for the cell-polarization slow flow

## Result

Consider the zero-membrane-diffusion slow-time limit in Section 3.1 of Niethammer--Röger--Velázquez, *Localization properties of a free boundary problem for cell polarization* (arXiv:2609.20609v1):

\[
\partial_t u=-(1-g)\xi+\alpha g,\qquad
0\le \xi\le1,\quad u\xi=u,\quad u\ge0,
\]
\[
\alpha(t)=\frac{\int_{\{u>0\}}(1-g)\,dS}{\int_{\{u>0\}}g\,dS},
\qquad \int_\Gamma u(\cdot,t)\,dS=1,
\]
where \(g=g(x)\) is time independent on the smooth closed surface \(\Gamma\). Let

\[
g_*:=\max_\Gamma g,\qquad
H(x):=\frac{g_*-g(x)}{g_*},\qquad
\alpha_*:=\frac{1-g_*}{g_*},
\]
\[
\phi(t):=g_*\bigl(\alpha(t)-\alpha_*\bigr),\qquad
\Phi(t):=\int_0^t\phi(s)\,ds.
\]

Assume the maximizer set of \(g\) is finite, and let \(u_0\ge0\) be the bounded continuous initial datum of the slow-time limit problem. Define the exact threshold

\[
\sigma(t):=\frac{\Phi(t)}{t+\Phi(t)}.
\]

Then the representation formula in the source can be rewritten exactly as

\[
\boxed{
 u(x,t)=\bigl[u_0(x)+(t+\Phi(t))(\sigma(t)-H(x))\bigr]_+ .
}
\]

Let

\[
G(s):=\int_\Gamma (s-H(x))_+\,dS.
\]

The first conclusion is a general localization-clock identity:

\[
\boxed{t\,G(\sigma(t))\longrightarrow1.}
\]

Thus the small-sublevel geometry of the signal determines the physical localization scale by asymptotic inversion of \(G\). In particular, if

\[
G(s)\sim C s^q\qquad(s\downarrow0),\qquad C>0,\quad q>1,
\]
then

\[
\boxed{
\sigma(t)\sim C^{-1/q}t^{-1/q},
\qquad
\Phi(t)\sim C^{-1/q}t^{1-1/q},
}
\]

and, for the monotone representative of \(\phi\),

\[
\boxed{
\phi(t)\sim \left(1-\frac1q\right)C^{-1/q}t^{-1/q},
\qquad
\alpha(t)-\alpha_*\sim
\frac{1-1/q}{g_*}\,C^{-1/q}t^{-1/q}.
}
\]

This upgrades the qualitative convergence \(\alpha(t)\downarrow\alpha_*\) from the source to an explicit rate whenever the signal has a power-law sublevel geometry.

## Homogeneous maxima and the full similarity profile

Suppose the maxima are \(x_1,\ldots,x_M\), and in local geodesic coordinates near \(x_j\),

\[
H(\exp_{x_j}z)=v_j(z)+o(|z|^{m_j}),
\]

where \(v_j\) is positive homogeneous of degree \(m_j>0\). Put

\[
m:=\max_j m_j,\qquad J_*:=\{j:m_j=m\},
\]
\[
C_j:=\int_{\mathbb R^2}(1-v_j(y))_+\,dy,
\qquad C:=\sum_{j\in J_*}C_j.
\]

The source computes the corresponding small-threshold law

\[
G(s)\sim C s^{1+2/m}.
\]

Combining it with the localization clock gives

\[
\boxed{
\sigma(t)\sim A t^{-m/(m+2)},
\quad
\Phi(t)\sim A t^{2/(m+2)},
\quad
\phi(t)\sim \frac{2A}{m+2}t^{-m/(m+2)},
}
\]

where

\[
A=C^{-m/(m+2)}.
\]

Consequently,

\[
\boxed{
\alpha(t)-\alpha_*
\sim \frac{2A}{(m+2)g_*}\,t^{-m/(m+2)}.
}
\]

In particular the instantaneous multiplier gap has a universal ratio to the geometric threshold,

\[
\boxed{
\frac{g_*(\alpha(t)-\alpha_*)}{\sigma(t)}\longrightarrow\frac{2}{m+2}.
}
\]

Moreover, at almost every large time,

\[
\boxed{
\frac{t\,\sigma'(t)}{\sigma(t)}\longrightarrow-\frac{m}{m+2}.
}
\]

Thus the corresponding spatial scale below has asymptotic logarithmic shrink speed \(t\ell'(t)/\ell(t)\to-1/(m+2)\).

Let

\[
\ell(t):=\sigma(t)^{1/m}\sim A^{1/m}t^{-1/(m+2)}.
\]

For every dominant maximum \(j\in J_*\), the rescaled concentration profile converges locally uniformly:

\[
\boxed{
\frac{u(\exp_{x_j}(\ell(t)y),t)}{\Phi(t)}
\longrightarrow (1-v_j(y))_+.
}
\]

Thus the long-time shape is not only a limiting measure: after the intrinsic shrinking rescaling, each dominant peak converges to the explicit positive-part profile selected by the leading homogeneous signal deficit.

The peak height and total support area also have sharp asymptotics. Since

\[
B_j:=|\{v_j<1\}|=\frac{m+2}{m}C_j,
\]

one obtains

\[
\boxed{
\max_\Gamma u(\cdot,t)\sim A t^{2/(m+2)},
}
\]

and

\[
\boxed{
|\{u(\cdot,t)>0\}|
\sim \frac{m+2}{m}\,C^{m/(m+2)}t^{-2/(m+2)}.
}
\]

The weights \(C_j/C\) at the flattest maxima agree with the source's limiting-measure weights; the new content is the full-time localization clock, the rates, and the local similarity profile.

## Generic Morse maxima

Assume every maximum is nondegenerate and let

\[
Q_j:=-D_\Gamma^2 g(x_j)>0.
\]

Then \(m=2\) and

\[
v_j(y)=\frac{1}{2g_*}y^\top Q_jy,
\qquad
C_j=\frac{\pi g_*}{\sqrt{\det Q_j}},
\]

so with

\[
C=\pi g_*\sum_{j=1}^M(\det Q_j)^{-1/2}
\]

we obtain

\[
\boxed{
\sigma(t)\sim\frac1{\sqrt{Ct}},
\qquad
\Phi(t)\sim\sqrt{\frac tC},
\qquad
\alpha(t)-\alpha_*
\sim\frac1{2g_*\sqrt{Ct}}.
}
\]

The spatial localization width is therefore

\[
\boxed{\ell(t)\sim(Ct)^{-1/4}},
\]

while

\[
\boxed{
\max u\sim\sqrt{\frac tC},
\qquad
|\{u>0\}|\sim2\sqrt{\frac Ct}.
}
\]

At each maximum,

\[
\boxed{
\frac{u(\exp_{x_j}((Ct)^{-1/4}y),t)}{\sqrt{t/C}}
\longrightarrow
\left(1-\frac{y^\top Q_jy}{2g_*}\right)_+.
}
\]

Thus a generic Morse signal produces a \(t^{-1/4}\) spatial width, a \(t^{-1/2}\) support area, a \(t^{1/2}\) peak height, and a \(t^{-1/2}\) multiplier gap, with explicit Hessian-dependent constants.

## Proof

The source proves \(\alpha(t)\downarrow\alpha_*\) and gives

\[
u(\cdot,t)=\left(u_0+\int_0^t[-(1-g)+\alpha(\tau)g]d\tau\right)_+.
\]

Since \(g=g_*(1-H)\) and \(\phi=g_*(\alpha-\alpha_*)\), the integrand is exactly

\[
\phi(\tau)(1-H)-H.
\]

Hence

\[
u=[u_0+\Phi-(t+\Phi)H]_+
=[u_0+(t+\Phi)(\sigma-H)]_+.
\]

Let \(M=\|u_0\|_\infty\) and \(F(s)=|\{H<s\}|\). Because \(\phi(t)\to0\), one has \(\Phi(t)=o(t)\), so \(\sigma(t)\to0\). From the exact representation,

\[
\{H<\sigma\}\subset\{u>0\}
\subset\left\{H<\sigma+\frac{M}{t+\Phi}\right\}.
\]

Mass conservation and \(u_0\ge0\) give

\[
(t+\Phi)G(\sigma)\le1
\]

and

\[
1\le (t+\Phi)G(\sigma)+M F\left(\sigma+\frac{M}{t+\Phi}\right).
\]

The maxima are finite, hence \(F(s)\to0\) as \(s\downarrow0\). Therefore

\[
(t+\Phi)G(\sigma)\to1.
\]

Since \(\Phi=o(t)\), this is precisely \(tG(\sigma)\to1\).

If \(G(s)\sim Cs^q\), inversion yields \(\sigma\sim C^{-1/q}t^{-1/q}\). The identity

\[
\Phi=\frac{t\sigma}{1-\sigma}
\]

gives the asymptotic for \(\Phi\). Finally \(\phi\) is nonincreasing because \(\alpha\) is. For \(\lambda>1\), monotonicity gives

\[
\phi(t)\ge\frac{\Phi(\lambda t)-\Phi(t)}{(\lambda-1)t},
\]

while for \(0<\lambda<1\),

\[
\phi(t)\le\frac{\Phi(t)-\Phi(\lambda t)}{(1-\lambda)t}.
\]

Using regular variation of \(\Phi\) and then taking \(\lambda\to1\) proves the stated asymptotic for \(\phi\). Differentiating the exact absolutely continuous quotient \(\sigma=\Phi/(t+\Phi)\) at almost every time gives

\[
\sigma'=\frac{t\phi-\Phi}{(t+\Phi)^2},
\]

and the stated logarithmic shrink rate follows from the asymptotics of \(\phi,\Phi,\sigma\).

For homogeneous maxima, the source's local scaling calculation gives \(G(s)\sim Cs^{1+2/m}\). The similarity profile follows directly from

\[
\frac{u(\exp_{x_j}(\ell y),t)}{\Phi}
=
\left[\frac{u_0(\exp_{x_j}(\ell y))}{\Phi}
+1-\frac{H(\exp_{x_j}(\ell y))}{\sigma}\right]_+
\]

and \(\ell^m=\sigma\). The support-area asymptotic follows from the two support inclusions above, because

\[
\frac{M/(t+\Phi)}{\sigma}=\frac{M}{\Phi}\to0,
\]

and the homogeneous sublevel measure satisfies

\[
F(s)\sim \left(\sum_{j\in J_*}|\{v_j<1\}|\right)s^{2/m}.
\]

For any positive homogeneous \(v\) of degree \(m\), layer-cake scaling gives

\[
\int(1-v)_+=\frac{m}{m+2}|\{v<1\}|,
\]

which yields the coefficient above. The Morse formulas are the specialization \(m=2\), with \(H\sim (2g_*)^{-1}z^\top Q_jz\).

## Relation to prior literature

The source paper arXiv:2609.20609v1 proves concentration of the slow-time limit, monotonicity of the multiplier, a representation formula, and a subsequential characterization of limit measures. Its Section 4 computes the small-threshold asymptotics of \(G\) and the limiting weights for asymptotically homogeneous maxima. The result here uses those ingredients but adds the asymptotic clock \(tG(\sigma(t))\to1\), explicit time exponents and constants, and the full local self-similar profile.

Earlier work on the same free-boundary model addresses well-posedness, global stability, support jumps, and interface continuity. The 2026 paper by Flores Sepúlveda--Niethammer--Velázquez studies a different stationary small-mass obstacle problem and obtains its own spatial blow-up laws (for Morse maxima, an \(m^{1/6}\) stationary width). That stationary exponent does not conflict with the \(t^{-1/4}\) dynamic width above because the present result concerns the zero-diffusion slow-time limit system.

## Limitations

The theorem concerns the \(D=\infty\) slow-time limit system (3.7)--(3.10) of arXiv:2609.20609v1, not the original parabolic free-boundary problem at fixed positive membrane diffusion and not the finite-cytosolic-diffusion limit of Section 3.2. The explicit power laws require finite isolated maxima with the stated homogeneous local asymptotics; without regular variation, the source exhibits signals for which threshold geometry can oscillate. The self-similar profile is local near dominant maxima and does not claim a quantitative convergence rate to that profile. The originality assessment is to the best of our knowledge.

## Reproducibility

`artifacts/verify_asymptotics.py` checks the exponent identities, homogeneous sublevel constants, the Morse specialization, and the exact algebraic relation between \(\sigma\) and \(\Phi\). Its output is recorded in `artifacts/verification_output.txt`.

## References

1. B. Niethammer, M. Röger, J. J. L. Velázquez, *Localization properties of a free boundary problem for cell polarization*, arXiv:2609.20609v1 (2026). https://arxiv.org/abs/2609.20609
2. S. Flores Sepúlveda, B. Niethammer, J. J. L. Velázquez, *On the shape of the positivity region for a free boundary problem describing cell polarization*, arXiv:2605.03553v1 (2026). https://arxiv.org/abs/2605.03553
3. A. Logioti, B. Niethammer, M. Röger, J. J. L. Velázquez, *Qualitative properties of solutions to a mass-conserving free boundary problem modeling cell polarization*, Commun. PDE 48 (2023), 1065--1101. https://doi.org/10.1080/03605302.2023.2247467
4. A. Logioti, B. Niethammer, M. Röger, J. J. L. Velázquez, *Interface behavior for the solutions of a mass conserving free boundary problem modeling cell polarization*, arXiv:2402.03034v1 (2024); later published in *Friends in Partial Differential Equations* (2025). https://arxiv.org/abs/2402.03034
