# Sharp dimension-seven onset of heterogeneity-assisted weak resetting in absorbing balls

## Finding

Let \(d\ge2\), \(R,D>0\), and let Brownian motion have generator \(D\Delta\) in the open Euclidean ball \(B_R\subset\mathbb R^d\), with absorption upon reaching its boundary. Initially and after each independent Poisson resetting event of rate \(\lambda\ge0\), draw a fresh position independently from the *same* probability law \(\nu\) supported in \(B_R\). No time is spent in relocating, and absorption terminates the process. Let \(M_d(\lambda;\nu)\) denote the unconditional mean time to absorption. For a draw \(X\sim\nu\), write
\[
U=1-\frac{|X|^2}{R^2},\qquad a=\mathbb E U,\qquad b=\mathbb E U^2.
\]
Then the exact weak-rate derivative is
\[
\boxed{\left.\frac{d}{d\lambda}M_d(\lambda;\nu)\right|_{\lambda=0^+}
=-\frac{R^4}{8D^2d^2(d+2)}\left[4a+db-2(d+2)a^2\right].}
\]
Thus a strictly negative right derivative (and hence a reduction in the mean for all sufficiently small positive rates) occurs exactly when \(4a+db>2(d+2)a^2\). A strictly positive derivative gives the opposite small-rate response; equality of the displayed criterion does not by itself decide higher-order behavior.

For a deterministic resetting position at radius \(r\), the weak-rate response is non-improving precisely when \(r\le R\sqrt{d/(d+4)}\). **The following sharp dimensional reversal holds:** a reset law \(\nu\) supported entirely in this deterministic non-improving core nevertheless has a strictly improving weak-rate response for some such \(\nu\) **if and only if \(d\ge7\)**.

Indeed, put \(t=4/(d+4)\). For \(d\ge7\), choose \(U=t\) with probability \(1-q\) and \(U=1\) with probability \(q\), where
\[
0<q<\frac{d^2-4d-16}{2d(d+2)}.
\]
The corresponding positions can be chosen on the sphere of radius \(R\sqrt{d/(d+4)}\) and at the center. For \(d=7\) and \(q=1/50\), the bracket in the derivative formula equals exactly \(217/75625>0\). By continuity, the noncentral position can also be moved slightly toward the center, making **both** deterministic components strictly non-improving to first order while their mixture strictly improves the mean.

## Assumptions and scope

The spatial dimension is an integer \(d\ge2\). The positional law is any Borel probability measure on the open ball; it may be discrete, singular, or angularly anisotropic. The law at the initial launch is the same as that at each reset, all draws are independent, and reset times form an independent Poisson process. The Brownian diffusion is isotropic with generator \(D\Delta\); the boundary is entirely absorbing. The conclusion concerns the right derivative at zero resetting rate, not necessarily the globally optimal rate. The lower-dimensional impossibility is restricted to laws supported in the deterministic non-improving core.

## Proof

**Exit-time moments.** Let \(\tau\) be the first boundary hitting time without resetting, started at a fixed radial position \(r<R\). The radial Dirichlet problems \(D\Delta m_1=-1\) and \(D\Delta m_2=-2m_1\), with zero boundary data and regularity at the center, yield uniquely
\[
m_1(r)=\frac{R^2-r^2}{2dD},\qquad
m_2(r)=\frac{(R^2-r^2)[(d+4)R^2-dr^2]}{4d^2(d+2)D^2}.
\]
For example, \(\Delta r^2=2d\) and \(\Delta r^4=4(d+2)r^2\), so substitution checks both differential equations and both boundary conditions. Averaging over \(\nu\) gives
\[
\mu=\mathbb E\tau=\frac{R^2a}{2dD},\qquad
m_2=\mathbb E\tau^2=\frac{R^4(4a+db)}{4d^2(d+2)D^2}.
\]
These moments are finite because the domain is bounded.

**Independent-cycle renewal.** Let \(\Phi(\lambda)=\mathbb E_\nu e^{-\lambda\tau}\). At each launch the chance of absorption before an independent exponential resetting clock is \(\Phi(\lambda)\), and the mean duration of that attempt is \((1-\Phi(\lambda))/\lambda\). The iid renewal decomposition therefore gives, for \(\lambda>0\),
\[
M_d(\lambda;\nu)=\frac{1-\Phi(\lambda)}{\lambda\Phi(\lambda)}.
\]
Expanding \(\Phi(\lambda)=1-\mu\lambda+(m_2/2)\lambda^2+o(\lambda^2)\) proves
\[
M_d(\lambda;\nu)=\mu+\left(\mu^2-\frac{m_2}{2}\right)\lambda+o(\lambda),
\]
which yields the stated derivative with its exact normalization and equivalence.

