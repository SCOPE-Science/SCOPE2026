# Independent mathematical audit

## correctness

PASS

For extended Hamming parity-check columns h_a=(1,a), any optimal correction support spans W=im S of dimension r. If first syndrome row u!=0, an affine basis of W gives lambda=r and M=|GL_r(2)|/[(2^r-1)r!]. If u=0 and S!=0, W lies in linear hyperplane and needs r+1 affine support points; counting affine bases in cosets v+W gives M=2^m|GL_r(2)|/(r+1)!, lambda=r+1. S=0 has (0,1). Rank-matrix formula counts syndrome types; fixed t, as m grows, full rank in zero-top-row matrices occurs with probability tending to 2^-t and dominates expected leader number 2^(m-t)|GL_t(2)|/(t+1)!. Independently enumerated all 64 syndrome matrices for m=2,t=2 (joint (lambda,M) histogram 1,12,36,9,6 at respective pair types), matching proof. The source code enumerates several larger cases but code logs are not proof of the all-m,t statement.

## originality

PASS

The maximum generalized covering radius of extended Hamming codes was previously proved (Elimelech–Wei–Schwartz, 2022, Prop 11); it is not new. The exact per-syndrome minimum column-support distance, number of distinct minimizers, rank distribution and resulting large list-size asymptotic are finer than the known maximum. Alfarano et al. 2026 investigate a finite-geometric broader framework, but its full text was inaccessible; their methods could already imply the affine-basis counts. Thus novelty is best-knowledge, not asserted from lack of search matches.

## value

PASS

Joint column-support minimization is a natural multirequest decoding/query-access invariant; the complete nearest-cover leader profile and exponentially many optimal corrections in the maximal-radius minority are exact useful facts beyond the radius maximum. It is a meaningful infinite parameter classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
