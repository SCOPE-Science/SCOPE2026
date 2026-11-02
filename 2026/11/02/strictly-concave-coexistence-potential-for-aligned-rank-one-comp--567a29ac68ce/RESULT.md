# Strictly concave coexistence potential for aligned rank-one competitive bivirus networks

## Finding

For the discrete-time competitive two-virus SIS system introduced by Gracy, Liu, Başar and Uribe, suppose the two infection matrices share the same strictly positive rank-one contact kernel but have different transmission intensities. With node-specific, strain-specific positive recovery rates, and provided the two normalized recovery profiles are linearly independent, **there is exactly one strictly positive coexistence equilibrium if and only if each strain can invade the other strain's single-virus equilibrium**. If either strict invasion condition fails, no strictly positive coexistence equilibrium exists. Whenever coexistence exists, its linearization has real strictly negative continuous-time eigenvalues, and the discrete equilibrium is locally exponentially attracting for every admissible physical Euler step. In particular, this class cannot exhibit two distinct positive coexistence equilibria or bistable, mutually noninvadable single-virus equilibria.

More precisely, let \(n\ge 2\), \(u_i,v_i,\beta_1,\beta_2,\delta_{i1},\delta_{i2}>0\), and set \(a_{i\ell}=u_i/\delta_{i\ell}\). Assume the columns of the \(n\)-by-\(2\) matrix \(a\) are linearly independent and \(R_\ell=\beta_\ell\sum_i v_i a_{i\ell}>1\) for \(\ell=1,2\). Define the uniquely determined positive single-virus forces \(c_\ell\) by

\[
\beta_\ell\sum_{i=1}^n\frac{v_i a_{i\ell}}{1+a_{i\ell}c_\ell}=1,
\]

and define the two cross-invasion numbers

\[
\mathcal I_{m\mid\ell}=\beta_m\sum_{i=1}^n\frac{v_i a_{im}}{1+a_{i\ell}c_\ell},\qquad m\ne\ell.
\]

Then an equilibrium with both viruses strictly positive at every node exists **if and only if** \(\mathcal I_{2\mid1}>1\) and \(\mathcal I_{1\mid2}>1\). It is unique. Its stability holds at every step size satisfying

\[
h>0,\qquad h\left(\delta_{i\ell}+u_i(\beta_1+\beta_2)\sum_jv_j\right)\le1\quad\text{for every }i,\ell.
\]

## Assumptions and scope

The state consists of \(x_{i\ell}\), the fraction of node \(i\) infected with virus \(\ell\), with \(x_{i\ell}\ge0\) and \(x_{i1}+x_{i2}\le1\). At each synchronous update,

\[
x_{i\ell}^{+}=x_{i\ell}+h\left[-\delta_{i\ell}x_{i\ell}+(1-x_{i1}-x_{i2})\,\beta_\ell u_i\sum_{j=1}^n v_jx_{j\ell}\right].
\]

The two strictly positive infection matrices are \(B^\ell=\beta_\ell uv^{\mathsf T}\); identical contact *pattern* does not require identical transmission intensity or recovery. The physical step condition above ensures the standard state simplex is forward invariant. Normalizations of \(u,v,\beta_\ell\) that preserve both \(B^\ell\) do not alter the equilibria or the invasion conditions. The theorem concerns **interior equilibrium existence, uniqueness, and local asymptotic stability**, not global convergence or the basin boundaries. The rank-two condition on the two recovery-adjusted contact columns excludes precisely the aligned proportional-degeneracy case for which a neutral continuum may occur.

## Proof

**1. Reduction to a two-variable force-of-infection system.** Write \(C_\ell=\beta_\ell\sum_j v_jx_{j\ell}\) and \(s_i=1-x_{i1}-x_{i2}\). At an interior equilibrium \(C_\ell>0\), and the stationarity equations imply

\[
x_{i\ell}=s_i a_{i\ell}C_\ell,\qquad
s_i=\frac1{1+a_{i1}C_1+a_{i2}C_2}.
\]

Consequently, both force-consistency equations are

\[
\frac1{\beta_\ell}=\sum_i\frac{v_i a_{i\ell}}{1+a_{i1}C_1+a_{i2}C_2},\qquad\ell=1,2.
\]

Conversely, any solution \((C_1,C_2)\in(0,\infty)^2\) gives one physical strictly interior equilibrium by the displayed formulas. No additional boundary solutions are counted as coexistence.

