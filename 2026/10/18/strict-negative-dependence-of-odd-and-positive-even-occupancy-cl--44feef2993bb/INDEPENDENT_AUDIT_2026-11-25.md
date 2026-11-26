# Independent mathematical audit

## correctness

PASS

Repaired theorem: raise the single-ball polynomial 1−p−q+px+qy to n; odd/even filters at ±1 followed by subtracting the even-empty term at y=0 give the joint probability, and the corresponding marginal product gives the displayed four-power covariance. Under p+q≤1/2, d=1−2p−2q is nonnegative, c=d+q and δ=2pq is strictly between zero and q. For f(x)=x^n, f′(d+2v)<f′(c+v) on [0,δ] even at d=0 and n=2. Integration gives strict ordered-pair negativity. Diagonal covariances are negative products of positive probabilities, and sum with the ordered-pair covariances. No all-pairs assumption is used in the proof for a single pair. Independent exact weighted enumeration in /workspace/repairs/5/verify_parity_occupancy.py confirmed the formula for three unequal vectors, including one exceeding the bound globally, and 208 qualifying ordered-pair signs; aggregate checks applied when every pair qualified. The frozen script's purported nonuniform grid enters its conditional loop only for uniform vectors; the repaired tests actually exercise unequal probabilities. The finite tests do not prove the sign theorem. For the original record, /workspace/review_reproduction.py 5 additionally checks small uniform instances, including m=n=3. Its small-box proof uses parity of O at m=2,3, and the limit follows by first-order expansion with the actual n/m: the off-diagonal sum per box tends to λ(e^(−4λ)−e^(−3λ)) in addition to the negative diagonal limit.

## originality

PASS

Pass only for the repaired inequality on different-mass ordered pairs and its diffuse aggregate consequence, not for parity moment evaluation or the substantially covered uniform theorem. The verified stronger uniform catalogue claim does not quantify over unequal probabilities; the distinct pairwise inequality also cannot be read off an aggregate sign even in its symmetric setting.

## value

PASS

For unequal urn weights, the sign is not a general monotone negative-association instance. A test using just the two relevant probabilities determines even the ordered-pair sign, including boundary cases, and can be applied on diffuse subsets without knowing all other weights. It gives strict aggregate covariance in a genuinely unequal regime and identifies a concrete checkable hypothesis rather than claiming a general negative-dependence property.

The dated certificate retains the supplied scientific assessment, sources and limitations.
