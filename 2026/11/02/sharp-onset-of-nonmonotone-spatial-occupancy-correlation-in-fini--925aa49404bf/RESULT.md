# Sharp onset of nonmonotone spatial occupancy correlation in finite mainland–island metapopulations

## Finding

In the homogeneous finite mainland–island patch-occupancy model defined below, fix the positive ratio \(u=b/e\) of outside immigration to extinction and let \(v=c/e\geq0\) be the internal per-neighbor colonization ratio. For distinct patches \(i,j\), write
\[
\rho_n(u,v)=\operatorname{Corr}_{\pi_{n,u,v}}(X_i,X_j).
\]
The following sharp patch-number distinction holds.

1. For two patches, \(\rho_2(u,v)=v/[(1+u)(1+u+v)]\), a strictly increasing function of \(v\geq0\) with limiting value \(1/(1+u)\).
2. For three patches, \(\rho_3(u,v)\) has **exactly one** critical point on \(v>0\); this point is a strict global maximum. In particular, \(\rho_3(u,0)=0\), \(\rho_3(u,v)>0\) when \(v>0\), and \(\rho_3(u,v)\to0\) as \(v\to\infty\). The stationary one-patch occupancy probability nevertheless increases strictly throughout \(v\geq0\).
3. For every finite \(n\geq3\), \(\rho_n(u,v)>0\) for finite \(v>0\), while \(\rho_n(u,0)=0\) and \(\rho_n(u,v)\to0\) as \(v\to\infty\). Hence at least one interior positive maximum occurs for each \(n\geq3\). No uniqueness assertion is made for \(n\geq4\).

Consequently **three is the minimum number of patches** allowing an interior peak in the stationary pairwise Pearson occupancy correlation when internal colonization varies at fixed immigration and extinction. Explicitly, set \(A=(1+u)^2\). Then
\[
\boxed{\rho_3(u,v)=\frac{v[A+(u+2)v]}{[A+uv][A+(3u+2)v+2v^2]}.}
\]
The unique maximizing rate \(v_*(u)\) is the unique positive zero of the quartic
\[
\begin{aligned}
H_u(v)={}&(1+u)^6+2(1+u)^4(u+2)v\\
&-(1+u)^2(u^2-4u-2)v^2\\
&-4u(1+u)^2v^3-2u(u+2)v^4.
\end{aligned}
\]
For the exact example \(u=1\), the correlations at \(v=1,2,3\) are respectively \(7/55,5/33,39/259\); therefore the intermediate connectivity yields the largest of these three pairwise correlations even though the corresponding mean occupancies rise strictly.

## Assumptions and scope

Let \(n\geq2\) and let \(X(t)\in\{0,1\}^n\) be a continuous-time Markov chain. A patch with state zero becomes occupied at rate \(b+c k\), where \(k\) is the number of **other** occupied patches; an occupied patch becomes empty at rate \(e\). The parameters satisfy \(b,e>0\), \(c\geq0\), and rates act independently in the standard single-event continuous-time construction. The model has a unique stationary distribution \(\pi_{n,u,v}\), because external immigration and extinction make the finite state space irreducible. Patches are exchangeable; all pairwise Pearson correlations are well-defined since each one-patch occupancy probability lies strictly between zero and one. The result concerns **simultaneous stationary spatial correlations**, not temporal correlations, dispersal range, absolute abundance, extinction before recolonization, or an arbitrary heterogeneous habitat network.

The internal colonization convention is **per occupied neighbor**. In the standard form \(ck(1-k/n)\) of the total Levins/Alonso–McKane count-chain colonization rate, the source's colonization coefficient equals \(nc\) under this convention.

## Proof

**1. Count-chain stationary law.** Put \(Y=\sum_{i=1}^n X_i\) and rescale time by \(e\). The birth and death rates are respectively
\[
\lambda_k=(n-k)(u+vk),\qquad\mu_k=k.
\]
Detailed balance implies that the stationary probability of \(Y=k\) is \(w_k/Z_n\), where
\[
w_k=\binom nk\prod_{j=0}^{k-1}(u+jv),\qquad Z_n=\sum_{k=0}^nw_k,
\]
with the empty product equal to one. Uniform conditional assignment of the \(k\) occupied sites follows from exchangeability. Thus
\[
p_n=\frac{\mathbb E[Y]}n,\qquad
q_n=\frac{\mathbb E[Y(Y-1)]}{n(n-1)},\qquad
\rho_n=\frac{q_n-p_n^2}{p_n(1-p_n)}.
\]

