# Same-model review

## Correctness
PASS. Restricting the two-dimensional quadratic \(F(u,v)=\tfrac{L}{2}(q u^2+v^2)\) to the invariant axis \(v=0\) gives the exact original-FISTA scalar map with contraction \(r=1-q\). The first four points reduce to \(x_1=rx_0\), \(x_2=r^2x_0\), \(x_3=r^2A(r)x_0\), and \(x_4=r^3B(r)x_0\), with \(A(r)=(1+\beta_2)r-\beta_2\) and \(B(r)=(1+\beta_3)A(r)-\beta_3\). Since \(|A(r)|<1\) for \(0<r<1\), no earlier objective increase is possible. The fourth comparison factors exactly into two quadratics whose positive roots give the displayed interval. At \(r_0=\beta_2/(1+\beta_2)\), \(A(r_0)=0\) and \(B(r_0)=-\beta_3\), proving the exact hit-and-leave statement. High-precision replay agrees with all formulas and sign regions.

## Originality
PASS with stated residual risk. The 2009 primary paper gives the recurrence and global rate but not this scalar finite-horizon classification. The 2009 monotone-FISTA follow-up explicitly says original FISTA is not monotone and introduces a monotone variant, but does not give the sharp fourth-point interval or an optimizer-hit-and-leave resonance. Liang--Fadili--Peyre explain local FISTA oscillation spectrally, but the inspected full text does not state this exact first-rise boundary. Targeted published-finding corpus searches found no implication-equivalent item.

The closest previously recorded result is the constant-momentum adaptive-restart resonance with opaque identifier `8ace13eb-0886-452f-b57a-0355a9e2dc4d`. That result concerns a different fixed-\(\beta\) model and detector nonactivation; it neither uses the original Beck--Teboulle varying momentum sequence nor implies the sharp \(x_3\)-to-\(x_4\) objective-rise window proved here.

Residual risk: a lecture note, implementation note, thesis, or unindexed discussion could contain the same first-four-iterate calculation or an equivalent curvature parameterization.

## Value
PASS. FISTA's nonmonotonicity is well known, but an exact earliest-onset classification is a natural finite-horizon question rather than an arbitrary parameter slice. The result gives a sharp curvature interval, proves that the first three comparisons cannot rise, and identifies an interior condition-number value at which the bare recurrence reaches the unique optimizer exactly and then leaves it. This isolates a concrete mechanism behind the motivation for monotone or restart variants and shows that the phenomenon already occurs on an invariant eigendirection of a very well-conditioned quadratic.

Same-model review: passed. Independent audit: not yet performed.
