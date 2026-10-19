# A positive escape wedge and a binary logarithmic clock for a three-dimensional Chialvo map

## Finding

For the electromagnetic-flux Chialvo recurrence below, a simple explicit open region is forward invariant, and every trajectory originating there escapes with a **lag-controlled** double-exponential law. The logarithmic base of the growth is exactly \(2\), not the cubic value \(3\) suggested by replacing the magnetic flux with an instantaneous multiple of the activation coordinate.

Define
\[
K=\frac{k_1}{1+k_2},\qquad B=\frac94 k\beta K^2,
\qquad A=3k\beta k_1^2.
\]
Choose \(Y,\Phi,R\) such that
\[
(1-a)Y\ge c,\qquad 3k\beta\Phi^2>4,\qquad
R>\max\left\{1,|k_0|,\frac{\Phi}{K},\frac{3}{\sqrt B}\right\}.
\]
Then the nonempty open escape wedge
\[
\Omega=\{(x,y,\phi):x>R,\ y<Y,\ \Phi<\phi<Kx\}
\]
is forward invariant. Every trajectory initially in \(\Omega\) has \(x_{n+1}>3x_n\), and
\[
\frac{\phi_n}{x_{n-1}}\longrightarrow k_1,\qquad
\frac{y_n}{x_{n-1}}\longrightarrow-b,\qquad
\frac{x_{n+1}}{x_nx_{n-1}^{2}}\longrightarrow A.
\]
Moreover the logarithmic height
\[
H=\lim_{n\to\infty}\frac{\log x_n}{2^n}
\]
exists and is strictly positive and finite. Hence
\[
x_n=\exp\bigl(H2^n+o(2^n)\bigr).
\]
For the first hitting index \(N(L)=\min\{n\ge0:x_n\ge L\}\),
\[
N(L)=\log_2\log L-\log_2 H+O(1)\quad(L\to\infty).
\]
In particular, divergence takes a doubly logarithmic number of iterations to reach an astronomical threshold.

## Assumptions and scope

The state space is \(\mathbb R^3\), and updates are performed in exact real arithmetic:
\[
\begin{aligned}
x_{n+1}&=x_n^2\exp(y_n-x_n)+k_0+kx_n(\alpha+3\beta\phi_n^2),\\
y_{n+1}&=a y_n-bx_n+c,\\
\phi_{n+1}&=k_1x_n-k_2\phi_n.
\end{aligned}
\]
The parameters obey \(0<a<1\), \(b>0\), \(k>0\), \(\beta>0\), \(k_1>0\), \(\alpha\ge0\), \(0\le k_2<1\), with arbitrary fixed \(c,k_0\in\mathbb R\). The displayed requirements on \(Y,\Phi,R\) can always be satisfied. The wedge is nonempty because for every \(x>\max\{R,\Phi/K\}\) the interval \((\Phi,Kx)\) is nonempty, and \(y<Y\) is arbitrary. No claim is made for initial conditions outside this wedge.

## Proof

