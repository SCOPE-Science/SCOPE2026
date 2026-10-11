# Independent mathematical audit

## correctness

PASS

For each translation, the STFT row is the Fourier transform of at most two point masses. If one point is occupied the row has all \(N\) frequencies; if two are occupied it loses exactly \(d=\gcd(a,N)\) frequencies precisely when the coefficient ratio is an \(L=N/d\)-th root. Thus minimizing total support is maximizing simultaneously good directed internal edges of the step-\(a\) cycles. All edges of a proper occupied path, and of a complete even cycle, can be made good by alternating phases; a complete odd cycle must lose exactly one because the product of the required ratios would be \(-1\). Hence the optimum number of good edges is \(E_a(S)-Q_a(S)\), proving the exact formula. Componentwise minimization gives global \(N\) only at \(L=2\), and otherwise \(2N\) exactly for singleton support. The package's exhaustive small-\(N\) replay is consistent with the analytic proof.

## originality

PASS

Originality passes. Krahmer--Pfander--Rashkov give universal and support-size lower bounds and generic-window results, but not the exact prescribed-support minimum for the fixed equal two-point window on every composite cyclic group. Nicola completely classifies equality in the universal \(N\)-point STFT bound; this subsumes the antipodal \(L=2\) equality branch but does not determine the fixed-window minima above \(N\) or the exact value for each support set. The audited odd-cycle defect term is therefore not implication-covered.

## value

PASS

Equal two-point windows are the simplest genuinely overlapping sparse Gabor windows. The theorem gives every prescribed signal support an exact optimum and identifies the composite-order obstruction as cycle parity, while also locating exactly when the universal bound is attainable. This is a natural complete structural classification rather than a narrow numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
