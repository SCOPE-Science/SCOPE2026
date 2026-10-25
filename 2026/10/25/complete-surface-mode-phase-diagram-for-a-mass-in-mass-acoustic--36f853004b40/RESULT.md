# Complete surface-mode phase diagram for a mass-in-mass acoustic chain

## Finding
Consider the semi-infinite, freely terminated nearest-neighbor mass-in-mass lattice described below. Its only inhomogeneity is the positive host mass at its first cell. The squared-frequency spectrum has two bulk bands and, depending on the boundary mass, zero, one, or two simple exponentially localized surface eigenvalues. Their existence, frequency ranges, profiles, and threshold emergence are classified exactly as follows.

For bulk host mass \(M>0\), internal mass \(m>0\), internal stiffness \(k>0\), host-to-host stiffness \(K>0\), and boundary host mass \(M_b=M+\delta>0\), put
\[
 w=\frac{k}{m},\qquad t_0=w+\frac{k}{M},\qquad D(t)=t\left(M+\frac{k}{w-t}\right).
\]
The two positive roots of \(D(t)=4K\), ordered \(t_-<t_+\), are
\[
 t_\pm=\frac{Mw+k+4K\pm\sqrt{(Mw+k+4K)^2-16KMw}}{2M}.
\]
They satisfy \(0<t_-<w<t_0<t_+\); the bulk squared-frequency bands are \([0,t_-]\) and \([t_0,t_+]\).

**Exact classification for all \(M,m,k,K,M_b>0\).**

1. If \(\delta>0\), there is precisely one surface mode, with squared frequency \(t\in(w,t_0)\). No other surface mode exists.
2. If \(\delta=0\), there are no square-summable surface modes.
3. If \(-M<\delta<0\), there is one mode above the optical band, \(t>t_+\), **if and only if** \(-\delta>2K/t_+\). Independently, there is one additional mode inside the resonance gap, \(t\in(t_-,w)\), **if and only if** \(-\delta>2K/t_-\). No other surface modes exist. Equalities are non-square-summable band-edge thresholds, not surface eigenvalues.

Consequently, two simultaneous surface modes are physically possible exactly when
\[
 k(M-m)>2Km,
\]
and the boundary mass is small enough to satisfy \(0<M_b<M-2K/t_-\). This is a **sharp host/resonator criterion for double localization**. Irrespective of this inequality, the above-optical mode can occur because \(2K/t_+<M/2\).

For every surface mode, its unique squared frequency is the root in the stated interval of
\[
 F_\delta(t):=M+\frac{k}{w-t}+\frac{\delta^2t}{K+\delta t}=0,
\]
and its physical displacements, up to one nonzero scalar, are
\[
 u_n=\lambda^{n-1},\qquad v_n=\frac{k}{k-mt}\lambda^{n-1},\qquad
 \lambda=\frac{K}{K+\delta t},\quad n=1,2,\ldots.
\]
Here \(u_n\) is the displacement of host mass \(n\), and \(v_n\) that of its internal resonator. In each allowed interval \(|\lambda|<1\): \(\lambda>0\) for the heavy-boundary mode and \(\lambda<0\) for either light-boundary mode.

All three band-edge births are quadratic. Let \(D'(t)=M+kw/(w-t)^2\) and \(C_j=t_j^2/[KD'(t_j)]\) for \(t_j\in\{t_-,t_0,t_+\}\). Then, as the stated thresholds are approached from the localized side,
\[
 \begin{aligned}
 t_0-t_{\rm heavy}(\delta)&=C_0\delta^2+O(\delta^3),&&\delta\downarrow0,\\
 t_{\rm upper}(\delta)-t_+&=C_+\left(-\delta-\frac{2K}{t_+}\right)^2+O\!\left(\left|-\delta-\frac{2K}{t_+}\right|^3\right),\\
 t_{\rm lower}(\delta)-t_-&=C_-\left(-\delta-\frac{2K}{t_-}\right)^2+O\!\left(\left|-\delta-\frac{2K}{t_-}\right|^3\right).
 \end{aligned}
\]
The lower-gap expansion is asserted only when its threshold lies in the physical range \(\delta>-M\). No band-edge eigenmode is counted.

## Assumptions and scope
The chain consists of cells indexed by integers \(n\ge1\), each containing a host point mass and one internal resonator. All masses and spring stiffnesses are strictly positive; the first host has mass \(M_b\), other hosts mass \(M\), all resonators mass \(m\); each host connects to its internal resonator by stiffness \(k\), and consecutive hosts connect by stiffness \(K\). The left end is free: there is no spring from host \(1\) to a fictitious host \(0\). Displacements are longitudinal, infinitesimal and conservative. Eigenvectors are required to be square-summable in the physical kinetic-energy norm \(\sum_{n\ge1}(M_n|u_n|^2+m|v_n|^2)\), with \(M_1=M_b\) and \(M_n=M\) otherwise. A surface mode means a genuine positive, isolated, square-summable eigenmode of this semi-infinite self-adjoint generalized stiffness problem; finite-chain edge resonances and band-edge generalized solutions are not included.

