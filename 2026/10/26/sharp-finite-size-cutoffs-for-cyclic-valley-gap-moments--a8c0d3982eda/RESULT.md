# Sharp finite-size cutoffs for cyclic valley-gap moments

## Finding

Let \(i\ge1\) be an integer and let \(D_{i,K}\) count oriented gaps of length \(i+1\) between successive strict local minima in a uniformly random circular permutation of \(K\ge3\) entries. This is also the number of length-\(i+1\) gaps between consecutive roots of homogeneous ballistic deposition on a cyclic strip. Write
\[
a_i=\frac{i2^{i+1}}{(i+1)(i+2)(i+4)i!}.
\]
The exact *small-volume* mean law is
\[
\mathbb E D_{i,K}=\begin{cases}
0,&3\le K\le i+2,\\
(i+4)a_i,&K=i+3,\\
Ka_i,&K\ge i+4.
\end{cases}
\]
In particular the established linear-mean cutoff \(K=i+4\) is sharp for **every** \(i\), not merely for finitely checked indices.

Let \(b_i\) be the established eventual variance-per-site constant, defined by \(\operatorname{Var}(D_{i,K})=Kb_i\) for \(K\ge2i+7\) [1]. At the unique immediately preceding size \(K=2i+6\),
\[
\boxed{\operatorname{Var}(D_{i,2i+6})
=(2i+6)(b_i+\delta_i)},\qquad \delta_i>0.
\]
Here \(\delta_i\) admits the all-\(i\) explicit operator integral
\[
\delta_i=\operatorname{Tr}(\mathcal K_i\mathcal C\mathcal K_i\mathcal C)
=\|\mathcal C^{1/2}\mathcal K_i\mathcal C^{1/2}\|_{\mathrm{HS}}^2,
\]
where the integral operators on \(L^2([0,1])\) have kernels
\[
k_i(s,t)=\frac{(s+t)^i-|s-t|^i}{2i!},\qquad
c(s,t)=\min(s,t)-st.
\]
Thus the established linear-variance cutoff \(K=2i+7\) is likewise **sharp for every** \(i\ge1\). The operator \(\mathcal C\) is the Brownian-bridge covariance operator, and the correction is strictly positive despite possible indefiniteness of the excursion operator \(\mathcal K_i\).

## Assumptions and scope

Let \(K\ge3\). Place independent continuous random priorities \(U_0,\ldots,U_{K-1}\) at the sites \(\mathbb Z/K\mathbb Z\); their distribution may be taken uniform on \((0,1)\), because only relative order matters. A site is a *valley* when its priority is strictly less than its two nearest neighbours. List the valley sites in cyclic order. Define \(D_{i,K}\) as the number of successive ordered valley pairs whose clockwise distance is \(g=i+1\). A gap crossing the cyclic origin counts once. If there is only one valley, there are no distinct consecutive valley pairs. In deposition, priorities are monotone transforms of the independent site-first-arrival clocks, so valleys coincide with roots.

The published exact mean and eventual linear variance formulas from [1] are assumed only as specifically identified background formulas; the boundary equalities and their strictness are proved below. No asymptotic limit is used for a finite identity.

## Proof

**1. Local excursion kernel.** Write \(Y_x\) for the indicator that \(x\) and \(x+g\) are valleys with no intermediate valley. Then \(D_{i,K}=\sum_{x\in\mathbb Z_K}Y_x\). A sequence with no intermediate valley must rise and then fall between the two anchors; integrating its \(i\) interior priority values conditional on the two endpoint *survival probabilities* \(s,t\in(0,1)\) gives the symmetric kernel
\[
k_i(s,t)=\frac{(s+t)^i-|s-t|^i}{2i!}.
\]
This is the excursion-kernel formula proved in [1, Lemma 4.2]. In an interval with two distinct outward neighbour sites, both outward-neighbour inequalities contribute the factor \(st\). Thus when \(K\ge g+3\), each marked window consists of distinct sites, and
\[
\mathbb P(Y_x=1)=a_i=\int_0^1\!\int_0^1 st\,k_i(s,t)\,ds\,dt.
\]

