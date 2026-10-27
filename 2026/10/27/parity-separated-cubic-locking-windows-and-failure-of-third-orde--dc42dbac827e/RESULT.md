# Parity-separated cubic locking windows and failure of third-order rotation-number expansion

## Finding
Let \(v(x)=1+\min(\{x\},1-\{x\})\) be periodic of period one, and let \(F_h(x)=x+h v(x)\), \(0<h<1\), be the lift of an orientation-preserving piecewise-affine circle homeomorphism. Denote its translation number by \(\rho(h)\). Put \(L=2\log(3/2)\). Define
\[
\begin{aligned}
 a_o&=-L^4/16-L^3/12+L^2/4,&b_o&=L^4/16-L^3/12-L^2/4,\\
 a_e&=-L^4/16+L^3/6,&b_e&=L^4/16-L^3/3.
\end{aligned}
\]
The positive widths are \(W_o=a_o-b_o=L^2/2-L^4/8>0\) and \(W_e=a_e-b_e=L^3/2-L^4/8>0\). For either parity \(p\in\{o,e\}\), any \(0<\varepsilon<W_p/2\), and every sufficiently large positive integer \(q\) of parity \(p\), the **entire nondegenerate interval**
\[
 L/q+(b_p+\varepsilon)/q^3\ \le h\le\ L/q+(a_p-\varepsilon)/q^3
\]
consists of maps with \(\rho(h)=1/q\). In particular the rational locking plateau around \(L/q\) contains an interval of width \((W_p-2\varepsilon)/q^3\). These are certified interior windows, not claims about the exact maximal tongue boundaries.

Furthermore, \(\rho(h)/h\to1/L\) as \(h\downarrow0\), but there are **no real coefficients** \(c_1,c_2,c_3\) for which
\[
\rho(h)=c_1h+c_2h^2+c_3h^3+o(h^3)\quad(h\downarrow0).
\]
The parity-dependent cubic locking windows obstruct a third-order Peano expansion at the identity map.

## Assumptions and scope
All limits in the locking theorem run through positive integers \(q\to\infty\) of a fixed parity. Each \(\varepsilon\) is fixed independently of \(q\). The sawtooth-shaped velocity \(v\) is continuous, strictly positive and globally Lipschitz, with breakpoints at the integers and half-integers. Since the slopes of \(F_h\) are \(1+h\) and \(1-h\), it is an increasing lift when \(0<h<1\). Its translation number is the uniform limit \(\rho(h)=\lim_{n\to\infty}(F_h^n(x)-x)/n\), independent of \(x\).

## Proof
**1. Positive first derivative at the identity.** Define \(H(x)=\int_0^x dt/v(t)\), extended by \(H(x+1)=H(x)+L\), with \(L=\int_0^1dt/v(t)=2\log(3/2)\). Since \(v\) is positive Lipschitz,
\[
 H(F_h(x))-H(x)=\int_x^{x+h v(x)}\!\frac{dt}{v(t)}=h+O(h^2)
\]
uniformly in \(x\). Summing along an orbit and using bounded displacement of the periodic difference \(H(x)-Lx\) gives \(L\rho(h)=h+O(h^2)\); hence \(\rho(h)/h\to1/L\).

**2. Exact endpoint-iterate identities.** Fix \(h=L/q+\gamma/q^3\) with \(\gamma\) in a fixed compact set. Starting at \(0\), the first-branch iterates are \(F_h^k(0)=(1+h)^k-1\) until crossing \(1/2\); starting at \(1/2\), second-branch iterates are \(F_h^k(1/2)=2-(3/2)(1-h)^k\) until crossing \(1\). Expanding the logarithms shows these crossings occur at step \(m+1\) for both starting points when \(q=2m+1\), and at steps \(m+1\) and \(m\), respectively, when \(q=2m\). The inequalities are strict, uniform for bounded \(\gamma\), and the remaining orbit segments do not encounter another branch boundary before time \(q\), for all sufficiently large \(q\). Composing affine branches therefore gives exact endpoint displacements \(D_0=F_h^q(0)-1\) and \(D_{1/2}=F_h^q(1/2)-3/2\):
\[
\begin{array}{ll}
q=2m+1:&D_0=1+((1+h)^{m+1}-3)(1-h)^m,\\
&D_{1/2}=(2-\tfrac32(1-h)^{m+1})(1+h)^m-\tfrac32;\\[3pt]
q=2m:&D_0=1+((1+h)^{m+1}-3)(1-h)^{m-1},\\
&D_{1/2}=(2-\tfrac32(1-h)^m)(1+h)^m-\tfrac32.
\end{array}
\]
For example, in the even case the \(0\)-orbit takes \(m+1\) first-branch steps and \(m-1\) second-branch steps; the other initial point takes \(m\) steps on each branch. All factors in these identities are exact, not numerical approximations.

