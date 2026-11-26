# Independent mathematical audit

## correctness

PASS

The original obstruction and ratio calculation are correct, and the replacement determines the full profile rather than merely excluding primitive representations. For even L the product is 1 mod a, so the defining residue of b forces y=aj−1. The strict lower bound b>N/(aL) excludes all j>L. For L=2, b=a−1 and the second candidate is feasible even at x=0. For L≥4, N≥a³L²: the first four factors give at least (880/81)a⁴, which exceeds 16a³, and every later factor grows faster than the ratio of successive squared indices. Therefore N/(aL−1)−N/(aL)≥a, enough to accommodate the upward rounding of b. This makes every j≤L feasible. Each candidate y divides N and is coprime to a, so y divides x and gcd(x,y)=y exactly. The estimate on b proves the displayed lower bound and both needed divergences for fixed a. I independently reproduced all original 77 pairs and 616 nonprimitive representations, and then explicitly swept every feasible y for 253 pairs with 3≤a≤25 and even L from 2 through 22; all 3036 representations had the full stated profile. Jaffe's boundary formulas apply with the same gcd convention, with g(2,1)=0 by exchange of the generators.

## originality

PASS

The original dichotomy and even its exact congruence-class unboundedness fail originality: Ding–Wang–Zhang already give a stronger subsequential logarithmic bound in that class, while the small-generator formulas are known. The replacement credits these and passes only for the exact constructive profile: a direct product and rounding, with any prescribed even number of candidates and their full gcd list, rather than a construction guaranteeing some common prime at each candidate. This profile is not a specialization of the inspected stronger gap bounds or of their witness families.

## value

PASS

The repaired claim is a motivated witness family with an exact parameter-controlled ordinary representation count and all gcds, not another looser estimate of the known largest-gap growth. It shows precisely how a target with arbitrarily many ordinary representations can have none primitive, and supplies reproducible examples for testing representation or sieve criteria without prime selection or searching for b. The qualitative elementary corollary is useful context but is not the value basis on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
