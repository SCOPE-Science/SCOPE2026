# Sharp exclusion probability for one forbidden grand-coupling map

## Finding

Fix an integer \(n\ge2\), let \(S=\{1,\ldots,n\}\), and fix any function \(f:S\to S\). Write \(\mathcal F=S^S\) and \(\mathcal G=\mathcal F\setminus\{f\}\). A row-stochastic matrix \(P=(p_{ij})\) is **representable without \(f\)** if there exists a probability measure on \(\mathcal G\) with one-coordinate marginals \(\Pr(F(i)=j)=p_{ij}\). For every strictly positive row-stochastic matrix,

\[
P\text{ is representable without }f\quad\Longleftrightarrow\quad \sum_{i=1}^{n}p_{i,f(i)}\le n-1.
\]

Now let \(U_{ij}\), \(1\le i,j\le n\), be independent uniform random variables on \((0,1)\), and set \(p_{ij}=U_{ij}/\sum_{k=1}^n U_{ik}\). Denote the probability that \(P\) is **not** representable without \(f\) by \(q_n\). This probability does not depend on the choice of \(f\), and

\[
\boxed{\displaystyle q_n\sim\frac{\exp(n+1/2)}{n^n\,[n(n-1)]!}\qquad(n\to\infty).}
\]

For \(n=2\), the exact value is \(q_2=1/2\). In particular, the probability of representability with one preassigned map excluded tends to one extraordinarily rapidly; the displayed asymptotic identifies its sharp multiplicative correction.

## Assumptions and scope

The state space is the labeled set \(S\) of cardinality \(n\). The coupling is a law on **deterministic functions** \(S\to S\), not a law on stochastic matrices and not a restriction on the maps occurring at every time in an arbitrary Markovian construction. The measure may give zero mass to additional functions. The matrix is strictly positive and hence irreducible; this is automatic almost surely in the sampled model. The sampling law is **row normalization of independent uniform \((0,1)\) entries**, not the uniform Dirichlet distribution on each row. The map \(f\) may be arbitrary and need not be injective.

Set \(a=n-1\). The asymptotic concerns the one-map omission event as \(n\to\infty\), with a different (but arbitrary preassigned) function permitted at each \(n\). It makes no assertion about simultaneously excluding multiple prescribed functions or about coalescence time.

## Proof

**1. Characterization of the support restriction.** Let \(B_i=\mathbf1_{\{F(i)=f(i)\}}\) and \(x_i=p_{i,f(i)}\). If a coupling gives zero mass to \(f\), then \(\sum_iB_i\le n-1\) almost surely, so \(\sum_i x_i\le n-1\). Conversely, the polytope

\[
\left\{x\in[0,1]^n:\sum_i x_i\le n-1\right\}
=\operatorname{conv}\left(\{0,1\}^n\setminus\{(1,\ldots,1)\}\right).
\]

Indeed, any vertex is integral: if the sum inequality is inactive, it is a cube vertex; if active, all but at most one coordinate are at bounds, forcing the remaining coordinate to be an integer. Thus any admissible \(x\) is the vector of means of a random binary vector \(B\) that never equals \((1,\ldots,1)\). Conditional on \(B_i=1\), set \(F(i)=f(i)\); conditional on \(B_i=0\), sample \(F(i)\ne f(i)\) using probabilities \(p_{ij}/(1-x_i)\). These auxiliary choices can be made independently given \(B\), and their marginals equal the prescribed rows. All denominators are positive because \(P\) is strictly positive and \(n\ge2\). Every realized function differs from \(f\) at some coordinate. This proves the equivalence.

**2. Independent deficit coordinates.** Define \(D_i=1-p_{i,f(i)}\). Because the input rows are independent and exchangeable within each row, the \(D_i\) are independent with a common law independent of \(f\). Let \(U\sim\mathrm{Uniform}(0,1)\) and let \(S_a\) be a sum of \(a\) independent \(\mathrm{Uniform}(0,1)\) random variables, independent of \(U\). Then \(D\stackrel{d}{=}S_a/(U+S_a)\). Put \(R=S_a/U\), so \(D=R/(1+R)\). If \(g_a\) denotes the density of \(S_a\),

