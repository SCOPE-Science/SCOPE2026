# An attracting endemic oscillation from finite opinion-response time in a homogeneous nonlinear-opinion SIS model

## Finding

The homogeneous, unforced nonlinear-opinion SIS (NOD-SIS) system of Ordorica Arango, Bizyaeva, Levin and Leonard admits a **nondegenerate supercritical Hopf bifurcation at an interior risk-averse endemic equilibrium**, even with just one well-mixed population. In particular, fix
\[
\bar\beta=k_p=k_x=\frac34,\qquad \delta=\frac3{16},\qquad u_0=\log 3-\frac9{16},
\]
and vary the positive opinion-response timescale \(\tau\). The equilibrium \((p_*,x_*)=(1/2,-1/2)\) is present for all \(\tau>0\). Set
\[
H=\frac34\log 3-\frac{23}{32},\qquad
\tau_H=\frac{16H}{3}=4\log 3-\frac{23}{6}=0.5611158213\ldots.
\]
For \(\tau>\tau_H\), this equilibrium is locally exponentially attracting; for \(0<\tau<\tau_H\), it is linearly unstable. At \(\tau=\tau_H\) its linear spectrum is \(\{\pm i\omega\}\), with
\[
\omega^2=\frac{9(4-3\log 3)}{32(24\log 3-23)}>0.
\]
There is \(\varepsilon>0\) such that **every** \(\tau\in(\tau_H-\varepsilon,\tau_H)\) admits a small, locally orbitally asymptotically stable periodic solution in the biological interior \(0<p<1\), \(-1<x<0\). Its amplitude tends to zero and its frequency tends to \(\omega\) as \(\tau\nearrow\tau_H\). This establishes endogenous attracting oscillations without opinion delays, external forcing, or population heterogeneity.

## Assumptions and scope

The state is infection prevalence \(p\in[0,1]\) and risk-seeking/risk-averse opinion \(x\in[-1,1]\), evolving in physical time by
\[
\begin{aligned}
\dot p&=\bar\beta(1+x)(1-p)p-\delta p,\\
\tau\dot x&=-x+\tanh\!\big((k_p p+k_xx^2+u_0)x\big).
\end{aligned}
\]
The coefficients are exactly as in the Finding, with \(\tau>0\). All positive parameters are in their source-model admissible ranges: in particular \(0<u_0<1\), \(k_p+u_0>1\), and \(\bar\beta,\delta,k_p,k_x\in(0,1)\). The model is the single-population, unconstrained, continuous-time NOD-SIS system, not a multi-population or filtered-prevalence surrogate. The Hopf conclusion is local near one specified equilibrium and one critical timescale.

## Proof

**Equilibrium and linear crossing.** At \((p_*,x_*)=(1/2,-1/2)\), the transmission gain is \(\bar\beta(1+x_*)=3/8\), balancing recovery \(\delta=3/16\). The opinion argument is \(-\frac12\log3\), whose hyperbolic tangent equals \(-1/2\). Consequently this point is an equilibrium for every \(\tau\). Differentiation gives
\[
J(\tau)=\begin{pmatrix}-3/16&3/16\\-9/(32\tau)&H/\tau\end{pmatrix},\qquad H=\frac34\log3-\frac{23}{32}.
\]
The positive bounds \(0<H<9/32\) follow, for example, from \(1.0986<\log3<1.0987\). Thus
\[
\operatorname{tr}J=-\frac3{16}+\frac H\tau,\qquad
\det J=\frac{3}{16\tau}\left(\frac9{32}-H\right)>0.
\]
The unique zero of the trace occurs at \(\tau_H=16H/3\). It gives the stated \(\omega\), and the real-part crossing derivative is
\[
\left.\frac{d\operatorname{Re}\lambda}{d\tau}\right|_{\tau_H}
=-\frac{H}{2\tau_H^2}<0.
\]
The trace and determinant criteria yield the stated local stability away from the crossing.

