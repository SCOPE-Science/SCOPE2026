# A strict separation between joint-parameter and location-only optimal Gaussian-plume transects

## Finding

A three-sensor crosswind transect has two different and uniquely determined optimal widths when a Gaussian-shaped concentration profile is observed through independent Poisson counts with *both source amplitude and constant ambient background unknown*. For every strictly positive signal-to-background ratio, maximizing the determinant of the full three-parameter Fisher information matrix requires a wider transect than minimizing the local Cramér–Rao bound for plume-center position, even when both designs use identical equal sensor exposures. The unique widths, their background dependence, and both limiting regimes have exact scalar descriptions below.

Put \(\beta=b/A>0\) and \(t=d^2/(2\sigma^2)\), where the sensor locations are \(-d,0,d\). The unique full-parameter D-optimal spacing is \(d_D=\sigma\sqrt{2t_D}\), where

\[
\frac1{t_D}+\frac{2}{e^{t_D}-1}
=\frac{2\beta e^{t_D}}{1+\beta e^{t_D}}.
\]

For fixed equal sensor exposure, the unique center-location c-optimal spacing is \(d_C=\sigma\sqrt{2t_C}\), where

\[
\frac1{t_C}-1=\frac{\beta e^{t_C}}{1+\beta e^{t_C}}.
\]

In particular,

\[
\boxed{\frac12<t_C(\beta)<1<t_D(\beta)\quad\text{for every }\beta>0.}
\]

Both optimizers move strictly inward as the background-to-signal ratio rises. They have the sharp limiting laws

\[
\begin{aligned}
t_C(\beta)&\longrightarrow 1 && (\beta\downarrow0),\\
t_C(\beta)&\longrightarrow\tfrac12 && (\beta\to\infty),\\
t_D(\beta)&=W\!\left(\frac1{2\beta}\right)+o(1) && (\beta\downarrow0),\\
t_D(\beta)&\longrightarrow t_\infty && (\beta\to\infty),
\end{aligned}
\]

where \(W\) denotes the positive real Lambert function and \(t_\infty\approx1.06144821036\) is the unique solution of \(1/t+2/(e^t-1)=2\). This establishes a qualitative design distinction: the full-parameter optimal transect becomes arbitrarily wide as the ambient background tends to zero, but the center-location optimal transect stays bounded.

## Assumptions and scope

Fix a known crosswind Gaussian width \(\sigma>0\). An unknown plume center \(x\in\mathbb R\), unknown peak concentration amplitude \(A>0\), and unknown spatially constant background \(b>0\) determine the count means at locations \(s\in\{-d,0,d\}\):

\[
Y_s\sim\operatorname{Pois}\!\left(w_s\left[A\exp\!\left(-\frac{(s-x)^2}{2\sigma^2}\right)+b\right]\right),
\]

independently, with known exposures \(w_-,w_0,w_+>0\) and \(d>0\). The total exposure \(E=w_-+w_0+w_+\) is fixed. All optimality criteria are **local at nominal center \(x=0\)** and conditional on nominal positive \(A,b\). The full Fisher matrix concerns the three-dimensional parameter vector \((x,A,b)\), without known-amplitude or known-background simplifications.

D-optimality means maximizing \(\det\mathcal I(x,A,b)\) over the *symmetric three-location family* and positive exposures summing to \(E\). For the c-optimal width, first fix the D-optimal equal exposure allocation \(w_-=w_0=w_+=E/3\), and then maximize the efficient Fisher information for \(x\) after accounting for the two unknown nuisance parameters. This is **not** a global optimum over every possible unsymmetric array, every exposure distribution, or every sensor number.

## Proof

Set \(q=e^{-t}\), so the center concentration is \(A+b\), whereas both wing concentrations are \(Aq+b\). At \(x=0\), the three rows of the mean-gradient matrix (with respect to \((x,A,b)\)) are

\[
J=\begin{pmatrix}
-Aqd/\sigma^2&q&1\\
0&1&1\\
Aqd/\sigma^2&q&1
\end{pmatrix}.
\]

The Poisson Fisher matrix factors as

\[
\mathcal I=J^{\mathsf T}\operatorname{diag}\!\left(
\frac{w_-}{Aq+b},\frac{w_0}{A+b},\frac{w_+}{Aq+b}
\right)J.
\]

