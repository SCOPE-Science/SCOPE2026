# Independent mathematical audit

## correctness

PASS

PASS: For all integers d>=2, from frozen RESULT.md 607879e derived identity z-a_J^2(1-(z-c_J)^2/b_J^2)=((d+1)^2/4)(z-z0)^2, z0=(d-1)/(d+1), hence John candidate lies inside capped quadratic epigraph and touches one pole and a rim sphere. Under ball normalization the pole plus rim measure with weights 1/(d+1),d/(d+1) has mean 0 and covariance I/d, so the John contact theorem proves global maximality. For L candidate A=d/sqrt(d^2-1), B=C=d/(d+1), the quadratic enclosure g(z)=z/A^2+(z-C)^2/B^2 satisfies g(0)=g(1)=1 and g(z)-1=((d+1)^2/d^2)z(z-1)<=0; normalized bottom-vertex/top-rim contacts have the same moment certificate and also belong to the strict subset cone, proving identical unique Löwner ellipsoid. Checked symbolic identities in dimension parameter and volume semiaxis ratio yielding ((d+1)/2)((d+1)/(d-1))^((d-1)/2), asymptotic e*d/2. Numerical optimization in supplied verify.py is supplementary only.

## originality

PASS

PASS, best-of-knowledge for the paraboloid's complete John/Löwner pair and the exact equality of the larger cap's Löwner ellipsoid with its smaller cone. Güler–Gürtuna explicitly solve truncated-cone outer ellipsoids; this covers cone-only geometry but cannot logically imply the larger quadratic cap shares that enclosure without an additional containment proof; their discussion expressly omits inscribed ellipsoid for the second class.

## value

PASS

PASS: A canonical all-dimensional compact quadratic epigraph and its strictly contained cone having an identical sharp enclosing ellipsoid is a structural extremal-geometric phenomenon. The complementary John contact geometry and exact all-dimensional volume-ratio limit give a reusable benchmark for convex optimization and affine geometry, not an arbitrary computational slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
