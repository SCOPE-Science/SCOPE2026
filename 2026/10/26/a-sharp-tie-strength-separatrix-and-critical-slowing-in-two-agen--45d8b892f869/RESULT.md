# A sharp tie-strength separatrix and critical slowing in two-agent adaptive opinion dynamics

## Finding
For a pair of agents whose continuous opinions and social tie coevolve by the logistic-weight dynamics of Nugent, Gomes, and Wolfram [1], with exponentially decaying opinion receptiveness, there is an exact initial-tie threshold separating eventual consensus from enduring disagreement. The threshold and its critical orbit are explicit in terms of a convergent analytic series.

Fix \(\alpha>0\). For \(d>0\), put
\[
\Psi_\alpha(d)=\log d-\sum_{k=1}^{\infty}\frac{(\alpha d)^k}{k\,k!},
\qquad d_c=\frac{\log 2}{\alpha}.
\]
The series converges absolutely for every positive \(d\). If \(d_0>d_c\), define
\[
w_c(\alpha,d_0)=\tanh\!\left(\frac{\Psi_\alpha(d_c)-\Psi_\alpha(d_0)}{2}\right).
\]
Then \(0<w_c<1\) and the following classification is exhaustive for initial tie strength \(0<w_0<1\):

1. When \(d_0\le d_c\), or \(d_0>d_c\) and \(w_0>w_c\), the opinion gap tends to zero and the tie strength tends to one.
2. When \(d_0>d_c\) and \(w_0<w_c\), the tie strength tends to zero and the opinion gap tends to the unique \(d_\infty\in(d_c,d_0)\) satisfying
   \[
   \Psi_\alpha(d_\infty)=\Psi_\alpha(d_0)+2\operatorname{artanh}(w_0).
   \]
3. When \(d_0>d_c\) and \(w_0=w_c\), the trajectory approaches the threshold equilibrium \((d_c,0)\) with the sharp laws
   \[
   d(t)-d_c\sim\frac{2}{\alpha t},\qquad
   w(t)\sim\frac{2}{(\log2)t^2}\quad(t\to\infty).
   \]

For opinions restricted to \([-1,1]\), the interaction-decay threshold \(\alpha_*=\tfrac12\log2\) is sharp: **all** two-agent initial conditions with \(0<w_0<1\) and nonzero opinion gap reach consensus when \(\alpha\le\alpha_*\), whereas at every \(\alpha>\alpha_*\) there are admissible initially connected configurations that retain a nonzero opinion gap forever.

## Assumptions and scope
There are exactly two agents, with real-valued initial opinions \(x_1(0),x_2(0)\in[-1,1]\), initially distinct and separated by \(d_0=|x_1(0)-x_2(0)|\in(0,2]\). The undirected social tie has common reciprocal weight \(w(0)=w_0\in(0,1)\). Self-weights are one, giving degree normalization \(k_1=k_2=1+w\). The interaction function is \(\phi(r)=e^{-\alpha r}\), and the social tie follows the logistic weight rule with unit weight-evolution rate. In the original time units of [1], the exact reduced equations are
\[
\dot d=-\frac{2w}{1+w}e^{-\alpha d}d,
\qquad
\dot w=w(1-w)(2e^{-\alpha d}-1).
\tag{1}
\]
The system preserves \(d>0\) and \(0<w<1\) at every finite time. The mean opinion is constant. The theorem classifies asymptotic behavior only for this symmetric two-agent reduction; no assertion about larger networks follows automatically. When \(d_0=0\), the opinions already agree. Endpoint initial weights are not part of the classification: a zero link stays zero, whereas a unit link stays at one.

## Proof
**1. Invariant and monotonicity.** The function \(\Psi_\alpha\) is differentiable term by term and satisfies
\[
\Psi_\alpha'(d)=\frac{2-e^{\alpha d}}{d}.
\]
Consequently, it increases strictly on \((0,d_c)\), decreases strictly on \((d_c,\infty)\), and has its unique global maximum at \(d_c\). Using (1),
\[
\frac{d}{dt}\Psi_\alpha(d)
=-\frac{2w}{1+w}(2e^{-\alpha d}-1),
\]
whereas
\[
\frac{d}{dt}\bigl[2\operatorname{artanh} w\bigr]
=\frac{2w}{1+w}(2e^{-\alpha d}-1).
\]
It follows that
\[
\boxed{\Psi_\alpha(d(t))+2\operatorname{artanh}w(t)
=C:=\Psi_\alpha(d_0)+2\operatorname{artanh}w_0.}
\tag{2}
\]
Also, \(d(t)\) decreases strictly while \(w(t)>0\); the sign of \(\dot w\) is positive, zero, or negative according as \(d<d_c\), \(d=d_c\), or \(d>d_c\).

**2. Consensus side.** If \(d_0\le d_c\), then \(d(t)<d_c\) for all positive times and \(w\) is increasing. If the decreasing gap approached \(d_\infty>0\), its differential equation would remain bounded above by a strictly negative multiple of \(d\), since \(w\ge w_0>0\) and the bounded gap gives a positive lower bound for \(e^{-\alpha d}\). This is impossible; hence \(d\to0\). Since \(2e^{-\alpha d}-1\to1\) and \(0<w_0<1\), the logistic equation gives \(w\to1\).

Next suppose \(d_0>d_c\) and \(C>\Psi_\alpha(d_c)\), equivalently \(w_0>w_c\). While \(d>d_c\), the tie decreases. If that regime lasted forever, monotonic limits \(d_\infty\ge d_c\) and \(w_\infty\ge0\) would exist. A strictly positive \(w_\infty\) contradicts the strict decrease of \(d\) to a positive limit, so \(w_\infty=0\). Taking limits in (2) would give \(C=\Psi_\alpha(d_\infty)\le\Psi_\alpha(d_c)\), a contradiction. Thus \(d\) crosses \(d_c\) in finite time, after which the preceding consensus argument applies. This proves the first case.

