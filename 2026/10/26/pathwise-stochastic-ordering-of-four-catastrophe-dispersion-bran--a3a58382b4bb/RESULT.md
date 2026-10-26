# Pathwise stochastic ordering of four catastrophe–dispersion branching schemes

## Finding

For the full, capacity-limited, independent-occupation, and uniform-composition dispersal mechanisms of de Lima and Machado [1], **offspring counts are ordered in first-order stochastic dominance**, not merely in expectation. This yields a **simultaneous pathwise ordering of colony counts in every generation**, for any common deterministic or random environment sequence. In particular, extinction probabilities are ordered at each finite generation and at infinity. For capacity two, the theorem also gives exact extinction probabilities for **every** homogeneous survivor-count distribution, and a nonempty range in which independent dispersal survives whereas uniform-composition dispersal dies out.

Write \(D_1,D_2,D_3,D_4\) for the mechanisms defined below. If \(Y\) is any nonnegative integer-valued survivor count and \(d\ge1\) is the capacity, then
\[
D_1(Y)\succeq_{\mathrm{st}}D_2(Y)\succeq_{\mathrm{st}}D_3(Y)\succeq_{\mathrm{st}}D_4(Y),
\]
where \(X\succeq_{\mathrm{st}}Y\) means \(\Pr(X\ge k)\ge\Pr(Y\ge k)\) for every integer \(k\).

For every fixed \(r\ge2,d\ge2\), the last inequality is strict at threshold two, with the exact gap
\[
\Pr(D_3(r)\ge2)-\Pr(D_4(r)\ge2)
=\frac{d}{\binom{r+d-1}{d-1}}-d^{1-r}>0.
\]
Consequently the offspring laws \(D_3(Y),D_4(Y)\) coincide **if and only if** \(d=1\) or \(\Pr(Y\ge2)=0\).

## Assumptions and scope

Fix \(d\in\mathbb N\) and \(r\in\mathbb N_0\). Mechanism \(D_1(r)=r\) creates a distinct colony for each survivor; \(D_2(r)=\min(d,r)\) imposes only the capacity limit. Under \(D_3(r)\), each of the \(r\) survivors chooses independently and uniformly from \(d\) labeled sites, and the offspring count equals the number of occupied sites. Under \(D_4(r)\), choose uniformly among all \(\binom{r+d-1}{d-1}\) weak compositions of \(r\) into \(d\) nonnegative occupancies, and count positive coordinates. At \(r=0\), every mechanism has zero offspring.

For the generation-dependent conclusion, let \((\mathcal E_n)_{n\ge0}\) be any, possibly dependent, random environment sequence. Conditional on its complete realization, each generation \(n\) has a specified survivor-count law \(\nu_n\) on \(\mathbb N_0\), a capacity \(d_n\ge1\), and independent identically distributed offspring counts across colony indices. All four mechanisms use the **same** \(\nu_n,d_n\) at each generation, differing only in dispersal. Fix any common finite initial colony count \(z_0\in\mathbb N_0\). No moment, stationarity, ergodicity, or independent-environment assumption is needed for the ordering.

## Proof

**1. Uniform site probabilities maximize the number occupied in stochastic order.** For a deterministic probability vector \(p=(p_1,\ldots,p_d)\), let \(K_p(r)\) be the number of occupied sites in \(r\) independent allocations. Consider two coordinates \(p_i,p_j\), with fixed total \(t=p_i+p_j\), and replace them by their average \(t/2,t/2\). Conditional on the number \(M\) of survivors routed to the pair and on all assignments outside the pair, both models have the same conditioning law. If \(M=0\), neither coordinate is occupied. If \(M\ge1\), at least one is occupied, and the pair contributes a second occupied site with probability
\[
 h_M(q)=1-q^M-(1-q)^M,\qquad q=p_i/t.
\]
For \(M=1\), this probability is zero. For \(M\ge2\), convexity and symmetry of \(q^M+(1-q)^M\) imply \(h_M(q)\le h_M(1/2)\). Hence averaging two coordinates increases the **whole** occupied-count variable in first-order stochastic order, conditionally and thus unconditionally. The case \(t=0\) is trivial. Repeatedly averaging a largest and a smallest coordinate converges to \((1/d,\ldots,1/d)\): writing \(V=\sum_i(p_i-1/d)^2\), an averaging of the maximum and minimum entries decreases \(V\) by \((\max_i p_i-\min_i p_i)^2/2\). Since \(V\le d(\max_i p_i-\min_i p_i)^2\), each such operation shrinks \(V\) by at least the factor \(1-1/(2d)\). Hence the iterates converge to the uniform vector. Since each probability \(\Pr(K_p(r)\ge k)\) is a polynomial in \(p\), continuity proves
\[
K_p(r)\preceq_{\mathrm{st}} K_{(1/d,\ldots,1/d)}(r)=D_3(r)
\]
for **every** probability vector \(p\), including vectors with zero entries. Equivalently, each tail of the occupied-count statistic is Schur-concave in site probabilities.