\[
f_R(r)=\int_0^1 u\,g_a(ru)\,du,\qquad r>0.
\]

For every \(s>0\), \(g_a(s)\le s^{a-1}/(a-1)!\), because the density of a sum of \(a\) nonnegative uniforms is bounded by the corresponding unrestricted simplex-section volume. Equality holds for \(0<s\le1\). Consequently

\[
f_R(r)\le\frac{a}{n!}\,r^{a-1},\qquad
f_D(d)\le\frac{a}{n!}\,d^{a-1}(1-d)^{-n},\quad0<d<1,
\]

with equality throughout \(0<d\le1/2\). Here and below \(n!=n(n-1)!\). By Step 1, the exclusion event is \(\sum_iD_i<1\), with the boundary having probability zero.

**3. A Dirichlet simplex comparison.** Let \(\nu_n\) be the Dirichlet law on \(d_1,\ldots,d_n\ge0\), \(\sum_id_i\le1\), having parameters \((a,\ldots,a,1)\) (the last parameter belongs to the slack coordinate). Set \(M=\max_id_i\) and \(W=\prod_i(1-d_i)^{-n}\). The product density bound above gives, with

\[
A_n=\left(\frac{a}{n!}\right)^n
\int_{\sum d_i<1}\prod_i d_i^{a-1}\,d\mathbf d
=\frac{1}{n^n\,[na]!},
\]

that

\[
A_n\,\mathbb E_{\nu_n}[W\mathbf1_{\{M\le1/2\}}]
\ \le\ q_n\ \le\ A_n\,\mathbb E_{\nu_n}[W].
\]

The lower integrand is exact on \(\{M\le1/2\}\), because each one-coordinate density attains its upper bound there. The standard multivariate beta integral gives the displayed closed expression for \(A_n\).

**4. Bulk asymptotics and uniform integrability.** Under \(\nu_n\), let \(G_0\sim\mathrm{Gamma}(1,1)\) and \(G_i\sim\mathrm{Gamma}(a,1)\) independently for \(1\le i\le n\), and write \(T=G_0+\sum_iG_i\), \(d_i=G_i/T\). Exponential concentration for gamma variables, together with independence, yields

\[
nM\to1,\qquad n\sum_i d_i^2\to1,\qquad
n\left(1-\sum_i d_i\right)\to0
\]

in probability. For example, \(T/[na]\to1\); the maximum of the \(n\) variables \(G_i/a\) tends to one by gamma Chernoff bounds and a union bound; and \(\sum_iG_i^2/(na^2)\to1\) by a second-moment estimate. Since \(M\to0\), Taylor expansion with its uniform remainder gives

\[
\log W=n\sum_i\left(d_i+\frac{d_i^2}{2}
+O\!\left(\frac{d_i^3}{1-M}\right)\right)
=n+\frac12+o_{\mathbb P}(1).
\]

It remains to justify passage to expectations. On \(M\le1/2\), using \(-\log(1-d)\le d+d^2/[2(1-d)]\) and \(\sum_i d_i^2\le M\sum_i d_i\le M\), we have \(W/e^n\le e^{nM}\). The variables \(e^{nM}\) are uniformly integrable: split according to \(T\ge na/2\). On that event \(nM\le2\max_iG_i/a\), and fixed exponential moments of \(2\max_iG_i/a\) are uniformly bounded for large \(n\), since \(\max_iG_i\le2a\) except with exponentially small probability, by gamma Chernoff bounds and a union bound (using an exponential tilt on the tail). On \(T<na/2\), the deterministic bound \(nM\le n\) and the gamma lower tail \(\Pr(T<na/2)\le e^{-c n a}\) give a vanishing contribution to every fixed exponential moment. Finitely many small \(n\) cause no issue. Hence

\[
\mathbb E_{\nu_n}\left[W\mathbf1_{\{M\le1/2\}}\right]
\sim e^{n+1/2}.
\]

**5. The omitted simplex corners are negligible.** Suppose \(n\ge3\) and \(M>1/2\). There is exactly one coordinate \(d_i=t>1/2\). For every \(j\ne i\), \(1-d_j\ge t\) and \(\sum_{j\ne i}d_j\le1-t\), so

