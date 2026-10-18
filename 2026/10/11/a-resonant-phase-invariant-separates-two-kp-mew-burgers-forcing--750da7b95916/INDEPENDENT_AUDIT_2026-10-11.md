# Independent mathematical audit

## correctness

PASS

From \(W\dot{}=i\omega_1W\) and \(V\dot{}=i\omega_2V\), the derivatives of \(|W|^2,|V|^2\) vanish and \(\dot K=i(\omega_2-2\omega_1)K=0\). The printed forcing yields \(W=e^{i\omega_1t}\), \(V=e^{2i\omega_1t}\), so \(K=1\) for every common time translate. The panel initial state \((w,p,z,q)=(4/5,3/5,4/5,3/5)\) gives \(W=(4+3i)/5\), \(V=(3+4i)/5\), and exact multiplication gives \(K=(117-44i)/125\). The retrieved source Figure 11 caption confirms these oscillator initial values and frequencies. The actual verify.py was inspected, and independent symbolic Lie-derivative/rational checks reproduced the conserved quantities and exact value; no Lyapunov numerics are used.

## originality

PASS

The primary publisher page identifies the two different numerical setups; the additional resonant first integral and its exact value are not among the accessible source statements. Earlier periodic forcing dynamics work is a precursor, not an analysis of this exact six-dimensional initialization. The page-level source comparison and all-op algebra substantiate the source-specific mismatch, subject to uninspected publisher full text and unavailable index.

## value

PASS

The relative phase is a genuine invariant of the resonant autonomous extension, so using different leaves undermines a specific published comparison of bifurcation and Lyapunov diagnostics unless phase-independence is proved. This is a motivated source-specific consistency result, not a routine computational typo.

The dated certificate retains the supplied scientific assessment, sources and limitations.
