# Exact optimizer on the \(D_5^+\) diagonal packing-covering ray
## Finding
Let \(D_5=\{z\in\mathbb Z^5:\sum_i z_i\equiv0\pmod 2\}\), let \(t=(1/2,1/2,1/2,1/2,1/2)\), and set \(X=D_5\cup(D_5+t)\). For \(\tau>0\), measure squared lengths by
\[
q_\tau(x)=x_1^2+x_2^2+x_3^2+x_4^2+\tau x_5^2,
\]
so the metric matrix is \(H_\tau=\operatorname{diag}(1,1,1,1,\tau)\). If \(\lambda_\tau\) is the minimum interpoint distance, \(\rho_\tau=\lambda_\tau/2\) the packing radius, \(\mu_\tau\) the covering radius, and \(\gamma_\tau=\mu_\tau/\rho_\tau\), then
\[
\gamma_\tau\ge \frac9{\sqrt{40}}
\quad\text{for every }\tau>0,
\]
with equality if and only if \(\tau=4/15\). Hence the coefficient \(4/15\) used by Ahrend--Dutour Sikirić is the unique global minimizer of the packing-covering constant on the entire symmetric diagonal ray \(H_\tau\) for the fixed two-periodic set \(X\).

## Assumptions and scope
The point set \(X\) is fixed; only the positive definite diagonal form \(H_\tau\) varies. No claim is made about all quadratic forms on \(X\), all two-periodic sets, or the unrestricted five-dimensional packing-covering optimum. The result is an exact one-parameter optimization theorem.

The public source of the distinguished point \(\tau=4/15\) is Ahrend--Dutour Sikirić, first public on 2026-09-24. Their Theorem 2.1 proves at that parameter
\[
\lambda^2=\frac{16}{15},\qquad
\mu^2=\frac{27}{50},\qquad
\gamma^2=\frac{81}{40}.
\]
The proof below independently reconstructs the packing formula for every \(\tau>0\), supplies explicit covering-radius lower witnesses on four parameter ranges, and independently rechecks the exact covering upper certificate at \(\tau=4/15\).

## Proof
For differences inside one \(D_5\) coset, parity gives
\[
\min_{0\ne z\in D_5}q_\tau(z)=\min\{4\tau,1+\tau,2}\}.
\]
The three values are attained by \(2e_5\), \(e_1+e_5\), and \(e_1+e_2\). Between the two cosets every coordinate is half-integral, hence the squared distance is at least \(1+\tau/4\), attained by \(t\). Therefore
\[
\lambda_\tau^2
=
\min\left\{4\tau,1+\tau,2,1+\frac\tau4}\right\}
=
\begin{cases}
4\tau,&0<\tau\le 4/15,\\
1+\tau/4,&4/15\le\tau\le4,\\
2,&\tau\ge4.
\end{cases}
\]

For \(0<\tau\le4/15\), use the fixed point
\[
h_0=\left(\frac{11}{30},\frac{11}{30},\frac1{15},0,1\right).
\]
Its nearest unconstrained integer vector is \((0,0,0,0,1)\), of odd parity. The base squared error is \(41/150\), and the least parity correction on this interval costs \(\tau\). Thus
\[
\operatorname{dist}_{H_\tau}(h_0,D_5)^2=\frac{41}{150}+\tau.
\]
For the translated coset the coordinatewise minimum is \(71/150+\tau/4\), which is no smaller on this interval and is equal only at \(\tau=4/15\). Hence
\[
\mu_\tau^2\ge \frac{41}{150}+\tau,
\qquad
\gamma_\tau^2\ge 1+\frac{41}{150\tau}
\ge\frac{81}{40},
\]
with equality in this bound only at \(\tau=4/15\).

For \(4/15\le\tau\le2/3\), set
\[
h_\tau=
\left(\frac{1-\tau}2,\frac{1-\tau}2,\frac\tau4,0,1\right).
\]
The nearest unconstrained integer vector is again \((0,0,0,0,1)\), and the cheapest parity correction costs \(\tau\). Direct substitution gives
\[
\operatorname{dist}_{H_\tau}(h_\tau,D_5)^2
=\frac12+\frac{9\tau^2}{16}.
\]
The point \(t\) is coordinatewise nearest in the translated coset and gives exactly the same value. Consequently
\[
\gamma_\tau^2
\ge
\frac{8+9\tau^2}{4+\tau}.
\]
The derivative has numerator \(9\tau^2+72\tau-8\), which is already positive at \(\tau=4/15\) and thereafter. Thus this lower bound is strictly increasing on the interval and equals \(81/40\) only at its left endpoint.

