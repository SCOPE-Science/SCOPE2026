# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The leading finite-step theorem uses only quantitative facts proved in Proposition 2.4 of arXiv:2609.20674v1: preservation of the finite-step topology, b_n(t) comparable to (1+t)^(-1), and time-integrability of every endpoint except b_n. Monotonicity of characteristics turns integrability into t x(t)->0 for every inner endpoint. Substitution into the exact source endpoint equation then gives b_n'=-c_n b_n^2+o(b_n^2), hence c_n t b_n->1. The L1 top-hat limit is an immediate geometric consequence of the endpoint limits under y=c_n t theta, and the moment hierarchy follows by change of variables.

For one interval, the differentiated quantity tan(a)/tan(b)^2 has logarithmic derivative bounded by C(a+b^2), which is integrable by the source decay estimates. This proves a/b^2 has a finite strictly positive limit. Re-expanding the exact outer-edge equation then gives (1/b)'=c-2c cot(2pi/m)b+O(b^2), from which the logarithmic denominator correction follows by a standard asymptotic integration argument. A standalone symbolic/numerical artifact checks the differentiated identity, expansion, and representative asymptotic clocks.

Stress tests included m=4, where cot(2pi/m)=0 and the logarithmic correction vanishes, and general m>4, where the logarithmic coefficient is positive. The proof does not require the inner plateau heights to be equal and correctly selects only the outermost height c_n in the leading spatial scale.

## Originality

PASS, to the best of our knowledge, with a narrow claim boundary. The source paper itself proves only b_n(t) comparable to 1/t, L1 mass comparable to 1/t, and an unspecified polynomial separation a/b <= (1+t)^(-gamma) for a single interval. Searches of the source text found no occurrence of `rescal`, `self-similar`, or `top-hat`, and no statement of the exact coefficient c_n t b_n->1, the renormalized top-hat limit, the universal moment constants, the a/b^2 limit, or the cot(2pi/m) logarithmic correction.

Repository searches by source identifier, mathematical object, and synonymous asymptotic terminology found no prior SCOPE record covering this result. Recent repository changes were also checked before publication.

External searches included the exact source title and identifier; combinations of `scale-invariant Euler`, `step function`, `endpoint asymptotic`, `self-similar`, `renormalized profile`, `top-hat`, `1/t`, and `t^-2`; and the surrounding long-time literature. No matching source-specific statement was located.

The strongest prior-work risk is Elgindi–Murray–Said (Ann. Sci. Éc. Norm. Supér. 2025, DOI 10.24033/asens.2621), which gives the general regulated-data relaxation theory for this scale-invariant Euler system. Its journal summary/abstract was inspected, but the complete article body was not exhaustively checked here. Because the 2026 source paper presents Proposition 2.4 as the quantitative step-packet estimate it needs and states only comparability/integrability there, this is treated as residual rather than concrete prior-coverage evidence. Cao–Fan–Qin arXiv:2608.16755 concerns the distinct m=3 theory and is also not claimed to be superseded.

The novelty claim is therefore restricted to the source-specific sharpening for finite positive step packets: exact outer-edge coefficient, L1 renormalized top-hat limit and moment hierarchy, plus the single-step quadratic edge slaving and logarithmic denominator correction. General facts about monotone integrable functions, asymptotic integration, or transport equations are not claimed as new.

## Value

PASS. The source paper uses finite steps as the elementary packets in its dense-orbit mechanism. The result identifies their actual asymptotic normal form rather than only their decay order. The universal mass clock t||g||_1->1 and the complete rescaled top-hat profile give reusable quantitative information for packet interactions, while the single-step correction separates a universal geometric logarithm from initial-data-dependent constants.

## Limitations

The result concerns finite positive step packets in the m>=4 reduced sector. It does not cover the infinite stacks used in the dense-orbit construction, arbitrary L-infinity data, sign-changing sector data, or the m=3 kernel regime. Subleading logarithmic asymptotics are proved only for one interval. Numerical output is supporting evidence only and does not constitute independent validation.
