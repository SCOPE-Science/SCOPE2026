# Independent mathematical audit

## correctness

PASS

The primary source gives the exact capacity union \([0,H(Y_1\mid Y_2)]\times[0,H(Y_2\mid Y_1)]\) over input distributions. For a positive support weight, the submitted weighted entropy objective has strictly negative second variation on the simplex tangent space and its maximizer is interior. Eliminating the Lagrange multiplier from the two stationary equations yields \(\ln x\ln y=\ln(1+x)\ln(1+y)\), equivalently \(\psi(x)\psi(y)=1\). Strict monotonicity of \(\psi\) gives uniqueness and the converse reconstructs the support weight. Fresh numerical root solves for representative \(x\) values independently satisfied both KKT equations to numerical precision; the continuum conclusion is analytic. At symmetry the relation gives \(x=y=\varphi^{-1}\), consistent with the source's exact maximum-sum point.

## originality

PASS

The focal paper gives the exact two-dimensional union, proves the symmetric maximum-sum point, and explicitly says the curved boundary in Figure 3 is sampled numerically by maximizing weighted conditional entropies over the input distribution. Its full text does not supply the submitted analytic odds relation or unique involution. Focused Resultary and web searches did not locate this \(\psi(x)\psi(y)=1\) parametrization in earlier Blackwell secrecy literature.

## value

PASS

The Blackwell channel is the focal explicit example in the new confidential-broadcast capacity paper. Replacing repeated two-dimensional numerical support optimization by a unique one-dimensional analytic involution gives a natural exact description of the entire Pareto curve and recovers the known golden-ratio point as a special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