For \(2/3\le\tau\le2\), the test point \(e_5\) has exact squared distance \(\min\{\tau,1\}\}\) to \(X\). Hence
\[
\gamma_\tau^2\ge
\begin{cases}
\dfrac{16\tau}{4+\tau},&2/3\le\tau\le1,\\[4pt]
\dfrac{16}{4+\tau},&1\le\tau\le2,
\end{cases}
\]
and both expressions are strictly greater than \(81/40\) on their stated ranges.

For \(\tau\ge2\), use
\[
p=(0,0,0,0,3/4).
\]
The nearest even-parity integer layer and the nearest translated layer show exactly
\[
\operatorname{dist}_{H_\tau}(p,X)^2=1+\frac\tau{16}.
\]
Therefore
\[
\gamma_\tau^2\ge
\begin{cases}
\dfrac{16+\tau}{4+\tau},&2\le\tau\le4,\\[4pt]
2+\dfrac\tau8,&\tau\ge4,
\end{cases}
\]
and these bounds are at least \(5/2>81/40\).

It remains only to certify attainability at \(\tau=4/15\). The accompanying exact checker independently enumerates the vertices of the rational chamber polytope used to contain a Voronoi fundamental chamber. It obtains exactly \(41\) vertices and verifies that the maximum of \(q_{4/15}\) over them is \(27/50\). Since a convex quadratic reaches its maximum over a polytope at a vertex, symmetry gives \(\mu^2\le27/50\); the point \(h_0\) has exact distance squared \(27/50\), so equality holds. Together with \(\lambda^2=16/15\), this gives \(\gamma^2=81/40\). All other parameter ranges above have a strict lower bound, proving uniqueness.

## Verification
Run `python verify.py`. The script uses exact rational arithmetic only. It independently checks the distinguished packing minimum, verifies the hole distance, enumerates all \(5\)-fold active intersections of the \(12\) rational chamber inequalities, recovers exactly \(41\) feasible vertices, and confirms the exact maximum squared radius \(27/50\). It also checks the endpoint identities and strict numerical margins used in the piecewise argument. A successful run prints `VERIFY_OK`.

The infinite statement in \(\tau\) is proved analytically above; the finite vertex enumeration is used only for the covering upper bound at the equality parameter.

## Relationship to prior work
Ahrend--Dutour Sikirić prove the single exact configuration at \(\tau=4/15\), obtaining \(\gamma=9/\sqrt{40}\), and explain that a three-parameter numerical optimization led to that configuration. Their statement does not give an exact global minimization theorem along the whole diagonal ray or prove uniqueness of \(4/15\) on that ray.

Schürmann--Vallentin's packing-covering algorithms and the generalized Voronoi reduction theory of Dutour Sikirić--Schürmann--Vallentin concern lattices or restricted families of quadratic forms attached to lattice Delone subdivisions. Those results do not cover this fixed non-lattice two-coset set \(D_5^+\). Searches for the aliases \(D_5^+\), two-periodic \(D_5\) translate, the coefficient \(4/15\), and the value \(9/\sqrt{40}\) did not locate a prior exact all-\(\tau\) statement.

## Limitations
The theorem is confined to the one-parameter metric family \(\operatorname{diag}(1,1,1,1,\tau)\) on one fixed two-periodic set. It does not prove local or global optimality under arbitrary deformations of the point set or the metric. A companion note cited by the lead paper under the title “Non-lattice periodic point sets for the packing-covering problem: ties, structure and search” could not be located in a publicly inspectable version; it remains a specific residual literature risk, although the lead paper itself does not state the ray theorem proved here.

## References
1. Sven Ahrend and Mathieu Dutour Sikirić, “A non-lattice periodic point set beating the optimal lattice packing-covering constant in dimension five,” arXiv:2609.30513v1, 2026-09-24.
2. Achill Schürmann and Frank Vallentin, “Computational Approaches to Lattice Packing and Covering Problems,” *Discrete & Computational Geometry* 35 (2006), 73–116; arXiv:math/0403272.
3. Mathieu Dutour Sikirić, Achill Schürmann, and Frank Vallentin, “A generalization of Voronoi's reduction theory and its application,” *Duke Mathematical Journal* 142 (2008), 127–164; arXiv:math/0601084.
