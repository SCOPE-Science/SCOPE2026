# Independent mathematical audit

## correctness

PASS

For d>=3, a,b in [0,1], use w=x-y in [-1,1]^d and S=sum w. Necessary slab |S|<=d-a-b follows from sum constraints. Writing p=sum positive coordinates, q=sum negative absolute coordinates gives exact attainable Y=sum y range [q,d-p], and existence iff it intersects [a,d-b] and [a-S,d-b-S]. All residual inequalities follow from p,q<=d-1 when w has both signs (since max(a,b)<=1), or p or q=|S|<=d-a-b when one sign. Therefore exact set equality K-K=[-1,1]^d intersect slab. Two removed corner simplices of side lengths a,b give vol(K)=1-(a^d+b^d)/d!, and in [-1,1]^d two slabs caps each vol s^d/d!, giving vol(K-K)=2^d-2s^d/d!. At fixed s in (0,2), strict convexity of a^d+(s-a)^d yields centered 2^d minimum and asymmetric endpoint maximum. Covers a=0,1 and b=0,1 and affine transformations. Independently verified 34,875 rational interval equivalences on d=3,4,5; unrestricted proof is analytic.

## originality

PASS

Universal Rogers-Shephard and Brunn-Minkowski ratios are prior art, as are broader Godbersen mixed-volume inequalities, but these do not identify the same exact difference-body set for an asymmetric one-parameter family and its strict sharp volume profile. Fixed-difference-body fiber degeneracy is the distinctive geometric statement.

## value

PASS

Difference bodies lose translational and certain asymmetry data; identifying a continuous explicit family of distinct full-dimensional bodies sharing the exact difference body, and the sharp possible volume range within it, addresses a natural reconstruction/extremal-geometry problem. The set-valued fiber is a stronger invariant than merely confirming a universal inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
