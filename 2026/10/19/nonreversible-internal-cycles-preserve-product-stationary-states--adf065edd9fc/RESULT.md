# Nonreversible internal cycles preserve product stationary states in colored exclusion rings

## Finding

The ring exclusion process with occupied-neighbor-triggered internal color changes has a factorized stationary law for *every* irreducible color generator, including generators with nonzero cycle circulation. In particular, the detailed-balance condition imposed in Section V of Basu and Mohanty (2010) is sufficient but **not necessary** for a product measure. The correct requirement for this product family is merely the global stationary balance of the finite color generator.

**Theorem.** Fix integers \(L\ge3\), \(2\le M<L\), and \(\nu\ge2\). Sites of a labelled periodic ring have state \(0\) (vacant) or a color \(I\in\{1,\ldots,\nu\}\) (occupied); exactly \(M\) sites are occupied. A particle of color \(I\) hops clockwise across a vacant neighboring site at rate \(\alpha_I>0\). If that right neighbor is occupied, the particle changes color \(I\to J\ne I\) at rate \(r_{IJ}\ge0\). Suppose the color transition generator \(R\) is irreducible. Let \(w=(w_1,\ldots,w_\nu)\) be its positive (not necessarily normalized) stationary weights, uniquely determined up to common scale:

\[
 w_I\sum_{J\ne I}r_{IJ}=\sum_{J\ne I}w_Jr_{JI}
 \quad\text{for all }I.
\]

For a labelled ring state \(s\), write \(g_i(s)\) for the number of consecutive vacant sites immediately clockwise of its occupied site \(i\), stopping at the next occupied site. Its unique stationary probability is

\[
 \pi(s)=\frac{1}{Z_{\mathrm{lat}}}\prod_{i:s_i\ne0}w_{s_i}\alpha_{s_i}^{-g_i(s)}.
\]

Set \(V=L-M\), \(F(x)=\sum_{I=1}^{\nu}w_I(1-x/\alpha_I)^{-1}\), and \(Z_{m,V}=[x^V]F(x)^m\), with \(Z_{0,0}=1\) and \(Z_{0,V}=0\) for \(V>0\). Then the canonical normalizer and the net rate of color transitions \(I\to J\) minus \(J\to I\), counted across the entire lattice, are exactly

\[
 Z_{\mathrm{lat}}=\frac LM Z_{M,V},\qquad
 \mathcal J_{IJ}=\frac{M Z_{M-1,V}}{Z_{M,V}}(w_Ir_{IJ}-w_Jr_{JI}).
\]

In particular, for three colors with \(r_{12}=r_{23}=r_{31}=u>0\) and \(r_{21}=r_{32}=r_{13}=v>0\), one can choose \(w=(1,1,1)\). **Every equal-time stationary lattice statistic is independent of both \(u\) and \(v\)**, whereas each oriented internal cycle-edge current equals

\[
 \mathcal J_{\circlearrowright}=(u-v)\frac{M Z_{M-1,V}}{Z_{M,V}}.
\]

For \(u\ne v\) this violates the reversible cycle condition \(u^3=v^3\) but has a factorized stationary law and a nonzero internal current. With \(L=3\), \(M=2\), \(\alpha=(1,2,3)\), the coefficient ratio equals \(MZ_{1,1}/Z_{2,1}=1/3\): hence \(\mathcal J_{\circlearrowright}=(u-v)/3\).

## Assumptions and scope

All time evolution is a continuous-time Markov chain on a finite periodic ring with *labelled* lattice sites. No particles enter or leave, and all rates are time-homogeneous. Color changes are allowed **only when the clockwise neighbor is occupied**, and their rates do not depend on that neighbor's color. Every hopping rate is strictly positive. Color transitions may have zero rates, but their directed graph must be strongly connected. The restrictions \(M\ge2\) and \(V\ge1\) ensure that color-changing blocked configurations and particle transport are both possible. An overall scale change of \(w\) cancels after normalization. No spatial translation quotient is taken in \(\pi\).

