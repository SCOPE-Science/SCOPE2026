# Density-one spectral Dirichlet energies for rationally independent \(-R\) honeycomb lengths

## Finding

For the periodic degree-three hexagonal graph with the \(-R\) preferred-orientation vertex coupling and edge lengths \(a,b,c>0\), there is an exact test for whether a single-edge Dirichlet momentum \(k_m=m\pi/a\), \(m\ge1\), is spectral. Define \(s_b=\sin(bk_m)\), \(s_c=\sin(ck_m)\). Then
\[
\boxed{k_m^2\in\sigma(H_{a,b,c})\iff (k_m^2+1)|\sin((b+c)k_m)|\le |k_m^2-1|(|s_b|+|s_c|).}
\]
If \(1,b/a,c/a\) are linearly independent over \(\mathbb Q\), the strict version holds for a set of positive integers \(m\) of natural density one. Each corresponding \(k_m^2\) lies in the **interior** of the spectrum. In particular, these special momenta are not, in general, centers of gaps: a density-one family belongs to spectral bands.

## Assumptions and scope

The graph, Hamiltonian and matching conditions are those defined in Exner--Pekař, arXiv:2409.03538v1, Sections 3--4, with positive edge lengths and the coupling length fixed to \(\ell=1\). The operator acts by the negative second derivative on edges; at each vertex its unitary coupling is \(U=-R\), a negative cyclic permutation. Quasimomenta \(\theta_1,\theta_2\) independently range over a full two-dimensional Brillouin torus. The momentum \(k_m\) is positive and not subject to a non-Dirichlet division or regularization. Only the density-one conclusion assumes rational independence; the spectral-membership equivalence holds for *every* positive length triple and integer \(m\). No assertions are made about negative energies or all other spectral gaps.

## Proof

**1. Exact fiber reduction without dividing by a sine.** Equation (19) of the primary reference is the un-divided secular equation for positive momentum \(k\). At \(k=k_m=m\pi/a\), put \(\varepsilon=(-1)^m\). Then \(\sin(ak_m)=0\) and \(\cos(ak_m)=\varepsilon\); dividing equation (19) only by the strictly nonzero factor \(2k_m^2\) gives
\[
(k_m^2-1)\bigl(s_b\cos\theta_2+s_c\cos\theta_1\bigr)
=\varepsilon(k_m^2+1)\sin((b+c)k_m).
\tag{1}
\]
The ordering of the two independent phase labels does not affect the spectral range. Since the pair of cosine values independently fills \([-1,1]^2\), the range of the left side of (1) is exactly
\[
[-|k_m^2-1|(|s_b|+|s_c|),\;|k_m^2-1|(|s_b|+|s_c|)].
\]
This proves the displayed equivalence, including \(k_m=1\) and possible simultaneous sine zeros. The un-divided equation is the determinant condition for the six traveling-wave coefficients of the Floquet cell, not merely an asymptotic relation. A zero of that determinant supplies a nonzero fiber eigenfunction. Continuity of the compact-cell fiber eigenvalues in quasimomentum places its energy in the spectrum of the full periodic direct integral. No division by \(\sin(ak_m)\) is used.

**2. An exact irrational witness.** Choose
\[
a=1,\qquad b=\tfrac12+\tfrac{\sqrt2}{1000},\qquad c=\tfrac12+\tfrac{\sqrt3}{1000},\qquad m=1,\qquad k_m=\pi.
\]
These lengths satisfy rational independence of \(1,b,c\), because the field automorphisms of \(\mathbb Q(\sqrt2,\sqrt3)\) changing the two radical signs separately force the coefficients of any rational relation to vanish. Put \(\delta_2=\pi\sqrt2/1000\) and \(\delta_3=\pi\sqrt3/1000\). Then \(s_b=\cos\delta_2\), \(s_c=\cos\delta_3\), and \(\sin((b+c)\pi)=-\sin(\delta_2+\delta_3)\). Define
\[
r=\frac{(\pi^2+1)\sin(\delta_2+\delta_3)}{(\pi^2-1)(\cos\delta_2+\cos\delta_3)}.
\]
The elementary bounds \(3<\pi<4\), \(1<\sqrt2,\sqrt3<2\), \(\sin x<x\) for \(x>0\), and \(\cos x\ge1-x^2/2\) imply \(0<\delta_j<0.008\), \(1<(\pi^2+1)/(\pi^2-1)<2\), and \(0<r<0.017<1\). Hence the exact choice \(\theta_1=\theta_2=\arccos r\) solves (1) with \(\varepsilon=-1\). In particular, \(\pi^2\) belongs to the spectrum even though all three lengths are incommensurate.

