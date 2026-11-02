# Two-scale reversal of output noise in the minimal pausing exclusion chain

## Finding

Consider stationary open totally asymmetric exclusion with one or two sites, a reversible paused state, and rates as defined below. Let \(F_L(k,u)\) be the long-time Fano factor of completed right-boundary exits on a chain of length \(L\). **For every \(0<u\le 1/10\), there are exactly two positive pausing rates \(k_-(u)<k_+(u)\)** for which \(F_2=F_1\). Their complete noise-ordering pattern is
\[
F_2<F_1\quad(0<k<k_-),\qquad F_2>F_1\quad(k_-<k<k_+),\qquad F_2<F_1\quad(k>k_+).
\]
The two crossings occur on *different singular scales* as unpausing becomes slow:
\[
\lim_{u\downarrow0}\frac{k_-(u)}{u^2}=\frac7{15},\qquad
\lim_{u\downarrow0}\frac{k_+(u)}{u}=t_c,
\]
where \(t_c=1.113211611282\ldots\) is the unique positive zero of
\(31t^4+78t^3+13t^2-100t-60\).

There is also a sharp leading global optimization law. For any global maximizer \(k_{\mathrm{opt}}(u)>0\) of \(F_2(k,u)\),
\[
\lim_{u\downarrow0}\frac{k_{\mathrm{opt}}(u)}u=t_*=1.001802622284\ldots,
\quad\lim_{u\downarrow0}u\max_{k>0}F_2(k,u)=g(t_*)=0.230468969852\ldots,
\]
where \(t_*\) is the unique positive root of \(63t^4+285t^3+150t^2-300t-200\) and
\[
g(t)=\frac{4t(9t^2+30t+20)}{(7t^2+15t+10)^2}.
\]
No finite-\(u\) uniqueness of the maximizing rate is asserted.

## Assumptions and scope

The system is an open chain of length \(L\in\{1,2\}\). Each site is empty \(0\), active \(A\), or paused \(P\). A particle enters the first empty site (only when site one is empty) at rate one in state \(A\); an active particle advances one site rightward into a vacancy at rate one; an active particle at the last site exits at rate one. At each occupied site, \(A\to P\) at rate \(k>0\) and \(P\to A\) at rate \(u>0\). Paused particles do not hop or exit. Time is measured in units of the common injection/hopping/exit rate. For these positive rates the three-state or nine-state chain is irreducible.

Write \(N_L(T)\) for the number of right exits in \([0,T]\) in its stationary process, \(J_L=\lim_{T\to\infty}\mathbb EN_L(T)/T>0\), and
\[
F_L(k,u)=\lim_{T\to\infty}\frac{\operatorname{Var}N_L(T)}{\mathbb EN_L(T)}.
\]
The comparison fixes identical microscopic rates and uses two separate chain lengths, not a thermodynamic limit. The universal double-crossing assertion is limited to \(0<u\le1/10\); the exact rational formulas hold for all \(k,u>0\).

## Proof

**1. Stationary counting formulas.** Index states lexicographically in \(\{0,A,P\}^2\). Let \(Q\) be the nine-state row generator and \(B\) its nonnegative off-diagonal matrix of counted exit transitions (entries one for each active right-boundary exit). For stationary column \(\pi\) satisfying \(Q^{\mathsf T}\pi=0\) and \(\mathbf1^{\mathsf T}\pi=1\), let \(b=B\mathbf1\), \(J=\pi^{\mathsf T}b\), and solve the uniquely normalized Poisson equation
\[
Qh=J\mathbf1-b,\qquad \pi^{\mathsf T}h=0.
\]
Perturbing the dominant eigenvalue of \(Q+(e^s-1)B\) at \(s=0\) gives exactly
\[
F_2=1+\frac{2\pi^{\mathsf T}Bh}{J}.
\]
The positive stationary rate and Poisson equation are solved by exact rational linear algebra, with the full independently executable generator construction in `verify.py`. Row elimination yields
\[
J_2=\frac{u(k+2u+2)(2k^2+4ku+k+2u^2+2u)}{D(k,u)},\qquad
F_2=\frac{P(k,u)}{D(k,u)^2},
\]
with the complete polynomials printed here:

\[
D(k,u)=4k^4+20k^3u+12k^3+38k^2u^2+40k^2u+7k^2
+32ku^3+47ku^2+15ku+10u^4+20u^3+10u^2.
\]

\[
\begin{aligned}
P(k,u)={}&8k^8+(80u+56)k^7+(336u^2+464u+158)k^6\\
&+(792u^3+1576u^2+1060u+220)k^5\\
&+(1164u^4+2912u^3+2836u^2+1172u+145)k^4\\
&+(1104u^5+3220u^4+3918u^3+2364u^2+620u+36)k^3\\
&+(664u^6+2168u^5+2989u^4+2210u^3+845u^2+120u)k^2\\
&+(232u^7+836u^6+1220u^5+940u^4+404u^3+80u^2)k\\
&+36u^8+144u^7+216u^6+144u^5+36u^4.
\end{aligned}
\]

The same three-state construction, or direct renewal accounting for successive exits, gives
\[
J_1=\frac{u}{k+2u},\qquad
F_1=\frac{k^2+2ku+2k+2u^2}{(k+2u)^2}.
\]
All denominators are strictly positive for positive parameters; the rational identities can be verified coefficientwise, without numerical fitting.

**2. Exactly two crossings.** Set
\[
C(k,u)=(k+2u)^2D(k,u)^2(F_2-F_1).
\]
In descending powers of \(k\), the eleven coefficients of the degree-ten polynomial \(C\) have signs
\[
(-,-,-,-,-,-,-,-,+,+,-),\qquad0<u\le1/10.
\]
An exact coefficient list and symbolic identity check are included in `verify.py`. The two potentially less obvious signs are the positive \(k^2\)-coefficient
\[
-2u^3(u+1)(664u^4+1644u^3+839u^2-161u-100)>0
\]
and positive \(k\)-coefficient
\[
-8u^4(u+1)^2(3u-1)(17u^2+35u+15)>0.
\]
For the first inequality, the positive part of the parenthesis is at most \(0.0664+1.644+8.39=10.1004\) while its negative constant is \(-100\). By Descartes' rule, there are at most two positive roots, counted with multiplicity. At \(k\downarrow0\), \(F_2-F_1=9/25-1/2=-7/50<0\); as \(k\to\infty\), \(F_2-F_1\to1/2-1=-1/2<0\). At \(k=u^2\), direct substitution and a positive denominator give
\[
F_2-F_1=-\frac{2E(u)}{(u+2)^2(4u^6+20u^5+50u^4+72u^3+64u^2+35u+10)^2},
\]
where
\[
E(u)=4u^{14}+40u^{13}+220u^{12}+836u^{11}+2377u^{10}+5218u^9+8938u^8+11925u^7+12267u^6+9511u^5+5298u^4+1899u^3+292u^2-68u-32.
\]
For \(0<u\le1/10\), its positive terms are bounded by their value at \(1/10\), which is less than \(7\), whereas its remaining terms are negative; hence \(E(u)<0\). Consequently there is a root on each side of \(u^2\), and Descartes' bound makes them the only two roots, both simple, establishing the strict ordering.

**3. Two different singular scales.** Uniformly for \(c\) in compact positive intervals, exact substitution \(k=cu^2\) yields
\[
F_2(cu^2,u)\to\frac{20c+9}{25},\quad
F_1(cu^2,u)\to\frac{c+1}{2},\quad
F_2-F_1\to\frac{15c-7}{50}.
\]
Bracketing the first root by \(c=(7/15)\pm\delta\) shows \(k_-/u^2\to7/15\). For \(k=ut\), uniformly for \(t\) in compact positive intervals,
\[
uF_2(ut,u)\to g(t),\quad
uF_1(ut,u)\to\frac{2t}{(t+2)^2},
\]
\[
g(t)-\frac{2t}{(t+2)^2}=
-\frac{2t(31t^4+78t^3+13t^2-100t-60)}{(t+2)^2(7t^2+15t+10)^2}.
\]
The quartic has one positive root by its single sign change; sign bracketing forces \(k_+/u\to t_c\). These asymptotics concern \(u\downarrow0\) with \(k\) scaled as stated and do not assert uniformity for arbitrary simultaneous approaches to the origin.