**Step 1: strict forward invariance.** Fix a point in \(\Omega\), write its image as \((x',y',\phi')\), and use positivity of the exponential and \(\alpha\):
\[
x'\ge k_0+3k\beta x\phi^2>4x-|k_0|>3x>R.
\]
The recovery coordinate satisfies
\[
y'=ay-bx+c<aY+c-bx\le Y-bx<Y.
\]
For the flux coordinate,
\[
\phi'=k_1x-k_2\phi\ge
(k_1-k_2K)x=Kx>\Phi.
\]
As \(0\le k_2<1\) and \(\phi>0\), we also have
\[
\phi'\le k_1x<3Kx<Kx'.
\]
Thus the strict inequalities defining the wedge persist, and \(x_n>3^n x_0\).

**Step 2: a delayed cubic lower estimate.** At every \(n\ge1\), invariance gives
\[
Kx_{n-1}\le\phi_n\le k_1x_{n-1}.
\]
As \(k\alpha x_n\ge0\) and \(k_0\ge-|k_0|\),
\[
\begin{aligned}
x_{n+1}&\ge 3k\beta x_n\phi_n^2-|k_0|\\
&\ge 3k\beta x_n\phi_n^2-x_n\\
&\ge\tfrac34(3k\beta x_n\phi_n^2)\\
&\ge Bx_nx_{n-1}^2.
\end{aligned}
\]
Here \(3k\beta\phi_n^2>4\), and \(B=9k\beta K^2/4\). In particular,
\[
\frac{x_{n+1}}{x_n}\ge Bx_{n-1}^2\longrightarrow\infty.
\]

**Step 3: exact lag limits.** The flux equation and its previous-step bound imply
\[
\frac{\phi_n}{x_{n-1}}=k_1-k_2\frac{\phi_{n-1}}{x_{n-1}},\qquad
0<\phi_{n-1}\le k_1x_{n-2}.
\]
The preceding super-geometric ratio therefore gives \(\phi_n/x_{n-1}\to k_1\).
Iterating the linear recovery equation and using monotonicity of \(x_j\),
\[
|y_{n-1}|\le a^{n-1}|y_0|+
\frac{|c|+b x_{n-2}}{1-a}\quad(n\ge2).
\]
Consequently \(y_{n-1}/x_{n-1}\to0\), and
\[
\frac{y_n}{x_{n-1}}=a\frac{y_{n-1}}{x_{n-1}}-b+\frac c{x_{n-1}}
\longrightarrow-b.
\]
Divide the activation update by \(x_nx_{n-1}^{2}\). The exponential term tends to zero because \(y_n<Y\) and \(x_ne^{Y-x_n}\to0\); the fixed bias and linear induction term vanish under the same normalization. The remaining term tends to \(3k\beta k_1^2=A\), proving
\[
\frac{x_{n+1}}{x_nx_{n-1}^{2}}\longrightarrow A.
\]

**Step 4: existence of the height.** Let \(L_n=\log x_n\). The positive asymptotic ratio gives a bounded real sequence \(e_n\to0\) such that
\[
L_{n+1}=L_n+2L_{n-1}+\log A+e_n\qquad(n\ge1).
\]
Putting \(z_n=L_n+\tfrac12\log A\) removes the constant term, giving \(z_{n+1}=z_n+2z_{n-1}+e_n\). Define
\[
W_n=2^{-n}(z_n+z_{n-1}).
\]
Then \(W_{n+1}-W_n=2^{-(n+1)}e_n\), an absolutely summable series. Write its finite limit as \(W\). The scalar recurrence
\[
\frac{z_n}{2^n}=W_n-\frac12\frac{z_{n-1}}{2^{n-1}}
\]
has a contraction coefficient \(1/2\), so \(2^{-n}z_n\to 2W/3\). As the difference between \(z_n\) and \(L_n\) is constant, \(H=2W/3\) exists and is finite.

**Step 5: positivity.** With \(u_n=L_n+\tfrac12\log B\), the lower estimate of Step 2 gives
\[
u_{n+1}\ge u_n+2u_{n-1}\quad(n\ge1).
\]
As \(x_0>R\) and \(BR^2>9\), both \(u_0>0\) and \(u_1>0\). Comparing to the exact equality recurrence shows
\[
\liminf_{n\to\infty}2^{-n}u_n
\ge\frac{u_0+u_1}{3}>0.
\]
Therefore
\[
H\ge\frac{\log x_0+\log x_1+\log B}{3}>0.
\]
Combining the positive finite height with strict monotonicity of \(x_n\) yields the hitting-time relation from the two-sided estimates \((H-\varepsilon)2^n\le\log x_n\le(H+\varepsilon)2^n\) for all sufficiently large \(n\). This proves the claim.

## Verification

The accompanying standalone `verify.py` (requires `mpmath`) checks the explicit wedge inequalities over three distinct admissible parameter choices, 36 successive updates, the delayed nonlinear lower bound, and the three normalized lag ratios at late finite times. The numerical checks are diagnostic; the infinite-time claims follow from the above inequalities and recurrences rather than from numerical extrapolation. Run with `python verify.py`.

## Relationship to prior work

Muni, Fatoyinbo, and Ghosh (2022) introduce the three-dimensional electromagnetic-flux Chialvo map and numerically examine diverging initial states among its basin configurations. The new result isolates an explicit open escape region and computes a sharp orbitwise double-exponential scale and a first-hitting-time clock. The 2022 numerical divergence observations do not by themselves imply a forward-invariant cone, the lag limits, or the positive finite height. A related existing result on *zero-bias two-dimensional* Chialvo compact recurrence concerns another map and a different dynamical regime. A general polynomial-growth recurrence is mathematically related, but the lag-reduction and invariant region for this particular smooth map are established directly here.

## Limitations

The region \(\Omega\) is a sufficient, not necessary, escape set; the full basin of infinity is not classified. The result assumes positive flux feedback, \(0\le k_2<1\), nonnegative linear memconductance, and exact arithmetic. Numerical trajectory overflow in finite precision is not itself a mathematical finite-time singularity. The escape height \(H\) depends on initial conditions and parameters. Published equivalent treatments or specialized supplementary computations not located by the literature comparison remain a priority risk. This work has not undergone an independent scientific audit.

## References

1. S. S. Muni, H. O. Fatoyinbo and I. Ghosh, *Dynamical effects of electromagnetic flux on Chialvo neuron map: nodal and network behaviors*, arXiv:2201.03219, first posted 2022-01-10; later published with DOI 10.1142/S0218127422300208. https://arxiv.org/abs/2201.03219
2. I. Ghosh, seminar presentation (2024), slide displaying the full three-dimensional electromagnetic-flux Chialvo recurrence. https://indrag49.github.io/uploads/AUT_seminar_slides_2024.pdf
3. I. Ghosh, S. S. Muni and H. O. Fatoyinbo, *On the analysis of a time varying noise-modulated heterogeneous coupled network of Chialvo neurons under the influence of electromagnetic flux*, arXiv:2206.04234 (2022); its abstract concerns numerically studied networks, not this asymptotic theorem. https://arxiv.org/abs/2206.04234