Since \(|\det J|=2Aqd(1-q)/\sigma^2\), taking determinants yields the exact formula

\[
\boxed{
\det\mathcal I=
\frac{8w_-w_0w_+}{\sigma^2 A(1+\beta)}
\frac{t(1-e^{-t})^2}{(1+\beta e^t)^2}.}
\]

Every factor is positive for \(d,A,b,\sigma,w_s>0\), proving local three-parameter identifiability within the model. At fixed \(E\), the strict arithmetic–geometric mean inequality gives \(w_-w_0w_+\le(E/3)^3\), with equality exactly at the equal exposure allocation. Thus the D-optimal width uniquely maximizes

\[
D_\beta(t)=\frac{t(1-e^{-t})^2}{(1+\beta e^t)^2},\qquad t>0.
\]

Its logarithmic derivative is

\[
H_D(t,\beta)=\frac1t+\frac{2}{e^t-1}-\frac{2\beta e^t}{1+\beta e^t},
\]

and the derivative of that derivative is strictly negative:

\[
\partial_t H_D=-\frac1{t^2}-\frac{2e^t}{(e^t-1)^2}-\frac{2\beta e^t}{(1+\beta e^t)^2}<0.
\]

As \(t\downarrow0\), \(H_D\to+\infty\); as \(t\to\infty\), \(H_D\to-2\). Hence exactly one critical point exists; the function increases before it and decreases afterward, proving the unique global D-optimum. Moreover \(H_D(1,\beta)>1+2/(e-1)-2>0\), since \(e<3\), so \(t_D>1\).

For equal wing exposures, the location-score row is odd in the wing location, whereas the scores for \(A\) and \(b\) are even. Their Fisher inner products vanish. The efficient location information therefore equals its diagonal Fisher entry:

\[
\boxed{\mathcal I_{x\mid A,b}=
\frac{4(E/3)A}{\sigma^2}
\frac{t e^{-t}}{1+\beta e^t}.}
\]

It is maximized by maximizing \(C_\beta(t)=t e^{-t}/(1+\beta e^t)\). Its log derivative

\[
H_C(t,\beta)=\frac1t-1-\frac{\beta e^t}{1+\beta e^t}
\]

is strictly decreasing because \(\partial_t H_C=-t^{-2}-\beta e^t/(1+\beta e^t)^2<0\). It tends to \(+\infty\) at zero and \(-2\) at infinity, with \(H_C(1/2,\beta)>0\) and \(H_C(1,\beta)<0\). Thus \(1/2<t_C<1\) is its unique maximizer. Combining this with \(t_D>1\) proves the strict separation for *every* positive background.

At fixed \(t\), both \(H_D\) and \(H_C\) strictly decrease with \(\beta\). Since they also decrease strictly in \(t\), the roots \(t_D(\beta)\) and \(t_C(\beta)\) strictly decrease in \(\beta\). On compact positive \(t\)-ranges, their respective limiting equations at \(\beta\to\infty\) are \(1/t+2/(e^t-1)=2\) and \(1/t=2\), yielding the stated limits by uniqueness and root bracketing. As \(\beta\downarrow0\), the c-optimal root tends to \(1\). The D-optimal root must tend to infinity, since the D-limit logarithmic derivative \(1/t+2/(e^t-1)\) is positive at every fixed finite \(t\). Its defining equation then gives \(2\beta t_D e^{t_D}\to1\); inversion of the monotone function \(t\mapsto te^t\) proves \(t_D=W(1/(2\beta))+o(1)\).

## Verification

A standalone Python 3 standard-library program `verify.py` accompanies this result. It checks the Fisher determinant in exact rational arithmetic using an independent three-by-three matrix calculation, checks the nuisance-orthogonality and efficient-information identities, compares analytical logarithmic derivatives against numerical differences, brackets both optima across a large range of positive backgrounds, and verifies strict separation and independent global-value comparisons on finite grids. The program prints `VERIFY_OK assertions=16105` on successful replay. These computations corroborate the formulas; the all-positive-parameter conclusions follow from the analytic inequalities in the proof, not from the grid tests.

