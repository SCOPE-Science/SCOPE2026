# Critical-tail binomial thinning: universal multiple-survivor law and an exact total-variation profile

## Finding

Let \(X\) be a nonnegative integer-valued population count, and retain each member independently with probability \(\varepsilon\in(0,1)\). Write \(T_\varepsilon\mid X\sim\operatorname{Bin}(X,\varepsilon)\). At the critical infinite-mean tail
\[
\Pr(X\ge k)\sim \frac{c}{k},\qquad c>0,
\]
the probability of seeing at least one member is much larger than that of seeing at least two:
\[
\Pr(T_\varepsilon\ge1)\sim c\varepsilon\log(1/\varepsilon),\qquad
\Pr(T_\varepsilon\ge r)\sim\frac{c\varepsilon}{r-1}\quad(r\ge2\text{ fixed}).
\]
In particular, \(\Pr(T_\varepsilon\ge2\mid T_\varepsilon\ge1)\sim1/\log(1/\varepsilon)\). Conditional on **at least** \(r\ge2\) survivors, the entire count approaches the universal law
\[
\mathcal L(T_\varepsilon\mid T_\varepsilon\ge r)\xrightarrow{\mathrm{TV}}Q_r,
\qquad Q_r\{j\}=\frac{r-1}{j(j-1)}\ (j\ge r).
\]

For the canonical integer Pareto law \(\Pr(X=k)=1/[k(k+1)]\) for \(k\ge1\), let \(Q_\varepsilon=\mathcal L(T_\varepsilon\mid T_\varepsilon\ge2)\) and \(Q_0=Q_2\). For every \(0<\varepsilon<1\), the likelihood ratios \(Q_\varepsilon\{j\}/Q_0\{j\}\) increase strictly with \(j\), with \(Q_\varepsilon\{2\}<Q_0\{2\}\) and \(Q_\varepsilon\{j\}>Q_0\{j\}\) for all \(j\ge3\). Moreover,
\[
\boxed{d_{\mathrm{TV}}(Q_\varepsilon,Q_0)
=\frac{\varepsilon[(1+\varepsilon)\log(1/\varepsilon)-2(1-\varepsilon)]}{2(1-\varepsilon)[1-\varepsilon-\varepsilon\log(1/\varepsilon)]}
\sim\frac{\varepsilon\log(1/\varepsilon)}{2}.}
\]
The displayed finite-parameter identity, rather than numerical curve fitting, determines the sharp asymptotic rate.

## Assumptions and scope

The random count \(X\) is almost surely finite and integer-valued; its tail has the stated first-order asymptotic with a finite positive constant \(c\). The thinning trials are conditionally independent given \(X\). All limits are as \(\varepsilon\downarrow0\), and \(r\) is held fixed. The exact distance and monotone-likelihood-ratio statements require the canonical law and apply at every strictly interior thinning probability. The source distribution may have infinite expectation.

## Proof

**Tail-generating identity.** Put \(a_k=\Pr(X\ge k)\), \(A(z)=\sum_{k\ge1}a_kz^{k-1}\), \(0<z<1\), and \(G_X(z)=\mathbb E[z^X]\). Summation by parts yields \(G_X(z)=1-(1-z)A(z)\). Because \(G_{T_\varepsilon}(z)=G_X(1-\varepsilon+\varepsilon z)\), differentiating the zero-through-\((r-1)\) truncation gives the exact identity
\[
\Pr(T_\varepsilon\ge r)
=\frac{\varepsilon^r}{(r-1)!}A^{(r-1)}(1-\varepsilon),\qquad r=1,2,\ldots.
\tag{1}
\]
One can also prove (1) termwise by checking a deterministic initial count and averaging.

**Critical Abelian estimate.** Since \(a_k\sim c/k\), splitting its generating sum at \(1/\varepsilon\) and bounding the geometric tail proves \(A(1-\varepsilon)\sim c\log(1/\varepsilon)\). For every fixed integer \(h\ge1\), termwise differentiation and comparison to the corresponding power series of the logarithm give
\[
A^{(h)}(1-\varepsilon)\sim c(h-1)!\varepsilon^{-h}.
\tag{2}
\]
For completeness, replace \(a_k\) beyond a sufficiently large index by \((c\pm\delta)/k\); finitely many initial terms contribute only bounded derivatives, whereas \(\sum_{k\ge1}z^{k-1}/k=-\log(1-z)/z\). Let \(\delta\downarrow0\). Inserting (2) into (1) proves all asserted tail asymptotics. Subtraction gives \(\Pr(T_\varepsilon=j)\sim c\varepsilon/[j(j-1)]\) for fixed \(j\ge2\). After division by \(\Pr(T_\varepsilon\ge r)\), every limiting conditional mass is \((r-1)/[j(j-1)]\); these masses sum to one by telescoping. Pointwise convergence of probability masses to another mass function of total mass one implies total-variation convergence (the countable Scheffé argument).

