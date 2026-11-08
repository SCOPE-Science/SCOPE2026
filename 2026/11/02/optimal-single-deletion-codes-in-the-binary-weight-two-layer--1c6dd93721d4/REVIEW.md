# Independent mathematical audit

## correctness

PASS

For every length n>=2, index words by 0<=a<=b<n−1 with ones at a,b+1. Deleting a one yields distinct weight-one outputs at a,b, except a=b; disjoint shadows force L+2E<=n−1 for L loop/adjacent-one words and E nonloops. Two loops at consecutive indices have a common weight-two deletion output, so L<=ceil((n−1)/2). Consequently |C|<=floor((3n−2)/4). The construction chooses even-index loops and disjoint odd-index nonloops (4t+1,4t+3); its weight-one outputs are disjoint by index parity and its weight-two outputs have gaps 1 for loops and 2 or 3 for nonloops, with distinct first coordinates across nonloops. Attains the bound for all n, including n=2. Independently enumerated deletion balls and exact maximum independent sets n=2..9 (1,1,2,3,4,4,5,6) and collision-free construction through n=89; the all-n proof is the packing argument.

## originality

PASS

Equivalent statement alpha(L_{1,n,2})=floor((3n−2)/4) for weight-two one-deletion confusability graph. Cullina–Kulkarni–Kiyavash's 2012 fixed-weight graph theorem gives CHROMATIC number, not independence number; authors distinguish the objectives. No 2019 MILP method targets unrestricted binary codes with numerical bounds. Published Resultary small-instance deletion-code tables solve different alphabets/weights/noise models. A historical all-n elementary special case could still cover this.

## value

PASS

Exactly solves the natural smallest nontrivial constant-weight family of single-deletion error-correcting codes for every length, with matching simple constructive codes and tight packing bound. The invariant is a genuine code capacity / graph independence number, not an arbitrarily selected toy instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
