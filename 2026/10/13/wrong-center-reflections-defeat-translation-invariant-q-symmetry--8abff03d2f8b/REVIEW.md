# Review: Wrong-center reflections defeat translation-invariant q-symmetry characterizations

## Correctness

PASS. The standard normal example satisfies the relevant support, positivity, differentiability, and finiteness assumptions. The exact identity
\[
X_{i:n}\overset{d}{=}-X_{n-i+1:n}
\]
implies
\[
q(X_{n-i+1:n})\overset{d}{=}1+X_{i:n}
\]
for \(q(x)=1-x\). Translation invariance then gives the Shannon identity and, at \(\alpha=2\), the Tsallis, Rényi, information-generating, and extropy identities. Yet \(q(X)\sim N(1,1)\), so prescribed q-symmetry fails.

The structural derivation is also exact: substituting \(u=1-F(x)\) into the source's quantile-density condition yields \(q'(x)=-f(x)/f(p(x))\), while differentiating \(p(x)=F^{-1}(1-F(x))\) yields the same derivative. Thus \(q=p+C\) on connected full support.

## Originality

PASS. The target 2026 full text was inspected at the q-symmetry definition, Lemma 3.1, Theorems 3.1--3.4 and 4.1, and the location-symmetry subsection. Searches using the exact title and DOI, fixed-center/reflection aliases, quantile-density aliases, translation invariance, and correction/corrigendum terms found no published correction or equivalent counterexample.

The closest literature located is the 2012 Rényi-entropy characterization and the 2019 multi-information-measure characterization of ordinary symmetry. Their accessible descriptions characterize symmetry without identifying a preassigned location center, so they do not dominate the present fixed-\(q\) obstruction.

Residual risk remains from a non-indexed note, a newly issued correction, or an equivalent observation expressed as location non-identifiability.

## Value

PASS. The source presents the information equalities as characterizations of a prescribed q-symmetry and explicitly motivates goodness-of-fit methodology from them. The counterexample shows that translation-invariant information measures cannot identify the prescribed reflection center and pinpoints the exact missing degree of freedom. This is a structural correction, not a parameter-specific numerical exception, and it indicates a minimal repair strategy: add an anchor that fixes the additive constant.

## Closest literature and limitations

The earlier symmetry-characterization papers support the center-free version of the idea and therefore clarify, rather than erase, the gap. The claim is intentionally limited to the fixed-\(q\) converse statements listed above and to the full-support additive-constant diagnosis. Weighted extropy and support-specific boundary repairs are not claimed.

Self-review: passed. Independent audit: not yet performed.
