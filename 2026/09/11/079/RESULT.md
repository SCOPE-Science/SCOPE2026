# Raw Z/2 augmentation counts are not presentation-independent: a certified 4-versus-2 gap on two plat presentations of one m(7_2) Legendrian knot

## Context

Legendrian knots in standard contact R^3 carry classical invariants (smooth type,
Thurston-Bennequin number tb, rotation number r) and non-classical invariants derived
from the Chekanov-Eliashberg differential graded algebra (DGA): graded augmentations
over Z/2, augmentation-homotopy classes, linearized contact homology, and graded
rulings. The Ng-Sabloff correspondence proves raw augmentation numbers and ruling
data determine each other up to an explicit many-to-one factor, and that raw counts
change by powers of 2 under algebraic stabilization. The admitted target asked for a
bare 3-versus-1 graded-augmentation gap with distinct linearized ranks separating two
nine-Reeb-chord m(7_2) fronts at (tb,r)=(1,0). Target work blocked that exact ledger
and instead certified the structural obstruction: raw counts vary across presentations
of even a single Legendrian knot while all invariant quotients agree.

## Definitions

Work over Z/2 with basepoint variable specialized t=1. A Z-graded (0-graded)
augmentation is an algebra map epsilon from the Chekanov-Eliashberg DGA to Z/2 with
epsilon o d = 0, epsilon(1)=1, supported only on degree-0 Reeb-chord generators.
P1 is the Ng-atlas braid word [6,7,7,5,8,9,5,4,6,3,5,2,4,7,8,3,1,2,2,4,6,8]
(Leg('mK7_2.0'), 22 crossings). P2 is the plat word
[8,7,7,9,7,6,5,4,3,2,1,8,7,6,5,4,3,2,2,4,6,8] obtained from the atlas 9x9 grid
diagram X=[5,0,8,7,2,1,4,3,6], O=[8,7,6,1,0,3,2,5,4] via grid->tangle->plat
conversion. Each plat has 27 Reeb-chord generators a[1..27]. Gradings P1:
3,4,-4,4,-2,-1,-4,-3,-3,-2,-2,-2,-1,-1,0,-1,-1,0,0,0,0,0,1,1,1,1,1.
Gradings P2: -5,-4,4,-4,-4,-4,-3,-3,-2,-2,-1,-3,-3,-2,-2,-1,-1,0,0,0,0,0,1,1,1,1,1.
Hence degree-0 generators {15,18,19,20,21,22} (P1) versus {18,19,20,21,22} (P2);
degree-1 generators a[23..27] on both sides.

## Result

Both plats present the single Ng-atlas Legendrian knot mK7_2.0 with tb=1, r=0, one
component, identical smooth Jones type, identical 0-graded ruling polynomial {0:1},
identical ruling summary {0:{0:1},4:{2:1}}, one Z-graded augmentation-homotopy class
each, three 2-graded homotopy classes of size 16 each, and uniform linearized
homology {-4:1,1:1,4:1} on every augmentation. Both differentials satisfy d^2=0.
P1 admits exactly 4 Z-graded augmentations:
{19,20,21,22}, {18,19,20,21,22}, {15,19,20,21,22}, {15,18,19,20,21,22}.
P2 admits exactly 2: {19,20,21,22}, {18,19,20,21,22}.
Both admit exactly 48 two-graded augmentations. Consequently a bare
"exactly N graded augmentations" ledger, without fixing the presentation or passing
to a homotopy quotient or stabilization-normalized count, is ill-typed as a
Legendrian non-isotopy witness.

## Proof / evidence

Filter each degree-1 differential to degree-0 words. On both sides:
d(a23) keeps 1,(19): 1+e19=0 so e19=1; d(a24) keeps 1,(20,19): e20=1;
d(a25) keeps 1,(21,20): e21=1; d(a26) keeps 1,(22,21): e22=1;
d(a27) keeps lam,(22): consistent with lam=1, e22=1. All other degree-1 monomials
pass through nonzero-degree chords and are dropped. No surviving condition constrains
a15 or a18 (P1) or a18 (P2). Hence solution sets are {forced 19-22} times free
variables: 2^2=4 versus 2^1=2. The stdlib-only solver artifacts/indep_aug.py parses
the embedded differential texts (verified line-identical to DGA.print_differential())
and brute-forces all 2^6/2^5 assignments, reproducing the lists plus 48/48
two-graded counts with no library solver code. Library cross-checks confirm
augmentations(), aug_homotopy_classes(), ruling_invariant(), and lin_hom data above.
The mechanism is the standard degree-0 stabilization effect: one extra unconstrained
degree-0 generator doubles raw counts while the homotopy quotient absorbs it.

## Limitations

Z/2 coefficients with t=1 only; no integer or multi-basepoint lift. Same-Legendrian
status rests on deterministic grid->plat provenance plus identical classical, ruling,
homotopy and linearized data; no explicit Reidemeister-move sequence is exhibited.
Full 2^22-state Jones replay timed out in audit; smooth identity uses conversion
determinism plus trefoil-calibrated code review. The surrounding negative target
ledger (exhaustive simple-plat enumeration, tangle sampling) is context and was not
re-enumerated here.

## Reproducibility

python3 output/artifacts/indep_aug.py re-derives 4-vs-2 and 48/48 from embedded
differentials (stdlib only). output/artifacts/legendrian_lib_snapshot.py is the exact
engine (commit b1e6f60): Leg('mK7_2.0') and Leg((X,O)) reproduce braids, tb=1, rot=0,
check_d_squared, augmentations, homotopy classes, rulings, linearized homology.
output/artifacts/verify_jones.py holds the trefoil-calibrated Jones code.

## References

Y. Chekanov, Differential algebra of Legendrian links; Computable Legendrian
invariants. L. Ng and J. Sabloff, Correspondence between augmentations and rulings
(math/0503168). J. Etnyre and L. Ng, Legendrian contact homology in R^3
(1811.10966). W. Chongchitmate and L. Ng, Atlas of Legendrian knots (1010.3997);
Ng atlas site, atlas-standalone-0324.pdf, atlas-standalone-0626.pdf.
