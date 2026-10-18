# Independent mathematical audit

## correctness

PASS

Reconstructed t*x_t=sum_{j<=t} z_j and z_t=t*x_t-(t-1)*x_{t-1}; the update z_{t+1}=[1-s(1-beta)]z_t-s*beta*x_t yields (1-q)(1-Aq)G_prime+s*beta*G=x_1 and the claimed closed form. Analytic coefficient transfer at q=1 for noninteger r, pole order m for integer r, and the singularity at 1/A establish rates and strict full-state boundary |A|<1 (beta=0 checked separately). At integer m=3,beta=3/4,s=4 independently iterated exact Fractions: x_1..x_4=(1,-1,1/3,0), with all later x zero and z=0 from t=5. These finite checks corroborate but do not replace the singularity proof.

## originality

PASS

The novel candidate is the exact beta-dependent scalar generating function, full-state boundary, and polynomial/geometric/finite-termination arithmetic trichotomy. The original Schedule-Free SGD paper supplies the update and empirical quadratic learning-rate enlargement, rather than this exact coefficient and resonance classification. A targeted Resultary semantic comparison identified the target itself and other scalar optimizer stability results, not a prior implication-equivalent theorem. Historical primal-averaging polynomial recurrence aliases remain a genuine risk.

## value

PASS

The exact stability ceiling and fragile finite annihilation conditions resolve a natural open quantitative question suggested by the base algorithm's quadratic experiments. It is a nontrivial asymptotic classification of a practical three-state update, with operationally important distinction between average x_t and full optimizer state; not an arbitrary parameter slice or mere transcription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
