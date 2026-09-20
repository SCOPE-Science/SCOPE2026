# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked separately at its three nontrivial interfaces.

First, the duality claim does not assume that the unilateral left and right shifts are conjugate on \(\mathbb N_0\). Instead, both polynomial norms are identified with the same bilateral convolution norm on \(\ell_s(\mathbb Z)\) for \(1\le s<\infty\): compression gives one inequality, while translating finitely supported vectors away from the boundary gives the reverse inequality. Combining this with ordinary \(\ell_p\)-\(\ell_{p'}\) adjoint duality yields \(R_p=R_{p'}\) for \(1<p<\infty\).

Second, the Möbius test is compatible with the fact that \(R_p\) is defined using polynomials only. For each \(a<1\), the automorphism \((a-z)/(1-az)\) is analytic on a neighborhood of the closed disk, so its Taylor polynomials converge uniformly there. Testing the \(N\)-th truncation on \(e_N\) gives the exact finite coefficient \(\ell_q\)-sum; passing to the limit gives
\[
R_q^q\le\frac{1-a^q}{a^q(1-a^q)+(1-a^2)^q}.
\]
No infinite functional calculus is assumed.

Third, the endpoint and asymptotic deductions were stress-tested. At \(p=1,\infty\), the operator norm is exactly the weighted coefficient \(\ell_1\)-sum, so the classical radius \(1/3\) applies. At \(p=2\), von Neumann's inequality gives radius one. Substituting \(a=2^{-1/2}\) gives the closed-form upper bound \((2^{q/2}-1)^{1/q}\), which is strictly below one for \(q<2\). Its expansion and the known interpolation lower bound give the claimed linear two-sided scale at \(p=2\).

No complementability, compactness, or inheritance assertion is used. In particular, the bilateral translation argument is a norm computation, not a claim that arbitrary block or invariant subspaces are complemented.

## Originality

The current Kania preprint introduces the relevant shift radius in the course of studying a canonical left-shift example and supplies the interpolation lower bound \(3^{-|1-2/p|}\); it leaves the exact radius as a finer quantitative question. Kayumov--Ponnusamy established the scalar powered Bohr theorem and the infimum formula used here. Those facts, classical Bohr's theorem, von Neumann's inequality, and elementary unilateral/bilateral shift transference are treated as prior art rather than discoveries.

The new contribution is the operator-theoretic transfer of the powered Bohr obstruction to Kania's \(\ell_p\) shift radius, together with the exact duality symmetry, strict inequality \(R_p<1\) for every \(p\ne2\), the exact endpoint limits, and the linear Hilbert-point separation with explicit logarithmic constants. Searches using the source-paper title, shift-radius terminology, unilateral-shift/\(\ell_p\) polynomial-calculus terminology, powered Bohr terminology, and equivalent dual-exponent formulations did not locate this package of conclusions.

The main residual prior-art risk is older literature on Matsaev-type polynomial bounds and analytic Toeplitz/convolution norms on \(\ell_p\), where an equivalent duality observation or a Möbius coefficient obstruction could have appeared under different terminology. The relevant current preprint statement and the powered-Bohr source were inspected; no stronger published theorem was found that determines \(R_p\) or implies the stated upper bound and asymptotic consequences as a named result. Originality is therefore asserted only to the best of our knowledge.

## Value

The result closes several qualitative gaps left by a lower-bound-only estimate: it identifies the Hilbert point as the unique full-radius exponent, proves the exact \(p\leftrightarrow p'\) symmetry, determines both non-Hilbert endpoint limits, and pins down the order of the defect near \(p=2\). The powered-Bohr formula also supplies a reusable scalar obstruction for future attempts to determine the exact radius.

## Limitations

The exact interior values remain unresolved, and no claim is made that Möbius functions are extremal for the operator norm problem. The powered Bohr theorem concerns a scalar coefficient inequality; the present proof only uses it after independently deriving the necessary operator-to-coefficient implication. Older shift-polynomial norm literature remains the principal originality uncertainty.
