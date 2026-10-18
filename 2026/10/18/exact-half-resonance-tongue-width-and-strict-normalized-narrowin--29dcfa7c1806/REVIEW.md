# Review: exact half-resonance Arnold tongue width

## Correctness — PASS
The proof is for the canonical real lift at \(0<K<1\), where the map is orientation preserving. A positively winding two-orbit gives the reversible midpoint/separation relations \(2d=K\cos m\cos d\) and \(\Omega-1/2=-K\sin m\sin d/(2\pi)\). The induced scalar width function has a unique interior maximum because its stationary equation \(Q(d)=K^2\) has \(Q'(d)>0\); boundary values vanish. The alternate normalized formula expresses \(4\pi W(K)/K^2\) as a maximum of a strictly \(K\)-decreasing sinc term with an interior maximizer, which proves global strict monotonicity. The order-six small-coupling expansion was reconstructed symbolically, and both width formulae and direct second-iterate roots were checked numerically. The symbolic and numerical checks are corroboration, not an infinite proof.

## Originality — PASS, with a recorded source-access risk
Schilder and Peckham's publicly available 2006 manuscript studies the equivalent sine circle map in full and computes tongues by numerical continuation; its section 4.1 does not derive the exact half-resonance root formula or normalized-width monotonicity. Duchet and coauthors' 2023 small-amplitude formula overlaps at leading order, not globally in coupling. Davie's directly relevant 1996 *width of Arnold tongues* article was available only through its bibliographic abstract; it could conceivably contain earlier equivalent q=2 results. The absent full text is a real priority risk and is not described as NOT_COVERING. Semantic result searches and the available archival claims gave no substantive matching implication, but no claim of independence or world-wide uniqueness follows.

## Mathematical value — PASS
The \(1:2\) tongue is the simplest genuinely quadratic mode-locking resonance of the classical circle map. Its exact all-coupling extent is a natural physical and dynamical invariant, while the strict decrease of \(W(K)/K^2\) quantifies finite-coupling suppression compared with the perturbative quadratic law. Both sides of the sharp envelope and its limiting attainment are proved. This is more informative than a numerical tongue plot or a routine low-order series calculation.

## Scope and remaining limitations
Only the classical sine circle diffeomorphism with \(0<K<1\), detuning period one, and one positive turn in two iterates are treated. No higher-resonance generalization, global attractor-stability classification, noise result, or critical coupling assertion is made. Priority uncertainty especially concerns the inaccessible complete Davie 1996 paper. The numerical replay uses SciPy.

Self-review: passed. Independent audit: not yet performed.