\[
\prod_{j\ne i}(1-d_j)^{-n}
\le\exp\left(\frac{n(1-t)}{t}\right)\le e^n.
\]

The marginal \(d_i\) is \(\operatorname{Beta}(a,b)\) with \(b=(n-1)a+1\). Thus \(b-n=(n-1)(n-2)>0\), and

\[
\begin{aligned}
\mathbb E_{\nu_n}[W\mathbf1_{\{M>1/2\}}]
&\le ne^n\,\mathbb E_{\nu_n}[(1-d_1)^{-n}\mathbf1_{\{d_1>1/2\}}]\\
&\le ne^n\frac{\Gamma(na+1)}{\Gamma(a)\Gamma(b)}
\frac{2^{-(b-n)}}{b-n}\\
&\le ne^n\frac{(na+1)^a}{\Gamma(a)}
\frac{2^{-(b-n)}}{b-n}=e^{-\Omega(n^2)}.
\end{aligned}
\]

Combining Steps 3–5 proves \(q_n\sim A_ne^{n+1/2}\), as claimed. Finally, for \(n=2\), the obstruction condition is \(p_{1,f(1)}+p_{2,f(2)}>1\). Two selected entries from independent, identically distributed rows are independent and symmetric about \(1/2\), so the event has probability \(1/2\).

## Verification

The standalone file `verify.py` executes finite linear-programming feasibility checks of the support restriction for sample sizes \(n=2,3\), independent numerical density-integral checks for the \(n=3\) coordinate law, exact factorial-normalization calculations, and Dirichlet importance-sampling checks of the asymptotic correction at \(n=5,8,12,20,40,80\). Run `python verify.py` with Python 3, NumPy, and SciPy installed. On the recorded execution, 259 finite checks passed; the importance-sampling normalized ratios at the six dimensions were 0.956741, 0.977207, 0.984713, 0.991160, 0.995598, and 0.998153. These checks are supportive and are **not** a substitute for Steps 1–5 of the proof.

## Relationship to prior work

Grimmett and Holmes, *Coalescence in Markov Chains*, Section 7, define \(\mathcal P(\mathcal G)\), pose Question 7.4 on its probability under the row-normalized independent-uniform random matrix law defined in their Remark 2.4, and establish \(1/2\) when \(n=2\) and exactly one map is forbidden (Proposition 7.5). Their accessible complete article does not give the stated higher-dimensional asymptotic. The present result is a sharp large-state answer for that same natural one-map restriction, not a claim about arbitrary \(\mathcal G\). The polytope criterion is an elementary marginal-coupling observation; the main advance is the sharp high-dimensional normalized-uniform probability with the \(e^{1/2}\) correction. The earlier *Non-coupling from the past* addresses attainable coalescence numbers, not this random-matrix exclusion asymptotic in its accessible abstract.

## Limitations

The input distribution is row-normalized independent \(\mathrm{Uniform}(0,1)\) variables; the result is not asserted for Dirichlet-distributed rows, other input distributions, or dependent rows. The sharp relative asymptotic is only as \(n\to\infty\) and does not provide uniform quantitative remainder bounds. The proof does not resolve Question 7.4 for sets obtained by forbidding multiple functions. Although published-source and research-record comparisons did not identify this asymptotic, unrecognized equivalent treatments under rare-event simplex integrals or marginal-coupling terminology remain possible. No independent validation has been performed.

## References

1. G. R. Grimmett and M. Holmes, *Coalescence in Markov Chains*, arXiv:2510.13572, first public version 15 October 2025; *Journal of Theoretical Probability* **39** (2026), article 49. https://arxiv.org/abs/2510.13572 ; https://doi.org/10.1007/s10959-026-01500-w . Primary material inspected: full open-access journal HTML, especially Remark 2.4 and Section 7, Questions 7.1/7.4 and Propositions 7.3–7.6.
2. G. R. Grimmett and M. Holmes, *Non-coupling from the past*, arXiv:1907.05605, 2019 preprint; in *In and Out of Equilibrium 3* (2021). https://arxiv.org/abs/1907.05605 . Accessible abstract inspected; full text not examined.
