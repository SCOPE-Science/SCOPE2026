# Independent mathematical audit

## correctness

PASS

For fixed radii (18,42,48,12,48,42,18), the claimed x(t)=z+u v_-+v v_+ has u=a(-1/6)^t in [-1/6,1] and v=b2^-t in [0,1]. Every off-center directed pair’s threshold decision is strict and constant throughout this rectangle; exact corner testing of all 7x7 linear gap inequalities confirms the fixed neighborhoods N1={1}, N2={1,2,3}, N3={2,3,4,5}, N5={3,4,5,6}, N6={5,6,7}, N7={7}. For i=4, x4-x3=x5-x4=12+3u-v so both central arcs are present iff v>=3u (inclusive). Both choices yield center mean 84. Symbolic exact row averaging on each side gives (u,v)->(-u/6,v/2), closing the induction for all real square parameters and integer times. At odd t, u<=0 implies arcs present; at even t=2j they are present iff b>=3a*9^-j. Thus in 0<b<3a exactly k=ceil(log_9(3a/b)) even times omit them, with 2k-1 changes and sharp T=2k-1; b=0<a alternates indefinitely, a=0 or b>=3a is constant. Area under b<c a with c=3^(3-2m) is 5/6 for m=1 or c/2 for m>=2. The integer tail-sum yields E[S]=5/6+2*(1/6)/(1-1/9)=29/24. Exact SymPy/Fraction independent computations verified all row identities, threshold corners, several boundary cases and tail identities; finite tests are only corroboration of an analytic general proof.

## originality

PASS

The source seven-agent construction of Hegarty–Ognissanti–Wedin proves precisely the negative-eigenvalue b=0 edge, not the independently checked transverse v_+ eigenmode invariant plane or its sharp finite-switch-count/area laws. The 2011 fixed-topology literature does not imply a first stabilization time; 2014 homogeneous asynchronous expected-switch bounds apply to another dynamics. The recent six-agent period-ten nonconvergence witness is stronger against global convergence but does not dominate the claimed seven-agent quantitative transient law. Published research-record searches did return an exact self-record, deliberately excluded as independent priority evidence. No inspected independent source entailed the full final claim; PASS is explicitly best of knowledge, not a priority certificate.

## value

PASS

The exact first graph-stabilization time and number of changes for a natural invariant two-eigenmode perturbation plane of a documented nonfreezing counterexample are motivated dynamical invariants. The transverse mode reveals arbitrarily long but finite switch transients accumulating logarithmically at the infinite-switch boundary, with every odd finite switch count on a positive-area parameter wedge and an exact uniform-area tail/expectation. The classification resolves more than simply restating the known b=0 trajectory: it establishes a stable invariant family and a sharp threshold arrangement with discrete equality cases. The result has meaningful illustrative use in distinguishing numerical finite observation from permanent switching, despite being confined to a specific seven-agent model and a 2D slice. No generic 7D or universal SBC stabilization theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
