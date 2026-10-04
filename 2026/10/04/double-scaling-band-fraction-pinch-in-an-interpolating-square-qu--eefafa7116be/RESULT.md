# Double-scaling band-fraction pinch in an interpolating square quantum graph
## Finding
Consider the equilateral square-lattice quantum graph of Exner--Turek--Tater with edge length \(\ell>0\), Kirchhoff endpoint \(\alpha=0\), and interpolation parameter \(t\in[0,1]\). Let \(H_t\) denote its Hamiltonian. For every \(\tau>0\) and every sequence \(t_m\in(0,1]\) such that \(m t_m\to\tau\), set
\[
C_m=\left[\left(\frac{{(m-\tfrac12)\pi}}{{\ell}}\right)^2,\left(\frac{{(m+\tfrac12)\pi}}{{\ell}}\right)^2\right].
\]
Then
\[
\frac{{|\sigma(H_{{t_m}})\cap C_m|}}{{|C_m|}}\longrightarrow
F_\ell(\tau):=1-\frac{{4}}{{\pi}}\arctan\!\left(\min\left\{{r,r^{{-1}}\right\}}\right),
\qquad r=\frac{{4\ell}}{{\pi^2\tau}}.
\]
The isolated Dirichlet eigenvalue at \((m\pi/\ell)^2\) has zero Lebesgue measure. The crossover has a unique pinch,
\[
F_\ell\!\left(\frac{{4\ell}}{{\pi^2}}\right)=0,
\]
and \(F_\ell(\tau)\to1\) both as \(\tau\downarrow0\) and as \(\tau\to\infty\). Thus the noncommuting high-energy and Kirchhoff limits are resolved by an explicit one-parameter scaling curve.

## Assumptions and scope
The graph, vertex family, and normalization are those of Exner, Turek, and Tater, arXiv:1804.01414, Section 7, in the special case \(\alpha=0\). The statement concerns Lebesgue measure in the energy variable and one full cell centered at the Dirichlet momentum \(m\pi/\ell\). It allows any sequence \(t_m\) with \(m t_m\to\tau\); it is not restricted to the exact choice \(t_m=\tau/m\).

The source separates the parameter-independent Dirichlet points from the continuous bands. A single Dirichlet point in \(C_m\) is retained in the spectrum but contributes zero to its Lebesgue measure. No claim is made here about density-of-states weights inside a band, negative spectrum, nonzero \(\alpha\), or a uniform convergence rate over unbounded \(\tau\)-ranges.

## Proof
Write
\[
x=k\ell,\qquad M=m\pi,\qquad y=x-M\in[-\pi/2,\pi/2],
\qquad A_m=\ell\cot\frac{{\pi t_m}}{{4}}.
\]
For \(y\ne0\), put \(u=\tan(|y|/2)\in(0,1]\). Independently of the parity of \(m\), the unordered pair
\[
\left\{\left|\tan\frac{{x}}{{2}}\right|,\left|\cot\frac{{x}}{{2}}\right|\right\}
\]
is \(\{{u,u^{{-1}}\}}\). The exact positive-band condition (34) of arXiv:1804.01414 is therefore equivalent to
\[
(xu-A_m)(x/u-A_m)\ge0,
\]
or, after multiplication by \(u/x^2>0\),
\[
(u-r_m(x))(1-r_m(x)u)\ge0,
\qquad r_m(x)=\frac{{A_m}}{{x}}.
\]
Because \(0<u\le1\), this holds exactly when
\[
u\ge \min\left\{{r_m(x),r_m(x)^{{-1}}\right\}}.
\]

From \(m t_m\to\tau\) and \(\cot z\sim z^{{-1}}\) as \(z\downarrow0\),
\[
\frac{{A_m}}{{M}}
=\frac{{\ell}}{{m\pi}}\cot\frac{{\pi t_m}}{{4}}
\longrightarrow r:=\frac{{4\ell}}{{\pi^2\tau}}.
\]
Moreover \(x/M\to1\) uniformly for \(|y|\le\pi/2\), so \(r_m(x)\to r\) uniformly across the whole cell. Hence, away from the measure-zero limiting boundary, the band condition converges to
\[
\tan\frac{{|y|}}{{2}}\ge q,
\qquad q:=\min\left\{{r,r^{{-1}}\right\}}.
\]
Thus the limiting momentum-band set in \([-\pi/2,\pi/2]\) is
\[
|y|\ge 2\arctan q,
\]
whose total length is \(\pi-4\arctan q\). The band indicators therefore converge almost everywhere on the cell and are uniformly bounded, so dominated convergence gives convergence of the normalized momentum measure, including at the critical case \(q=1\).

