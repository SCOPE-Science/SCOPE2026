# Independent mathematical audit

## correctness

PASS

A codeword with adjacent ones loads one weight-one output; a nonadjacent pair loads two distinct such outputs. Hence a+2b≤ℓm and a≤m, giving the stated bound after also taking the total number of pairs. The selected adjacent words use one slot at each weight-one output, and each added nonadjacent word (i,j+1) uses a slot at i and j, so any simple graph of maximum degree at most ℓ−1 respects these constraints. The three preimages listed in RESULT.md exhaust insertion of a zero before, between or after the two ones. For ℓ=2 and adjacent output ones, forbidding consecutive graph edges removes the only third candidate; for nonadjacent output ones, either the middle candidate is absent, or its edge excludes both outer candidates by sharing an endpoint with each. The distant-index matching attains the bound for m≥3. For ℓ≥3 the circular offsets give the required even degrees, and the extra matching for odd d is disjoint from the previous offsets. In odd m its offset (m−1)/2 is coprime to m, so the matching from that cycle really misses just one vertex. n=2 permits the sole word; for (n,ℓ)=(3,2) all three inputs share output 11, but the two adjacent inputs work. Independent bit-deletion replay (python3 /workspace/branches/independent_replays.py, function deletion) exhausts all subsets at n=2,…,6, with ℓ=2,…,n+1 and confirms the exception and formula. The proof, not that replay, establishes arbitrary lengths.

## originality

PASS

The exact two-or-more-list capacity and exceptional binary weight-two collision are distinct from unique decoding on the identical weight slice. No examined result or code table supplies the required all-length equalities under the same list and channel constraints.

## value

PASS

Weight two is the first small slice in which deletion of a one can impose a genuine two-endpoint constraint and deletion of a zero a distinct three-way constraint. The exact formula and extremizers for every list size, including the isolated obstruction and full-space saturation threshold, resolve both constraints rather than merely evaluating a short instance. They give a usable benchmark for more general constant-weight deletion packings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
