# Scientific review — logarithmic radial Bergman kernels

## Correctness — PASS

The monomial moment identity is an exact gamma integral, giving the kernel with the required normalization. The proof of zero-freeness is not a numerical root search: it constructs two absolutely convergent Bernstein integral representations whose individual integrands have strictly positive real part for every scalar product \(|u|<1\). Endpoint exponents \(p=1\) and \(p=2\) are explicit. For \(2<p<4\), the sign of the analytically continued eta value at \(-1\), established through the zeta functional equation, and continuity give an interior negative root. For \(p\ge4\), a rigorously decreasing alternating tail gives a universally negative evaluation; the inequality and exact rational value at \(p=4\) were independently checked. The union covers all real \(p>0\), with no gaps.

Risks considered: convergence of the Bernstein integrals at both endpoints; strictness of the right-half-plane statements; analyticity at \(u=0\); and the limiting-value interpretation at \(-1\). None requires assuming that finite numerical testing proves an infinite assertion.

## Originality — PASS, subject to independent historical review

Perälä's 2017 radial moment formula and constructions establish the appropriate background, but their hypotheses and theorems do not state this exact logarithmic-weight phase diagram. Yamamori's 2011 Proposition 1 explicitly covers the already-known **integer** polylogarithm zeros \(p\ge3\), which are not claimed as new. Zeytuncu's radial examples concern weights comparable with the unweighted norm, unlike the present exact logarithmic moment sequence. Blaschke's superficially close 2011/2012 logarithmic-weight paper analyzes asymptotic singularities for weights with \(\log(1/(1-|z|^2))\) factors; the weight here uses \(-\log|z|^2\) and the asserted global kernel-zero threshold is not that paper's conclusion. Hedenmalm's known log-subharmonic zero-free criterion implies part of the negative-weight-exponent range; the contribution beyond it is the full sharp real-exponent threshold and explicit right-half-plane certificate. Current searches of equivalent terminology, parameter reductions, and published mathematical results did not identify a result implying this full statement.

The serious residual risk is an earlier general theorem on fractional negative-order polylogarithm zeros from special-function or analytic-combinatorics literature. This independent-priority risk is disclosed; absence from searches is not a proof of originality.

## Mathematical value — PASS

The Lu Qi-Keng property is a structural kernel invariant. Logarithmic radial weights form a simple natural continuous family with **exact gamma moments**, not an arbitrarily selected finite slice. The theorem identifies the full, sharp real-parameter stability boundary and supplies a stronger analytic certificate on its zero-free side, while separating known integer cases from the noninteger transition. This provides a concrete boundary example for interpreting more general radial Bergman kernel zero criteria.

The result neither counts all zeros above threshold nor addresses general radial weights. Its claims and limitations are identical throughout RESULT.md, SLOGAN.txt, and the structured records.

Self-review: passed. Independent audit: not yet performed.
