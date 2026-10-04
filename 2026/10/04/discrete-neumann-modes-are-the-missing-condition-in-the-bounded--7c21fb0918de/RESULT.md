# Discrete Neumann modes are the missing condition in the bounded-domain Turing criterion
## Finding
For the supplemented predator--prey reaction--diffusion model studied by Hazra, Banerjee and Jana, the continuous quadratic-discriminant condition used in their Theorem 6 does not by itself imply a Turing instability on a bounded interval. The missing requirement is that the open band of unstable continuous squared wavenumbers contain an actual Neumann Laplacian eigenvalue.

More precisely, on \(\Omega=(0,l\pi)\) the admissible squared wavenumbers are \(z_k=k^2/l^2\), \(k\in\mathbb N_0\). Under the kinetic stability conditions \(R_1\) and \(R_2\), define
\[
A=d_1d_2,\qquad B=a_1d_2+cb_2d_1,\qquad C=ca_1b_2-a_2b_1.
\]
If \(B>0\) and \(S=B^2-4AC>0\), let
\[
z_\pm=\frac{{B\pm\sqrt S}}{{2A}}.
\]
Then diffusion-driven instability occurs if and only if there exists \(k\ge1\) such that
\[
z_-<\frac{{k^2}}{{l^2}}<z_+.
\]
Thus the paper's condition \(R_5\), which is only \(B>0\) and \(S>0\), is necessary but not sufficient on a bounded interval.

An exact witness keeps the paper's values \(\gamma=11\), \(\alpha=1\), \(\delta=1\), \(\beta=39/10\), and \(\xi=3/10\), and chooses
\[
x^*=\frac13,\qquad y^*=\frac{{784}}{{495}},\qquad c=\frac{{41415}}{{38416}},\qquad d_1=\frac{{13}}{{1000}},\qquad d_2=1.
\]
For \(l=1/10\), all Neumann modes are stable even though \(R_5\) holds. For \(l=1\), the same local kinetics and diffusivities have unstable modes \(k=2\) and \(k=3\).

## Assumptions and scope
The claim concerns the linear stability of the positive homogeneous coexistence equilibrium for the one-dimensional Neumann problem in the source model. It uses the source notation
\[
D_k=d_1d_2z_k^2-(a_1d_2+cb_2d_1)z_k+(ca_1b_2-a_2b_1),
\]
with \(z_k=k^2/l^2\). It does not assert existence, stability, or selection of nonlinear patterned steady states after instability.

The exact parameter witness is within the model's positive-parameter regime. The competition coefficient is chosen from the equilibrium equation so that \(x^*=1/3\) is exact rather than numerically approximated.

## Proof
At the coexistence equilibrium, the characteristic polynomial for mode \(k\) is
\[
\lambda^2-T_k\lambda+D_k=0,
\]
where
\[
T_k=-(d_1+d_2)z_k+(a_1+cb_2).
\]
Under \(R_1\), \(a_1+cb_2<0\), so \(T_k<0\) for every \(k\ge0\). Therefore a mode is unstable exactly when \(D_k<0\).

Write \(D(z)=Az^2-Bz+C\) with \(A=d_1d_2>0\), \(B=a_1d_2+cb_2d_1\), and \(C=ca_1b_2-a_2b_1>0\) by \(R_2\). If \(B\le0\) or \(B^2-4AC\le0\), then \(D(z)\ge0\) for every \(z\ge0\). If \(B>0\) and \(S=B^2-4AC>0\), the two positive roots are \(z_-<z_+\), and strict negativity occurs exactly for \(z\in(z_-,z_+)\). Because the bounded Neumann problem permits only \(z_k=k^2/l^2\), diffusion-driven instability is therefore equivalent to the spectral-intersection condition
\[
\exists k\ge1:\quad z_-<k^2/l^2<z_+.
\]
This proves the corrected criterion.

