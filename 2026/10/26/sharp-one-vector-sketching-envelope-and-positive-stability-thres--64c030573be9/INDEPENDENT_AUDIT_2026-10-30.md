# Independent mathematical audit

## correctness

PASS

Restrict the sketch Gram M=S^TS to U=span{b,Ab}, with 1−ε<=M<=1+ε. The spectral polynomial implies M²<=2M−(1−ε²)I. For ||b||=1, d=b^TMb, this yields ||Mb||/d<=1/sqrt(1−ε²). Writing A=αI+T, ||T||<=δ gives |h_S−α|<=δ/sqrt(1−ε²). Dimension-two A=diag(μ,L), M=[[1,−ε],[−ε,1]], B=(MA+AM)/2 give det(B−zM)=(1−ε²)(z−α)²−δ²; generalized eigenvectors attain both ends. Lower end equals zero at εcrit; explicit (μ,L,ε,b)=(1,9,4/5,(2,1)) yields h_S=−5/3, and at (1,9,3/5,(3,1)) yields zero. Independent symbolic rational pencil checks passed.

## originality

PASS

Best-of-knowledge original for the restricted final claim after direct implication-based comparison; primary overlap, unavailable full text and mathematical reduction risks are explicitly documented, not treated as absence-proof.

## value

PASS

This is a sharp stability design constraint for sketching Krylov matrix-function surrogates: it specifies both attainable extremal Ritz values and exact failure threshold, beyond qualitative instability or a nonsharp localization bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
