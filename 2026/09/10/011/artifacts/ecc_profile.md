# Exact eccentricity profile ecc(t) of J_a (target-directed: radius vs diameter)

## Claim
By join symmetry (X=S^2 homogeneous, Y=S^1_a homogeneous), ecc(p) depends only
on join parameter t. Let c = cos(a/2) (<=0 iff a>=pi). Then:
  (i)  if a <= pi: ecc(t) = pi - t;
  (ii) if a >  pi: ecc(t) = acos(-sqrt(cos^2 t + c^2 sin^2 t)).
Consequences: diam = ecc(0) = pi for all a (antipodal t=0 pair);
radius r(a) = min_t ecc(t) = ecc(pi/2) = max(pi/2, a/2).

## Proof
For p=(·,·,t), q=(x',y',t'): cos d = cos t cos t' cos dx + sin t sin t' cos dy,
dx in [0,pi], dy in [0,a/2]. Eccentricity = max over (t',dx,dy) of d, i.e.,
minimize C = cos t cos t' cos dx + sin t sin t' cos dy.
- dx choice: min at cos dx = -sgn(cos t cos t') (boundary ±1 since dx ranges
  full [0,pi] for t>0... at t'=pi/2 cos t'=0, dx irrelevant). So first term
  contributes -|cos t cos t'| = -cos t cos t' (t,t' in [0,pi/2], cos>=0).
- dy choice: min of cos dy over dy in [0,a/2]. If a<=pi: a/2<=pi/2, cos dy>=0,
  min at... we minimize C: coefficient sin t sin t'>=0, so take SMALLEST cos dy
  = cos(a/2) = c>=0. Then C_min(t') = -cos t cos t' + c sin t sin t'
  = -cos(t+t'+phi)-type; d/dt': derivative cos t sin t' + c sin t cos t' >= 0
  for t'>0? At t'=0: C=-cos t; increasing t' raises C? dC/dt' = cos t sin t' +
  c sin t cos t' >= 0 on [0,pi/2] (all terms >=0 since c>=0). So C minimized at
  t'=0: C=-cos t, ecc(t)=acos(-cos t)=pi-t. With t=0: pi (diameter); t=pi/2:
  pi/2 (radius for a<=pi). ∎ (case i)
- If a>pi: c<0, cos dy ranges [c,1], min cos dy = c. C(t') = -cos t cos t' +
  c sin t sin t'. Minimize over t' in [0,pi/2]: dC/dt' = cos t sin t' +
  c sin t cos t' = 0 iff tan t' = -c tan t (using c<0, both sides >=0).
  Optimal t'* = atan(-c tan t) in (0,pi/2). Value: write C = -(A cos t' + B sin t')
  with A=cos t, B=-c sin t>0: min = -sqrt(A^2+B^2) = -sqrt(cos^2 t + c^2 sin^2 t).
  Hence ecc(t)=acos(-sqrt(...)). At t=0: acos(-1)=pi (diameter, all a). At
  t=pi/2: acos(-|c|)=acos(cos(a/2))=a/2 (since a/2 in (pi/2,pi]).
  Min over t: t=pi/2 (sqrt-term smallest? d/dt of sqrt-term: -2cos t sin t(1-c^2)
  <=0, so sqrt decreases in t, -sqrt increases, acos decreases: min at t=pi/2).
  Radius = a/2 for a>pi. ∎ (case ii)

## Verification
check_eccentricity.py: closed form dominates brute-force grid max (gap in
[-1e-9, 0.02], grid under-resolution only) across a in {0.5,...,2pi}, t grid;
radius formula max(pi/2,a/2) confirmed to 1e-3. Analytic proof above is primary;
script is a consistency check.

## Target significance (audit, not substitute)
- Diameter f(a)=pi constant: reconfirmed as ecc(0) in a full profile.
- The ONLY kink is radius at a=pi (r=max(pi/2,a/2)); a diameter-pinned a_c with
  diam=pi/2 cannot exist. Grove–Petersen-type radius framing would threshold at
  pi, a different theorem with a different constant — not developed (would be a
  substitute, out of scope in target phase).
