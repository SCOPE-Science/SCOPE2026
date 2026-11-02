# Independent mathematical audit

## correctness

PASS

For positive m1,m2,k,γ, after quotienting the common translation zero mode the 3D state has exact cubic P(s)=s³+gs²+s+θg with θ=m1/(m1+m2)∈(0,1), ω²=k(1/m1+1/m2), g=γ/(m1ω)>0. Routh–Hurwitz holds since g>θg. A real root -r uniquely induces g=G(r)=r(1+r²)/(r²+θ); other pair mean decay α=r(1-θ)/(2(r²+θ)). The derivative numerator r⁴+(3θ-1)r²+θ and discriminant -4θg⁴+(1+18θ-27θ²)g²-4 have real-branch phase separation at θ=1/9 (discriminant of quadratic in g²=(1-θ)(1-9θ)^3). In one-complex-pair regimes the slow exponent is min(r,α), with α peaking at r=√θ and crossing r at r_c²=(1-3θ)/2; transition of maximizing bottleneck at θ=1/5. Below θ=1/9 the three-real-root interval ends at the slow-pair double collision r²=u_-=(1-3θ-√((1-θ)(1-9θ)))/2; monotonic root-branch analysis puts unique global optimum there. Consequently g*=(1+3u_-)/(2√u_-), R*=√u_- for θ<1/9; g*=3√((1-3θ)/2), R*=√((1-3θ)/2) for 1/9<=θ<=1/5; g*=(1+θ)/(2√θ), R*=(1-θ)/(4√θ) above. Triple defective root at θ=1/9 and continuous phase boundary at 1/5 are correctly normalized. Defects allow polynomial transients, so R is spectral exponential supremal rate, not a uniform finite-time estimate at exact R. Fresh symbolic discriminant/derivative derivation and 663 numerical eigen-spectrum comparisons for candidate vs neighboring damping parameters corroborate branch formulas; uniqueness for the continuum follows from the proof, not samples.

## originality

PASS

Classical spectral abscissa minimization, defectivity and damping design are prior knowledge. Freitas–Lancaster 1999 study less constrained damping-matrix optimization, not one grounded dashpot of a translational dimer; Dolfo–Vigué 2018 full text treats anelastic damping/topology rather than the strictly viscous dashpot free dimer; Arnold–Gendelman–Zharnitsky 2026 abstract concerns more general two-degree-of-freedom damping matrix and multiple eigenvalues, not the exact θ=1/9,1/5 unique line of constrained global optima. Main–Krenk 2005 and Cox–Overton 1996 likely relevant but only metadata/abstracts available, so no full-text NOT_COVERING claimed and prior specialized solutions remain a material risk. Targeted Resultary and published searches did not locate both exact mass-fraction thresholds. Best-of-knowledge PASS for the constrained three-regime law and global uniqueness; not a priority certificate.

## value

PASS

For a physically natural free translating spring-linked dimer, a damper can attach to one body but not the center of mass; tuning this single grounded dashpot is a genuine constrained engineering/mathematical optimum distinct from arbitrary matrix damping. Exact sharp universal mass thresholds 1/9 and 1/5, triple/double exceptional-point transitions, and unique global decay optimizer give structurally meaningful information, including that an equal-real-part optimum need not be defective. No claim for transient energy envelope, general damping matrices, forced or nonlinear oscillators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
