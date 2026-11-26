# Logarithmic flattening of the XY support boundary of translation-invariant reduced states

## Finding

Let \(X,Y,Z\) be the standard Pauli matrices (eigenvalues \(\pm1\)). Let \(\operatorname{Red}_2\) be the set of trace-one nearest-neighbor reduced states of translation-invariant infinite spin-\(1/2\) chains. Put
\[
H_0=X\otimes X+Y\otimes Y,\qquad H_1=-X\otimes X+Y\otimes Y,
\quad \mathcal C=\{(\operatorname{tr}(\rho H_1),\operatorname{tr}(\rho H_0)):\rho\in\operatorname{Red}_2\}.
\]
For \(-1<\gamma<1\), its minimum support value in the direction \((\gamma,1)\) is
\[
\epsilon(\gamma)=\min_{(a,b)\in\mathcal C}(b+\gamma a)
=-\frac{4}{\pi}E\!\left(\sqrt{1-\gamma^2}\right),
\]
where \(E(k)=\int_0^{\pi/2}(1-k^2\sin^2q)^{1/2}\,dq\) uses the modulus convention. With \(L=\log(4/|\gamma|)\),
\[
\epsilon(\gamma)=-\frac4\pi-\frac{2\gamma^2}{\pi}\left(L-\frac12\right)
-\frac{3\gamma^4}{4\pi}\left(L-\frac{13}{12}\right)+O(\gamma^6 L).
\]
The lower boundary near the point exposed by \(H_0\) is a graph \(b=g(a)\). Its value and second derivative at the exposed point are \(g(0)=-4/\pi\) and \(g''(0)=0\), and
\[
g''(a)\sim \frac{\pi}{4\log(1/|a|)}\qquad(a\to0).
\]
Thus the graph is \(C^2\) there but has no third derivative at zero. The support value is \(C^1\) but not \(C^2\) at \(\gamma=0\). The logarithmic term also gives a local obstruction to semialgebraicity of \(\operatorname{Red}_2\).

## Assumptions and scope

The observable coordinates use standard Pauli matrices without any additional scaling, and the interaction counts one nearest-neighbor bond per lattice site. Blakaj–Wolf's printed Eq. (11) has a prefactor smaller by a factor of 16 than the support value for their displayed Hamiltonian in Eq. (10) with the variational normalization of Eq. (6). The graph describes the planar projection near the indicated point, not the local geometry of the full reduced-state set.

## Proof

### Support value and normalization

Write \(h=H_0+\gamma H_1\), and let \(e_N\) be the minimum energy of the open chain \(\sum_{j=1}^{N-1}h_{j,j+1}\). Every translation-invariant state satisfies \((N-1)\operatorname{tr}(\rho h)\ge e_N\). Conversely, tile the chain with independent copies of an open-chain ground state and average over the \(N\) shifts of the tiling. The resulting translation-invariant state has bond energy at most \((e_N+\|h\|)/N\), since only one bond per tile crosses its boundary. This identifies the minimum with \(\lim_{N\to\infty}e_N/N\) once the limit is evaluated.

For the open chain use Jordan–Wigner annihilators \(c_j=(\prod_{i<j}Z_i)\sigma_j^+\), with \(\sigma^+=(X+iY)/2\). The bulk Hamiltonian in fermions is
\[
\sum_{j=1}^{N-1}\Bigl[2(c_j^\dagger c_{j+1}+c_{j+1}^\dagger c_j)
-2\gamma(c_j^\dagger c_{j+1}^\dagger+c_{j+1}c_j)\Bigr].
\]
Close this *fermionic* chain with the same bilinear between \(N\) and \(1\). The added term has bounded norm independent of \(N\), so it changes the ground-state energy per site by \(O(N^{-1})\). This uses a periodic fermion Hamiltonian only for computing the limit and makes no identification of finite periodic spin and fermion boundary conditions.

Take Fourier modes \(q=2\pi m/N\). For each \(q,-q\) pair with \(0<q<\pi\), subtract the centering constant \(4\cos q\) from its hopping term. The centered pair has hopping term \(4\cos q(n_q+n_{-q}-1)\) and pairing amplitude of modulus \(4|\gamma\sin q|\) between vacuum and double occupancy. Its two odd-sector levels are zero and its even-sector energies are \(\pm4\sqrt{\cos^2 q+\gamma^2\sin^2q}\). The centering constants sum to \(O(1)\) by the vanishing sum of cosines over the full Fourier grid; the exceptional modes \(0,\pi\), when present, also contribute \(O(1)\). Hence the minimum energy density is
\[
-\frac4{2\pi}\int_0^\pi\sqrt{\cos^2q+\gamma^2\sin^2q}\,dq
=-\frac4\pi E\!\left(\sqrt{1-\gamma^2}\right).
\]
For a check on the normalization, the continuous \(\gamma\to1\) limit is \(-2\), the variational minimum of \(2Y\otimes Y\) attained by averaging the two staggered \(Y\)-polarized product states.

### Boundary regularity

