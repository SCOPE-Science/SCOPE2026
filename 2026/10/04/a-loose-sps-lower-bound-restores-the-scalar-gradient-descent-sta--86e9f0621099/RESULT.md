# A loose SPS lower bound restores the scalar gradient-descent stability ceiling
## Finding
Consider the deterministic one-sample specialization of the stochastic Polyak stepsize (SPS) update on
\[
f(x)=\frac{{a}}{{2}}x^2,\qquad a>0,
\]
with a valid but strictly loose lower bound \(C=-c\), where \(c>0\), and a constant cap \(\alpha>0\). At any nonzero iterate,
\[
\tau(x)=\min\left\{\alpha,\frac{{f(x)-C}}{{|f'(x)|^2}}\right\}
=\min\left\{\alpha,\frac{{1}}{{2a}}+\frac{{c}}{{a^2x^2}}\right\},
\qquad x^+=x-\tau(x)ax.
\]
Set \(q=\alpha a\). Then all initial states converge to the minimizer if and only if \(0<q<2\).

More precisely, for \(0<q<2\), every nonzero trajectory enters the cap-active branch after finitely many iterations, that branch remains active thereafter, and the tail satisfies
\[
x_{{k+1}}=(1-q)x_k.
\]
For every \(q\ge2\), the points
\[
x_\star=\sqrt{\frac{{2c}}{{3a}}},\qquad -x_\star
\]
form an exact two-cycle. Along this cycle,
\[
f(x_\star)=\frac c3,
\qquad
\delta^{{\mathrm{{SPS}}}}=\frac{{4c}}{{3}}\left(1-\frac1q\right).
\]
Thus a strict lower-bound error can preserve a bounded SPS stability index while destroying pointwise convergence at exactly the ordinary scalar gradient-descent large-step threshold.

## Assumptions and scope
The result concerns the SPS update defined from the truncated model with a constant cap, specialized to one deterministic sample. The lower bound is valid because \(C=-c<0=\inf_x f(x)\). At \(x=0\), the gradient vanishes and the iteration is taken to remain at the minimizer; the displayed quotient is only used for \(x\ne0\).

The claim is a sharp classification for this scalar model, not a general lower bound for stochastic optimization and not a contradiction of the stability-index inequalities in the source. The source's stability index controls terms in convergence bounds; the present calculation separates that index from global pointwise dynamics under lower-bound misspecification.

## Proof
Introduce the dimensionless coordinate
\[
y=x\sqrt{\frac ac}.
\]
The proposal satisfies
\[
a\frac{{f(x)-C}}{{|f'(x)|^2}}=\frac12+\frac1{{y^2}},
\]
so for \(y\ne0\) the SPS map is
\[
F_q(y)=
\begin{{cases}}
(1-q)y,&q\le\frac12+\frac1{{y^2}},\\[4pt]
\frac y2-\frac1y,&q>\frac12+\frac1{{y^2}}.
\end{{cases}}
\]
At branch equality the two formulas agree.

Assume first \(0<q<2\). On the cap-active branch,
\[
|F_q(y)|=|1-q|\,|y|<|y|.
\]
Moreover, once this branch is active it remains active, because decreasing \(|y|\) increases \(\frac12+1/y^2\).

On the uncapped branch one necessarily has \(q>1/2\) and
\[
y^2>\frac1{{q-1/2}}>\frac23.
\]
For \(y^2>2/3\),
\[
\left|\frac y2-\frac1y\right|<|y|,
\]
because after squaring and clearing denominators this is equivalent to
\[
3y^4+4y^2-4>0,
\]
whose unique positive zero in \(y^2\) is \(2/3\). Hence every nonzero step strictly decreases \(|y|\).

It remains to show finite entry into the cap-active branch. If the uncapped branch remained active forever, then \(|y_k|\) would decrease to a limit \(r\ge0\). The uncapped condition gives
\[
r^2\ge\frac1{{q-1/2}}>\frac23,
\]
so \(r>0\). Continuity of the uncapped magnitude map and convergence of successive magnitudes would then force
\[
\left|\frac r2-\frac1r\right|=r,
\]
which is equivalent to \(r^2=2/3\), a contradiction. Thus the cap becomes active in finite time and thereafter the geometric recursion \(y_{{k+1}}=(1-q)y_k\) yields convergence to zero.

Now let \(q\ge2\) and choose \(y_\star=\sqrt{2/3}\). Its normalized Polyak proposal is
\[
\frac12+\frac1{{y_\star^2}}=2\le q.
\]
Hence the actual normalized step equals \(2\), regardless of whether equality occurs at \(q=2\) or the uncapped proposal is selected for \(q>2\), and
\[
F_q(y_\star)=-y_\star,\qquad F_q(-y_\star)=y_\star.
\]
Returning to \(x\) gives \(x_\star=\sqrt{2c/(3a)}\), proving failure of universal convergence for every \(q\ge2\).

Finally, on the cycle \(\tau=2/a\), \(\alpha=q/a\), and \(|f'(x_\star)|^2=2ac/3\). Substitution into the source stability-index formula
\[
\delta^{{\mathrm{{SPS}}}}=\tau\left(1-\frac{{\tau}}{{2\alpha}}\right)|f'(x)|^2
\]
gives
\[
\delta^{{\mathrm{{SPS}}}}=\frac{{4c}}{{3}}\left(1-\frac1q\right).
\]

## Verification
The proof is analytic. The accompanying `verify.py` independently replays the exact branch formulas numerically, checks the two-cycle at several cap values, checks the stability-index identity, and stress-tests convergence for representative \(q<2\). Its numerical tests are corroborative only; they are not used to prove the universal quantifiers.

## Relationship to prior work
Schaipp, Gower, and Taylor define SPS from a truncated model using any valid lower bound \(C_s\le\inf_z f(z,s)\), derive its stability index, and identify the expected lower-bound estimation error as one contributor to the SPS stability term. Their quadratic appendix treats exact lower bounds, while their misspecified-lower-bound discussion is qualitative rather than an exact dynamical classification.

Loizou et al. analyze SPS and capped SPS under exact component minima and show linear convergence in interpolation regimes. Their discussion also notes robustness issues under misspecification, but the inspected statements do not give the sharp scalar lower-bound-error threshold or the explicit cycle above. Schaipp, Gower, and Ulbrich motivate ProxSPS partly because lower bounds available for composite objectives can be loose; that observation is compatible with, but does not imply, the present exact threshold.

Targeted searches for equivalent SPS lower-bound-error cycles, scalar threshold \(q=2\), and the objective floor \(c/3\) found no statement implying this classification. This search evidence does not prove novelty; an older equivalent observation under different Polyak-step terminology remains a residual risk.

## Limitations
The result is one-dimensional and deterministic, although it is a legitimate one-sample specialization of SPS. It classifies the dynamics only for a quadratic with a constant cap and a constant strict lower-bound error. It does not establish analogous thresholds for heterogeneous sampling, varying caps, proximal variants, or other adaptive Polyak-type rules. It also does not say that the SPS stability index is incorrect; rather, it shows that boundedness of that index alone is not equivalent to pointwise convergence under a loose lower bound.

## References
1. F. Schaipp, R. M. Gower, A. Taylor, *Step-Size Stability in Stochastic Optimization: A Theoretical Perspective*, arXiv:2602.09842, first public 2026-02-10.
2. N. Loizou et al., *Stochastic Polyak Step-size for SGD: An Adaptive Learning Rate for Fast Convergence*, Proceedings of AISTATS 2021, PMLR 130.
3. F. Schaipp, R. M. Gower, M. Ulbrich, *A Stochastic Proximal Polyak Step Size*, arXiv:2301.04935.
