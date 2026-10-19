# Negative apex four-point correlations and exact nonlinear response at Toblerone compensation

## Finding
For the translation-invariant infinite zero-field decorated two-leg Ising ladder specified below, exactly at vanishing effective rung coupling, the connected four-point function of four **distinct** apex spins is strictly negative and has a universal crossed-pair factorization. If \(i_1<i_2<i_3<i_4\), then
\[
\operatorname{cum}(S_{i_1},S_{i_2},S_{i_3},S_{i_4})
=-C(i_1,i_3)C(i_2,i_4)
=-\frac{u^4}{4}\rho^{(i_2-i_1)+2(i_3-i_2)+(i_4-i_3)}<0,
\]
where \(C(i,j)=\mathbb E[S_iS_j]=(u^2/2)\rho^{|i-j|}\) for distinct indices, \(\rho=\tanh(J/T)\), and \(u=\tanh(2G/T)\).

The *integrated* connected fourth-order response also has a closed form. For \(M_N=\sum_{i=1}^N S_i\),
\[
\lim_{N\to\infty}\frac{\operatorname{cum}_4(M_N)}{N}
=-2-\frac{8u^2\rho}{1-\rho}
-\frac{3u^4\rho^2(3+2\rho-3\rho^2)}{(1-\rho)^3(1+\rho)}<0.
\]
Consequently, the cubic coefficient in the apex-only uniform-field magnetization response is strictly negative at compensation. In the strong-leg limit \(J/T\to\infty\) with fixed \(u\in(0,1)\), this fourth-cumulant density is asymptotic to \(-3u^4e^{6J/T}/8\).

## Assumptions and scope
Let \(A_i,B_i,S_i\in\{-1,1\}\) for \(i\in\mathbb Z\), and fix \(T,J,G>0\). The finite-range energy, with no direct apex-apex bond and no external fields, is
\[
\mathcal H=-\sum_i\left[J(A_iA_{i+1}+B_iB_{i+1})+R A_iB_i+G(A_i+B_i)S_i\right].
\]
Select exactly the compensated rung coupling
\[
R=-\frac T2\log\cosh(2G/T).
\]
All probabilities and expectations refer to the unique translation-invariant infinite-volume Gibbs state at this strictly positive temperature. Connected fourth moments mean joint cumulants: for centered variables \(Y_1,\dots,Y_4\),
\[
\operatorname{cum}(Y_1,Y_2,Y_3,Y_4)
=\mathbb E[Y_1Y_2Y_3Y_4]-\mathbb E[Y_1Y_2]\mathbb E[Y_3Y_4]-\mathbb E[Y_1Y_3]\mathbb E[Y_2Y_4]-\mathbb E[Y_1Y_4]\mathbb E[Y_2Y_3].
\]
The theorem addresses the apex spins and is not asserted for nonzero fields, uncompensated rungs, or apex-apex interactions. The strong-leg asymptotic holds with the dimensionless apex parameter \(u\) fixed.

## Proof
**1. Exact decoration-iteration reduction.** Summing one apex spin gives
\[
\sum_{S=\pm1}e^{(G/T)(A+B)S}
=2\cosh[(G/T)(A+B)]
=2\sqrt{\cosh(2G/T)}\,e^{[\log\cosh(2G/T)/2]AB}.
\]
Thus the total effective rung coupling equals \(R+(T/2)\log\cosh(2G/T)=0\). The leg-spin marginal is exactly the product of two independent zero-field Ising chains with nearest-neighbor coupling \(J\). In each chain, the nearest-neighbor sign increments are independent with mean \(\rho=\tanh(J/T)\); accordingly, for strictly ordered sites,
\[
\mathbb E[A_iA_j]=\rho^{j-i},\qquad
\mathbb E[A_{i_1}A_{i_2}A_{i_3}A_{i_4}]
=\rho^{(i_2-i_1)+(i_4-i_3)}.
\]
The same is true for \(B\), independently of \(A\). Conditional on the leg spins, the apex spins at distinct sites are independent and
\[
\mathbb E[S_i\mid A,B]
=\tanh[(G/T)(A_i+B_i)]=\frac u2(A_i+B_i).
\]

**2. Distinct-site fourth cumulant.** Put \(g_1=i_2-i_1\), \(g_2=i_3-i_2\), \(g_3=i_4-i_3\), all positive integers. Expanding the independent two-chain product yields
\[
\mathbb E[S_{i_1}S_{i_2}S_{i_3}S_{i_4}]
=\frac{u^4}{4}\rho^{g_1+g_3}(1+\rho^{2g_2}).
\]
For distinct \(i,j\), \(C(i,j)=u^2\rho^{|i-j|}/2\). The three pair products in the cumulant are respectively \(u^4\rho^{g_1+g_3}/4\), \(u^4\rho^{g_1+2g_2+g_3}/4\), and the same crossed term again. Subtracting gives precisely the negative formula in the Finding; its strict sign follows from \(0<u,\rho<1\).

