# Sharp boundary-regularity transition for intermittent return excesses

## Finding

Consider the Liverani–Saussol–Vaienti intermittent map with parameter \(\alpha>0\):
\[
T_\alpha(x)=\begin{cases}
x(1+2^\alpha x^\alpha),&0\le x\le 1/2,\\
2x-1,&1/2<x\le1.
\end{cases}
\]
Let \(Y=(1/2,1]\). Take an initial point in \(Y\) according to a probability density \(\rho\) (Lebesgue density, not necessarily invariant) having the boundary asymptotic
\[
\rho(1/2+t)=c\,t^\kappa\bigl(1+d\,t^\beta+o(t^\beta)\bigr)
\quad(t\downarrow0),
\]
where \(c>0\), \(\kappa>-1\), \(\beta>0\), and \(d\in\mathbb R\setminus\{0\}\). The density is assumed nonnegative and integrable on \(Y\). Let \(\tau\) denote the first positive return time to \(Y\). Define, for \(u\ge1\) and integers \(n\ge1\),
\[
S_n(u)=\Pr_\rho\{\tau>\lfloor un\rfloor\mid\tau>n\}.
\]
Set
\[
r=\kappa+1,\quad p=r/\alpha,\quad \delta=\beta/\alpha,
\quad C_\alpha=(\alpha 2^\alpha)^{-1/\alpha},
\quad Q_\alpha=\frac{1+\alpha}{2\alpha^2},
\quad L=\frac{dr}{r+\beta}\,2^{-\beta}C_\alpha^\beta.
\]
The limiting excess survival law is Pareto, \(S_n(u)\to u^{-p}\), **uniformly over all** \(u\ge1\). Its first nonzero error has a sharp transition at the boundary-density exponent \(\beta=\alpha\):

**Rough boundary correction, \(0<\beta<\alpha\):**
\[
\sup_{u\ge1}\left|n^\delta\bigl(S_n(u)-u^{-p}\bigr)
-Lu^{-p}(u^{-\delta}-1)\right|\longrightarrow0,
\]
\[
\lim_{n\to\infty}n^\delta\sup_{u\ge1}|S_n(u)-u^{-p}|
=|L|\frac{\delta}{p+\delta}\left(\frac p{p+\delta}\right)^{p/\delta}>0.
\]

**Smooth enough boundary correction, \(\beta\ge\alpha\):**
\[
\sup_{u\ge1}\left|\frac n{\log n}\bigl(S_n(u)-u^{-p}\bigr)
-rQ_\alpha u^{-p}(u^{-1}-1)\right|\longrightarrow0,
\]
\[
\lim_{n\to\infty}\frac n{\log n}\sup_{u\ge1}|S_n(u)-u^{-p}|
=rQ_\alpha\frac1{p+1}\left(\frac p{p+1}\right)^p>0.
\]
The maxima are attained in the limiting profiles at \(u=(1+\delta/p)^{1/\delta}\) and \(u=1+1/p\), respectively. Both constants are exact, so neither asserted rate can be improved within the stated density class. For the unmodified return time, the moment criterion is \(\mathbb E_\rho[\tau^s]<\infty\) precisely when \(0<s<p\); this remains true for \(\alpha\ge1\), when the usual invariant measure is infinite.

## Assumptions and scope

The map and return section are exactly as defined above, with \(\alpha>0\). No invariance, differentiability away from \(1/2\), or monotonicity of \(\rho\) is assumed. The stated positive and integrable boundary form guarantees that \(\rho\) defines a probability law after normalization. The little-oh expansion is required only from the right of \(1/2\). The return-time law conditions on \(\tau>n\) under that initial law; it is not a statement about conditioning on avoiding a remote open hole under the global invariant measure. Endpoints of branch intervals have probability zero.

## Proof

**1. Exact return cylinders.** Write \(f(x)=x(1+2^\alpha x^\alpha)\) on \([0,1/2]\) and define \(x_0=1/2\), \(x_{j+1}=f^{-1}(x_j)\). The sequence decreases to zero. A point starting in \(Y\) has first image \(2y-1\), and its next iterates stay in the left branch through time \(n\) exactly when \(2y-1\le x_{n-1}\). Hence for every integer \(n\ge1\),
\[
\Pr_\rho\{\tau>n\}
=\int_{1/2}^{(1+x_{n-1})/2}\rho(y)\,dy
=:\Phi(x_{n-1}).
\]
In particular, \(S_n(u)=\Phi(x_{\lfloor un\rfloor-1})/\Phi(x_{n-1})\) **exactly**.

**2. Second-order inverse orbit.** Put \(b=2^\alpha\), \(w_j=x_j^{-\alpha}\), \(A=\alpha b\), and \(B=\alpha(1+\alpha)b^2/2\). Since \(x_j=f(x_{j+1})\), Taylor expansion at zero gives
\[
w_{j+1}-w_j
=w_{j+1}\bigl[1-(1+b/w_{j+1})^{-\alpha}\bigr]
=A-\frac B{w_{j+1}}+O_\alpha(w_{j+1}^{-2}).
\]
As \(w_j\to\infty\), its increments tend to \(A>0\), hence \(w_j=Aj+o(j)\). The displayed expansion then improves this to \(w_j=Aj+O_\alpha(\log j)\). Substitution gives
\[
\frac1{w_{j+1}}=\frac1{A(j+1)}+O_\alpha\!\left(\frac{\log(j+1)}{(j+1)^2}\right).
\]
The error series is summable, yielding
\[
w_j=Aj-\frac BA\log j+O_\alpha(1),
\quad
x_j=C_\alpha j^{-1/\alpha}\left(1+Q_\alpha\frac{\log j}{j}+O_\alpha(j^{-1})\right).
\]
Here \(B/(\alpha A^2)=Q_\alpha\). These are analytical all-index asymptotics; no numerical extrapolation is used.

