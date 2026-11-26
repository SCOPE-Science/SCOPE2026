# Independent mathematical audit

## correctness

PASS

The sign-specific proximal optimality condition with input rx and threshold c gives the asserted clipped affine maps, preserving [−a,a]; synchronous coupling contracts W₁ with factor r<1 and yields a unique invariant law. At a≤s, including equality, T_+(−a)=a and T_−(a)=−a force the two maps to be constant, so one step produces fair endpoint atoms. For s<a<b, monotonicity makes the worst initial point for a plus block −a, with image min(a,b−r^n(b+a)); this gives the stated least uniform constant-sign length, inclusive of the threshold equality. In fact no shorter mixed word can reset either: a first collapsing step must clip its entire nondegenerate interval to an endpoint, and monotone all-plus/all-minus bounds prevent reaching that endpoint from the appropriate extreme before N. A qualifying word occurs almost surely at a finite past time (use disjoint iid length-N blocks). Backward iteration is then a finite image of an endpoint, giving full mass to a countable set, not a claim about countability of its closure. The endpoints have mass at least 2^(−N); successive images of a under T_+∘T_− are s+r^(2j)(a−s), pairwise distinct atoms since their specified words have positive probability. At a≥b both clips are inactive on the invariant interval (with possible affine equality at a=b), giving the classical absolutely convergent signed series. If a maximal atom existed, both inverse affine branches would have to attain its mass; iterating the plus inverse exits [−b,b] from every x<b, while the minus inverse exits at x=b. This proves nonatomicity even with overlaps. The two image intervals cover [−b,b] exactly when r≥1/2; otherwise their separation gives the Cantor dimension by the open-set condition. Independence gives the variance and the fixed-objective stepsize threshold follows by rearranging a≤2τλ/(2−τμ). Independent replay `python3 /workspace/independent_reproduction.py 5` enumerated all sign words through length five for r=2/3,c=1 at a=s, a=3/2, and a=b, found the predicted respective first lengths 1,3,and none through five, and reproduced the middle orbit 3/2,1,7/9,55/81,… by exact proximal arithmetic. Neither word enumeration nor coupling asserts almost-sure convergence of forward paths.

## originality

PASS

The supported distinct contribution is the full stationary-measure classification for the two clipped maps, particularly the intermediate infinitely atomic law and explicit least uniform reset length. The randomized incremental method, existence tools, and the whole affine Bernoulli-convolution branch are prior ingredients. Earlier and later catalogue hits directly overlap the affine branch and related reset reasoning, but the inspected statements do not supply the same middle clipping law or the two sharp surfaces.

## value

PASS

A scalar quadratic with two shifted absolute penalties is a natural nonsmooth splitting with a fixed optimizer, not an arbitrary selected dynamical map. Its constant-step stationary law can change from endpoint-only to infinitely atomic to diffuse, behavior that expected objective rates do not describe. The sharp thresholds and least reset length characterize a distinct finite-word memory-loss mechanism and let practitioners distinguish genuine phase changes from finite simulation or rounding artifacts. This value is for the clipped proximal specialization, not for rediscovering the affine Cantor/interval dichotomy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
