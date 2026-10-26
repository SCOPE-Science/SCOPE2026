# Sharp three-regime allocation of endpoint dephasing in a detuned quantum trimer

## Finding
For a coherent three-site chain with a detuned center, irreversible collection at the right endpoint, and a **fixed total rate of pure dephasing restricted to the two endpoints**, the mean time to collection has an exact formula. Its optimum undergoes a sharp allocation transition as detuning varies, including a regime with a uniquely optimal nontrivial split.

Let \(G>0\), \(\kappa>0\), and \(\Delta\in\mathbb R\). Allocate \(u\in[0,G]\) of the dephasing budget to site 1 and \(G-u\) to site 3. Write \(x=G+\kappa\) and \(Q(u)=4+u(x-u)\). The mean absorption time from site 1 is
\[
\boxed{T(u)=\frac3\kappa+\frac{2x-u}{4}+\frac{\Delta^2(x+u)}{Q(u)}.}
\]
In particular, \(T\) is strictly convex for \(\Delta\ne0\), and for \(\Delta=0\) it is strictly decreasing. Put
\[
A_0=-\frac14+\frac{\Delta^2(4-x^2)}{16},\qquad
A_G=-\frac14+\frac{\Delta^2(2G^2+4-\kappa^2)}{(4+\kappa G)^2}.
\]
The unique global minimizer is \(u_*=0\) if \(A_0\ge0\), \(u_*=G\) if \(A_G\le0\), and otherwise the unique root in \((0,G)\) of
\[
4\Delta^2\bigl(u^2+2xu+4-x^2\bigr)
=\bigl(4+xu-u^2\bigr)^2.
\]
These cases are mutually exclusive except for the trivially consistent boundary formula when \(\Delta=0\), for which \(u_*=G\).

When \(G+\kappa<2\), define
\[
\Delta_{\rm S}=\frac{4+\kappa G}{2\sqrt{2G^2+4-\kappa^2}},
\qquad
\Delta_{\rm T}=\frac{2}{\sqrt{4-(G+\kappa)^2}}.
\]
Then \(0<\Delta_{\rm S}<\Delta_{\rm T}\) and the allocation classification simplifies to
\[
\boxed{
\begin{array}{ll}
u_*=G,&|\Delta|\le\Delta_{\rm S},\\
0<u_*<G,&\Delta_{\rm S}<|\Delta|<\Delta_{\rm T},\\
u_*=0,&|\Delta|\ge\Delta_{\rm T}.
\end{array}}
\]
Here the interior optimizer moves continuously between the endpoints. When \(\kappa^2\ge2G^2+4\), \(u_*=G\) for every detuning. In the other parameter regimes the preceding sign tests give the exact classification.

## Assumptions and scope
Use units with nearest-neighbor hopping amplitude and \(\hbar\) equal to one. The Hilbert space has basis \(|1\rangle,|2\rangle,|3\rangle\) and real Hermitian Hamiltonian
\[
H=\begin{pmatrix}0&1&0\\1&\Delta&1\\0&1&0\end{pmatrix}.
\]
Write \(P_j=|j\rangle\langle j|\). The unnormalized survivor density matrix evolves by the completely positive trace-decreasing generator
\[
\mathcal L_u(\rho)=-i[H,\rho]-\frac{\kappa}{2}\{P_3,\rho\}
+u\left(P_1\rho P_1-\frac12\{P_1,\rho\}\right)
+(G-u)\left(P_3\rho P_3-\frac12\{P_3,\rho\}\right).
\]
Initial state: \(\rho(0)=P_1\). Define the survival probability \(S_u(t)=\operatorname{Tr}\rho(t)\) and mean absorption time \(T(u)=\int_0^\infty S_u(t)\,dt\). All assertions concern \(G,\kappa>0\), \(u\in[0,G]\), and arbitrary finite real \(\Delta\). A zero allocation at one endpoint is permitted, but the total budget is strictly positive. At no point is dephasing applied to site 2.

