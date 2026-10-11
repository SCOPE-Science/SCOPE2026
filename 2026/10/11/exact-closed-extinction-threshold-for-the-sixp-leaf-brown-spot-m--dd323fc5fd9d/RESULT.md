# Exact closed extinction threshold for the SIXP leaf-brown-spot model
## Finding
Consider the printed four-compartment model
\[
\begin{{aligned}}
\dot S&=\kappa-(\pi+\mu)S+\delta P-(R_xX+R_cI)\frac{{S}}{{S+I}},\\
\dot I&=(R_xX+R_cI)\frac{{S}}{{S+I}}-cI,\\
\dot X&=\sigma I-\varepsilon X,\\
\dot P&=\pi S-(\delta+\mu)P,
\end{{aligned}}
\qquad c=\frac1i+\mu.
\]
Define
\[
R_0=\frac{{R_c+R_x\sigma/\varepsilon}}{{c}}
=\frac{{i(R_x\sigma+R_c\varepsilon)}}{{\varepsilon(1+\mu i)}}.
\]
For every nonnegative initial condition with \(S+I>0\), the pathogen-free equilibrium
\[
E_0=\left(\frac{{\kappa(\delta+\mu)}}{{\mu(\delta+\mu+\pi)}},0,0,
\frac{{\kappa\pi}}{{\mu(\delta+\mu+\pi)}}\right)
\]
is globally asymptotically stable exactly for \(R_0\le1\). For \(R_0>1\), it is unstable.

## Assumptions and scope
All parameters \(\kappa,\pi,\delta,\mu,R_x,R_c,\sigma,\varepsilon,i\) are strictly positive, and the standard-incidence term is the one printed in the source. Initial data satisfy \(S,I,X,P\ge0\) and \(S+I>0\). The result concerns the uncontrolled autonomous model only; it does not address the source's optimal-control system or the endemic equilibrium.

The denominator cannot collapse along such a solution. With \(Y=S+I\) and \(C=\max\{\pi+\mu,c\}\),
\[
\dot Y=\kappa-(\pi+\mu)S+\delta P-cI\ge\kappa-CY,
\]
so
\[
Y(t)\ge Y(0)e^{{-Ct}}+\frac{{\kappa}}C(1-e^{{-Ct}})>0.
\]
Also, with \(N=S+I+P\),
\[
\dot N=\kappa-\mu N-\frac Ii\le\kappa-\mu N,
\]
which bounds \(S,I,P\); then \(X\) is bounded by its scalar linear equation. Thus every forward orbit is precompact in the region where the vector field is smooth.

## Proof
Put \(\Lambda=R_xX+R_cI\) and define
\[
V=I+\frac{{R_x}}{{\varepsilon}}X.
\]
Direct differentiation, using \(cR_0=R_c+R_x\sigma/\varepsilon\), gives
\[
\begin{{aligned}}
\dot V
&=\Lambda\frac{{S}}{{S+I}}-cI
+\frac{{R_x}}{{\varepsilon}}(\sigma I-\varepsilon X)\\
&=-\frac{{\Lambda I}}{{S+I}}-c(1-R_0)I.
\end{{aligned}}
\]
Hence \(\dot V\le0\) whenever \(R_0\le1\). For either \(R_0<1\) or \(R_0=1\), equality along a trajectory forces \(I=0\). The largest invariant subset of \(\{I=0\}\) also has \(X=0\), because when \(I=0\) and \(S>0\),
\[
\dot I=R_xX,
\]
and \(S>0\) follows from the lower bound for \(S+I\). LaSalle's invariance principle on the compact closure of the forward orbit therefore gives \(I(t),X(t)\to0\).

On \(I=X=0\), the remaining subsystem is
\[
\binom{{\dot S}}{{\dot P}}
=\begin{{pmatrix}}-(\pi+\mu)&\delta\\ \pi&-(\delta+\mu)\end{{pmatrix}}
\binom{{S}}{{P}}+\binom{{\kappa}}{{0}}.
\]
Its matrix has trace \(-(\pi+\delta+2\mu)<0\) and determinant \(\mu(\pi+\delta+\mu)>0\), so it is Hurwitz and converges to the \(S,P\) coordinates of \(E_0\). This proves global attraction.

At \(R_0=1\), Lyapunov stability is also direct. Since \(V(t)\le V(0)\),
\[
0\le I(t)\le V(0),\qquad
0\le X(t)\le\frac{{\varepsilon}}{{R_x}}V(0).
\]
Writing \(z=(S-S_0,P-P_0)^T\), the \(S,P\) equations are the Hurwitz linear system above plus the forcing \((-\Lambda S/(S+I),0)^T\), whose norm is bounded by a constant times \(V(0)\). Variation of constants therefore keeps \(z(t)\) uniformly small whenever \(z(0)\) and \(V(0)\) are small. Thus \(E_0\) is Lyapunov stable at the critical value, completing global asymptotic stability for \(R_0\le1\).

For sharpness, the infected linear block at \(E_0\) is
\[
B=\begin{{pmatrix}}R_c-c&R_x\\ \sigma&-\varepsilon\end{{pmatrix}},
\qquad
\det B=\varepsilon c(1-R_0).
\]
If \(R_0>1\), then \(\det B<0\), so \(B\) has one positive real eigenvalue and the full equilibrium is unstable. Hence the closed threshold \(R_0\le1\) is exact.

## Verification
The accompanying `verify.py` symbolically checks the exact derivative identity, the infected-block determinant \(\varepsilon c(1-R_0)\), and the trace and determinant of the \(S,P\) block. Running the checker from the packaged file prints `VERIFY_OK`. The proof does not use finite-time simulation or numerical evidence.

## Relationship to prior work
Lertnaweephorn, Humphries and Khan formulate this exact SIXP model and state the local pathogen-free threshold \(R_0<1\). Their Theorem 2.2 is internally inconsistent: its displayed statement says \(R_0>1\), while the subsequent discussion says \(R_0<1\). More importantly, the displayed proof sets \(I=0\), \(X=0\) when introducing its Lyapunov function and later replaces \(X\) by \(\sigma I/\varepsilon\), which is an equilibrium relation rather than an identity along general transient solutions. The exact two-variable Lyapunov identity above avoids those restrictions and proves the full global statement, including the previously untreated critical case \(R_0=1\).

The 2021 predecessor by Lertnaweephorn and Humphries concerns the earlier SIX model without the protected compartment. Focused searches for the present four-state SIXP equations, the critical equality case, and the Lyapunov combination \(I+(R_x/\varepsilon)X\) found no source stating this closed global threshold. General epidemic threshold results do not by themselves supply the model-specific exact identity or the critical-case stability argument used here.

## Limitations
No claim is made about the global stability of the endemic equilibrium, uniqueness or rates of convergence beyond what is needed for asymptotic stability, or the controlled optimality system. The originality assessment is limited by the accessible indexed literature and by incomplete access to the full text of the 2021 predecessor; that predecessor has different state dimension and does not itself constitute same-system coverage.

## References
1. S. Lertnaweephorn, U. W. Humphries, A. Khan, “Stability analysis and optimal control for leaf brown spot disease of rice,” *AIMS Mathematics* 8 (2023), 9602–9623, DOI: 10.3934/math.2023485. Published 20 February 2023; MSC 34D20, 34D23.
2. S. Lertnaweephorn, U. Humphries, “A Mathematical Model for Leaf Brown Spot Disease of Rice with Standard Incidence Rate,” *Chiang Mai Journal of Science* 48 (2021), 931–941.
3. P. van den Driessche, J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” *Mathematical Biosciences* 180 (2002), 29–48.
