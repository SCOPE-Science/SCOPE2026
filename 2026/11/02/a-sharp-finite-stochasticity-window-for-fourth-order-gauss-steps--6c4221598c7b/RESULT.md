# A sharp finite stochasticity window for fourth-order Gauss steps on the directed eight-cycle

## Finding

Let \(S\) be the directed eight-cycle shift and \(Q=S-I_8\) its unit-rate continuous-time Markov generator. For the two-stage fourth-order Gauss–Legendre method, the one-step endpoint matrix \(M(h)\) is entrywise nonnegative **if and only if**
\[
 h=0\quad\text{or}\quad 6\alpha\le h\le6\beta.
\]
Here \(\alpha\) and \(\beta\) are the unique positive roots, respectively, of
\[
 A(x)=756x^6+1512x^5+1260x^4+504x^3+84x^2-1,
\]
\[
\begin{aligned}
 B(x)={}&14580x^{12}+46656x^{11}+64152x^{10}+49572x^9+20898x^8\\
 &-6939x^6-5508x^5-2511x^4-756x^3-150x^2-18x-1.
\end{aligned}
\]
In particular, \(6\alpha\approx0.512251544372714\), \(6\beta\approx3.527197466269433\), and this irreducible conservative chain loses endpoint positivity at *every sufficiently small positive step*. For each endpoint one cyclic-displacement probability is zero; throughout the open interval all entries are positive. The endpoint map conserves mass for every nonnegative step for which it is defined.

## Assumptions and scope

Index states by \(0,1,\ldots,7\) modulo eight. Set \(S_{i,j}=1\) exactly when \(j=i+1\pmod8\), all other entries zero, and \(Q=S-I_8\). Then \(Q\mathbf1=0\) and the continuous-time chain is irreducible. The timestep \(h\) is real with \(h\ge0\), and the unit jump rate fixes the normalization. The fourth-order Gauss endpoint map is exactly the rational matrix
\[
 M(h)=\left(I_8-\frac h2 Q+\frac{h^2}{12}Q^2\right)^{-1}
       \left(I_8+\frac h2 Q+\frac{h^2}{12}Q^2\right).
\]
This is only an endpoint entrywise-positivity statement, not an internal-stage or accuracy assertion. A jump rate \(\lambda>0\) replaces \(h\) by \(\lambda h\).

## Proof

**Step 1: cyclic coefficients and denominator.** Put
\[
 D(z,h)=12+6h(1-z)+h^2(1-z)^2,
 \qquad N(z,h)=12-6h(1-z)+h^2(1-z)^2.
\]
Since \(S^8=I\), reduce \(N/D\) in the quotient ring \(\mathbb Q(h)[z]/(z^8-1)\): there are exact rational functions \(c_j(h)\) such that
\[
 M(h)=\sum_{j=0}^{7}c_j(h)S^j,\qquad
 \sum_{j=0}^{7}c_j(h)=1.
\]
The denominator \(D(S,h)\) is nonsingular for every \(h\ge0\): its scalar stability denominator has roots \(3\pm i\sqrt3\), whereas the eigenvalues of \(hQ\) have nonpositive real parts. A strictly positive common denominator for \(h\ge0\) is
\[
\begin{aligned}
 W(h)={}&4(h^2+3h+3)(h^4+6h^3+18h^2+36h+36)\\
 &\cdot(h^8+12h^7+84h^6+432h^5+1800h^4+5184h^3\\
 &\qquad+9504h^2+10368h+5184).
\end{aligned}
\]
Straight polynomial reduction gives \(c_j(h)=H_j(h)/W(h)\), with the following exact factorizations. Define
\[
\begin{aligned}
 P_1(h)={}&5h^{12}+96h^{11}+792h^{10}+3672h^9+9288h^8\\
 &-111024h^6-528768h^5-1446336h^4-2612736h^3\\
 &-3110400h^2-2239488h-746496,\\
 P_2(h)={}&h^{10}+10h^9-516h^7-4248h^6-19728h^5\\
 &-60912h^4-128736h^3-181440h^2-155520h-62208,\\
 P_3(h)={}&h^{10}-12h^9-396h^8-3888h^7-22176h^6\\
 &-84672h^5-225072h^4-414720h^3-508032h^2\\
 &-373248h-124416,\\
 P_7(h)={}&7h^6+84h^5+420h^4+1008h^3+1008h^2-432.
\end{aligned}
\]
Then
\[
\begin{aligned}
 H_1&=-3hP_1(h),& H_2&=-9h^2(h+2)P_2(h),\\
 H_3&=-3h^3P_3(h),& H_7&=3h^7P_7(h).
\end{aligned}
\]
The other four numerators are nonnegative polynomials with strictly positive coefficients:
\[
\begin{aligned}
 H_0={}&4h^{14}+63h^{13}+420h^{12}+1512h^{11}+3276h^{10}\\
 &+4536h^9+7344h^8+58320h^7+399168h^6+1632960h^5\\
 &+4354560h^4+7838208h^3+9331200h^2+6718464h+2239488,\\
 H_4={}&3h^4(h^9+48h^8+624h^7+4284h^6+18648h^5\\
 &+54432h^4+106704h^3+134784h^2+98496h+31104),\\
 H_5={}&9h^5(h+2)(h^7+22h^6+180h^5+816h^4\\
 &+2232h^3+3600h^2+3024h+864),\\
 H_6={}&3h^7(5h^6+84h^5+588h^4+2268h^3\\
 &+5040h^2+6048h+3024).
\end{aligned}
\]
These identities can be checked by multiplying \(D(z,h)\sum_jH_j(h)z^j\), reducing modulo \(z^8-1\), and comparing with \(W(h)N(z,h)\); the included exact-arithmetic program independently performs the modular inverse and factor checks. Thus no numerical fit is used.

