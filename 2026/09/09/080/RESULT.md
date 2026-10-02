# S0 chain-type stem over F5: full second-cohomology automorphism-orbit census and a class-2 center obstruction

## Object

Let \(Q\) be the five-dimensional class-2 Lie algebra over \(\mathbf F_5\) with basis \(e_0,e_1,e_2,f_0,f_1\) and nonzero brackets
\[
[e_0,e_1]=f_0,\qquad [e_0,e_2]=f_1.
\]
Then \(Z(Q)=Q'\) has dimension 2.

## Result

The second Lie cohomology \(H^2(Q,\mathbf F_5)\) has dimension 6. The automorphism group has order 750000000 and partitions the \(5^6=15625\) cohomology classes into exactly eight orbits with sizes
\[
1,\ 4,\ 24,\ 96,\ 600,\ 2400,\ 5000,\ 7500.
\]
The corresponding stabilizer orders are obtained exactly by orbit-stabilizer and are recorded in `artifacts/committed_log.json`.

Let \(W\subset H^2(Q,\mathbf F_5)\) be the subspace represented by cocycles that vanish on \(Z(Q)\times Q\). Then \(\dim W=1\), it is automorphism-stable, and its nonzero four classes form one orbit. A one-dimensional central extension of \(Q\) remains class at most 2 exactly when its cohomology class lies in \(W\). The split class and the unique nonzero \(W\)-orbit both produce six-dimensional extensions with center dimension 3. Consequently this stem has no six-dimensional class-2 exponent-5 extension with center dimension 2.

## Verification

A fresh reconstruction checks the Jacobi identities, center and derived algebra, builds the cocycle and coboundary spaces, reconstructs the automorphism action, enumerates all 15625 cohomology classes, and independently recomputes the two extension centers. The orbit sizes above are exhaustive, not sampled.

## Reproducibility

- `python3 artifacts/s0_h2_aut_orbits.py` rebuilds the cohomology space, automorphism generators and full orbit partition.
- `python3 artifacts/w_orbits.py` analyzes the class-preserving subspace.
- `python3 artifacts/verify.py` independently reconstructs the calculation and prints `VERIFY_OK`.

## Scope

The statement concerns this explicit stem and the exponent-5 Lazard stratum. It does not claim a complete classification of all groups of order \(5^6\), and the surrounding family label is not needed for the algebraic obstruction.
