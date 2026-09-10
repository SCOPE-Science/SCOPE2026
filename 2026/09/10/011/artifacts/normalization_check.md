# Normalization / re-interpretation check (target-directed, closes escape routes)

## 1. "Circle of length a" is the only consistent reading
- Admitted statement: "circle S^1_a of length a", a in (0,2pi].
- Y=S^1_a has diam = a/2 <= pi on this range; 1-dim curv>=1 iff length<=2pi.
  Join theorem hypotheses (factors curv>=1, diam<=pi) hold for the WHOLE range.
- Alternative reading "radius a" (length 2pi·a) would give diam(Y)=pi·a, which
  exceeds pi for a>1 and violates curv>=1 (length 2pi·a>2pi) over most of the
  stated range (1,2pi]. It would make J_a undefined as curv>=1 join for a>1,
  contradicting the admitted "Each J_a is closed 4-dim curv>=1". So rejected;
  length reading is forced.

## 2. No rescaling in "metric spherical join"
- Standard spherical join metric is unrescaled (cosine formula above); factors
  embed isometrically (verified exact). Any global rescaling (e.g., normalizing
  diam to 1) is absent from the admitted statement. Introducing one would change
  the object and the constant (pi/2 scales too), i.e., a different theorem.
- Within the stated object, the t=0 antipodal pair is well-defined: at t=0 the
  Y-coordinate collapses, so p_i=(x_i,·,0) depends only on x_i; x1≠x2 antipodal
  gives two distinct join points at distance acos(cos pi)=pi. No identification
  loophole.

## 3. Curvature hypothesis double-check (1-dim factor)
- Complete 1-dim Alexandrov space with curv>=1: circle of length L<2pi, resp.
  <=2pi (closed). Our Y lengths a in (0,2pi] satisfy this. Segment/suspension
  edge cases irrelevant. Join curvature conclusion stands, so the obstruction
  cannot be dismissed as "join not curv>=1, hence diam bound inapplicable" —
  the join IS curv>=1 and its diameter IS pi.

## 4. Bottom line for target
- Under the unique consistent reading, f(a)=pi constant is exact, not an artifact
  of normalization. The premise "strict monotonicity => unique a_c with diam=pi/2"
  fails mathematically, not notationally.
