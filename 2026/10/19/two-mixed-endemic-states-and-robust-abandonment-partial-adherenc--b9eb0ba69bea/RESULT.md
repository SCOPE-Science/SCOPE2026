# Two mixed endemic states and robust abandonment–partial-adherence bistability

## Finding

For the coupled SIRS–replicator model defined below, there are **at most two distinct stationary states with both positive infection and strictly mixed adherence**. This is a sharp bound. A fully rational parameter choice attains it and has precisely two locally attracting endemic states, one with no adherence and the other with strictly partial adherence. A third endemic state, with smaller but positive adherence, is a hyperbolic saddle separating these alternative outcomes locally. This yields coexistence of intervention abandonment and sustained partial protection, rather than the abandonment–universal-protection bistability illustrated in earlier parameter studies.

Specifically, for the parameters given in the assumptions, the only two mixed endemic adherence fractions are
\[
 x_{\pm}=\frac{409\pm\sqrt{109681}}{2880},
 \qquad 0.027<x_-<0.028,\qquad 0.257<x_+<0.258.
\]
The lower state is a saddle and the upper state a locally asymptotically stable equilibrium. The no-adherence endemic equilibrium is also locally asymptotically stable. All three endemic states are hyperbolic, so their existence and stability persist under sufficiently small simultaneous perturbations of the parameters.

## Assumptions and scope

Let \(S,I,R\geq0\), \(S+I+R=1\), and \(x\in[0,1]\) be respectively susceptible, infectious, recovered, and adherence fractions. Dynamics on the invariant simplex are
\[
\begin{aligned}
 \dot S&=\mu-\beta b(x)SI+\delta(1-S-I)-\mu S,\\
 \dot I&=\beta b(x)SI-(\gamma+\mu)I,\\
 \dot x&=\varepsilon x(1-x)\alpha(x,I),
\end{aligned}
\]
where
\[
 b(x)=(1-ax)(1-ex),\qquad
 \alpha(x,I)=-c+a\xi\beta I(1-ex)+\kappa(2x-1).
\]
Here \(\mu,\delta,\gamma,\beta,c,\xi,\varepsilon>0\), \(a,e\in[0,1]\), and \(\kappa\geq0\). By a *mixed endemic state* we mean an equilibrium with \(I>0\) and \(0<x<1\). The count bound holds for every such parameter set, including the degenerate cases \(a=0\), \(e=0\), and \(a=1\). It counts distinct states and does not assert all are stable.

For the sharp example, all numbers are exact rationals:
\[
(\mu,\delta,\gamma,\beta,a,e,\xi,c,\kappa,\varepsilon)
=\left(\frac1{10},\frac9{10},1,\frac{33}{10},\frac9{10},\frac1{10},\frac{800}{297},\frac{503}{300},1,\frac1{100}\right).
\]
Set \(\rho=\beta/(\gamma+\mu)\) and \(K=(\mu+\delta)/(\mu+\delta+\gamma)\). For this example \(\rho=3\), \(K=1/2\). All epidemic parameters are positive and all behavioral efficacy parameters lie strictly between zero and one.

## Proof

