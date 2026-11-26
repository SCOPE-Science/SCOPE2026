# Independent mathematical audit

## correctness

PASS

The frozen all-palette formula is mathematically correct; its failure was originality, not an incorrect enumeration. In its q=r case, each blade must initially be missing at most one leaf, and if the hub is blank it must be the first force and see all r-1 leaf colours. Relative to a proper completion the r-1 excluded patterns are exactly the patterns in which every blade omits the same colour. Counting relative to a completion does not duplicate seeds: every proper completion of a seed must agree with every forced step, by induction, so a successful seed has one completion. The repaired claim is restricted to r<q<=N. No leaf can be forced since its degree r-1 is less than q-1, so only total assignments or assignments blank solely at the hub can succeed. Proper total assignments have q choices for the hub and independent blade-wise injections. With a blank hub, precisely q-1 colours must appear on the leaves. Choosing the absent colour and applying inclusion–exclusion to unused colours gives the repaired z^(N-1) coefficient. It is positive throughout the claimed range: partition the q-1 available leaf colours into m groups of size at most r-1, then pad each blade with distinct colours. This is possible also at q=N, when every leaf must use a distinct colour. It proves the minimum and multiplicity. The stated probability model weights each monomial coefficient by p^k(1-qp)^(N-k), including the endpoints. Fresh enumeration of 139,868 initial states across eight cases, including both retained palette endpoints for W(3,2), matched the coefficient vectors and the probability transform at p=1/(2q). The repaired program separately compared union-size dynamic programming against inclusion–exclusion in 435 cases, also checking the factorial count at q=N and the vanishing coefficient at q=N+1.

## originality

PASS

This PASS applies only to the reassessed intermediate-palette claim r<q<=N. The frozen all-palette finding fails originality as stated: an earlier exact windmill result and an earlier broader bouquet result already cover its entire q=r seed enumerator, minimum, multiplicity and probability transform. The omitted q<r and q>N regimes are already consequences of Farr's general propositions. The necessary scientific repair is to remove all three regimes from the claimed contribution, retaining the nonzero hub-blank coefficient and its minimum-size consequences for the intermediate range. No earlier coverage of that narrower coefficient was established. A distinct later record gives the same larger-palette enumeration; it is equivalent coverage, not evidence of earlier priority.

## value

PASS

The retained coefficient evaluates, for an unbounded natural graph family, the entire contribution of successful incomplete seeds above the chromatic palette and at or below the largest palette permitting any local force. A minimum-size statement alone would not give the seed count or the probability of a final hub force; the exact colour-coverage coefficient gives both and replaces a search over all partial assignments. It isolates a genuine structural change from the prior chromatic-palette case, in which leaves can still be forced and fewer seeds suffice. Its significance is this precise intermediate regime, not the already known extreme regimes or the simplicity of the inclusion–exclusion method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
