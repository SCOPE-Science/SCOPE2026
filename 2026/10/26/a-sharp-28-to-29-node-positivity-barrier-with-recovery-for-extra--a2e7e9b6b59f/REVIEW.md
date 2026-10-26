# Self-review

## Correctness — PASS
The full projector decomposition reduces matrix positivity to an explicit cubic sign condition. The sign of every off-diagonal and diagonal entry is accounted for, the dimension-28 inequality covers a continuum of positive timesteps, and the dimension-29 witness together with Descartes' rule establishes both sharp roots for every larger order. The standalone exact checker verified the claimed identities and 21 complete matrix cases. No finite test is used as an infinite proof.

## Originality — PASS (qualified)
The 2008 Euler-extrapolation source fixes the method but not the complete-graph positivity classification. The closest published Richardson-positivity result gives the scalar sign frontier \(2+2\sqrt2\) and explicitly restricts its statement to scalar decay. The graph theorem is not a restatement: negative scalar amplification does not imply negative Markov matrix entries, and the new dimension boundary and recovered-positivity interval need the complete-graph projector and cubic analysis. Other publicly indexed positivity results treat different rational methods. Full indexing cannot be guaranteed; an equivalent specialized result could exist.

## Value — PASS
The sharp largest graph order allowing unrestricted step selection is a natural structural stability boundary for a common accuracy-acceleration construction. Recovery at large steps is surprising because scalar amplification remains negative in the stiff tail. The exact endpoint classification distinguishes graph-state positivity from stability and scalar positivity, relevant to numerical diffusion and probability preservation. This is an exact infinite-family classification rather than an isolated numerical example.

## Closest literature and limits
Constantinescu–Sandu, TR-08-13 (2008) and SIAM J. Sci. Comput. (2010), supply original extrapolation framework. The full accessible scientific result *Richardson acceleration creates a sharp positivity barrier for backward Euler* covers scalar decay, not matrix positivity. A 2008 PDF was inspected in its introduction and extrapolation section, including the Aitken–Neville construction, with additional document-wide searches for related graph/positivity vocabulary; unreviewed material and literature indexed under different names remain risks. The theorem covers unweighted complete graphs only.

Self-review: passed. Independent audit: not yet performed.
