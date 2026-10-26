# A sharp logarithmic compactness threshold for Dirichlet-series Volterra operators

## Finding

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). For \(z\in\mathbb D\), define
\[
L(z)=1-\operatorname{Log}(1-z),\qquad M(z)=2+\operatorname{Log}L(z),
\]
where \(\operatorname{Log}\) is the principal logarithm. For each real parameter \(\alpha\), set
\[
H_\alpha(z)=M(z)^\alpha-2^\alpha,\qquad g_\alpha(s)=H_\alpha(2^{-s}),\quad \operatorname{Re}s>0,
\]
with \(M^\alpha=\exp(\alpha\operatorname{Log}M)\). These branches are analytic on \(\mathbb D\), and \(H_\alpha(0)=0\); hence \(g_\alpha\) is an ordinary Dirichlet series supported on powers of \(2\).

For the Volterra operator
\[
T_{g_\alpha}f(s)=-\int_s^{+\infty}f(w)g_\alpha'(w)\,dw,
\]
the exact parameter trichotomy is:

- If \(\alpha<1\), then \(T_{g_\alpha}\) is compact on both \(BMOA_{\mathcal D}\) and \(VMOA_{\mathcal D}\).
- If \(\alpha=1\), then \(T_{g_1}\) is bounded on both spaces, but is neither compact, weakly compact, nor completely continuous on either space.
- If \(\alpha>1\), then \(T_{g_\alpha}\) is unbounded on both spaces.

