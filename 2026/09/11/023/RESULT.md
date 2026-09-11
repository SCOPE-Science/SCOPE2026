# No single Hall isoclinism family of order-64 class-2 2-groups contains both SmallGroup(64,199) and the nine Bogomolov-positive stems

## Context

The admitted target asked for an epicenter-certified capability dichotomy
over "the full Hall isoclinism stem family of order-64 class-2 2-groups
containing SmallGroup(64,199) (the Bogomolov-positive family)", i.e. one
family containing both the anchor SmallGroup(64,199) and the nine
order-64 groups with nontrivial Bogomolov multiplier B0. Capability of
small 2-groups is a recognized boundary in Schur-multiplier, isoclinism
(Hall), and rationality-obstruction (Bogomolov/Noether) theory.

## Definitions

- SmallGroup(64,n): GAP SmallGroups library ID; order 64.
- Hall isoclinism family: equivalence class under Hall isoclinism
  (isomorphisms G/Z(G) -> H/Z(H) and G' -> H' compatible with commutators).
- B0(G): Bogomolov multiplier of finite group G (subgroup of Schur
  multiplier; trivial denoted B0 = 0 / [] in HAP).
- The nine Bogomolov-positive order-64 stems: SmallGroup(64,n) for
  n in {149,150,151,170,171,172,177,178,182}.

## Result

No single Hall isoclinism family F of order-64 class-2 2-groups contains
both SmallGroup(64,199) and the nine Bogomolov-positive stems. Hence the
target claim's definite description
("the ... family containing SmallGroup(64,199) (the Bogomolov-positive
family)") refers to nothing, and the claimed per-stem Z* table over such
an F cannot exist as stated.

## Proof / Evidence

Fact A (B0 is an isoclinism invariant, Moravec). The official HAP
documentation page "About HAP: The Bogomolov Multiplier" states:

> Theorem. If G is isoclinic to H then B0(G) is isomorphic to B0(H),

attributed to Primož Moravec, Amer. J. Math. 134 (2012), 1679–1704.
Consequence: a group with B0 = 0 is never isoclinic to a group with
B0 != 0.

Fact B (exhaustive B0 census at order 64, HAP docs). The same page
publishes the exhaustive loop over `AllSmallGroups(n)` for
n dividing 128 with output list `NonTrivial`. The order-64 entries are
exactly [64,149],[64,150],[64,151],[64,170],[64,171],[64,172],
[64,177],[64,178],[64,182] — nine groups. [64,199] is absent from the
nontrivial list while the loop covers all small groups of each order, so
B0(SmallGroup(64,199)) = 0 (trivial) and B0 != 0 on each of the nine.

Contradiction. Suppose one Hall family F contained SmallGroup(64,199)
together with the nine. Any two members of one family are isoclinic, so
by Fact A all members have pairwise isomorphic B0. But by Fact B the
anchor has B0 = 0 while each of the nine has B0 != 0 — contradiction.
Therefore no such F exists.

Version drift does not rescue the claim. B0 attaches to the isomorphism
type, not the label: relabelling permutes IDs but cannot move a
B0-trivial class into a B0-nontrivial isoclinism family. The Jena
cohomology catalogue fingerprints confirm the types (anchor 64gp199 =
Hall–Senior 106, 4 minimal generators, exponent 4, centre rank 2; the
nine IDs are the Hall–Senior block 225–233), used only as per-group
fingerprints, not family identifiers.

## Limitations

- Proves only the family-level impossibility; computes no Z*(G), decides
  no capability status, and maps no isoclinism classes.
- Relies on two published sources (HAP docs census output; Jena
  per-group pages) via live fetch rather than a local GAP run.
- Hall–Senior numbers used only as per-group fingerprints.

## Reproducibility

- `output/artifacts/fetch_evidence.py` (stdlib only) re-fetches the HAP
  page, asserts the Moravec theorem sentence and all nine order-64
  IDs present / [64,199] absent; re-fetches the Jena pages and asserts
  anchor HS106 and the nine-to-HS225–233 correspondence; fetches the
  Groupprops order-64 page for the isoclinic = Hall–Senior-family
  identification. Harvest log: `output/artifacts/fetch_evidence.log`.
- Key URLs:
  https://gap-packages.github.io/hap/www/SideLinks/About/aboutBogomolov.html
  https://users.fmi.uni-jena.de/~green/Coho_v3/64gps/64gp199.html
  (and 64gp{149,150,151,170,171,172,177,178,182}.html)
  https://groupprops.subwiki.org/wiki/Groups_of_order_64

## References

- Jezernik–Moravec, "Bogomolov multipliers of all groups of order 128" —
  B0 census context; proves isoclinic groups have isomorphic B0; no
  capability/epicenter table.
- Moravec, "Unramified Brauer groups of finite and infinite groups",
  Amer. J. Math. 134 (2012) — invariance theorem source.
- Groupprops, "Groups of order 64" — IDs/background; isoclinic groups =
  Hall–Senior families.
- Jena cohomology catalogue, groups of order 64 — per-group Hall–Senior
  fingerprints.
