# Independent mathematical audit

## correctness

PASS

Continuity and the delta jump condition give the exact monotone scalar equation k_d tanh(k_d d)+q_d tanh(q_d d)=alpha. Subcritically, expanding at the unique full-line root a and using b>a shows k_d-a=(2ab/alpha)e^(-2ad)(1+o(1)), which converts to the stated energy coefficient. At criticality, the root equation first forces k_d d to zero and y_d d=O(e^(-2alpha d)); expanding both tanh terms in y=k_d^2 yields y(d+1/(2alpha))=2alpha e^(-2alpha d)(1+o(1)). Independent numerical roots reproduced the subcritical rescaled constants within about 0.6 percent or better and the critical constants to better than 1e-6 in the tested cases.

## originality

PASS

Exner's Lemma 3.1 gives only a coarse O(d^{-1}) lower estimate for the finite Neumann transverse energy and immediately remarks that the actual Neumann error is exponentially small. It does not state the biased leading coefficient, and it does not analyze the critical threshold resonance where an extra inverse-length prefactor appears. The audited scalar root expansion therefore sharpens an explicitly identified source gap.

## value

PASS

The result turns an explicitly qualitative source remark into sharp finite-volume asymptotics and identifies a genuine threshold change caused by the zero-energy resonance. That distinction is directly relevant to spectral bracketing and truncation-error estimates near critical bias.

The dated certificate retains the supplied scientific assessment, sources and limitations.
