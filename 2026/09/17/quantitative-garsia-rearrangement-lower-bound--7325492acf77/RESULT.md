# An explicit iterated-log lower bound for the finite Garsia rearrangement constant

## Statement

For an \(N\)-term orthonormal system
\[
\Phi=(\phi_1,\ldots,\phi_N)
\]
on a probability space, with \(|\phi_j|\le 1\), and a permutation
\(\tau\in S_N\), write
\[
M_{\Phi,\tau}a(x)
=
\max_{1\le q\le N}
\left|
\sum_{j=1}^q a_{\tau(j)}\phi_{\tau(j)}(x)
\right|.
\]
Define the finite Garsia rearrangement constant
\[
G(N)
=
\sup_{\Phi}
\inf_{\tau\in S_N}
\|M_{\Phi,\tau}\|_{\ell^2_N\to L^2}.
\]

Let
\[
\log_{(1)}x=\log x,\qquad
\log_{(j+1)}x=\log(\log_{(j)}x).
\]
Then there are absolute constants \(c>0\) and \(N_0\) such that
\[
\boxed{
G(N)\ge c\,\log_{(6)}N
}
\qquad (N\ge N_0).
\]

Thus the qualitative divergence of the optimal universal constant, proved by
Lewko in 2026, admits an explicit quantitative lower rate. Bourgain's upper
bound gives \(G(N)\lesssim\log\log N\), so a large gap remains.

## Context

Lewko proved that \(G(N)\to\infty\) by constructing finite systems from two
copies of the trigonometric system. His paper explicitly notes that the proof
as written gives no useful dependence of the required dimension \(N\) on the
target maximal-operator size \(H\), because it invokes qualitative Fourier
divergence and Szemeredi's theorem, and states that the true growth rate is
unknown.

Two quantitative ingredients make an explicit rate available:

1. Karagulyan proved that for every \(m>1\) there is a permutation
   \(\pi\in S_m\) for which the rearranged trigonometric maximal operator has
   \(L^2\)-operator norm comparable to \(\log m\).
2. Gowers gave an explicit quantitative form of Szemeredi's theorem. One
   convenient consequence is
   \[
   \frac{r_m(N)}{N}
   \le
   (\log\log N)^{-2^{-2^{m+9}}},
   \]
   in the range where the right side is meaningful, where \(r_m(N)\) is the
   largest cardinality of an \(m\)-term-arithmetic-progression-free subset of
   \([N]\).

The proof below inserts these quantitative inputs into Lewko's finite
two-copy combinatorial construction.

## 1. Quantifying the permutation-embedding lemma

Fix \(m\ge2\) and a prescribed permutation \(\pi\in S_m\). Put
\[
K=m^2,\qquad
B=\binom{K}{m},\qquad
\eta_m=(2m)^{-10m}.
\]

Lewko's coloring argument considers the family \(\mathcal F_N\) of
\(K\)-colorings of \([N]\) which fail to contain an \(m\)-term arithmetic
progression whose colors are distinct and occur in the prescribed order
\(\pi\). His deletion expansion gives the following explicit consequence.

If
\[
r_m(N)\le \eta_m N,
\]
then every nonzero intersection term in the expansion has a support \(S\)
satisfying
\[
|S|\le \theta_m N,\qquad
\theta_m:=B\eta_m,
\]
and hence
\[
|\mathcal F_N|
\le
(m-1)^N
\sum_{0\le j\le \theta_m N}
\binom Nj
\left(\frac{B}{m-1}\right)^j.
\tag{1}
\]

Indeed, for each fixed \(m\)-element color set \(Q\), the points at which the
deletion expansion chooses the intersection indexed by \(Q\) form an
\(m\)-term-progression-free set. There are \(B\) possible sets \(Q\).

