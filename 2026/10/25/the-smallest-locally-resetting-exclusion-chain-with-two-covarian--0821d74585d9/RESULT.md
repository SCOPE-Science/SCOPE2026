# The smallest locally resetting exclusion chain with two covariance sign reversals

## Finding

In the open-boundary totally asymmetric simple exclusion process with local resetting to its injection site, a chain of **three** sites is the smallest size at which a stationary nearest-neighbour covariance can change sign twice as the resetting rate increases. More precisely, with injection rate \(a=1\), extraction rate \(b=1/10\), unit rightward hopping, and individual bulk-to-first-site resetting at rate \(r\geq0\), the covariance between the final two occupations is

\[
C_{23}(r)=\operatorname{Cov}_{\pi_r}(\eta_2,\eta_3)=-\frac{20Q(r)}{D(r)^2},
\]
where
\[
\begin{aligned}
Q(r)&=30000r^4+93500r^3+6900r^2-114345r+7497,\\
D(r)&=200r^3+4230r^2+21471r+28455.
\end{aligned}
\]
The polynomial \(Q\) has exactly two strictly positive, simple roots, \(r_-=0.0660689676548\ldots\) and \(r_+=0.9091462368103\ldots\), so \(C_{23}(r)<0\) for \(0\leq r<r_-\) and \(r>r_+\), while \(C_{23}(r)>0\) for \(r_-<r<r_+\). At either threshold the covariance vanishes. These two reversals persist (at least two distinct sign changes, not necessarily exactly two) for all injection/extraction rates in a nonempty open neighbourhood of \((a,b)=(1,1/10)\).

For **every** two-site chain with \(a,b>0\), the sole nearest-neighbour covariance equals \((1-a-b-r)/T(r)^2\), where \(T(r)=b/a+a/b+a+b+r+1>0\); hence it has at most one positive zero. One site has no adjacent pair. The claimed three-site threshold is therefore minimal with respect to chain size.

## Assumptions and scope

A configuration is \(\eta=(\eta_1,\ldots,\eta_L)\in\{0,1\}^L\). Allowed transitions occur independently in continuous time: inject a particle at site \(1\) at rate \(a>0\) when empty; extract one at site \(L\) at rate \(b>0\) when occupied; move a particle from \(j\) to \(j+1\) at rate \(1\) when the departure site is occupied and destination vacant; for each occupied site \(j>1\), relocate that particle to site \(1\) at rate \(r\geq0\), but only if site \(1\) is empty. The last action does **not** create or destroy a particle. Each finite chain is irreducible for \(a,b>0\) (including at \(r=0\)), and therefore has a unique stationary law \(\pi_r\). All covariances here are **equal-time stationary** covariances, not temporal correlations or thermodynamic-limit covariances. The exact three-site formula is for \(a=1,b=1/10\), with a local robustness assertion around that parameter pair.

## Proof

**1. Two-site obstruction.** Enumerate states as \(00,01,10,11\). Set
\[
T=\frac ba+\frac ab+a+b+r+1.
\]
The probabilities
\[
(\pi(00),\pi(01),\pi(10),\pi(11))=T^{-1}(b/a,1,a+b+r,a/b)
\]
sum to one and solve the exact four global balance equations. Thus \(\operatorname{Cov}(\eta_1,\eta_2)=\pi(11)-[\pi(10)+\pi(11)][\pi(01)+\pi(11)]=(1-a-b-r)/T^2\). Its numerator is affine in \(r\), so it has at most one positive root for any positive \(a,b\).

**2. Three-site invariant probabilities.** For \(a=1\) and \(b=1/10\), enumerate states in the order
\[
000,001,010,011,100,101,110,111.
\]
All eight stationary probabilities have common positive denominator \(D(r)\), with respective numerators
\[
\begin{aligned}
N_{000}&=20r+21,\\
N_{001}&=10(20r+21),\\
N_{010}&=(10r+11)(20r+21),\\
N_{011}&=100(10r+21),\\
N_{100}&=200r^3+830r^2+991r+252,\\
N_{101}&=10(10r+21)(20r+11),\\
N_{110}&=1200r^2+3530r+2331,\\
N_{111}&=1000(10r+21).
\end{aligned}
\]
Direct substitution into the eight stationary generator equations \(G^\mathsf{T}N=0\) gives zero identically, and \(\sum N_\eta=D\). Positivity and uniqueness establish that \(\pi(\eta)=N_\eta/D\) is the exact stationary law, for every \(r\geq0\). The generator is specified constructively in `check.py`, with no approximation or truncation.