More precisely, write \(Q(t,h)=\{\sigma+i\tau:0<\sigma<h,\ t<\tau<t+h\}\), \(d\mu_g(s)=|g'(s)|^2\sigma\,d\sigma\,d\tau\), and
\[
[g]_{LMOA_{\mathcal D},\delta}=\sup_{t\in\mathbb R,\ 0<h\le\delta}\log(e/h)\left(\frac{\mu_g(Q(t,h))}{h}\right)^{1/2}.
\]
For every fixed \(\alpha\ne0\) and sufficiently small \(h\), the per-scale profile satisfies
\[
\log(e/h)\left(\frac{\sup_{t\in\mathbb R}\mu_{g_\alpha}(Q(t,h))}{h}\right)^{1/2}\asymp_\alpha |\alpha|\bigl(\log\log(e/h)\bigr)^{\alpha-1}.
\]
Consequently, for \(\alpha<1\), \(\alpha\ne0\), the small-scale seminorm tends to zero; for \(\alpha=1\) it stays bounded away from zero; and for \(\alpha>1\) it is infinite. At \(\alpha=0\), \(g_0\equiv0\) and \(T_{g_0}=0\).

## Assumptions and scope

All logarithms are principal branches on the domains specified above. Since \(\operatorname{Re}L(z)=1-\log|1-z|>1-\log2>0\), \(\operatorname{Log}L\) is analytic. Also \(|L(z)|\ge\operatorname{Re}L(z)>1-\log2\), so \(\operatorname{Re}M(z)>2+\log(1-\log2)>0\); therefore \(M^\alpha\) is analytic for every real \(\alpha\). The symbol has zero constant Dirichlet coefficient. The result concerns the stated family and the two spaces \(BMOA_{\mathcal D}\) and \(VMOA_{\mathcal D}\); it does not assert an exact numerical value for the operator essential norm or classify other symbols.

## Proof

For \(\alpha\ne0\), differentiation gives
\[
H_\alpha'(z)=\frac{\alpha M(z)^{\alpha-1}}{(1-z)L(z)},\qquad
 g_\alpha'(s)=-(\log2)2^{-s}H_\alpha'(2^{-s}).
\]
As \(z\to1\) within \(\mathbb D\), put \(r=|1-z|\). Then \(|L(z)|\asymp\log(e/r)\) and \(|M(z)|\asymp\log\log(e/r)\). Thus, for each fixed nonzero \(\alpha\),
\[
|H_\alpha'(z)|\asymp_\alpha\frac{(\log\log(e/r))^{\alpha-1}}{r\log(e/r)}.
\]
The boundary singularities of \(g_\alpha\) occur at \(s=i\tau_k\), where \(\tau_k=2\pi k/\log2\), \(k\in\mathbb Z\). Near each such point, \(|1-2^{-s}|\asymp(\sigma^2+|\tau-\tau_k|^2)^{1/2}\). Hence the density of \(\mu_{g_\alpha}\) near that boundary point is comparable to
\[
\frac{\sigma\,(\log\log(e/r))^{2\alpha-2}}{r^2\log^2(e/r)},\qquad r=(\sigma^2+|\tau-\tau_k|^2)^{1/2}.
\]
In polar coordinates in the half-plane, \(\sigma=r\cos\theta\), so integration over a box of side \(h\) containing a singular height gives
\[
\mu_{g_\alpha}(Q(\tau_k,h))\asymp_\alpha
\int_0^h\frac{(\log\log(e/r))^{2\alpha-2}}{\log^2(e/r)}\,dr
\asymp_\alpha h\frac{(\log\log(e/h))^{2\alpha-2}}{\log^2(e/h)}.
\]
The lower bound follows by restricting to a fixed angular sector inside the box. For the upper bound uniformly in \(t\), use the periodicity in \(\tau\) and split each box into dyadic shells about the nearest \(\tau_k\). If the interval is within distance \(2h\) of a singular height, the same polar estimate applies; if its distance is \(d>2h\), the contribution is bounded by the near-scale expression times a constant, since the factor \((h/d)^2\) dominates the ratios of the slowly varying logarithmic factors. Boxes a fixed distance from all \(\tau_k\) have bounded derivative and contribute \(O_\alpha(h^3)\). Therefore the displayed per-scale profile is valid uniformly after taking the supremum over \(t\).

The definition of \([g]_{LMOA_{\mathcal D},\delta}\) now yields, for \(\alpha<1\), \(\alpha\ne0\),
\[
[g_\alpha]_{LMOA_{\mathcal D},\delta}\asymp_\alpha |\alpha|\bigl(\log\log(e/\delta)\bigr)^{\alpha-1}\longrightarrow0.
\]
For \(\alpha=1\), the same seminorm is bounded above and below by positive constants at small scales. For \(\alpha>1\), its supremum over \(0<h\le\delta\) diverges for every \(\delta>0\). The same box bounds at fixed scales show that the cases \(\alpha\le1\) lie in \(BMOA_{\mathcal D}\), so the logarithmic-mean-oscillation criterion applies. Theorem 1.1 of Tong, Wang, and Yuan identifies boundedness of \(T_g\) on both spaces with \(g\in LMOA_{\mathcal D}\); Theorem 1.2 identifies compactness, weak compactness, and complete continuity with \(g\in LMOA_{\mathcal D,0}\). These two criteria give the stated trichotomy. For \(\alpha=0\), the symbol is identically zero, so the conclusion is immediate.

## Verification

The branch domains and derivative identity are checked directly above. The critical estimate is a boundary Carleson-box integral, not a finite numerical experiment: polar coordinates give the lower bound near a singular height, and the dyadic-shell estimate gives the uniform upper bound. The proof establishes the infinite-scale statements; no finite computation is used to infer compactness or unboundedness. The constants in \(\asymp_\alpha\) may depend on the fixed parameter \(\alpha\). No exact numerical essential-norm constant is claimed.

## Relationship to prior work

Tong, Wang, and Yuan characterize boundedness of \(T_g\) on \(BMOA_{\mathcal D}\) and \(VMOA_{\mathcal D}\) by \(g\in LMOA_{\mathcal D}\), and prove that compactness, weak compactness, and complete continuity are equivalent to membership in \(LMOA_{\mathcal D,0}\). Their Lemma 3.1 explains why one-variable analytic functions composed with \(2^{-s}\) yield Dirichlet-series symbols. Those general criteria do not evaluate the present one-parameter family. The additional result here is the explicit logarithmic Carleson-box profile and the sharp parameter boundary for this lifted family, rather than a new general compactness criterion.

The classical one-variable Volterra theory cited in the recent paper is relevant to the critical double-logarithmic boundary behavior. The specific power-family calculation in the Dirichlet-series half-plane is the object of this finding; priority for the one-variable critical example alone is not claimed.

## Limitations

The result supplies asymptotic comparability, not an exact leading constant for the Carleson profile or the essential norm of \(T_{g_\alpha}\). The classification is restricted to the explicit symbols \(g_\alpha\) and to the two stated spaces. A prior one-variable result may contain an equivalent critical example; the claim does not assert priority for that classical example, and the family-specific half-plane profile is the asserted contribution.

## References

1. C. Tong, M. Wang, and Z. Yuan, *Volterra operators on the BMOA space of Dirichlet series*, arXiv:2610.21873v1, first submitted 15 October 2026; Theorems 1.1–1.2 and Lemma 3.1.
2. A. Aleman and A. Siskakis, *An integral operator on \(H^p\)* (1995), and A. Siskakis and R. Zhao, *A Volterra type operator on spaces of analytic functions* (1999), as cited for the classical one-variable context in the introduction of reference 1. The full text of reference 2 was not used to assert noncoverage.
