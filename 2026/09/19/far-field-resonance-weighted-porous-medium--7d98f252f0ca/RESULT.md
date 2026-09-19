# Far-field resonance in dominating weighted porous-medium absorption

## Statement

Consider the self-similar profile equation

\[
(f^m)''+\frac{N-1}{\xi}(f^m)'+\alpha f-\beta\xi f'-\xi^\sigma f^p=0,
\]

with

\[
1<p<m,\qquad \sigma>0,\qquad
L=\sigma(m-1)+2(p-1),
\]

\[
\alpha=\frac{\sigma+2}{L},\qquad
\beta=\frac{m-p}{L}.
\]

For any bounded self-similar profile covered by Theorem 1.1 of Iagar--Munteanu (arXiv:2609.20397v1), the source proves

\[
f(\xi)\sim c_*\xi^{-r},\qquad
c_*=(p-1)^{-1/(p-1)},\qquad
r=\frac{\sigma}{p-1}.
\]

Define the two far-field rates

\[
q=\frac{L}{p-1},\qquad h=\frac{L}{m-p},
\]

and

\[
D=m r\,(m r-N+2),\qquad C_0=c_*^{m-1}D.
\]

Then the next far-field scale has a sharp trichotomy.

### 1. Forced regime: \(m<2p-1\)

Here \(q<h\), and every bounded profile has the same first relative correction:

\[
\boxed{
 f(\xi)=c_*\xi^{-r}\left(1+A\xi^{-q}+o(\xi^{-q})\right)
}
\]

with

\[
\boxed{
 A=\frac{C_0}{1-\beta q}
 =\frac{c_*^{m-1}m r(mr-N+2)(p-1)}{2p-1-m}.
}
\]

Thus the first correction is universal: it does not depend on which of the bounded profile families is chosen. If \(mr\neq N-2\), all bounded profiles approach the common leading tail from the same side. In particular,

\[
\operatorname{sgn} A=\operatorname{sgn}(mr-N+2).
\]

### 2. Resonant regime: \(m=2p-1\)

Now \(q=h=1/\beta\). There exists a profile-dependent constant \(B_f\in\mathbb R\) such that

\[
\boxed{
 f(\xi)=c_*\xi^{-r}
 \left[
 1+K_{\log}\xi^{-q}\log\xi+B_f\xi^{-q}+o(\xi^{-q})
 \right]
}
\]

where the logarithmic coefficient is universal:

\[
\boxed{
 K_{\log}=\frac{C_0}{\beta}
 =\frac{c_*^{m-1}m r(mr-N+2)}{\beta}.
}
\]

Hence \(m=2p-1\) is a genuine spatial far-field resonance: the diffusion-forced mode and the free stable mode have exactly the same exponent, producing a logarithmic correction.

### 3. Free-mode regime: \(m>2p-1\)

Here \(h<q\). For every bounded profile there is a constant \(B_f\in\mathbb R\) such that

\[
\boxed{
 f(\xi)=c_*\xi^{-r}
 \left(1+B_f\xi^{-h}+o(\xi^{-h})\right).
}
\]

The coefficient \(B_f\) is not fixed by the common leading tail and may vanish for a special trajectory. Thus the first visible correction is generally profile-dependent in this regime.

## Exact harmonic exceptional surface

If

\[
mr=N-2,
\]

then \(D=C_0=0\). In dimensions where this is compatible with \(\sigma>0\),

\[
\boxed{f_s(\xi)=c_*\xi^{-r}}
\]

is itself an exact (singular-at-the-origin) solution of the profile ODE on \(\xi>0\): indeed \(f_s^m\propto \xi^{2-N}\) is radial harmonic, while the drift and absorption terms cancel exactly. Consequently the universal forced coefficient vanishes. At the resonance \(m=2p-1\), the logarithmic coefficient vanishes as well and the leading correction reverts to the profile-dependent \(B_f\xi^{-q}\) term.

## Proof

Set

\[
t=\log\xi,\qquad f(\xi)=c_*e^{-rt}F(t),\qquad F(t)\to1.
\]

Since

\[
q=(m-1)r+2,
\qquad
\alpha+\beta r=c_*^{p-1}=\frac1{p-1},
\]

a direct substitution gives the exact normalized equation

\[
\begin{aligned}
&c_*^{m-1}e^{-qt}
\Big[
(F^m)_{tt}+(N-2-2mr)(F^m)_t+mr(mr-N+2)F^m
\Big]\\
&\hspace{25mm}-\beta F_t+\frac1{p-1}(F-F^p)=0.
\end{aligned}
\tag{1}
\]

Write \(F=1+y\). Linearizing only for the purpose of extracting the first nonzero order, (1) becomes

\[
\boxed{
\beta y_t+y=C_0e^{-qt}+R(t),
}
\tag{2}
\]

where

