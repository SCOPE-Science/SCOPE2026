# Scientific review: exact residue-class entropy bias

## Correctness — PASS

The stated Markov entropy is the stationary conditional Shannon entropy, with uniform stationary law because the skew tent map preserves Lebesgue measure. Every complete source cell maps affinely onto a length-\(L/s\) output interval, and its row-entropy contribution is a periodic function of the cell index of period \(s\). The only exceptional source cell, when present, crosses the turning point; both partial images share their terminal output coordinate, and the proof counts their **overlapping** bin masses without double-counting. This establishes the exact expression for \(NH_N\), hence the \(L\)-step additive recursion, the full finite-resolution formula, and the universal sharp error order. For the \((1,4)\) example, the exact symbolic difference is \((2/25)\log(32/27)\), so positivity is not a floating-point inference.

The standalone checker constructs the Markov matrix by inverse-branch intersections with exact rational arithmetic and independently tests 338 parameter-and-resolution triples; it returns `VERIFY_OK`. These finite tests complement, but do not replace, the all-integer proof. The claimed sign change and the scope of stationary within-cell resampling are checked in the original domain.

## Originality — PASS, with residual risk

The closest primary source is Yano, arXiv:1205.1848 (2012). Its Theorem 4.1 establishes the limiting entropy and its Section 5 evaluates that limit for rational skew tent maps. Yano's Equation (4.27) already supplies the per-complete-cell entropy calculation; that ingredient is explicitly credited. The material inspected does not state an **exact** \(L\)-periodic scaled error for every finite resolution, perform the crossing-cell overlap computation, or identify the exact above-limit residue classes in the \((1,4)\) family. The new statement is a quantitative finite-resolution strengthening, not a rebranding of Yano's limiting formula.

Related work on transfer-operator spectra for Markov coarse-graining (MacKernan–Nicolis, 1994) and deterministic finite-alphabet threshold coding concerns different invariants or processes. Query comparisons for finite-grid entropy, rational slopes, and modular oscillations identified no equivalent or dominating prior statement. These searches are not a proof of historical priority. A full text of all possible later work was not available; unindexed derivations remain a residual risk.

## Mathematical value — PASS

The motivating 2012 paper determines the zero-noise entropy, but finite-resolution data need not approach that limit uniformly from one side. The theorem gives the exact leading error **at every resolution** for a natural two-parameter rational skew tent family, a finite algorithm for every phase coefficient, optimal \(1/N\) convergence, and a concrete all-resolution sign reversal. The positive phase occurs on an infinite congruence class, rather than being an isolated numerical anomaly. These facts are relevant to finite-resolution entropy extrapolation and to understanding arithmetic resonance of coarse-graining grids. The result does not assert a general formula beyond rational breakpoints or interpret the resampled chain as a deterministic symbolic observation process.

Self-review: passed. Independent audit: not yet performed.