**2. Uniform compositions are Dirichlet mixtures.** Let \(P\sim\operatorname{Dirichlet}(1,\ldots,1)\), and, conditionally on \(P\), independently assign \(r\) survivors to the sites with probabilities \(P_i\). For every weak composition \((n_1,\ldots,n_d)\) of \(r\), Dirichlet integration gives
\[
\Pr(N_1=n_1,\ldots,N_d=n_d)
=\frac{r!}{\prod_i n_i!}\frac{\Gamma(d)}{\Gamma(d+r)}\prod_i\Gamma(n_i+1)
=\frac{1}{\binom{r+d-1}{d-1}}.
\]
It is therefore **exactly** mechanism \(D_4(r)\). Applying step 1 conditionally on \(P\) and then averaging proves \(D_4(r)\preceq_{\mathrm{st}}D_3(r)\). The deterministic bounds \(D_3(r)\le\min(d,r)=D_2(r)\le r=D_1(r)\) give the other comparisons. Conditioning on the arbitrary survivor variable \(Y\) preserves all inequalities.

**3. Sharp strictness.** For \(r\ge2,d\ge2\), \(D_3(r)=1\) exactly when all survivors independently choose one site, an event of probability \(d^{1-r}\). For uniform weak compositions, \(D_4(r)=1\) for exactly \(d\) of the \(\binom{r+d-1}{d-1}\) compositions. Thus the displayed exact gap follows. It is strictly positive because, under the nondegenerate Dirichlet distribution, strict Jensen convexity gives \(\mathbb E\sum_iP_i^r>\sum_i(\mathbb EP_i)^r=d^{1-r}\). For \(r=0,1\) or \(d=1\), mechanisms \(D_3,D_4\) coincide deterministically. Integrating the nonnegative conditional gaps over \(Y\) proves the claimed equality characterization.

**4. Simultaneous branching-process coupling.** For each environment realization, each generation \(n\), and each potential colony label \(j\in\mathbb N\), take independent uniforms \(U_{n,j}\) and use the generalized inverse distribution functions of the four offspring laws to form \(\xi^{(a)}_{n,j}\), for \(a\in\{1,2,3,4\}\). First-order stochastic dominance gives \(\xi^{(1)}_{n,j}\ge\cdots\ge\xi^{(4)}_{n,j}\) almost surely for every \(n,j\). For each \(a\), set
\[
Z_0^{(a)}=z_0,\qquad Z_{n+1}^{(a)}=\sum_{j=1}^{Z_n^{(a)}}\xi_{n,j}^{(a)}.
\]
Induction and nonnegativity show \(Z_n^{(1)}\ge\cdots\ge Z_n^{(4)}\) simultaneously for every \(n\), almost surely, conditional on the environment. The construction preserves the prescribed within-process conditional independence. Since zero is absorbing, \(\Pr(Z_n^{(1)}=0\mid\mathcal E)\le\cdots\le\Pr(Z_n^{(4)}=0\mid\mathcal E)\) for all \(n\); increasing unions give the same ordering for ultimate extinction. Averaging yields annealed inequalities. An **arbitrary time course** of the environment is allowed.

**5. Exact capacity-two extinction law and a strict phase separation.** In a homogeneous environment with \(d=2\), put \(s=\Pr(Y=0)\) and
\[
A_3=\sum_{r\ge2}\Pr(Y=r)(1-2^{1-r}),\qquad
A_4=\sum_{r\ge2}\Pr(Y=r)\frac{r-1}{r+1}.
\]
These are precisely the probabilities of two offspring. Indeed, with \(r\ge1\), independent allocation occupies both sites with probability \(1-2^{1-r}\), whereas among \(r+1\) uniform weak compositions exactly \(r-1\) have both sites occupied. The two offspring pgfs are
\[
F_a(z)=s+(1-s-A_a)z+A_az^2,\qquad a\in\{3,4\}.
\]
The fixed-point equation factors as \((z-1)(A_az-s)=0\). Therefore, if \(s>0,A_a>0\), the extinction probability is \(q_a=\min\{1,s/A_a\}\); if \(s>0,A_a=0\), it is \(1\); and if \(s=0\), it is \(0\). The last case includes deterministic one-offspring reproduction, for which extinction never occurs. A nontrivial process with \(s>0\) survives with positive probability exactly when \(A_a>s\).

