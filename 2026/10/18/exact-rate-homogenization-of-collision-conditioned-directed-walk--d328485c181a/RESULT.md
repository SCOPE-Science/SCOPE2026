# Exact rate homogenization of collision-conditioned directed walkers on a ring

## Finding
For a fixed directed cycle, **conditioning labeled particles of unequal jump rates to survive forever without collision exactly removes the rate ratios from their dynamics**. The resulting Markov generator coincides with that of equal-rate walkers conditioned on noncollision, with common rate equal to the geometric mean of the original rates. The collision exponent, quasi-stationary law, and the weak-rate-disorder crossover remain explicitly computable.

Write \(c=(\prod_{i=1}^k a_i)^{1/k}\), \(s_{n,k}=\sin(k\pi/n)/\sin(\pi/n)\). The principal killing exponent is
\[
\lambda_a=\sum_{i=1}^k a_i-cs_{n,k}.
\]
The perpetual-survival conditioned process has stationary distribution proportional to the square of the cyclic Vandermonde \(h_0\), regardless of heterogeneity, while its quasi-stationary distribution depends on the rates through a positive diagonal gauge.

## Assumptions and scope
Fix integers \(n\ge3\), \(2\le k<n\), positive constants \(a_1,\ldots,a_k\), and a collision-free initial configuration of labeled particles on \(\mathbb Z/n\mathbb Z\). Particle \(i\) performs independent clockwise rate-\(a_i\) exponential jumps. The process is killed at its first attempted jump onto another particle. All formulas below refer to the communicating component \(\mathcal C\) having the initial cyclic order of labels. Distinct components are treated separately; no labeling equivalence or mixing between components is presumed.

Choose a cyclic ordering \(\sigma(1),\ldots,\sigma(k)\) of the labels associated with \(\mathcal C\). At state \(x\), choose the unique integer lifts with \(0\le y_{\sigma(1)}<n\) and
\[
y_{\sigma(1)}<\cdots<y_{\sigma(k)}<y_{\sigma(1)}+n,
\qquad y_i\equiv x_i\pmod n.
\]
Define
\[
D(x)=\prod_{i=1}^k(c/a_i)^{y_i},\qquad
h_0(x)=\prod_{1\le i<j\le k}|e^{2\pi\mathrm i x_j/n}-e^{2\pi\mathrm i x_i/n}|.
\]
Both are strictly positive on \(\mathcal C\). Adding \(n\) to every lift leaves \(D\) unchanged because \(\prod_i(c/a_i)=1\). Let \(Q_a\) denote the subgenerator on \(\mathcal C\) with diagonal \(-\sum_i a_i\) and off-diagonal \(a_i\) for a legal clockwise particle-\(i\) jump. The homogeneous \(Q_c\) is defined analogously using rate \(c\) for every particle.

## Proof
**Step 1: the exact gauge.** When particle \(i\) makes a legal clockwise jump \(x\to x^{i,+}\), the lifts can be chosen to change only \(y_i\to y_i+1\), up to a simultaneous shift by an integer multiple of \(n\). Consequently,
\[
\frac{D(x^{i,+})}{D(x)}=\frac c{a_i}.
\]
It follows entry by entry, including the killed diagonals, that
\[
\boxed{Q_a=D Q_c D^{-1}-(\sum_i a_i-kc)I.}\tag{1}
\]
This equality holds without an approximation, for every finite \(n\) and positive rate profile.

**Step 2: a self-contained cyclic Vandermonde eigenidentity.** Set \(\zeta=e^{2\pi\mathrm i/n}\), choose the ordered lifts from above, and define \(A(y)=\det(\zeta^{(j-1)y_i})_{1\le i,j\le k}\). The determinant expansion shows that the sum of \(A\) after increasing each individual \(y_i\) by one is
\[
\sum_i A(y+e_i)=(1+\zeta+\cdots+\zeta^{k-1})A(y).
\]
Any increment producing a collision contributes zero because two determinant rows then coincide. The Vandermonde factorization gives, up to a configuration-independent unit complex factor,
\[
A(y)=e^{\pi\mathrm i(k-1)\sum_i y_i/n}\prod_{i<j}2\sin\!\left(\frac{\pi(y_j-y_i)}n\right)
\]
when the lifts are in cyclic increasing order. The sine factors are strictly positive. Under a global shift of all lifts by \(n\), the compensating exponential changes by \((-1)^{k(k-1)}=1\); hence the positive function is well-defined on the ring. Multiplying the determinant identity by the inverse exponential phase yields
\[
\sum_{i:\,x^{i,+}\in\mathcal C}h_0(x^{i,+})
=\frac{\sin(k\pi/n)}{\sin(\pi/n)}h_0(x)=s_{n,k}h_0(x).
\]
(The constant \(2\) factors cancel.) Thus \(Q_ch_0=-c(k-s_{n,k})h_0\). Reversing clockwise and counterclockwise shifts, or conjugating the determinant identity, gives \(h_0^{\mathsf T}Q_c=-c(k-s_{n,k})h_0^{\mathsf T}\).

**Step 3: principal eigenfunctions and tails.** The finite killed chain is irreducible within every cyclic-order component: gap surplus can be successively transported around the directed cycle, and a surviving moving vacancy permits shifts of the absolute position. Perron–Frobenius theory for the irreducible sub-Markov semigroup therefore identifies the strictly positive right/left eigenfunctions as its principal pair. Combining Step 2 with (1) gives
\[
h_a=Dh_0,\qquad \ell_a=h_0/D,\qquad
\lambda_a=\sum_i a_i-cs_{n,k}.
\]
Furthermore \(\langle\ell_a,h_a\rangle=\sum_{y\in\mathcal C}h_0(y)^2\). Spectral projection of \(e^{tQ_a}\) onto its simple Perron mode implies for each initial state \(x\in\mathcal C\)
\[
\mathbb P_x(\tau>t)\sim
\frac{D(x)h_0(x)\sum_{y\in\mathcal C}h_0(y)/D(y)}{\sum_{y\in\mathcal C}h_0(y)^2}
\,e^{-\lambda_a t}\quad(t\to\infty).
\]
In particular the quasi-stationary conditional law at large surviving times is \(\nu_a(x)\propto h_0(x)/D(x)\).

