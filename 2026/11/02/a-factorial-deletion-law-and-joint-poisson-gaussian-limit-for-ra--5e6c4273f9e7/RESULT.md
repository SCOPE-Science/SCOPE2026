# A factorial deletion law and joint Poisson–Gaussian limit for random chord diagrams

## Finding

For each integer \(n\ge2\), let \(D_n\) be a uniformly random perfect matching of \(2n\) labeled points in cyclic order. Let \(S_n\) count chords joining cyclically consecutive endpoints (including the wrap-around pair), and let \(C_n\) count pairs of crossing chords. Put \(C_0=0\), and let \(T_m(v)=\mathbb E[v^{C_m}]\) for integers \(m\ge0\).

For \(0\le r\le n\), define
\[
M_{n,r}=\frac{2n}{2n-r}\binom{2n-r}{r},\qquad
b_{n,r}=M_{n,r}\frac{(2n-2r-1)!!}{(2n-1)!!},
\]
where \((-1)!!=1\). The following **exact joint probability-generating identity** holds for all complex \(u,v\):
\[
\boxed{\mathbb E[u^{S_n}v^{C_n}]
=\sum_{r=0}^{n}(u-1)^r b_{n,r}T_{n-r}(v).}
\tag{1}
\]
Equivalently, for every bounded function \(f\) on the nonnegative integers and every \(0\le r\le n\),
\[
\boxed{\mathbb E[(S_n)_r f(C_n)]
=r!b_{n,r}\,\mathbb E[f(C_{n-r})],}
\tag{2}
\]
where \((s)_r=s(s-1)\cdots(s-r+1)\) and \((s)_0=1\).

Writing \(\mu_n=n(n-1)/6\) and \(\sigma_n^2=n(n-1)(n+3)/45\), the exact Pearson correlation is
\[
\boxed{\operatorname{Corr}(S_n,C_n)=-\sqrt{\frac5{n+3}}.}
\tag{3}
\]
More strongly, as \(n\to\infty\),
\[
\boxed{\left(S_n,\frac{C_n-\mu_n}{\sigma_n}\right)
\Longrightarrow (P,Z),\qquad
P\sim\operatorname{Poisson}(1),\ Z\sim N(0,1),\ P\perp Z.}
\tag{4}
\]
In particular, the standardized crossing count also converges to \(N(0,1)\) **conditional on having no simple chords**.

## Assumptions and scope

The matching is uniform over all \((2n-1)!!\) pairings of the labeled, cyclically ordered endpoints. A crossing means the alternating circular order of four distinct endpoints of two chords; a simple chord joins adjacent endpoints. All stated finite identities hold for integers \(n\ge2\), including \(r=0\) and \(r=n\). For a zero-chord matching, \(C_0\) is deterministically zero; for \(n=1\), the two descriptions of the single adjacent cyclic edge coincide, so the finite formulas are deliberately restricted to \(n\ge2\). The convergence statements concern \(n\to\infty\) in this fixed uniform model.

## Proof

**1. Exact deletion identity.** The graph of allowed simple edges on the \(2n\) endpoints is the cycle graph. The number of its \(r\)-edge matchings is
\[
M_{n,r}=\frac{2n}{2n-r}\binom{2n-r}{r},\qquad 0\le r\le n.
\]
To derive this without a generating function, write \(2n\) binary marks around a cycle with exactly \(r\) nonadjacent marked edges. Count marked cycles with a distinguished selected edge: choose the distinguished edge in \(2n\) ways, then place the \(r\) positive separation gaps among the remaining \(2n-r\) unmarked/marked slots. This gives the displayed standard circular matching count, including the two perfect alternating selections at \(r=n\).

For any prescribed collection of \(r\) disjoint simple chords, the probability all occur is \((2n-2r-1)!!/(2n-1)!!\). Conditional on their occurrence, the remaining endpoints are paired uniformly. Removing these forced chords and preserving the cyclic order leaves a uniform chord diagram with \(n-r\) chords. Every removed chord crossed no other chord, while deletion does not alter the interleaving of any four remaining endpoints. Hence the remaining diagram has **exactly the same crossing count** as the original and its conditional crossing law is \(C_{n-r}\).

Expanding \((S_n)_r\) as the sum over ordered \(r\)-tuples of distinct simple chords counts each unordered admissible collection \(r!\) times. The conditional-deletion observation therefore yields (2), including arbitrary bounded test functions. The binomial identity \(u^s=\sum_{r=0}^{s}(u-1)^r(s)_r/r!\) yields (1), a polynomial identity. In particular, coefficient extraction at \(u=0\) gives the exact crossing-count distribution among diagrams with no simple chord:
\[
\Pr(S_n=0,C_n=c)=\sum_{r=0}^n(-1)^r b_{n,r}\Pr(C_{n-r}=c).
\tag{5}
\]

**2. Finite covariance and correlation.** The cases \(r=1\) and \(r=2\) of (2) give
\[
\mathbb ES_n=\frac{2n}{2n-1},\qquad
\mathbb E(S_n)_2=\frac{2n}{2n-1},\qquad
\operatorname{Var}(S_n)=\frac{4n(n-1)}{(2n-1)^2}.
\]
Using the known exact crossing moments \(\mathbb EC_m=m(m-1)/6\) and \(\operatorname{Var}(C_m)=m(m-1)(m+3)/45\), (2) at \(r=1\) yields
\[
\operatorname{Cov}(S_n,C_n)
=\frac{2n}{2n-1}\left(\mu_{n-1}-\mu_n\right)
=-\frac{2n(n-1)}{3(2n-1)}.
\]
Dividing by the two exact standard deviations gives (3). These established marginal moments and the simple-chord covariance are background inputs/consequences, not independently claimed as a new discovery; the principal result is the full mixed-factorial deletion law and joint asymptotic independence.

