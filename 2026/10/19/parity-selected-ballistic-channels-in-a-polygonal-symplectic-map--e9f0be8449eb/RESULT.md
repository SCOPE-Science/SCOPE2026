# Parity-selected ballistic channels in a polygonal symplectic map

## Finding
Consider the plane lift of a periodically forced McMillan–Hénon map, \(F(q,p)=(p,-q+f(p))\), with \(f(p)=0\) for \(0\le p\bmod 2<1\) and \(f(p)=2((p\bmod2)-1)\) for \(1\le p\bmod2<2\). This is the period-\(2\) piecewise-affine force \([\{0,1\},\{2,1\};2]\) in the integrable-diffusion example of Zolkin–Kharkov–Nagaitsev [1], on its full planar lift rather than only its torus projection. Here the residue \(p\bmod2\) always belongs to \([0,2)\).

**Rational-orbit transport dichotomy.** For every \((q,p)\in\mathbb Q^2\), the lifted trajectory is either periodic or ballistic: there is \(c>0\) such that \(\lim_{m\to\infty}\|F^m(q,p)\|_2/m=c\). More precisely, if \(n\) is the first return time of the rational torus projection modulo \(2\mathbb Z^2\) and \(F^n(z)=z+2v\) with \(v\in\mathbb Z^2\), then the lifted orbit is periodic when \(4\nmid n\) or \(v=0\). Otherwise, for every \(0\le j<n\) and integer \(k\ge0\),
\[
 F^{kn+j}(z)=F^j(z)+2k R^jv,
 \qquad R=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
 \qquad c=\frac{2\|v\|_2}{n}.
\]
The phase-resolved velocity is explicit. In general the *vector* \(F^m(z)/m\) oscillates between phases; only its norm has the stated limit.

**A countable family of full transport segments.** For each even integer \(N\ge4\), let \(t=1/N\), \(n=N+4\), and
\[
 S_N=\{(t+h,t-h):-t<h<t\}.
\]
Every point of this open straight segment avoids all switching boundaries for one full \(n\)-step itinerary, whose word is \(AB^{N/2}AAB^{N/2}A\), with \(A\) the zero-force branch and \(B\) the other branch. Its exact planar return is
\[
 F^{N+4}(z)=\begin{cases}
 z+(2,-2),&N\equiv0\pmod4,\\
 z,&N\equiv2\pmod4.
 \end{cases}
\]
Thus every point of \(S_N\) is periodic when \(N\equiv2\pmod4\), while every point is ballistic when \(N\equiv0\pmod4\), with exact radial speed \(2\sqrt2/(N+4)\). These infinitely many nonzero speeds accumulate at zero. The segment length is \(2\sqrt2/N\) in the Euclidean metric. The period-\(n\) return derivative has the nontrivial unipotent matrix
\[
 D F^n\big|_{S_N}=\begin{pmatrix}N+1&N\\-N&1-N\end{pmatrix},
\]
so the segments are nonisolated parabolic resonances, not attracting channels.

## Assumptions and scope
The map is a deterministic planar lift, not a quotient which forgets lattice displacement. The parameters of [1] are fixed at periodic forcing period \(L=2\), zero slope on one half-cell and slope \(2\) on the other half-cell. The rational-dichotomy theorem quantifies over rational initial positions only. The explicit segment theorem quantifies over all real \(h\) satisfying \(|h|<1/N\), including irrational positions. The map is symplectic and piecewise affine off switching interfaces; its torus quotient is a continuous piecewise-linear homeomorphism. It is not differentiable at its switching interfaces. No claim concerns irrational initial positions outside the displayed segments, invariant probability for noncompact transport, generic diffusion, or positive-area ballistic sets.

## Proof
**1. Finite rational torus grid.** Write \(R(q,p)=(p,-q)\). Since \(f(p+2r)=f(p)\) for every integer \(r\),
\[
 F(z+2u)=F(z)+2Ru\quad (u\in\mathbb Z^2).
\]
Also \(F^{-1}(q,p)=(-p+f(q),q)\). Both directions preserve the finite rational grid \((d^{-1}\mathbb Z/2\mathbb Z)^2\) for any denominator \(d\) of \(z\). The quotient map is a bijection of that finite grid, so the quotient point has a least period \(n\) and \(F^n(z)=z+2v\) for a unique \(v\in\mathbb Z^2\). By lattice covariance, \(F^{kn}(z)=z+2\sum_{r=0}^{k-1}R^{rn}v\). Since \(R^4=I\), this sum vanishes after \(4/\gcd(n,4)\) terms if \(4\nmid n\). If \(4\mid n\), \(R^n=I\) and \(F^{kn+j}(z)=F^j(z)+2kR^jv\). Taking Euclidean norms and dividing by \(kn+j\) proves the dichotomy and its exact speed. The case \(v=0\) is periodic regardless of \(n\).