**3. Density one and interior points.** Assume that \(1,b/a,c/a\) are rationally independent and write \(x_m=bk_m\pmod{2\pi}\), \(y_m=ck_m\pmod{2\pi}\). The Weyl--Kronecker theorem gives equidistribution of \((x_m,y_m)\) on the torus. Set
\[
\Delta(x,y)=|\sin x|+|\sin y|-|\sin(x+y)|.
\]
Always \(\Delta\ge0\). Moreover \(\Delta>0\) when \(\sin x\sin y\ne0\): from \(\sin(x+y)=\sin x\cos y+\cos x\sin y\), both \(|\cos x|\) and \(|\cos y|\) are strictly smaller than one. Consequently \(\{\Delta=0\}\) is contained in the two coordinate sine-zero sets and has torus measure zero. For \(k_m>1\), the strict membership inequality follows from
\[
\Delta(x_m,y_m)>\frac{2|\sin(x_m+y_m)|}{k_m^2-1};
\]
indeed this is the same inequality after the identity \((k_m^2+1)/(k_m^2-1)=1+2/(k_m^2-1)\). Fix \(\eta>0\). Since the zero set of the continuous function \(\Delta\) has measure zero, choose \(\delta>0\) so that the torus-measure of \(\{\Delta\le2\delta\}\) is less than \(\eta\). For sufficiently large \(m\), \(2/(k_m^2-1)<\delta\). Every exceptional index then satisfies \(\Delta(x_m,y_m)\le\delta\). A continuous cutoff supported on \(\{\Delta\le2\delta\}\), together with equidistribution, bounds its upper natural density by \(\eta\). Letting \(\eta\downarrow0\) proves density one.

When the strict inequality holds, the secular equation takes both signs at suitable pairs of quasimomenta at \(k_m\). By continuity, the signs persist for all \(k\) in some open interval about \(k_m\); the intermediate-value theorem in the quasimomentum variables gives a zero of the secular determinant for every such \(k\). Thus \(k_m^2\) is interior to the spectral set. This strengthens mere spectral membership without asserting any universal quantitative band width.

## Verification

The accompanying `verify.py` constructs the six original Bloch matching equations for the positive-energy wave ansatz and performs exact symbolic determinant expansion at both parities of Dirichlet momenta \(ak=m\pi\). It confirms the factor \(64 i k^2 pq\) multiplying the reduced two-phase expression, up to interchange of the two independently variable phase names, where \(p=e^{-i\theta_2}\) and \(q=e^{-i\theta_1}\). The script also checks numerically that the explicit exact irrational witness satisfies the reduced equation and that the strict inequality holds; these numerical checks are supplemental, while the proof above establishes the infinite-density theorem. Run `python3 verify.py` with SymPy installed.

## Relationship to prior work

Exner--Pekař, arXiv:2409.03538v1, derive the governing un-divided equation (19) and in Section 4.1, after substituting \(k=m\pi/a\), say these momenta cannot belong to the spectrum for incommensurate lengths, explaining this by separate cancellation of the \(k^4\)- and \(k^2\)-proportional terms. Equation (1) instead requires only their **sum** to cancel. The source later notes a different exceptional commensurate situation where two cosines vanish, but does not establish this exact general criterion or the density-one spectral-interior phenomenon for rationally independent edge lengths. Exner--Turek, arXiv:1405.0694v1, study a dilated honeycomb graph with a \(\delta\)-type rather than the \(-R\) coupling. Its spectral condition cannot be specialized to the present vertex condition. Results about global high-energy band density do not imply that this particular deterministic subsequence of Dirichlet energies has spectral density one.

## Limitations

The density statement counts integers \(m\), not Lebesgue measure of the energy spectrum or density of gaps. It requires rational independence; no universal count is claimed for commensurate ratios. The result does not exclude infinitely many gaps with centers *away from* this Dirichlet subsequence and does not prove new flat-band assertions. The scientific comparison addresses the publicly available 2024 preprint; a 2025 journal version of the same work exists, but its complete text was not available for comparison, so version-specific corrections are a residual risk.

## References

1. P. Exner and J. Pekař, *Spectral properties of hexagonal lattices with the \(-R\) coupling*, arXiv:2409.03538v1 (first public 2024-09-05), especially equations (3), (17)--(19) and Section 4.1. https://arxiv.org/pdf/2409.03538
2. P. Exner and O. Turek, *Spectrum of a dilated honeycomb network*, arXiv:1405.0694v1 (2014), especially Sections 2--3. https://arxiv.org/pdf/1405.0694
3. Exner--Pekař, journal bibliographic record, *Reports on Mathematical Physics* **96** (2025), 101--114, DOI: 10.1016/S0034-4877(25)00057-6. Journal-body comparison remains open.
4. Weyl--Kronecker equidistribution theorem (standard torus-rotation result).
