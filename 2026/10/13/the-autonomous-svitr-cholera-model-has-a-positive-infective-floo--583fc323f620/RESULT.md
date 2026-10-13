# The autonomous SVITR cholera model has a positive infective floor
## Finding
For the autonomous SVITR system printed as model (2.1) by Tirfe et al., suppose \(\Pi>0\), \(\mu>0\), \(\alpha>0\), \(\eta>0\), \(0<p<1\), and all remaining rates are nonnegative. Define
\[
h=\omega+\mu+\xi,
\qquad
V_\infty=\frac{\alpha\Pi}{\eta+\mu}.
\]
Then every nonnegative solution for which the standard-incidence term is defined obeys
\[
\liminf_{{t\to\infty}} I(t)
\ge
\frac{{(1-p)\eta\alpha\Pi}}{{(\eta+\mu)(\omega+\mu+\xi)}}
>0.
\]
In particular, every equilibrium has strictly positive infectious coordinate. Hence the point called the cholera-free equilibrium in the source is not an equilibrium of its printed autonomous system under these assumptions. Threshold, local/global stability, and transcritical-bifurcation conclusions that are evaluated at that point therefore do not apply to model (2.1) on this parameter domain.

## Assumptions and scope
The printed equations used here are
\[
V'=\alpha\Pi-(\eta+\mu)V,
\]
\[
I'=\frac{{\beta I}}{{N}}S+(1-p)\eta V-(\omega+\mu+\xi)I.
\]
The claim assumes \(N(t)>0\) wherever \(\beta I/N\) is evaluated. The source states \(p\in(0,1)\) and nonnegative model parameters; the result additionally isolates the nondegenerate vaccination regime \(\alpha\Pi\eta>0\) and \(\mu>0\). No assertion is made for the degenerate cases \(p=1\), \(\alpha=0\), \(\Pi=0\), or \(\eta=0\).

## Proof
The vaccinated equation is autonomous and linear, so
\[
V(t)=V_\infty+\bigl(V(0)-V_\infty\bigr)e^{-(\eta+\mu)t},
\qquad
V_\infty=\frac{{\alpha\Pi}}{{\eta+\mu}}>0.
\]
Because \(\beta IS/N\ge0\) for nonnegative states, the infectious equation gives
\[
I'+hI\ge (1-p)\eta V,
\qquad h=\omega+\mu+\xi>0.
\]
Multiplying by \(e^{ht}\) and integrating yields
\[
I(t)\ge e^{-ht}I(0)+(1-p)\eta
\int_0^t e^{-h(t-s)}V(s)\,ds.
\]
The exponentially weighted convolution on the right converges to \(V_\infty/h\), because \(V(s)\to V_\infty\). Therefore
\[
\liminf_{{t\to\infty}}I(t)
\ge\frac{{(1-p)\eta V_\infty}}{h}
=\frac{{(1-p)\eta\alpha\Pi}}{{(\eta+\mu)(\omega+\mu+\xi)}}>0.
\]
At any equilibrium the same conclusion follows directly: \(V^*=V_\infty\), and
\[
0=\frac{{\beta I^*}}{{N^*}}S^*+(1-p)\eta V^*-hI^*
\]
implies
\[
I^*\ge\frac{{(1-p)\eta V_\infty}}{h}>0.
\]
Thus an equilibrium with \(I^*=0\) cannot exist. The source's proposed \(E_0\) sets \(I=T=R=0\) while retaining \(V_0=\alpha\Pi/(\eta+\mu)\); substituting it into the printed infectious equation leaves the strictly positive residual \((1-p)\eta V_0\).

## Verification
The bundled `verify.py` evaluates the residual and infective floor with exact rational arithmetic for a nondegenerate admissible parameter witness. The general result itself is analytic: it uses the explicit solution of the vaccinated linear equation, positivity of the incidence contribution, and one scalar comparison inequality. No finite computation is used to infer the quantified asymptotic statement.

The source full text was inspected at the model formulation, equation (2.1), the cholera-free equilibrium construction, the next-generation calculation, and the local/global cholera-free stability sections. It explicitly prints the \((1-p)\eta V\) inflow in \(I'\), then drops that equation when solving for the cholera-free point. The standard next-generation framework of van den Driessche and Watmough assumes the disease-free subspace is invariant, excluding density-independent inflow into infected compartments.

## Relationship to prior work
Tirfe et al. introduce the five-compartment SVITR model and state a cholera-free equilibrium, a reproduction-number threshold, local and global stability of that equilibrium, and a bifurcation analysis. The present finding does not rederive those calculations; it identifies a structural obstruction in the printed vector field and strengthens it to a uniform asymptotic lower bound on the infectious compartment.

Van den Driessche and Watmough's next-generation construction explicitly assumes that disease-free states remain disease free, equivalently that there is no density-independent immigration into infected compartments. The printed SVITR term \((1-p)\eta V\) violates that premise whenever \(V>0\). Ezeagu, Togbenon, and Moyo provide a related cholera-vaccination model in which vaccination moves susceptible individuals toward immunity rather than supplying an autonomous positive inflow into infection; that model therefore does not imply the present obstruction.

## Limitations
The result concerns the autonomous system exactly as printed. It does not decide existence, uniqueness, or stability of the model's positive equilibrium, and it does not assess the optimal-control system after controls alter the equations. If the intended vaccinated-to-infectious flow was meant to depend on infectious exposure, or if one imposes \(p=1\), \(\alpha=0\), or \(\eta=0\), the obstruction disappears and the threshold analysis must be derived for that modified system rather than inherited from the printed one.

## References
1. T. L. Tirfe, L. L. Obsu, E. D. Gurmu, A. B. Celestine, and Shyamsunder, “Optimal Control and Bifurcation Analysis of Cholera Model,” *Journal of Prime Research in Mathematics*, Special Issue (2026), 1–28. Published online 2026-03-06. https://jprm.sms.edu.pk/index.php/jprm/article/view/279
2. P. van den Driessche and J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” *Mathematical Biosciences* 180 (2002), 29–48. DOI: 10.1016/S0025-5564(02)00108-6.
3. N. J. Ezeagu, H. A. Togbenon, and E. Moyo, “Modeling and Analysis of Cholera Dynamics with Vaccination,” *American Journal of Applied Mathematics and Statistics* 7(1) (2019), 1–8. DOI: 10.12691/ajams-7-1-1.
