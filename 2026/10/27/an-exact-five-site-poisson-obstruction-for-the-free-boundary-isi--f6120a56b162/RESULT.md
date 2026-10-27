# An exact five-site Poisson obstruction for the free-boundary Ising square

## Finding
Let \(G\) be the \(3\times3\) square nearest-neighbour graph with free boundary. Let \(S\) consist of its centre and the four vertices immediately north, south, east and west of that centre. The zero-field ferromagnetic Ising model of coupling \(\beta>0\) on \(G\) does **not** admit a representation as the union of random subsets from a Poisson process whenever
\[
0<\beta<\beta_*=0.23285659134411550047\ldots.
\]

More precisely, the unique *putative* Poisson intensity of the exact five-vertex atom \(S\), whether positive or negative, is
\[
\Lambda_S(\beta)=\log\frac{P_0(t)P_2(t)^6P_4(t)}{P_1(t)^4P_3(t)^4},\qquad t=e^{-2\beta},\quad P_k(t)=(1+t^3)^k+t^4(1+t)^k.
\]
This quantity is negative exactly on the displayed interval, zero at \(\beta_*\), and positive for \(\beta>\beta_*\). The threshold is the unique \(\beta_*>0\) obtained from a root \(t_*\in(0,1)\) of the explicit polynomial below by \(\beta_*=-\tfrac12\log t_*\). Only **the five-site obstruction**, not complete Poisson representability, has this sharp sign threshold.

## Assumptions and scope
The vertex set \(V=\{(i,j):0\le i,j\le2\}\) contains nine sites and the edge set joins vertices at Manhattan distance one (twelve edges). Write \(\sigma_v\in\{-1,+1\}\). The law of a spin configuration is proportional to \(\exp(\beta\sum_{\{u,v\}\in E}\sigma_u\sigma_v)\). Equivalently, relative to the all-minus configuration, the weight of its set \(C\) of plus vertices is \(t^{b(C)}\), where \(t=e^{-2\beta}\) and \(b(C)\) is the number of edges with precisely one endpoint in \(C\). The event \(X_v=0\) means \(\sigma_v=-1\). A Poisson-union representation would be a family of independent Poisson counts indexed by the nonempty subsets \(T\subseteq V\), with nonnegative finite means \(\nu(T)\), such that \(X\) is the indicator of their union. Every all-zero avoidance event has strictly positive probability, so putative means are finite.

## Proof
**(1) Unique inversion of avoidance probabilities.** For \(U\subseteq V\), put \(q(U)=\Pr(X_v=0\text{ for every }v\in U)\), which is strictly positive. In a Poisson-union representation,
\[
-\log q(U)=\sum_{T:T\cap U\ne\varnothing}\nu(T).
\]
For \(B\subseteq V\), set \(F(B)=q(V\setminus B)\). Then
\[
\log F(B)=-\sum_{T\ne\varnothing}\nu(T)+\sum_{T\subseteq B}\nu(T).
\]
Möbius inversion yields for every nonempty \(S\subseteq V\)
\[
\nu(S)=\sum_{B\subseteq S}(-1)^{|S|-|B|}\log F(B).
\]
This is a necessary, *uniquely determined* intensity, and representability requires \(\nu(S)\ge0\). It is a genuine single-atom test, not an equivalence to representability unless all nonempty atom intensities are nonnegative.

**(2) Exact constrained partition functions.** The five-site cross has one centre and four arms; all four grid corners lie outside \(S\). To compute \(F(B)\), force every vertex outside \(B\) minus, and sum the Ising weights over plus spins allowed on \(B\). Suppose \(B\) contains exactly \(k\) arms. If it excludes the centre, each selected arm independently contributes a choice of being minus (weight \(1\)) or plus (three disagreeing edges, weight \(t^3\)), so its constrained weight is \((1+t^3)^k\). If it includes the centre, configurations with centre minus give the same term; configurations with centre plus have baseline weight \(t^4\) from the four centre-arm edges, and each selected arm offers an additional factor \(1+t\). Thus the numerator of \(F(B)\) is
\[
Z_{0,k}(t)=(1+t^3)^k\quad\text{or}\quad Z_{1,k}(t)=P_k(t)=(1+t^3)^k+t^4(1+t)^k.
\]
The common global partition function cancels from the fivefold alternating logarithmic sum. Because \(\log Z_{0,k}=k\log(1+t^3)\) is affine in \(k\), its fourth difference vanishes. The remaining fourth difference of \(\log P_k\) is
\[
\Lambda_S=\sum_{k=0}^{4}(-1)^{4-k}\binom4k\log P_k
=\log(P_0P_2^6P_4/(P_1^4P_3^4)).
\]

