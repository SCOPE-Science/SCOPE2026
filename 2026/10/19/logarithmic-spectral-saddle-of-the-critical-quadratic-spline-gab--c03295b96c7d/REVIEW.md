# Independent mathematical audit

## correctness

PASS

The critical unit-lattice Zak map sends the shifts and modulations to the orthonormal Fourier characters times Zg, so Parseval gives the multiplier |Zg|² for the stated unit-integral window. Expanding the three Zak terms gives H=1-V+V²T²/4. Its V derivative is at most -1/2; together with the independent laws of T and V this justifies conditioning and the CDF and density formulas, including absence of atoms. The only interior critical value is the saddle at (0,1/2), with x=0 and x=1 identified. Its local quadratic form is -2u²+π²w²/2; rescaling to q²-p² gives area factor 1/π, and the product-coordinate coarea integral contributes log(1/|s-1/4|)+O(1). The Jacobian error is integrable uniformly there. To check the lower-edge remainder directly, write z=1-v_s(t). Then s-t²/4=z(1-t²/2+t²z/4), uniformly with t≤2√s, z=O(s). In the density put t=2√s r; the integral is (1/π) times the integral of (1-r²)^(-1/2) with relative error O(√s). This gives 1/2+O(√s) and the stated resolvent remainder. At the upper edge v_s(t)=(1-s)(1+O(1-s)) uniformly and the integral gives 1/(π√(1-s)). The product moments give 11/20, and the full essential range and atomless level sets give the stated multiplication-operator conclusions. Step 3's C² wording is correct for H, not for the underlying spline window g, which is only C¹. The frozen verify_b3.py and verification_output.txt provide quadrature and finite sampling corroboration, not proof or an independent replay.

## originality

PASS

The supported distinct claim is the quantitative spectral measure for this unit-integral B3 at a=b=1: the one-dimensional law, all singular levels with their exact normalized coefficients, and the regularized inverse mean. The unique Zak zero, critical non-frame behavior, multiplier framework and the general two-dimensional Morse-saddle mechanism are not new. The strongest inspected primary and indexed comparisons concern zero sets and frame bounds, not the measure near an interior level or its quantitative tails.

## value

PASS

At critical sampling the zero lower frame bound indicates noninvertibility but says nothing about how much fiber area has poorly conditioned response. The exact lower-tail constant controls the normalized regularized inverse, and the interior singularity and two different edge scales give quantitative structure independent of the spectral range. These are motivated invariants of a standard spline and critical Gabor operator, not values on an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
