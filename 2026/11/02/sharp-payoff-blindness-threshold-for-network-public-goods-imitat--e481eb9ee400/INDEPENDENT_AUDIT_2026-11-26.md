# Independent mathematical audit

## correctness

PASS

The frozen iff is false at C4, r=9, epsilon=0: (I+A)^2=I+2J (J all ones), so pi_x−pi_y=(r/3−3)(s_x−s_y)=0. Its lines 30 and 75 incorrectly infer a nonzero witness from attainment of a possibly zero maximum; the frozen verify.py tests maximum values only and does not include r=9. The repaired iff is Theta=0 or epsilon>Theta. In the shared-pool model the accumulated benefit is r(I+A)^2s/(d+1), and h_x=a>=0,h_y=−a with zero total contrast. The free signs set separately attain H and 2a−H, and complementing spins negates the entire payoff difference. Thus Theta is exactly the attained maximum. At a positive maximum equality retains a nonzero comparison; a zero maximum is neutral for every admissible cutoff. Independently checked L>=6 stencil support: positive coefficients 3 at x, 2 at the two diagonals away from y, and four ones, reflected to the negative side, giving endpoints −5,11; the two affine magnitudes cross at 25/3. K5 has equal benefits and a difference of magnitude 5. Regular ordered-edge symmetry gives a bounded count martingale and connectedness supplies a positive-probability absorption path, hence b/n. Ran the newly written repairs/3/verify.py (not the uploaded script): direct group sums confirm C4 and K5 equality cases and above-threshold behavior; full free torus stencils match at L=6,7,10. The all-graph proof is independent of these finite tests.

## originality

PASS

The repaired claim is the exact maximum-contrast expression and complete statewise neutrality criterion (with torus specialization), not the prior thresholding rule, accumulated-payoff convention or classical voter formula.

## value

PASS

The exact maximum gives a concrete state-independent calibration for genuine neutrality rather than weak selection, with different cutoffs on equal-degree graphs. Retaining the zero case prevents misclassifying a genuinely payoff-independent dynamics even without active thresholding. The torus contrast and general fixed-cutoff criterion survive intact with the corrected boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
