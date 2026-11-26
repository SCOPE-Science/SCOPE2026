# Independent mathematical audit

## correctness

PASS

Any two distinct shared part values determine the third part by the total, including repeats, so distinct supports intersect at most once. A nontrivial family cannot contain a singleton support and must contain a triangle with three distinct pairwise intersections a,b,c. With three full supports the only candidate avoiding a,b,c uses the three private values; its fixed sum would force a+b+c=n and make a private value coincide with a base value. Each candidate meeting exactly one base vertex is determined by that vertex and the opposite private value. For candidates at a and b only their remaining parts could coincide, but those parts b+c-a and a+c-b coincide only for a=b. With a repeated base member (a,a,b), all additions must meet at a or b; the opposite private value is required, so a missing private value rules out the corresponding addition and each orientation supplies at most one. When both private values exist, the two candidates again can only meet via the remaining parts b-a+c and a-b+c, impossible as a!=b. This proves the cap including repetitions. The displayed witnesses at 8 and for n>=9 are distinct and pairwise intersecting without a common part. A star has floor((n-j)/2) members by deleting j, so at n>=11 a largest family is a largest full star with the stated centers. Independently ran python3 /workspace/checks/3_small_orders.py, enumerating all subfamilies at n=3,...,10: maxima 1,1,2,2,3,4,4,4, with exactly the stated largest family at 8. The frozen script and stored output were inspected, not executed; the infinite cap follows from the proof, not the stored table.

## originality

PASS

The distinct contribution is the sharp four-member nontrivial bound uniform in the total, and the resulting exact star regime/maximizer description beyond the previously known range. Do not credit as new the n=8 exception, whose four-family and full ground list appear in Borg (and whose uniqueness can be read off), or the eventual existence of an optimal star. The inspected large-k asymptotic result does not entail any fixed k=3 claim.

## value

PASS

Solves the natural small-length gap between a known exception and the eventual star theorem. The proof gives an additive obstruction on extending an intersection triangle, explaining a sharp, total-independent cap that generic triple-system bounds or a few enumerated totals do not provide. It determines exactly when larger stars are forced and which stars can maximize.

The dated certificate retains the supplied scientific assessment, sources and limitations.
