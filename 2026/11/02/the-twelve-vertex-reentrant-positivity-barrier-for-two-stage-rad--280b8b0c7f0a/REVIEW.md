# Independent mathematical audit

## correctness

PASS

PASS: For the exactly normalized two-stage Radau endpoint R(z)=(6-2z)/(z²+4z+6), the three Laplacian eigenspaces on K_{s,...,s} give the diagonal, within-part, and cross-part entries stated in the frozen RESULT.md. The cross-part sign is 1-R(mt)>0, while a direct rational identity makes all within-part offdiagonals positive for t>0. The scalar minimum rho=(5-3sqrt(3))/2 gives 1+10rho>0 for n<=11. At t=6/(m-1) diagonal is nonpositive for n>=12 and strictly negative except (m,s)=(2,6), where t=8 has exact numerator -500/8313. The diagonal numerator equals quartic F_{m,s}; its coefficient signs have at most two positive roots by Descartes, and the two sign crossings force exactly two simple roots. Independent SymPy algebra reconstructed F and the offdiagonal identity and isolated two positive roots for (2,6),(3,4),(12,1),(3,5),(4,3),(5,3),(100,1), with none for checked n<12. The finite tests do not replace the all-m,s argument.

## originality

PASS

PASS (qualified): general absolute-monotonicity/SSP work supplies conditions for stability functions, not an exact entrywise characterization for this specific multipartite Laplacian. Existing Resultary work on Gauss [2/2] Padé and Crank–Nicolson analyzes different rational functions. I found no decisive same-map stronger classification; an unindexed Radau-specific analysis remains possible.

## value

PASS

PASS: This is a sharp all-parameter classification for a canonical symmetric network family, with a surprising nonmonotone time-step positivity window and exact minimal vertex count 12. It reveals a concrete distinction between L-stability, classical SSP horizons and eventual endpoint positivity; the precise graph-family quartic can be reused when selecting integration steps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
