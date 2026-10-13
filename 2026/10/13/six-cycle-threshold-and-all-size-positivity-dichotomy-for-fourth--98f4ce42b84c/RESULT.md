# Six-cycle threshold and all-size positivity dichotomy for fourth-order Gauss diffusion

## Finding
Let \(C_n\), \(n\ge3\), be the unit-rate nearest-neighbor periodic diffusion chain, whose generator \(Q_n=-L(C_n)\) has off-diagonal entry one at each cyclic neighbor and diagonal entry \(-2\). The fourth-order two-stage Gauss–Legendre end-step map is
\[
T_n(h)=R(hQ_n),\qquad
R(z)=\frac{12+6z+z^2}{12-6z+z^2},\qquad h\ge0.
\]

**All-size dichotomy.** For \(n=3,4,5\), \(T_n(h)\) is entrywise strictly positive at every positive step. For every \(n\ge6\), nearest-neighbor entries become negative at all sufficiently large steps, with the sharp leading asymptotic
\[
\boxed{[T_n(h)]_{0,1}=-\frac{(n-1)(n-5)}{nh}+O_n(h^{-2}).}
\]
Thus a six-point periodic mesh is the first uniform periodic diffusion mesh for which this fourth-order implicit Gauss update loses unconditional nonnegativity.

