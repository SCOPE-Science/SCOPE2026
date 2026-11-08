# Independent mathematical audit

## correctness

PASS

For ideal Mogi surface displacement μ=A(x−X,y−Y,d)/[(x−X)²+(y−Y)²+d²]^(3/2), local 4-vector parameters (A,d,X,Y) and n≥3 full three-component isotropic iid Gaussian observations on one common radius r, explicit differentiated Jacobian columns yield FIM. Angular rotation conjugates parameter X,Y block, and strict concavity logdet bounds any FIM by group average. Equality iff FIM itself invariant, equivalent to vanishing first and second complex angular sums; regular n-gon reaches it for all n≥3. Balanced determinant is (n⁴ A⁶/σ⁸) r²(d²+(5/2)r²)²/(r²+d²)^14, positive for r,d,A>0. With z=r²/d², derivative of z(1+5z/2)²/(1+z)^14 =−(5z+2)(55z²+11z−2)/(4(1+z)^15), unique positive maximizer z=(sqrt(561)−11)/110; zero at endpoints guarantees global radius optimality. Independently computed full Fisher blocks and determinant in exact SymPy arithmetic and checked unbalanced angular strict loss and derivative root.

## originality

PASS

The first/second Fourier angular necessary-and-sufficient condition and unique algebraic common ring radius jointly optimize four unknowns in an ideal Mogi inverse model; specific published empirical GNSS inversion and geophysical error studies do not appear to state the exact theorem.

## value

PASS

The theorem solves an entire natural restricted experiment-design family: how to position n full-vector GNSS stations on a common ring while estimating both source strength, depth and horizontal position. Exact moment conditions plus universal depth-scaled radius form a reproducible benchmark for simulation and design comparison, without claiming real-world optimal monitoring.

The dated certificate retains the supplied scientific assessment, sources and limitations.
