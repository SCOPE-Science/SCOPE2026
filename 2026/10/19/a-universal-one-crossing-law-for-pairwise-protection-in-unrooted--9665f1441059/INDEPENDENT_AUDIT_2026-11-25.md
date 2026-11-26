# Independent mathematical audit

## correctness

PASS

An edge contributes iff both leaf sides have a survivor. With independent risks and no protection its expected fraction is (1−Q_A)(1−Q_B), with side products set to zero if a taxon on that side is protected. The mixed protection difference is Q_AQ_B if x and y are separated and −Q_A(1−Q_B) if both are on side A. Dividing by the positive product Q over all taxa therefore yields total tree length minus the sum of positive lengths divided by their away-side risk products on off-path edges. Each away side is nonempty, strictly increasing in product risk, and tends from 0 to 1. A third leaf forces an off-path edge; the normalized interaction consequently increases continuously and strictly from −∞ to the positive x–y distance. These limits concern H/Q, not H itself. With only two leaves H=d_T(x,y)Q>0; with a protected anchor each edge is a constant plus a nonnegative weighted coverage indicator. The three-leaf star reduces to q²(3q−1). Independently enumerated natural survivors using unions of pair paths on a different weighted four-leaf tree: heterogeneous risks (t,t²,t,t³) give H_02=t⁷(21−3/t²−5/t³), with exact sign and anchored checks. Replay: python /workspace/calculations/reproduce_frozen.py (check phylo). The finite instance does not prove the general crossover.

## originality

PASS

Best of current knowledge: credit the known heterogeneous independent-extinction edge expectation and related single-taxon protection formula, not as new results. The supported contribution is the strict and unique negative-to-positive crossover for the initial unanchored interaction of any pair along every full-range increasing heterogeneous risk path, with its two-leaf exception. The anchored coverage observation is not separately novel.

## value

PASS

A single-protection ranking can miss complementarity in the unanchored objective. The theorem specifies exactly when the interaction changes direction without a shared risk law, and shows why a fixed anchor eliminates the positive regime. It is a structural characterization of the risk model, not evidence of particular intervention efficacy or a multi-taxon optimization guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
