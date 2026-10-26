# Exact Bessel jamming law for alternating-rate dimers on the integer chain

## Finding
Consider irreversible nearest-neighbor dimer adsorption on the infinite vertex chain \(\mathbb Z\), initially empty. Each edge \(\{j,j+1\}\) independently proposes a dimer at Poisson rate \(\alpha>0\) for even \(j\), or \(\beta>0\) for odd \(j\). The first proposal on an edge occupies its two vertices if both are vacant; otherwise all proposals there fail. Occupation is permanent. Put
\[
\nu=\frac{\alpha}{\alpha+\beta},\qquad \mu=\frac{\beta}{\alpha+\beta},\qquad h=\nu\mu,
\]
and write \({}_0F_1(;c;z)=\sum_{m\ge0} z^m/[m!(c)_m]\). Every vertex has the same vacancy probability \(p(t)\). Its limiting value, and hence the exact jammed coverage \(\Theta=1-p(\infty)\), is
\[
\boxed{p(\infty)=\frac{h}{2+h}\,{}_0F_1(;2+\nu;h)\,{}_0F_1(;2+\mu;h).}
\]
The formula holds for *every* positive rate pair. It reduces to the standard \(p(\infty)=e^{-2}\) when \(\alpha=\beta\). More sharply, for \(\varepsilon=\min(\alpha,\beta)/\max(\alpha,\beta)\downarrow0\),
\[
\boxed{p(\infty)=\frac{\varepsilon}{2}-\frac{5\varepsilon^2}{6}+O(\varepsilon^3).}
\]
Thus the jammed vacancy fraction decreases linearly toward zero in the strongly staggered regime, with exact first and second coefficients. The finite-time vacancy law is also explicit in modified Bessel functions, as proved below.

## Assumptions and scope
Edges are undirected and have independent homogeneous-in-time Poisson attempt processes of the stated positive rates. A dimer excludes other dimers sharing either endpoint. The initial state is completely vacant, and the observable is the probability that a fixed lattice vertex has never been covered by time \(t\ge0\). Reflection about the midpoint of an edge exchanges even and odd vertices without changing edge-rate parity, so their vacancy probabilities coincide. Infinite-volume dynamics is defined through finite intervals and consistent finite-time local limits; the local dependence expansion has factorially decaying boundary influence for bounded rates.

## Proof
**Step 1: two half-chain cavities.** Remove the boundary edge of a semi-infinite path. Let \(A(t)\) be the probability that its endpoint remains vacant through time \(t\) when the first remaining edge has rate \(\alpha\), and \(B(t)\) the analogous quantity when that rate is \(\beta\). Conditioning on the independent exponential time of that first edge and requiring the other endpoint to be vacant in the path with this first edge deleted gives
\[
A'(t)=-\alpha e^{-\alpha t}B(t),\qquad B'(t)=-\beta e^{-\beta t}A(t),\qquad A(0)=B(0)=1.
\]
These equations describe genuine random-greedy matching on a chain; no mean-field factorization is used. To cover a vertex through its \(\alpha\)-edge at first-attempt time \(s\), both endpoints must be vacant in the two independent residual half-chains, each of cavity type \(B\). The \(\beta\)-edge similarly has two residual cavities of type \(A\). Consequently
\[
p'(t)=-\alpha e^{-\alpha t}B(t)^2-\beta e^{-\beta t}A(t)^2=(A(t)B(t))'.
\]
Because \(p(0)=A(0)B(0)=1\), we have \(p(t)=A(t)B(t)\) for all \(t\ge0\).

