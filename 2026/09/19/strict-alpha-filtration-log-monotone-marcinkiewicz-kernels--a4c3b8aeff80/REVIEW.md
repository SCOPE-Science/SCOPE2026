# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The main claim was checked directly from the definitions of Huang's \(\Phi_\alpha\).

1. **Parameter monotonicity.** For \(\alpha<\beta\), one has
   \(p_n^{(\alpha)}<p_n^{(\beta)}\). The normalized \(L^p\) means on
   \([0,T_n]\) are monotone in \(p\), so
   \(A_n^{(\alpha)}(h)\le A_n^{(\beta)}(h)\) termwise. This yields
   \(\Phi_\alpha\le\Phi_\beta\) without an interchange of limits.

2. **Probe membership.** For
   \(R_n=\exp(L_n-r_n^\gamma)\) and block mass \(r_n\), the constructed
   decreasing probe has cumulative mass \(L_n+O(1)\) at \(R_n\), while
   \(\log R_n\sim L_n\). Concavity of \(\log\) controls points inside each
   block. Hence \(h_\gamma\in M_\psi\); the argument does not assume an
   unproved complementability or closure property.

3. **Dominant-block asymptotics.** At the sampling scale \(T_n\), the
   \(n\)-th compressed block contributes
   \(C_n=r_n^p(\Delta_n')^{1-p}\). Jensen's inequality bounds all preceding
   blocks by \(R_{n-1}^{1-p}M_{n-1}^p=o(C_n)\). The portion of the
   \((n+1)\)-st block before \(T_n\) is exponentially smaller because
   \(L_{n+1}\gg L_n\) and \(r_{n+1}^\gamma=o(L_{n+1})\).
   Thus the full moment is asymptotic to \(C_n\).

4. **Threshold constant.** Substitution of
   \(\log\Delta_n'=L_n-r_n^\gamma+o(1)\) and
   \(1-p=r_n^{-\alpha}\) leaves precisely
   \(\exp[-r_n^{\gamma-\alpha}/p]\). This gives the three limits
   \(0,e^{-1},1\), including the boundary constant \(e^{-1}\).

5. **Strictness.** Given \(\alpha<\beta\), choosing
   \(\gamma\in(\alpha,\beta)\) produces
   \(h_\gamma\in X_\alpha\setminus X_\beta\).

6. **Hardy--Littlewood obstruction.** Huang's original pair \(g\prec\!\prec f\)
   was re-evaluated for arbitrary \(0<\alpha<1\). The same exact integral for
   \(f\) gives \(\Phi_\alpha(f)=0\), while the final-block estimate gives
   \(\Phi_\alpha(g)=1\) for every \(0<\alpha\le1\). Hence every interior
   \(X_\alpha\) fails Hardy--Littlewood solidity and every
   \(N_{\lambda,\alpha}\) fails strong symmetry.

The finite initial modification used to make the probe globally decreasing is
bounded and supported on finite measure, and the proof is written so that its
contribution is absorbed into fixed constants; it does not affect the limiting
moment calculation.

## Originality

The primary source inspected was Huang's current arXiv:2609.20270v1. It defines
\(\alpha\in(0,1]\) at the construction stage but then uses only
\(\alpha=1\) for the first example and \(\alpha=1/2\) for the second. Searches
using the arXiv identifier, title, "alpha", "kernel", "nested", "strict",
"continuum", "Marcinkiewicz", and "logarithmic submajorization" did not locate
a published statement of the strict filtration
\(X_\beta\subsetneq X_\alpha\) or the threshold formula for \(h_\gamma\).

Kalton--Sukochev (2008) is important prior art for singular
rearrangement-invariant functionals on Marcinkiewicz spaces that fail
Hardy--Littlewood symmetry. That general phenomenon is not claimed as new.
The present originality claim is restricted to the exact ordering and
concentration-threshold structure of Huang's explicit 2026 seminorm family.

No specifically identified inaccessible paper was found that is likely to
contain this exact claim. Older singular-functional literature remains a
residual risk for an abstractly equivalent concentration mechanism, so the
claim is explicitly to the best of our knowledge rather than exhaustive.

SCOPE archive searches by the source identifier, Marcinkiewicz terminology,
logarithmic submajorization, and the claim family found no prior record covering
this result.

## Value

The result turns a construction used at two isolated parameter values into a
complete one-parameter geometric hierarchy. The exact probes identify what the
parameter measures: sensitivity to mass compressed into a relative scale
\(\exp(-r_n^\gamma)\). This yields continuum many distinct logarithmically
solid, strongly symmetric but non-fully-symmetric ideals inside one fixed
classical Marcinkiewicz space.

## Limitations

The result is tied to Huang's explicit scales and \(\psi(t)=1+\log t\) for
large \(t\). It establishes distinctness under the common embedding in
\(M_\psi\), not pairwise Banach-lattice non-isomorphism. It does not classify
the endpoint \(X_1\) with respect to full symmetry and does not claim a
noncommutative analogue.
