# Curvature law for mean rectification in vector \(p\)-Laplacian Duffing responses
## Finding
Consider the periodically forced vector \(p\)-Laplacian Duffing system introduced by Mawhin and Novoa, with \(p>2\), restoring functions
\[
g_j(s)=b_js^3+c_js^2+d_js,
\]
and a simple averaged state \(\alpha\), meaning \(g_j(\alpha_j)=\bar e_j\) and \(g_j'(\alpha_j)\neq0\) for every component. Let
\[
\gamma=\frac1{p-1},\qquad w=\mathcal K(e-\bar e),
\]
where \(\mathcal K\) is the zero-mean periodic inverse used in the source and \(w\) is the leading profile in its Proposition 3.1. Then every local periodic-solution family supplied by that proposition as \(\varepsilon\to0^+\) obeys, componentwise,
\[
\overline{u_{\varepsilon,j}}
=\alpha_j-
\frac{g_j''(\alpha_j)}{2g_j'(\alpha_j)}
\overline{w_j^2}\,\varepsilon^{2/(p-1)}
+o\!\left(\varepsilon^{2/(p-1)}\right).
\]
For the cubic restoring force this becomes
\[
\overline{u_{\varepsilon,j}}
=\alpha_j-
\frac{3b_j\alpha_j+c_j}{3b_j\alpha_j^2+2c_j\alpha_j+d_j}
\overline{w_j^2}\,\varepsilon^{2/(p-1)}
+o\!\left(\varepsilon^{2/(p-1)}\right).
\]
Consequently, when \(g_j''(\alpha_j)\neq0\) and \(w_j\not\equiv0\), the periodic response has a nonzero mean displacement for all sufficiently small positive \(\varepsilon\). Its sign is opposite to \(g_j''(\alpha_j)/g_j'(\alpha_j)\). The coefficient contains no velocity-coupling matrix entry.

## Assumptions and scope
The statement uses exactly the vector Duffing family and notation of Mawhin--Novoa, arXiv:2610.02155v1, Section 3.1. The parameter satisfies \(p>2\), the forcing is continuous and periodic, and \(\alpha\) is a nondegenerate zero of the averaged map. The asymptotic is one-sided, \(\varepsilon\to0^+\), matching Proposition 3.1. No uniqueness of the periodic branch is assumed: the argument applies to every local solution family for which the source's leading profile holds.

## Proof
Write \(\delta_{\varepsilon,j}=u_{\varepsilon,j}-\alpha_j\). Proposition 3.1 gives
\[
\delta_{\varepsilon,j}=\varepsilon^\gamma w_j+o(\varepsilon^\gamma)
\]
in the uniform norm, with \(\overline{w_j}=0\). Hence \(\overline{\delta_{\varepsilon,j}}=o(\varepsilon^\gamma)\),
\[
\overline{\delta_{\varepsilon,j}^2}
=\varepsilon^{2\gamma}\overline{w_j^2}+o(\varepsilon^{2\gamma}),
\qquad
\overline{\delta_{\varepsilon,j}^3}=O(\varepsilon^{3\gamma}).
\]

Average the \(j\)-th differential equation over one period. The average of the derivative \((\Phi_p(u'))'_j\) vanishes by periodicity, and the average of each velocity term \(u_k'\) also vanishes. Thus the exact compatibility identity is
\[
\overline{g_j(u_{\varepsilon,j})}=\bar e_j=g_j(\alpha_j).
\]
Because \(g_j\) is cubic, Taylor expansion about \(\alpha_j\) is exact:
\[
0=g_j'(\alpha_j)\overline{\delta_{\varepsilon,j}}
+\frac12g_j''(\alpha_j)\overline{\delta_{\varepsilon,j}^2}
+b_j\overline{\delta_{\varepsilon,j}^3}.
\]
Since \(g_j'(\alpha_j)\neq0\), substitution of the moment asymptotics yields
\[
\overline{\delta_{\varepsilon,j}}
=-\frac{g_j''(\alpha_j)}{2g_j'(\alpha_j)}
\overline{w_j^2}\,\varepsilon^{2\gamma}
+o(\varepsilon^{2\gamma}),
\]
which is the asserted formula. The sign corollary follows because \(\overline{w_j^2}>0\) exactly when \(w_j\not\equiv0\).

## Verification
The proof uses only two imported facts from the source: the exact periodic system and its leading profile \(u_\varepsilon=\alpha+\varepsilon^{1/(p-1)}w+o(\varepsilon^{1/(p-1)})\), with \(w\) zero mean. All remaining steps are exact period averaging and an exact cubic identity. No numerical truncation, finite enumeration, or unproved limiting interchange is used. The uniform source asymptotic directly controls the second and third moments needed above.

## Relationship to prior work
Mawhin--Novoa prove the leading nonconstant profile and explicitly state that velocity coupling and restoring terms enter at higher order, but they do not give a higher-order mean-displacement coefficient. The present identity extracts the first possible mean correction without solving a second complementary equation: it follows from the exact averaged compatibility equation and the already-proved leading profile. The earlier Cid--Mawhin--Zima Fredholm averaging paper treats a semilinear framework and different applications; it does not contain this vector \(p\)-Laplacian Duffing coefficient. A same-author companion preprint excludes the nondifferentiable \(p\)-Laplacian case \(p\neq2\) from its implicit-function framework.

## Limitations
The formula does not give the full next-order time-dependent waveform. If \(g_j''(\alpha_j)=0\) or \(w_j\equiv0\), it only proves that the mean displacement is \(o(\varepsilon^{2/(p-1)})\); a later nonzero term would require additional analysis. The result concerns the local periodic responses supplied by the cited averaging theorem and does not address their dynamical stability.

## References
1. J. Mawhin and J. Novoa, "An abstract averaging method for quasilinear equations," arXiv:2610.02155v1, 2026, especially Corollary 2.5 and Proposition 3.1.
2. J. A. Cid, J. Mawhin, and M. Zima, "An abstract averaging method with applications to differential equations," Journal of Differential Equations 274 (2021), 231--250, DOI 10.1016/j.jde.2020.11.051.
3. J. Mawhin and J. Novoa, "An averaging method for periodic solutions of quasilinear equations in Banach spaces," arXiv:2610.02156v1, 2026.
