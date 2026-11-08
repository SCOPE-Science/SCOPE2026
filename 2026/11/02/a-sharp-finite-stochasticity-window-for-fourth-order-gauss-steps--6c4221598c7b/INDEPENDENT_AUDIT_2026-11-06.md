# Independent mathematical audit

## correctness

PASS

PASS. The fixed conservative directed eight-cycle Q=S-I with S^8=I and row-generator convention has two-stage fourth-order Gauss/Padé endpoint rational map R(hQ)=[I+hQ/2+h^2Q^2/12][I-hQ/2+h^2Q^2/12]^{-1}. Since the scalar denominator zeros have Re>0 whereas spec(Q) has Re<=0, it is well-defined for all h>=0; Q*1=0 gives row sums one. Recomputed exact inverse in Q(h)[z]/(z^8-1), all eight cyclic numerator polynomials H_j and strictly positive denominator W(h); an independent exact SymPy check verified ALL eight factorization formulas. For j=0,4,5,6, coefficients ensure positivity for h>0. Each of P1,P2,P3,P7 has one positive zero by Descartes sign changes; exact rational brackets show P7 root in (1/2,3/5), P1 in (7/2,4), and P2,P3 still negative at 4. Thus c7<0 for 0<h<h_minus, c1<0 for h>h_plus, and every cyclic probability is positive between; at the two endpoints the respective active probability vanishes. Positive endpoints h_minus=6alpha, h_plus=6beta are uniquely specified by given degree-6 and degree-12 primitive polynomials. Independent exact checks and numerical roots gave h_minus≈0.5122515443725, h_plus≈3.5271974662694. The ten finite rational matrices from source verify.py are corroboration, not the continuum proof.

## originality

PASS

Best-of-knowledge, theorem/implication-based comparison of relevant primary literature; a failed search by itself does not prove historical priority. Closest known published results address different parameters/objects or only more general frameworks.

## value

PASS

PASS. Fourth-order A-stable Gauss time stepping can preserve row mass yet violate Markov positivity both for arbitrarily small and sufficiently large steps; the full exact positive window on an irreducible conservative cyclic generator is a natural sharp numerical-analysis invariant. The algebraic boundary and all-step if-and-only-if complement prior absorbing pure-birth eight-state results without merely repeating the small-step obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
