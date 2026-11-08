# Independent mathematical audit

## correctness

PASS

For Q=[-1,1]^3 and U Haar uniform on S², the orthogonal shadow onto U-perp has circumradius R=max_{v in ±1³}||P_E v||=sqrt(3-min_v(v·U)^2). Sorting absolute coordinates a<=b<=c gives exactly min|±a±b±c|=|c-a-b|, valid also at chamber boundaries. Forty-eight symmetry chambers contribute 12/pi times the Haar density sin(theta)dtheta dphi for 0<=phi<=pi/4, theta<=atan(sec phi). The threshold |cos theta-(cos phi+sin phi)sin theta|>=t yields the disjoint positive and negative spherical regions B(t),J(t), with J activating only t<1/sqrt3. Expansion of h(phi)=sin phi/sqrt(1+cos²phi) near pi/4 and the threshold integrand gives J~9sqrt3/(4pi)(t*-t)^2, whose r-map derivative gives jump 36sqrt3/pi in F_R second derivative. Six coordinate-axis diamonds give lower F(sqrt2+eps)~6 eps²/pi; four transversal great-circle bands give the upper tail 4sqrt(3-r²)/sqrt3. Independent orthogonal-projection calculations, numerical 1D quadrature and uniform-sphere Monte Carlo agree; such numerical checks do not prove exact continuum geometry.

## originality

PASS

Best-of-knowledge, after implication-aware prior/source comparisons: No inspected prior theorem implies the signed-min CDF or its second derivative jump; the symmetry and spherical chamber proof provide the new calculation.

## value

PASS

The random planar shadow of a cube is a canonical fixed-dimensional integral-geometric model, and its full metric circumradius CDF has a genuine interior differentiability transition and sharp endpoint laws. Those features are finer than expected face counts, area/perimeter, directional width or dual section inradius, so the precise fact is a reusable natural probability law rather than a contrived finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
