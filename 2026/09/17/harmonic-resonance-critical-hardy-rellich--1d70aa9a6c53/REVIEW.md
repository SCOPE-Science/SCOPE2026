# Review

## Scientific claim reviewed

For the weighted critical Hardy--Rellich functional
\[
\mathcal I_a[u]=\int_{\mathbb R^N}\left|\nabla(u/|x|)\right|^N|x|^a\,dx,
\]
the record claims two results for \(N\ge2\):

1. the Hessian inequality \(\mathcal I_a[u]\le C\int|D^2u|^N|x|^a\) holds exactly for \(a\notin\{0,N\}\);
2. the Laplacian inequality fails whenever \(a=N(1-\beta)\) for a homogeneity \(\beta\) of a nonzero homogeneous harmonic mode, yielding infinitely many explicit failure weights and, in particular, failure at both Muckenhoupt boundary weights \(-N\) and \(N(N-1)\).

## Correctness

**PASS.**

The counterexample family was checked directly. For a spherical harmonic \(Y_m\) and a harmonic homogeneity \(\beta\), the logarithmically cut off mode
\[
u_L=r^\beta Y_m\,\eta((\log r)/L)
\]
is a legitimate member of \(C_c^\infty(\mathbb R^N\setminus\{0\})\) for each finite \(L\). The exact polar formula
\[
\Delta u_L=r^{\beta-2}Y_m\left[(2\beta+N-2)L^{-1}\eta'+L^{-2}\eta''\right]
\]
uses only the identity \(\beta(\beta+N-2)=m(m+N-2)\). At \(a=N(1-\beta)\), the radial density becomes \(dr/r\). The transition region has logarithmic length proportional to \(L\), so the weighted \(L^N\) norm of the Laplacian is \(O(L^{1-N})\).

On the central plateau, the left side is the weighted norm of \(\nabla(r^{\beta-1}Y_m)\). This gradient cannot vanish identically for a nonzero harmonic mode in dimension \(N\ge2\), and the same scale cancellation makes the plateau contribution at least \(cL\). The ratio therefore diverges at least as \(L^N\). The formulas were stress-tested at the special modes \((m,\beta)=(0,0),(1,1),(2,2)\) and at the fundamental homogeneity \(\beta=2-N\), including the \(N=2\) double-root convention.

For the Hessian formulation, the only counterexamples needed are the affine harmonic modes \(1\) and \(x_1\). Their Hessians vanish on the plateau, and differentiating the cutoff gives \(|D^2u_L|\lesssim r^{\beta-2}(L^{-1}+L^{-2})\); hence the same \(O(L^{1-N})\) versus \(\Omega(L)\) comparison proves failure at \(a=N\) and \(a=0\). Conversely, Majdoub's displayed radial and angular estimates (3.5) and (3.6) directly establish the Hessian inequality for every \(a\notin\{0,N\}\). The final patch at \(a=0\) is the only step that uses the superseded unweighted claim. This supports the exact Hessian classification.

Within \(-N<a<N(N-1)\), weighted Calderon--Zygmund theory applies to \(|x|^a\). Combining it with the valid Hessian estimates proves the Laplacian inequality away from \(a=0,N\), while the harmonic modes prove failure at those resonant values when they lie in the interval. The endpoint modes \(m=2\) and \(\beta=2-N\) verify failure at \(-N\) and \(N(N-1)\), respectively; for \(N=2\), the upper endpoint equals the already resonant value \(a=N=2\).

No step treats a timeout, an inaccessible source, or failure of a search as mathematical evidence.

## Originality

**PASS, to the best of our knowledge.**

The closest recent source is Majdoub, arXiv:2606.15668v1. Its Theorems 1.4--1.5 state that the Hessian inequality holds for every \(a\ne N\) and call \(a=N\) the unique critical weight; Corollary 1.6 includes \(a=0\) in the Laplacian range; Remark 5.4 asks whether the Laplacian estimate persists at or outside the Muckenhoupt boundaries. Relevant theorem, proof, and concluding passages were inspected in the public full text.

Castro, arXiv:2511.16537v4, postdates Majdoub v1 and explicitly states that the unweighted Laplacian conjecture is false, using approximations of \(x_1\); its revised weighted theorems exclude \(a=0\). Therefore failure of the *Laplacian* inequality at \(a=0\) is prior art and is not claimed as new here. The present record extends the same resonance mechanism to the Hessian form at \(a=0\), combines that with the valid part of Majdoub's proof to give the corrected exact Hessian range, and derives an infinite family of Laplacian failure weights, including both boundary values singled out by Majdoub's open question.

Targeted searches for the exact functional, the Majdoub preprint, harmonic-mode counterexamples, the two boundary weights, and synonymous weighted Hardy--Rellich formulations found no later correction or equivalent statement. The current SCOPE repository was searched under Hardy/Rellich, Majdoub, harmonic resonance, and related terminology, with no overlapping record found.

The main residual originality risk is classical weighted elliptic theory. McOwen (1979) studies the Laplacian on weighted Sobolev spaces and is widely cited for exceptional weights associated with harmonic polynomials. Its full text was not available through the inspected source; metadata and secondary theorem descriptions were checked. Such general Fredholm theory may subsume the structural origin of the resonance set. The review therefore claims originality only for the explicit present-functional obstruction and its consequences for the two 2026 preprints, not for the general concept of indicial or exceptional weights. Older Hardy--Rellich literature using spherical harmonics also creates residual risk, but searches did not locate this critical functional or the stated endpoint correction.

## Value

**PASS.**

The result is not a routine numerical refinement. It identifies the analytic mechanism behind the missing angular critical weight, repairs a claimed sharp Hessian range in a recent preprint, gives a corrected exact validity set in the currently accessible Muckenhoupt regime, and answers the two boundary cases of an explicitly posed range question by a single reusable harmonic-resonance construction. The infinite discrete obstruction family also shows that failure beyond the Muckenhoupt range is structured rather than confined to the first endpoints.

## Review status

Same-model review: passed. Cross-model review: not yet performed.

This is not independent validation, formal verification, journal peer review, or a guarantee of first discovery.
