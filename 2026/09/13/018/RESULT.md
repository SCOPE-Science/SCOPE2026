# Refined L6 Decoupling on Sparse Unions for the 3+1 Cone Is False Without Amplitude Uniformity

## Context

Refined decoupling and refined Strichartz estimates improve classical
decoupling bounds by a sparsity factor such as $(M/W)^{\alpha}$ when the
function concentrates on a sparse union $Y$ of $M$ small balls out of $W$
possible locations. Since the work of Guth–Iosevich–Ou–Wang and subsequent
refined decoupling literature, the standard correct statements include a
crucial hypothesis: the contributing wave packets have comparable amplitudes
(up to dyadic pigeonholing, with at most logarithmic loss), or the estimate
sums over dyadic amplitude classes. The admitted target asks whether the
naive hypothesis-free form holds for the truncated light cone in
$\mathbb{R}^{3+1}$ at the $L^{6}$ exponent.

## Definitions

Let $\Gamma$ be the truncated light cone in $\mathbb{R}^{3+1}$, $E$ its
extension operator, $\theta$ the canonical $R^{-1/2}$-caps, and $B_{R}$ the
radius-$R$ ball, $R\ge 2$. Write $Ef=\sum_{\theta}Ef_{\theta}$ where each
$Ef_{\theta}$ is a sum of essentially disjoint tube wave packets $T$ of size
approximately $R^{1/2}\times R^{1/2}\times R^{1/2}\times R$ pointing in the
cap normal direction. Let $Y$ be any union of $M$ disjoint $R^{1/2}$-balls
in $B_{R}$, let $W$ be the total number of such balls meeting the
wave-packet support, and let $\mu\ge 1$ bound the mean wave-packet
multiplicity per ball of $Y$. Let $w_{B_{R}}$ be the standard rapidly
decaying weight adapted to $B_{R}$.

## Result

The claimed uniform bound

$$
\|Ef\|_{L^{6}(Y)}
\le C_{\epsilon}R^{\epsilon}(M/W)^{1/6}
\Bigl(\sum_{\theta}\|Ef_{\theta}\|_{L^{6}(w_{B_{R}})}^{2}\Bigr)^{1/2}
\qquad\text{for all }f,\ Y,\ R\ge 2
$$

with only $\mu\ge 1$ on $Y$ is FALSE. There exists an explicit single-cap
family $(f_{R},Y_{R})$ with $\mu=1$ such that

$$
\frac{\|Ef_{R}\|_{L^{6}(Y_{R})}}
{(M_{R}/W_{R})^{1/6}\|Ef_{R}\|_{L^{6}(w_{B_{R}})}}
\ge c\,R^{1/4}(1-o(1)),
$$

so

$$
\limsup_{R\to\infty}
R^{-\epsilon}\frac{\|Ef_{R}\|_{L^{6}(Y_{R})}}
{(M_{R}/W_{R})^{1/6}\|Ef_{R}\|_{L^{6}(w)}}
=+\infty
\quad\text{for every }\epsilon<1/4.
$$

Parameters: $N\sim R^{3/2}$ parallel disjoint tubes, $L\sim R^{1/2}$ balls
per tube, $M=L$, $W=NL\sim R^{2}$, $W/M\sim R^{3/2}$, $\mu=1$. No finite
$C_{\epsilon}$ can repair the stated power for fixed $\epsilon<1/4$; in
particular the estimate fails for the conventional arbitrary-$\epsilon$
reading and for any fixed $\epsilon_{0}$ such as $1/8$.

## Proof / Evidence

It suffices to falsify the single-cap case, since one-cap data are
admissible $f$. Then the right side collapses to
$C_{\epsilon}R^{\epsilon}(M/W)^{1/6}\|F\|_{L^{6}(w)}$ with $F=Ef$.

Fix one cap $\theta_{0}$. Its packets are parallel essentially disjoint
tubes $T_{1},\dots,T_{N}$ with $N\sim R^{3/2}$ (transverse lattice
$(R/R^{1/2})^{3}$). Tile $B_{R}$ by essentially disjoint $R^{1/2}$-balls;
each interior tube meets $\sim L:=cR^{1/2}$ balls $S(T_{j})$, uniformly in
$j$ up to constants; discard boundary tubes. Let $b>0$ be the per-ball
$L^{6}$ mass unit and $\phi_{T_{j}}$ Schwartz tube packets with
$\sum_{q\in S(T_{j})}\|\phi_{T_{j}}\|_{L^{6}(q)}^{6}\sim Lb$ and rapidly
decaying tails summable to a small fraction of $b$ per ball.

