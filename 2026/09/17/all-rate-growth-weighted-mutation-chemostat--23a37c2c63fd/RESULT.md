# All-rate threshold theorem for growth-weighted reversible mutation in a chemostat

## Context

Alvarez-Latuz, Bayen and Coville study chemostats with a substrate-dependent exchange matrix. Their Section 4.2 uses a growth-weighted cyclic mutation matrix and proves the equilibrium classification only under the sufficient restriction \(0\leq\varepsilon\leq 1/2\); for larger mutation rates, strict monotonicity of the Perron root in the substrate and the resulting coexistence classification are supported numerically. The result below proves that monotonicity for every \(\varepsilon>0\), and at the same time extends the cycle to any irreducible reversible mutation network. It also proves global asymptotic stability of washout at the critical dilution rate, where the cited proposition states stability but only asserts global asymptotic stability for strict inequality.

## Model and assumptions

Let \(n\ge 2\). Let \(L\in\mathbb R^{n\times n}\) be an irreducible conservative mutation generator in the **column convention**:

- \(L_{ij}\ge 0\) for \(i\ne j\);
- \({\bf 1}^{\top}L=0\);
- there is a probability vector \(\pi\gg0\) with \(L\pi=0\);
- detailed balance holds: \(L_{ij}\pi_j=L_{ji}\pi_i\).

For \(i=1,\dots,n\), let \(\mu_i:[0,s_{in}]\to[0,\infty)\) be \(C^1\), satisfy \(\mu_i(0)=0\), and be strictly increasing, hence \(\mu_i(s)>0\) for \(s>0\). Let \(Y_i>0\), \(D(s)=\operatorname{diag}(\mu_1(s),\dots,\mu_n(s))\), \(u>0\), and \(\varepsilon>0\). Consider

\[
\dot x=\big((I+\varepsilon L)D(s)-uI\big)x,
\qquad
\dot s=-\sum_{i=1}^n\frac{\mu_i(s)x_i}{Y_i}+u(s_{in}-s).
\tag{1}
\]

The exchange term is \(\varepsilon L D(s)x\): mutation flux is proportional to reproduction/growth. The cycle in Section 4.2 of Alvarez-Latuz--Bayen--Coville is obtained by taking \(L\) to be the symmetric nearest-neighbour cycle generator with diagonal \(-2\).

Define
\[
M_\varepsilon(s)=(I+\varepsilon L)D(s),\qquad
r_\varepsilon(s)=s\big(M_\varepsilon(s)\big),\qquad
u_c(\varepsilon)=r_\varepsilon(s_{in}),
\]
where \(s(A)\) denotes the spectral bound.

## Theorem

Under the assumptions above:

1. **Strict substrate monotonicity for every mutation rate.** For every \(\varepsilon>0\), \(r_\varepsilon(0)=0\), \(r_\varepsilon(s)>0\) for \(s>0\), and \(s\mapsto r_\varepsilon(s)\) is strictly increasing on \([0,s_{in}]\).

2. **Exact equilibrium threshold for every mutation rate.** If \(u\ge \nu_c(\varepsilon)\), washout \(E_0=(0,s_{in})\) is the only equilibrium. If \(0<u<\nu_c(\varepsilon)\), there are exactly two equilibria: washout, which is unstable, and one coexistence equilibrium \((x^*,s^*)\gg0\) in biomass coordinates, with \(0<s^*<s_{in}\).

3. **Washout is globally asymptotically stable at and above threshold.** For every \(u\ge\nu_c(\varepsilon)\), every solution of (1) with \(x(0)\ge0\), \(0\le s(0)\le s_{in}\) converges to \(E_0\). In particular, the equality case \(u=\nu_c(\varepsilon)\) is globally asymptotically stable, not merely Lyapunov stable.

4. **Mutation-strength structure.** If the endpoint growth rates \(\mu_i(s_{in})\) are not all equal, then \(\nu_c(\varepsilon)\) is strictly decreasing for \(\varepsilon>0\), and
\[
\lim_{\varepsilon\to\infty}\nu_c(\varepsilon)
=\left(\sum_{i=1}^n\frac{\pi_i}{\mu_i(s_{in})}\right)^{-1}.
\tag{2}
\]
For a symmetric cycle, \(\pi_i=1/n\), so the limit is the ordinary harmonic mean of the endpoint growth rates. The non-increase of the critical spectral bound with mixing is consistent with the general reduction phenomenon; the explicit harmonic formula is a specialization of the limiting Perron-vector formula in the source paper.

No claim is made here that the coexistence equilibrium is locally or globally stable for arbitrary \((\varepsilon,u)\) below threshold; the cited paper explicitly identifies all-rate local stability of coexistence as a further question.

## Proof

