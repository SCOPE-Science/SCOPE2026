# A counterattack threshold reverses predator invasion over a two-cycle of prey

## Finding

For a positive-parameter subfamily of the juvenile/adult-predator map in Bhattacharjee, Ray, Das and Sarmah [1], the predator-free prey population has an attracting **period-two** orbit. The rare-predator Floquet multiplier on that orbit can cross one in either direction relative to the natural *static* predator reproduction benchmark at prey carrying capacity. In particular, holding the static benchmark at exactly one and increasing juvenile counterattack produces a **single, exact sign reversal** at \(A=2/35\). Two rational parameter witnesses demonstrate both strict reversals: a predator whose static benchmark exceeds one cannot invade the prey cycle, and another whose static benchmark is below one can invade the same prey cycle.

The result is a local spectral threshold, not a persistence or coexistence theorem.

## Assumptions and scope

We use the forward-Euler map (2.2) in the source [1] with step \(h=1\), carrying capacity \(k=1\), refuge fraction \(n=1/2\), prey growth rate \(r=22/5\), adult conversion \(\mu=1/2\), juvenile predation \(\alpha_1=1/10\), juvenile natural mortality \(\beta=11/20\), maturation \(\gamma=1/4\), and adult mortality \(m=4/5\). Write the positive juvenile counterattack rate as \(A=\alpha_3\), and set the positive adult predation rate to \(\alpha_2=4C\). For each \(A,C>0\), the explicit map is

\[
\begin{aligned}
x_{t+1}&=x_t+\tfrac{11}{5}x_t(1-x_t)-\tfrac{1}{10}x_ty_t-2Cx_tz_t,\\
y_{t+1}&=(\tfrac15-Ax_t)y_t+Cx_tz_t,\\
z_{t+1}&=\tfrac14y_t+\tfrac15z_t.
\end{aligned}
\]

Here \(x\) denotes prey, \(y\) juvenile predators, and \(z\) adult predators. The positive cone is asserted invariant only **locally** near the specified predator-free two-cycle; no claim of global nonnegativity is made for the explicit Euler map.

The predator-free prey recurrence \(f(x)=x+(11/5)x(1-x)\) has the positive period-two orbit

\[
x_- =\frac{21-\sqrt{21}}{22},\qquad
x_+ =\frac{21+\sqrt{21}}{22},\qquad f(x_-)=x_+,\ f(x_+)=x_-.
\]

Its scalar two-generation multiplier is \(f'(x_-)f'(x_+)=4/25\), so the prey cycle is attracting within the predator-free boundary. For a rare predator, let

\[
M(u;A,C)=\begin{pmatrix}\frac15-Au&Cu\\\frac14&\frac15\end{pmatrix},
\qquad P(A,C)=M(x_+;A,C)M(x_-;A,C).
\]

In all strict comparisons below \(M(x_\pm;A,C)\) is entrywise positive. Write \(\rho(P)\) for the spectral radius. The meaningful static benchmark, evaluated at the prey *fixed point* \(x=1\), is

\[
\mathcal R_{\rm static}(A,C)=\frac{5C}{16(A+4/5)}.
\]

It is precisely the rare-predator matrix threshold \(\rho(M(1;A,C))\gtrless1\) when its entries are positive; since the prey fixed point is unstable for these parameters, this is a comparative static benchmark, **not** a prediction of stability of the full prey-only fixed point.

**Sharp reversal on the static threshold.** Define \(C_0(A)=\tfrac{16}{5}(A+\tfrac45)\). For every

\[
0<A<\frac{22}{5(21+\sqrt{21})},
\qquad C=C_0(A),
\]

we have \(\mathcal R_{\rm static}=1\) and

\[
\boxed{\det(I-P(A,C_0(A)))=-\frac{48}{15125}(35A-2).}
\]

Consequently \(\rho(P)<1\) for \(A<2/35\), \(\rho(P)=1\) at \(A=2/35\), and \(\rho(P)>1\) for \(A>2/35\), throughout the displayed range. At equality only a neutral *linear* multiplier is asserted.

**Opposite strict rational witnesses.** Two admissible pairs are:

\[
\begin{array}{c|c|c|c}
(A,C)&\mathcal R_{\rm static}&\det(I-P)&\text{cycle response}\\\hline
(1/100,13/5)&325/324>1&21327/6050000>0&\rho(P)<1\\
(1/10,287/100)&287/288<1&-58119/19360000<0&\rho(P)>1
\end{array}
\]

The first three-dimensional predator-free cycle is locally asymptotically stable, including small nonnegative predator perturbations; the second has a positive expanding predator Floquet direction and is linearly invasible. Both have identical prey-only cycles; only the adult predation and juvenile counterattack parameters differ.

## Proof

**1. Exact attracting prey cycle.** The explicit recurrence is \(f(x)=(16/5)x-(11/5)x^2\). Direct substitution proves the two-cycle expressions and shows \(x_-+x_+=21/11\) and \(x_-x_+=105/121\). Its product derivative is \(4/25\), strictly inside the unit circle.