**1. Reduction and universal bound.** At any endemic equilibrium, the infection equation forces \(\beta b(x)S=\gamma+\mu\), and the recovered-state balance gives \(R=\gamma I/(\mu+\delta)\). Hence
\[
 S=\frac{1}{\rho b(x)},\qquad
 I=E(x):=K\left(1-\frac1{\rho b(x)}\right),\qquad \rho b(x)>1.
\]
The mixed behavioral equation is equivalent to \(G(x):=\alpha(x,E(x))=0\). If \(a>0\), cancellation of \(1-ex\) yields on the endemic domain
\[
 G(x)=-c-\kappa+2\kappa x+a\xi\beta K
 \left(1-ex-\frac1{\rho(1-ax)}\right).
\]
Because \(\rho b(x)>1\), necessarily \(1-ax>0\). Multiplying by this strictly positive factor gives the quadratic polynomial identity
\[
 (1-ax)G(x)=(A_0+B_0x)(1-ax)-\frac{P}{\rho},
 \quad P=a\xi\beta K,
 \quad A_0=-c-\kappa+P,
 \quad B_0=2\kappa-eP.
\]
When \(a>0\), the quadratic coefficient is \(-aB_0\), which may vanish; nevertheless this is always a polynomial of degree at most two. A nonzero polynomial of degree at most two has at most two roots. It cannot vanish identically: if \(B_0=0\), its linear coefficient is \(-aA_0\); vanishing also requires \(A_0=0\), which would leave the nonzero constant \(-P/\rho\). If \(a=0\), then \(G(x)=-c+\kappa(2x-1)\) is affine and has at most one root (or none). Thus there are at most two mixed endemic states for every admissible parameter choice. Distinct \(x\) determine distinct endemic \((S,I,x)\).

**2. Exact sharp witness.** Substitution of the rational parameters into the endemic feedback gives
\[
 G(x)=\frac{1440x^2-409x+10}{100(9x-10)}.
\]
The discriminant of the numerator is \(109681\), so its two simple roots are the displayed \(x_\pm\). Rational sign certificates are
\[
\begin{array}{c|rrrr}
 x&27/1000&28/1000&257/1000&258/1000\\\hline
 1440x^2-409x+10&169/25000&-2019/6250&-61/25000&4127/12500
\end{array}
\]
(the signs alone are also sufficient). Both roots lie below \(13/50\), where \(b(x)>7/10\) and \(\rho b(x)>21/10>1\), so they give genuine positive-infection equilibria with \(I>1/4\). At each, \(S=1/[3b(x)]\), \(I=(1-1/[3b(x)])/2\), and \(R=I\). Also \(G(0)=-1/100<0\), and the no-adherence endemic equilibrium is \((S,I,x)=(1/3,1/3,0)\).

**3. Stability at the mixed states.** Write \(C=\beta bI\), \(A=\mu+\delta+C=1+C\), \(B=\delta+\gamma+\mu=2\), and set
\[
 h=\varepsilon x(1-x),\quad
 u=-\beta b'(x)SI>0,\quad
 v=h a\xi\beta(1-ex)>0,\quad
 w=h(2\kappa-ae\xi\beta I).
\]
At either mixed equilibrium the Jacobian is
\[
 J=\begin{pmatrix}-A&-B&u\\ C&0&-u\\0&v&w\end{pmatrix}.
\]
Its characteristic polynomial \(\lambda^3+C_1\lambda^2+C_2\lambda+C_3\) satisfies
\[
\begin{aligned}
 C_1&=A-w,\\ C_2&=BC-Aw+uv,\\
 C_3&=(\mu+\delta)uv-BCw=-BC hG'(x),\\
 C_1C_2-C_3&=ABC-A^2w+Aw^2+uv(C-w).
\end{aligned}
\]
For \(0<x<13/50\) at these equilibria, \(I>1/4\), \(b>7/10\), and therefore
\[
 \frac{231}{400}<C\le\frac{33}{20},\qquad
 1<A\le\frac{53}{20},\qquad
 0<w\le\frac1{200}<C.
\]
Indeed \(ae\xi\beta=4/5\), so \(w>0\), and \(h\le1/400\) gives the asserted upper bound. It follows immediately that \(C_1>0\), \(C_2>0\), and
\[
 C_1C_2-C_3>
 2\frac{231}{400}-\left(\frac{53}{20}\right)^2\frac1{200}>0.
\]
Because the denominator \(100(9x-10)\) is negative, the lower numerator root has \(G'(x_-) >0\), while the upper has \(G'(x_+)<0\). Hence \(C_3<0\) at \(x_-\), giving exactly one eigenvalue with positive real part by Routh's sign criterion; it is a hyperbolic saddle. At \(x_+\), all four strict cubic Routh–Hurwitz inequalities hold, so it is a hyperbolic sink.

