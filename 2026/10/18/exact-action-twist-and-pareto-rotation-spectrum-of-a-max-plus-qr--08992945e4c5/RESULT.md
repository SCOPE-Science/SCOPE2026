# Exact action-twist and Pareto rotation spectrum of a max-plus QRT map

## Finding

For the area-preserving planar homeomorphism
\[
 F(x,y)=\bigl(y,\max(0,y+1)-x\bigr),
\]
set
\[
 H(x,y)=\max\{1-x-y,2-x,2-y,1+x-y,1-x+y,x,y\}.
\]
For each \(c\ge 3\), the invariant sublevel polygon \(K_c=\{H\le c\}\) has exact area
\[
 A(c)=\operatorname{area}(K_c)=\frac{5c^2-6c-3}{2},\qquad A(3)=12.
\]
Every nonfixed invariant curve \(\{H=c\}\) has a clockwise-positive rotation number. It is \(\rho(c)=1/6\) for \(1<c\le3\) and, on every exterior polygon \(c>3\),
\[
 \rho(c)=\frac{c-1}{5c-3},\qquad \frac16<\rho(c)<\frac15.
\]
On the exterior annulus the area action \(I(c)=A(c)/(2\pi)\) has an exact, strictly positive twist,
\[
 \frac{d\rho}{dI}(c)=\frac{4\pi}{(5c-3)^3}.
\]

Let \(C>3\), let \(Z_C\) be uniform with respect to planar area on \(K_C\), and let \(R_C=\rho(H(Z_C))\); define its value at the fixed point arbitrarily because that point has zero area. The **entire rotation-frequency probability law**, including its atomic component, is
\[
 \mathbb P(R_C\in dr)=\frac{12}{A(C)}\,\delta_{1/6}(dr)
 +\frac{4}{A(C)(1-5r)^3}\,
 \mathbf1_{(1/6,\,(C-1)/(5C-3))}(r)\,dr.
\]
There are no other atoms. In the large-area limit, the magnified gap from the maximal exterior frequency has the Pareto-two distribution:
\[
 C\left(\frac15-R_C\right)\ \Longrightarrow\ W,\qquad
 \mathbb P(W\le w)=
 \begin{cases}
 0,&w<2/25,\\[2pt]
 1-\bigl(2/(25w)\bigr)^2,&w\ge2/25.
 \end{cases}
\]
In particular, the limiting density is \(8/(625w^3)\) on \(w>2/25\). The scaling law concerns uniform *area* sampling, not arclength sampling on a single orbit.

## Assumptions and scope

