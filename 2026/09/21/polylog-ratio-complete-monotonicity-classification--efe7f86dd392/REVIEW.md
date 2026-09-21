# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The definitions were checked against Wei--Guo (2014): for \(i\ge1\),
\(f_i=g_i=\operatorname{Li}_{-i}(e^{-t})\), while the two \(i=0\) base
functions differ by \(1\). Hence the two ratio families coincide from index
\(1\) onward.

The low-index positive cases were re-derived explicitly. In particular,
\[
\mathcal F_2=\mathcal G_2
=\frac{1+4z+z^2}{1-z^2}
=1+4\sum_{k\ge0}z^{2k+1}+2\sum_{k\ge1}z^{2k},
\quad z=e^{-t},
\]
so the previously untreated index \(2\) is a positive discrete Laplace
transform.

The negative result was checked independently from the low-index expansion.
For \(i\ge1\),
\[
\mathcal F_i(t)=\frac{A_{i+1}(e^{-t})}
{(1-e^{-t})A_i(e^{-t})}.
\]
Classical Eulerian real-rootedness gives simple negative zeros; coefficient
symmetry makes \(A_i\) reciprocal. For every \(i\ge3\), this forces a zero
\(\rho_i\in(-1,0)\). The Eulerian differential recurrence shows
\[
A_{i+1}(\rho_i)=\rho_i(1-\rho_i)A_i'(\rho_i)\ne0,
\]
so the denominator zero is not canceled. It becomes a pole at
\(-\log|\rho_i|+i\pi\), strictly inside the right half-plane.

The analytic obstruction is valid: every completely monotone function on
\((0,\infty)\) is the Laplace transform of a nonnegative measure, and that
transform is holomorphic throughout \(\Re t>0\). On each compact set bounded
away from the imaginary axis, local uniform convergence follows by domination
with the transform at a smaller positive real argument. The identity theorem
then makes a genuine pole of the explicit meromorphic continuation impossible.

As a separate real-axis check, exact symbolic calculation confirms
\(\mathcal F_3^{(10)}(\log 500)<0\). Thus the first failed index is not merely
an artifact of complex continuation.

The logarithmic-complete-monotonicity corollary was also checked separately.
For \(i=1\), \(-(\log\mathcal F_1)'=2e^{-t}/(1-e^{-2t})\) is a positive
discrete Laplace transform. For \(i=2\), the logarithmic derivative inherits
a pole from the inner zero of \(A_3\), excluding complete monotonicity of that
derivative. Larger indices already fail ordinary complete monotonicity.

## Originality

PASS, to the best of our knowledge.

The 2014 primary source was inspected through its theorem and conjecture
statements. Theorem 3 proves only decreasing monotonicity of the ratio
families. Section 5 explicitly lists the initial completely monotone ratio
cases before Conjecture 12 asks for complete monotonicity at every index. The
source does not state the \(i=2\) positive expansion, the failure beginning at
\(i=3\), or an all-index classification.

Searches were performed using the exact title and DOI, “Conjecture 12,”
consecutive derivatives of \(1/(e^t-1)\), negative-integer polylogarithm
ratios, the explicit rational functions from Eulerian polynomials, and
complete-monotonicity plus Eulerian-root terminology. No located source stated
the classification
\[
i\in\{0,1,2\}
\]
or the right-half-plane Eulerian-pole obstruction.

Current-status checking also located later complete-monotonicity literature
that cites Wei--Guo and later work using the derivative-ratio monotonicity,
but no located statement resolves Conjecture 12. Chow (2022) supplies a modern
reference for the classical simple negative roots and interlacing of Eulerian
polynomials; those root facts themselves are prior art and are not part of the
originality claim.

The concrete residual risk is notation mismatch: a resolution could have
appeared as a theorem about ratios
\(\operatorname{Li}_{-(n+1)}(e^{-t})/\operatorname{Li}_{-n}(e^{-t})\), or
about rational functions of Eulerian polynomials, without citing the 2014
conjecture. No specific inaccessible paper located in this review gave
positive evidence of such coverage.

## Value

PASS.

The result completely settles an explicit 2014 conjecture rather than merely
adding another verified index. It identifies the exact threshold, includes
the nontrivial positive case \(i=2\), and explains the entire failure regime
\(i\ge3\) by one reusable analytic mechanism: denominator zeros inside the
unit disk become forbidden right-half-plane singularities of any putative
Laplace transform. The same mechanism also separates ordinary from
logarithmic complete monotonicity.

## Limitations

- The classification concerns the specific consecutive-derivative/polylogarithm
  ratios in Wei--Guo (2014); it does not classify general ratios with a larger
  index gap or other polylogarithm orders.
- The root-location and reciprocity facts for Eulerian polynomials and the
  Hausdorff--Bernstein--Widder theorem are classical ingredients, not new
  results.
- Originality is to the best of our knowledge; equivalent coverage under
  different Eulerian/polylogarithm notation remains a residual risk.
- Independent audit has not been performed.