The coefficient \([x^V]\) means the coefficient of degree \(V\) in the formal power series at the origin; all needed coefficients are finite sums. An internal current \(\mathcal J_{IJ}\) is an expected *net number of transitions per unit physical time*, not a spatial particle-hopping current.

## Proof

**1. Zero-range coordinates.** Number the \(M\) particles cyclically (this auxiliary particle root does not modify the physical state), and let \(n_k\ge0\) be the number of vacancies immediately to the right of particle \(k\), and \(\tau_k\) its color. Then \(\sum_kn_k=V\). Its hop is precisely the transfer

\[
 (n_{k-1},n_k)\longmapsto(n_{k-1}+1,n_k-1)
 \quad\text{at rate }\alpha_{\tau_k}\quad\text{if }n_k>0,
\]

and \(\tau_k\to J\) occurs at rate \(r_{\tau_kJ}\) precisely when \(n_k=0\).

**2. Hopping stationarity without detailed balance.** Put \(f_I(n)=w_I\alpha_I^{-n}\) and \(W(n,\tau)=\prod_kf_{\tau_k}(n_k)\). Consider a target state and an incoming hop from box \(k\) to box \(k-1\). This can occur exactly when its target has \(n_{k-1}>0\). Its predecessor has \((n_{k-1}-1,n_k+1)\), whose weight divided by the target weight is \(\alpha_{\tau_{k-1}}/\alpha_{\tau_k}\). Multiplying by the predecessor hop rate \(\alpha_{\tau_k}\), this incoming flux is \(W\alpha_{\tau_{k-1}}\). Summing over \(k\) gives total incoming hopping flux

\[
 W\sum_k\alpha_{\tau_{k-1}}\mathbf1_{n_{k-1}>0}
 =W\sum_k\alpha_{\tau_k}\mathbf1_{n_k>0},
\]

exactly equal to outgoing hopping flux. The equality is purely a cyclic reindexing; it requires no pairwise reversibility.

**3. Color-flip stationarity without detailed balance.** At each box with \(n_k=0\), the incoming color-flip flux into color \(I=\tau_k\) is

\[
 W\sum_{J\ne I}\frac{w_J}{w_I}r_{JI}
 =W\sum_{J\ne I}r_{IJ},
\]

where the last equality is precisely \(wR=0\). This equals its outgoing flip flux. No equation \(w_Ir_{IJ}=w_Jr_{JI}\) is assumed. Summing independent local balances over all sites proves stationarity of \(W\).

**4. Uniqueness and labelled normalization.** With all hopping rates positive, the vacancy chips on the cyclic box graph can be transferred between any boxes by repeated clockwise particle hops. For any chosen box, a vacancy configuration with \(n_k=0\) is reachable; since \(R\) is irreducible, its color can be changed along a directed path. Thereafter the vacancies can be redistributed to any target composition without changing colors. Repeating box by box establishes irreducibility of the rooted description and hence the physical labelled chain; a finite irreducible Markov chain has exactly one stationary distribution.

The unrooted cyclic particle sequence has \(M\) possible choices of distinguished occupied particle, while on a labelled ring that root can be assigned to any one of \(L\) sites. Consequently, the total stationary weight of labelled configurations is \(\frac LM\) times the sum over the \(M\) ordered gap boxes, namely \(\frac LM Z_{M,V}\). This identity can also be seen by summing weights over pairs (labelled configuration, distinguished occupied site) in two orders; it remains exact for rotationally symmetric configurations.

**5. Finite-size color current.** In the canonical gap ensemble, the combined weight of configurations with \(n_k=0\) and \(\tau_k=I\) at a fixed box is \(w_I Z_{M-1,V}\); division by \(Z_{M,V}\) gives its probability. Multiply by \(r_{IJ}\), subtract the reverse event count, and sum over \(M\) boxes to obtain the displayed \(\mathcal J_{IJ}\). Because \(V>0\) and every \(w_I>0\), the coefficient ratio is positive, and a nonzero local cycle current remains nonzero after coupling to the exclusion dynamics.