**Sharp dimension cutoff.** For a point mass, \(b=a^2\), and the bracket becomes \(a[4-(d+4)a]\); non-improvement is equivalent to \(a\ge t=4/(d+4)\), or \(r\le R\sqrt{d/(d+4)}\). For a general law supported in that core, \(U\in[t,1]\), so \((U-t)(1-U)\ge0\) implies \(b\le(1+t)a-t\). Consequently,
\[
4a+db-2(d+2)a^2
\le(a-t)[d-2(d+2)a].
\]
Since \(a\ge t\), the final bracket is at most
\[
d-2(d+2)t=\frac{d^2-4d-16}{d+4}.
\]
This is strictly negative for integer \(2\le d\le6\), proving impossibility there. For \(d\ge7\), let \(U\) take the endpoints \(t,1\) with probabilities \(1-q,q\). The quadratic-moment bound is now an equality and \(a=t+q(1-t)\). Its bracket is positive precisely when
\[
0<q<\frac{d^2-4d-16}{2d(d+2)}.
\]
This interval is nonempty exactly for integers \(d\ge7\). At \(d=7\), \(t=4/11\) and \(q=1/50\) give \(4a+db-18a^2=217/75625\). Strict positivity persists under sufficiently small perturbations of \(t\) upward, completing the strict-component variant.

## Verification

Run `python verify.py` from the directory containing this document. The script uses exact rational arithmetic to check the dimension cutoff and the two-point witness over many dimensions. If `mpmath` is installed, it additionally evaluates the independent modified-Bessel exit-time Laplace transform and compares finite-difference resetting derivatives with the proved formula. The executed version passed 387 checks, including nine independent Bessel-transform comparisons. These finite computations corroborate the proof; they are not substituted for its all-dimensional argument.

## Relationship to prior work

Chen and Huang (arXiv:2109.11101, first posted 23 September 2021) obtained the fixed-start radial first and second exit moments and the deterministic critical radius \(R\sqrt{d/(d+4)}\). Evans and Majumdar (arXiv:1107.4225) studied spatial reset distributions for one-dimensional diffusion, and Toledo-Marin and Boyer (arXiv:2206.14387) developed renewal formulas for random relocation in one-dimensional first passage. The general criterion based on the coefficient of variation of the unreset completion time is also established in earlier restart literature. Those facts are prerequisites here, not claimed as new. The additional assertion is the **sharp all-law geometric dichotomy at dimension seven**, obtained by an extremal second-moment inequality on the individually non-improving core, together with the explicit heterogeneity counterexample. A different one-dimensional protocol where an alarm can itself absorb the particle has no implication for this iid randomized spatial-resetting model.

## Limitations

Only the sign of the first derivative at zero rate is classified; at zero derivative a higher-order expansion is needed, and no claim of global monotonicity, uniqueness, or optimal resetting rate is made. The dimension-seven statement assumes that *every allowed deterministic reset radius* is individually non-improving to first order. The result does not address finite-time absorption quantiles, resetting overhead, moving targets, reflecting boundary pieces, or state-dependent reset clocks. The literature relationship relies on a comparison of the inspected works and targeted searches; priority relative to any unlocated equivalent higher-dimensional random-relocation theorem remains open to independent scrutiny.

## References

1. H. Chen and F. Huang, *First passage of a diffusing particle under stochastic resetting in bounded domains with spherical symmetry*, arXiv:2109.11101 (posted 23 September 2021), Physical Review E 105, 034109 (2022). https://arxiv.org/html/2109.11101v2
2. M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, arXiv:1107.4225 (2011), Journal of Physics A 44, 435001. https://arxiv.org/html/1107.4225v2
3. J. Q. Toledo-Marin and D. Boyer, *First passage time and information of a one-dimensional Brownian particle with stochastic resetting to random positions*, arXiv:2206.14387 (posted 29 June 2022). https://arxiv.org/html/2206.14387v1
4. A. Pal and S. Reuveni, *First Passage under Restart*, Physical Review Letters 118, 030603 (2017). https://doi.org/10.1103/PhysRevLett.118.030603