### 1. Reversible symmetrization and a Rayleigh quotient

Let \(R=\operatorname{diag}(\pi_i^{-1/2})\) and \(A=RLR^{-1}\). Detailed balance gives \(A=A^{\top}\). Because \(A\) is similar to the irreducible Markov generator \(L\), \(A\) is negative semidefinite and
\[
\ker A=\operatorname{span}\{\sqrt\pi\},
\qquad \sqrt\pi=(\sqrt{\pi_1},\dots,\sqrt{\pi_n})^{\top}.
\]
For \(s>0\), \(R\) commutes with \(D(s)\), and
\[
R M_\varepsilon(s)R^{-1}=(I+\varepsilon A)D(s).
\]
Conjugating once more by \(D(s)^{1/2}\) shows that \(M_\varepsilon(s)\) is similar to the symmetric matrix
\[
S_\varepsilon(s)=D(s)^{1/2}(I+\varepsilon A)D(s)^{1/2}.
\]
Hence
\[
r_\varepsilon(s)
=\max_{z\ne0}
\frac{z^{\top}(I+\varepsilon A)z}{z^{\top}D(s)^{-1}z}.
\tag{3}
\]
Taking \(z=\sqrt\pi\) makes the numerator \(\|\sqrt\pi\|^2=1\), so \(r_\varepsilon(s)>0\).

If \(0<s_1<s_2\), strict growth monotonicity gives
\(D(s_2)^{-1}<D(s_1)^{-1}\) entrywise on the diagonal. Let \(z_1\) maximize (3) at \(s_1\). Its numerator is positive because the maximizing quotient equals \(r_\varepsilon(s_1)>0\). Therefore
\[
\frac{z_1^{\top}(I+\varepsilon A)z_1}{z_1^{\top}D(s_2)^{-1}z_1}
>
\frac{z_1^{\top}(I+\varepsilon A)z_1}{z_1^{\top}D(s_1)^{-1}z_1}
=r_\varepsilon(s_1),
\]
which implies \(r_\varepsilon(s_2)>r_\varepsilon(s_1)\). At \(s=0\), \(D(0)=0\), hence \(r_\varepsilon(0)=0\).

### 2. Equilibria

For every \(s>0\), \(M_\varepsilon(s)\) is irreducible Metzler. If a nonzero equilibrium has \(x\ge0\), Perron--Frobenius implies \(x\gg0\) and \(u=r_\varepsilon(s)\). By part 1, such an \(s\) exists exactly when \(0<u<\nu_c(\varepsilon)\), and then it is unique. If \(v(s^*)\gg0\) is the Perron vector normalized arbitrarily, the substrate equation fixes its scale uniquely:
\[
x^*=\alpha v(s^*),\qquad
\alpha=\frac{u(s_{in}-s^*)}{\sum_i \mu_i(s^*)v_i(s^*)/Y_i}>0.
\]
At \(u=\nu_c\), the only possible Perron root occurs at \(s=s_{in}\), but the substrate balance forbids nonzero biomass there. Thus washout is the sole equilibrium for \(u\ge\nu_c\). If \(u<\nu_c\), the biomass block of the washout Jacobian has Perron eigenvalue \(\nu_c-u>0\), so washout is unstable.

### 3. Global asymptotic stability of washout at the critical value

Put \(D_\infty=D(s_{in})\), \(M_\infty=(I+\varepsilon L)D_\infty\), and let \(p\gg0\) be a left Perron vector:
\[
p^{\top}M_\infty=\nu_c p^{\top}.
\]
Since
\[
M_\varepsilon(s)=M_\infty Q(s),\qquad
Q(s)=D_\infty^{-1}D(s)=\operatorname{diag}(q_i(s)),
\]
where \(0\le q_i(s)\le1\), the linear functional \(V(x)=p^{\top}x\) satisfies
\[
\dot V=\sum_i p_i\big(\nu_c q_i(s)-u\big)x_i.
\tag{4}
\]
If \(u>\nu_c\), then \(\dot V\le-(u-\nu_c)V\), hence \(x(t)\to0\) exponentially and then \(s(t)\to s_{in}\).

Let now \(u=\nu_c\). Equation (4) gives \(\dot V\le0\), with strict inequality whenever \(x\ne0\) and \(s<s_{in}\). On the boundary \(s=s_{in}\), any state with \(x\ne0\) has
\[
\dot s=-\sum_i\frac{\mu_i(s_{in})x_i}{Y_i}<0,
\]
so it cannot remain in the zero-derivative set. Solutions are bounded: with \(Y_{max}=\max_iY_i\),
\[
B=s+\frac1{Y_{max}}\sum_i x_i
\]
satisfies \(\dot B\le u(s_{in}-B)\), because \({\bf1}^{\top}LD(s)x=0\). LaSalle's principle therefore implies \(x(t)\to0\). Then, writing \(q=s_{in}-s\),
\[
\dot q=\sum_i\frac{\mu_i(s)x_i}{Y_i}-uq
\]
and the forcing term tends to zero, so \(q(t)\to0\), i.e. \(s(t)\to s_{in}\).