**2. Transverse linearization.** Along the predator-free orbit, the full three-dimensional Jacobian is block upper triangular with scalar prey diagonal \(f'(x_t)\) and a predator block \(M(x_t;A,C)\). Thus the eigenvalues of the two-generation Jacobian consist of \(4/25\) and the two eigenvalues of \(P=M(x_+)M(x_-)\); the upper-right prey-to-predator couplings cannot alter them. In the stated parameter ranges \(1/5-Ax_+>0\), and every entry of both predator matrices is strictly positive, so \(P\) is positive and its Perron eigenvalue \(\rho(P)\) is simple and larger in modulus than its other eigenvalue.

**3. A determinant criterion without numerical eigenvalue inference.** Direct multiplication and the two symmetric identities in Step 1 give the exact rational polynomial

\[
\begin{aligned}
D(A,C):=\det(I-P)={}&-\frac{504}{605}A^2+\frac{504}{1375}A
+\frac{105}{1936}C^2\\
&+\left(\frac{21}{242}A-\frac{273}{550}\right)C
+\frac{576}{625}.
\end{aligned}
\]

Moreover \(P_{22}=1/25+(C/4)x_-<1\) for the entire static-threshold family (because \(A<22/[5(21+\sqrt{21})]<2/5\), hence \(C_0(A)<96/25\), and \(x_-<1\)) and for both witnesses (because \(C<3\)). For every positive \(2\times2\) matrix with its lower-right entry less than one, \(D>0\) is equivalent to \(\rho(P)<1\), \(D=0\) to \(\rho(P)=1\), and \(D<0\) to \(\rho(P)>1\). Indeed, writing \(P=(p_{ij})\), \(D=(1-p_{11})(1-p_{22})-p_{12}p_{21}\); for \(D>0\) and \(p_{22}<1\), also \(p_{11}<1\), and the nonsingular \(M\)-matrix criterion (or characteristic polynomial and Perron monotonicity) applies. More directly, because the off-diagonal entries are strictly positive, the smaller eigenvalue of \(P\) lies strictly below \(\min\{p_{11},p_{22}\}<1\), while the larger one is \(\rho(P)\). Thus \(D=(1-\rho(P))(1-\lambda_{\rm other})\) and all three sign conclusions follow without ambiguity.

**4. Exact switch and witnesses.** At the fixed prey level \(x=1\), \(\det(I-M(1))=\tfrac45(A+\tfrac45)-\tfrac14 C\), so the natural static threshold is \(C=C_0(A)\). Substituting it in \(D\) yields \(-48(35A-2)/15125\). The crossover \(A=2/35\) lies strictly inside the allowed positive range. Substituting each rational witness into the same exact polynomial yields the two signed rational determinants displayed above; inserting these parameters into \(\mathcal R_{\rm static}\) gives the opposite inequalities.

**5. Full local stability.** At the suppressed witness, every eigenvalue of the squared three-dimensional Jacobian has modulus below one: the prey multiplier is \(4/25\), and the strict Perron criterion controls both predator eigenvalues. The hyperbolic periodic-orbit stability theorem gives a local basin containing biologically positive points. At the promoted witness, Perron–Frobenius theory gives a strictly positive predator eigenvector with eigenvalue exceeding one, hence a transversely expanding direction. Nothing in this local statement proves long-term predator persistence after growth or characterizes remote attractors.

## Verification

Run `python3 verify.py` using only the Python standard library. The file implements exact arithmetic in \(\mathbb Q(\sqrt{21})\), checks both prey-cycle substitutions, their sum/product and multiplier, multiplies both exact predator matrices, compares the determinant with the rational formula, checks the static-threshold factorization for rational probe values, and checks both complete strict witness identities. This computation is a reproducible algebraic check of selected claims; the universally quantified sharp switch and local dynamical conclusions are justified analytically above. No numerical simulation is used as an infinite-time proof.

## Relationship to prior work

Bhattacharjee, Ray, Das and Sarmah [1] introduced the refuge-and-counterattack discrete model, calculated fixed points and their linear stability, and analyzed Neimark–Sacker and period-doubling bifurcations at coexistence equilibria. Those results are not asserted as new. The new comparison concerns invasion of an **attracting predator-free period-two resident orbit**, which is governed by the ordered two-generation product of juvenile/adult matrices, not merely their evaluation at carrying capacity. General positive-matrix Floquet principles are standard [2]; the model-specific counterattack reversal, exact crossover, and opposite rational witnesses are the contribution assessed here. Stage-structured predator/prey studies [3,4] address related dynamics but not this specific threshold.

## Limitations

The assertions are local and spectral. At \(A=2/35\), nonlinear invasion or extinction is not classified. The prey-only fixed point at \(x=1\) is itself unstable, so its static invasion number is an informative counterfactual benchmark, not a stable-resident invasion criterion. Neither global preservation of the positive cone by explicit Euler, stochastic persistence, global predator extinction after introduction, nor nonlinear positive coexistence follows. The source also contains an inconsistent later displayed index form of the adult equation; the theorem uses the maturation inflow \(\gamma y_t\) in the source's boxed Euler formula, which agrees with its continuous equation. Priority claims remain subject to other, potentially unindexed analyses.

## References

[1] D. Bhattacharjee, N. Ray, D. Das, H. K. Sarmah, *A discrete-time dynamical model of prey and stage-structured predator with juvenile hunting incorporating negative effects of prey refuge*, arXiv:2308.08864 (first posted 17 August 2023), https://arxiv.org/html/2308.08864v1 ; *Partial Differential Equations in Applied Mathematics* **10** (2024), article 100710, https://doi.org/10.1016/j.padiff.2024.100710 .

[2] H. L. Smith, *Monotone Dynamical Systems: An Introduction to the Theory of Competitive and Cooperative Systems*, American Mathematical Society, 1995 (positive-matrix and monotone-system background).

[3] A. Wikan, *An Analysis of Discrete Stage-Structured Prey and Prey-Predator Population Models*, *Discrete Dynamics in Nature and Society* (2017), article 9475854, https://doi.org/10.1155/2017/9475854 .

[4] H. J. Wearing, S. M. Sait, T. C. Cameron, P. Rohani, *Stage-structured competition and the cyclic dynamics of host–parasitoid populations*, *Journal of Animal Ecology* (2004), https://doi.org/10.1111/j.0021-8790.2004.00846.x .
