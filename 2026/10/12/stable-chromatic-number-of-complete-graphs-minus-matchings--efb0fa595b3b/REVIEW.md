# Independent mathematical audit

## correctness

PASS

For r>=1, an acyclic total-order orientation starts with the endpoints of a deleted edge; as they are nonadjacent, each vertex reaches at most n-1 vertices including itself. The reverse-order most-preferred unused-reachable-color algorithm with n-1 colors is proper and permits no envy arc against the orientation: an assumed backward envy arc would force a repeated reachable color, contradicting the earlier endpoint choice. Lower bound for r>=2: with q=n-2 colors, each proper color class has size at most 2 and every doubled class must be an absent edge; at least 2 distinct absent pairs must be doubled. On each absent pair impose opposite rankings of q colors. Two doubled classes of colors a != b then have adjacent members that mutually envy and form a 2-cycle. r=1 is forced by clique size n-1; r=0 complete graph has stable chi n; chi ordinary is n-r. Independently enumerated every proper (n-2)-coloring in 9 profiles 4<=n<=8, 2<=r<=floor(n/2): 11,888 colorings and each had the mutual-envy obstruction. The universal quantifiers follow from proof, not enumeration.

## originality

PASS

The new September 2026 graph-coloring-with-preferences paper supplies definitions, a general reachability upper bound and complete bipartite special case K4-M2. The full two-color-class obstruction for arbitrarily many absent disjoint pairs is a distinct theorem and is not in the accessible material. A related published Resultary result evaluates K_{2,3,3}, a different complete multipartite graph. Full 2026 arXiv text could not be obtained after open-access search; authorized Oxford retrieval reported VPN disconnected. No whole-document negative claim is drawn from its abstract.

## value

PASS

A sharp exact value on the full natural matching-deletion/cocktail-party family reveals an unbounded preference-stability versus ordinary-coloring gap and supplies an explicit obstruction/constructive sharp upper bound; this is independently useful for a recently defined graph parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