**3. Exact covariance.** Summing the displayed stationary weights gives
\[
\begin{aligned}
\mathbb E\eta_2&=\frac{2(700r^2+7480r+12831)}{D},\\
\mathbb E\eta_3&=\frac{20(100r^2+825r+1281)}{D},\\
\mathbb E(\eta_2\eta_3)&=\frac{1100(10r+21)}{D}.
\end{aligned}
\]
Subtracting the product of the two means and factoring the numerator yields the stated \(C_{23}=-20Q/D^2\). Every coefficient of \(D\) is strictly positive, so its denominator never vanishes on \(r\geq0\).

**4. Exactly two sign reversals.** The coefficient sequence of \(Q\) in descending powers is \((+,+,+,-,+)\), with exactly two sign changes. Descartes' rule therefore allows at most two positive roots, counted with multiplicity. On the other hand, the covariance at three rational rates is
\[
C_{23}(0)=-\frac{68}{367205}<0,\qquad
C_{23}(1/4)=\frac{6105560}{18594322321}>0,\qquad
C_{23}(1)=-\frac{29440}{184660921}<0.
\]
By continuity and the intermediate value theorem, \(Q\) has a root in \((0,1/4)\) and another in \((1/4,1)\). Descartes' bound proves that they are the only positive roots and that both are simple. Thus the full stated strict sign pattern follows, including all \(r>1\). Root decimals are optional descriptions of these uniquely characterized algebraic numbers; no numerical approximation is needed for the theorem.

**5. Open parameter stability.** At each fixed \(r=0,1/4,1\), the irreducible finite-state stationary distribution is a continuous (indeed rational analytic) function of positive \((a,b)\). The three strict covariance signs just established remain valid throughout some open neighbourhood of \((1,1/10)\). Therefore every such nearby rate pair admits a positive crossing in each of \((0,1/4)\) and \((1/4,1)\). We do not assert that there are exactly two crossings for every nearby parameter pair.

## Verification

Running `python check.py` with SymPy constructs the two- and three-site transition generators independently from the stated elementary moves. It checks the four and eight global-balance equations, normalizations, first and joint moment formulas, exact covariance identities, and rational sign witnesses, and locates the two positive quartic roots numerically only for reference. The recorded output is in `check_output.txt`; the program reports 24 passed exact stationary/polynomial/sign assertions. Descartes' theorem, continuity, and irreducibility complete the infinite-continuum sign classification analytically; numerical roots are not used as an exhaustive search.

## Relationship to prior work

Pelizzola and Pretti introduced and analysed this open-boundary TASEP with local resetting, including nearest-neighbour covariances, mainly via mean-field analysis, a thermodynamic continuum regime, and Monte Carlo simulation [1]. Their paper first appeared as a journal article in November 2022, with a later openly readable arXiv version. The exact three-site covariance polynomial, two sign reversals, and minimal-size obstruction are not results claimed here as originating in [1]. Their ordinary-open-TASEP cluster work [2] predates resetting and treats approximate pair/triplet closure, not this exact finite-state resetting sign classification. Periodic-boundary local-resetting models [3] have a different generator and lack these injection/extraction boundary transitions. Exact finite-state stationary linear algebra and Descartes' rule are standard tools; the claim concerns their specific physically motivated reentrant covariance consequence and its minimality, not a new solution method.

## Limitations

The two exact transition rates are established for the specified three-site parameter pair, with nearby existence only. No general phase diagram in the full \((a,b,r)\) parameter space and no extension to longer chains or a thermodynamic limit is proved. The signs concern the downstream pair of sites \((2,3)\), not all pairs. The transition is a finite-system sign crossover, **not** a thermodynamic phase transition.

## References

[1] A. Pelizzola and M. Pretti, *Totally asymmetric simple exclusion process with local resetting and open boundary conditions*, J. Phys. A: Math. Theor. **55** (2022) 454001, https://doi.org/10.1088/1751-8121/ac9d72 ; freely readable https://arxiv.org/html/2402.13698v1 (posted 2024-02-21).

[2] A. Pelizzola and M. Pretti, *Cluster approximations for the TASEP: stationary state and dynamical transition* (2017), https://arxiv.org/html/1710.10873v1 .

[3] A. Pelizzola, M. Pretti and M. Zamparo, *Simple exclusion processes with local resetting* (2020 preprint; 2021 journal), https://arxiv.org/abs/2012.10993 .
