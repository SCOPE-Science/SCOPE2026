# Tilted quartic two-cut model: no spontaneous Z2 breaking of the planar first moment

## Context

The target asks whether the symmetric two-cut quartic Hermitian one-matrix model exhibits spontaneous Z2 symmetry breaking detectable through an infinitesimal linear tilt. The untilted potential V_0(x)=x^4/4-2x^2, i.e. (r,g)=(-4,1), lies in the symmetric two-cut regime. The question is whether the planar first moment remembers the sign of a vanishing tilt after the large-N limit, giving nonzero iterated limits e_+=-e_-=m_*>0 selected by two-cut endpoint equations plus equal-potential filling, or whether the limits return to zero.

## Definitions

Let dM be Lebesgue measure on N x N Hermitian matrices. For h in [-1,1] define

mu_{N,h}(dM) = Z_{N,h}^{-1} exp(-N Tr(-2M^2+M^4/4-hM)) dM,

V_h(x) = x^4/4-2x^2-hx, e_N(h) = E_{mu_{N,h}}[N^{-1} Tr M].

Let F_N(h)=N^{-2} log Z_{N,h}, G_N(h)=F_N(h)-F_N(0). On probability measures on R define the log-gas rate function

I_h(mu) = int V_h dmu - Sigma(mu), Sigma(mu) = iint log|x-y| dmu(x)dmu(y).

Denote by mu_h^* the minimizer of I_h when it exists and is unique, and m(h)=int x dmu_h^*(x).

## Result

1. For every N, e_N(-h)=-e_N(h); in particular e_N(0)=0 exactly, so lim_N e_N(0)=0.
2. For every fixed h in (-1,1), m(h)=lim_{N->infty} e_N(h) exists and equals the mean of the unique minimizer mu_h^* of I_h.
3. h -> m(h) is continuous with m(0)=0 (the h=0 minimizer is symmetric by uniqueness).
4. Hence both iterated tilted limits exist and e_+ = lim_{h downarrow 0} lim_N e_N(h) = 0, e_- = lim_{h uparrow 0} lim_N e_N(h) = 0.
5. In particular there is no m_*>0 with e_+=-e_-=m_*. Any asymmetric two-cut stationary point with nonzero mean is not the global free-energy minimizer at h=0: symmetrization strictly lowers I_0, and equal-chemical-potential selection at the symmetric point forces symmetric 1/2-1/2 filling with mean zero. The stated spontaneous Z2 breaking fails at this reference point; the limit free energy is differentiable at h=0.

## Proof / evidence

Finite-N symmetry: M -> -M preserves dM, flips Tr M, and preserves the V_0 weight, so Z_{N,-h}=Z_{N,h} and e_N(-h)=-e_N(h). Z_{N,h}<infty by quartic confinement uniform for |h|<=1; h -> Z_{N,h} is smooth. Moreover d/dh log Z_{N,h}=N^2 e_N(h), so F_N'=e_N and F_N''>=0: each F_N is convex and smooth. Eigenvalue decomposition gives an h-independent unitary volume that cancels in free-energy differences and derivatives.

Equilibrium measure: V_h satisfies the Anderson-Guionnet-Zeitouni growth hypothesis quartically, so the speed-N^2 Coulomb-gas LDP applies with rate I_h up to an h-independent additive constant. Uniform coercivity: phi(x)=inf_{|h|<=1} V_h(x)-2log(1+|x|) is bounded below and superlinear (|x|/phi->0), since V_h>=x^4/4-2x^2-|x|. The key inequality Sigma(mu)<=2 int log(1+|x|) dmu gives I_h(mu)>=int phi dmu. The uniform reference nu_0=Unif[-1,1] has finite I_h uniformly, so inf I_h<=C_0<infty. Hence sublevel sets are uniformly tight, I_h is lower semicontinuous, and each I_h admits a minimizer with compact support and no atoms. Strict concavity of Sigma (logarithmic-energy Fourier representation) makes I_h strictly convex, so the minimizer mu_h^* is unique for every h.

Stability: if h_n->h, uniform tightness plus a moving-h lower-semicontinuity argument using bounded first moments gives whole-sequence weak convergence mu_{h_n}^*->mu_h^*. Uniform integrability from int phi dmu_n<=C_0+1 and |x|/phi->0 yields m(h_n)->m(h); thus m is continuous. At h=0, evenness of V_0 plus uniqueness forces mu_0^* symmetric, so m(0)=0. Symmetrization bar mu=(mu+check mu)/2 preserves int V_0 and strictly increases Sigma unless mu is symmetric, so I_0(bar mu)<I_0(mu) for asymmetric finite-energy mu.

Double limit: with F(h)=-inf I_h, the minimizer as trial measure gives F(k)>=F(h)+(k-h)m(h), so m(h) is a subgradient of the convex finite function F; with continuity of m the difference quotient is squeezed, giving F differentiable with F'=m. Pointwise convergence G_N->G=F-F(0) with convex G_N plus differentiability of G gives by Griffiths' lemma (three-secant inequality) G_N'(h)->G'(h), i.e. lim_N e_N(h)=m(h) at each fixed h. Continuity at 0 yields e_+=e_-=0. Normalizations (N^{-1} Tr observable, Nh tilt, N^{-2} log Z scaling, h-independent Haar constants) are verified and cancel where claimed.

## Limitations

Uses standard cited tools (AGZ LDP, strict concavity of logarithmic energy, Griffiths convex-differentiation lemma) whose proofs are referenced, not reproduced. Does not classify all asymmetric Schwinger-Dyson saddle points; it shows none is the free-energy-selected h->0 double limit, which is the content of the target. Numeric artifact checks analytic coercivity bounds only; the proof does not depend on numerics.

## Reproducibility

The uniform bounds can be rechecked by running output/artifacts/coercivity_check.py, which confirms the global lower bound on phi, tail growth, |x|/phi->0, and finiteness of I_h(nu_0) (grid min phi approx -8.35, Sigma(Unif[-1,1]) approx -0.81). The analytic proof is self-contained in the sections above given the cited textbook theorems.

## References

- G. Anderson, A. Guionnet, O. Zeitouni, An Introduction to Random Matrices, Ch. 2.6.
- P. Deift, Orthogonal Polynomials and Random Matrices: A Riemann-Hilbert Approach, Ch. 6.
- K. Johansson, On fluctuations of eigenvalues of random Hermitian matrices, Duke Math. J. 91 (1998).
- R. T. Rockafellar, Convex Analysis, Thm 25.7.