**First failing cycle, with exact threshold.** Set
\[
F_6(h)=5h^4-12h^3-102h^2-144h-72.
\]
The polynomial has exactly one positive root,
\[
h_6=6.36885080963102\ldots.
\]
Then
\[
\boxed{T_6(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad0\le h\le h_6.}
\]
The inequality is sharp at \(h=h_6\), where the nearest-neighbor entries vanish. All other distinct entries are strictly positive whenever \(h>0\). At the simple rational step \(h=7\),
\[
[T_6(7)]_{0,1}=-\frac{25354}{4790839}<0.
\]
The exact Markov semigroup \(e^{hQ_n}\), by contrast, is entrywise positive for every \(h>0\). Moreover, \(T_n(h)\) itself remains symmetric, mass-conserving, positive definite and spectrally stable at all finite steps. Hence neither symmetry nor spectral stability protects stochastic positivity.

## Assumptions and scope
The chain is a *simple unweighted undirected cycle* with \(n\ge3\). Each vertex has two distinct neighbors; the unit edge rate fixes the time scale. For a common edge rate \(\gamma>0\), replace \(h\) by \(\gamma h\) in all thresholds. The theorem applies to exact arithmetic and the end-step matrix, not to internal implicit Runge–Kutta stages or rounded linear solves.

The adjective *unconditionally nonnegative* means every matrix entry is nonnegative for every \(h\ge0\); it is not a statement about convergence order. Since \(T_n(h)\mathbf1=\mathbf1\), entrywise nonnegativity is equivalent to the end-step matrix being a valid Markov transition matrix.

The first-size claim is only within periodic simple cycles; smaller **noncycle** graphs can lose entrywise positivity under the same rational method. The full positivity interval is classified exactly only for the first failing case \(n=6\), not for every larger cycle.

## Proof

### 1. Exact positivity certificates for cycles of sizes three through five
All denominators below are positive for \(h\ge0\). The rational propagator is circulant and symmetric, so its entries depend only on cyclic graph distance \(d\). Write \(t_{n,d}(h)=[T_n(h)]_{0,d}\), using \(0\le d\le\lfloor n/2\rfloor\).

For \(n=3\), with \(D_3=3h^2+6h+4\),
\[
t_{3,0}=\frac{3h^2-2h+4}{D_3},\qquad
t_{3,1}=\frac{4h}{D_3}.
\]
The quadratic \(3h^2-2h+4\) is strictly positive because its discriminant is negative.

For \(n=4\), put \(D_4=(h^2+3h+3)(4h^2+6h+3)\). Then
\[
\begin{aligned}
t_{4,0}&=\frac{4h^4+3h^3+6h^2+9h+9}{D_4},\\
t_{4,1}&=\frac{3h}{4h^2+6h+3},\\
t_{4,2}&=\frac{9h^2(h+1)}{D_4}.
\end{aligned}
\]
Every displayed numerator is strictly positive for \(h>0\).

For \(n=5\), let \(D_5=25h^4+150h^3+360h^2+360h+144\). One finds
\[
\begin{aligned}
t_{5,0}&=\frac{25h^4+30h^3+72h^2+72h+144}{D_5},\\
t_{5,1}&=\frac{72h(h+2)}{D_5},\\
t_{5,2}&=\frac{12h^2(5h+6)}{D_5}.
\end{aligned}
\]
These entries are strictly positive for every \(h>0\). This proves unconditional positivity up through the five-cycle.

All these identities can be verified by multiplying the claimed rational matrix by
\[
12I-6hQ_n+h^2Q_n^2
\]
and comparing coefficients with \(12I+6hQ_n+h^2Q_n^2\). The supplied standalone checker performs the comparisons as exact identities in the polynomial ring \(\mathbb Q[h]\).

### 2. Sharp positivity interval for the six-cycle
The common denominator is
\[
D_6=(h^2+6h+12)(3h^2+6h+4)(4h^2+6h+3).
\]
Exact matrix multiplication gives the four distinct cyclic-distance entries
\[
\begin{aligned}
t_{6,0}&=\frac{12h^6+44h^5+121h^4+168h^3+276h^2+288h+144}{D_6},\\
t_{6,1}&=\frac{-2h(5h^4-12h^3-102h^2-144h-72)}{D_6},\\
t_{6,2}&=\frac{2h^2(13h^3+48h^2+72h+36)}{D_6},\\
t_{6,3}&=\frac{2h^3(19h^2+48h+24)}{D_6}.
\end{aligned}
\]
Each factor in \(D_6\) is strictly positive on \(h\ge0\), and the numerators for cyclic distances \(0,2,3\) are strictly positive for \(h>0\). Thus the sign of the entire matrix depends only on \(t_{6,1}\).

The coefficient sequence of
\[
F_6(h)=5h^4-12h^3-102h^2-144h-72
\]
has exactly one sign change, so Descartes' rule gives at most one positive real root. Since \(F_6(0)<0\) and \(F_6(h)\to+\infty\), it has exactly one. Also \(F_6(6)<0<F_6(7)\), locating that root within \((6,7)\). Therefore nearest-neighbor entries are positive for \(0<h<h_6\), zero at \(h=h_6\), and strictly negative for every \(h>h_6\). Substituting \(h=7\) gives the stated exact negative entry.

### 3. Every larger cycle eventually violates Markov positivity
Put \(L_n=-Q_n\). It is the positive semidefinite cycle Laplacian, with kernel \(\operatorname{span}\{\mathbf1\}\). For a positive nonzero eigenvalue \(\lambda\),
\[
R(-h\lambda)
=\frac{h^2\lambda^2-6h\lambda+12}{h^2\lambda^2+6h\lambda+12}
=1-\frac{12}{h\lambda}+O(h^{-2})
\]
as \(h\to\infty\). Since each fixed finite cycle has a finite nonzero spectrum, functional calculus gives
\[
T_n(h)=I-\frac{12}{h}L_n^++O_n(h^{-2}),
\]
where \(L_n^+\) is the Moore–Penrose pseudoinverse. The remainder is in operator norm, hence also entrywise.

A direct discrete Green-function calculation gives
\[
(L_n^+)_{0,d}=g_d:=\frac{n^2-1}{12n}-\frac{d(n-d)}{2n},\qquad0\le d\le n-1.
\]
To check this identity without invoking any external formula, first sum over \(d\) to obtain \(\sum_{d=0}^{n-1}g_d=0\). The cyclic second-difference identity gives
\[
2g_d-g_{d-1}-g_{d+1}=\mathbf1_{\{d=0\}}-\frac1n,
\]
with indices modulo \(n\). Thus the circulant matrix formed by \(g_d\) satisfies
\[
L_nG=I-\frac1n\mathbf1\mathbf1^{\mathsf T},\qquad G\mathbf1=0,
\]
which uniquely identifies \(G=L_n^+\).

At cyclic distance one,
\[
g_1=\frac{(n-1)(n-5)}{12n}.
\]
Consequently,
\[
[T_n(h)]_{0,1}
=-\frac{12g_1}{h}+O_n(h^{-2})
=-\frac{(n-1)(n-5)}{nh}+O_n(h^{-2}).
\]
This is strictly negative for all sufficiently large \(h\) whenever \(n\ge6\). Together with the exact small-size formulas, this establishes the all-size dichotomy.

### 4. Stability survives the positivity failure
Every eigenvalue of \(Q_n\) is \(-\lambda\) with \(\lambda\ge0\). For \(t>0\),
\[
R(-t)=\frac{(t-3)^2+3}{t^2+6t+12}\in(0,1),
\]
while \(R(0)=1\). Therefore \(T_n(h)\) is symmetric positive definite, has spectral norm one, and contracts strictly on the orthogonal complement of constants at every \(h>0\). Since \(Q_n\mathbf1=0\), it also has exactly unit row sums. This establishes that the negative transition weights are genuinely a *positivity failure* rather than a loss of mass conservation or spectral stability.

## Verification
Run `python verify.py` using Python's standard library. The checker reconstructs each cycle generator for sizes \(n=3,4,5,6\); represents the displayed numerators and denominators as rational-coefficient polynomials; verifies the full matrix identity
\[
(12I-6hQ_n+h^2Q_n^2)N_n(h)
=D_n(h)(12I+6hQ_n+h^2Q_n^2)
\]
coefficient by coefficient; and checks each row-sum polynomial identity. It also checks the exact negative entry at \(h=7\), the elementary location of the threshold in \((6,7)\), and rational instances of the cyclic Green-function identity.

The argument for all \(n\ge6\) is analytical; the finite rational Green-function tests are only corroborative. The polynomial checks are exact identities, not numerical sampling or incomplete parameter enumeration.

## Relationship to prior work
The possibility that diagonal Padé methods preserve spectral stability while violating positive-system invariance is established in Zappavigna, Colaneri, Kirkland, and Shorten (2010, 2012). Their methods provide general sufficient conditions and examples of positivity failure, but do not state the periodic-cycle size dichotomy or the sharp six-cycle boundary here.

The absolute-monotonicity theory of Lóczi and Ketcheson (2013) provides universal Runge–Kutta positivity context; the primary MSC classification \(65L06\) is explicit in the first public version. Generic positivity-radius obstructions for fourth-order Gauss methods do not determine exactly which finite periodic Markov systems remain nonnegative for every step.

A published result on the fourth-order Padé Markov map exhibits an eight-state pure-birth chain with loss of positivity at *arbitrarily small* steps and proves that eight states are minimal for that different effect. Here the cycle generator is symmetric and diffusion-like, all small steps are nonnegative, and the obstruction is instead *large-step* nearest-neighbor negativity. Another published result makes a different filtered Crank–Nicolson propagator unconditionally positive on periodic heat lattices; that rational map is not the two-stage Gauss propagator studied here.

The all-size cycle theorem adds a structural reason for the threshold: the sign of the nearest-neighbor entry in the cycle Laplacian Green kernel changes at six vertices. The exact first-failure cutoff is then determined by a single quartic.

## Limitations
The theorem is for uniform one-dimensional *periodic* cycles with unit or common positive edge rates. Nonuniform cycles, open paths, arbitrary reversible chains, and higher-dimensional lattices are not covered by the size dichotomy.

For cycles with \(n\ge7\), only eventual large-step positivity failure is proved; the exact entire set of positivity-preserving steps is not classified here. The quantitative \(O_n(h^{-2})\) remainder is a fixed-\(n\) asymptotic, not a bound uniform in mesh size.

The statement concerns end-step entrywise nonnegativity in exact arithmetic, not stage positivity, error magnitude, numerical rounding, or a general optimal time-step choice.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland, and R. Shorten, “On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems,” MTNS 2010. Public repository version deposited 2010-10-15. https://mural.maynoothuniversity.ie/id/eprint/2195/
2. A. Zappavigna, P. Colaneri, S. Kirkland, and R. Shorten, “Essentially Negative News About Positive Systems,” *Linear Algebra and its Applications* 436 (2012), 3425–3442, DOI 10.1016/j.laa.2011.12.021. https://mural.maynoothuniversity.ie/id/eprint/3761/
3. L. Lóczi and D. I. Ketcheson, “Rational functions with maximal radius of absolute monotonicity,” arXiv:1303.6651v1, submitted 2013-03-26. https://arxiv.org/abs/1303.6651
4. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab
5. “Unconditional lattice positivity from backward-Euler-filtered Crank-Nicolson,” public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-backward-euler-filtered-cn-lattice-positivity--1f6f56bd0eac
