# An exact isolated-gap distribution and harmonic tail law for reflective numerical semigroups

## Finding
Let \(g\ge2\) be an integer, and choose a reflective numerical semigroup \(S\) of genus \(g\) uniformly from all such semigroups. Here *reflective* means that its \(g\) gaps occupy distinct residue classes modulo \(g\). An *isolated gap* is a gap \(h\) with \(h-1,h+1\in S\). Write \(I_g\) for the number of isolated gaps, \(\tau\) for the divisor-counting function, \(\sigma\) for the sum-of-divisors function, and
\[
D(g)=\sum_{d=1}^{g}\left\lfloor\frac gd\right\rfloor.
\]
Then the population has \(N_g=g+1-\tau(g)\) members. For every integer \(k\ge1\), put \(b=\lfloor g/k\rfloor\), and define \(d_g(b)=\#\{a:2\le a\le b,\ a\mid g\}\). Its **exact tail count** is
\[
\begin{aligned}
C_g(k):=N_g\Pr(I_g\ge k)
={}&\max(0,b-1)-d_g(b)\\
&+\mathbf1_{\{k\ge2,\ (k-1)\mid(g-1),\ (g-1)/(k-1)\ge2\}}\\
&+\mathbf1_{\{g\ \mathrm{odd},\ (g+1)/2<k\le g\}}.
\end{aligned}
\]
Furthermore,
\[
\boxed{\sup_{k\ge1}\left|\Pr(I_g\ge k)-\frac1k\right|\le\frac{2\tau(g)+4}{g+1-\tau(g)}.}
\]
This uniform rate has the **optimal divisor-count scale**. For \(g\ge3\),
\[
\Pr(I_g\ge2)-\frac12=
\begin{cases}
\displaystyle\frac{3-\tau(g)}{2N_g},&g\text{ even},\\[4pt]
\displaystyle\frac{2-\tau(g)}{2N_g},&g\text{ odd}.
\end{cases}
\]
Thus a family with \(\tau(g)\to\infty\), such as \(g=2^t\), forces an error of order \(\tau(g)/g\); the displayed uniform bound is therefore sharp in order along divisor-rich genera.

Consequently, as \(g\to\infty\),
\[
\Pr(I_g=k)\longrightarrow\frac{1}{k(k+1)}\qquad(k=1,2,3,\ldots).
\]
The limiting distribution has an infinite mean, and the finite-genus means satisfy the **exact identity**
\[
\boxed{\mathbb E I_g=
\frac{D(g)-\sigma(g)+\tau(g-1)-1+\frac{g-1}{2}\mathbf1_{\{g\ \mathrm{odd}\}}}{g+1-\tau(g)}.}
\]
In particular \(\mathbb E I_g\sim\log g\). Exactly one reflective semigroup of genus \(g\ge2\) has no isolated gaps: the ordinary semigroup \(\{0\}\cup[g+1,\infty)\). When \(g\) is odd, the unique multiplicity-two member has all \(g\) gaps isolated, producing a finite-population extreme outlier.

## Assumptions and scope
A numerical semigroup is a cofinite additive submonoid of \(\mathbb N_0\). The genus is the number of missing positive integers. The probability is the **uniform counting measure on semigroups of a fixed genus**, not on numerical integers or on all numerical semigroups. All claims concern integers \(g\ge2\), \(k\ge1\); indicator conditions involving divisibility apply only when their divisors are positive. The asymptotics run through every integer genus, not just prime genera.

The parametrization of reflective semigroups by genus \(g\) and multiplicity \(a\), \(2\le a\le g+1\), \(a\nmid g\), and the explicit gap decomposition are established in Shor's earlier work. They are inputs, not claimed as new results. The contribution here is an exact isolated-gap histogram and its uniform heavy-tail limit, with an exact mean, a quantified approximation bound, and its order-sharpness on divisor-rich genera.

## Proof
**1. The isolated-gap count for a given multiplicity.** Fix \(2\le a\le g+1\) with \(a\nmid g\), and write \(g=qa+r\), \(1\le r<a\). Shor's classification (Proposition 3.4 and its proof, arXiv:2207.00051v1) yields precisely
\[
H(S)=\{h:1\le h<g,\ a\nmid h\}\ \cup\ \{g+ja:0\le j\le q\}.
\]
For \(a\ge3\), no gap strictly below \(g\) is isolated: when its two neighbors also lie below \(g\), both would have to be divisible by \(a\), contradicting \(a\ge3\); the boundary gap \(g-1\), when present, has the gap \(g\) to its right. Every upper-layer gap \(g+ja\) with \(j\ge1\) is isolated because its two neighbors belong to the semigroup. The initial upper-layer gap \(g\) is isolated exactly when \(a\mid(g-1)\), equivalently \(r=1\). For \(a=2\), the nondivisibility condition forces \(g\) odd; all gaps are odd with both even neighbors in \(S\), so all \(g\) gaps are isolated. Consequently,
\[
I(g,a)=\left\lfloor\frac ga\right\rfloor+\mathbf1_{\{a\mid(g-1)\}}+\frac{g-1}{2}\mathbf1_{\{a=2,\ g\ \mathrm{odd}\}}.
\]
This also proves that exactly \(a=g+1\) gives \(I(g,a)=0\) for \(g\ge2\).

**2. Exact population tails.** The base condition \(\lfloor g/a\rfloor\ge k\) counts precisely the admissible multiplicities in \([2,\lfloor g/k\rfloor]\), namely \(\max(0,b-1)-d_g(b)\). The bonus \(\mathbf1_{\{a\mid(g-1)\}}\) adds one more semigroup to \(I_g\ge k\) precisely when \(\lfloor g/a\rfloor=k-1\), that is, \(k\ge2\) and \(a=(g-1)/(k-1)\ge2\) is integral. The multiplicity-two exception contributes one further member for \((g+1)/2<k\le g\) when \(g\) is odd. This proves the displayed formula for \(C_g(k)\).

**3. Uniform bound.** The base count differs from \(g/k\) by at most \(\tau(g)+2\), while the two corrections each lie in \(\{0,1\}\). Therefore \(|C_g(k)-g/k|\le\tau(g)+4\) for all \(g\ge2,k\ge1\). As \(|N_g-g|=\tau(g)-1\), division by \(N_g\) proves the boxed uniform error bound. For \(k=2\) and \(g\ge3\), every divisor of \(g\) other than \(1,g\) lies at most \(g/2\), so \(d_g(\lfloor g/2\rfloor)=\tau(g)-2\). The divisor-of-\(g-1\) correction contributes exactly one, and the multiplicity-two outlier correction contributes zero. Hence \(C_g(2)=\lfloor g/2\rfloor+2-\tau(g)\), which proves the sharp-scale formula in the finding. The standard divisor estimate \(\tau(g)=o(g)\) proves uniform convergence of the tails; differencing adjacent tails gives the limiting mass \(1/[k(k+1)]\). Its sum is one by telescoping, while its mean diverges by comparison with the harmonic series.

**4. Exact mean and asymptotics.** Sum the multiplicity formula over \(a=2,\ldots,g+1\) with \(a\nmid g\). The floor-term sum equals \(D(g)-\sigma(g)\): subtract \(\sum_{a\mid g}g/a=\sigma(g)\) from \(\sum_{a=1}^{g+1}\lfloor g/a\rfloor=D(g)\). The indicator \(a\mid(g-1)\) contributes \(\tau(g-1)-1\). There is a single multiplicity-two correction of \((g-1)/2\) for odd \(g\). Divide by \(N_g\).

The elementary hyperbola method gives \(D(g)=g\log g+O(g)\). Also \(\sigma(g)/g=\sum_{d\mid g}d^{-1}=o(\log g)\): for any fixed \(\epsilon>0\), split divisors at \(g^\epsilon\); the small-divisor contribution is at most \(\epsilon\log g+O(1)\), and the large-divisor contribution is at most \(\tau(g)g^{-\epsilon}=o(1)\), using \(\tau(g)=O_\delta(g^\delta)\) with \(0<\delta<\epsilon\). Since \(N_g\sim g\) and the remaining corrections are \(O(g)\), the mean is asymptotic to \(\log g\).

## Verification
The independent finite enumeration script `reflection_gap_verify.py` uses only the Python standard library. It constructs semigroups from Shor's generators and checks, without relying on the predicted gap lists, all actual gap sets and isolated-gap positions for 4,668 admissible genus/multiplicity pairs with \(1\le g\le100\). It separately verifies exact tail counts, means, uniqueness of the perfect member, the uniform inequality, and its sharp order at tail level two for every genus \(2\le g\le1200\), comprising 467,488 tail-level checks. All assertions passed. These are finite checks of explicit identities; the infinite statements follow from the mathematical proof above. Reproduce with `python3 reflection_gap_verify.py`.

## Relationship to prior work
Shor, *Reflective Numerical Semigroups* (2022 preprint, 2023 journal), gives the complete classification by genus and multiplicity and the requisite explicit gap sets; thus the elementary local gap description is **already derivable from published work** and is not independently claimed as an original classification. Smith (2022) developed the isolated-gap/perfect-semigroup framework, and Singh and Ram (2024) classified isolated gaps in embedding dimension two, covering the multiplicity-two reflective case. The new statement examined here is the fixed-genus isolated-gap **distribution**, its exact arithmetic tail law and uniform \(1/k\) limit, and the logarithmically divergent mean. Later work on minimum isolated gaps of two-generated semigroups studies a different invariant and restricted generator families. No inspected primary text gives the exact fixed-genus distribution or tail limit. It remains possible that the asymptotic is an unrecorded or implicit consequence elsewhere.

## Limitations
The fixed-genus law is not a claim about the distribution of isolated gaps across all numerical semigroups. The heavy-tail limit has infinite mean even though every finite-genus population has a finite mean. The existing complete reflective-semigroup parametrization is essential; no new classification of numerical semigroups is claimed. Results have not received independent scientific validation. The bibliographic search cannot rule out unpublished or unindexed derivations, and one older isolated-gap source could only be inspected by its abstract, not its entire text.

## References
1. C. M. Shor, *Reflective Numerical Semigroups*, arXiv:2207.00051v1, publicly posted 30 June 2022, Proposition 3.4 and proof, Corollary 3.6, Proposition 5.2; Albanian Journal of Mathematics 17 (2023), 41–68. https://arxiv.org/abs/2207.00051
2. H. J. Smith, *On isolated gaps in numerical semigroups*, Turkish Journal of Mathematics 46 (2022), 123–129. DOI: 10.3906/mat-2107-54.
3. S. N. Singh and R. K. Ram, *On Isolated Gaps of Numerical Semigroups of Embedding Dimension Two*, arXiv:2406.09848v1, posted 14 June 2024. https://arxiv.org/abs/2406.09848
4. N. Sawatraksa et al., *The Minimum Isolated Gap in Numerical Semigroups...*, European Journal of Pure and Applied Mathematics 19 (2026), article 7641, restricted two-generator families. https://www.ejpam.com/ejpam/article/view/7641/2771