**2. Strict concavity and the exact invasion test.** On the closed quadrant define

\[
\Phi(C_1,C_2)=\sum_i v_i\log(1+a_{i1}C_1+a_{i2}C_2)-\frac{C_1}{\beta_1}-\frac{C_2}{\beta_2}.
\]

Its gradient is exactly the pair of consistency residuals. Its Hessian is

\[
\nabla^2\Phi(C)=-\sum_i\frac{v_i}{(1+a_{i1}C_1+a_{i2}C_2)^2}\,a_i a_i^{\mathsf T},\quad a_i=(a_{i1},a_{i2})^{\mathsf T}.
\]

Because the columns of \(a\) are independent and all \(v_i>0\), this Hessian is negative definite throughout the quadrant. Also \(\Phi(C)\to-\infty\) as \(\|C\|\to\infty\) in that quadrant, since the negative linear terms dominate logarithmic growth. Thus there is one unique constrained maximizer. The origin is not the maximizer because \(\partial_\ell\Phi(0)=(R_\ell-1)/\beta_\ell>0\).

On the virus-\(\ell\)-only axis, strict concavity and \(R_\ell>1\) give the unique maximizer \(c_\ell\) defined above. The inward derivative at this point is

\[
\left.\partial_m\Phi\right|_{C_\ell=c_\ell,\,C_m=0}=\frac{\mathcal I_{m\mid\ell}-1}{\beta_m}.
\]

By the necessary **and sufficient** first-order condition for maximization of a concave differentiable function on the quadrant, an axis maximizer is also the global maximizer exactly when this inward derivative is nonpositive. Hence the global maximizer is interior precisely when **both** inward derivatives are strictly positive. In the interior, its vanishing gradient gives the unique coexistence equilibrium. If either derivative is zero, the maximizer remains on that axis and interior coexistence does not exist. The same argument rules out simultaneous nonpositive inward derivatives at distinct axes: strict concavity permits only one maximizer.

**3. Negative definite symmetrization of the Jacobian.** Let \(J\) be the continuous-time Jacobian, i.e. the Jacobian of the vector field inside the square brackets, at coexistence. For the index pairs \((i,\ell),(j,m)\),

\[
J_{i\ell,jm}= -\delta_{i\ell}\mathbf1_{i=j,\ell=m}+s_i\beta_\ell u_iv_j\mathbf1_{\ell=m}-u_iC_\ell\mathbf1_{i=j}.
\]

Define the positive diagonal matrix \(W\) with \(W_{i\ell,i\ell}=v_i/(s_i u_iC_\ell)\). Direct substitution shows \(WJ=(WJ)^{\mathsf T}\). Moreover for every real perturbation vector \(z\),

\[
\begin{aligned}
z^{\mathsf T}WJz
={}&\sum_{\ell=1}^2\frac1{C_\ell}\left[\beta_\ell\left(\sum_i v_iz_{i\ell}\right)^2-\sum_i\frac{v_i\delta_{i\ell}}{s_iu_i}z_{i\ell}^2\right]\\
&-\sum_i\frac{v_i}{s_i}(z_{i1}+z_{i2})^2.
\end{aligned}
\]

The force-consistency equations imply \(\beta_\ell\sum_i v_i s_i u_i/\delta_{i\ell}=1\). Weighted Cauchy–Schwarz therefore makes each bracket nonpositive; equality for a fixed \(\ell\) requires \(z_{i\ell}=t_\ell s_i a_{i\ell}\) at all nodes. Equality in the final negative sum simultaneously demands \(t_1a_{i1}+t_2a_{i2}=0\) for all \(i\). Column independence forces \(t_1=t_2=0\). Thus \(WJ\) is strictly negative definite. Because \(W^{1/2}JW^{-1/2}\) is symmetric negative definite, **all** eigenvalues of \(J\) are real and strictly negative.