**4. The abandonment endemic state and robustness.** At \(x=0\), the endemic SIRS two-dimensional subsystem has negative trace \(-[\mu+\delta+\beta I]\) and determinant \((\delta+\gamma+\mu)\beta I>0\). The transverse behavioral eigenvalue is \(\varepsilon G(0)=-1/10000<0\), so \((1/3,1/3,0)\) is a hyperbolic sink. These three endemic states remain in the admissible region, with the same local types, under sufficiently small simultaneous perturbations of the parameters by continuity and the implicit-function theorem. The exact existence of two mixed equilibria, together with the universal two-root bound, excludes any additional mixed endemic stationary state in the perturbed regime.

## Verification

The standalone file `check.py` verifies by exact SymPy rational arithmetic the feedback-function identity, discriminant and rational root brackets, the endemic-domain inequalities, the characteristic-coefficient formulas and \(C_3=-BChG'\), and the strict Routh–Hurwitz bounds. Execute `python check.py` with Python 3.10+ and SymPy installed. The analytical argument above proves the universal claim; finite computations only reproduce its algebraic certificates. For reference, the mixed adherence fractions are approximately \(0.0270204099742\) and \(0.257007367804\), with corresponding prevalences \(0.328716436127\) and \(0.277462481588\).

## Relationship to prior work

Kumata, Ito, and Yamamichi (arXiv:2610.12519v1, posted 7 October 2026) introduce the very same private-protection/source-control/conformity SIRS model, write its endemic feedback function and a general Jacobian, and numerically describe stable partial adherence, periodic solutions, abandonment–full-adherence bistability, and partial–full-adherence coexistence. Those constructions and the reduced equilibrium formulas are prior work, not claimed new. Their main discussion, figure classifications, and supplementary derivations do not give an attained **universal bound of two mixed endemic stationary states** or a certified coexistence of stable **no-adherence endemic** and stable **partially adherent endemic** states. The present contribution is the sharp algebraic bound plus exact rational three-endemic-state realization with rigorously assigned local stability types.

Saad-Roy and Traulsen (2023) analyze the earlier adherence-coupled SIRS model without this product protection and conformity combination. Their full text does not contain the above sharp mixed-state multiplicity/concurrent-sink witness. Other epidemic–behavior and evolutionary feedback models can exhibit bistability, so bistability alone is not claimed new.

## Limitations

The claim concerns deterministic homogeneous-mixing mean-field dynamics and local stability. It does not establish global basin geometry, transition probabilities for finite stochastic populations, empirical efficacy of any intervention, or invariance under arbitrary model modifications. The witness uses a small behavioral-update rate, \(\varepsilon=1/100\), although the two-interior-state count is independent of that rate. The motivating preprint supplies nearly all the general equilibrium/Jacobian formulas; the novelty is the particular complete quantitative conclusion and phenomenon, not a new modeling framework. Work containing an equivalent unindexed multiplicity theorem remains a bibliographic risk; there has been no independent audit.

## References

1. R. Kumata, H. Ito, and M. Yamamichi, *Voluntary nonpharmaceutical intervention as a feedback-evolving game*, arXiv:2610.12519v1 (7 October 2026), https://arxiv.org/html/2610.12519v1. Examined main text, model equations, figures and supporting sections S1–S4.
2. C. M. Saad-Roy and A. Traulsen, *Dynamics in a behavioral–epidemiological model for individual adherence to a nonpharmaceutical intervention*, PNAS **120** (2023), e2311584120, https://doi.org/10.1073/pnas.2311584120. Examined full text.
3. A. Martin, H. Castella, and F. Hamelin, *Wearing face masks to protect oneself and/or others*, Journal of Theoretical Biology (2026), https://doi.org/10.1016/j.jtbi.2026.112395. Abstract consulted; full text not examined.
