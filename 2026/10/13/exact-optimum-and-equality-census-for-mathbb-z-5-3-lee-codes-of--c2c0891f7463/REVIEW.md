# Independent mathematical audit

## correctness

PASS

I independently enumerated the five horizontal layers of the torus, without using the frozen clique search. Within a layer, disjoint radius-one balls of size five cap the size at five. The legal layer counts for sizes zero through five are 1,25,150,200,50,10. Between adjacent layers the horizontal Lee distance must be at least two (ban the occupied horizontal radius-one neighborhoods); between nonadjacent layers it must be at least one (ban identical horizontal positions). Exact recursive combination of compatible layers through 000 excludes size 16 and yields 24 size-15 codes. Translation takes every nonempty code to one through 000, and a larger code would have a 16-subcode. Full translation gave 200 labeled sets, exactly the orbit of one witness under all 6000 distinct signed coordinate permutations with translations. The stabilizer has order 30, and direct counts give every stated symbol multiplicity and pair-distance tally. For the linear contrast, a two-dimensional code has at least 25 points, excluded even by the radius-one packing bound 17; the span of (1,1,1) attains size five.

## originality

PASS

The checked exact table is for linear codes, not arbitrary subsets; the checked unrestricted table does not evaluate these parameters. The closest indexed same-alphabet equality census uses a different pair relation. The independently supported distinct finding is the unrestricted maximum together with the complete labeled census and orbit and profile information.

## value

PASS

Single-error packing in the small three-dimensional Lee torus is a natural unrestricted coding parameter with an independently motivated linear comparison. The exact optimum closes a gap left by the elementary packing bound, and the complete equality orbit with uniform balance and distance profile gives a concrete structural benchmark for nonlinear Lee-code bounds or searches. This is not just a rerun of the linear table or a witness without optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