**2. Positivity at every finite size.** For \(v>0\), take a Gamma random variable \(T\) of shape \(u/v\) and unit scale, so \(\mathbb E[T^k]=(u/v)_k\). Tilt its law by the positive weight \((1+vT)^n/Z_n\). Given \(T\) under this tilted law, generate the \(n\) patch states independently with success probability \(R(T)=vT/(1+vT)\). The resulting probability of each configuration containing \(k\) occupied patches is
\[
\frac{\mathbb E[(vT)^k]}{Z_n}=
\frac{\prod_{j=0}^{k-1}(u+jv)}{Z_n},
\]
precisely its stationary probability from step 1. Hence
\[
\operatorname{Cov}(X_i,X_j)=\operatorname{Var}_{\mathrm{tilted}}(R(T))>0
\]
for distinct sites: the Gamma law is nondegenerate and \(R\) is strictly increasing. At \(v=0\), every patch is an independent immigration–extinction chain, giving zero correlation.

**3. Two patches.** The unnormalized count weights are \(1,2u,u(u+v)\). Their first two factorial moments inserted into step 1 yield
\[
\rho_2(u,v)=\frac{v}{(1+u)(1+u+v)},\qquad
\frac{\partial\rho_2}{\partial v}=\frac1{(1+u+v)^2}>0.
\]
Its limit as \(v\to\infty\) is \(1/(1+u)\).

**4. Three patches and strict unimodality.** The count weights are
\[
1,\quad3u,\quad3u(u+v),\quad u(u+v)(u+2v),
\]
whose sum is \(Z_3=(1+u)^3+3u(1+u)v+2uv^2\). The first two factorial moments give
\[
 p_3=\frac{u[A+(3u+2)v+2v^2]}{Z_3},\qquad
\operatorname{Cov}(X_1,X_2)=\frac{uv[A+(u+2)v]}{Z_3^2}.
\]
Dividing by \(p_3(1-p_3)\) gives the displayed \(\rho_3\). Direct differentiation gives
\[
\frac{\partial\rho_3}{\partial v}
=\frac{H_u(v)}{[A+uv]^2[A+(3u+2)v+2v^2]^2}.
\]
For any fixed \(u>0\), the quartic coefficients of \(H_u\), in descending degree order, have the signs
\[
(-,-,\operatorname{sgn}[-(u^2-4u-2)],+,+).
\]
Deleting a possible zero coefficient, there is **exactly one sign change** irrespective of the quadratic coefficient. Descartes' rule of signs gives at most one positive zero, counted with multiplicity. Since \(H_u(0)=(1+u)^6>0\) and its leading coefficient is \(-2u(u+2)<0\), the intermediate value theorem gives a positive zero. It is unique and simple, and the derivative changes from positive to negative there. The function therefore has exactly one critical point and one strict global maximum. Also \(\rho_3(u,0)=0\) and \(\rho_3(u,v)=O(v^{-1})\) for large \(v\).

Finally,
\[
\frac{\partial p_3}{\partial v}
=\frac{2u[(1+u)^3+2(1+u)^2v+uv^2]}{Z_3^2}>0.
\]
Thus the nonmonotonic spatial correlation is not a reversal in marginal occupancy.

**5. More than three patches.** From the count weights,
\[
\frac{w_{n-1}}{w_n}=\frac n{u+(n-1)v}=O(v^{-1}),
\]
and for \(n\geq3\),
\[
\frac{w_{n-2}}{w_n}
=\frac{n(n-1)}{2[u+(n-1)v][u+(n-2)v]}=O(v^{-2}).
\]
The remaining lower weights are \(O(v^{-2})\) relative to \(w_n\) as well. Let \(r_n=\Pr(X_i=0)\) and \(s_n=\Pr(X_i=X_j=0)\) for distinct sites. Exchangeability gives \(r_n\sim1/[(n-1)v]\) and \(s_n=O(v^{-2})\). Therefore
\[
\rho_n=\frac{s_n-r_n^2}{r_n(1-r_n)}=O(v^{-1})\longrightarrow0.
\]
Step 2 gives strict positivity for every finite \(v>0\), and continuity together with the zero limits at both ends forces at least one interior global maximum. This completes the sharp patch-count assertion.