## Proof
**1. Bulk bands and reduction.** For a normal mode of squared frequency \(t\), the resonator equation reads \((k-mt)v_n=ku_n\). When \(t\ne w=k/m\), eliminate \(v_n\) to obtain the effective host mass \(\mathcal M(t)=M+k/(w-t)\), and the bulk recurrence
\[
 t\mathcal M(t)u_n=K(2u_n-u_{n-1}-u_{n+1}),\qquad n\ge2.
\]
Its propagating Bloch parameter \(e^{iq}\) has \(D(t)=2K(1-\cos q)\in[0,4K]\). Solving the endpoint equations \(D(t)=0\) and \(D(t)=4K\) yields the two bands and endpoints in the finding, with \(t_-<w<t_0<t_+\). The full mass-normalized lattice is a finite-rank boundary perturbation of the periodic half-line operator, so its essential spectrum is exactly these bulk bands. At \(t=w\), the resonator equations force all \(u_n=0\), and then the host equations force all \(v_n=0\); thus the apparent elimination pole is **not** an eigenfrequency.

**2. Boundary matching and exact secular equation.** Off the bands and \(t=w\), every square-summable bulk solution is a multiple of \(u_n=\lambda^{n-1}\), where \(0<|\lambda|<1\) and
\[
 D(t)=K(2-\lambda-\lambda^{-1}).
\]
At the free first host, \(t(\mathcal M(t)+\delta)u_1=K(u_1-u_2)\). Subtracting the bulk equation gives
\[
 \delta t=K(\lambda^{-1}-1),\qquad \lambda=\frac{K}{K+\delta t}.
\]
On substitution, this is equivalent to \(F_\delta(t)=0\). Conversely, any root satisfying the indicated interval and \(|\lambda|<1\) yields the explicit nonzero square-summable eigenvector, and the recurrence plus boundary condition hold exactly. The square-summable solution space in each gap is one-dimensional, so each eigenvalue is simple.

**3. Exhaustion and sharp thresholds.** For \(t>0\) away from poles,
\[
 F_\delta'(t)=\frac{k}{(w-t)^2}+\frac{\delta^2K}{(K+\delta t)^2}>0.
\]
If \(\delta>0\), the boundary formula forces \(0<\lambda<1\). The only positive bulk-forbidden interval with decaying positive \(\lambda\) is \((w,t_0)\): here \(D(t)<0\). On it \(F_\delta(w+)=-\infty\), while \(F_\delta(t_0)=\delta^2t_0/(K+\delta t_0)>0\), giving exactly one root. If \(\delta=0\), boundary matching gives \(\lambda=1\), never a decaying mode.

If \(-M<\delta<0\), decay requires \(-1<\lambda<0\), equivalently \(t>2K/(-\delta)\). Negative decaying Bloch factors occur only on \((t_-,w)\) and \((t_+,\infty)\). On either interval, the left band-edge \(t_e\in\{t_-,t_+\}\) has \(D(t_e)=4K\). Put \(s=(-\delta)t_e/K\). If \(s>2\), the secular function at that edge is
\[
 F_\delta(t_e)=-\frac K{t_e}\frac{(s-2)^2}{s-1}<0.
\]
At the right end of \((t_-,w)\), the function tends to \(+\infty\); on \((t_+,\infty)\), it tends to \(M_b>0\). Strict monotonicity therefore gives exactly one root in either eligible interval. If \(s\le2\), decay would require starting at \(t\ge2K/(-\delta)\ge t_e\), where the bulk identity gives \(D(t)\ge4K\); at the putative boundary \(\lambda=-1\), the secular function equals \((D(t)-4K)/t\ge0\), and strict monotonicity forbids a root. At equality \(s=2\), the band-edge solution has \(\lambda=-1\), so is not square-summable. These possibilities exhaust the entire positive complement of the bands, with no embedded eigenmodes because bulk Bloch solutions in a band are nondecaying and no nonzero compact-support solution survives the irreducible bulk recurrence.

The higher threshold is always accessible since \(D(t_+)=4K\) and \(\mathcal M(t_+)<M\) imply \(t_+>4K/M\) and hence \(2K/t_+<M/2\). The lower threshold can be crossed by some \(M_b>0\) exactly when \(t_->2K/M\). Comparing \(D(2K/M)\) with \(4K\) on the acoustic branch simplifies this condition precisely to \(k(M-m)>2Km\), proving the double-localization criterion.

