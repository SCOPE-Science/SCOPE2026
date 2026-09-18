# Exact rotation law on the trigonometric Nosé–Hoover a=0 axis

## Statement

Consider the trigonometric Nosé–Hoover system of Szumiński and Llibre

\[
\dot x=\sin y,\qquad
\dot y=-\sin x-a\sin y\sin z,\qquad
\dot z=b(1-2\cos y)
\]

on \(\mathbb T^3\). On the volume-preserving axis \(a=0\), assume \(b\ne0\) and write

\[
H(x,y)=\cos x+\cos y.
\]

For every regular mechanical energy

\[
h\in(-2,0)\cup(0,2),
\]

the invariant set \(\{H=h\}\times\mathbb S^1_z\) is a two-torus. Let

\[
k(h)=\sqrt{1-\frac{h^2}{4}},\qquad
T(h)=4K(k(h)),\qquad
\Omega(h)=\frac{2\pi}{T(h)}=\frac{\pi}{2K(k(h))},
\]

where \(K\) is the complete elliptic integral of the first kind. Then the exact thermostat rotation accumulated during one mechanical period is

\[
\boxed{\rho_b(h)=\frac{\Delta z(h)}{2\pi}
      =\frac{b(1-h)}{\Omega(h)}
      =\frac{2bK(k(h))}{\pi}(1-h).}
\]

Equivalently, on every compact regular energy annulus there is a smooth angular change of variable \(z\mapsto\zeta\) for which the full \(a=0\) dynamics becomes

\[
\boxed{
\dot h=0,\qquad
\dot\theta=\Omega(h),\qquad
\dot\zeta=b(1-h).
}
\]

Thus each invariant energy torus is exactly conjugate to a linear Kronecker flow, not merely approximated by one.

Consequently:

1. if \(\rho_b(h)=p/q\in\mathbb Q\) in lowest terms, every trajectory on that energy torus closes after \(q\) mechanical circuits;
2. if \(\rho_b(h)\notin\mathbb Q\), every trajectory is dense on the energy torus;
3. at the distinguished energy \(h=1\), \(\rho_b(1)=0\), so every trajectory is periodic with mechanical period \(T(1)\), despite the nontrivial oscillation of \(z(t)\) during the period;
4. on the positive-energy family \(0<h<2\), the rotation function is strictly monotone. For \(b>0\) it decreases from \(+\infty\) to \(-b\), while for \(b<0\) the orientation is reversed. Hence each admissible rational rotation number selects exactly one positive energy; periodic energy tori are countable and dense, while irrational tori have full Lebesgue measure;
5. on any open invariant regular annulus, every continuous first integral factors through \(H\). In particular, for \(b\ne0\) there is no second globally single-valued continuous first integral functionally independent of \(H\) on such an annulus.

The branchwise elliptic expressions given in arXiv:2609.19958v1 are therefore valid local first integrals, but they do not globalize to a second continuous first integral on a full invariant regular annulus. Their branch dependence is the local manifestation of the nonzero rotation monodromy above.

## Derivation of the rotation law

For \(a=0\), the mechanical subsystem is Hamiltonian and \(H\) is constant. Szumiński and Llibre give, for \(0<h<2\), the exact mechanical period

\[
T(h)=4K(k(h))
\]

and compute the full-orbit average

\[
\left\langle\cos y\right\rangle_h=\frac h2.
\]

Therefore, with no averaging approximation,

\[
\begin{aligned}
\Delta z(h)
&=b\int_0^{T(h)}(1-2\cos y(t))\,dt\\
&=bT(h)\left(1-2\left\langle\cos y\right\rangle_h\right)\\
&=bT(h)(1-h).
\end{aligned}
\]

Dividing by \(2\pi\) gives \(\rho_b(h)\). For \(-2<h<0\), shifting \((x,y)\mapsto(x-\pi,y-\pi)\) reduces the mechanical orbit to the positive-energy family with energy \(-h\); since \(\cos y\) changes sign, its average is again \(h/2\), while the period is \(T(h)=T(-h)\). Hence the same formula holds on both regular families.

## Positive-energy twist and exact resonance spectrum

On \(0<h<2\), the function

\[
C(h)=\frac{\rho_b(h)}{b}=\frac{2}{\pi}(1-h)K\left(\sqrt{1-\frac{h^2}{4}}\right)
\]

is strictly decreasing. This follows directly from the integral representation of \(K\). Set

\[
D(h,\varphi)=\sqrt{\cos^2\varphi+\frac{h^2}{4}\sin^2\varphi}.
\]

Then

\[
C(h)=\frac{2}{\pi}\int_0^{\pi/2}\frac{1-h}{D(h,\varphi)}\,d\varphi,
\]

and pointwise

\[
\frac{\partial}{\partial h}\left(\frac{1-h}{D}\right)
=-\frac{4\cos^2\varphi+h\sin^2\varphi}{4D^3}<0.
\]

Moreover,

\[
C(h)\to+\infty\quad(h\to0^+),\qquad
C(h)\to-1\quad(h\to2^-).
\]

Thus \(C:(0,2)\to(-1,\infty)\) is a continuous strictly decreasing bijection. For \(b>0\), every rational \(r>-b\) corresponds to exactly one positive energy with \(\rho_b(h)=r\); for \(b<0\), every rational \(r<-b\) does likewise. Because the rationals and irrationals are both dense, both periodic and irrational energy tori are dense in \(0<h<2\). The periodic energies are nevertheless countable, so irrational Kronecker tori occupy full Lebesgue measure in the positive-energy family.

## Exact reduction to linear torus flow

On a compact regular energy annulus, use the source paper's smooth energy-phase coordinates \((h,\theta)\), normalized by

\[
\dot\theta=\Omega(h),\qquad \theta\in\mathbb S^1.
\]

