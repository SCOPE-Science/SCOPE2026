# Independent mathematical audit

## correctness

PASS

The equilibrium manifold follows directly because at \(x=m=v=0\) the stored maximum \(V>0\) is unchanged. Since the current second moment is strictly below \(V\), the max branch is locally inactive. Differentiating the actual four-state recurrence gives the submitted Jacobian: a \(2\times2\) position-momentum block of determinant \(\beta_1\) and trace \(1+\beta_1-c\), plus eigenvalues \(\beta_2\) and \(1\). Jury's criterion reduces exactly to \(0<c<2(1+\beta_1)\); the boundary factorization, negative-discriminant interval, constant conjugate modulus and large-\(V\) limit then follow algebraically. An independent symbolic reconstruction of the block characteristic polynomial matched the stated quadratic.

## originality

PASS

The defining AMSGrad paper introduces the running maximum of past second moments and proves regret/convergence properties, but does not classify the constant-step optimizer-state equilibrium manifold or its leaf-dependent transverse spectrum. The later convergence-correction paper likewise concerns regret inequalities rather than this local autonomous spectrum. Focused semantic searches did not find a published same-object theorem with the sharp memory threshold or damping plateau.

## value

PASS

The retained maximum is the defining structural modification of AMSGrad. Showing that it labels a continuum of equilibrium leaves, creates a sharp stability threshold, a momentum-controlled damping plateau, and an over-damped slow-memory regime gives a motivated local dynamical interpretation of that state variable rather than a routine normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