**2. Mean exactly below the linear cutoff.** If \(K\le g+1\), two valleys cannot be separated clockwise by \(g\), because distinct valleys on a cycle have at least one intervening site in both directions; hence \(D_{i,K}=0\). At \(K=g+2=i+3\), the left exterior guard of the first valley and the right exterior guard of the second valley are the **same** random site. Conditional on the two endpoint probabilities \(s,t\), its contribution is therefore \(\min(s,t)\), not \(st\). Consequently
\[
\mathbb P(Y_x=1)=\int_0^1\!\int_0^1\min(s,t)k_i(s,t)\,ds\,dt
=\frac1{i!(i+3)}\int_0^1u\big[(1+u)^i-(1-u)^i\big]du
=\frac{i2^{i+1}}{(i+1)(i+2)(i+3)i!}
=\frac{i+4}{i+3}a_i.
\]
The second equality follows by symmetry and the substitution \(s=ut\) on the triangle \(0<s<t<1\); the third is integration of two elementary powers. Summing over \(K=i+3\) starting sites proves the claimed boundary mean \((i+4)a_i\). As \(a_i>0\), this differs strictly from \((i+3)a_i\). The eventual formula applies for \(K\ge i+4\) by the same distinct-window integral.

**3. Covariance diagrams at the variance boundary.** Put \(g=i+1\) and \(K=2g+4\). Now every single marked window is ordinary, with probability \(a_i\). On the infinite priority line, a joint event \(Y_0Y_h\) can differ from independence only for \(|h|\le g+2\). For \(1\le|h|<g\) and for \(|h|=g+1\), the two prescribed gaps are incompatible. For \(|h|=g\), three consecutive valleys are allowed; write their joint probability as \(u_i\). For \(|h|=g+2\), the two long-gap patterns have one intervening short arc of length two; write their joint probability as \(v_i\). It follows by covariance summation that the established eventual variance density is
\[
b_i=a_i-(2g+5)a_i^2+2u_i+2v_i,
\]
in agreement with [1].

At the cycle length \(K=2g+4\), the two offsets \(h=+(g+2)\) and \(h=-(g+2)\) refer to the **same antipodal** site pair, rather than two separate covariance terms. Every other covariance diagram is unchanged. If \(w_i\) denotes the cyclic joint probability for this antipodal pair, the exact change in variance per site is
\[
\frac{\operatorname{Var}(D_{i,2g+4})}{2g+4}-b_i
=w_i-2v_i+a_i^2.
\]
The independence reference \(a_i^2\) is necessary because the two ordinary covariance terms are replaced by one cyclic covariance term.