**Step 2: exact finite-time solution.** Eliminating \(B\) yields
\[
A''+\alpha A'-\alpha\beta e^{-(\alpha+\beta)t}A=0,
\]
with \(A(0)=1\), \(A'(0)=-\alpha\). Let \(x=2\sqrt h\), \(z(t)=x\exp[-(\alpha+\beta)t/2]\), and let \(I_\rho,K_\rho\) denote the usual modified Bessel functions. The substitution \(A(t)=z(t)^\nu U(z(t))\) gives the modified Bessel equation of order \(\nu\). Its unique initial-value solution is
\[
A(t)=x\left(\frac{z(t)}x\right)^\nu\bigl[K_{\nu+1}(x)I_\nu(z(t))+I_{\nu+1}(x)K_\nu(z(t))\bigr].
\]
Interchanging \(\nu,\mu\) gives the same formula for \(B\). The normalization and initial derivative follow from the Bessel Wronskian identity \(I_\rho(x)K_{\rho+1}(x)+I_{\rho+1}(x)K_\rho(x)=1/x\) and standard order-recurrence identities.

**Step 3: jammed density.** Since \(\nu,\mu>0\), the limits \(z^\rho K_\rho(z)\to2^{\rho-1}\Gamma(\rho)\) and \(z^\rho I_\rho(z)\to0\) as \(z\downarrow0\) give
\[
A(\infty)=2^{\nu-1}\Gamma(\nu)x^{1-\nu}I_{\nu+1}(x)
=\frac{h}{\nu(1+\nu)}{}_0F_1(;2+\nu;h),
\]
\[
B(\infty)=\frac{h}{\mu(1+\mu)}{}_0F_1(;2+\mu;h).
\]
Their product simplifies because \(\nu+\mu=1\), \(\nu\mu=h\), and \((1+\nu)(1+\mu)=2+h\), proving the boxed formula. At equal rates, the cavity equations have \(A=B=\exp(e^{-\alpha t}-1)\); hence \(p(\infty)=e^{-2}\).

**Step 4: sharp strongly staggered expansion.** By rate-exchange symmetry set \(\beta/\alpha=\varepsilon\). Then \(\nu=(1+\varepsilon)^{-1}\), \(\mu=\varepsilon/(1+\varepsilon)\), and \(h=\varepsilon/(1+\varepsilon)^2\). Inserting the absolutely convergent hypergeometric series gives, as \(\varepsilon\downarrow0\),
\[
\frac{h}{2+h}=\frac\varepsilon2-\frac{5\varepsilon^2}{4}+O(\varepsilon^3),\qquad
{}_0F_1(;2+\nu;h){}_0F_1(;2+\mu;h)=1+\frac{5\varepsilon}{6}+O(\varepsilon^2).
\]
Multiplication gives \(p(\infty)=\varepsilon/2-5\varepsilon^2/6+O(\varepsilon^3)\), as claimed. Analyticity in \(\varepsilon\) near zero follows from the hypergeometric series with parameters in a compact subset of \((0,\infty)\).

## Verification
The provided standalone program `verify.py` evaluates the hypergeometric expression, an independently integrated pair of cavity differential equations, and the Bessel finite-time solution. Independently, it enumerates complete edge-arrival orders with *exact rational probabilities* on small finite paths, verifying a first-edge path recursion; that recursion then approximates the infinite-volume vacancy probability on successively longer paths. It also checks \(e^{-2}\) and the two-term small-minority-rate expansion. All 61 assertions grouped into four families passed in the recorded execution. The finite-path comparisons support, but do not replace, the infinite-chain derivation above. Run `python verify.py` after installing the dependencies in `requirements.txt`.

## Relationship to prior work
The homogeneous one-dimensional dimer result \(\Theta=1-e^{-2}\) and exact-solvability machinery are classical and expressly *not* new here. De Oliveira, Tomé and Dickman (1992) study unequal deposition orientation rates on the **square lattice**, and their Appendix treats homogeneous one-dimensional dimer deposition; their model does not furnish the two-period **bond** rate law above. Loscar, Borzi and Albano (2003) analyze jamming fluctuations on random and binary-alloy substrates, including a one-dimensional system where some bonds are forbidden; they do not evaluate a positive-two-rate periodic Bessel law. Privman and Yan (2016) analyze imprecise geometric landing sites with homogeneous site rate and state the classic lattice benchmark; geometric positional imprecision is not the alternating-clock system solved here. These comparisons distinguish models and observables, not merely titles. Exact priority recursions and Bessel identities are established tools; the claimed evaluated result is the explicit all-rate alternating-bond vacancy function and its sharp minority-rate expansion.

## Limitations
The conclusion is specific to nearest-neighbor dimers, a deterministic period-two edge-rate pattern, independent Poisson arrivals, and one-dimensional infinite-volume occupancy. It neither asserts a rate-ratio monotonicity theorem nor gives a jammed-coverage variance, a full correlation function, or a result for general random rate disorder, non-Poisson arrivals or longer deposited objects. Historical coverage of every possible specialized periodic-deposition treatment has not been established.

## References
1. M. J. de Oliveira, T. Tomé, R. Dickman, *Anisotropic random sequential adsorption of dimers on a square lattice*, Physical Review A **46** (1992), 6294–6299. https://doi.org/10.1103/PhysRevA.46.6294
2. E. S. Loscar, R. A. Borzi, E. V. Albano, *Fluctuations of jamming coverage upon random sequential adsorption on homogeneous and heterogeneous media*, Physical Review E **68** (2003), 041106; public preprint arXiv:cond-mat/0312171. https://arxiv.org/abs/cond-mat/0312171
3. V. Privman, H. Yan, *Random Sequential Adsorption on Imprecise Lattice*, Journal of Chemical Physics **144** (2016), 244704; public preprint arXiv:1606.01823. https://arxiv.org/abs/1606.01823
4. J. W. Evans, *Random and cooperative sequential adsorption*, Reviews of Modern Physics **65** (1993), 1281–1329. https://doi.org/10.1103/RevModPhys.65.1281