DLMF 19.12.2 is a convergent logarithmic series in the complementary modulus \(k'=|\gamma|\). Its initial terms are
\[
E=1+\tfrac12\gamma^2(L-\tfrac12)+\tfrac3{16}\gamma^4(L-\tfrac{13}{12})+O(\gamma^6 L).
\]
The coefficients of the logarithm and the nonlogarithmic part are convergent power series in \(\gamma^2\) near zero. Differentiating away from zero gives
\[
\epsilon'(\gamma)=-\frac4\pi\gamma(L-1)+O(\gamma^3 L),\qquad
\epsilon''(\gamma)=-\frac4\pi L+\frac8\pi+O(\gamma^2 L).
\]
The energy expansion gives \(\epsilon'(0)=0\); continuity of \(\epsilon'\) and the divergent quotient \(\epsilon'(\gamma)/\gamma\) show that \(\epsilon\) is \(C^1\) but not twice differentiable at zero.

The image \(\mathcal C\) is compact and convex. At every sufficiently small \(\gamma\), differentiability of \(\epsilon\) fixes the first coordinate of any minimizer to \(a(\gamma)=\epsilon'(\gamma)\): for any minimizer \((a,b)\), \(\epsilon(\gamma+t)\le\epsilon(\gamma)+ta\) for both signs of \(t\). The supporting line then fixes \(b(\gamma)=\epsilon(\gamma)-\gamma\epsilon'(\gamma)\). The map \(a(\gamma)\) is continuous and strictly decreasing through zero, so these points cover the lower graph for an open interval of \(a\). This is also the full boundary locally at the exposed point: the projected set is two-dimensional (the uniform and staggered \(X\)- and \(Y\)-polarized states yield four noncollinear projected points after translation averaging), and the maximally mixed state gives \((0,0)\) above the lower boundary.

Away from zero, differentiation on the exposed graph gives
\[
g'(a(\gamma))=-\gamma,\qquad g''(a(\gamma))=-1/\epsilon''(\gamma).
\]
Since \(|a(\gamma)|\sim (4/\pi)|\gamma|L\), one has \(\log(1/|a(\gamma)|)\sim L\), yielding the stated asymptotic in graph coordinates. At zero, \(b(\gamma)-b(0)=O(\gamma^2 L)\) and \(|a(\gamma)|\asymp |\gamma|L\), giving \(g'(0)=0\). The quotient \(-\gamma/a(\gamma)\) tends to zero, so \(g''(0)=0\); the asymptotic makes \(g''\) continuous there. But \(|g''(a)-g''(0)|/|a|\to\infty\), ruling out the third derivative.

### Local obstruction to semialgebraicity

If \(\operatorname{Red}_2\) were semialgebraic, the graph of the minimum would be semialgebraic by quantifier elimination, as in Blakaj–Wolf's Eq. (9). In particular, on a sufficiently small positive interval the graph would satisfy a nonzero polynomial relation. This is impossible even locally: let \(u=\epsilon(\gamma)-\epsilon(0)\), so \(u\sim-(2/\pi)\gamma^2\log(1/\gamma)\). In a nonzero polynomial in \(\gamma,u\) choose among monomials \(\gamma^i u^j\) of lowest weight \(i+2j\) the one of largest \(j\). Its asymptotic dominates all the others, so the polynomial cannot vanish identically on the interval. Thus the log term proves the obstruction without requiring analyticity through the isotropic point.

## Verification

The normalization follows from the open-chain bond estimate and the explicit Fourier pair energies. At \(\gamma=0\) it can also be checked directly by filling the negative modes of dispersion \(4\cos q\). The complementary-modulus expansion and the local curvature calculation are analytic. See `VERIFICATION.md` for further checks of the normalization and the leading singularity.

## Relationship to prior work

The XY dispersion and elliptic-integral expansion are classical. The printed Eq. (11) of Blakaj–Wolf has the same elliptic dependence, so it already displays the nonanalytic term, contrary to the analyticity asserted in their Theorem 3 on \((-1,1)\). The positive normalization factor does not change their non-semialgebraicity conclusion.

There is also an equivalent critical arc in the transverse-field Ising reduced-state projection. For coordinates \(x=\langle X_iX_{i+1}\rangle\), \(z=\langle Z_i\rangle\), the energy is the support value of \(-Jx-Bz\). In the one-dimensional Ising chain the free-fermion dispersion is \(2\sqrt{J^2+B^2-2JB\cos q}\). Setting \(J=1-\gamma\), \(B=1+\gamma\) and substituting \(q/2\) in the energy integral gives precisely the support value above. Thus under \(a=x-z, b=-x-z\) the two local exposed arcs coincide. Zauner et al. discuss the Ising projected support geometry and display an exact critical curve; this is prior coverage of the geometric representation, not a new projection method here. The result quantified above is the exact graph-coordinate regularity and reciprocal-logarithmic coefficient, together with the normalization correction and the local non-semialgebraicity proof for the stated XY projection.

## Limitations

The derivative \(g''\) is in the specified observable coordinates, not an affine-invariant curvature. The result is local for the projected set. It makes no general claim about critical reduced-state boundaries or priority for the classical energy and logarithmic singularity.

## References

1. V. Blakaj and M. M. Wolf, *On the set of reduced states of translation invariant, infinite quantum systems*, Letters in Mathematical Physics 114, 28 (2024), DOI: 10.1007/s11005-024-01776-1; arXiv:2308.14585, Eqs. (6), (9)–(11), Theorem 3.
2. NIST Digital Library of Mathematical Functions, §19.12, Eq. 19.12.2.
3. E. Lieb, T. Schultz, and D. Mattis, *Two soluble models of an antiferromagnetic chain*, Annals of Physics 16 (1961), 407–466.
4. V. Zauner et al., *Symmetry breaking and the geometry of reduced density matrices*, New Journal of Physics 18 (2016), 113033, DOI: 10.1088/1367-2630/18/11/113033, §2 and Fig. 1.
5. P. Pfeuty, *The one-dimensional Ising model with a transverse field*, Annals of Physics 57 (1970), 79–90.
