# Independent mathematical audit

## correctness

PASS

Project the centered edge cube orthogonally onto the cycle space of a three-path theta graph, with f_i path indicators and intrinsic Euclidean metric. With h=P/S, projected generators p_i=f_i-hg have lengths squared i-h and pairwise dot products -h; the zonotope is a six-vertex equal-radius hexagon with R²=(T-h)/4, Euclidean area sqrt S, and two central-triangle area fractions w_i=i(T-i)/(2S). Dirichlet barycentric triangle moments give I=R²/6 Σw_i(2+c_i) and J=R⁴/45 Σw_i(7+6c_i+2c_i²), reducing to the stated rational formula for J and the previously known I=(ST+P)/(12S). The upper deficit 9/5-J/I²=4(3P²+2S³)/(5(ST+P)²)>0. For a=x,b=x+y,c=x+y+z with x>0,y,z>=0, explicit polynomial certificate for J/I²-168/125 has only nonnegative terms, positive except y=z=0; the a=b=2,c→∞ limit reaches upper 9/5. Independent SymPy expansion/triangle integrations verifies all symbolic identities; the all-positive polynomial and geometry, not 1331 integer samples, establish the theorem on all positive real lengths.

## originality

PASS

The same projected-cube/Voronoi representation and second radial moment are already published by de Jong–Shokrieh, and zonotope combinatorics by Bach–Beck–Rehberg; only the fourth moment and sharp normalized upper/lower extremal classification are assessed as original. Inspected sources do not contain those higher-moment results.

## value

PASS

An exact higher moment and sharp normalized shape inequality for a canonical genus-two tropical Jacobian completes meaningful geometric statistical information not present in the known second-moment literature. The bounds have natural equality at equilateral branches and a degeneration supremum, and can benchmark tropical quantization/torsion-distance estimates. Not an arbitrary table recomputation: the ratio is invariant under overall metric scaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