## Verification

The standalone `verify.py` uses exact SymPy identities to reconstruct the stationary laws, Pearson correlations, positivity of the three-patch occupancy derivative, and the quartic derivative identity. It independently constructs the birth–death chain and checks detailed balance and exact Pearson correlations for patch counts from two to six across 240 rational parameter pairs, totaling 1,200 rational assertions. It also verifies the three displayed exact fractions and all quartic coefficients. Run with `python verify.py` in an environment with SymPy installed. These finite checks supplement, but do not replace, the full proof above.

## Relationship to prior work

Alonso and McKane (2002) derived the exact stationary count distribution, stationary mean, and higher moments for this mainland–island model, using the total internal colonization rate convention stated above. Those are prior results, and the stationary formula here is recalled, **not claimed as new**. The new conclusion assessed here is the sharp global shape of the stationary **pairwise Pearson correlation as a function of internal colonization**, its unique peak for three patches for every positive immigration-to-extinction ratio, and the minimal-patch distinction between two and at least three patches. These shape statements are not stated in the inspected source sections.

Foxall (2014) develops general monotonicity and convergence for spontaneous-infection contact processes; monotonicity of increasing events does not imply monotonicity of a normalized pair correlation. Cator and Van Mieghem (2014) establish nonnegative infection correlations in the Markovian SIS setting; the positive-association component here is consistent with, not a challenge to, that prior result. The 2012 and 2015 finite-network SIS studies by Van Mieghem and collaborators give additional related complete-graph and covariance frameworks, but their complete technical contents could not be compared here. No priority claim is made for the detailed-balance formula or generic positive association.

## Limitations

This is an exact theorem for homogeneous, exchangeable, finitely many patches with constant immigration, colonization and extinction rates. The unique-maximum result is proven only for **three** patches; for all higher patch counts, only existence is proved. It does not establish statistical identifiability of colonization from noisy observations, numerical robustness, or ecological forecasting for spatially heterogeneous landscapes. General stationary formulas in prior literature are strong background coverage; independent priority verification, especially of related finite-network SIS covariance papers whose full text was unavailable, remains necessary. No independent scientific audit has been performed.

## References

1. Alonso, D. and McKane, A. J. (2002). “Extinction Dynamics in Mainland–Island Metapopulations: An N-patch Stochastic Model.” *Bulletin of Mathematical Biology* **64**, 913–958. DOI: https://doi.org/10.1006/bulm.2002.0307. Accessible complete text: https://math.hawaii.edu/~gautier/Extinction%20Dynamics%20in%20Mainland-Island%20Metapopulations.pdf.
2. Foxall, E. (2014). “Convergence and Monotonicity for a Model of Spontaneous Infection and Transmission.” *Advances in Applied Probability* **46**, 560–584. DOI: https://doi.org/10.1239/aap/1401369707.
3. Cator, E. and Van Mieghem, P. (2014). “Nodal infection in Markovian susceptible-infected-susceptible and susceptible-infected-removed epidemics on networks are non-negatively correlated.” *Physical Review E* **89**, 052802. DOI: https://doi.org/10.1103/PhysRevE.89.052802.
4. Van Mieghem, P. and Cator, E. (2012). “Epidemics in networks with nodal self-infection and the epidemic threshold.” *Physical Review E* **86**, 016116. DOI: https://doi.org/10.1103/PhysRevE.86.016116.
5. Van Mieghem, P. and van de Bovenkamp, R. (2015). “Accuracy criterion for the mean-field approximation in susceptible-infected-susceptible epidemics on networks.” *Physical Review E* **91**, 032812. DOI: https://doi.org/10.1103/PhysRevE.91.032812.
