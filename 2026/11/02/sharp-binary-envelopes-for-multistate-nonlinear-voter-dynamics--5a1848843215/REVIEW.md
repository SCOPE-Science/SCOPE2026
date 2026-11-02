# Scientific review — sharp binary envelopes for multistate nonlinear voter dynamics

## Correctness — PASS

The specified generator is the same rate convention as the main primary source, including the denominator \(N-1\). At a jointly vacant focal site the entering-\(A\) rates are monotone in the focal count. At a jointly occupied focal site the multistate departure rate is respectively bounded above or below by the binary departure rate, by strict power-sum super/subadditivity. This gives a consistent sitewise basic coupling despite the non-Markovian count projection. The binary birth/death ratios telescope to \(\binom{N-1}{r}^{q-1}\), which provides the exact fixation harmonic function. Dynkin's formula on the finite absorbing chain establishes the correction identity and its strictness criterion. Numerical and exact-rational finite-state checks, recorded in `VERIFICATION.md`, reproduce both inequality directions and the finite-time comparisons. Risks: no extension to arbitrary graphs or different update conventions is proved.

## Originality — PASS with residual priority risk

Ramirez et al., arXiv:2310.20548 (Sec. IV.1, Eq. (28)), give the same nonlumpable departure rate and do not assert a pathwise stochastic binary envelope, an all-size sharp fixation bound, its strictness criterion, or an exact stopped-generator correction. The 2012 linear multistate voter work treats \(q=1\), while the older binary nonlinear voter and noisy multistate variants cannot imply the nonlinearly competing-label statement as published. Searches for nonlinear voter multistate binary comparison, fixation under rival-opinion splitting, and pathwise coupling identified no stated equivalent. This is evidence of an unfilled comparison gap, not proof of global uniqueness. Remaining risk: general attractiveness arguments may have been applied to this precise process in specialist literature not retrieved.

## Mathematical value — PASS

The existing nonlinear model lacks a closed binary projection. The theorem nevertheless gives a finite-time sample-path comparison and an explicit binomial-sum bound on eventual focal victory, with complete equality and strictness conditions for every \(N\) and every real \(q>0\). The exact integral defect identifies how competitors' fragmentation quantitatively changes fixation. The result directly separates majority-reinforcing from minority-reinforcing imitation and bounds nonlumpable multistate dynamics by a solvable chain, rather than offering a numerical restatement or an arbitrary parameter slice.

Independent mathematical review of the proof and publication priority is still needed.

Self-review: passed. Independent audit: not yet performed.