**2. A branch itinerary on every \(S_N\).** Put \(m=N/2\) and denote the branch matrices by
\[
 A=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad B=\begin{pmatrix}0&1\\-1&2\end{pmatrix}.
\]
The first branch is \(A\), since \(0<t-h<1\). On the torus modulo \(2\), both branches are given by these matrices: the constant \(-2\) in the lifted \(B\)-branch disappears. Because \((B-I)^2=0\), \(B^j=I+j(B-I)\). Consequently, for \(0\le j\le m\),
\[
 B^jA(t+h,t-h)=\big((1-2j)t-h, -(1+2j)t-h\big)\pmod2.
\]
For \(0\le j<m\), the second coordinate has residue in \((1,2)\), so the next \(m\) branches are all \(B\); after \(j=m\), the residue belongs to \((0,1)\), giving two consecutive \(A\)-branches. The same calculation after those two branches gives the second \(B\)-run's vertical residues \(1+(2j+1)t+h\) for \(0\le j<m\) and a final \(A\). All inequalities are strict because \(|h|<t\). The word is therefore exactly \(AB^m A^2 B^m A\), with no boundary ambiguity.

The derivative along this word is
\[
 A B^m A^2 B^m A=-AB^{2m}A
  =\begin{pmatrix}N+1&N\\-N&1-N\end{pmatrix}=M_N.
\]
In particular \(M_N(1,-1)^\mathsf T=(1,-1)^\mathsf T\), so the translated return \(F^{N+4}(t+h,t-h)-(t+h,t-h)\) is constant along \(S_N\). It suffices to evaluate its center \(z_*=(t,t)\).

**3. Exact center displacement, including parity.** Let \(H=m+2=(N+4)/2\) and \(S(q,p)=(p,q)\). An elementary four-step induction along the first \(B\)-run yields, while still in that run,
\[
 F^{1+4\ell}(z_*)=((1-8\ell)t,-(1+8\ell)t),\qquad
 F^{3+4\ell}(z_*)=(2-(3+8\ell)t,2-(5+8\ell)t).
\]
These formulas, together with the two intervening steps, give the exact halfway-position table:
\[
\begin{array}{c|c}
 N\bmod8&F^H(z_*)\\\hline
 0&(-1-t,1-t)\\
 2&(1-t,1-t)\\
 4&(1-t,-1-t)\\
 6&(-1-t,-1-t)
 \end{array}
\]
The map is reversible: direct substitution gives \(SFS=F^{-1}\). Since \(S z_*=z_*\), the halfway state satisfies \(F^{-H}(z_*)=S(F^H(z_*))\). When \(N\equiv2\pmod4\), the halfway state is fixed by \(S\); hence \(F^{2H}(z_*)=z_*\). When \(N\equiv0\pmod8\), the halfway state equals its \(S\)-image plus \((-2,2)\) and \(H\equiv2\pmod4\). When \(N\equiv4\pmod8\), it equals its \(S\)-image plus \((2,-2)\) and \(H\equiv0\pmod4\). Applying lattice covariance and \(R^H=\mp I\) respectively gives in *both* cases \(F^{2H}(z_*)=z_*+(2,-2)\). The same identity holds for every point on \(S_N\), by the tangent-fixed return matrix. The transport-speed and periodicity claims now follow from Step 1 for rational points, or directly from covariance and \(R^{N+4}=I\) for *all* points of the segments. QED.

## Verification
The accompanying `verify_transport.py` is a standalone Python 3 standard-library checker using exact fractions and exact integer matrices. Execute `python3 verify_transport.py` to reproduce `EXACT_RATIONAL_CHECKS_OK 3624`. It tests \(N=4,6,\ldots,260\), the exact midpoint table and itinerary word at six rational interior points per segment, the full return and four return blocks, derivative matrices, and a finite rational torus-grid dichotomy including branch boundaries (denominators at most \(12\)). These finite checks are reproducibility diagnostics, **not** substitutes for the quantified proof in Steps 1–3.

## Relationship to prior work
Zolkin, Kharkov and Nagaitsev [1] define the polygon-tessellated symplectic families and describe this period-two forcing as exhibiting 'integrable diffusion' on unwrapping. Their discussion, formulas and illustrations provide the motivating model and qualitative orbit geometry. The present result proves a discrete arithmetical selection of *periodic versus ballistic lifts*, an exact family of nontrivial transport segments, and corresponding radial speeds. Neither the map's area preservation nor bounded torus dynamics alone supplies these lift-specific claims; a torus orbit can close while its planar lift translates. The earlier general discovery article [2] supplies wider background on polygonal integrability, not the claimed classification of the 2023 periodically forced lift.

## Limitations
The all-rational dichotomy is silent on irrational initial points. The explicit ballistic segments are one-dimensional and therefore have zero planar Lebesgue measure; the theorem does not establish normal diffusion or ballistic transport for typical points. The period in the construction is a return time, and is not asserted to be the *least* period in each case. Global originality cannot be inferred from a finite literature/database search; possible alternate formulations and inaccessible antecedents remain a priority risk. No independent mathematical validation has been performed.

## References
[1] A. Zolkin, Y. Kharkov and S. Nagaitsev, *Integrable symplectic maps with a polygon tessellation*, arXiv:2311.17616 (first public version 2023-11-29), especially periodic-force definition and the discussion of integrable diffusion. https://arxiv.org/abs/2311.17616

[2] A. Zolkin et al., *Machine-assisted discovery of integrable symplectic mappings*, arXiv:2201.13133 (2022). https://arxiv.org/abs/2201.13133