All coordinates and level parameters are real. The map is a continuous bijection of \(\mathbb R^2\) with inverse \(F^{-1}(u,v)=(\max(0,u+1)-v,u)\), and its two affine branches have determinant one. The term \(\rho\) means the number of **clockwise turns per original iterate** of the induced orientation-preserving circle homeomorphism on an invariant polygon (not the return map's rotation number). A clockwise turn counts positively, so conventional counterclockwise rotation number is \(-\rho\pmod1\). The center \((1,1)\) is fixed with \(H=1\). All other levels \(1<c\le3\) have the six-step periodic motion. At every exterior level \(c>3\), the polygon is a simple invariant Jordan curve, including irrational levels with nonperiodic dense orbits. Each statement involving \(Z_C\) is with respect to normalized two-dimensional Lebesgue measure on \(K_C\).

## Proof

**1. Conservation and area preservation.** Split into \(y\ge-1\) and \(y\le-1\) in \(H\circ F\). In the first branch the terms reduce, after removing affine terms dominated using \(y\ge-1\), to \(\max\{2-y,1+x-y,x,2-x,y,1-x+y\}\), which is exactly the original \(H\) there. In the second branch both max expressions reduce to \(\max\{1-x-y,2-y,1+x-y\}\). Thus \(H\circ F=H\) globally. Each affine branch has Jacobian determinant \(1\), and the displayed continuous inverse shows global preservation of planar area.

**2. Exact polygon and action.** The inequalities \(H\le c\) are seven closed half-plane constraints. For \(c>3\), their boundary is the clockwise octagon with consecutive vertices
\[
 (c,c),\ (c,1),\ (c-2,-1),\ (1,2-c),\ (-1,2-c),\ (2-c,-1),\ (2-c,1),\ (1,c).
\]
All lie on active constraints, and their consecutive edges exhaust the boundary of the convex intersection. Its signed shoelace sum is \(-(5c^2-6c-3)/2\); taking the absolute value gives \(A(c)\), and continuity gives \(A(3)=12\). Consequently \(dI/dc=(5c-3)/(2\pi)\).

**3. Rotation number per physical iterate.** The exact return section from Takahashi–Iwao is the two-edge clockwise arc from \((c,1)\) through \((c-2,-1)\) to \((1,2-c)\). Its first return on normalized arclength \(r\in\mathbb R/\mathbb Z\) is the rigid rotation \(r\mapsto r-h\pmod1\), where \(h=2/(c-1)\in(0,1)\). Returns from the first subarc (relative length \(h\)) take six original iterates, and all other returns take five. Each return traverses the invariant polygon clockwise once and hits that arc again. If \(h=m/k\) is reduced, in \(k\) returns precisely \(m\) of them take six iterates; therefore the original map completes \(k\) clockwise turns in \(5k+m\) steps. If \(h\) is irrational, unique ergodicity of circle rotations gives asymptotic relative frequency \(h\) of the six-iterate visits and mean return time \(5+h\). Both cases give \(\rho(c)=1/(5+h)=(c-1)/(5c-3)\). The inner area is a linear order-six elliptic cell centered at \((1,1)\), with clockwise-positive frequency \(1/6\). Differentiating gives \(d\rho/dc=2/(5c-3)^2\), hence the strict area-twist identity.

**4. Full finite-cutoff spectral law.** For \(c>3\), \(\rho(c)\) is strictly increasing, and its inverse is \(c=(1-3r)/(1-5r)\). The normalized uniform-area law of \(H(Z_C)\) has cumulative distribution \(A(c)/A(C)\) for \(3\le c\le C\). The whole inner polygon carries the single frequency \(1/6\) and has area \(12\). On the exterior, the chain rule gives
\[
 \frac{dA}{dr}=\frac{dA}{dc}\frac{dc}{dr}
 =\frac4{(1-5r)^3}.
\]
Integration over the stated exterior interval yields \(A(C)-12\), proving the displayed probability law and the absence of any other atoms.

**5. Large-cutoff distribution.** For \(0<t<1\), the area ratio satisfies \(\mathbb P(H(Z_C)/C\le t)=A(tC)/A(C)\to t^2\). Thus \(H(Z_C)/C\) converges to a random variable \(T\) on \((0,1)\) with cumulative distribution \(t^2\). Since \(1/5-\rho(c)=2/[5(5c-3)]\), the continuous-mapping theorem (the limiting law has no mass at \(T=0\)) gives \(C(1/5-R_C)\Rightarrow 2/(25T)\). The exact distribution of the latter is the stated Pareto-two law. The inner atom has mass \(12/A(C)=O(C^{-2})\), so it vanishes in this limit.

## Verification

The standalone `verify.py` uses SymPy for exact polynomial and rational-function identities. It verifies the shoelace formula, the area-twist derivative, change-of-variables density, exact density normalization, and the algebraic tail scaling. Independently, it checks invariant conservation at a finite rational grid and computes exact rational orbit periods plus geometric windings for five levels, including \(c=4\) (seventeen iterations, three clockwise turns) and \(c=9/2\) (thirty-nine iterations, seven turns). The command is `python verify.py`, with SymPy available. Its successful output is `VERIFY_OK`. Infinite irrational-return and limiting-distribution assertions follow from the analytic proof, not from the finite computational controls.

## Relationship to prior work

Takahashi and Iwao, *Geometrical dynamics of an integrable piecewise-linear mapping* (2007), derived the conserved max-plus integral, outer polygon geometry, a two-edge rigid first-return rotation, and rational orbit periods. Those facts are used as inputs and **are not new**. The present contribution reconstructs the **physical-time** rotation number, the exact area-action twist, and the complete Lebesgue-area frequency distribution—including its fixed-frequency atom, cubic exterior density, and Pareto-two asymptotic after cutoff normalization. Their paper does not state or analyze an area-weighted rotation law or its scaling limit. Cimà, Gasull, Mañosa and Mañosas (2020 preprint) study different, discontinuous pointwise-periodic piecewise-affine maps with quantized level values; their discrete first-integral spectra do not imply the continuously foliated frequency law for the present max-plus QRT map.

## Limitations

The theorem concerns this fixed parameter normalization and area sampling; it does not prove analogous laws for arbitrary ultradiscrete QRT maps, under non-integrable perturbations, or for random samples from arclength on a single curve. The twist is an area-action derivative of the integrable foliation and by itself gives no KAM theorem for nonsmooth perturbations. All quantities are consequences of the known exact polygon and return structure combined with new geometric and measure-theoretic calculations; consequently the chief priority risk is an unlocated prior computation of the same pushforward law or Pareto limit. The source's earliest publicly available day may predate the day-precise bibliographic date cited here.

## References

1. D. Takahashi and M. Iwao, *Geometrical Dynamics of an Integrable Piecewise-Linear Mapping*, in *Bilinear Integrable Systems: From Classical to Quantum, Continuous to Discrete*, pp. 291–300 (2007), doi:10.1007/978-1-4020-3503-6_25. Author-posted public PDF: https://hakotama.jp/laboratory/works/public/2005-NATO-Science-Series.pdf (especially Sections 4–5 and Figures 3–6).
2. A. Cimà, A. Gasull, V. Mañosa, and F. Mañosas, *Pointwise periodic maps with quantized first integrals*, arXiv:2010.12901 (2020); *Communications in Nonlinear Science and Numerical Simulation* 108 (2022), 106150. Related but distinct systems.

3. M. Iwao and D. Takahashi, *Ultradiscrete Hamiltonian Systems*, *Glasgow Mathematical Journal* 47 (2005), 87–97, doi:10.1017/S0017089505002314. Earlier general convex lattice-polygon Hamiltonian framework.
4. M. Iwao, *Analysis of Ultradiscrete Hamiltonian Systems with Lattice Polygons*, *Journal of the Physical Society of Japan* 74 (2005), 3167–3178, doi:10.1143/JPSJ.74.3167. Bibliographic abstract was available; full text was not inspected.
