# Independent mathematical audit

## correctness

PASS

For A_r=[[1,r],[r,-1]] with 0<r<=1 (condition number exactly one), i.i.d. squared-entry sample probability and relaxation 1/2, the exact sample update matrices yield conditional E||x+||²=(3/4)||x||²; Markov inequality and Borel–Cantelli yield a.s. convergence. Rotation symmetry leaves three-dimensional quartic span P=x1^4+x2^4, Q=x1^3 x2-x1 x2^3, R=x1²x2² invariant under expectation; expansion gives C_r with entries ((r^4+16r²+1)/(32r²), (1-r²)/(16r),1/8), ((r²-1)/(8r),1/8,0), (3/8,0,1/4), and det(I-C_r)=-3(5r^4-94r²+5)/(1024r²). Nonnegative quartic cone, invertible updates and no shared projective eigenlines yield a strictly positive Perron quartic H comparable with ||x||^4, proving Theta(lambda_r^k) for every nonzero initial state, not merely a positive spectral eigenvalue. Continuity, r=1 spectrum and unique determinant zero in 0<r<=1 establish r*=sqrt((47-2sqrt(546))/5), and divergence/constant/decay trichotomy. Independently evaluated C_r spectra: leading eigenvalue ~1.160110226458334 at r=1/5 and ~0.788054341406048 at r=1/3. Finite checks alone cannot prove the all-k threshold.

## originality

PASS

DSGS by Razaviyayn–Hong–Reyhanian–Luo (arXiv:1810.05251, Algorithm 1 and main mean-square theorem) uses the same squared-entry selection and proves lower-moment convergence. Du–Sun and Han–Xie extend or compare convergence methods, but the inspected source does not derive this uniform-orthogonality fourth-moment phase transition. General positive-operator facts not novel; exact fixed-relaxation family/threshold assessed as new.

## value

PASS

The sharp high-moment instability of an almost-surely convergent, mean-square contractive algorithm on perfectly conditioned matrices is a substantive counterexample to interpreting lower-order error bounds as control of tail risk. Algebraic r* makes the boundary precise and distinguishes entry sampling from row Kaczmarz.

The dated certificate retains the supplied scientific assessment, sources and limitations.