**4. Brownian-bridge factorization and strictness.** Define integral operators \(\mathcal M\) and \(\mathcal R\) with kernels \(m(s,t)=\min(s,t)\) and \(r(s,t)=st\), respectively. A length-two arc between neighboring valleys shares its single intervening outward-guard priority, giving kernel \(m\); two unshared outward guards give \(r\). Conditional independence of the remaining interior priorities of the two long arcs therefore yields
\[
w_i=\operatorname{Tr}(\mathcal K_i\mathcal M\mathcal K_i\mathcal M),\qquad
v_i=\operatorname{Tr}(\mathcal K_i\mathcal M\mathcal K_i\mathcal R),\qquad
a_i^2=\operatorname{Tr}(\mathcal K_i\mathcal R\mathcal K_i\mathcal R).
\]
These are absolutely convergent multiple integrals because all kernels are bounded on the compact square. Cyclic symmetry of trace and symmetry of the kernels imply that the two mixed traces agree. Substitution gives
\[
w_i-2v_i+a_i^2=\operatorname{Tr}(\mathcal K_i(\mathcal M-\mathcal R)\mathcal K_i(\mathcal M-\mathcal R))
=\operatorname{Tr}(\mathcal K_i\mathcal C\mathcal K_i\mathcal C)=\delta_i.
\]
The kernel \(c(s,t)=\min(s,t)-st\) is the covariance kernel of a standard Brownian bridge. Its orthonormal eigenfunctions are \(\sqrt2\sin(\pi n s)\), with strictly positive eigenvalues \(1/(\pi n)^2\) for all integers \(n\ge1\). Thus \(\mathcal C\) is positive and injective, and \(\mathcal C^{1/2}\) has dense range. The nonzero continuous real symmetric operator \(\mathcal K_i\) is Hilbert–Schmidt. It follows that
\[
\delta_i=\|\mathcal C^{1/2}\mathcal K_i\mathcal C^{1/2}\|_{\mathrm{HS}}^2>0,
\]
for if the norm were zero, \(\mathcal K_i\) would vanish on the dense range of \(\mathcal C^{1/2}\) and hence everywhere, contrary to \(k_i(s,t)>0\) for \(s,t>0\). This proves strictness for all \(i\ge1\), not merely by checking small values. Combining with Step 3 completes the variance identity and sharp-cutoff theorem.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic and enumerates all labeled cyclic priority rankings after fixing the global minimum at site zero by rotation. It independently confirms the mean boundary formula for \(1\le i\le6\) and the variance boundary formula at \(i=1,2\). For these two variance cases, the exact boundary corrections are
\[
\delta_1=\frac{29}{28350},\qquad \delta_2=\frac1{2025}.
\]
The corresponding established eventual variance densities are \(b_1=1772/14175\) and \(b_2=32/405\). The exhaustive checks cover all \((K-1)!\) cyclic rankings at each tested length; they do not prove the all-\(i\) statement, which follows from the operator argument above.

Run `python verify.py` from the directory containing the extracted files; Python 3 standard library suffices. The program raises an assertion if any tested identity fails.

## Relationship to prior work

Matijasevick [1, Theorem A; Proposition 3.1; Lemma 4.2; Remark 3.2] proves exact eventual linearity for \(K\ge i+4\) (mean) and \(K\ge2i+7\) (variance), derives the excursion kernel and records finite-index computational checks of optimality, but does not give an analytic proof of sharpness for all \(i\). Mansour, Rastegar and Roitershtein [2] studied root gaps and selected finite-index moments. The present result derives the complete below-cutoff mean law and proves that the first below-cutoff variance always has the strictly positive Brownian-bridge correction.

Ehrenborg [3] develops operator traces for weighted cyclic consecutive-pattern enumerations; this is methodologically related but the inspected theorem concerns cyclic avoidance counts rather than the two simultaneous valley-gap moments at their finite-size boundary. A possible less-direct specialization of general operator enumeration to these moments remains a literature-overlap risk.

## Limitations

The statement concerns homogeneous continuous-priority deposition/root valleys on a one-dimensional cyclic strip. It does not address nonuniform site clocks, other root-gap definitions, complete finite-\(K\) variance formulas below \(2i+6\), nor arbitrary joint gap covariances. The formula for \(b_i\) is inherited from the cited established theorem. Independent mathematical validation has not been performed.

## References

[1] M. Matijasevick, *Gaps between roots in ballistic deposition on a strip: linear variance, Gaussian limits and a Poisson regime*, arXiv:2610.21094v1 (first public 2026-10-15), https://arxiv.org/abs/2610.21094 .

[2] T. Mansour, R. Rastegar and A. Roitershtein, *On ballistic deposition process on a strip*, arXiv:1903.12548v2 (first public 2019-03-29), https://arxiv.org/abs/1903.12548 .

[3] R. Ehrenborg, *Cyclically consecutive permutation avoidance*, arXiv:1312.2051v1 (2013), https://arxiv.org/abs/1312.2051 .
