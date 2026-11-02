# Scientific review

## Correctness: PASS

The endpoint is the matrix rational function \(R(hQ_n)\), with scalar coefficients independently matched to equation (3.2) of Bonaventura and Della Rocca at the L-stable parameter. The exact resolvent identity \(P=(1+\sqrt2)T^2-\sqrt2T\) and a geometric-series expansion of the cyclic resolvent establish the entry formula. Its bracket is strictly increasing with cyclic distance, making the common diagonal the only possible obstruction. The positivity test reduces to a scalar polynomial. Strict decrease in dimension supplies the four-versus-five boundary; an exact Bernstein certificate and a rational five-cycle witness prove the cutoff. Descartes' rule and endpoint derivative signs prove exactly one forbidden interval; a fixed-scaling limit proves both asymptotic laws. The standalone verifier passed 8,541 assertions, including exact surd and polynomial identities and independently inverted finite endpoint matrices. Finite computations are corroboration, not the proof of the quantified claims.

## Originality: PASS, with residual risks

The focal 2015 paper establishes the TR-BDF2 stability function and absolute-monotonicity radius, but not an exact per-cycle endpoint positivity domain, finite-dimensional immunity, a unique unsafe interval, or large-step reentrance. The 2012 Padé work is especially relevant because it studies positive discretization of cyclic chains, but it uses different rational maps and its examples do not determine the TR-BDF2 cycle formula. Other numerical positivity results for Crank–Nicolson, Radau IIA, SSP-SDIRK, and Gauss–Legendre are method-specific and do not imply the current theorem. Searches for direct wording and for equivalent rational-kernel or resolvent representations did not reveal an earlier matching theorem; searches alone do not certify novelty. Residual risks are overlooked specialized cyclic transfer-kernel literature and possible republication or unpublished derivations.

## Mathematical value: PASS

For a standard, practically used L-stable second-order integrator, the theorem gives a complete, exactly computable set of safe timesteps on an infinite family of finite-state transport models. The sharp minimal unsafe state count, the fact that one diagonal test controls all entries, the single bounded unsafe interval, and the linear asymptotic recovery scale expose operationally important phenomena not apparent from an absolute-monotonicity radius alone. The result is not offered as a theorem about all generators or internal stages; those boundaries are explicit.

## Checked literature and limits

Bonaventura and Della Rocca, arXiv:1510.04303v1 (2015), Sections 2–3, numerical-experiment discussion and Appendix; Zappavigna, Colaneri, Kirkland and Shorten (2012), *Essentially Negative News About Positive Systems*, especially the cyclic-chain model, the nilpotent-shift counterexample, and the Padé positivity section. Public searches additionally examined near-equivalent descriptions of TR-BDF2, positivity, cyclic generators and Markov endpoint matrices. The named papers were materially inspected in full-text form in the relevant sections, including original method equations and claims, not just abstracts.

The independent consistency checks in `verify.py` do not constitute an independent mathematical audit, and no independent validation is claimed. The scientific case is limited to the stated homogeneous directed cycles.

Self-review: passed. Independent audit: not yet performed.
