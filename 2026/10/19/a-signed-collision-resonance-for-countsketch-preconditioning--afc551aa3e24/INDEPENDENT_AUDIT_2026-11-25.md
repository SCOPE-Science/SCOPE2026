# Independent mathematical audit

## correctness

PASS

Independently partitioned the three informative hash outcomes. All three in one bucket drops rank with probability 1/s²; three distinct buckets preserve rank (that case has probability zero when s=2); a specified pair collides in exactly two buckets with probability (s−1)/s². Write x_i for the perturbed rows and let k be the remaining row. The equal-pair-sign determinant, ignoring row signs, is det(x_i+x_j,x_k)=ε det(v,r_k) exactly because the row sum is εv. Opposite pair signs give determinant of absolute value √3 at ε=0, and hence preserve rank near zero. The failure probabilities are therefore (3s−1)/(2s²) at zero and 1/s² off zero sufficiently nearby. On each equal-sign collision the top squared singular value tends to 2 and the product of the two singular values is the determinant magnitude, so |ε|κ tends to 2/|det(v,r_k)|. All other surviving classes stay bounded. Their finite weighted sum, using the total survivor probability 1−1/s², gives the factor 1/(s+1). The QR factor shares the sketch's singular values; the scaled input Gram tends to identity, sandwiching κ(AεRε^−1)/κ(Rε) between 1/κ(Aε) and κ(Aε). This gives the identical conditional limit for QR. Verified 17/72, 1/36, and (1+2√3)/7 at s=6 and v=(1,1). Read but did not run the frozen verifier: it enumerates discrete outcomes at a few selected parameters, using numerical minor and Gram tolerances, which cannot certify all directions or the limiting coefficient.

## originality

PASS

The distinct claim is the explicit direction-dependent reciprocal-distance pole of the full-rank conditional mean, including its transfer to actual QR preconditioning. The two rank formulas are covered by a later indexed weighted triangle specialization and the original frame lies in the fixed-triangle setting of another later record; none of the checked passages gives the perturbed conditional mean. General collision lower bounds and high-probability embedding-based guarantees address different quantifiers.

## value

PASS

The equiangular three-row frame is the simplest redundant planar tight example, asymptotically perfectly conditioned before sketching. The theorem separates exact rank failure from instability within the apparently successful full-rank sample: the latter mean diverges with a sharp, direction-sensitive coefficient for each fixed oversampling size. This is useful for interpreting rank-only diagnostics or fixed-oversampling experiments, including s=6, and is substantive beyond the known qualitative collision hazard or later rank-only formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
