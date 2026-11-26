# Independent mathematical audit

## correctness

PASS

On the zero-sum form, pendant contrasts contribute −a, the mean-zero parent sectors have diagonal (−1,(r−1)a−rb) and off-diagonal √r(1−a), and the remaining constant line has per-group value G=r[(n−3)+(n−1)(b−2a)]+(r−1)a, where b=a^(log₂3). Direct substitution gives G(2)=−2 and G(4)=2rn−4; G strictly increases for a≥2 since (log₂3)·3/2>2. The standard-block determinant F=r(b−a²+a−1)+a is strictly concave, positive at 2, and first zero at a_s≤4. For r>1, F(2+2/r)=[2b−a²−2]/(a−2)>0 there because the numerator is strictly concave and vanishes at 2 and 4. For r=1 the first zero is 4. Substitution at a_s yields G_{2,r}=a_s[r(a_s−2)−2]≥0 and G_{n,r}>G_{2,r} for n≥3 by 1+b−2a_s>0. Thus G crosses first, so the only critical mode is the global line with load −r on the core and +1 on the leaves; it violates above the root. Strict lower-exponent nesting and Gram rank give all embedding and kernel conclusions. The root moves strictly left as n or r increases: the increments at the previous root are positive by 1+b−2a>0 and G=rQ_n(a)−a with Q_n(a)=a/r>0. Expanding G at p=1, with derivative r(n−1)(3 ln 3−4 ln 2)+2(r−1)ln 2, or normalizing G by n or r and using implicit differentiation, gives both first-order terms and their separate fixed-parameter remainders; both limits are 1. At p=1 the larger eigenvalue of the standard block dominates −2 and −2/(r+1), since shifting the block by 2/(r+1) makes its determinant negative. Frozen support was inspected without execution; the independent `python /workspace/branches/independent_reproduction.py 4` passed 25 shortest-path Gram cases below, at, and above the threshold and checked sample parameter monotonicity.

## originality

PASS

The ordinary QEC is already known for every r. A separately indexed exact weighted-corona theorem also covers the entire powered r=1 slice when the common pendant length equals one. Credit is restricted to the additional multi-leaf powered classification, the decisive dominance over the contrast/mean-zero sectors, and the two-parameter consequences; the exact r=1 overlap and QEC carry no originality credit.

## value

PASS

Uniform private leaf bundles are natural clique coronas. The multi-leaf classification identifies a global critical mode, quantifies how either parameter moves the threshold and exhibits different first-order decay regimes despite equal limits. At every fixed r≥2 it gives a family with equal ordinary QEC but different sharp Hilbert thresholds, a substantive distinction from the prior QEC calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