**3. Boundary integration and uniform ratios.** Let \(r=\kappa+1\). Integrating the assumed density asymptotic gives
\[
\Phi(z)=\frac{c}{r2^r}z^r
\left[1+\frac{dr}{r+\beta}2^{-\beta}z^\beta+o(z^\beta)\right]
\quad(z\downarrow0).
\]
Uniformly in real \(u\ge1\), setting \(k=\lfloor un\rfloor-1\) entails \(k=un+O(1)\) and \(k\ge n-1\). Thus both \(k^{-p}=(un)^{-p}(1+O(n^{-1}))\) and
\[
\frac{\log k}{k}=\frac{\log n}{nu}+O(n^{-1})
\]
hold uniformly, since \(\sup_{u\ge1}(\log u)/u<\infty\). All relative remainder bounds are uniform because \(x_k\le x_{n-1}\to0\). Inserting the last two expansions into the exact ratio from step 1 gives, uniformly for \(u\ge1\), the leading correction
\[
S_n(u)=u^{-p}\left[1+
L n^{-\delta}(u^{-\delta}-1)
+rQ_\alpha\frac{\log n}{n}(u^{-1}-1)
+o(n^{-\delta})+O(n^{-1})+O\!\left(\frac{(\log n)^2}{n^2}\right)
\right]
\]
where the \(o(n^{-\delta})\) term is relative to the boundary-density remainder. For \(\delta<1\), the first correction dominates; for \(\delta\ge1\), the logarithmic term dominates. This yields the two claimed **uniform profile** limits. The more detailed joint remainder display is used only for these comparisons; no claim of a universal next-order coefficient is made.

**4. Optimal constants and moments.** For positive \(p,\eta\), the function \(u^{-p}(1-u^{-\eta})\), \(u\ge1\), has its unique maximum at \(u=(1+\eta/p)^{1/\eta}\) and maximum \(\frac\eta{p+\eta}(p/(p+\eta))^{p/\eta}\). Uniform profile convergence therefore gives the two exact positive constants. Finally, step 3 implies \(\Pr_\rho\{\tau>n\}\asymp n^{-p}\); applying the discrete tail-sum criterion gives finite moments exactly for \(s<p\), with divergence at the boundary \(s=p\).

## Verification

The standalone script `verify.py` checks the inverse-branch identity and return cylinder endpoints for four representative intermittent parameters and evaluates twelve finite-horizon normalized-error measurements for four boundary-density choices. It reports `VERIFY_OK return_cylinder_tests=52 weighted_cases=4 normalized_rate_checks=12` when executed with Python 3. Its finite samples are sanity checks; the uniform limits and the universal quantifiers are proved in the preceding steps.

## Relationship to prior work

Korepanov, Wei and Wormell (arXiv:2610.01879, 2026) already develop an Abel-function asymptotic expansion for the left LSV branch and analyze invariant densities and mean returns; the logarithmic inverse-orbit term is not claimed to originate here. Wang and Su (arXiv:2610.21175, 2026) establish first-order return-tail estimates and open-system conditional laws, including an \(O(\log n/n)\) inverse-orbit bound. Neither examined work states the **sharp initial-boundary-regularity phase transition** in the distribution of normalized *first-return excesses*, its two distinct explicit uniform bias profiles, and their exact Kolmogorov constants for arbitrary \(\kappa>-1\), \(\beta>0\), and \(\alpha>0\). This result uses the shared inverse-branch framework but concerns a different choice of initial law and a different statistical quantity.

## Limitations

The theorem is for the exact two-branch LSV map and the canonical section \((1/2,1]\), not arbitrary intermittent maps or holes. The correction coefficient \(d\) must be nonzero; if it vanishes, a higher boundary expansion determines the leading correction. The asymptotic is for the conditional *first-return time*, not a global open-system Birkhoff-sum limit. Broader second-order regular-variation theory may provide alternative derivations; an exhaustive historical-priority certification is not asserted. All claims of convergence and optimality are analytical, with no reliance on finite experiments for infinite quantifiers.

## References

- A. Korepanov, Y. Wei and C. Wormell, *Rigorous and effective numerics for Liverani–Saussol–Vaienti maps*, arXiv:2610.01879v1, first posted 2026-10-01, especially Sections 2 and 5. https://arxiv.org/abs/2610.01879
- C. Wang and Y. Su, *Conditional limit laws for open intermittent dynamics*, arXiv:2610.21175v1, first posted 2026-10-15, especially Lemma 4.1 and the induced-return construction. https://arxiv.org/html/2610.21175v1
- M. Demers and B. Fernandez, *Escape rates and singular limiting distributions for intermittent maps with holes*, arXiv:1410.4995, 2014. https://arxiv.org/abs/1410.4995
- J. Duvall, *Survivor-conditioned renewal laws and observable bounds for open intermittent maps*, arXiv:2606.27488v1, 2026. https://arxiv.org/abs/2606.27488