**3. Uniform cubic-window asymptotics.** Put \(z=1/q\). For bounded \(\gamma\), the expansions \(\log(1\pm h)=\pm Lz-L^2z^2/2+(\pm\gamma\pm L^3/3)z^3+O(z^4)\) hold uniformly. Substitution into the above exact identities, using \(e^{L/2}=3/2\), cancels the constant and first-order terms. It yields, uniformly on each compact \(\gamma\)-set,
\[
\begin{array}{lll}
q\text{ odd}:&q^2D_0=\gamma-a_o+O(1/q),&q^2D_{1/2}=\tfrac32(\gamma-b_o)+O(1/q),\\
q\text{ even}:&q^2D_0=\gamma-a_e+O(1/q),&q^2D_{1/2}=\tfrac32(\gamma-b_e)+O(1/q).
\end{array}
\]
Here \(W_o=a_o-b_o=L^2/2-L^4/8>0\) and \(W_e=a_e-b_e=L^3/2-L^4/8>0\), since \(0<L<1\). Consequently for \(b_p+\varepsilon\le\gamma\le a_p-\varepsilon\), one has \(D_0<0<D_{1/2}\) once \(q\) is sufficiently large. By continuity, some \(x\in(0,1/2)\) satisfies \(F_h^q(x)=x+1\), so monotonicity of the lift implies \(\rho(h)=1/q\). This proves the asserted **whole interval** at either parity.

**4. Failure of third-order expansion.** Suppose \(\rho(h)=c_1h+c_2h^2+c_3h^3+o(h^3)\). Step 1 forces \(c_1=1/L>0\). Fix either parity and an \(\varepsilon\) as above, and use the two distinct endpoints \(h_q^-\) and \(h_q^+\) of its certified locking interval. They have equal translation number \(1/q\), yet \(h_q^+-h_q^-=(W_p-2\varepsilon)/q^3\). As both endpoints are \(L/q+O(q^{-3})\), their squared and cubed differences are \(O(q^{-4})\) and \(O(q^{-5})\). Subtracting their putative expansions gives \(0=c_1(W_p-2\varepsilon)/q^3+o(q^{-3})\), contradiction.

## Verification
The accompanying `CHECK.py` computes the exact affine iterate expressions at interior-window endpoints with high precision for several odd and even denominators, checks the predicted signs and rescaled asymptotics, and prints `LOCKING_WINDOW_DIAGNOSTICS_PASS` if successful. These finite tests are reproducibility diagnostics only; the proof for all sufficiently large denominators is the uniform asymptotic argument in Steps 2–4. The program requires Python 3 and `mpmath`.

## Relationship to prior work
Glendinning, Ma and Montaldi (2025), arXiv:2505.13689, analyze piecewise-linear circle maps, conjugation to rational rotations, and perturbative scaling near a **fixed** rational rotation. Glendinning (2025), arXiv:2506.19508, studies further scaling of rotation number near rational rotations. The theorem here instead studies a fixed one-parameter **positive-velocity** family in the singular regime where rotation denominators diverge as the family approaches the identity. It gives parity-sensitive cubic-width interior locking windows and uses them to disprove a third-order expansion at the identity. Campbell, Galeeva, Tresser and Uherka (1996) study broader piecewise-linear models and mode locking; the present statements must be assessed against that broader literature, which was not completely accessible during preparation.

## Limitations
The explicit constants are **lower bounds on normalized plateau widths**, via rigorously certified subintervals. No equality with full tongue widths or complete boundary asymptotics is asserted. The theorem applies to the stated triangular-velocity family, not to arbitrary Lipschitz circle maps. The third-order nonexpansion is a Peano/Taylor statement and does not rule out first-order differentiability or other regularity. Independent originality and proof validation remain outstanding.

## References
1. P. Glendinning, Y. Ma, and J. Montaldi, *Piecewise linear circle maps and conjugation to rigid rational rotations*, arXiv:2505.13689v1 (2025-05-19), https://arxiv.org/abs/2505.13689.
2. P. Glendinning, *Scaling of the rotation number for perturbations of rational rotations*, arXiv:2506.19508 (2025), https://arxiv.org/abs/2506.19508.
3. D. K. Campbell, R. Galeeva, C. Tresser, and D. J. Uherka, *Piecewise linear models for the quasiperiodic transition to chaos*, Chaos 6 (1996), 121–154, https://doi.org/10.1063/1.166159.
