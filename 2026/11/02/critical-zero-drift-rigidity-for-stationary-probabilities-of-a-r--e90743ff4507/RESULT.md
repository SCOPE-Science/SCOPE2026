# Critical zero-drift rigidity for stationary probabilities of a random interval map

## Finding

**Theorem.** Let \(\gamma_*\) be the unique solution in \((0,1)\) of
\[
2(\log 2-1)-\gamma_*(\log\gamma_*-1)=0.
\]
At each discrete time, independently select \(\beta\) uniformly from \([\gamma_*,2]\), and apply
\[
T_\beta(x)=\begin{cases}
\beta x,&0\le x\le\frac12,\\
2x-1,&\frac12<x\le1.
\end{cases}
\]
Every stationary Borel probability measure on \([0,1]\) is of the form
\[
\boxed{\mu=t\delta_0+(1-t)\delta_1,\qquad 0\le t\le1.}
\]
In particular, none charges the open interval and there is no absolutely continuous stationary probability at the zero-drift threshold.

## Assumptions and scope

The distribution of \(\beta\) is the normalized Lebesgue law \(d\beta/(2-\gamma_*)\) on \([\gamma_*,2]\), independently resampled at each iteration. The branch convention at the discontinuity \(x=1/2\) is the **left** branch. Stationarity means
\[
\int\varphi(x)\,d\mu(x)=\int\!\int\varphi(T_\beta(x))\,\frac{d\beta}{2-\gamma_*}\,d\mu(x)
\]
for every bounded Borel function \(\varphi\). No density, nonatomicity, or logarithmic moment of \(\mu\) is assumed. The result concerns stationary **probability** measures, not sigma-finite invariant measures or almost-sure convergence from nonstationary initial conditions.