**Nonlinear criticality.** Write \(a=3/16\), \(L=\log3\), and make the invertible linear change at the crossing
\[
X=p-\frac12,\qquad Y=\frac a\omega\left(p-\frac12-(x+\frac12)\right).
\]
Then the linearization has canonical form \(\dot X=-\omega Y\), \(\dot Y=\omega X\). Denote the nonlinear parts of these two transformed equations by \(f(X,Y)\) and \(g(X,Y)\), whose value and first derivatives vanish at the origin. The planar first Lyapunov coefficient in this normalization is
\[
\ell_1=\frac{f_{XXX}+f_{XYY}+g_{XXY}+g_{YYY}}{16}
+\frac{f_{XY}(f_{XX}+f_{YY})-g_{XY}(g_{XX}+g_{YY})-f_{XX}g_{XX}+f_{YY}g_{YY}}{16\omega},
\]
all derivatives evaluated at \((0,0)\). Exact differentiation and simplification, with the square of \(\omega\) substituted from the characteristic equation, give
\[
\boxed{\ell_1=\frac{27\big(1728L^4-4080L^3+17171L^2-34432L+21696\big)}{4096(3L-4)(24L-23)^2}}.
\]
The numerator quartic \(P(L)\) is positive. Indeed, with \(z=L-11/10\),
\[
P(11/10+z)=1728z^4+\frac{17616}{5}z^3+\frac{406307}{25}z^2-\frac{283291}{125}z+\frac{4242987}{2500}.
\]
Using \(-14/10000<z<-13/10000\), we can discard its nonnegative even-degree terms and bound the remaining terms to obtain
\[
P(L)>\frac{4242987}{2500}+\frac{283291}{125}\frac{13}{10000}-\frac{17616}{5}\left(\frac{14}{10000}\right)^3>1700.
\]
The rational enclosure of \(\log3\) used here is certified by the positive series \(\log3=2\sum_{j\ge0}[2^{-(2j+1)}(2j+1)^{-1}]\) and a geometric remainder bound, reproduced in the executable checker. Because \(3L-4<0\) and \(24L-23>0\), the displayed coefficient satisfies \(\ell_1<0\) (numerically \(-1.4043220562\ldots\)).

The planar nondegenerate Hopf theorem applies: the eigenvalues cross transversely and \(\ell_1<0\). Since the equilibrium becomes unstable when \(\tau\) decreases through \(\tau_H\), an attracting periodic orbit exists for every sufficiently small positive \(\tau_H-\tau\). Because it bifurcates from the interior point \((1/2,-1/2)\), the orbit lies entirely in \(0<p<1\), \(-1<x<0\) when sufficiently small. This proves the claim.

## Verification

Run `python verification/check_hopf.py` from the package root after installing the `verification/requirements.txt` dependency. The standalone script computes the second- and third-derivative tensors of both original vector-field components, transforms them to canonical Hopf coordinates, and derives the Lyapunov coefficient using exact symbolic arithmetic. It asserts equality with the displayed rational function of \(\log3\), checks the exact Jacobian determinant and trace crossing, proves the elementary logarithm and quartic sign bounds with rational arithmetic, and checks admissible parameter ranges. No numerical finite-time simulation is used to establish the existence or stability of periodic orbits. Approximate numbers are for presentation only.

## Relationship to prior work

The NOD-SIS model and its biological state space are exactly the single-population equations (2)–(3) of Ordorica Arango et al. (2024), Sections III–IV. That work proves equilibrium and threshold results and investigates strong peer pressure, but its examined text does not contain a supercritical Hopf theorem or an attracting cycle for a homogeneous risk-averse population. The earlier actSIS filtered-infection-feedback model of Zhou, Levin and Leonard (2020) produces oscillations for heterogeneous behavioral responses with a different nonlinear feedback law and state variable; it does not imply this claim. The network SIS risk-aversion formulation of Bizyaeva et al. (2023) and the distributed opinion-density model of Götz et al. (2024) likewise have nonidentical dynamics. The present theorem is an explicit parameter-certified phenomenon in the original homogeneous NOD-SIS equations rather than an assertion that oscillations have never been studied in behavior–epidemic models.

## Limitations

The result proves local Hopf bifurcation and existence of an attracting small cycle, not uniqueness or global stability of periodic solutions. It applies to the specific admissible parameter slice and an open one-sided interval of opinion-response timescales, without providing a numerical value for the interval width. Other equilibria may coexist. Bibliographic priority remains subject to independent review; the present source comparison is not an exhaustive proof of novelty. No external or independent validation has been performed.

## References

1. Marcela Ordorica Arango, Anastasia Bizyaeva, Simon A. Levin, and Naomi Ehrich Leonard, *Opinion-driven risk perception and reaction in SIS epidemics*, arXiv:2410.12993v1 (first public release 2024-10-16), https://arxiv.org/html/2410.12993v1 .
2. J. Zhou, S. A. Levin, and N. E. Leonard, *Active Control and Sustained Oscillations in actSIS Epidemic Dynamics*, arXiv:2007.01424 (2020), https://arxiv.org/abs/2007.01424 .
3. A. Bizyaeva and collaborators, *Active risk aversion in SIS epidemics on networks*, arXiv:2311.02204 (2023), https://arxiv.org/abs/2311.02204 .
4. T. Götz and collaborators, *Chaos in opinion-driven disease dynamics*, arXiv:2410.08030 (2024), https://arxiv.org/abs/2410.08030 .