**4. Every physically admissible Euler step is stable.** Let \(P\) be diagonal with entries \(+1\) for virus one and \(-1\) for virus two. All off-diagonal entries of \(PJP\) are nonnegative: same-strain infection coupling is positive, and negative cross-strain susceptibility coupling has its sign reversed. Furthermore, by the step condition and \(C_\ell\le\beta_\ell\sum_jv_j\), every diagonal entry of \(P(I+hJ)P\) is nonnegative. This is therefore a nonnegative matrix. Its real Perron eigenvalue is its spectral radius, and because it differs from \(PJP\) only by the identity shift, its spectral radius is \(1+h\,s(J)\), where \(s(J)=\max\{\Re\lambda:\lambda\in\operatorname{spec}(J)\}<0\). Thus its spectral radius is strictly less than one, so every multiplier of the discrete Jacobian \(I+hJ\) lies strictly inside the unit disk. Standard discrete linearization yields local exponential asymptotic stability.

## Verification

A particularly transparent rational example has \(n=2\), \(u=v=(1,1)^{\mathsf T}\), \(\beta_1=\beta_2=1\), and recovery matrix \((\delta_{i\ell})=\begin{psmallmatrix}1&4\\4&1\end{psmallmatrix}\), with \(h=1/16\). The unique coexistence solution is

\[
C_1=C_2=\frac15,\quad (s_1,s_2)=\left(\frac45,\frac45\right),\quad
(x_{i\ell})=\begin{pmatrix}4/25&1/25\\1/25&4/25\end{pmatrix}.
\]

The two single-virus forces equal \(c_1=c_2=(\sqrt{13}-3)/2\). Both cross-invasion numbers equal \((27-5\sqrt{13})/8>1\). The continuous-time Jacobian has the four eigenvalues \(-19/10\pm3\sqrt{29}/10\) and \(-19/10\pm\sqrt{13}/2\), which are strictly negative; the discrete multipliers are \(1+\lambda/16\). The strict step bound is satisfied (in fact \(h(4+4)=1/2\)).

Reproduce independent exact-equation and numerical checks with `python verify.py` after installing the two dependencies in `requirements.txt`. The script checks the equilibrium reconstruction, the Jacobian symmetrization, its negative spectrum, the discrete multipliers, both invasion factors, and a seeded collection of other full-rank positive configurations. The script is supporting finite evidence; steps 1–4 are the arbitrary-parameter proof.

## Relationship to prior work

Gracy, Liu, Başar and Uribe (arXiv:2310.13853v1, 2023-10-20) define the discrete competitive bivirus SIS model and give general equilibrium stability, exclusion, and coexistence conditions. Their network model permits more complicated coexistence behavior and does not derive this all-dimensions strict-concavity reduction for common positive rank-one contacts. Ye, Anderson and Liu (arXiv:2111.07507v1) analyze equilibria of continuous-time general networked bivirus SIS models, including degenerate continuous families and examples beyond rank one; the degeneracy is excluded here by column independence. Anderson and Ye (arXiv:2210.11044) analyze equilibrium-count questions via Poincaré–Hopf and manifold methods for general matrices; those results do not supply the exact two-sided invasion criterion here. Doshi, Hu and Eun (arXiv:2209.07304) prove coexistence/stability results with different homogeneity assumptions and do not imply the node-heterogeneous rank-one result. These comparisons do not rule out every equivalent result elsewhere.

## Limitations

The strict rank-two assumption on \((a_{i\ell})\) is necessary for the proof of uniqueness and strict decay; proportional recovery-adjusted profiles may support a neutral continuum. The positivity of both contact vectors and recovery parameters, as well as both single-virus reproduction numbers exceeding one, are substantive hypotheses. Outside the stated Euler step range, discrete local stability is not asserted. No global convergence, resilience-to-noise, or multiple-strain extension is proved. The finite numerical checks are not a proof of absence of unindexed prior literature. Independent validation has not been performed.

## References

1. Gracy, Liu, Başar and Uribe, *A Discrete-time Networked Competitive Bivirus SIS Model*, arXiv:2310.13853v1 (first public 2023-10-20). https://arxiv.org/abs/2310.13853
2. Ye, Anderson and Liu, *Convergence and Equilibria Analysis of a Networked Bivirus Epidemic Model*, arXiv:2111.07507 (2021). https://arxiv.org/abs/2111.07507
3. Anderson and Ye, *Equilibria Analysis of a Networked Bivirus Epidemic Model Using Poincaré–Hopf and Manifold Theory*, arXiv:2210.11044 (2022). https://arxiv.org/abs/2210.11044
4. Doshi, Hu and Eun, *Bi-SIS Epidemics on Graphs — Quantitative Analysis of Coexistence Equilibria*, arXiv:2209.07304 (2022). https://arxiv.org/abs/2209.07304