For the exact witness, the model functions give
\[
y^*=F(x^*)=\frac{{784}}{{495}},\qquad h(x^*)=\frac{{251}}{{490}},\qquad c=\frac{{h(x^*)}}{{\xi F(x^*)}}=\frac{{41415}}{{38416}}.
\]
The linearization coefficients are
\[
a_1=\frac{{271}}{{1617}},\quad a_2=-\frac{{10}}{{49}},\quad b_1=\frac{{1248}}{{539}},\quad b_2=-\frac{{392}}{{825}},\quad cb_2=-\frac{{251}}{{490}}.
\]
Hence
\[
a_1+cb_2=-\frac{{5573}}{{16170}}<0,
\qquad
C=ca_1b_2-a_2b_1=\frac{{306379}}{{792330}}>0.
\]
With \(d_1=13/1000\) and \(d_2=1\),
\[
B=\frac{{2602321}}{{16170000}}>0,
\qquad
S=\frac{{1514610947041}}{{261468900000000}}>0,
\]
so the source condition \(R_5\) holds. The vertex of \(D\) is at
\[
\frac{B}{2A}=\frac{{2602321}}{{420420}}<100.
\]
For \(l=1/10\), every nonzero Neumann eigenvalue satisfies \(z_k=100k^2\ge100\). Since \(D\) is increasing for \(z\ge100\) and
\[
D(100)=\frac{{301859687}}{{2641100}}>0,
\]
all nonzero modes have \(D_k>0\). Together with \(T_k<0\), every mode is linearly stable. This contradicts the source theorem's implication from \(R_5\) to the existence of an unstable integer mode.

The effect is genuinely geometric rather than a failure of the continuous instability band. With the same kinetics and diffusivities but \(l=1\),
\[
D(4)=-\frac{{3239273}}{{66027500}}<0,
\qquad
D(9)=-\frac{{6921071}}{{792330000}}<0,
\]
so modes \(k=2\) and \(k=3\) are unstable.

## Verification
The accompanying `verifier.py` uses only Python's exact `fractions.Fraction` arithmetic. It reconstructs the equilibrium relation, the four linearization coefficients, \(R_1\), \(R_2\), \(B\), \(S\), the vertex bound, and the exact signs of \(D(4)\), \(D(9)\), and \(D(100)\). It also checks the claimed monotonicity argument for all \(z\ge100\).

The source paper itself defines the bounded-domain spectrum as \(z_k=k^2/l^2\) and later introduces mode-by-mode Turing curves and the set of admissible modes \(Q\). Those later formulas are consistent with the spectral-intersection correction, but they do not repair the earlier theorem's stated sufficiency of \(R_5\) for fixed bounded-domain parameters.

## Relationship to prior work
Hazra, Banerjee and Jana formulate the model on \(\Omega=(0,l\pi)\), derive the discrete Neumann spectrum, and state in Theorem 6 that \(R_5\) implies the existence of an unstable integer mode. In Section 7 they instead work mode by mode through explicit Turing curves \(d_1^k\) and an admissible-mode set \(Q\), which already reflects the discrete spectrum.

General bounded-domain Turing analyses likewise organize instability by Laplacian eigenmodes rather than by the continuous dispersion curve alone. Jiang, Cao and Wang explicitly describe mode-dependent Turing bifurcation curves and regions of single- and multiple-mode patterns on bounded domains. The present result is the model-specific exact correction and counterexample for the 2026 supplemented predator--prey theorem.

## Limitations
This result is a linear spectral correction. It does not determine the nonlinear attractor when an admissible mode is unstable, and it does not challenge the source paper's numerical examples on \(l=1\), where admissible modes do intersect the unstable band. The exact witness chooses a competition coefficient close to, but not equal to, the paper's illustrative value \(c=1.1\) so that every algebraic check can be replayed with rational arithmetic.

## References
1. A. Hazra, A. Banerjee, D. Jana, “Predator self-limitation controls pattern formation in a predator--prey system with additional food: a Turing--Hopf analysis,” arXiv:2609.29052v1, 24 September 2026. https://arxiv.org/html/2609.29052v1
2. W. Jiang, X. Cao, C. Wang, “Turing instability and pattern formations for reaction-diffusion systems on 2D bounded domain,” Discrete and Continuous Dynamical Systems - B 27 (2022), 1163--1178. https://doi.org/10.3934/dcdsb.2021085