**Canonical integral representation.** For \(\Pr(X=k)=1/[k(k+1)]\), use \(1/[k(k+1)]=\int_0^1(1-v)v^{k-1}\,dv\) and sum the binomial generating series. For \(j\ge2\),
\[
p_j(\varepsilon):=\Pr(T_\varepsilon=j)
=\varepsilon\int_0^1r_\varepsilon(v)(1-v)v^{j-2}\,dv,\quad
r_\varepsilon(v)=\frac{v}{\varepsilon+(1-\varepsilon)v}.
\tag{3}
\]
Writing \(D(\varepsilon)=\Pr(T_\varepsilon\ge2)\), the identity \(\sum_{j\ge2}(1-v)v^{j-2}=1\) gives
\[
D(\varepsilon)=\varepsilon\int_0^1r_\varepsilon(v)\,dv
=\frac{\varepsilon[1-\varepsilon+\varepsilon\log\varepsilon]}{(1-\varepsilon)^2}.
\tag{4}
\]
Direct integration at \(j=2\) gives
\[
p_2(\varepsilon)=
\frac{\varepsilon[1-\varepsilon^2+2\varepsilon\log\varepsilon]}{2(1-\varepsilon)^3}.
\tag{5}
\]

**One crossing, all finite parameters.** Let \(V_j\sim\operatorname{Beta}(j-1,2)\) and \(U\sim\operatorname{Unif}[0,1]\). Normalizing (3) using \(\int_0^1(1-v)v^{j-2}\,dv=1/[j(j-1)]\) yields
\[
\frac{Q_\varepsilon\{j\}}{Q_0\{j\}}=
\frac{\mathbb E r_\varepsilon(V_j)}{\mathbb E r_\varepsilon(U)}.
\tag{6}
\]
The family \(V_j\) is strictly stochastically increasing in \(j\), and \(r_\varepsilon\) is strictly increasing, so (6) increases strictly. Since \(V_2\sim\operatorname{Beta}(1,2)\) is strictly stochastically smaller than \(U\), the ratio at \(j=2\) is below one. At \(j=3\), the beta density is \(6v(1-v)\). The symmetrized function \(s(v)=[r_\varepsilon(v)+r_\varepsilon(1-v)]/2\) is strictly increasing on \((0,1/2)\), because \(r_\varepsilon'\) is strictly decreasing; so is \(v(1-v)\). Their positive covariance under uniform measure on \([0,1/2]\) proves \(\mathbb E r_\varepsilon(V_3)>\mathbb E r_\varepsilon(U)\). The ratio therefore exceeds one at \(j=3\) and at every larger index. This proves the claimed single crossing.

The total-variation distance consequently equals the sole deficit \(Q_0\{2\}-Q_\varepsilon\{2\}=1/2-p_2(\varepsilon)/D(\varepsilon)\). Substitution of (4) and (5) gives the boxed closed form. Its denominator stays positive because \(D(\varepsilon)>0\), and expansion at zero yields the asserted sharp leading constant.

## Verification

The companion standalone `verify.py` checks exact closed formulas for \(D(\varepsilon)\) and \(p_2(\varepsilon)\) against beta-integral evaluations; compares integrals with directly truncated binomial-mixture sums for several thinning parameters and survivor counts; checks selected likelihood-ratio inequalities and small-thinning distance trends; and tests the generating-tail identity on arbitrary finite distributions. It reports 125 successful checks when run with Python and `mpmath`. These checks corroborate finite calculations only: the universal limits, monotonicity for every real parameter and sharp total-variation asymptotics are established by the proof above.

## Relationship to prior work

Kella and Löpker [1, Theorem 11] establish that conditioning a thinned count on being nonzero yields a point mass at one when the original count has finite mean, and a Sibuya limit for regularly varying tails with exponent strictly between zero and one. Their theorem does not state the present critical exponent-one multiple-survivor conditional laws. The critical case is delicate because the one-survivor event has an additional logarithmic factor. Klebanov and Šumbera [2] describe Sibuya-related distributions, and Levina and Priesemann [3] analyze power-law subsampling. Neither inspected text asserts the canonical exact finite-parameter likelihood-ratio crossing and total-variation formula. These comparisons concern the stated results, not a claim of exhaustive historical priority.

## Limitations

The universal conclusion assumes the exact asymptotic \(\Pr(X\ge k)\sim c/k\); a general varying slowly varying multiplier is not covered. Conditional thresholds \(r\) are fixed, not growing with the thinning parameter. The sharp exact total-variation expression is restricted to the specified canonical law. No claim is made about optimal convergence rates for arbitrary exponent-one tails, about an independence certificate, or about historical priority beyond the materials inspected. The code does not replace the all-parameter analytical proof.

## References

[1] O. Kella and A. Löpker, *On Binomial Thinning and Mixing*, arXiv:2202.10296 (first version 2022-02-21), Theorem 11 and §2–3; *Indagationes Mathematicae* 34 (2023), 1121–1145. https://arxiv.org/html/2202.10296v3

[2] L. B. Klebanov and M. Šumbera, *On Sibuya-like distributions in branching and birth-and-death processes*, arXiv:2204.08871 (2022). https://arxiv.org/html/2204.08871v2

[3] A. Levina and V. Priesemann, *Subsampling scaling*, *Nature Communications* 8 (2017), article 15140. https://www.nature.com/articles/ncomms15140
