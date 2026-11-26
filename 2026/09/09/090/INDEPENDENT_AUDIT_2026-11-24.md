# Independent mathematical audit

## correctness

PASS

Independently verified the repaired proof. E is bounded balanced convex, so its infinitesimal metric at zero equals the Minkowski norm by linear discs and complex Hahn–Banach plus Schwarz. For admissible f and A=df₀, metric monotonicity through the image gives |Av|≤m(v)≤|Av|/r. Consequently |Ae_i|≥r at the axes and |Av_±|≤1 for v_±=(√3/2,±1/√2) on ∂E. The average of the two squared norms is (3/4)|Ae₁|²+(1/2)|Ae₂|²≥5r²/4. The scalar map attains the bound since the Euclidean unit ball lies in E and x+y=(x+y²)+(y−y²)<5/4 on E. The original phase-diagonal optimization likewise works with a supremum over the open domain, equivalently a maximum over its closure. At a weak point, expanded as (1+u,v), the pure order ord(u) and mixed order 4ord(v) cannot cancel, so the normalized vanishing order is at most 4 for any germ, attained along (1,ζ). Ma's squares at p=(1,1), m=(1,2) are 3/4 and √3/2; the first axis bounds that map's inradius by √3/2, strictly smaller than the optimum. Read the frozen scaling_check.py, which supplies numerical corroboration only (finite/tolerance-based tests, not a proof); no uploaded code was run. No uniform bound, interior formula off the origin, or boundary-limit result is claimed.

## originality

PASS

The strongest earlier same-family source, DGZ Remark 7.2, raises a relationship with Ma's Jacobian-extremal maps but does not compute this origin value. Ma's formula was verified and actually yields an embedding with an insufficient inradius, so substituting into it does not give the squeezing optimizer. A later real mixed-power Banach–Mazur calculation obtains the reciprocal number and expressly relates it to this earlier record; real-linear maps and complex-linear maps require a comparison, not just a shared number. The strongest other directly relevant abstract, Zhong–Wang, assumes Shilov boundary transitivity, which fails for this ellipsoid; uninspected parts are a residual risk, not a negative finding. Pass is limited to the exact complex ordinary-squeezing value at the origin, not general metric linearization or a priority assertion about all ellipsoids.

## value

PASS

The quartic ellipsoid is the basic decoupled weak finite-type model in dimension two, and an exact interior origin value supplies a concrete calibration not furnished by near-boundary estimates or general symmetric-domain formulas. The geometry distinguishes the inscribed radius from the close determinant optimum in precisely the family highlighted by DGZ, and rules out the proposed 1/√2 origin value. These uses motivate the precise invariant beyond the ease of the final calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
