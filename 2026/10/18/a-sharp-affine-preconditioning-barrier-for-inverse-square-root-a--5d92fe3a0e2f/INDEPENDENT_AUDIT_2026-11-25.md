# Independent mathematical audit

## correctness

PASS

With X=KN and X³=0, the product is B=I+aN+b₂N², a=K(1−2t), b₂=K²(t²−2t). A, q_t(A) and B are upper triangular with diagonal one. Uniform positivity for complex Rayleigh quotients is equivalent to positive definiteness of the real symmetric part. I eliminated the middle coordinate using its unit diagonal; the remaining 2×2 Schur complement has eigenvalues 1−b₂/2 and 1+(b₂−a²)/2. Now a²−b₂=K² f(t), f(t)=1−2t+3t²=2/3+3(t−1/3)², and b₂<K² f(t) for K>0. Thus the exact safety interval for each slope is K² f(t)<2, also valid at K=0. Its maximal range is K<√3 for the unique t=1/3; t=1/2 gives K<√(8/3). To independently check the witness, the unnormalized real vector (1,y,1) has quadratic form (y+a)²+2−K² f(t), with a real zero whenever K≥√3, for every slope. Applying q_t(A)⁻¹ to this vector and starting with q_t(A)b realizes the zero in H₁ after normalization. At the optimal endpoint v=(1,−1/√3,1) comes from the stated input b=(1,0,1). In the truncated polynomial ring the square of I−X/2+3X²/8 is I−X+X² and multiplication by I+X gives I; in size two already X²=0 and the linear Taylor polynomial works for all K. The finding concerns exact real normalized affine slopes and one-step left Arnoldi. Above the threshold, a failing real input exists for each slope; not every input fails. I inspected the supplied checker without executing it; these conclusions are algebraic.

## originality

PASS

Credit the optimized λ=1 Jordan-family obstruction for left inverse-square-root Arnoldi: the sharp uniform threshold, the optimizer and the zero compression for some real input at every slope at and above the threshold. The Arnoldi method and branch condition are established, the joint geometry of the first two Jordan powers has a prior exact characterization through two Ritz values, and degree-two Taylor exactness is routine nilpotent calculus. The inspected prior results do not supply the optimization over this preconditioning curve.

## value

PASS

This is the minimal Jordan dimension where first-order Taylor exactness fails, and left inverse-square-root Arnoldi is a previously motivated numerical method that actually needs nonsingular compressions. The example excludes every real affine slope past a sharp point despite an innocuous preconditioner spectrum, rather than just noting that eigenvalues may misrepresent the field of values. The sharp comparison to the standard Taylor slope and the explicit singular input make the obstruction usable as a benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
