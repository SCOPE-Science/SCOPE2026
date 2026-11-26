# Independent mathematical audit

## correctness

PASS

The c y_1 y_2 term is nonnegative, vanishes when either donor vanishes, cancels pointwise and leaves y_1'=a y_2 and y_2'=−a y_2. For any fixed forward and backward rates r,l in a conservative weighted solve, the first component is (u+hrs)/(1+h(r+l)), s=u+v. Apply this first with r=a+cu, l=cv and then with r=P_c/V, l=Q_c/U after averaging the two Heun flux rows at (u,v) and (U,V)=z. This gives δ=hav/[1+h(a+cs)] and Δ−δ=[ha(v+V)/2−δ]/[1+h(P_c/V+Q_c/U)]. The first formula yields 0<δ<v and the second has positive numerator; the endpoint second component is [v+hQ_c s/U]/[1+h(P_c/V+Q_c/U)]>0. Both conserve s. As c increases, U→u, V→v, P_c/c,Q_c/c→uv, and the final rate sum divided by c tends to s. The numerator in the uncombined difference formula tends to hav. Thus cδ and c(Δ−δ) both tend to av/s, cΔ tends to 2av/s, and the exact flow moves a positive distance v(1−e^(−ah)). This gives the asserted error ratio and rules out a representation-uniform multiplicative bound. A fixed positive absolute tolerance gives a lower bound on all weighted RMS denominators. Exact-rational independent scalar solves agree with the difference identity and numerical limits for three unequal/equal cases, including c=0 and c=10^10.

## originality

PASS

The defensible distinct result is the sharp deterioration of the embedded estimate among donor-vanishing splittings of a fixed one-way decay ODE, for every positive initial state (including u=v), with the stated exact constants. PDS nonuniqueness and the embedded procedure are known. A strong overlapping mPDeC catalogue theorem actually implies stalling and a vanishing successive-endpoint discrepancy for the same Heun embedded pair in a different model: take two Lobatto nodes and one/two corrections. However, that theorem is for symmetric two-way exchange and a constant flux offset that does not vanish at zero donor. It does not cover the specified donor-vanishing nonlinear equal-flux perturbation or its all-state coefficient and fixed-flow error for one-way decay. Neither basic representation sensitivity nor the generic masking phenomenon alone is claimed as distinct.

## value

PASS

This counterexample rules out a natural proposed safeguard: requiring the auxiliary production and destruction terms to vanish at their donor boundary does not by itself make the embedded discrepancy control the true error uniformly. The vector field has fixed stiffness, the rates are donor-vanishing and conservative, and exact step positivity survives, so the effect isolates the flux representation rather than physical stiffness or positivity failure. The sharp estimate is a reusable test for representation sensitivity in the actual embedded pair, not a claim to have invented the broader stalling phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