Define with $\delta:=(N-1)^{-1/6}$

$$
F:=\phi_{T_{0}}+\delta\sum_{j=1}^{N-1}\phi_{T_{j}}.
$$

By disjoint-support $L^{6}_{6}$ additivity up to $1+o(1)$ Schwartz factors:

$$
\|F\|_{L^{6}(q)}^{6}\sim b\ \ (q\in S(T_{0})),\qquad
\|F\|_{L^{6}(q)}^{6}\sim\delta^{6}b\ \ (q\in S(T_{j}),j\ge 1).
$$

Set $Y$ to be the $L$ balls of $S(T_{0})$. Then $M=L$; every tube carries
nonzero polynomial-amplitude mass ($\delta\sim R^{-1/4}$), so $W=NL$ under
the stated support definition; only $T_{0}$ meets $Y$ so $\mu=1$. Moreover

$$
\|F\|_{L^{6}(Y)}^{6}\sim Lb\sim Mb,\qquad
\|F\|_{L^{6}(w)}^{6}\sim Lb\,[1+(N-1)\delta^{6}]=2Lb,
$$

by $\delta^{6}=1/(N-1)$. Hence the claimed right side to the sixth power
is $(M/W)\cdot 2Lb=(1/N)2Lb$, and the ratio is exactly

$$
\bigl[\|F\|_{L^{6}(Y)}^{6}/((M/W)\|F\|_{L^{6}(w)}^{6})\bigr]^{1/6}
\sim (N/2)^{1/6}\sim cR^{1/4}.
$$

The tails jointly carry half the global $L^{6}_{6}$ mass, so no
thresholding notion of $W$ that discards half the mass is the stated $W$;
$\delta$ is polynomial, far above any Schwartz threshold. Dyadic
pigeonholing does not close the gap: the mass is split across two dyadic
classes each carrying half the mass, and restricting to either class
changes the denominator by only $2^{1/6}$ while the gap is $R^{1/4}$. The
$\mu\ge 1$ hypothesis is satisfied vacuously. The equal-amplitude
specialization gives ratio $\sim 1$, confirming sharpness of the diagnosis:
amplitude non-uniformity invisible to $(M,W,\mu\text{-on-}Y)$ is the exact
failure mechanism. Realization as $Ef$ uses the standard cap wave-packet
expansion with coefficients $1$ on $T_{0}$ and $\delta$ elsewhere, up to
absolute-constant tails.

Closed-form verification in `artifacts/scaling_check.py` confirms
ratio $=(N/2)^{1/6}$, log-log slope $0.2500$, and monotone growth of
ratio$/R^{1/8}$ from $1.26$ at $R=16$ past $5.04$ at $R=2^{20}$.

## Limitations

Absolute-constant errors (Schwartz tails, boundary tubes, disjoint-thinning
fractions, $w_{B_{R}}$ versus indicator) are absorbed by the unbounded
$R^{1/4}$ power and stated as $1+o(1)$ or absolute constants rather than
fully written kernel bounds. The passage from the discrete tube model to a
literal $Ef_{R}$ relies on standard cone wave-packet calculus. No broader
repair (correct uniform-amplitude or amplitude-spread form) is proved here;
the target asked to decide the stated bound, and the decision is that it
does not hold.

## Reproducibility

Run `python3 artifacts/scaling_check.py` from the record root; it prints
the $(R,N,L,\text{ratio},R^{1/4},\text{ratio}/R^{1/8})$ table, checks the
closed form against $(N/2)^{1/6}$ to $10^{-9}$, fits the log-log slope, and
writes `artifacts/scaling_check_results.json`.

## References

- C. Demeter, On the refined Strichartz estimates, arXiv:2002.09525 (2020):
  positive linear/multilinear refined Strichartz via refined decoupling.
- X. Du, Y. Ou, H. Wang, R. Zhang, On a free Schroedinger solution studied
  by Barcelo–Bennett–Carbery–Ruiz–Vilela, arXiv:2303.10563 (2023): sharp
  example for the true refined decoupling theorem.
- S. Singh, V. P. Singh Parmar, Repairing the refined-decoupling proof of
  the 5/4 planar pinned Falconer theorem, arXiv:2608.28711 (2026):
  distinct collar falsification of a planar Falconer arbitrary-packet form.
- L. Guth, A. Iosevich, Y. Ou, H. Wang type refined decoupling setup:
  background correct form requiring dyadic amplitude uniformity.
