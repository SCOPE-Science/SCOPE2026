# Independent mathematical audit

## correctness

PASS

For each fixed nonzero starting vector, singular updates have probability zero and rotational invariance makes the conditional log multiplier law independent of the past. The norm multiplier is between min(1,|1-bS|) and max(1,|1-bS|) with S=||u||^2, so the squared logarithm is integrable under the exponential radial density, even at S=1/b. The variance is positive since the multiplier is nonconstant on the Gaussian support. Circle averaging gives log((1+|1-bS|)/2); S/2 is unit exponential. The split at S=1/b, integration by parts with cancelling boundary terms, and evaluation give exactly the displayed E1/Ei expression. Differentiation is justified on compact positive b intervals; the derivative sign is that of 1-R(b), and the factor b^-1 exp((1/2-t)/b) makes R strictly decreasing from infinity to zero. Together with the limits Lambda(0+)=0 and Lambda(b)~log b as b goes to infinity, this proves unique minimization and a unique positive stability zero. The critical LIL gives unbounded positive and negative excursions of the log norm and hence norm liminf 0 and limsup infinity. The Gaussian second and fourth moments independently give the multiplier 1-2b+4b^2, with neutral endpoint 1/2 and minimizer 1/4. Replay: python3 /workspace/reproduction/5.py (mpmath and standard library; output 5.txt). Independent quadrature of the split expectation and its derivative reproduced the displayed digits and brackets at 65-digit working precision (not an interval certificate for the digits). A separate directed rational Taylor/Riemann bound certifies Lambda(1)>0.0236062 without relying on floating-point exp, placing the positive zero in the asserted domain. The theorem is pathwise for the stated fixed noiseless recursion; simulations or finite trajectories are not its proof.

## originality

PASS

Best-of-knowledge pass for the distinct planar analytic calculation: the closed E1/Ei rate and proof of unique rate optimum and positive zero, providing the sharp evaluated planar boundary. The generic Gaussian logarithmic-multiplier formula and the existence of a regime beyond the second-moment edge were already established for this same matrix family by Gürbüzbalaban et al.; they are not separate contributions here. The random walk at the critical root is a standard LIL consequence once the root and increment hypotheses are identified. The known mean-square identities are not new.

## value

PASS

The actual typical-trajectory rate and best constant step differ materially from the classical second-moment prescription. The explicit scalar evaluation and strict single-minimum proof resolve the natural full step-size optimization in the planar baseline and give the precise limit of almost-sure contraction, rather than asserting only the previously known existence of a gap. The scope is the homogeneous model; these rates cannot replace expected-error guarantees for a noisy or drifting optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