**4. Global noise maximization.** Differentiate the limiting profile:
\[
g'(t)=-\frac{4(63t^4+285t^3+150t^2-300t-200)}{(7t^2+15t+10)^3}.
\]
Its numerator has exactly one positive zero, with positive derivative before and negative afterward, proving the unique limiting maximizer \(t_*\). To justify *global*, not merely local, convergence, put \(H_u(t)=uF_2(ut,u)\). All coefficients of \(P\) and \(D\) are nonnegative. For \(0<u\le1\), direct grouping by powers in the displayed exact polynomials yields bounds, with a numerical constant \(C\) independent of \(u,t\),
\[
0<H_u(t)\le C(t+u)\quad(0<t\le1),\qquad
0<H_u(t)\le C(t^{-1}+u)\quad(t\ge1).
\]
For the second estimate: \(P(ut,u)/u^3\le C t^3(1+ut)^5\), whereas \(D(ut,u)/u^2\ge t^2(4(ut)^2+12ut+7)\ge c_0t^2(1+ut)^2\). For the first, use \(D(ut,u)/u^2\ge10\) and group every numerator monomial as \(O(t+u)\). Thus for any sequence \(u\downarrow0\), global maximizers of \(H_u\) cannot escape toward \(0\) or infinity: outside a compact interval the upper bounds tend to zero, while \(H_u(t_*)\to g(t_*)>0\). Compact convergence and uniqueness of the maximum of \(g\) imply the stated limits for every choice of global maximizers. Existence follows because \(F_2\) extends continuously to \(k=0\) and \(k=\infty\), where for sufficiently small \(u\), \(uF_2\) lies below its interior value.

## Verification

Run `python verify.py` with SymPy installed. It independently constructs all nine generator states and counting edges, solves the exact stationary and normalized Poisson systems, confirms each polynomial identity, verifies the difference coefficients and limiting profiles, and checks selected positive rational parameter pairs. The code asserts the limiting quartic derivative identities and isolates numerical root approximations. Analytic positivity, root counts, compactness, and universal quantifiers are established in the proof above; finitely many tests are not substituted for those arguments.

## Relationship to prior work

Thommen (2026) studies low-frequency output noise in open exclusion with reversible particle pausing, emphasizes finite-size intermittency and a noise maximum for substantially larger chains, and supplies approximate collective explanations. Keisers et al. (2024) establish the pausing-particle model and its finite-size mean-current consequences, including a particle-hole mapping to dynamical defects. Wang et al. (2014) study an earlier pause-aware transcriptional model. The general eigenvalue-perturbation/Poisson method for Markov current cumulants predates this work. The present specific claim is the *strict length-two versus length-one noise-ordering reversal at two distinct singular scales*, together with its exact, globally optimized asymptotic profile. It does not claim the underlying Markov method or the existence of nonmonotone noise as new.

## Limitations

The explicit proof assumes injection, hopping, and exit rates all equal one, and the double-reversal theorem is stated for \(0<u\le1/10\). Arbitrary chain lengths, different boundary rates, finite-time noise, and the exact uniqueness of the maximizing rate for each finite \(u\) are not established. The asymptotic optimization is proved as \(u\downarrow0\), not for fixed macroscopic unpausing rates. A broader pre-existing exact small-chain full-counting calculation or a general implication theorem could cover part of this statement; independent priority assessment has not occurred.

## References

1. Quentin Thommen, *Low-frequency output fluctuations in an open exclusion process with particle pausing*, arXiv:2608.08074v1 (first public 2026-08-08), https://arxiv.org/abs/2608.08074.
2. Johannes Keisers, Lorenzo Vito Dal Zovo, Norbert Kern, Luca Ciandrini, *Biologically relevant finite-size effects in a driven lattice gas with particle pausing and dynamical defects*, arXiv:2406.16569 (first public 2024-06-24), https://arxiv.org/abs/2406.16569.
3. Wang et al., *Minimal model of transcriptional elongation processes with pauses*, arXiv:1411.4978 (2014), https://arxiv.org/abs/1411.4978.