Since
\[
B\le (em)^m,
\]
our choice of \(\eta_m\) gives
\[
\theta_m\le
\left(\frac{e}{2^{10}m^9}\right)^m.
\]
Consequently the logarithm of the sum in (1) is
\[
o(N/m)
\tag{2}
\]
uniformly for sufficiently large \(m\). This follows directly from the
standard entropy estimate
\[
\sum_{j\le\theta N}\binom Nj A^j
\le
\exp\!\left(
N\theta\log\frac{eA}{\theta}+o(N\theta)
\right)
\]
when \(\theta\to0\).

Now assume \(K\mid N\). The number \(\mathcal B_N\) of balanced
\(K\)-colorings satisfies
\[
|\mathcal B_N|
=
\frac{N!}{((N/K)!)^K}
\ge
\frac{K^N}{(N+1)^K}.
\tag{3}
\]
For a uniformly random \(\sigma\in S_N\), Lewko's averaging argument bounds
the expected number of balanced colorings exceptional both before and after
composition with \(\sigma^{-1}\) by
\[
\frac{|\mathcal F_N|^2}{|\mathcal B_N|}.
\]
Using (1)--(3),
\[
\log\frac{|\mathcal F_N|^2}{|\mathcal B_N|}
\le
N\!\left(2\log(m-1)-2\log m\right)
+o(N/m)+m^2\log(N+1).
\tag{4}
\]
The main term in (4) is
\[
-2N\log\frac{m}{m-1}\sim-\frac{2N}{m}.
\]
Thus, once \(N\) is sufficiently large relative to \(m\), (4) is negative.
Therefore there is a permutation \(\sigma\in S_N\) such that every
\(\tau\in S_N\) contains the prescribed order \(\pi\) on an \(m\)-term
arithmetic progression in at least one of the two frequency orders
\[
\tau,\qquad \sigma\circ\tau.
\tag{5}
\]

This is Lewko's permutation-embedding lemma with an explicit sufficient size
condition.

## 2. A five-fold exponential size bound

Gowers' quantitative Szemeredi theorem implies that
\[
r_m(N)\le \eta N
\]
whenever, for example,
\[
N\ge
2^{\,2^{\,\eta^{-\,2^{\,2^{m+9}}}}}.
\tag{6}
\]
Insert \(\eta=\eta_m=(2m)^{-10m}\). If
\[
E_1(t)=e^t,\qquad E_{j+1}(t)=\exp(E_j(t)),
\]
then (6) is bounded above by
\[
E_5(Cm)
\tag{7}
\]
for an absolute \(C\) and all sufficiently large \(m\). The divisibility
condition \(m^2\mid N\), as well as the elementary largeness requirement
needed in (4), can be imposed without changing the five-fold exponential
form.

Hence for every sufficiently large \(m\) and every prescribed
\(\pi\in S_m\), one may choose
\[
N_m\le E_5(Cm)
\tag{8}
\]
and \(\sigma\in S_{N_m}\) satisfying (5).

## 3. Transferring Karagulyan's logarithmic obstruction

Karagulyan's theorem supplies, for each \(m\), a permutation \(\pi\in S_m\)
and coefficients \(b_1,\ldots,b_m\) with
\[
\sum_{j=1}^m|b_j|^2=1
\]
such that
\[
\left\|
\max_{q\le m}
\left|
\sum_{j\le q}b_j e(\pi(j)x)
\right|
\right\|_{L^2(\mathbb T)}
\ge c_0\log m
\tag{9}
\]
for an absolute \(c_0>0\). Here \(e(t)=e^{2\pi i t}\).
If one starts from the operator formulation of Karagulyan's theorem, project
the maximizing input onto the span of the first \(m\) characters; this
preserves the relevant Fourier coefficients and cannot increase its
\(L^2\)-norm.

Apply the quantified embedding above to this \(\pi\), and form Lewko's
two-copy system on \(\mathbb T\times\{0,1\}\):
\[
\phi_n(x,0)=e(nx),\qquad
\phi_n(x,1)=e(\sigma(n)x),
\qquad n\in[N_m],
\]
where each copy has measure \(1/2\). This is an orthonormal system and
\(|\phi_n|=1\).

