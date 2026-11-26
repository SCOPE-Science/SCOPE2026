# Independent mathematical audit

## correctness

PASS

The u-dependent bump and uniform leakage each integrate to one in v because the bump is supported below sqrt(u). The cutoff has integral 3δ/4. The bump-height estimate H≤2 exp(4/3)<8 implies m(v)≤2H sqrt(δ)+δ<1/4 at δ=2^-14, so g=(1-m)/J is strictly positive, bounded, and integrates to one. Row and column integrals of c_* are both exactly one. For v in any compact interior interval the bump vanishes uniformly at sufficiently small u, which justifies all derivatives in the column integral; flatness of the cutoff at δ justifies pasting, and leakage guarantees strict positivity for u>0. On every fixed positive ray the mass is O(s^(3/2))+O(s²), so dividing by s gives zero; the Clayton limit follows by substitution into its exact CDF. At (t,sqrt(t)) all bump mass is included and the deficit from t is at most t exp(-1/t²), while Clayton's deficit is asymptotic to t^(1+θ/2)/θ for each fixed θ>0. This proves eventual strict reversal for each θ with one fixed c_*, not a θ-uniform threshold. For entropy the row bump contributes -log(u)/2+∫h log h, with the latter finite by boundedness and the convention 0 log 0=0. Convexity bounds both mixtures by the integrable row contributions, and z log z is bounded below. RESULT.md lines 17–70 suffice for these continuum claims. VERIFICATION.md and check.py were inspected, not executed; their listed quadratures and finite theta diagnostics do not establish exact normalization, positivity, or continuum inequalities.

## originality

PASS

Pass is for the conjunction of strict positivity, interior smoothness, finite information, and reversal against all Clayton parameters with the same density. Example 3 of Siburg–Strothmann already supplies the exact curved path and parameter scope with singular mass. The closest inspected smooth reversal has a different comparison family; the closest positive-density same-day construction cannot reverse this ordering. None of those actual statements supplies the regularity extension. This is a bounded evidence-based comparison, not priority certification.

## value

PASS

This closes a meaningful regularity loophole in a known negative implication: eliminating the singular component, requiring interior smoothness and positivity everywhere, and even limiting information do not restore a local order. The example captures a genuine boundary effect: bounded density near the corner would give O(t^(3/2)) rather than the nearly maximal mass t. The mechanism is not a tuned finite numerical case or a claim about smooth extension to the closed square.

The dated certificate retains the supplied scientific assessment, sources and limitations.