Let

\[
g(h,\theta)=1-2\cos Y(h,\theta).
\]

Its \(\theta\)-average is exactly \(1-h\). Hence

\[
g(h,\theta)-(1-h)
\]

has zero mean. The periodic cohomological equation

\[
\Omega(h)\,\partial_\theta\psi(h,\theta)
=g(h,\theta)-(1-h)
\]

therefore has a smooth \(2\pi\)-periodic solution \(\psi\). Define

\[
\zeta=z-b\psi(h,\theta)\pmod{2\pi}.
\]

Since \(\dot h=0\),

\[
\dot\zeta
=b g-b\Omega\partial_\theta\psi
=b(1-h),
\]

which proves the exact normal form.

The time-\(T(h)\) return on a transverse mechanical phase section is consequently the rigid circle rotation

\[
\boxed{z\longmapsto z+2\pi\rho_b(h)\pmod{2\pi}.}
\]

The periodic/dense dichotomy is then the standard rational/irrational dichotomy for a linear flow on \(\mathbb T^2\).

## Obstruction to a global second continuous first integral

On \(0<h<2\),

\[
\rho_b(h)=b\frac{1-h}{\Omega(h)}
\]

is real analytic. It is not constant: in particular,

\[
\rho_b'(1)=-\frac{b}{\Omega(1)}\ne0.
\]

Therefore it cannot be constant on any nonempty open energy interval. Every such interval contains energies with irrational \(\rho_b(h)\); indeed irrational energies are dense.

Let \(G\) be a continuous first integral on an invariant regular annulus \(H^{-1}(I)\times\mathbb S^1_z\). On every irrational-rotation torus, each orbit is dense, hence continuity forces \(G\) to be constant on the entire torus. Approximating any rational-energy torus by irrational-energy tori and using continuity shows that \(G\) is constant on every energy torus. Thus

\[
G=\Phi(H)
\]

for a continuous scalar function \(\Phi\). If \(G\) is \(C^1\), its differential is everywhere collinear with \(dH\) wherever \(\Phi'\) exists in the usual smooth sense, so it cannot supply a second functionally independent regular first integral.

The same argument applies on the negative-energy regular family \(-2<h<0\), where the rotation law is again analytic and nonconstant; indeed \(\rho_b(h)\to 3b\) as \(h\to-2^+\) and \(|\rho_b(h)|\to\infty\) as \(h\to0^-\).

## Monodromy of the branchwise first integral

The source paper obtains locally, on a fixed branch, a first integral of the form

\[
F=z+bP_h(y),
\]

with \(P_h\) an elliptic primitive. Analytically continue this primitive around one full mechanical circuit. Since \(F\) stays constant along the lifted trajectory while \(z\) increases by \(\Delta z(h)\), the primitive must acquire the period

\[
\Delta P_h=-T(h)(1-h).
\]

Thus the elliptic contribution has monodromy

\[
\boxed{b\,\Delta P_h=-2\pi\rho_b(h).}
\]

Except at \(h=1\), this period is nonzero. This gives an explicit global reason for the branch choices in the local formulas and shows why they cannot be assembled into a single-valued real second integral on a complete regular energy circle. The stronger dense-orbit argument above excludes any alternative continuous second integral on a full regular annulus, not only one of this particular primitive form.

## Relation to the source paper

The source paper correctly identifies \(H=\cos x+\cos y\), constructs branchwise second first integrals on regular domains, derives energy-phase coordinates, gives

\[
T(h)=4K(k),\qquad \langle\cos y\rangle_h=h/2,
\]

and introduces

\[
C(h)=\frac{1-h}{\Omega(h)}.
\]

The present result combines those exact ingredients in the finite-\(b\), \(a=0\) system itself rather than in the later small-parameter averaging calculation. This yields the exact torus return map and the complete rational/irrational orbit classification. It also separates local branchwise integrability from global single-valued integrability on the natural torus phase space.

This does not invalidate the local characteristic calculation or the local formulas in the source. It sharpens their global interpretation: the \(a=0\) flow is exactly reducible to a one-parameter family of Kronecker flows, and for generic energies the corresponding invariant torus is filled densely by a single trajectory.

## Verification

`artifacts/verify_rotation.py` integrates the exact \(a=0\) ODE for nine positive and negative regular energies at \(b=1/2\), using the analytical mechanical period \(4K(k)\). It checks both return of \((x,y)\), the predicted thermostat drift \(bT(h)(1-h)\), and sampled strict decrease of the positive-energy rotation factor. With Python 3, NumPy and SciPy 1.17.0, the executed check gave maximum angular mechanical-return error \(1.284\times10^{-11}\) and maximum drift error \(8.830\times10^{-12}\). This is a numerical sanity check only; the theorem follows from the exact identities above.

## Limitations

The normal form is stated on regular energy annuli away from the separatrix \(h=0\) and the elliptic critical levels \(h=\pm2\). The singular separatrix requires separate analysis. The global-first-integral obstruction assumes \(b\ne0\) and continuity of the candidate integral on a full invariant regular annulus; it does not contradict local branch first integrals on non-global charts, nor does it address singular or discontinuous invariants. The result concerns the exactly decoupled axis \(a=0\) and does not assert persistence of these tori for \(a\ne0\).

## References

1. W. Szumiński and J. Llibre, *Trigonometric Nosé–Hoover oscillator: chaos, periodic orbits and integrability*, arXiv:2609.19958v1 (2026), https://arxiv.org/abs/2609.19958 .
2. A. Katok and B. Hasselblatt, *Introduction to the Modern Theory of Dynamical Systems*, Cambridge University Press, 1995. Standard facts about linear/Kronecker flows on tori are used only as background and are not part of the originality claim.