For \(\Pr(Y=2)=t\) and \(\Pr(Y=0)=1-t\), one has \(A_3=t/2,A_4=t/3\). Thus independent allocation survives when \(t>2/3\), whereas uniform-composition allocation survives only when \(t>3/4\). For \(2/3<t\le3/4\), the first survives and the second becomes extinct almost surely. For \(3/4<t<1\), the exact extinction probabilities are \(q_3=2(1-t)/t\) and \(q_4=3(1-t)/t\); their gap is \((1-t)/t\). At \(t=4/5\), they are \(1/2\) and \(3/4\), respectively.

## Verification

The standalone standard-library program `dispersion_order_verification.py` runs `python3 dispersion_order_verification.py` and reports `PASS 13989 exact rational assertions`. It independently enumerates occupancy distributions, compares upper tails for uniform compositions and independent allocations, checks nonuniform probability vectors (including zeros), verifies the exact two-occupancy gap, and tests the capacity-two generating-function example. The program is supplementary evidence for finite cases only. The statements for every capacity, survivor law, and environment sequence rest on the analytic arguments in the Proof section; a finite test cannot establish them.

## Relationship to prior work

De Lima and Machado [1], Sections 2.2–3, define the four dispersal schemes, derive offspring formulas, and establish **ordering of offspring means**. Their results do not themselves state full stochastic ordering or a common-environment pathwise ordering of the four population processes. Junior, Machado and Roldán-Correa [2], Remark 2.2, already prove independent-dispersion survival superiority over uniform composition **for capacities two and three**, using cumulative offspring distributions in a geometric-catastrophe tree setting; those two capacities and that restricted setting are **not newly claimed**. Their result does not state arbitrary-capacity first-order dominance for all survivor-count laws and all common environment histories. The 2024 uniform-dispersion paper [3] also studies extinction and survival on spatial trees with different restrictions. The present contribution is the all-capacity, all-survivor-law stochastic ordering and the ensuing quenched population-path coupling; the capacity-two formula supplies an explicit general-law illustration, not a claim that low-capacity survival comparisons were unknown.

The majorization component uses classical convexity and Dirichlet–multinomial identities; the general principle that stochastically ordered offspring laws permit coupled branching processes is also classical. The contribution is the precise uniform-weak-composition versus uniform-iid occupancy comparison in this four-mechanism framework, with no restrictions on capacity, survivor law, or environmental dependence. A previously published occupancy-majorization theorem might yield this conclusion directly when combined with general branching coupling; no uniqueness assertion is made.

## Limitations

The population processes here are **colony-count branching representations** without spatial site conflicts between descendants of different parents. The theorem does not order interacting spatial models in which different parents compete for the same physical territory. The same survivor kernel and capacity must be compared across the four mechanisms at each generation. The stochastic order makes no claims about unbounded continuous-time population sizes or spatial occupation histories between catastrophes. Exact capacity-two extinction probabilities assume a homogeneous (generation-independent) reproduction law. Neither finite numerical tests nor the cited literature comparison constitute independent certification or an exhaustive prior-art search.

## References

1. Lucas R. de Lima and Fábio P. Machado, *Catastrophe–dispersion models in random and varying environments across generations*, arXiv:2605.04048v1 (first public May 5, 2026), Sections 2–4. https://arxiv.org/html/2605.04048v1
2. Valdivino Vargas Junior, Fábio Prates Machado and Alejandro Roldán-Correa, *Evaluating dispersion strategies in growth models subject to geometric catastrophes*, arXiv:2012.12027 (first public December 22, 2020), especially Section 2 and Remark 2.2. https://arxiv.org/abs/2012.12027
3. Valdivino V. Junior, Fábio P. Machado and Alejandro Roldán-Correa, *Uniform dispersion in growth models on homogeneous trees*, arXiv:2407.14654 (first public July 19, 2024). https://arxiv.org/abs/2407.14654