To pass from momentum to energy, note that \(E=k^2=x^2/\ell^2\), so \(dE=2x\,dx/\ell^2\). The energy-cell length is
\[
|C_m|=\frac{{(M+\pi/2)^2-(M-\pi/2)^2}}{{\ell^2}}=\frac{{2\pi M}}{{\ell^2}}.
\]
Since \(x/M\to1\) uniformly on the cell, normalizing the weighted energy measure changes the limit by \(o(1)\). Therefore the normalized energy spectral measure tends to the normalized limiting momentum length,
\[
F_\ell(\tau)=1-\frac{{4}}{{\pi}}\arctan q.
\]

The map \(q=\min\{{r,r^{{-1}}\}}\) lies in \((0,1]\), equals \(1\) only at \(r=1\), and tends to \(0\) as \(r\to0\) or \(r\to\infty\). This proves the unique zero at \(\tau_c=4\ell/\pi^2\) and both limiting values \(1\).

Finally, the source's exact collapse parameter for the band centered at \(((j-\tfrac12)\pi/\ell)^2\) is
\[
t_j^*=\frac{{4}}{{\pi}}\operatorname{{arccot}}\!\left(\frac{{(j-\tfrac12)\pi}}{{\ell}}\right).
\]
Consequently \(j t_j^*\to4\ell/\pi^2\). The two band halves adjacent to the cell \(C_m\) have indices \(m\) and \(m+1\), and both collapse scales converge to the same constant \(\tau_c\), agreeing with the zero of \(F_\ell\).

## Verification
The accompanying `verify.py` independently evaluates the source inequality (32) on dense midpoint grids and compares it with a bisection solution of the exact factor condition (34). It also checks convergence to the stated scaling function for several edge lengths and values on both sides of the pinch, verifies the reciprocal symmetry of the limiting formula, and checks the scaled exact-collapse parameters. Running

`python3 verify.py`

returns `VERIFY_OK`.

## Relationship to prior work
Exner--Turek--Tater derive the exact band condition, the parameter-dependent finite-index collapse points, and a fixed-\(t\) high-energy gap-width asymptotic. Their fixed-\(t\) expansion is not uniform as \(t\to0\): its leading width grows like \(\cot(\pi t/4)\), while the pure Kirchhoff endpoint has no positive gaps. The result above resolves precisely this singular regime by keeping \(m t_m\) finite and computing the entire normalized cell-band fraction.

Exner--Turek (arXiv:1006.1446) classify high-energy band and gap widths for a fixed general square-lattice vertex coupling; that classification does not address a coupling varying with the band index or the present scaling curve. Exner's 2020 review (arXiv:2003.06189) discusses the preferred-orientation high-energy behavior but does not state this simultaneous limit. Exner--Pekař (arXiv:2403.09457) study interpolation on periodic chain graphs, a different topology.

Targeted database and literature searches for a square-lattice interpolation double-scaling law, normalized cell spectral fraction, and an \(m t\)-crossover found no statement implying the formula above. The closest retrieved mathematical-physics records concerned different operators or fixed-coupling asymptotics.

## Limitations
The proof is specific to the Kirchhoff endpoint \(\alpha=0\), where the source's band condition factorizes into two scalar half-angle factors. It establishes only the leading scaling limit for Lebesgue spectral fraction. It does not assert an optimal finite-\(m\) error bound, a density-of-states limit, or an analogous formula for \(\alpha\ne0\).

An equivalent crossover could conceivably be implicit in literature using singular-perturbation or nonuniform high-energy terminology rather than quantum-graph band-fraction language. The searches and inspected primary sources did not reveal such a result.

## References
1. P. Exner, O. Turek, M. Tater, *A family of quantum graph vertex couplings interpolating between different symmetries*, arXiv:1804.01414; J. Phys. A 51 (2018) 285301; DOI 10.1088/1751-8121/aac651.
2. P. Exner, O. Turek, *High-energy asymptotics of the spectrum of a periodic square-lattice quantum graph*, arXiv:1006.1446.
3. P. Exner, *Topologically induced spectral behavior: the example of quantum graphs*, arXiv:2003.06189.
4. P. Exner, J. Pekař, *Vertex coupling interpolation in quantum chain graphs*, arXiv:2403.09457.