**6. Explicit irreversible family.** In the three-state cyclic rate family each state has total outgoing rate \(u+v\) and total incoming rate \(u+v\), so \(w=(1,1,1)\) satisfies global balance. The factorized stationary distribution depends only on \(w\) and \(\alpha\), hence is unaffected by \(u,v\); the cyclic current is the stated nonzero multiple of \(u-v\). For \(L=3\), \(M=2\), and \(\alpha=(1,2,3)\), direct coefficient extraction gives \(Z_{2,1}=11\) and \(Z_{1,1}=11/6\). This proves every assertion.

## Verification

Run `python3 verify.py` from the directory containing this document. The verifier uses only Python's standard library, builds the original labelled-ring Markov generator directly, and evaluates each edge flux and candidate stationary weight with exact rational arithmetic. Its 32 independent rational-rate cases comprise rings of three through six sites, two or three occupied particles, three distinct nonreversible cycle-rate matrices, and one noncirculant irreducible color-rate matrix. It checks 5,004 individual state master equations, exact normalization, and every pairwise stationary color flux; it also checks the minimal example and invariance between opposite rate biases. These finite checks are verification of the derivation, not proof for arbitrary parameters or sizes; the preceding algebra supplies that proof.

## Relationship to prior work

Basu and Mohanty, *TASEP on a ring with internal degrees of freedom* (first public preprint 2010-08-02, arXiv:1008.0316v1), introduced exactly these colored hops, blocked-neighbor flips, and the zero-range box mapping. Their Section V, equations (47)–(49), requires individual pairwise flip balance to construct a product measure and states that the \(\nu\ge3\) product measure cannot exist for unrestricted rates. The present proof retains their physically motivated weight form and mapping, but uses **global color stationarity in place of pairwise balance**; this supplies an explicit family outside the previously asserted condition. The earlier \(\nu=2\) formulas are not challenged, because any two-state irreducible color chain is automatically reversible. Nothing about the pre-existing two-state spatial-correlation formulas is claimed as new.

Basu and Mohanty's earlier work on zero-range/exclusion spatial correlations (arXiv:0912.2912) supplies general mapping and correlation machinery, but not the arbitrary nonreversible flip-generator conclusion. Greenblatt and Lebowitz's product-measure criteria for generalized zero-range processes (arXiv:cond-mat/0506776) concern zero-range particle transport and do not explicitly supply the blocked-neighbor internal color-cycle mechanism or its current formula. The Evans–Hanney zero-range review (arXiv:cond-mat/0501338) provides broader background. These comparisons do not establish that differently indexed literature has no equivalent result.

## Limitations

The theorem concerns **finite**, periodic, fully asymmetric transport and an irreducible **state-independent** color generator acting only at blocked particles. The independence in the three-color example applies to equal-time stationary laws and their functions, not to trajectory distributions, relaxation times, dynamic correlations, or noise levels. The result does not assert irreducibility for one occupied particle, a product law for nonconstant neighbor-color-dependent flip rates, or a thermodynamic-limit dynamical classification. A historical publication outside the inspected materials could contain equivalent global-balance reasoning; complete novelty certification is not claimed. No external scientific audit has been performed.

## References

1. U. Basu and P. K. Mohanty, *TASEP on a ring with internal degrees of freedom*, arXiv:1008.0316v1 (first public 2010-08-02), especially Section V, equations (47)–(49). https://arxiv.org/abs/1008.0316
2. U. Basu and P. K. Mohanty, *Particle Ordering in Zero Range Process: Exact spatial correlations of the corresponding exclusion models*, arXiv:0912.2912. https://arxiv.org/abs/0912.2912
3. M. Greenblatt and J. L. Lebowitz, *Product Measure Steady States of Generalized Zero Range Processes*, arXiv:cond-mat/0506776. https://arxiv.org/abs/cond-mat/0506776
4. M. R. Evans and T. Hanney, *Nonequilibrium Statistical Mechanics of the Zero-Range Process and Related Models*, arXiv:cond-mat/0501338. https://arxiv.org/abs/cond-mat/0501338
