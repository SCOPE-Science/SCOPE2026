# Independent mathematical audit

## correctness

PASS

With Q=-L, the Padé series has positive coefficients in degrees 1–5, zero in degree 6, and -1/1728 in degree 7. A path-distance d pair has a unique length-d walk; at distance 6 its degree-seven matrix power is strictly negative (one negative diagonal stay, no length-seven all-edge walk by parity), so the first nonzero Padé contribution there is positive. Diagonal continuity and finiteness then settle n<=7, including P1. At distance 7 the leading entry is -h^7/1728, proving obstruction on every larger path. For P8 the denominator matrix is positive definite and the explicit scalar D is positive on h>=0. An independent exact replay (python3 /workspace/replay_pade_path.py) used the Padé Taylor recurrence and powers of Q to compute coefficients of 4D times the step through degree 16, without running the interpolation checker. The degree-15 and -16 terms vanish in all entries; multiplying the degree-14 truncation by the degree-two denominator gives the exact degree-at-most-16 polynomial identity, since their Taylor coefficients agree to that degree. This reproduced both exceptional numerators, both rational root brackets, the decimal locations within 10^-15, and the 40+20 sign classes. Descartes gives one simple positive root for each controlling polynomial; for each other numerator with one sign change, the positive value at 9/2 and near zero put its sole positive root beyond 9/2. Thus on the closed positive window all other entries are strictly positive, with just the indicated pair vanishing at each endpoint. Outside it one controlling entry is strictly negative, while at h=0 the step is I. The exact certificate is not a sampling argument and is separate from the arbitrary-n proof.

## originality

PASS

The negative seventh coefficient and its small-step positivity-loss mechanism are prior. The earlier general CTMC result already gives small-step positivity through dimension seven, a dimension-eight obstruction and a disconnected window for a different directed generator. The supported distinct result is the exact complete positivity interval for the canonical symmetric reflecting P8, with different controlling polynomials and entry endpoints, plus the explicit path specialization on the obstructed side. Neither generic bounds nor a window for a directed example determine this one.

## value

PASS

The unit reversible path is a canonical conservative heat discretization, and eight is the first size where arbitrarily small steps fail. The exact window is useful for deciding positivity at any chosen step in this first obstructed geometry: it proves that decreasing the step can destroy positivity, and shows that making it large again also fails by a different entry. Neither A-stability nor a directed-generator example can answer that question for the reflecting path.

The dated certificate retains the supplied scientific assessment, sources and limitations.