At \(\beta=1\), the roots are \(t_D\approx1.27338014967\) and \(t_C\approx0.60706468154\). The corresponding distances satisfy \(d_D/\sigma\approx1.59585723\) and \(d_C/\sigma\approx1.10187538\). With identical equal exposures, the D-optimal determinant is approximately \(2.0190\) times that at the c-optimal spacing, while the location-only Cramér–Rao lower bound at D-optimal spacing is approximately \(1.4972\) times that at the c-optimal spacing.

## Relationship to prior work

Sensor placement using Gaussian-process mutual information is developed by Guestrin, Krause and Singh (2005), but its Gaussian process covariance-utility model does not compute the Fisher determinant of independent Poisson observations with two unknown concentration nuisances. Jones, Goldstein, Jonathan and Randell (2015) explicitly motivate optimal sensing of Gaussian-plume pollutants, but their Bayesian design and emulation approach uses Gaussian data/priors and general expected-loss criteria rather than this exact symmetric three-count design. Battistelli and collaborators (2015) derive source identifiability and filtering for a more general time-dependent PDE source model, not the present Poisson D-versus-c width classification.

Gallatin and Berglund (2012) derive optimal Poisson fluorescence scan paths for a known spatial intensity profile, including a single-parameter Gaussian peak-localization rule. Their nominal model does not jointly estimate a positive constant Poisson background and an unknown peak amplitude, and it does not imply the full three-parameter D-optimal root from the single-position information result. Ristic, Gunatilaka and Gailis (2015) treat Gaussian-plume parameter inference with a network of *binary* sensors, a closely related but distinct observation model. Its full text was unavailable during comparison, so an earlier equivalent result cannot be conclusively excluded.

## Limitations

The result is a **local** Fisher-information theorem, not a global source-location identification, Bayesian robustness, field-data conclusion, or unconditional estimator-performance guarantee. It presumes a Gaussian crosswind shape of known width, independent Poisson observations, stable known exposures and a spatially constant positive background. The finite sensor family is constrained to one center and a symmetric wing pair, so conclusions about unrestricted designs, different sensor numbers, heterogeneous exposure measurement costs, and unknown plume widths are not made. The \(b\downarrow0\) statement is a limit of regular models with \(b>0\), not a claim that standard regular Fisher theory applies without qualification at the boundary \(b=0\). The novelty comparison is best-knowledge only; specialized earlier optimal-design literature may contain equivalent formulations.

## References

- Guestrin, C., Krause, A., and Singh, A. P. (2005), *Near-Optimal Sensor Placements in Gaussian Processes*, ICML, DOI: https://doi.org/10.1145/1102351.1102385 .
- Gallatin, G. M., and Berglund, A. J. (2012), *Optimal Laser Scan Path for Localizing a Fluorescent Particle in Two or Three Dimensions*, *Optics Express* 20, 16381–16393. Full text: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=910609 .
- Jones, M., Goldstein, M., Jonathan, P., and Randell, D. (2015), *Bayes linear analysis for Bayesian optimal experimental design*, *Journal of Statistical Planning and Inference* 171, 115–129. Full text: https://www.lancaster.ac.uk/~jonathan/JGJR15_OptDsg.pdf .
- Battistelli, G., Chisci, L., Forti, N., Pelosi, G., and Selleri, S. (2015), *Point source estimation via finite element multiple-model Kalman filtering*, 54th IEEE CDC. Full text: https://flore.unifi.it/retrieve/e398c37a-c1b0-179a-e053-3705fe0a4cff/Point%20source%20estimation%20via%20finite%20element%20multiple-model%20Kalman%20filtering%20%28CDC%202015%29.pdf .
- Ristic, B., Gunatilaka, A., and Gailis, R. (2015), *Achievable accuracy in Gaussian plume parameter estimation using a network of binary sensors*, *Information Fusion* 25, 42–48, DOI: https://doi.org/10.1016/j.inffus.2014.10.007 (abstract inspected; full text unavailable).
- Achanta, H. K., Dasgupta, S., Mudumbai, R., Xu, W., and Ding, Z. (2019), *Optimum sensor placement for localization of a hazardous source under log normal shadowing*, *Numerical Algebra, Control and Optimization* 9, 361–382, DOI: https://doi.org/10.3934/naco.2019024 (abstract and formal model inspected).