## Proof
**Absorption and integrability.** The dynamics preserves positivity and \(S_u'(t)=-\kappa\rho_{33}(t)\le0\). A nonzero initial positive state cannot remain in the nullspace of the collection observable on any time interval: if \(\rho_{33}(t)=0\) there, positivity forces its entire third row and column to vanish; the \((2,3)\) equation then forces \(\rho_{22}(t)=0\), and the \((1,2)\) equation forces \(\rho_{11}(t)=0\). This contradicts positive initial trace. Thus \(S_u(t)<S_u(0)\) for any \(t>0\). For any fixed \(t_0>0\), the compact set of unit-trace positive matrices and continuity imply \(q=\sup_{\rho\ge0,\operatorname{Tr}\rho=1}\operatorname{Tr}(e^{t_0\mathcal L_u}\rho)<1\). Semigroup iteration gives \(S_u(nt_0)\le q^n\) and hence \(S_u\) integrable. Therefore \(X=\int_0^\infty\rho(t)\,dt\) exists and satisfies \(\mathcal L_u(X)=-P_1\).

**Solve the nine integrated equations.** Write \(X_{12}=a+ib\), \(X_{23}=c+id\), \(X_{13}=e+if\), and \(X_{jj}=p_j\) with real coefficients. The diagonal equations give \(b=d=1/2\), \(p_3=1/\kappa\). The real \((1,3)\) equation gives \(e=0\). The real \((1,2)\), real \((2,3)\), and imaginary \((1,3)\) equations yield
\[
f=-\frac{2\Delta}{Q(u)},\qquad
a=-\frac{\Delta(x-u)}{Q(u)},\qquad
c=\frac{\Delta u}{Q(u)}.
\]
The remaining two imaginary coherence equations read
\[
p_1-p_2=\frac u4+\frac{\Delta^2(x-u)}{Q(u)},\qquad
p_2-p_3=\frac{x-u}{4}+\frac{\Delta^2u}{Q(u)}.
\]
Taking the trace \(T(u)=p_1+p_2+p_3\) proves the boxed rational expression, valid at both allocation endpoints without limiting arguments.

**Convex optimization.** Direct differentiation gives
\[
T'(u)=-\frac14+\Delta^2\frac{u^2+2xu+4-x^2}{Q(u)^2},
\qquad
T''(u)=\frac{2\Delta^2\bigl((x-u)^3+2u^3+12u\bigr)}{Q(u)^3}.
\]
Since \(x-u=\kappa+G-u\ge\kappa>0\), \(Q(u)\ge4\), and \(u\ge0\), the second derivative is strictly positive whenever \(\Delta\ne0\). The endpoint derivatives are exactly \(A_0\) and \(A_G\); monotonicity of \(T'\) proves the unique global minimizer and the exact interior equation. For \(\Delta=0\), \(T'=-1/4\), yielding \(u_*=G\).

**Sharp detuning transition.** If \(G+\kappa<2\), then \(4-x^2>0\), \(2G^2+4-\kappa^2>0\), and both endpoint slopes grow affinely in \(\Delta^2\). The zero of \(A_G\) occurs at \(\Delta_{\rm S}\) and the zero of \(A_0\) at \(\Delta_{\rm T}\). Strict positivity of \(T''\) forces \(A_G>A_0\) for nonzero \(\Delta\), hence \(\Delta_{\rm S}<\Delta_{\rm T}\); continuity of the unique root follows from strict monotonicity of \(T'\). If \(\kappa^2\ge2G^2+4\), then \(A_G\le-1/4\) for every \(\Delta\), proving the claimed all-source regime.

## Verification
The standalone `check_endpoint_noise.py` (Python 3.10+, NumPy, SciPy and SymPy) checks the nine integrated-density equations symbolically and independently constructs a complex nine-dimensional Lindblad superoperator to compute \(\operatorname{Tr}[-\mathcal L_u]^{-1}P_1\). With fixed random seed 20261024, it passes 11 symbolic identities, 900 independent superoperator solutions, 1,200 strict-convexity/derivative comparisons, and 650 global-optimization comparisons. It also checks all three placement regimes for \(G=1\), \(\kappa=0.5\): detuning values \(0.5\), \(1.2\), and \(2\) respectively give \(u_*=1\), \(u_*\approx0.504836059077\), and \(u_*=0\). Finite tests supplement, and do not replace, the preceding analytical proof.

## Relationship to prior work
Environment-assisted transfer in one-dimensional quantum chains was already examined by Kassal and Aspuru-Guzik (2012). Contreras-Pulido and collaborators (2014) studied a three-quantum-dot chain with uniformly applied dephasing and source/drain currents. Zhang and collaborators (2017) derived exact trimer transport times for uniformly applied dephasing and treated detuning disorder. Behzadi and collaborators (2014) studied selective dephasing in larger networks. Lawrence, Wang, and Segal (2026) considered site-engineered noise and a three-site ramped system, but their analytic expressions concern other noise locations and perturbative transport limits. None of the examined passages establishes the **fixed two-endpoint dephasing-budget exact mean-time optimum** with its two sharp detuning thresholds. This comparison is not a claim of exhaustive priority: an equivalent specialized treatment may exist in unindexed literature.

## Limitations
The theorem fixes the coherent hopping strengths to one, uses the single-excitation Markovian Lindblad model, applies dephasing only at endpoints, and optimizes unconditional mean collection time from site 1. No claims are made about many-excitation transport, interactions, general three-site detunings, stochastic budget constraints, finite-time arrival quantiles, finite-temperature baths, or laboratory calibration. The 2026 source is used as later comparative literature, not as the archive-date focal source. The result has undergone only its stated self-review; no independent audit was performed.

## References
1. I. Kassal and A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems*, arXiv:1201.5202, first submitted 2012-01-25; full text: https://arxiv.org/html/1201.5202v2.
2. P. Contreras-Pulido and collaborators, *Dephasing-assisted transport in linear triple quantum dots*, arXiv:1407.0924, first submitted 2014-07-03; https://arxiv.org/html/1407.0924v2.
3. N. Behzadi and collaborators, *Dephasing-assisted selective incoherent quantum transport*, arXiv:1412.3745, first submitted 2014-12-11; https://arxiv.org/abs/1412.3745.
4. Zhang and collaborators, *Optimal Dephasing for Ballistic Energy Transfer in Disordered Linear Chains*, arXiv:1706.09524, first submitted 2017-06-29; https://arxiv.org/abs/1706.09524.
5. Lawrence, Wang and Segal, *Design Principles for Enhanced Quantum Transport with Site-Dependent Noise*, arXiv:2604.23005, first submitted 2026-04-24; https://arxiv.org/html/2604.23005v1.