**3. Mixed factorial limits and independence.** Fix an integer \(r\ge0\). As \(n\to\infty\), elementary ratios in the finite formula give \(r!b_{n,r}\to1\). For every bounded continuous \(g:\mathbb R\to\mathbb R\), apply (2) to
\(f(c)=g((c-\mu_n)/\sigma_n)\) to obtain
\[
\mathbb E\!\left[(S_n)_r g\!\left(\frac{C_n-\mu_n}{\sigma_n}\right)\right]
=r!b_{n,r}\;\mathbb E\!\left[g\!\left(\frac{C_{n-r}-\mu_n}{\sigma_n}\right)\right].
\]
The published crossing central limit theorem applies to \(C_{n-r}\) because \(n-r\to\infty\). Moreover \((\mu_{n-r}-\mu_n)/\sigma_n=O(n^{-1/2})\to0\) and \(\sigma_{n-r}/\sigma_n\to1\), so the right side converges to \(\mathbb Eg(Z)\) for \(Z\sim N(0,1)\). In particular all factorial moments of \(S_n\) tend to one, proving its Poisson limit.

To justify the stronger joint claim rather than merely deduce decorrelation, note the two marginal limits make the joint laws tight. Along any convergent subsequence \((S_n,Z_n)\Rightarrow(S,Z)\), all fixed moments of \(S_n\) are uniformly bounded: express ordinary moments as finite linear combinations of its factorial moments. Consequently \((S_n)_r g(Z_n)\) is uniformly integrable, and the limiting mixed identity is \(\mathbb E[(S)_r g(Z)]=\mathbb Eg(Z)\) for every nonnegative bounded continuous \(g\) and every \(r\). For a fixed such \(g\), summing these identities by monotone convergence gives
\[
\mathbb E[g(Z)(1+t)^S]
=\mathbb Eg(Z)\sum_{r=0}^{\infty}\frac{t^r}{r!}
=e^t\mathbb Eg(Z),\qquad t\ge0.
\]
Uniqueness of the probability-generating function implies that the conditional law of \(S\) given \(Z\) is \(\operatorname{Poisson}(1)\), independent of \(Z\). Every subsequential limit is therefore the same product law, proving (4).

Finally, \(\Pr(S_n=0)\to e^{-1}>0\). Because \(S_n\) is integer-valued, the zero-event is a continuity event of the joint limit. Dividing the joint probability \(\Pr(S_n=0,Z_n\le t)\to e^{-1}\Phi(t)\) by \(\Pr(S_n=0)\) proves the conditional central limit theorem.

## Verification

The included standalone \(\texttt{check.py}\) enumerates all uniform perfect matchings on \(2n\) labeled endpoints for \(2\le n\le6\), computes cyclic simple-chord and crossing counts directly, and compares the **full mixed crossing-count distribution for each factorial order** against the deletion formula, using exact rational arithmetic. It also checks the finite means, variances, and covariance. The complete replay reports 266 exact assertions passed; the largest finite enumeration has 10,395 matchings. No finite calculation is treated as proof of the infinite-dimensional joint limit.

To replay, extract \(\texttt{check.py}\) and run \(\texttt{python check.py}\) using Python 3 standard library. The displayed identities were separately derived symbolically as in the Proof section.

## Relationship to prior work

Flajolet and Noy (2000, Theorem 3) establish the exact crossing mean and variance and the marginal Gaussian limit; the Touchard–Riordan crossing polynomial is also classical. Acan (2015 preprint; 2017 article) analyzes the random chord diagram and its intersection graph, including monolithic structure. Paguyo (first posted 2021-04-02; Theorems 1.1–1.2) gives quantitative normal and Poisson approximations for crossing and simple-chord **marginals**, respectively. Krasko and Omelchenko (2016 preprint; 2017 article) enumerate loopless chord diagrams, including generating functions in loop counts, without a simultaneous crossing count.

The distinction here is simultaneous dependence: two marginal limit theorems do not imply their limiting independence. The exact marked-deletion relation (2) yields the finite joint law (1), the mixed factorial identities, the product limit (4), and crossing asymptotics conditioned on excluding simple chords. The simple-chord/crossing covariance by itself is already readily derivable from prescribed-chord conditioning and is not claimed as a novel standalone formula.

## Limitations

No rate of joint convergence or uniform approximation in a growing factorial order is established. The Poisson–Gaussian product is specific to fixed adjacent cyclic chords and the uniform perfect matching law; arbitrary chord-length classes and nonuniform matchings are outside scope. The proof uses established marginal crossing asymptotics; it does not independently reprove them. Priority remains subject to possible earlier equivalent multi-parameter generating functions, and independent validation has not been performed.

## References

1. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134v1, publicly posted 2021-04-02, especially Sections 1–4 and Theorems 1.1–1.2. https://arxiv.org/abs/2104.01134
2. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, 2000, Theorem 3. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf ; DOI: 10.1007/978-3-662-04166-6_17.
3. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, 2015; journal article 2017. https://arxiv.org/abs/1501.01489
4. E. Krasko and A. Omelchenko, *Enumeration of Chord Diagrams without Loops and Parallel Chords*, arXiv:1601.05073v1, 2016. https://arxiv.org/abs/1601.05073
