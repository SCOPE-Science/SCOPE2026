# Independent mathematical audit

## correctness

PASS

Columnwise weighted means s_j and differences d_j transform the quadratic objective exactly into independent mean squares and c_j-weighted isotonic regression of d, c_j=a_jb_j/(a_j+b_j). Inside each PAV pooling cell, output-row absolute Jacobian sums are 1+2[b_j/(a_j+b_j)](1-c_j/C_B) and 1+2[a_j/(a_j+b_j)](1-c_j/C_B). C_B<=C bounds globally; strictly decreasing d forces an interior all-pooled cell and a sign-vector perturbation attaining the maximal row sum. This proves Lip_inf=1+2 max_j alpha_j(1-c_j/C). Equality at the minimal value 2-1/m requires equal all weights; strictly positive finite weights give modulus<3 and one unbalanced column approaches 3. Independent exact-rational perturbation/Jacobian tests covered 72 instances.

## originality

PASS

Prior anti-Monge estimation articles establish the cone and statistical least-squares objectives; general isotonic and unweighted l_p sensitivity theory addresses different operator/metrics. The reconstructed weighted 2-row projector combines a coordinate change and pooling Jacobians that are not represented by a simple isotonic l_inf contraction claim.

## value

PASS

The exact sup-norm error-amplification modulus and sharp weight-design range are natural worst-case robustness measures for the canonical two-row anti-Monge projection under heteroscedastic errors. The attained extremizers expose a genuine pooling-induced amplification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