The defining function \(q(\gamma)=2(\log2-1)-\gamma(\log\gamma-1)\) is continuous on \((0,1]\), strictly increasing since \(q'(\gamma)=-\log\gamma>0\), and satisfies \(q(0+)<0<q(1)\). Thus \(\gamma_*\) exists uniquely and
\[
\mathbb E[\log\beta]=\frac{q(\gamma_*)}{2-\gamma_*}=0.
\]
The endpoints \(0\) and \(1\) are fixed by every \(T_\beta\).

## Proof

**Step 1: a bounded logarithmic cutoff rules out stationary mass in the upper branch.** For each real \(M>0\), set
\[
h_M(0)=-M,\qquad h_M(x)=\max\{\log x,-M\}\quad(0<x\le1).
\]
This is a bounded Borel test function. For \(x\in(0,1/2]\), write \(u=\log x\), \(Z=\log\beta\), and \(g_M(v)=\max\{v,-M\}\). Since \(g_M\) is convex and \(\mathbb EZ=0\), Jensen's inequality gives
\[
D_M(x):=\mathbb E[h_M(\beta x)-h_M(x)]
=\mathbb E[g_M(u+Z)]-g_M(u)\ge0.
\]
Also \(D_M(0)=0\). If \(x\ge e^{-M}/\gamma_*\), neither \(\log x\) nor \(\log(\beta x)\) is truncated for any admissible \(\beta\), so \(D_M(x)=\mathbb EZ=0\). Because \(g_M\) is one-Lipschitz,
\[
0\le D_M(x)\le C:=\max\{-\log\gamma_*,\log2\}
\quad(0<x\le1/2).
\]
It follows for any probability \(\mu\) that
\[
0\le\int_{[0,1/2]}D_M\,d\mu
\le C\mu\bigl((0,e^{-M}/\gamma_*)\bigr)\longrightarrow0
\quad(M\longrightarrow\infty).
\tag{1}
\]
The last limit follows from continuity from above of finite measures: the shrinking sets exclude the endpoint \(0\).

On the right branch, for \(1/2<x\le1\), one has \(0<2x-1\le x\), and therefore
\[
B_M(x):=h_M(2x-1)-h_M(x)\le0.
\]
Fix \(\varepsilon\in(0,1/4)\) and let \(J_\varepsilon=[1/2+\varepsilon,1-\varepsilon]\). For \(M\) large enough that \(e^{-M}<2\varepsilon\), both arguments of \(h_M\) on this interval are untruncated, and
\[
B_M(x)=\log\frac{2x-1}{x}\le
\log\frac{1-2\varepsilon}{1-\varepsilon}
=-\eta_\varepsilon<0\qquad(x\in J_\varepsilon).
\]
Stationarity applied to \(h_M\), together with nonpositivity of \(B_M\) everywhere, yields
\[
\eta_\varepsilon\mu(J_\varepsilon)
\le \int_{[0,1/2]}D_M\,d\mu
\le C\mu((0,e^{-M}/\gamma_*)).
\]
Letting \(M\to\infty\) and then taking the increasing union of \(J_{\varepsilon}\) as \(\varepsilon\downarrow0\) gives
\[
\mu((1/2,1))=0.\tag{2}
\]

**Step 2: every point of the lower branch reaches the open upper branch with positive probability.** First fix \(x\in(0,1/2)\). Select \(b\in(3/2,7/4)\) such that \(xb^j\ne1/2\) for every positive integer \(j\); only countably many choices are excluded. Let \(n\ge1\) be the least integer with \(xb^n>1/2\). Then \(xb^j<1/2\) for \(0\le j<n\), whereas
\[
\frac12<xb^n<\frac b2<1.
\]
Thus the constant parameter word \((b,\ldots,b)\) of length \(n\) sends \(x\) into \(U=(1/2,1)\) while respecting every strict lower-branch inequality beforehand. These inequalities persist for all parameter words in an open neighborhood of this word. At the omitted boundary \(x=1/2\), the chosen left-branch convention gives \(T_b(1/2)=b/2\in U\) in one step for every \(b\in(3/2,7/4)\), so the required positive-probability neighborhood also exists there. As the uniform law has positive density on \((\gamma_*,2)\),
\[
P^n(x,U)>0\qquad\text{for some }n=n(x)\ge1.
\tag{3}
\]
Here \(P\) is the one-step Markov kernel and \(P^n\) its \(n\)-step iterate.

If \(\mu\) is stationary, (2) implies \(0=\mu(U)=\int P^n(y,U)\,d\mu(y)\) for **every** \(n\ge1\). Nonnegativity implies \(\mu(\{y:P^n(y,U)>0\})=0\) for each \(n\). Their countable union contains \((0,1/2]\) by (3); consequently
\[
\mu((0,1/2])=0.\tag{4}
\]
Combining (2) and (4) shows \(\mu((0,1))=0\). Hence \(\mu=t\delta_0+(1-t)\delta_1\). Conversely, both endpoint atoms are stationary because both endpoints are fixed under every branch choice, so every such mixture is stationary. This completes both directions of the classification. \(\square\)

## Verification

The key equality \(\mathbb E\log\beta=0\) follows symbolically from the normalized uniform integral. The inequalities in Step 1 are exact Jensen, Lipschitz, and monotonicity inequalities. Step 2 uses a positive-probability cylinder, not a generic-orbit assertion or finite sampling. The attached `verify.py` independently brackets the critical parameter with decimal arithmetic, checks that both endpoint atoms are fixed, and tests nonexceptional upper-branch reachability on an exact-rational grid. These finite checks supplement, but do not replace, the all-point proof.

## Relationship to prior work

The random map is equation (4.7) of Pérez Otero's 2023 dissertation, where Example 5.1 (Chapter 5, page 69) identifies the zero-logarithmic-drift threshold. Its published earlier formulation is Maldonado–Pérez Otero (2021). The dissertation treats the strictly negative and strictly positive regimes, but its displayed conclusions do not classify Borel stationary probabilities at equality. The theorem above fills that exact boundary case and includes possible singular measures, not only densities.

Kalle–Maggioni (2018) develop absolutely continuous invariant densities for expanding random systems; their hypotheses and conclusions do not furnish the boundary classification here. Homburg–Kalle–Ruziboev–Verbitskiy–Zeegers (2022) examine a different class with superstable-branch intermittency, and Yan–Majumdar–Ruffo–Sato–Beck–Klages (2023) treat a Bernoulli selection between doubling and halving. Their critical systems differ from the present uniformly distributed slope family. This comparison does **not** establish exhaustive publication priority.

## Limitations

The statement classifies only finite stationary **probabilities**, not sigma-finite stationary measures or scaling limits. It neither states nor proves almost-sure convergence at criticality, rates of approach, or behavior under other slope distributions. The full text of the 2021 journal article was not available in this investigation; the accessible complete 2023 dissertation, authored by one of the journal paper's coauthors, contains the original example and detailed threshold analysis. Additional specialized literature might contain an equivalent zero-drift rigidity theorem. No independent validation was performed.

## References

1. R. A. Pérez Otero, *Invariant densities and phase transition phenomenon in random maps in the interval*, doctoral dissertation, Instituto Potosino de Investigación Científica y Tecnológica, public repository dated 2023-04-25, handle:11627/5859, especially Sections 4.5 and 5.3.3.
2. C. Maldonado and R. A. Pérez Otero, “Phase transition in piecewise linear random maps in the interval,” *Chaos* **31** (2021), 093112, DOI:10.1063/5.0051242.
3. C. Kalle and M. Maggioni, “Invariant densities for random systems of the interval,” arXiv:1805.11430 (2018).
4. A. J. Homburg, C. Kalle, M. Ruziboev, E. Verbitskiy, and B. Zeegers, “Critical Intermittency in Random Interval Maps,” *Communications in Mathematical Physics* **394** (2022), 1–37, DOI:10.1007/s00220-022-04396-9.
5. J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck, and R. Klages, “Transition to anomalous dynamics in a simple random map,” arXiv:2308.09269 (2023).