Lyapunov stability at equality also follows directly. Since \(V(t)\le V(0)\), \(\sum_i x_i(t)\le V(0)/p_{min}\). Thus for
\(C=\max_i \mu_i(s_{in})/(Y_i p_i)\),
\[
\dot q\le C V(0)-u q,
\]
so \(q(t)\le q(0)e^{-ut}+(C/u)V(0)\). Norm equivalence now gives stability of \(E_0\). Together with global attraction this proves global asymptotic stability.

### 4. Dependence on mutation intensity

At \(s=s_{in}\), formula (3) gives
\[
\nu_c(\varepsilon)=\max_{z\ne0}
\frac{\|z\|^2+\varepsilon z^{\top}Az}{z^{\top}D_\infty^{-1}z}.
\tag{5}
\]
Since \(A\le0\), \(\nu_c\) is non-increasing. For \(\varepsilon>0\), irreducibility makes the top eigenvalue simple, so differentiation of the symmetric eigenvalue problem shows that equality in the derivative can occur only when the maximizing \(z\in\ker A\). The generalized eigenvalue equation then forces \(D_\infty\) to be a scalar matrix. Therefore, unless all endpoint growth rates coincide, \(\nu_c\) is strictly decreasing.

As \(\varepsilon\to\infty\), boundedness of the maximizing quotient in (5) forces maximizing vectors toward \(\ker A=\operatorname{span}\{\sqrt\pi\}\). Substitution of \(z=\sqrt\pi\) in the limiting quotient yields (2).

## Numerical reproduction of the source example

For the five Monod kinetics in Table 1 of Alvarez-Latuz--Bayen--Coville and the cycle generator in their Section 4.2, the verification script in `artifacts/verify.py` obtains

| \(\varepsilon\) | \(\nu_c(\varepsilon)\) |
|---:|---:|
| 0.01 | 0.6435469795 |
| 0.5 | 0.4539126856 |
| 1 | 0.4206311213 |
| 5 | 0.3920724851 |
| 100 | 0.3855666041 |
| 10000 | 0.3852334198 |

The harmonic limit is \(0.3852300575\), explaining the approximately \(0.39\) limiting value reported in the source figure. The script also checks the symmetrization and strict substrate monotonicity on randomly generated reversible networks. These computations are diagnostics, not substitutes for the proof.

## Limitations

- The theorem requires the special growth-weighted form \(T(s)=LD(s)\), reversibility of \(L\), irreducibility, and strict increase of every \(\mu_i\). It does not resolve arbitrary substrate-dependent exchange matrices.
- No all-rate stability theorem for the coexistence equilibrium is claimed.
- Originality is to the best of our knowledge. The final journal record is identifiable as DOI `10.1016/j.nonrwa.2025.104509` / HAL `hal-04860652v2`, but the accessible full theorem text inspected for this review was the 2025 preprint; the final HAL v2 full text could not be inspected through the available route. A change between versions could therefore affect originality.
- The source paper says its Section 4.2 model is closely related to Lobry, *La compétition dans le chémostat* (2013), Section 4.2. The accessible record did not expose that section's text, so it remains the main uninspected historical source capable of affecting originality.
- The reversible-matrix symmetrization itself is standard in Markov-chain theory; the research claim is the all-rate chemostat threshold theorem and its application/generalization, not novelty of that algebraic device in isolation.

## References

1. C. Alvarez-Latuz, T. Bayen, J. Coville, *Global stability of perturbed chemostat systems*, arXiv:2501.08011; Nonlinear Analysis: Real World Applications 88 (2025), 104509. DOI: 10.1016/j.nonrwa.2025.104509. https://arxiv.org/abs/2501.08011
2. T. Bayen, H. Cazenave-Lacroutz, J. Coville, *Stability of the chemostat system with a mutation factor*, arXiv:2110.09582; Discrete and Continuous Dynamical Systems B 28 (2023), 2104--2129. https://arxiv.org/abs/2110.09582
3. L. Altenberg, *Resolvent positive linear operators exhibit the reduction phenomenon*, Proc. Natl. Acad. Sci. USA 109 (2012), 3705--3710. DOI: 10.1073/pnas.1113833109. https://pmc.ncbi.nlm.nih.gov/articles/PMC3309728/
4. C. Lobry, *La compétition dans le chémostat*, Hermann, 2013. (Section 4.2 is cited by reference 1 as closely related to its growth-weighted mutation example.)