**Step 4: complete dynamics after conditioning.** The Doob transform with \(h_a\) has off-diagonal rate
\[
Q_a(x,x^{i,+})\frac{h_a(x^{i,+})}{h_a(x)}
=a_i\frac{D(x^{i,+})}{D(x)}\frac{h_0(x^{i,+})}{h_0(x)}
=c\frac{h_0(x^{i,+})}{h_0(x)}.
\]
Its diagonal is determined by row sums. Hence \(Q_a^{h_a}=Q_c^{h_0}\) as generators, not merely in distribution at a single time. Its unique stationary probability is \(\pi(x)=h_0(x)^2/\sum_{y\in\mathcal C}h_0(y)^2\), because the left/right eigenfunctions of the homogeneous killed chain both equal \(h_0\).

**Step 5: sharp rate penalty and crossover.** Since \(c\) is the geometric mean, arithmetic-geometric mean gives \(\lambda_a-\lambda_c=\sum_i a_i-kc\ge0\), with equality only if all rates coincide. For fixed \(k\), expand \(\sin(k\pi/n)/\sin(\pi/n)=k-k(k^2-1)\pi^2/(6n^2)+O(n^{-4})\). With \(a_{i,n}=a\exp(u_i/n)\) and \(\bar u=k^{-1}\sum_i u_i\), expansion of exponentials yields
\[
\lim_{n\to\infty}n^2\lambda_{a,n}
=a\left(\frac12\sum_i(u_i-\bar u)^2+\frac{\pi^2k(k^2-1)}6\right).
\]
This identifies the exact competition between finite-ring survival costs and heterogeneous speed variance in a natural \(n^{-1}\) rate-disorder window.

## Verification
Run `python verify.py` with Python 3 and NumPy. The program enumerates complete cyclic-order state spaces for \(n=3,\ldots,8\), \(2\le k\le\min(4,n-1)\), and three rate profiles. It checks, state by state and transition by transition, both eigenvectors, the eigenvalue, and equality of every Doob jump rate, and also tests the explicit two-particle quasi-stationary and stationary formulas. These finite calculations validate normalizations and boundary conventions but **do not prove** the all-\(n\), all-\(k\) theorem; the general proof is the determinant/gauge argument above.

For \(k=2\), the gap \(d\in\{1,\ldots,n-1\}\) is a birth-death process killed at the endpoints; its right eigenfunction is \((a_1/a_2)^{d/2}\sin(\pi d/n)\) and its eigenvalue is \(a_1+a_2-2\sqrt{a_1a_2}\cos(\pi/n)\). This independently checks the gauge direction and the ring-boundary orientation.

## Relationship to prior work
Shiatis, *Exclusion vs Noncolliding Dynamics in Markov Processes* (arXiv:2610.00741v1, first posted 2026-09-30), studies noncollision/exclusion changes of measure for \(k\) copies of a **common** Markov process and explicitly recalls the unit-rate ring eigenfunction. Johnston, *Continuous Kasteleyn theory for the bead model* (arXiv:2207.13538; JEMS 2025), gives the homogeneous clockwise-ring noncolliding construction. Both supply background, but neither of the inspected formulations supplies the heterogeneous particle-specific diagonal similarity, its exact arithmetic-geometric survival penalty, or the resulting rate-homogenized conditional process. Bisi–Liao–Saenz–Zygouras, *Non-intersecting Path Constructions for TASEP with Inhomogeneous Rates and the KPZ Fixed Point* (2023), studies **discrete-time exclusion** with particle/time-dependent parameters, nonintersecting path representations, and Fredholm determinants rather than perpetual noncollision conditioning of independent particle-specific Poisson clocks on a finite ring. The established homogeneous sine Vandermonde and standard Perron–Frobenius/Doob machinery are not claimed as new.

## Limitations
The conclusion applies to finite directed rings, strictly clockwise independent Poisson walkers, **positive time-homogeneous particle rates**, fixed cyclic-label-order classes, and eternal noncollision conditioning. It does not assert finite-horizon conditional process equality, universality of quasi-stationary laws, bidirectional jumps, spatially dependent rates, or a corresponding infinite-volume stationary law. The originality comparison is best-knowledge and not an independent priority certification; an unindexed general gauge-transform treatment could imply the result.

## References
1. R. Shiatis, *Exclusion vs Noncolliding Dynamics in Markov Processes*, arXiv:2610.00741v1 (2026), https://arxiv.org/abs/2610.00741 .
2. S. G. G. Johnston, *Continuous Kasteleyn theory for the bead model*, *Journal of the European Mathematical Society* (2025), DOI: 10.4171/JEMS/1728; https://arxiv.org/abs/2207.13538 .
3. E. Bisi, Y. Liao, A. Saenz, N. Zygouras, *Non-intersecting Path Constructions for TASEP with Inhomogeneous Rates and the KPZ Fixed Point*, *Communications in Mathematical Physics* 402 (2023), 285–333, DOI: 10.1007/s00220-023-04723-8.
4. S. G. G. Johnston and R. Shiatis, *The Integrable Snake Model*, arXiv:2501.15483 (2025), https://arxiv.org/abs/2501.15483 .