Fix any permutation \(\tau\) of the functions. By (5), on one of the two
copies there is an arithmetic progression
\[
x_j=a+dj,\qquad 1\le j\le m,
\]
whose frequencies appear in the order
\[
x_{\pi(1)},\ldots,x_{\pi(m)}
\]
as a subsequence. Give those functions the coefficients \(b_j\), in this
order, and give every intervening function coefficient zero. On that copy
the corresponding maximal partial sum has the same distribution as (9),
because
\[
e((a+d\pi(j))x)=e(ax)e(\pi(j)dx)
\]
and \(x\mapsto dx\) preserves Haar measure. Therefore
\[
\|M_{\Phi,\tau}\|_{\ell^2\to L^2}
\ge
\frac{c_0}{\sqrt2}\log m
\]
for every \(\tau\), and hence
\[
G(N_m)\gtrsim\log m.
\tag{10}
\]

The construction can be padded to every larger size by extending
\(\sigma\) to fix the additional frequencies. With zero coefficients on
the added functions, any full permutation restricts to a permutation of
the original subsystem. Thus (10) remains valid for all \(N\ge N_m\).

Choose \(m\) proportional to \(\log_{(5)}N\), with a sufficiently small
absolute proportionality constant so that (8) gives \(N_m\le N\). Then
\[
\log m
=
\log_{(6)}N+O(1),
\]
which proves
\[
G(N)\gtrsim\log_{(6)}N.
\]

## Limitations and scope

- The bound is asymptotic and its numerical threshold is enormous. It is a
  quantitative existence result, not a practical estimate at moderate \(N\).
- The six-fold iterated logarithm is not expected to be sharp. It records
  the explicit dependence obtained by combining the stated quantitative
  ingredients.
- The result is for the complex unit-modulus finite systems in the definition
  above. No quantitative claim for the real-valued variant is made here.
- The lower bound remains very far from Bourgain's
  \(O(\log\log N)\) upper bound.
- Any improvement in the dependence on progression length and density in the
  relevant quantitative Szemeredi input can potentially improve the
  iterated-log rate.

## Originality boundary

Lewko's September 2026 paper explicitly states that its proof gives no useful
bound on \(N\) as a function of \(H\) and that the true growth rate of the
optimal finite constant is unknown. Searches by the source theorem, the
Garsia/Kolmogorov terminology, quantitative rearrangement constants, and the
Karagulyan lower bound found no prior statement extracting an explicit
divergence rate by combining the two-copy construction with a quantitative
Szemeredi theorem.

The ingredients themselves are not claimed as new: Karagulyan's logarithmic
finite trigonometric lower bound, Lewko's two-copy embedding mechanism,
Gowers' quantitative Szemeredi estimate, and Bourgain's upper bound are all
prior work. The originality claim is limited to the quantitative synthesis
above, to the best of our knowledge. Because the motivating preprint is very
recent, contemporaneous or not-yet-indexed observations remain the main
priority risk.

## References

1. M. Lewko, *On Kolmogorov's rearrangement problem and Garsia's conjecture*,
   arXiv:2609.18491 (2026).
   https://arxiv.org/abs/2609.18491
2. G. A. Karagulyan, *On Weyl multipliers of the rearranged trigonometric
   system*, Sbornik Mathematics 211 (2020), 1704--1736.
   https://arxiv.org/abs/2004.01003
3. W. T. Gowers, *A new proof of Szemeredi's theorem*, Geometric and
   Functional Analysis 11 (2001), 465--588.
   https://doi.org/10.1007/s00039-001-0332-9
4. J. Bourgain, *On Kolmogorov's rearrangement problem for orthogonal systems
   and Garsia's conjecture*, in Geometric Aspects of Functional Analysis
   (1987--88), Lecture Notes in Mathematics 1376, Springer (1989), 209--250.
   https://doi.org/10.1007/BFb0090057
