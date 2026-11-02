# Scientific review: first-box trace spectrum

## Correctness — PASS

The six scalar symplectic column conditions are equivalent to the full standard-form identity, and the completion sets in the proof traverse each ternary integer matrix once. The 1,440 contributing first-column pairs have multiplicities distributed as \(512,128,416,128,96,128,32\) at completion counts \(8,9,12,14,18,21,27\); their weighted sum is exactly \(17{,}312\). A disjoint algebraic enumeration over four ternary \(2\times2\) blocks independently reproduces every integer-trace count. The two computations are complete searches of finite, explicitly bounded domains, not statistical evidence or inferences about larger boxes. Residual correctness risk: the arithmetic tables depend on faithfully replaying the short standalone program; no closed-form handwritten coefficient derivation is claimed.

## Originality — PASS, with residual priority risk

The primary full-text comparison is Wurzinger, arXiv:2610.29794v1, especially its introduction, definition of centered boxes, symplectic column conditions, and Section 5. Its uniform upper bound and asymptotic centered growth do not determine the integer count or trace spectrum at radius one. The known \(\operatorname{SL}_2(\mathbb Z)\) shell formula quoted there concerns rank one. OEIS A364771 counts symplectic groups over finite quotient rings, not bounded integral lifts. Targeted literature searches for the exact count and trace multiset found no dominating formula or table. An unpublished computation or unindexed earlier example is still possible; search absence is not a proof of uniqueness.

## Value — PASS

The centered radius-one box is the canonical first nonempty arithmetic ball for the first higher-rank symplectic lattice, not an arbitrary parameter slice. The full nine-coefficient trace distribution refines the scalar lattice-point count by a natural conjugacy-invariant statistic; it supplies a reproducible exact benchmark for higher-rank symplectic box counting and trace-stratified experiments. The completion-count histogram records additional structural information about primitive isotropic frames. The claim does not assert new asymptotics or major general theory, but an exact natural initial shell is useful independently of those goals.

## Closest literature and limits

Wurzinger, *Integer symplectic matrices in expanding boxes* (21 October 2026), arXiv:2610.29794v1; OEIS A364771, *Order of the symplectic group of 4 X 4 matrices over Z_n*. Neither inspected source supplies the exact integer first-box trace spectrum. The first establishes bounds/asymptotics; the second deals with modular groups. The finite census and associated verifier are self-contained. Priority remains subject to external verification.

Self-review: passed. Independent audit: not yet performed.