**Step 2: isolate the two active boundaries.** Each of \(P_1,P_2,P_3,P_7\) has exactly one sign change in its descending nonzero coefficients, is strictly negative at zero and positive at sufficiently large \(h\). Descartes' rule, with continuity, therefore gives **exactly one positive real root** for each. Let \(h_-\) be that of \(P_7\), and \(h_+\) that of \(P_1\). Exact rational evaluations give
\[
\frac12<h_-<\frac35<\frac72<h_+<4,
\qquad P_2(4)<0,\quad P_3(4)<0.
\]
Consequently, for \(0<h\le4\), both \(H_2\) and \(H_3\) are strictly positive; \(H_0,H_4,H_5,H_6\) are also strictly positive. Since \(W>0\), the only remaining conditions on this range are
\[
 H_7(h)\ge0\iff h\ge h_-,\qquad
 H_1(h)\ge0\iff h\le h_+.
\]
For any \(0<h<h_-\), the seventh cyclic-displacement entry is negative. For \(h>h_+\), the first cyclic-displacement entry is negative, including all \(h>4\). Hence \(M(h)\ge0\) entrywise exactly for \(h\in[h_-,h_+]\) among positive steps. At zero, \(M(0)=I\).

**Step 3: normalize the algebraic endpoints.** Substitute \(h=6x\). Taking the positive primitive integer multiples gives \(P_7(6x)\sim A(x)\) and \(P_1(6x)\sim B(x)\). Thus \(h_-=6\alpha\) and \(h_+=6\beta\). Uniqueness and the stated endpoints follow. Because every row of \(Q\) sums to zero, \(M(h)\mathbf1=\mathbf1\) always, so entrywise nonnegativity is exactly row-stochasticity. At \(h_-,h_+\) respectively just \(H_7,H_1\) vanish, proving the strict interior statement.

## Verification

The standalone `verify.py` requires Python 3.10+ and SymPy 1.10+. Run `python verify.py`. It reconstructs the rational function in the quotient algebra from scratch, verifies all eight exact numerator identities, proves the Descartes sign-variation and rational-root bracket assertions, checks the two primitive endpoint polynomials, and computes the full rational \(8\times8\) inverse independently at ten rational timestep values. These finite instances test the formulas; the global if-and-only-if is established by the preceding sign proof, not by sampling.

## Relationship to prior work

Zappavigna–Colaneri–Kirkland–Shorten (publicly deposited June 19, 2012) demonstrate that diagonal Padé discretization need not preserve positivity, including an eight-state nilpotent shift and related Metzler examples. Their general feedback-chain matrix includes cyclic feedback as a possible architecture, but their inspected proof does not give the exact conservative eight-cycle stochasticity set. The published eight-state pure-birth Markov result gives a different absorbing-endpoint window, not this periodic closure; it also establishes the minimal number of states for small-step failure, which is not claimed anew. Lóczi–Ketcheson give general rational absolute-monotonicity theory, and Higueras–Ketcheson–Kocsis study modified Runge–Kutta methods. Neither inspected work supplies this explicit unmodified Gauss cycle interval. The exact finite cyclic-window boundary, rather than the already known existence of negative entries, is the additional assertion here.

## Limitations

Only the directed unit-rate eight-cycle and its uniform positive time/rate rescaling are classified. The result does not classify all cycle lengths, unequal rates, internal-stage positivity, floating-point behavior, approximation error or other Padé orders. The exact algebraic endpoints are not asserted to optimize accuracy. Relevant literature may contain an equivalent formula not identified in the material inspected; independent mathematical review is not yet available.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, publicly deposited June 19, 2012, https://mural.maynoothuniversity.ie/id/eprint/3761/ (public manuscript, especially Section 4).
2. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651 (initially March 26, 2013), https://arxiv.org/abs/1303.6651 .
3. I. Higueras, D. I. Ketcheson, T. A. Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge–Kutta method*, arXiv:1505.04024 (initially May 15, 2015), https://arxiv.org/abs/1505.04024 .
4. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, published technical result, https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab .
