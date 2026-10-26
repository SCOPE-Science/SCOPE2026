# Subexponential exceptional sets still force constant curvature in surface geodesic flows

## Finding

Let \((S,g)\) be a closed connected \(C^\infty\) surface with strictly negative curvature. Let \(\phi^t\) be its geodesic flow, \(\mathcal P\) the set of primitive periodic orbits modulo time translation, \(\ell_g(\gamma)\) the period of \(\gamma\), and \(\chi^u(\gamma)\) its unstable Lyapunov exponent per unit time. Define
\[
N_{\mathrm{exc}}(T)=\#\{\gamma\in\mathcal P\setminus E:\ell_g(\gamma)\le T\}.
\]
If some \(\alpha>0\) and \(E\subset\mathcal P\) satisfy
\[
\chi^u(\gamma)=\alpha\quad(\gamma\in E),\qquad
\limsup_{T\to\infty}\frac{1}{T}\log(1+N_{\mathrm{exc}}(T))=0,
\]
then
\[
K_g\equiv-\alpha^2.
\]
Thus the all-periodic-orbit hypothesis in the known surface rigidity theorem can be weakened to allow an exceptional family whose counting growth is subexponential in orbit length.

## Assumptions and scope

The surface is closed, connected, and \(C^\infty\), and its curvature is strictly negative. Its geodesic flow is therefore transitive Anosov and has positive topological entropy. The set \(\mathcal P\) counts primitive periodic orbits; iterates do not change the exponent, and adding their iterates multiplies an exceptional counting function by at most a polynomial factor, which does not change whether its exponential growth rate is zero. The conclusion concerns Gaussian curvature. No claim is made for finite-volume noncompact surfaces, higher-dimensional manifolds, or exceptional sets with positive exponential growth.

## Proof

Let \(E^u\) denote the one-dimensional unstable bundle and define its infinitesimal expansion potential by
\[
a(v)=\left.\frac{d}{dt}\right|_{t=0}
\log\left\|D_v\phi^t\big|_{E^u(v)}\right\|.
\]
For a periodic orbit \(\gamma\) of period \(\ell_g(\gamma)\),
\[
\chi^u(\gamma)=\frac{1}{\ell_g(\gamma)}
\int_0^{\ell_g(\gamma)}a(\phi^t v)\,dt,
\]
where \(v\) lies on \(\gamma\). Set \(\psi=a-\alpha\). Every orbit in \(E\) has zero \(\psi\)-average.

Suppose, for contradiction, that \(\psi\) is not a flow coboundary. The Livšic periodic-orbit criterion then gives a periodic orbit whose \(\psi\)-average is some \(c\ne0\). Let \(\nu\) be a measure of maximal entropy, with positive entropy \(h_\nu>0\), and write \(b=\int\psi\,d\nu\). Choose \(s\in(0,1)\) so that \((1-s)b+sc\ne0\). The specification property permits long orbit segments typical for \(\nu\) to be concatenated with a fixed positive fraction of time shadowing the nonzero-average periodic orbit. The resulting periodic orbits have \(\psi\)-averages bounded away from zero, while the choices of the positive-entropy segments give exponentially many distinct periodic orbits as their lengths grow. Equivalently, the exceptional set \(\mathcal P\setminus E\) has positive exponential counting growth. This contradicts the assumed subexponential bound.

Hence \(\psi\) is a flow coboundary, so its integral vanishes on every periodic orbit. It follows that \(\chi^u(\gamma)=\alpha\) for every \(\gamma\in\mathcal P\). Theorem 1.3 of Nina Zarate and Romaña, *Rigidity of Lyapunov Exponents for Geodesic Flows* (arXiv:2402.05518v1), then gives \(K_g\equiv-\alpha^2\). This establishes the claim.

## Verification

The exponent is represented as the orbit average of the unstable expansion potential. The contradiction uses three standard ingredients: the Livšic periodic-orbit criterion, specification for a transitive Anosov flow, and entropy counting of periodic orbits shadowing positive-entropy orbit segments. The final curvature conclusion is exactly the cited surface rigidity theorem. No finite numerical experiment is used to infer an infinite-orbit statement.

## Relationship to prior work

Nina Zarate and Romaña prove curvature rigidity when the unstable exponent is constant on every periodic orbit; the present statement adds a precise subexponential-exception criterion for reaching that hypothesis. Cantrell and Reyes develop subset rigidity for marked length spectra using exponential growth of subsets of conjugacy classes, but their observable is marked length rather than the unstable Lyapunov exponent. Butt studies how finitely many closed-geodesic lengths approximately control a marked length spectrum; that is a different conclusion and does not imply the exact exponent statement here. The proof's specification and Livšic ingredients are standard dynamical tools, not claimed as new theorems.

## Limitations

The result requires the exceptional periodic-orbit count to have zero exponential growth rate. It does not show rigidity when the exceptional family has positive exponential growth, nor does it give an effective finite length cutoff. The proof uses the known rigidity theorem for compact negatively curved surfaces and standard specification/periodic-orbit counting. A direct prior statement of this exact Lyapunov-potential corollary was not located; priority risk remains because the extension is built from established thermodynamic formalism.

## References

1. N. Nina Zarate and S. Romaña, “Rigidity of Lyapunov Exponents for Geodesic Flows,” arXiv:2402.05518v1 (submitted 8 February 2024), especially Theorem 1.3.
2. S. Cantrell and E. Reyes, “Marked length spectrum rigidity from rigidity on subsets,” arXiv:2304.13209v2 (2024), especially Theorems 1.4 and 1.6.
3. K. Butt, “Approximate control of the marked length spectrum by short geodesics,” arXiv:2210.15101v1 (submitted 27 October 2022), especially Theorem 1.2 and Corollary 1.8.
4. R. Bowen, “Periodic orbits for hyperbolic flows,” American Journal of Mathematics 94 (1972), 1–30.
5. A. N. Livšic, “Cohomology of dynamical systems,” Mathematics of the USSR-Izvestiya 6 (1972), 1278–1301.
