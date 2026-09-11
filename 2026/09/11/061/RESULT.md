# Genus-zero refined floor-diagram ledger for Hirzebruch bidegree (3,4) on F0

## Context

Refined Block–Göttsche counts conjecturally interpolate complex, real (Welschinger),
and log/DT invariants. Hirzebruch surfaces are the natural testing ground where floor
diagrams make the refined count computable, yet explicit q-ledgers are published only
for scattered low bidegrees. Bidegree (3,4) on F0 = P1×P1 is the next unsurveyed case
large enough to exhibit nontrivial multi-floor interaction but small enough for a
complete hand-auditable census. General theory (Block–Göttsche 2016, Bousseau,
Cavalieri–Johnson–Markwig–Ranganathan, Itenberg–Mikhalkin, Brugallé–Jaramillo Puentes)
proves invariance and polynomiality for fixed cogenus but publishes no explicit (3,4)
q-polynomial or per-diagram table.

## Definitions

Surface S = Σ0 = P1×P1 (m = 0). Line bundle L = 3H + 4F, bidegree (L·F, L·H) = (3,4).
Newton polygon rectangle [0,4]×[0,3]. Arithmetic genus (3−1)(4−1) = 6, equal to the
number of interior lattice points. Genus 0 connected implies cogenus δ = 6.
dim|L| = (3+1)(4+1)−1 = 19; point conditions n = 19−6 = 13.
Chamber: vertically stretched configuration P with floor order f1 < f2 < f3.
Floor-diagram axioms are Block–Göttsche arXiv:1407.2901 §5, Σm case m = 0
(Defs 5.1/5.2/5.4, Thm 5.7): vertex set {1,2,3}; s = (s1,s2,s3), sum 4;
div(j) = out(j) − in(j) ≤ sj; tj = sj − div(j); refined multiplicity
mult(D;y) = ∏e [we]y² with [n]y = y^{(n−1)/2}+…+y^{−(n−1)/2};
marking number ν(D) = linear extensions of D̃ (Steps 1–4) with distinguishable added
vertices divided by ∏ sj! tj!; combinatorial refined Severi degree
N = ΣD mult(D;y) ν(D).

## Result

For the above data and chamber, the genus-0 connected refined floor-diagram sum
R(q) = ΣD mult(D;q) ν(D) over all 80 marked floor diagrams (chain A: 50,
fan-from-1 E: 15, fan-into-3 F: 15; cogenus 6) equals the symmetric ledger L(q)
with coefficients for exponents e = −6..6:

1, 16, 140, 868, 4222, 16396, 44258, 16396, 4222, 868, 140, 16, 1.

Hence L(1) = 87544 (per-pattern A 65208, E 11168, F 11168) is the recomputed
unrefined count and L(−1) = 18424 is its signed real (tropical Welschinger)
specialization. Total marking sum Σν = 26422. Rebuilding the census with shuffled
iteration order (same chamber datum) returns byte-identical L(q).
The full per-diagram table (s, weights, edges, div, t, mult_q, ν, LE) is archived
in ledger_conn.json (80 rows). Disconnected same-cogenus doubled-edge diagrams
(33 rows, L(1) = 10127) are enumerated separately and excluded from this claim.

## Proof / evidence

Scripted exhaustive census (enumerate.py): connected genus-0 on 3 vertices forces
exactly 2 edges forming a tree; undirected-tree classification gives exactly
patterns A/E/F. Loops over all compositions s of 4 and admissible weights
(a in [1,s1] etc., with div₂ ≤ s₂ for A; a+b ≤ s1 for E) are exhaustive upper
bounds, verified by independent rerun (113 total incl. disconnected; 80 connected).
Markings counted by subset-DP linear-extension counter with LE % (∏s!t!) = 0
asserted per row; no parallel edges in A/E/F so no extra edge symmetry.
Quantum weights [w]y² recomputed from definition; mult(D;1) = ∏w² rechecked.
verify.py checks: C1 exact symmetry L(q) = L(q⁻¹); C2/C3 unrefined recombination
L(1) = Σν·mult(1) = 87544; C4 shuffled-rerun byte-identical L(q) plus the
combinatorial-fixity argument (floor order is the only chamber datum entering
Def 5.4, so a within-chamber perturbation fixes the census; cf. Thm 5.7);
C5 minimal row A [4,0,0] weights (4,4) has ν = 1; C6 independent
recursive-backtracking recount agrees on a stratified 9-row sample.
calib.py: the same generic counter reproduces classical P1×P1 counts
N(1,1) = 1, N(2,1) = 1, N(2,2) = 12 with brute-force permutation cross-checks
(n ≤ 9). Auditor independently re-executed enumeration logic and confirmed the
80-count, the exact coefficient vector, L(1)/L(−1), and per-pattern splits.

## Limitations

Within-chamber invariance is established as combinatorial fixity of the
floor-ordered census plus a shuffled-rerun determinism check, not as an
independent geometric perturbation of P with a re-derived tropical curve count;
a move changing the floor order leaves the chamber and is not claimed invariant.
L(1) = 87544 is the recomputed floor-diagram sum at y = 1 calibrated against
classical (1,1)/(2,1)/(2,2) counts, not cross-checked against an independent
published closed-form (3,4) number (none found). L(−1) is the y = −1
specialization of the certified ledger (signed real rule); no separate
real-algebraic curve count is performed. No claims beyond F0, this chamber, or
descendant/relative invariants.

## Reproducibility

Stdlib-only Python 3. From output/artifacts/: python3 enumerate.py → ledger.json
(113 rows); ledger_conn.json holds the 80 connected rows used here;
python3 verify.py → ALL_CHECKS_PASS; python3 calib.py → CALIBRATION_PASS.

## References

- F. Block, L. Göttsche, Refined curve counting with tropical geometry,
  arXiv:1407.2901 (Compositio 152, 2016), §5.
- F. Block, q-Floor diagrams computing refined Severi degrees for plane curves.
- P. Bousseau, Refined floor diagrams from higher genera and lambda classes.
- R. Cavalieri, P. Johnson, H. Markwig, H. Ranganathan, Counting curves on
  Hirzebruch surfaces (arXiv:1706.05401).
- I. Itenberg, G. Mikhalkin, On Block–Göttsche multiplicities.
- E. Brugallé, H. Jaramillo Puentes, Polynomiality properties of tropical
  refined invariants.
