# Independent mathematical audit

## correctness

PASS

The random-recursive-tree parent-choice construction has (n-1)! equiprobable trees. Reconstructing the increasing-tree EGF T'(z,q)=exp(T)+(q-1)(exp(T-z)-1) gives T(z,1)=-log(1-z) and A(z)=partial_q T|_1=F(z)/(1-z), F=1-exp(-z)-z+z^2/2. Marking only ORIGINAL-root child degree with u gives mixed derivative (1+L)F/(1-z)^2+(L-z)exp(-z)/(1-z), and subtraction of H_(n-1)*E[P_n] proves the claimed exact coefficient covariance for n>=3. Singularity extraction at z=1 yields constant 1/2-3/e and 1/(n-1) coefficient (1+e^-1)/2; the remaining entire coefficients and (1-z)log correction yield O(n^-2). Independent exhaustive parent-array enumeration for n=3,...,8 gave exact covariances -1/4,-5/12,-31/72,-683/1440,-3547/7200,-51263/100800, matching formula. Finite enumeration does not prove asymptotics.

## originality

PASS

The assessed original claim is the exact mixed moment of ONE DISTINGUISHED ROOT degree and total two-protected count, including a strictly negative limiting covariance; the protected-node mean, its variance, and generic increasing-tree EGFs are prior work. Mahmoud-Ward 2015 determines the first two moments of P_n, not the D_n cross moment. Holmgren-Janson 2015 treats broad fringe-subtree count limits but does not explicitly evaluate this root-fixed cross. Resultary root-degree/LEAF count gives a positive different covariance; it neither implies nor contradicts the two-protected result.

## value

PASS

Root degree and a depth-two local structural statistic form a motivated joint invariant of random recursive growth. The exact all-n covariance and negative limit distinguish protective structure from the positive leaf-count correlation and quantify weak root/whole-tree dependence. This is substantially more than a textbook substitution, without claiming a full joint distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
