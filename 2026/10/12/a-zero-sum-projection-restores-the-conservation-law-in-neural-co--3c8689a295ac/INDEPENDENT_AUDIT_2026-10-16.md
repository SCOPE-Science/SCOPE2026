# Independent mathematical audit

## correctness

PASS

The published closed SIR model has f_dist=(-βSI,βSI−γI,γI) and therefore 1^T f_dist=0 identically. For hybrid xdot=f_dist+λf_NN, differentiating M=1^Tx gives Mdot=λ1^Tf_NN; unconstrained three-output residual cannot guarantee conservation. For training targets Y=d x_obs^SG/dt−f_dist(x_obs), direct summation and linearity of Savitzky–Golay differentiation give 1^T Y=d(1^Tx_obs^SG)/dt. The source perturbs and clips observations separately; it does not enforce fixed observed totals, so preprocessing may inject unnecessary normal-to-simplex learning signal. In the controlled same-structure parameter-mismatch setup r=f_true−f_dist has 1^Tr=0. P=I−(1/3)11^T is orthogonal projection onto that tangent plane; P²=P=P^T and 1^TP=0, so its use for NN outputs ensures mass invariance, and ||PY−r||²=||Y−r||²−||(I−P)Y||²≤||Y−r||² pointwise. Independent exact rational checks verified P²=P, 1^TP=0 and representative zero-sum residuals. This establishes a guarantee, not empirical mass drift or performance improvement in source figures.

## originality

PASS

General invariant-preserving neural ODE architectures, projection of vector fields into conservation tangent spaces, and Pythagorean nonexpansiveness are established background; none is claimed invented here. The reviewed July 2026 Annuš–Kmeť specific hybrid method adds an unrestricted learned three-vector and trains on componentwise perturbed/clipped observations; its own discussion proposes physics constraints as future work. The exact combination of the source residual-target sum diagnostic and non-worsening projection on its known parameter-bias residual is a model-specific identified omission and correction, not an assertion that zero-sum projection is a new general algorithm. Literature priority remains best-of-knowledge.

## value

PASS

In a concrete recent controlled epidemic-modeling pipeline, violation of the fundamental closed-population invariant is scientifically consequential: the correction identifies exactly which component of the learned target can be pure preprocessing artifact and gives a guaranteed non-worsening tangent estimate of the known true same-structure residual. The argument is algebraically simple and uses textbook orthogonal projection, but it diagnoses and resolves a substantive structural model/data mismatch rather than an arbitrary tiny numerical check or a generic rebranding of projection. Scope is carefully bounded and no claimed empirically improved predictions are invented.

The dated certificate retains the supplied scientific assessment, sources and limitations.
