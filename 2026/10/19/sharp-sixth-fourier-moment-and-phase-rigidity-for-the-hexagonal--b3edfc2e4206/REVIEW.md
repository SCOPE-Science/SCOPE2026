# Independent mathematical audit

## correctness

PASS

Normalized orthogonality gives the squared norm of the triple convolution. The triangle inequality reduces the maximum to magnitudes. The antipodal RMS operation increases each nonnegative autocorrelation by Cauchy–Schwarz and preserves R₀=M. If it changes an unequal pair, the sum of magnitudes strictly increases, so some nonzero R_h increases and the (h,−h,0) term in the autocorrelation cube increases strictly. For balanced magnitudes, independently expand the three antipodal Laurent binomials. Since v₂=v₁+v₃, surviving signed exponents are (k,−k,k), so all three pair degrees have the same parity, hence are all even in degree six. Up to permutation the patterns (6,0,0),(4,2,0),(2,2,2) contribute respectively 20, 15·6·2=180 and 90·(8+1+1)=900. This yields 20s³+120s e₂+420e₃, with M=2s; the two sharp symmetric-polynomial bounds force X=Y=Z, and give moment ratio 85/9. With all magnitudes equal, alignment in each fiber v_j makes the antipodal products common. Factoring their square root λ, the zero-sum triangles force (η₁η₃/η₂)²=1, and the sign choice of λ removes the minus branch. The basis v₁,v₃ therefore gives exactly the scalar character family, which attains equality. Differences of root vertices generate the lattice, so the projective character parameters are unique. At N≥7 there is no aliasing between triple sums in [−3,3]²; no Nth-root restriction on phases is needed. At N=6 the only distinct collisions are the three opposite-vertex pairs at the six extreme triple sums (each a singleton), adding 6 to 2040 and giving the strict lower witness 341/36. No optimal norm at smaller grids is inferred. The independent enumeration in /workspace/branches/30df5558-c964-4978-ade3-1ca8f5928351/record3-independent-check.txt agrees on all 37 fibers, the polynomial, and the residue counts. Frozen checker.py and checker_output.txt were inspected, not executed; python3 checker.py is the packaged replay. The global inequalities, not the finite test arrays, establish optimality.

## originality

PASS

Credit the existing flat walk count, the previously proved unimodular maximum and phase classification, and the general RMS reflection inequality. The supported distinct contribution is global optimization over arbitrary coefficient magnitudes (which forces flatness and thus extends the equality classification globally), together with the explicit N=6 obstruction at the stable-grid boundary. The prior unimodular theorem already covers the maximizing phase orbit and grid transfer on that slice; those pieces are not independently novel here.

## value

PASS

The motivated object is the smallest planar hexagonal root aperture, and the exact ℓ²-to-L⁶ operator norm is a weighted invariant, not just an enumerated return count. The theorem identifies which complex weightings actually attain that norm, while the first aliasing witness explains why the limiting norm fails at the adjacent grid boundary. These are useful for periodic Fourier synthesis on the support even after crediting the known flat slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
