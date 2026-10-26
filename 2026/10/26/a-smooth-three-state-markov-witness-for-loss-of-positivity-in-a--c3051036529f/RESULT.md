# A smooth three-state Markov witness for loss of positivity in a third-order Magnus integrator

## Finding

For the seven-exponential third-order commutator-free Magnus method (3.19) of Blanes, Iserles, and Macnamara, there exists a single bounded \(C^3\) time-dependent three-state Markov generator \(A(t)\) and initial state \(y(0)=e_1\) such that, for every \(n\ge1\), the method's one-step output at step

\[
h_n=10^{-1}100^{-(n-1)}\longrightarrow0
\]

has third coordinate

\[
\widehat y_3(h_n)=\frac{C-\exp(c s_n)-c\exp(-s_n)}{C}<0,
\qquad s_n=\frac{h_n^5}{2},\quad C=\frac{2\sqrt3}{3},\quad c=C-1>0.
\]

The exact ODE solution remains in the probability simplex. The negative numerical coordinate satisfies

\[
\widehat y_3(h_n)=-\frac{c}{8}h_n^{10}+O(h_n^{15}),
\]

so the exact positivity failure does not contradict the method's third-order convergence.

## Assumptions and scope

Use column-vector dynamics \(y'=A(t)y\). A Markov generator here means that every off-diagonal entry of \(A(t)\) is nonnegative and every column sum is zero. Define the two one-way transition generators

\[
G_{12}=\begin{pmatrix}-1&0&0\\1&0&0\\0&0&0\end{pmatrix},\qquad
G_{23}=\begin{pmatrix}0&0&0\\0&-1&0\\0&1&0\end{pmatrix}.
\]

Both are graph Laplacians in the convention of the cited paper. Let \(b_-=\tfrac12-\tfrac{\sqrt3}{6}\), \(b_+=\tfrac12+\tfrac{\sqrt3}{6}\), \(\delta=1/50\), and let \(\psi\) be any nonnegative \(C^\infty\) bump supported in \([-1,1]\) with \(\psi(0)=1\). For example, take \(\psi(u)=e\exp[-1/(1-u^2)]\) for \(|u|<1\), and zero otherwise. Set \(a_n=h_n^4\), and define on \([0,1]\)

\[
A(t)=\sum_{n\ge1}a_n\psi\!\left(\frac{t-b_-h_n}{\delta h_n}\right)G_{12}
+\sum_{n\ge1}a_n\psi\!\left(\frac{t-b_+h_n}{\delta h_n}\right)G_{23}.
\]

The pulses are disjoint. The sequence of step sizes is used only to evaluate this one fixed generator at \(t=0\); the generator itself does not depend on which step is being tested.

## Proof

**Regularity and exact-flow positivity.** Each summand is a nonnegative scalar multiple of a graph Laplacian, so \(A(t)\) has nonnegative off-diagonal entries and zero column sums for every \(t\). For derivatives of order \(k\le3\), the contribution of a pulse is bounded by a constant times

\[
\frac{a_n}{(\delta h_n)^k}=\delta^{-k}h_n^{4-k}\longrightarrow0.
\]

The supports are locally finite away from zero and their derivatives through order three tend to zero at zero. Hence \(A\in C^3([0,1])\) and is bounded. The positive cone is forward invariant: at a boundary point where \(y_i=0\) and \(y\ge0\), one has \(y_i'=\sum_{j\ne i}A_{ij}(t)y_j\ge0\). Also \(\frac{d}{dt}\mathbf1^Ty=\mathbf1^TA(t)y=0\). Thus the exact solution from \(e_1\) stays in the probability simplex.

**Values seen by the numerical method.** The eight sampling fractions in formula (3.19) are

\[
\frac16-\frac{\sqrt3}{12},\ \frac1{12},\ \frac16+\frac{\sqrt3}{12},\
\frac13-\frac{\sqrt3}{6},\ \frac16,\ \frac13+\frac{\sqrt3}{6},\ b_-,\ b_+.
\]

They are distinct; the smallest is \(\frac16-\frac{\sqrt3}{12}>0.022\). With \(h_{n+1}=h_n/100\), every pulse at a smaller scale lies below this first sampling fraction for step \(h_n\), while every larger-scale pulse lies outside \([0,h_n]\). The radius \(\delta h_n\) is smaller than the distance from either of the two pulse centers to every other sampling node. Therefore, for the step \(h_n\), all sampled matrices in the first five exponentials are zero, and the two final sampled matrices are exactly

\[
\mathcal B_1=a_nG_{12},\qquad \mathcal B_2=a_nG_{23}.
\]

Consequently the first five exponentials act as the identity. Write

\[
\alpha=\frac12+\frac{\sqrt3}{3},\qquad
\beta=\frac12-\frac{\sqrt3}{3},\qquad
\alpha+\beta=1,\quad \beta<0,
\]

and \(s_n=a_nh_n/2=h_n^5/2\). The remaining two factors are

\[
\widehat y(h_n)=\exp\!\big(s_n(\alpha G_{23}+\beta G_{12})\big)
\exp\!\big(s_n(\beta G_{23}+\alpha G_{12})\big)e_1,
\]

where the rightmost factor is applied first. Directly solving the triangular two-stage transitions gives

\[
\widehat y_1=e^{-s_n},\qquad
\widehat y_2=\frac{e^{c s_n}-e^{-s_n}}{C},\qquad
\widehat y_3=1-\widehat y_1-\widehat y_2
=\frac{C-e^{c s_n}-c e^{-s_n}}{C},
\]

with \(C=\alpha-\beta=2\sqrt3/3=1+c\). Define \(g(s)=e^{cs}+ce^{-s}-(1+c)\). Then \(g(0)=0\) and

\[
g'(s)=c(e^{cs}-e^{-s})>0\qquad(s>0).
\]

Thus \(g(s_n)>0\), so \(\widehat y_3(h_n)<0\) for every \(n\). Taylor expansion at zero gives \(\widehat y_3(h_n)=-cs_n^2/2+O(s_n^3)=-ch_n^{10}/8+O(h_n^{15})\). This proves the claim.

## Verification

The algebraic sign argument above is exact and applies to every \(s_n>0\). The accompanying `verify.py` evaluates the closed form at several decreasing step sizes using high-precision decimal arithmetic and confirms strict negativity; it is a numerical cross-check, not the proof of the infinite sequence. The proof also explicitly verifies the generator sign pattern, column sums, \(C^3\) regularity, the stage-sampling separation, and preservation of positivity and mass by the exact flow.

## Relationship to prior work

Blanes, Iserles, and Macnamara introduce the seven-exponential third-order method and state that positivity is conditional on two weighted combinations of sampled graph Laplacians retaining the graph-Laplacian sign pattern. They note that the negative coefficient \(\beta\) means positivity is not assured. The present claim is narrower and more explicit: it gives one fixed bounded \(C^3\) generator, a sequence \(h_n\to0\), and a closed-form negative component at every step size in that sequence. A related 2020 paper studies a different fourth-order commutator-free Magnus integrator and likewise discusses the risk from negative weighted combinations; that result does not imply the exact seven-exponential witness proved here.

## Limitations

The construction is deliberately structured and the negative component is of order \(h_n^{10}\), so its practical size can be very small. It proves failure of exact nonnegativity, not instability, loss of convergence order, or practical failure for a particular application. It does not claim that negativity occurs for every smooth generator or every sufficiently small step size. The novelty assessment is best-knowledge and cannot exclude an unindexed equivalent construction.

## References

1. S. Blanes, A. Iserles, and S. Macnamara, “Positivity-preserving methods for ordinary differential equations,” *ESAIM: Mathematical Modelling and Numerical Analysis* 56 (2022), 1843–1870. First public preprint: arXiv:2102.08242, 16 February 2021. DOI: 10.1051/m2an/2022042.
2. S. MacNamara, S. Blanes, and A. Iserles, “Simulation of bimolecular reactions: Numerical challenges with the graph Laplacian,” *ANZIAM Journal* 61 (2020), C59–C74. DOI: 10.21914/anziamj.v61i0.15169.