**3. Polarization side.** Suppose \(d_0>d_c\) and \(C<\Psi_\alpha(d_c)\), equivalently \(w_0<w_c\). The orbit cannot reach \(d_c\), because (2) there would imply \(C\ge\Psi_\alpha(d_c)\). Therefore \(d>d_c\) forever and \(w\) decreases. Strictly positive limiting \(w\) again contradicts convergence of the decreasing positive gap, so \(w\to0\). By (2), \(\Psi_\alpha(d_\infty)=C\). Since \(\Psi_\alpha\) is strictly decreasing on \((d_c,\infty)\) and \(\Psi_\alpha(d_0)<C<\Psi_\alpha(d_c)\), exactly one \(d_\infty\in(d_c,d_0)\) satisfies this identity. This proves the second case.

**4. Critical orbit and rates.** Now take \(C=\Psi_\alpha(d_c)\) and \(d_0>d_c\). The same no-crossing argument applies. The limits are \(d\to d_c\) and \(w\to0\). Set \(z=d-d_c>0\). Direct differentiation gives
\[
\Psi_\alpha''(d_c)=-\frac{2\alpha}{d_c},
\qquad
\Psi_\alpha(d_c)-\Psi_\alpha(d_c+z)
=\frac{\alpha}{d_c}z^2+O(z^3).
\]
Using (2) and \(2\operatorname{artanh}w=2w+O(w^3)\), we obtain \(w=\frac{\alpha}{2d_c}z^2(1+O(z))\). Substitution in (1) yields \(\dot z=-\frac\alpha2 z^2(1+O(z))\). Integrating the asymptotic differential inequality for \(1/z\) gives \(z\sim2/(\alpha t)\), and hence \(w\sim2/(\alpha d_c t^2)=2/[(\log2)t^2]\). No finite-time contact with either boundary occurs because the smooth vector field contains the corresponding positive multiplicative factors.

**5. Sharp global parameter boundary.** Since both initial opinions belong to \([-1,1]\), \(d_0\le2\). If \(\alpha\le(\log2)/2\), then \(d_c\ge2\), placing every initial condition in the consensus case. Conversely, if \(\alpha>(\log2)/2\), take \(x_1(0)=-1\), \(x_2(0)=1\), so \(d_0=2>d_c\), and choose \(0<w_0<w_c(\alpha,2)\). Case 2 gives permanent asymptotic disagreement. The boundary is therefore optimal.

## Verification
A self-contained Python 3 program, `verify.py`, evaluates the convergent series without external packages, compares its numerical derivative with the proved derivative, tests the differential identity (2), and integrates representative trajectories using fourth-order Runge–Kutta. It checks both sides of the separatrix, the critical \(t^{-1}\) and \(t^{-2}\) scaling, and the sharp interaction-rate boundary. The program reports `VERIFICATION_OK: 128 independently evaluated numerical/algebraic assertions` when executed as `python3 verify.py`.

For \(\alpha=1\) and \(d_0=3/2\), the critical initial tie is approximately \(0.341759008217\). An initial tie of \(1/5\) leads to limiting disagreement \(d_\infty\approx1.20672588053\); a tie of \(9/10\) leads to consensus. At criticality the numerical trajectory at \(t=1000\) has \(d\approx0.695151595187\) and \(w\approx2.88882737931\times10^{-6}\). These calculations are consistency checks; the proof above supplies the all-time and all-parameter conclusions.

## Relationship to prior work
Nugent, Gomes, and Wolfram [1] introduced the coupled continuous-time network/opinion system, including the logistic edge-weight rule and exponential interaction function. They proved well-posedness and several consensus results and used simulations to exhibit the possibility of clustering when the social ties adapt. The present two-agent result uses exactly that normalization and logistic law, but resolves the complete parameter-dependent asymptotic trichotomy in its smallest nontrivial connected network, including the sharp initial-weight separatrix and algebraic critical rates.

Kan, Feng, and Porter [2] also investigate consensus and polarization in adaptive social networks. Their adaptive Deffuant–Weisbuch mechanism changes the network by discrete rewiring after a tolerance test, rather than by the continuous logistic-weight equation (1); its phase-transition results do not specify the invariant (2) or the exact threshold here. The elementary scalar separation embodied by (2) is a general ODE technique; no priority over general phase-plane methods is claimed.

## Limitations
This is a two-agent, symmetric, undirected, deterministic continuous-time result; asymmetric influence, more agents, discrete rewiring, stochastic updates, and non-exponential interaction functions may have different phase portraits. The model's 'polarization' means a strictly positive limiting opinion gap while the tie tends to zero; it does not imply that opinions move farther apart (indeed, the gap strictly decreases). The numerical checks do not prove any asymptotic claim. Although relevant literature was compared, priority over all possible formulations of equivalent scalar adaptive-link dynamics is not established independently.

## References
[1] A. J. Nugent, S. N. Gomes, and M.-T. Wolfram, *On evolving network models and their influence on opinion formation*, arXiv:2305.09483v1, initially public May 16, 2023. https://arxiv.org/abs/2305.09483; equations (3), (8), (12), and the exponential interaction example.

[2] U. Kan, M. Feng, and M. A. Porter, *An adaptive bounded-confidence model of opinion dynamics on networks*, Journal of Complex Networks **11** (2023), cnac055, https://doi.org/10.1093/comnet/cnac055; the discrete rewiring model and its numerical polarization study.