**4. Quadratic emergence.** Write the decaying Bloch factor near the optical-band bottom as \(\lambda=e^{-\eta}\), and near either band edge associated with \(D(t)=4K\) as \(\lambda=-e^{-\eta}\), with \(\eta\downarrow0\). Then respectively
\[
 D(t)=-K\eta^2+O(\eta^4),\qquad D(t)=4K+K\eta^2+O(\eta^4).
\]
The boundary identity is respectively \(\delta=(K/t)(e^\eta-1)\) and \(-\delta=(K/t)(1+e^\eta)\). Since \(D'(t_e)=M+kw/(w-t_e)^2>0\), inversion yields \(\eta=(t_e/K)\times\text{(distance to the mass threshold)}+O(\text{distance}^2)\) and the three stated quadratic detachment laws. No finite computation is used to infer these infinite-domain statements.

## Verification
The accompanying standalone `check_surface_modes.py` evaluates the exact secular equations independently of finite-chain eigensolvers and reconstructs the full host/resonator generalized stiffness matrix before mass normalization. Its current deterministic run passed three symbolic identities, 40 finite-chain matrix-spectrum comparisons across positive parameter cases, 40 predicted surface-mode eigenvector matches, exclusion of spurious finite-volume gap/exterior eigenvalues away from the specified thresholds, and the three quadratic band-edge tests. Both one-mode and two-mode regimes were exercised. Run with Python 3, NumPy, SciPy, and SymPy: `OPENBLAS_NUM_THREADS=1 python check_surface_modes.py`. The numerical checks are independent illustrations, not proofs of the semi-infinite spectral assertions, which follow from the recurrence and monotonic secular equation.

## Relationship to prior work
The effective dynamic mass of a locally resonant phononic cell and the bulk dispersion mechanism are classical; the 2005 analysis of Liu, Chan and Sheng concerns these bulk effects. The 2016 paper of Luo treats defect vibrational modes in finite monatomic chains without an internal resonator; its large-chain free-end light-mass threshold is consistent with the \(m\downarrow0\) limit of the present *lower-gap* threshold when \(k\) is fixed. The 2014 study of Pichard and collaborators derives localized boundary modes for translation–rotation granular chains with different coupling and boundary dynamics. Fedele, Suryanarayana and Yavari (2023) study effective-mass reduction and internal/macro-stiffness defects, principally in a chiral periodic structure. None of the inspected source claims supplies the present complete boundary-**host-mass** phase diagram for a semi-infinite scalar mass-in-mass lattice, including the exact possibility criterion for two modes and all three birth coefficients. General Green-function and transfer-matrix methods may provide alternative derivations; their existence alone is not being claimed as new. Priority against all historical specialized treatments cannot be established by search alone.

## Limitations
The theorem concerns a single free surface, one altered host mass, linear nearest-neighbor springs, and strictly positive parameters. It does not classify boundary resonator mass/stiffness defects, loss, nonlinear interactions, long-range couplings, finite-chain avoided crossings, or embedded resonances. The explicit classification is for **point spectrum** outside the two essential bands, not a scattering-amplitude or excitation-efficiency result. Published earlier special cases, effective mass, band edges, and general boundary-state methods are not claimed as new. The literature comparison establishes no absolute priority; an unlocated earlier treatment of precisely the same mass-in-mass boundary model is a residual risk.

## References
1. Z. Liu, C. T. Chan and P. Sheng, “Analytic model of phononic crystals with local resonances,” *Physical Review B* **71**, 014103 (published 3 January 2005), DOI: 10.1103/PhysRevB.71.014103.
2. Q. Luo, “Local vibrational mode of impurity in a monatomic linear chain under open and periodic boundary conditions,” arXiv:1607.06946v1 (submitted 23 July 2016); *European Journal of Physics* **37**, 065501 (2016).
3. H. Pichard, A. Duclos, J.-P. Groby, V. Tournat and V. E. Gusev, “Localized transversal-rotational modes in linear chains of equal masses,” *Physical Review E* **89**, 013201 (7 January 2014), DOI: 10.1103/PhysRevE.89.013201.
4. “Broadband locally resonant metamaterials with graded hierarchical architecture,” *Journal of Applied Physics* **123**, 095108 (5 March 2018), DOI: 10.1063/1.5003264.
5. F. Fedele, P. Suryanarayana and A. Yavari, “On the Effective Mass of Mechanical Lattices with Microstructure,” arXiv:2306.13096v1 (2023), §§2–3.