**3. Repeated indices and summation.** A single apex spin is centered and takes the values \(\pm1\), so \(\operatorname{cum}_4(S_i)=-2\). For \(i\ne j\), direct cumulant identities using \(S_i^2=1\) give
\[
\operatorname{cum}(S_i,S_i,S_i,S_j)=-2C(i,j),\quad
\operatorname{cum}(S_i,S_i,S_j,S_j)=-2C(i,j)^2,\quad
\operatorname{cum}(S_i,S_i,S_j,S_k)=-2C(i,j)C(i,k)
\]
when the three sites in the last expression are distinct. Sum the ordered quadruples in \(\operatorname{cum}_4(M_N)\) according to their site multiplicity patterns \(4\), \(3+1\), \(2+2\), \(2+1+1\), and \(1+1+1+1\). Absolute summability follows from \(0<\rho<1\), so dividing by \(N\) and taking \(N\to\infty\) gives these five contributions in order:
\[
\begin{aligned}
&-2,\\
&-\frac{8u^2\rho}{1-\rho},\\
&-\frac{3u^4\rho^2}{1-\rho^2},\\
&-\frac{12u^4\rho^2}{(1-\rho)^2}+\frac{6u^4\rho^2}{1-\rho^2},\\
&-\frac{6u^4\rho^4}{(1-\rho)^2(1-\rho^2)}.
\end{aligned}
\]
The last contribution uses the ordered-gap sum \(\sum_{g_1,g_2,g_3\ge1}\rho^{g_1+2g_2+g_3}=\rho^4/[(1-\rho)^2(1-\rho^2)]\). Collecting the terms proportional to \(u^4\) produces the rational expression in the Finding. It is strictly negative since \(3+2\rho-3\rho^2=3(1-\rho^2)+2\rho>0\).

**4. Nonlinear response and asymptotic.** Adding \(-h\sum_i S_i\) to the energy, the third derivative at zero field of magnetization per apex site is the fourth-cumulant density divided by \(T^3\). No thermodynamic singularity at finite positive \(T\) is claimed. Finally \(1-\tanh(J/T)\sim2e^{-2J/T}\), yielding \(-3u^4e^{6J/T}/8\) for the leading density.

## Verification
The accompanying standalone program `verify.py` uses `mpmath` and `sympy`; run `python verify.py`. It independently constructs the finite periodic four-state transfer matrix with an apex magnetic field, computes the fourth Taylor coefficient of the finite partition function, and compares the resulting fourth cumulant per site with the infinite-chain formula at two lengths and several positive couplings. It also enumerates leg-index assignments for widely separated distinct apex quadruples and simplifies the geometric-series identity symbolically. The recorded execution passed 38 checks. Finite-size transfer agreement supports but does not replace the infinite-volume proof above; convergence there rests on absolute summability.

## Relationship to prior work
Hutak et al. established the decoration-iteration transformation and vanishing effective rung coupling for the two-leg Ising ladder. Chapman, Tomasello and Carr then analyzed the same model's eigenvalue crossing, pair correlations, correlation-length bifurcation, and linear top-spin susceptibility. The present result uses their known compensation mechanism rather than claiming its discovery. The new evaluated objects are the connected four-distinct-apex function, its exact crossed-pair identity, and the fully summed fourth-cumulant density giving the cubic apex-only magnetic response, including its strong-leg amplification. General Ising-chain multipoint identities and general transfer-matrix machinery imply a route to these expressions; priority of an equivalent previously evaluated specialization requires independent investigation.

## Limitations
This is an exact zero-field, compensated-rung statement for one infinite-volume Gibbs state. A fixed-rung experimental temperature sweep crosses the compensation condition only at special temperatures. Negative fourth cumulants do not imply a genuine positive-temperature phase transition. The theorem does not address finite-sample observability, direct apex bonds, general fields, unequal legs, or arbitrary finite sizes. The calculation is supported by finite-periodic tests but is mathematically proven by the conditional-independence and summation arguments. Independent audit and external priority validation have not been performed.

## References
1. J. Chapman, B. Tomasello, and S. T. Carr, *Bifurcation in correlation length of the Ising model on a “Toblerone” lattice*, arXiv:2405.20749 (first public version 31 May 2024); *Journal of Statistical Mechanics* **2024**, 093214. https://arxiv.org/abs/2405.20749
2. T. Hutak, T. Krokhmalskii, O. Rojas, S. M. de Souza, and O. Derzhko, *Low-temperature thermodynamics of the two-leg ladder Ising model with trimer rungs: A mystery explained*, arXiv:2008.03753 (2020); *Physics Letters A* **387**, 127020 (2021). https://arxiv.org/abs/2008.03753
3. W. Yin, *Paradigm for approaching the forbidden spontaneous phase transition in the one-dimensional Ising model at a fixed finite temperature*, *Physical Review Research* **6**, 013331 (2024), arXiv:2006.08921. https://arxiv.org/abs/2006.08921