\[
R(t)=O\!\left(e^{-qt}(|y|+|y_t|+|y_{tt}|)+y^2\right).
\tag{3}
\]

The needed decay control is supplied by the far-field stable-node structure already established in the source paper. In its desingularized center-manifold variables, Eq. (2.21) has eigenvalues

\[
-q=-\frac{L}{p-1},\qquad -h=-\frac1\beta=-\frac{L}{m-p}.
\]

Moreover, combining the source identities

\[
\frac{d}{d\nu}=\frac1X\frac{d}{d\eta},
\qquad
\frac{d\log\xi}{d\eta}=X
\]

gives exactly

\[
\frac{d\log\xi}{d\nu}=1.
\]

Thus the stable-node exponents in \(\nu\) are exactly the power exponents in \(\xi\), not merely comparable rates. Standard local stable-manifold estimates imply, for any \(\delta<\min\{q,h\}\), exponential control of \(y\) and its first two \(t\)-derivatives by \(O(e^{-\delta t})\). Choosing \(\delta>\frac12\min\{q,h\}\) makes the remainder in (3) lower order at the relevant first scale.

Equation (2) can then be integrated by variation of constants.

If \(q<h\), the forcing \(C_0e^{-qt}\) decays more slowly than the homogeneous solution \(e^{-ht}\), and

\[
y(t)=\frac{C_0}{1-\beta q}e^{-qt}+o(e^{-qt}).
\]

Since

\[
1-\beta q=\frac{2p-1-m}{p-1},
\]
this gives the forced-regime coefficient above.

If \(h<q\), multiplying (2) by \(e^{ht}\) gives an integrable right-hand side, hence

\[
e^{ht}y(t)\to B_f,
\]
which yields the free-mode regime.

Finally, if \(q=h=1/\beta\), multiplying (2) by \(e^{qt}\) gives

\[
\frac{d}{dt}(e^{qt}y(t))=\frac{C_0}{\beta}+o(1)
\]
with an integrable error after subtracting the constant term. Therefore

\[
e^{qt}y(t)=\frac{C_0}{\beta}t+B_f+o(1),
\]
which is exactly the logarithmic formula because \(t=\log\xi\).

## Scientific interpretation

The source paper identifies a unique leading tail for every bounded self-similar profile. The refinement above shows that the next order is not uniform across parameter space. The surface

\[
\boxed{m=2p-1}
\]

separates a universal diffusion-forced correction from a profile-dependent stable mode, and on the separating surface the two rates resonate to create a logarithm. A second surface,

\[
\boxed{\frac{m\sigma}{p-1}=N-2},
\]

annihilates the diffusion forcing because the leading power becomes radial harmonic. These two surfaces are independent mechanisms.

The result is potentially useful in matched-asymptotic and comparison arguments for the companion large-time problem: in the forced regime it provides both a sharp rate and an eventual side of approach shared by all bounded similarity profiles.

## Limitations

- The statement refines the far field of the bounded self-similar profiles of arXiv:2609.20397v1; it is not a large-time convergence theorem for arbitrary PDE solutions.
- The coefficient \(B_f\) in the free-mode and resonant regimes is not determined here from the profile's behavior near the origin.
- If \(B_f=0\) in the free-mode regime, this result does not classify the next nonzero term; additional nonlinear resonances can then matter at higher order.
- The exact harmonic profile is singular at the origin and therefore is not itself one of the globally bounded profiles classified by the source paper.
- Originality is asserted only to the best of our knowledge. Older homogeneous-absorption papers identified below were not all available in full text during the literature check.

## Reproducibility

`artifacts/verify_tail_resonance.py` symbolically checks the exponent identities, exact logarithmic-coordinate radial-diffusion identity, nonresonant coefficient, resonant coefficient, and representative parameter regimes. `artifacts/verification_output.txt` records the executed output. These checks support the algebra but do not constitute independent validation.

## References

1. R. G. Iagar and D.-R. Munteanu, *A porous medium equation with dominating weighted absorption: three types of self-similar solutions*, arXiv:2609.20397v1 (2026), https://arxiv.org/abs/2609.20397.
2. R. G. Iagar and D.-R. Munteanu, *A porous medium equation with spatially inhomogeneous absorption. Part I: Self-similar solutions*, J. Math. Anal. Appl. 543 (2025), 128965, https://doi.org/10.1016/j.jmaa.2024.128965.
3. J. B. McLeod, L. A. Peletier and J. L. Vázquez, *Solutions of a nonlinear ODE appearing in the theory of diffusion with absorption*, Differential Integral Equations 4 (1991), 1--14.
4. V. A. Galaktionov and J. L. Vázquez, *Asymptotic behaviour of nonlinear parabolic equations with critical exponents. A dynamical systems approach*, J. Funct. Anal. 100 (1991), 435--462.
