# Review: two-frequency reconstruction of a positive two-layer climate model

## Correctness — PASS

The exact transfer \(H(i\omega)^{-1}=\lambda+i\omega C+\gamma i\omega	au/(1+i\omega	au)\), with \(	au=C_D/\gamma\), follows from elimination of the deep-layer phasor. The two impedance differences are strictly positive, with ratio \(b/a=	au\); this uniquely forces all four parameters. Substitution proves sufficiency of strict positivity of reconstructed \(C,\lambda\), and a continuous parameter family proves one-frequency ambiguity (also with known equilibrium gain). The perturbation bound follows from one division identity. A separate symbolic calculation confirmed the difference and reconstruction algebra, and the standalone forward/inverse checker passed 12,000 well-conditioned randomized configurations and the exact rational witness. These tests do not prove uniqueness; the algebra does.

## Originality — PASS, historical priority provisional

MacMynowski, Shin and Caldeira (2011; doi:10.1029/2011GL048623) published the two-box frequency response and multi-period fitted comparisons, establishing the transfer-function setting. Geoffroy et al. (2013; doi:10.1175/JCLI-D-12-00195.1) provide analytic step/ramp response and modal calibration. Soldatenko and Colman (2022; doi:10.16993/tellusa.40) derive the two-box spectral transfer and sensitivity formulas. Bortner and Sullivant (2021; arXiv:2107.06271) prove broader RC-network full-response local identifiability criteria. Full-response identifiability, use of phasors and the two-layer model are excluded from the novelty claim; the asserted contribution is the exact **two-sample minimality**, globally positive *realization criterion*, parameter formulas, DC-plus-one-frequency ambiguity, and exchange-time sensitivity bound. Available full-text sections and mathematical-claim searches identified no statement implying this combined finite-data result. A generic rational-interpolation or inverse-RC-network theorem may cover it, and the complete 2013 original appendix could not be read; those are residual priority risks.

## Mathematical value — PASS

Two calibrated harmonic experiments give the smallest exact finite measurement design that separates four physical climate-response parameters; the explicit positivity test detects data that the ideal model cannot realize. The result is motivated by interpreting upper versus deep thermal storage and exchange rather than by a numerical parameter coincidence. The one-frequency/DC nonidentifiability class explains why a seemingly adequate experiment cannot identify the deep ocean and feedback uniquely, while the sensitivity bound identifies a concrete ill-conditioning mechanism. The theorem supplies no performance guarantee for noisy observational calibration, and climate dynamics need not obey a fixed linear two-box law.

Self-review: passed. Independent audit: not yet performed.
