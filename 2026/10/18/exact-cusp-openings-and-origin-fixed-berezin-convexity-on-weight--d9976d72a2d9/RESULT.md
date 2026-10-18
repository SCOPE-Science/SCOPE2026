# Exact cusp openings and origin-fixed Berezin convexity on weighted Dirichlet spaces

## Finding
Let \(0<s<1\), and let \(\mathcal D_s\) be the reproducing-kernel Hilbert space on \(\mathbb D\) with kernel \(K_s(z,w)=(1-z\overline w)^{-s}\). For every holomorphic disk self-map \(\phi\) fixing the origin whose composition operator \(C_\phi\) is bounded on \(\mathcal D_s\), the Berezin range \(\operatorname{Ber}(C_\phi)\) is convex **if and only if** \(\phi(z)=a z\) for a real \(a\in[-1,1]\).

Moreover, let \(\phi\) be nonlinear and write its first nonlinear jet as
\[
\phi(z)=a z+bz^{m+1}+O(z^{m+2}),\qquad m\in\mathbb N,\quad b\ne0,\quad |a|<1.
\]
Put \(\vartheta=\arg(1-a)\), \(\nu=1+m/2\), and
\[
\kappa=\frac{|b|}{s^{m/2}|1-a|^{\nu}}>0.
\]
The Berezin transform is \(F(w)=((1-|w|^2)/(1-\overline w\phi(w)))^s\) (principal holomorphic power). Use the rotated coordinates \(x+iy=e^{-i\vartheta}(1-F(w))\). There is a small fixed neighborhood of the origin in these coordinates and a real-analytic function \(h(x)\), defined for \(x\ge0\) near zero, with \(h(0)=h'(0)=0\), such that for every sufficiently small \(x>0\), the vertical section of the locally transformed Berezin range is exactly an interval \([Y_-(x),Y_+(x)]\), where
\[
Y_\pm(x)=h(x)\pm\kappa x^{\nu}+O(x^{\nu+1/2}),\qquad x\downarrow0.
\]
The centerline is canonical: if \(F_a(t)=((1-t)/(1-at))^s\), \(U_a(t)=e^{-i\vartheta}(1-F_a(t))\), and \(t_a(x)\) is the unique small nonnegative solution of \(\operatorname{Re}U_a(t)=x\), then \(h(x)=\operatorname{Im}U_a(t_a(x))\). In particular, the half-width satisfies
\[
\frac{Y_+(x)-Y_-(x)}2\sim\kappa x^{1+m/2}.
\]
For fixed \(s\) and known \(a\), the local Berezin-range germ therefore determines both the least nonlinear degree \(m+1\) and the modulus \(|b|\). Every exponent \(3/2,2,5/2,\ldots\) is realized by a bounded composition operator with symbol \(\phi(z)=c z^{m+1}\), \(0<|c|<1\).

## Assumptions and scope
We use the exact kernel \(K_s\) as the norm definition of \(\mathcal D_s\). The symbol must map \(\mathbb D\) into itself, satisfy \(\phi(0)=0\), and induce a bounded composition operator; no boundedness of arbitrary disk symbols on \(\mathcal D_s\) is asserted. The nonlinear expansion uses the first nonzero coefficient after the linear term. The statement concerns the unweighted composition operator, not the general weighted operator \(C_{\psi,\phi}\). Sections are restricted to a sufficiently small neighborhood of the Berezin value \(1\); no global convexity or topology is inferred from numerical sampling.

## Proof
**1. Exact transform and exclusion of remote preimages.** Kernel evaluation gives
\[
F(w)=\langle C_\phi\widehat K_w,\widehat K_w\rangle=\left(\frac{1-|w|^2}{1-\overline w\phi(w)}\right)^s,\qquad F(0)=1.
\]
The denominator has positive real part, so the branch is unambiguous. If \(\phi\) is nonlinear then Schwarz's lemma gives \(|a|<1\). Schwarz--Pick for \(\psi(w)=\phi(w)/w\), with \(\psi(0)=a\), gives
\[
|\psi(w)|\le\frac{|a|+r}{1+|a|r},\quad r=|w|.
\]
Consequently
\[
|F(w)|^{1/s}\le\frac{1-r^2}{1-r^2|\psi(w)|}\le 1-\frac{(1-|a|)r^2}{1+r+r^2+|a|r}.
\]
For every \(r_0>0\) this bounds \(|F(w)|\) uniformly below \(1\) on \(|w|\ge r_0\). Thus \(F(w_j)\to1\) forces \(w_j\to0\): the local geometry at \(1\) has no remote branch.

**2. Uniform angular expansion.** Write \(w=\sqrt t e^{i\theta}\), \(t\ge0\), and \(\nu=1+m/2\). The nonlinear jet gives, uniformly in \(\theta\),
\[
\overline w\phi(w)=at+b t^{\nu}e^{im\theta}+O(t^{\nu+1/2}).
\]
Taylor expansion of the principal power at its nonzero denominator therefore yields
\[
F(w)=F_a(t)+s b t^{\nu} e^{im\theta}+O(t^{\nu+1/2}).
\]
Set \(U(t,\theta)=e^{-i\vartheta}(1-F(\sqrt t e^{i\theta}))\) and \(U_a(t)=e^{-i\vartheta}(1-F_a(t))\). Then
\[
U(t,\theta)=U_a(t)-s e^{-i\vartheta}b t^{\nu}e^{im\theta}+O(t^{\nu+1/2}),
\]
and \(U_a'(0)=s|1-a|>0\) is real. Uniformly in angle, \(\partial_t\operatorname{Re}U(t,\theta)=s|1-a|+O(t^{1/2})\) for small \(t>0\). (The angular remainder is analytic in \(\sqrt t\) and differentiable termwise.) Therefore, at every small horizontal level \(x>0\), there is a unique small radius square \(t=t(x,\theta)\) with \(\operatorname{Re}U(t,\theta)=x\), continuous in \(\theta\). Let \(t_a(x)\) be the inverse of \(\operatorname{Re}U_a\); then
\[
t(x,\theta)=t_a(x)+O(x^{\nu}),\qquad t_a(x)=\frac{x}{s|1-a|}+O(x^2).
\]
Since \(\operatorname{Im}U_a'(t)=O(t)\), substitution into the imaginary part gives, uniformly in \(\theta\),
\[
\operatorname{Im}U(t(x,\theta),\theta)=h(x)-s\operatorname{Im}(e^{-i\vartheta}be^{im\theta})\left(\frac{x}{s|1-a|}\right)^\nu+O(x^{\nu+1/2}).
\]
The map \(\theta\mapsto\operatorname{Im}U(t(x,\theta),\theta)\) is continuous on a connected circle, so its image is a full interval. Because \(m\ge1\), the harmonic leading term attains both \(+\kappa x^\nu\) and \(-\kappa x^\nu\). Uniform remainders then yield the stated exact vertical interval and both endpoint asymptotics. The separation estimate in step 1 ensures no other preimages contribute to these sufficiently local sections.

**3. Convexity classification.** The exact half-width is positive for small \(x\), so the nonlinear Berezin range has points whose transverse coordinate \(y\) differs from zero. But every point near the included endpoint \(1\) obeys \(y=h(x)+O(x^\nu)=o(x)\). If the full range were convex, its segment from \(1\) to any point with nonzero transverse-to-tangent coordinate would contain points tending to \(1\) with a fixed nonzero ratio \(y/x\), a contradiction. A transverse point exists by step 2. Hence nonlinear symbols cannot give convex ranges.

When \(\phi(z)=a z\), \(a\in\overline{\mathbb D}\), the Berezin range is the curve \(\{((1-t)/(1-at))^s:0\le t<1\}\). For real \(a\in[-1,1)\) it equals \((0,1]\), and for \(a=1\) it is \(\{1\}\). Conversely, if \(a\notin\mathbb R\), this curve is rectifiable with empty planar interior and is noncollinear with its accumulation points \(0\) and \(1\): its small-\(t\) tangent is \(-s(1-a)\), nonreal. A convex curve with empty planar interior must lie on a line, contradiction. Thus the only convex linear cases are the real ones. This also follows from the previously published linear-symbol classification.

**4. Recovery and sharpness.** The half-width identity implies \(\lim_{x\downarrow0}\log[(Y_+-Y_-)/2]/\log x=1+m/2\) and \(\lim_{x\downarrow0}(Y_+-Y_-)/(2x^{1+m/2})=\kappa\). Hence the least nonlinear degree and its coefficient modulus are recoverable when \(a,s\) are fixed. For \(\phi(z)=c z^{m+1}\) with \(0<|c|<1\), the composition operator is bounded on \(\mathcal D_s\): it maps the normalized monomial basis orthogonally to monomials with squared norm ratio \(\frac{(s)_k/k!}{(s)_{(m+1)k}/((m+1)k)!}|c|^{2k}\), which is asymptotic to \((m+1)^{1-s}|c|^{2k}\) as \(k\to\infty\). Therefore every indicated cusp order is genuinely attained in the stated operator class.

## Verification
The exact normed reproducing-kernel formula, Schwarz--Pick estimate, Taylor remainder and uniform angular inversion are analytic, not numerical. The included standalone standard-library checker evaluates exact Berezin transforms for 12 polynomial symbol families with nonreal linear terms and two small scales each, comparing 48 normalized upper/lower section extrema with the claimed coefficient. Run \(\texttt{python3 check_berezin_cusp.py}\). The finite diagnostics are supplementary and do not prove the asymptotic statements.

## Relationship to prior work
Barik, Sen and Paul (2026), Section 5 and Question 5.3, classify linear symbols and certain automorphisms on \(\mathcal D_s\) and explicitly pose the general weighted Dirichlet Berezin-range convexity problem. The classification above treats every **bounded unweighted origin-fixed** composition operator on \(0<s<1\) and supplies its local cusp exponent and constant. Augustine, Garayev and Shankar (2023) treat Hardy and Bergman elliptic/automorphic symbol families; their 2024 work concerns classical Dirichlet and Fock symbol families. Sen, Barik and Paul (2025) study weighted Bergman spaces and selected automorphisms. Bourdon, Le and Thompson (2026) obtain qualitative Hardy-space \(H^2\) cusp behavior and convexity information, and this is not claimed as new here; the present statement concerns the strictly fractional kernel range \(0<s<1\) with a sharp quantitative section law. The listed inspected works do not state this fractional weighted Dirichlet nonlinear classification or quantitative local section law.

## Limitations
There is no classification here for arbitrary symbols with \(\phi(0)\ne0\), for weighted operators \(C_{\psi,\phi}\), or for kernel exponents \(s\) outside \((0,1)\). No unproved generic boundedness is assumed. Possible independent rediscovery or equivalent formulations in uninspected articles remain publication-priority risks. Independent scientific auditing is outstanding.

## References
1. S. Barik, A. Sen, K. Paul, *Numerical range and Berezin range of weighted composition operators on weighted Dirichlet spaces*, arXiv:2602.09481v1 (first public 2026-02-10), Section 5, Question 5.3. https://arxiv.org/html/2602.09481v1
2. A. Augustine, M. Garayev, P. Shankar, *Composition operators, convexity of their Berezin range and related questions*, arXiv:2302.12547 (2023), Sections 4–5. https://arxiv.org/abs/2302.12547
3. A. Augustine, M. Garayev, P. Shankar, *On the convexity of the Berezin range of composition operators and related questions*, arXiv:2401.03176 (2024), Sections 2–3. https://arxiv.org/abs/2401.03176
4. A. Sen, S. Barik, K. Paul, *On the Berezin range of Toeplitz and weighted composition operators on weighted Bergman spaces*, arXiv:2506.04052 (2025), Section 4. https://arxiv.org/abs/2506.04052
5. P. Bourdon, T. Le, D. Thompson, *Berezin Ranges of Composition Operators on \(H^2\)*, arXiv:2610.17634 (2026), Sections 3–4. https://arxiv.org/abs/2610.17634