**(3) Sign certificate and unique threshold.** Define \(H(t)=P_0P_2^6P_4-P_1^4P_3^4\). Exact polynomial multiplication gives
\[
H(t)=-t^8(t-1)^4(t+1)^{16}Q_{28}(t),
\]
where the *ascending-power* coefficients of \(Q_{28}(t)\), beginning with its constant term, are
\[
(-1,12,-78,352,-1221,3432,-8074,16236,-28305,43180,-57950,68532,-71207,64384,-49506,30592,-12493,-980,8324,-10228,8732,-5948,3370,-1592,624,-196,48,-8,1).
\]
These coefficients completely specify the integer polynomial without any omitted terms. Let \(z=t/(1-t)\), so \(t=z/(1+z)\). The ascending coefficients of the transformed polynomial \(R(z)=(1+z)^{28}Q_{28}(z/(1+z))\) are
\[
(-1,-16,-132,-740,-3146,-10752,-30614,-74360,-156642,-289544,-473518,-688884,-894228,-1036304,-1069782,-977884,-782196,-534968,-297388,-115684,-7447,36724,40606,28052,14449,5680,1648,320,32).
\]
The coefficients of \(R\) change sign exactly once; its constant term is negative and its leading coefficient positive. Descartes' rule of signs and the intermediate value theorem imply that \(R\) has exactly one positive real root. The change of variables is a bijection from \((0,1)\) to \((0,\infty)\), so \(Q_{28}\) has exactly one root \(t_*\) in \((0,1)\). Moreover \(Q_{28}(0)=-1\) and \(Q_{28}(1)=32\). The prefactor multiplying \(-Q_{28}\) in \(H\) is strictly positive for \(0<t<1\), while the denominator of the logarithm is positive. Therefore \(\Lambda_S\) is positive for \(t<t_*\), zero at \(t=t_*\), and negative for \(t_*<t<1\). Since \(t=e^{-2\beta}\) decreases strictly with \(\beta\), the asserted temperature ordering follows. The exact algebraic and finite enumeration identities are reproducible with the included verification program.

**(4) Boundary behavior.** The same factorization and positive denominator give \(\Lambda_S(\beta)=-2\beta^4+O(\beta^5)\) as \(\beta\downarrow0\) and \(\Lambda_S(\beta)\sim e^{-16\beta}\) as \(\beta\to\infty\). These are expansions of the single putative atom intensity, not expansions of any full representability probability.

## Verification
Run \(`python3 verification/check_cross_intensity.py`\) using the Python standard library. Its exact-arithmetic component constructs all five polynomials, verifies the displayed degree-56 factorization, computes all twenty-nine coefficients of \(R\) by a binomial transform, proves the single sign change, and isolates the root by decimal bisection. Its separate numerical check enumerates all \(2^9=512\) spin configurations at five specified temperatures and compares the fivefold Möbius inversion with the compressed formula. The latter finite-temperature checks are supporting consistency tests; the polynomial identity and Descartes certificate establish the statement for all \(\beta>0\).

## Relationship to prior work
Forsström, Gantert and Steif (first arXiv appearance January 2024) introduced Poisson representability, the finite-set inversion framework, and nonrepresentability results for certain infinite-dimensional Ising models. Bethuelsen and Forsström (first arXiv appearance January 24, 2025) studied mixing and excluded the Ising plus phase in the ordered region of the infinite square lattice. Forsström's 2025 tree-indexed Markov chain preprint studies parameter-dependent representability on trees. The present statement neither reclaims those general criteria nor draws a conclusion about infinite-volume ordering: it computes an exact five-site intensity in a free-boundary nine-spin cyclic graph and determines its sharp sign transition.

## Limitations
The result concerns the centre-plus-arms Poisson atom on exactly the free-boundary \(3\times3\) Ising grid. It proves nonrepresentability for \(0<\beta<\beta_*\). At \(\beta=\beta_*\) this atom intensity vanishes, and for \(\beta>\beta_*\) it is positive; **nothing here establishes that all the other Poisson intensities are nonnegative**, so no full representability phase transition is asserted. No thermodynamic-limit, boundary-field, sparse-graph or higher-dimensional extension is proved. The originality assessment is based on primary-literature comparison, not a guarantee of exhaustive historical priority.

## References
1. S. A. Bethuelsen and M. P. Forsström, *Mixing for Poisson representable processes and consequences for the Ising model and the contact process*, arXiv:2501.14445, first submitted January 24, 2025. https://arxiv.org/abs/2501.14445.
2. M. P. Forsström, N. Gantert and J. E. Steif, *Poisson representable processes*, arXiv:2401.13412, first submitted January 2024; *Probability Theory and Related Fields* 195 (2026). https://arxiv.org/abs/2401.13412.
3. M. P. Forsström, *Poisson representations for tree-indexed Markov chains*, arXiv:2501.14428, first submitted January 24, 2025. https://arxiv.org/abs/2501.14428.
